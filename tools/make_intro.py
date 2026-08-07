"""Synthesize the audiobook introduction with edge-tts, in all eight voices.

A short spoken preface that opens the audiobook: a welcome to the
experienced General upgrading to Extra — the last license class, what Extra
opens (the Extra-only HF segments and full amateur privileges), what Your
Last Ham License is, that it was written by Kimi K3 running in
Kimi Code, a word on how it was made (the multi-agent workflow and its
estimated token cost), and how to use the eight-voice edition. Kept separate
from the chapter tracks so it can be regenerated on its own.

Like the chapters, the default voice (Ryan) writes ``intro.mp3`` and every
other voice writes ``<voice>-intro.mp3``, so the player's voice switcher can
treat the intro as a normal track.

Usage:
  python tools/make_intro.py                  # every voice: intro.mp3 + <voice>-intro.mp3
  python tools/make_intro.py --voice sonia    # one voice only
  python tools/make_intro.py --dry            # print the intro text and exit (no synth, no network)

Requires: edge-tts (pip install edge-tts) and ffmpeg on PATH.
Resumable: a voice whose MP3 already exists (> 100 KB) is skipped unless
--force is given. Edit INTRO and rerun to change the narration.
"""

import argparse
import asyncio
import subprocess
import sys
from pathlib import Path

import edge_tts

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.make_audiobook import DEFAULT_VOICE, VOICES
from tools.make_audiobook import dest_name as section_dest_name

OUT_DIR = Path(__file__).resolve().parent.parent / "audiobook"
INTRO_SECTION = "intro"
RETRIES = 5
CONCURRENCY = 3

INTRO = """Your Last Ham License: The Extra Course, 2024 to 2028. A welcome to the top of the ladder.

This audiobook was written by Kimi K3 — an artificial intelligence made by Moonshot AI — running inside the coding tool Kimi Code.

You already hold your General license. You know your way around HF, you know the bands where contacts cross oceans — and you have probably noticed the segments your ticket does not quite reach. This course is your last upgrade: in eleven chapters it takes you from General to Amateur Extra, the highest license class the FCC grants. The Extra-only segments of the HF bands, operating at the edge — satellites, moonbounce, weak signal — the exotic propagation paths, complex impedance and the Smith chart, and safety math at full depth. Every fact and every practice question is checked against the official twenty twenty-four to twenty twenty-eight Extra question pool, so what you hear is what the exam asks.

This book completes the series that began with Your First Ham License and continued with Your Next Ham License: three courses, from your first contact to every privilege the service offers.

It exists to carry an experienced General all the way to a passed Extra exam, and it was built by a multi-agent AI workflow: an accuracy canon as law, every fact audited against it, and all five hundred ninety-nine pool questions checked mechanically, verbatim, answer keys included. All told, the build consumed an estimated five point eight million subagent tokens.

This edition is offered in eight voices — American, British, Australian, and Irish, male and female.

And now — Your Last Ham License. Your final upgrade begins whenever you are ready."""


def dest_name(voice_key: str) -> str:
    """Intro MP3 name for a voice, same scheme as the chapter tracks:
    ``intro.mp3`` for the default voice, ``<voice>-intro.mp3`` otherwise."""
    return section_dest_name(voice_key, INTRO_SECTION)


async def synth(voice_key: str, sem: asyncio.Semaphore, force: bool) -> str:
    voice, label, accent, gender = VOICES[voice_key]
    dest = OUT_DIR / dest_name(voice_key)
    if not force and dest.exists() and dest.stat().st_size > 100_000:
        return f"skip  {dest.name} (exists)"
    async with sem:
        raw = dest.with_suffix(".raw.mp3")
        last = None
        for attempt in range(1, RETRIES + 1):
            try:
                await edge_tts.Communicate(INTRO, voice).save(str(raw))
                if raw.stat().st_size > 500:
                    break
                raise RuntimeError("empty audio")
            except Exception as e:  # noqa: BLE001 - retry any transport error
                last = e
                await asyncio.sleep(min(2 * attempt, 12))
        else:
            raise RuntimeError(f"synthesis failed after {RETRIES} tries: {last}")

        await asyncio.to_thread(subprocess.run, [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
            "-c", "copy",
            "-metadata", "title=Introduction",
            "-metadata", "artist=Kimi K3",
            "-metadata", "album=Your Last Ham License",
            "-metadata", "track=0/11",
            "-metadata", "genre=Audiobook",
            "-metadata", "date=2026",
            "-metadata", f"composer={label}",
            "-metadata", f"comment=Read by {label} ({accent} {gender})",
            str(dest),
        ], check=True)
        raw.unlink(missing_ok=True)
    return f"done  {dest.name} ({dest.stat().st_size/1e6:.1f} MB) — {label}"


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", choices=list(VOICES), default=None,
                    help="build one voice only (default: all eight)")
    ap.add_argument("--force", action="store_true", help="rebuild existing files")
    ap.add_argument("--dry", action="store_true",
                    help="print the intro text and exit (no synth, no network)")
    args = ap.parse_args()

    if args.dry:
        print(INTRO)
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    keys = [args.voice] if args.voice else list(VOICES)
    sem = asyncio.Semaphore(CONCURRENCY)
    results = await asyncio.gather(
        *(synth(k, sem, args.force) for k in keys), return_exceptions=True)
    lines, failed = [], []
    for k, r in zip(keys, results):
        if isinstance(r, Exception):
            failed.append(f"{k}: {r}")
        else:
            lines.append(r)
    for line in lines:
        print(line, flush=True)
    if failed:
        print("FAILED:\n" + "\n".join(failed), flush=True)
        sys.exit(1)
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
