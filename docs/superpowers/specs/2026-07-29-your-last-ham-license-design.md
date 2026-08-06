# Your Last Ham License — Design Spec

**Full title:** *Your Last Ham License: The Extra Course (2024–2028)*
**Repo:** `Atvriders/your-last-ham-license` (public), local dir `~/your-last-ham-license/`
**Type:** Educational nonfiction — the capstone course + exam prep for the US Amateur Extra class license
**Date:** 2026-07-29
**Status:** Draft — awaiting human sign-off before implementation planning.

This is **the capstone of the series** (following *Your First Ham License* — Technician, and *Your Next Ham License* — General). It reuses the series' production machinery and method end to end: toolchain, canon discipline, pool-fidelity audit, series-site machinery, multi-agent workflow. The series arc completes: First → Next → Last.

> **Series note:** mounted at `/extra/` on the series site; the book-switcher bar shows Extra highlighted, Technician and General live. Shipping this book activates `/extra/` and completes the three-book series site.

---

## 1. Purpose & audience

A single-volume **capstone course** that takes a **General-class ham** to a passed **Amateur Extra exam (Element 4, 2024–2028 pool)**. The reader is an experienced operator with Book 3's theory under their belt — this is the deepest book in the series, at full technical-enthusiast depth: real math, real circuits, real propagation physics.

Two jobs at once, same method as the series:
- **Teaches** the advanced craft: complex impedance and phase, advanced filters and DSP/SDR, transmission lines and matching networks, the Smith chart properly, exotic propagation, EME/satellite/weak-signal operating.
- **Prepares for the exam**: after each chapter, the reader can answer every question in the mapped pool subelement(s). Element 4 is the hardest exam: **50 questions drawn from a pool of ~600+, 37 to pass** — the margin for half-learning is gone.

**Spine (organizing idea):** *mastery* — the last license class asks you to stop pattern-matching and start understanding: the same physics as the first two books, now all the way down.

**Non-goals:** not a beginner book (Book 2), not the intermediate ramp (Book 3), not an engineering textbook (stays exam-aligned, pool-first).

**Tone:** peer-to-peer with an experienced ham; dense but clear; every formula derived just enough to be believed, then drilled with the pool's own numbers.

## 2. Relationship to Books 2–3 (what we reuse)

