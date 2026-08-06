# Your Last Ham License

*The Extra Course (2024–2028) · from General to the top of the license ladder · 113,805 words*

> You already hold the General license — the Extra exam is 50 questions drawn
> one per group from a public 599-question pool, and 37 correct answers opens
> everything the FCC grants an amateur: the Extra-only slices of five HF bands,
> every operating privilege, the top of the license ladder. This book teaches
> the deep radio behind the questions — then hands you the questions.

A complete capstone course for the US Amateur Extra class amateur radio license
(Element 4, 2024–2028 NCVEC question pool), written for the licensed General: it
assumes the General course's knowledge — no more, no less — and goes all the way
down: complex impedance and phasors, DSP/SDR internals, transmission lines and the
Smith chart properly, exotic propagation, and satellite, EME, and weak-signal
operating. Eleven chapters walk from what the upgrade opens through the rules at
Extra depth, operating beyond the General bands, propagation beyond the ordinary,
the workbench of instruments and receivers, electrical principles, components,
practical circuits, signals and emissions, antennas and transmission lines at
Extra depth, and RF exposure and safety — and every teaching chapter ends with an
**Exam Focus** section quoting the exact pool questions that chapter unlocks,
verbatim, with the keyed answer and a one-line plain-language why. It is **Book 4
— the capstone — of the three-book program** begun with *[200 Meters and
Down](https://github.com/Atvriders/200-meters-and-down)*, *[Your First Ham
License](https://github.com/Atvriders/your-first-ham-license)* (the Technician
course), and *[Your Next Ham
License](https://github.com/Atvriders/your-next-ham-license)* (the General
course). First → Next → Last: the series is complete.

## What's inside

- **11 chapters** (~53,500 words) — a real capstone course, not a cram sheet: each
  concept is taught plainly first, then tied to the pool questions it answers.
  This is the deepest book in the series — real math, real circuits, real
  propagation physics, every formula derived just enough to be believed and then
  drilled with the pool's own numbers.
- **The exam-focus method** — every one of the **599 active pool questions** is
  answerable after its mapped chapter; the chapter map (canon §5) is the contract,
  and a mechanical audit verifies every quoted question and answer letter against
  the official pool.
- **Appendix A: the complete 2024–2028 pool** — all 599 active questions verbatim
  (the four withdrawn questions simply do not appear, exactly as the official
  document omits them), choices A–D, correct answer marked, one-line why naming
  the chapter that teaches it.
- **Appendix B: glossary & formulas** — 502 terms in plain language plus the
  book's complete formula set (42 formulas, each with a worked example from the
  pool's own numbers).
- **39 original figures**, including all ten of the pool's official graphics
  redrawn as clean, themeable SVGs — among them the E9-3 Smith chart in its
  corrected post-errata orientation (infinity on the right).
- **A practice-exam generator** and an **8-voice audiobook** — see below.

## Formats

| File | What it is |
|---|---|
| [`build/index.html`](build/index.html) | The book, typeset as a single self-contained page — linked table of contents, light/dark themes, 39 figures and all math embedded inline. Open it in any browser; it works fully offline. The nicest way to read it. |
| [`build/your-last-ham-license.pdf`](build/your-last-ham-license.pdf) | PDF edition — open in any PDF reader. |
| [`build/your-last-ham-license.txt`](build/your-last-ham-license.txt) | Plain-text edition — open in any editor; math spoken as words, figures as placeholders. |
| [`chapters/`](chapters/) | The 11 source chapters as Markdown (`ch00.md` … `ch10.md`). |
| [`appendices/`](appendices/) | Appendix A ([the complete annotated pool](appendices/pool.md)) and Appendix B ([glossary & formulas](appendices/glossary-and-formulas.md)). |
| Audiobook (release v1.0) | Eight voices, each reading all 11 chapters, plus a spoken introduction — see below. |
| [`Dockerfile`](Dockerfile) / [`docker-compose.yml`](docker-compose.yml) | Serve the book yourself — see below. |