| Reused | Retargeted to Book 4 |
|---|---|
| Full toolchain (books 2/3 share it, incl. markdown-table support, h4, speak_math formula tokens) | Copied; constants retargeted (title, chapters, ID3, GHCR image, `/extra/` series highlight, localStorage key `ylhl-audio`) |
| Canon discipline + pool-fidelity audit (check #8) | Same law; canon carries the **2024–2028 Extra pool verbatim** (E-question IDs, E1–E0 sort, 50-question exam structure) |
| Chapter skeleton & Exam Focus method | Same format laws (only ch00 exempt) |
| Audiobook (8 voices, chapters only) + player w/ auto-play-next | Same; new capstone intro |
| `make_exam.py` | Retargeted: **Extra exam = 50 questions, 37 to pass**, one per group per NCVEC structure |
| Series site | Extra highlighted; all three live — series complete |

**Depth change:** full technical-enthusiast level — complex numbers as everyday tools, phasors, the Smith chart in full (it IS pool-relevant here, unlike General), filter synthesis concepts, DSP/SDR internals, antenna modeling concepts.

## 3. Source materials

- **NCVEC Element 4, 2024–2028 Amateur Extra pool** (public domain) — subelements **E1–E0**; question count/group structure verified at ingestion (expected ~600+ questions, ~50 groups; exam = **50 Q, one per group, 37 to pass**). Valid **2024-07-01 → 2028-06-30**. Any errata incorporated with the revision record pinned. Any pool figures (the Extra pool historically ships several schematics/diagrams, incl. Smith-chart and filter figures) redrawn as original SVGs.
- Source: ncvec.org (exact page located at ingestion; errata cross-checked).
- **FCC Part 97** (public domain) — §97.301/§97.305 Extra-only segments, §97.307 emission standards, §97.311/313.
- **Owned references:** ARRL Handbooks 1927–1983 (depth; reproduction only from the 7 PD editions).
- **Books 2–3** — series foundation; notation/voice consistent; the Extra course references earlier chapters without re-teaching.
- Research workflow as before: pool ingestion → parallel researchers (Part 97 Extra privileges; per-subelement teaching notes E1–E5 / E6–E0; advanced operating color: EME, weak-signal, contest/DX at depth) → assembler writes `accuracy-canon.md` with zero UNVERIFIED.

## 4. Chapter outline (11 chapters + 2 appendices, ~50–65k words, ~30–40 figures)

One subelement per chapter, series-consistent (exact split finalized after pool ingestion):

| # | Chapter (working titles) | Pool subelement(s) | Teaches |
|---|---|---|---|
| 00 | **The last license: why Extra, and how this book works** | — | What Extra opens (the Extra-only HF segments, full privileges); the 50-question exam; how the series fits together. ~2.5–3k |
| 01 | **The rules at full depth** | E1 | Extra-only band segments exact; emission standards; special operations (automatic control, remote bases, auxiliary); CEPT/international. |
| 02 | **Operating at the edge: satellites, EME, weak signal** | E2 | Satellite orbits/keps, EME path loss basics, weak-signal VHF+, contest/DX at depth, net/digital operations. |
| 03 | **Propagation: the exotic paths** | E3 | Auroral propagation, meteor scatter, transequatorial (TE), sporadic-E at depth, ducting, solar-terrestrial indices properly. |
| 04 | **Amateur practices & test equipment** | E4 | Measurement theory (accuracy/resolution), oscilloscopes, spectrum analyzers, SWR/impedance analyzers, noise sources, receiver performance (dynamic range, IMD). |
| 05 | **Electrical principles at full depth** | E5 | Complex impedance (rectangular/polar), phase relationships, Q in depth, time constants, resonance in depth, impedance matching theory. |
| 06 | **Circuit components at full depth** | E6 | Semiconductor physics (junctions, FET/MOSFET), displays, digital logic families, counters/registers, ADC/DAC. |
| 07 | **Practical circuits at full depth** | E7 | Active filters, PLLs, DSP/SDR (sampling, aliasing, FFT, I/Q), power supply design, amplifier design at depth. |
| 08 | **Signals & emissions at full depth** | E8 | AC waveform analysis, modulation at depth (QAM, OFDM concepts), digital protocols (FT8 internals, PSK, spread spectrum), emission measurement. |
| 09 | **Antennas & transmission lines at full depth** | E9 | The Smith chart in full (normalized impedance, constant-SWR circles, matching solutions), transmission-line transformations (λ/4, λ/2, stubs), antenna modeling concepts, pattern/gain/efficiency at depth. |
| 10 | **Safety at full depth** | E0 | RF exposure math (MPE calculations, averaging, duty factors at depth), grounding/bonding at depth, tower/antenna safety at depth. |
| A | **Appendix A: the complete 2024–2028 Extra pool** | all | Every question verbatim + one-line why naming the teaching chapter. Print-only. |
| B | **Appendix B: glossary & formulas** | — | Glossary from canon; the Extra formula set with micro-examples. |

**Exam-prep integration:** identical to the series — Exam Focus per chapter (5–10 verbatim questions + whys); Appendix A complete annotated pool; audit check #8 enforces byte-exact quotes and answer keys.

## 5. Per-chapter anatomy (format laws)

Identical skeleton to the series (audit-enforced): exact heading; opener; teaching `###` sections; figures via `{{fig:id}}`; ≥1 `> **Worked example:**` (real calculations — complex impedance, Smith-chart values, MPE math); `> **The math, if you want it:**` sidebars for derivations; `### Exam Focus`; `### Key Takeaways`; 3–5 `**FACT:**` lines verbatim from the canon; banned phrases; no fabricated quotations. ch00 keeps the checklist adaptation (no pool).

## 6. The accuracy canon

Same law: canonical pool files (`canon/pool-extra.txt` + `.json` with sha256s), pinned FACTs with sources, notation & units (series standard), glossary (series-consistent), subelement→chapter map, copyright ledger (carried over), resolved uncertainties (zero open), time-sensitive register (pool expiry 2028-06-30; fees re-verified at build).

## 7. Copyright discipline

Identical rules: prose original; Part 97 + NCVEC pool public domain; pool figures redrawn as original SVGs; archival Handbook material only from the 7 PD editions, tagged; `figreg` enforces.

## 8. Production architecture

Identical to Books 2–3: Phase A (this spec → sign-off → task plan) → Phase B (scaffold copy from the General repo — newest toolchain — retarget constants incl. the 50-question exam structure in make_exam.py and any E-specific audit constants) → Phase C1 (pool ingestion + canon) → Phase C2 (figures, incl. pool-figure redraws + the Smith-chart figure family) → Phase C3 (chapters + appendix + span auditors) → Phase D (front matter) → Phase E (verify, one commit, repo via REST API, push, audiobook, release v1.0, CI→GHCR public, **series-site completion: Extra live everywhere** — the Technician and General repos' series bars/landing pages flip Extra live as their own tiny commits, human-approved at that moment).

## 9. Deliverables

Same as the series: self-contained HTML/PDF/TXT; `make_exam.py` (50-question Extra exams); 8-voice audiobook (chapters only) on release v1.0; Docker image `ghcr.io/atvriders/your-last-ham-license:latest`; series-site completion (`/extra/` live); `AI-CONTEXT.md`; README with honest stats block and pool-currency notice (valid → 2028-06-30).

## 10. Verification

Same gates: pytest green; `audit_book.py` exit 0 (8 checks incl. pool fidelity); real build; figure eyeballing (pool-figure redraws vs official side-by-side); human-style spot-read; then ship.

## 11. Open items / risks

- **Depth control at the top end:** E5/E7/E9 invite textbook drift. Mitigation: pool-first discipline — nothing taught beyond what the pool tests plus one sidebar; span auditors grade "peer-level but exam-aligned" per chapter.
- **Smith-chart figures:** the hardest figures in the series (constant-resistance/reactance circles must be geometrically correct). Mitigation: a dedicated figure agent with matplotlib-generated chart grids + side-by-side review against pool figures.
- **Pool size (~600+):** Appendix A is the largest yet (~45k+ words verbatim) — the fragment→assemble pipeline handles it; ingestion verification is even more load-bearing.
- **Series completion touches three repos at ship:** the Extra-flip commits in the Tech/General repos are separate tiny commits, each human-approved at that moment (per the standing rule, not assumed).