## Read online via Docker

The image packages the book and the audiobook behind nginx, built and pushed to
`ghcr.io/atvriders/your-last-ham-license` by CI on every push to `master`. On any
Docker host:

```sh
docker compose pull && docker compose up -d
```

Serves the book at [http://localhost:8080](http://localhost:8080) and the
audiobook player at `/audiobook/`.

To build locally instead: regenerate the typeset editions, fetch the audiobook
from the release (it is not stored in git), then build the image:

```sh
python3 tools/build_book.py --html --txt --pdf --out build/
# fetch audiobook/ from release v1.0 (see .github/workflows/build.yml for the exact loop), then:
docker build -t ghcr.io/atvriders/your-last-ham-license:latest .
```

## The series site — now complete

This book is the third and last of three to ship (Technician, General, Extra) —
**all three books are now live**. The repo carries the machinery for the whole
series behind one nginx proxy:

```sh
docker compose -f series-docker-compose.yml up -d
```

Serves everything at [http://localhost:8080](http://localhost:8080): a landing
page at `/` with a card per book, the Technician book (text + audiobook) at
`/tech/`, the General book at `/general/`, and this book at `/extra/` — with the
book-switcher bar at the top of every page linking all three, the current book
highlighted, and no "coming soon" labels left anywhere. Config lives in
[`series/`](series/) (proxy + landing page) and
[`series-docker-compose.yml`](series-docker-compose.yml). This book's ship also
flips Extra live in the Technician and General repos' own series bars and landing
pages — two tiny commits, each human-approved at ship time.

## Audiobook

The audiobook comes in **eight voices** — men and women in **American, British,
Australian, and Irish** accents — each reading all eleven chapters, synthesized
with [edge-tts](https://pypi.org/project/edge-tts/) via
[`tools/make_audiobook.py`](tools/make_audiobook.py) (`--voice <key>` for one
voice, `--all` for every voice) plus a spoken introduction via
[`tools/make_intro.py`](tools/make_intro.py). Formulas and figures are narrated in
words, not read as raw markup. The verbatim pool appendix is print-only and is not
narrated.

All audio is hosted on **release v1.0** rather than committed to git. The player
lives at **`/audiobook/`** in the container: a themed page with continuous
chapter-to-chapter playback, a **voice switcher** grouped by accent, a live
visualizer, **resume** (it remembers your voice, chapter, and position between
visits), and an **Auto-play next chapter toggle** — on by default; switch it off
and playback stops at the end of each chapter.

## Practice-exam generator

Draw a valid practice exam from the pool — exactly one question per NCVEC group,
**50 questions, 37 correct to pass**, just like the real thing:

```sh
python3 tools/make_exam.py            # random draw
python3 tools/make_exam.py --seed 7   # reproducible draw
```

Writes `build/practice-exam.md` (questions and choices A–D, never the answers —
print it and circle) and `build/practice-exam-key.md` (the answer key with a
subelement tally). Pass `--out` to write elsewhere.

## Pool currency — this pool expires 2028-06-30

**This book tracks the NCVEC 2024–2028 Extra question pool, valid for exams
2024-07-01 through 2028-06-30 — after that date, exams use the successor pool.**
The book incorporates all four errata issued for this pool (through the 4th,
2026-02-04; four questions withdrawn across the four). The next Extra pool takes
effect 2028-07-01; check [ncvec.org](https://ncvec.org/) from late 2027 for the
successor pool. The pool is public domain and is carried verbatim in
[`canon/pool-extra.txt`](canon/pool-extra.txt) (byte-exact) and
[`canon/pool-extra.json`](canon/pool-extra.json) (structured), with sha256 hashes
and full provenance in [`accuracy-canon.md`](accuracy-canon.md) §1.

When an errata issues — or when the 2028–2032 pool arrives — the swap is contained
by design, because only the pool-facing artifacts change with the pool:

1. Ingest the new pool into `canon/` (new canonical files, sha256s, errata ledger,
   deleted-ID list, ingestion report) and update the canon's revision record.
2. Re-run `python3 tools/audit_book.py` — check #8 mechanically flags every
   chapter/appendix quote and answer letter that drifted, and any coverage gap.
3. Refresh the affected quotes (script-assisted, never retyped), the chapters'
   Exam Focus picks, and Appendix A against the new files; update any FACT lines
   the canon change invalidates.
4. Rebuild. Nothing else changes — notation, glossary, chapter map, teaching
   prose, and figures stand.

Any printing of this book after mid-2028 must state which pool exams actually
use. Fees and other time-sensitive values carry verification dates and re-verify
triggers in the canon (§7.11).

## Development

```sh
python3 -m pytest -q                              # 107 tooling tests
python3 tools/audit_book.py                       # the 8-check accuracy/format/pool gate (exit 0 = green)
python3 tools/build_book.py --html --txt --pdf --out build/   # rebuild the editions
```

The audit is the gate: figure integrity, copyright tags, TOC/anchors, math
rendering, canon cross-check of every `**FACT:**` line, no unresolved uncertainty
markers, format laws, and pool fidelity (every quoted question byte-exact, every
answer letter matching the key, all 599 active questions in Appendix A exactly
once).

## For AI models

[`AI-CONTEXT.md`](AI-CONTEXT.md) is a complete machine-oriented context dump — the
accuracy-canon discipline, pool record (four-errata ledger, four deleted IDs, the
ten figure redraw specs), chapter/subelement map, format laws, pool-fidelity
rules, figure pipeline, tooling, series machinery, copyright ledger, resolved
uncertainties (including the 60 m rule change and the /AE upgrade wording law),
time-sensitive register, and production history — sufficient to understand,
extend, or adapt the book without contradicting it.

## How it was made

Built by a **multi-agent workflow** over `accuracy-canon.md` — a bible-as-law
accuracy canon carrying the entire 599-question pool verbatim (double-parsed from
the official .docx and .pdf and cross-checked to zero disagreement beyond the two
published figure-ID typos, with the four-errata ledger and the four withdrawn
questions cataloged), pinned Part 97 facts, notation, glossary, the chapter map,
and the copyright ledger — reusing the production machinery of its sibling
projects, *[200 Meters and
Down](https://github.com/Atvriders/200-meters-and-down)*, *[Your First Ham
License](https://github.com/Atvriders/your-first-ham-license)*, and *[Your Next
Ham License](https://github.com/Atvriders/your-next-ham-license)*.

| | |
|---|---|
| **Sections** | 13 (11 chapters + 2 appendices) |
| **Words** | 113,805 (53,537 chapters · 47,998 annotated pool · 12,270 glossary & formulas) |
| **Figures** | 39 (all original — hand-authored themeable SVG + matplotlib-plotted curves; all ten NCVEC pool figures redrawn, never copied, including the E9-3 Smith chart in its rotated post-errata form) |
| **Pool questions annotated** | 599/599 — every active question verbatim, answer keyed, one-line why (four errata incorporated, four withdrawals omitted) |
| **Agents** | ~50 subagent launches across tooling, canon, figures, chapters, appendix, and audit phases (estimate), plus retries after transient engine errors |
| **Tooling tests** | 107 pytest tests |
| **Audit checks** | 8, including mechanical verbatim-pool verification: 599/599 questions in Appendix A, every quote byte-exact, every answer key matching the pool |
| **Calendar build span** | 2026-07-29 → 2026-07-31, with parallel agents throughout |
| **Subagent tokens** | **~5.8M subagent tokens** (estimate — modeled from agent reads + written volume at ~4 chars/token; this runtime does not meter subagent tokens) |
