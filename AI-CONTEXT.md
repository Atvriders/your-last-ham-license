# AI-CONTEXT — Your Last Ham License: The Extra Course (2024–2028)

This document is a complete, machine-oriented context dump for AI models (and humans)
working with this repository. It contains everything needed to understand, extend,
adapt, or continue *Your Last Ham License: The Extra Course (2024–2028)* without
contradicting the finished book: what the book is and who it is for, the accuracy-canon
discipline, the pool record, the chapter/subelement map, the format laws, the
pool-fidelity rules, the figure pipeline, the tooling, the series-site machinery, the
copyright ledger, the resolved uncertainties, the time-sensitive register, how to
extend the series, and the production history. Treat **`accuracy-canon.md`** (plus its
companion canonical pool files under `canon/`) as law — the published chapters already
conform to it exactly, and this file only summarizes it.

Credentials, API tokens, and personal contact details from the production session are
deliberately omitted.

---

## 1. What this is

*Your Last Ham License: The Extra Course (2024–2028)* is a **113,805-word** capstone
course + exam-prep book for the **US Amateur Extra class amateur radio license
(Element 4, 2024–2028 NCVEC question pool)**: **53,537 words across 11 chapters**
(ch00–ch10: 3,066 / 5,623 / 4,972 / 4,065 / 4,971 / 5,142 / 5,604 / 6,062 / 4,567 /
6,082 / 3,383) plus **2 appendices** (Appendix A, the complete annotated pool, 47,998
words; Appendix B, glossary & formulas, 12,270 words — 502 terms + 42 formulas), with
**39 original figures** (ten of them redrawn from the NCVEC pool's ten graphics,
including the E9-3 Smith chart).

The audience is the **licensed General** upgrading to Amateur Extra — a reader who
already has Book 3's theory under their belt: real AC theory, HF operating, practical
circuits at General depth. The book assumes Book 3's knowledge, **no more, no less**:
concepts beyond General scope are taught before use; General-scope material gets at
most a one-line refresher and a pointer to Book 3. The book does two jobs at once:
teaches the advanced craft the Extra ticket crowns (complex impedance and phasors,
DSP/SDR internals, transmission lines and the Smith chart properly, exotic
propagation, satellite/EME/weak-signal operating), and prepares for the exam — after
reading a chapter, the reader can answer every question in its mapped pool subelement.
Element 4 is the hardest exam: **50 questions drawn one per group from a 599-question
pool, 37 correct to pass** — the margin for half-learning is gone. Spine: *mastery* —
the last license class asks you to stop pattern-matching and start understanding: the
same physics as the first two books, now all the way down.

This is **Book 4 of the three-book "Your First Ham License" program — the capstone**,
following Book 1 (*200 Meters and Down*, a technical history of amateur radio — not
exam prep), Book 2 (*Your First Ham License: The Technician Course (2026–2030)*), and
Book 3 (*Your Next Ham License: The General Course (2023–2027)*). The series arc
completes: First → Next → Last. Production machinery (build, audit, figures,
audiobook, Docker, series site) is inherited from Book 3 and retargeted; new here are
the `make_exam.py` 50-question/37-to-pass parameterization, the E-ID letter class
widened to A–H (E7/E9 groups reach H), the `mathsvg`/`speak_math` extension for the
Extra formula set (complex impedance, Γ, τ, ω, ∠), ten pool-figure redraws with
side-by-side geometric verification, the largest Appendix A in the series, and the
series-site completion (all three books live, Extra current).

## 2. The accuracy canon is LAW

**`accuracy-canon.md`** is the single, binding source of truth for every pool wording,
number, date, notation choice, glossary definition, chapter mapping, and copyright
determination in the book. Where a draft ever disagreed with the canon, the canon won.
**Prose is always original** — facts, 47 CFR Part 97, and the NCVEC pool are public
domain and free to quote; everything else is written fresh.

What the canon pins down (read the file before adding or changing any fact):

- **§1 Pool record** — the canonical pool files and their provenance (§3 below), the
  four-errata ledger, the deleted-ID list, and **§1.4, the binding component-by-
  component redraw specification for each of the ten pool figures**, with the
  question→position maps that the owning chapters' Exam Focus blocks obey.
- **§2 Pinned facts with sources** — the fact reservoir. Each line is
  `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers
  copy the sentence **verbatim** (minus the trailing source tag) into their chapters;
  the build audit greps every chapter `**FACT:**` line for an exact match in this file
  (check #5). Rule quotations are verbatim from the **eCFR current text of 47 CFR
  Part 97, issue date 2026-07-28** (byte-identical to 2026-07-20; pool-era comparisons
  against the 2024-07-01 issue), pulled 2026-07-30. Where current rule text differs
  from the pool-era text the 2023 pool was written against, the FACT pins the
  **current** text and §7.1/§7.2 carry the difference — the hazard areas are 60 m and
  the post-pool amendments, both resolved (§10 below).
- **§3 Notation & Units** — one symbol set (V, I, R, P, Q, f, λ, c, C, L, X, Z, j, ∠,
  Y, G, B, τ, ω, Γ, SWR, N). Prose uses **V** for voltage and **×** for
  multiplication, exactly as Books 2 and 3 do. **New to the series at Extra depth
  (binding):** complex-number conventions — impedance rectangular (Z = R ± jX; +j
  inductive, −j capacitive) or polar (|Z| ∠θ, degrees always); the **j-operator** (the
  engineering j, never the mathematician's i); admittance Y = G + jB in siemens; Γ and
  the SWR family. The pool prints complex impedances in ASCII j-form with a hyphen
  minus ("0 - j100") — prose writes 0 − j100 with the house minus and Ω, and verbatim
  pool quotes always keep the pool's own typography byte-exact. Unit case is
  load-bearing (kHz, MHz, mA, µV, pF). The pool's own shortcut **λ(m) = 300 / f(MHz)**
  is taught as an approximation of c = f·λ, never an exact identity. dB =
  10·log₁₀(P₂/P₁) is first-class exam math (as in Book 3); Extra additions stated
  openly: **dBm**, and 20·log₁₀ for amplitude ratios (return loss).
- **§4 Glossary** — canonical one-line definitions (**502 terms** feed Appendix B).
  Series law: where a term also appears in Book 3's canon, the definition is Book 3's
  **verbatim** (which kept Book 2's); terms new to the Extra course carry new
  definitions in the same style. A chapter may expand a term but must not contradict
  it.
- **§5 Subelement → chapter map** — the ownership contract (§4 below).
- **§6 Copyright ledger** — (§9 below).
- **§7 Resolved uncertainties** — every research flag closed to a sourced value or a
  deliberately careful wording (12 subsections; highlights in §10 of this file). **No
  open uncertainty markers remain**; the audit greps for `UNVERIFIED` (check #6).

## 3. The pool record (canon §1)

The 2024–2028 Extra pool is carried as **canonical files — the only quoting
sources**:

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-extra.txt` | 175,707 | `a03fb3c8b4a8401a196057c34199bd1d355931170c1fef9625fbdd9421f48d0e` |
| `canon/pool-extra.json` | 267,486 | `6fdf1cae68793c94dd2965dfac02a4e614e0ee2d825009ef4cd76fe06a8bfa50` |

The `.txt` is the byte-exact human-readable rendering (ID lines `E1A01 (D) [97.305,
97.307(b)]`, `~~` separators, published headings with their **plain hyphens** — unlike
the General pool's en dashes, preserved not normalized — the `#`-comment provenance
header, and the published tail lines); the `.json` is the structured form (`{id:
{group, subelement, question, choices{A–D}, answer, figure}}`). Question text,
choices, and answer letters are quoted from these two files **only** — never from
memory, web mirrors, or study guides.

Key facts:

- **599 active questions** (603 published IDs minus 4 withdrawn), 10 subelements
  (E1–E9, E0), **50 groups**; every question has exactly 4 choices A–D and one keyed
  answer (letters A×150, B×150, C×150, D×149). Group letters run to **H** (E7 A–H, E9
  A–H). **The exam: 50 questions, one drawn from each group; 37 correct to pass** (47
  CFR §97.503(c)). Print "**37 of 50**" — the rule pins a count, not a percentage;
  "74%" is derived arithmetic and is flagged as such wherever it appears (§10.3
  below).
- **Valid for exams 2024-07-01 through 2028-06-30. THIS POOL EXPIRES MID-2028.** The
  successor Extra pool takes effect 2028-07-01 (four-year rotation: Technician
  2026–2030, General 2023–2027, Extra 2024–2028; no pools updated in 2025 or 2029).
  Every printing, chapter, exam product, and web page derived from this book states
  the 2024–2028 validity window; the contained-swap procedure is pinned in canon §7.11
  (§11 below).
- **Public domain:** released as such by the NCVEC Question Pool Committee (stated
  twice on the release page, captured in `canon/source/release-page.html`, fetched
  2026-07-30). Initial release **2023-12-07** (603 questions); the current document is
  the **4th-errata release of 2026-02-04**, whose pool body already incorporates every
  change.
- **Four-errata ledger** (from the document's front-matter errata sheets,
  cross-checked against the release page): **Errata 1 (2024-01-31)** — **diagram E9-3
  (the Smith chart) rotated 90°** to the conventional horizontal orientation, infinity
  on the right; 5 questions modified (E1D07 wording, E1F03 answer D replaced, E4D12
  and E4D13 "100 W"→"10 W", E6A06 answer B gains "The change in"); citation-only fixes
  E1E10 → `[97.509(m)]`, E1E11 → `[97.509(i)]`; **E9E10 withdrawn** (E9E not
  renumbered, 10 remain). **2nd errata (2024-11-08)** — **E2A13 withdrawn** (E2A not
  renumbered, 12 remain). **3rd errata (2025-09-24 release page / sheet dated
  2025-09-25)** — **E6D07 withdrawn** ("more than one correct answer"; E6D not
  renumbered, 11 remain). **4th errata (2026-02-04)** — **E4D05 withdrawn** (E4D not
  renumbered, 13 remain). All five published text modifications and both citation
  fixes (errata 1) were verified present in the final pool text byte-exactly during
  ingestion. **No 5th errata exists as of 2026-07-30.**
- **The four deleted IDs: E9E10, E2A13, E6D07, E4D05.** Withdrawn **without
  renumbering** (each printed in the source as `EnX## Question Deleted (section not
  renumbered)`; E9E10's placeholder carries a double space — placeholders are not
  carried into the canonical files). Three leave an interior numbering gap; **E2A13
  leaves none** (it was the last question of E2A, which now ends at E2A12). The
  canonical files carry the active pool only; **deleted questions are never quoted,
  taught, or referenced as exam content anywhere in the book** — they appear only as
  numbering gaps and in this ledger.
- **Syllabus reconciliation:** the printed syllabus claims E2:61, E4:64, E9:94 (sum
  602); the parse-authoritative counts are **60, 63, 93** — the printed numbers are
  stale (not updated for the 2nd/4th/1st errata withdrawals). The parse, not the
  syllabus, is authoritative.
- **Provenance:** downloaded 2026-07-30 from ncvec.org into `canon/source/` (sha256s
  in canon §1.2, including the 3rd-errata release kept as the pre-4th baseline — it
  differs from the 4th only by the removal of E4D05, zero content differences among
  the 599 common questions, all 60 heading lines identical). Parsed from the `.docx`
  (authoritative; python3 `zipfile` + `ElementTree`, no third-party packages) and
  independently re-parsed from the `.pdf` with `pdftotext -layout`; the two agreed on
  all 599 questions, all 2,396 choices, all answer letters, all Part 97 refs, and all
  60 headings, with exactly 12 field differences — ten PDF-side hyphen-wrap artifacts
  plus one PDF-side heading wrap (docx authoritative) and **two genuine content
  differences**: the published figure-ID typos `Figure E73` (E7G07) and `Figure E92`
  (E9B04), which the PDF hyphenates; the canonical files carry the typo forms
  byte-exactly. ARRL hosts no separate copy of this pool, so the docx-vs-pdf double
  parse is the cross-check of record. Full evidence in `canon/ingestion-report.md`.
- **Published quirks are preserved, never repaired** (full list in §7.1 below): the 66
  E1 Part-97 ID-line tags in their published form (including E1A06's superseded
  `[97.303(h)(1)]` and the errata-1-corrected `[97.509(m)]`/`[97.509(i)]`); the three
  figure-stem typos; the E5C on/in variance; the E8B04 interior double space; E2D04's
  double space after the choice-D label; E1C10 choice A's `- 43 dB` interior space;
  the E0 banner casing quirk (`SUBELEMENT E0 - SAFETY - [1 exam question - 1 group]`);
  published Unicode punctuation byte-exactly (curly apostrophe U+2019 ×60, curly
  quotes U+201C/U+201D ×16 each — the only non-ASCII characters in the pool text). The
  only whitespace normalization applied anywhere is paragraph-edge stripping: E1C12's
  entire block carried a leading double tab in the .docx, and 20 pool-body paragraphs
  carried a single trailing space — edges, never content.
- **The ten pool figures (28 questions):** the Extra pool ships ten graphics — E5-1,
  E6-1, E6-2, E6-3, E7-1, E7-2, E7-3, E9-1, E9-2, E9-3 — all obtained in three
  independent forms (the figures PDF, three JPG diagram pages — **page 3 is the "V2"
  re-issue incorporating the 1st-errata Smith-chart rotation** — and
  `e4_2024-svgs.zip`, all ten as verified well-formed SVG). **E9-3 is confirmed in its
  post-errata form**: conventional horizontal orientation, **infinity on the right**,
  0 on the left. The book **redraws every figure as an original SVG conveying exactly
  the official content — same components, same labels, same numbered positions — never
  copies the published graphic** (§6 below). Canon §1.4 carries the binding redraw
  specifications, one per figure, with the question→position maps:
  - **E5-1** (3 questions: E5C10–E5C12 → ch05) — a rectangular-coordinate **impedance
    graph, not a circuit** (§10.4): square frame, ±600 Ω both axes, eight labeled
    points; keyed points P4/P3/P1.
  - **E6-1** (2: E6A10, E6A11 → ch06) — six FET symbols; the three discriminators
    (JFET vs MOSFET, arrow direction, dual-gate) resolve every option mechanically.
  - **E6-2** (1: E6B10 → ch06) — eight diode symbols; the Schottky (6) is the keyed
    one; its tell is the squared S-hooks at both cathode-bar ends.
  - **E6-3** (3: E6C08, E6C10, E6C11 → ch06) — six logic gates; the 2×2 matrix
    (D-shape = AND family, curved-input = OR family, bubble = negation, triangle pair).
  - **E7-1** (3: E7B10–E7B12 → ch07) — NPN amplifier stage: voltage-divider bias,
    self bias (R3; "emitter bypass" names C3's job — the classic misread), common
    emitter.
  - **E7-2** (3: E7D06–E7D08 → ch07) — linear voltage regulator: series-pass Q1, C2
    bypasses ripple around the Zener reference; its numbers drive E7D13's dissipation
    math ((25 − 12) V × 1 A = 13 W).
  - **E7-3** (5: E7G02, E7G07, E7G09–E7G11 → ch07) — inverting op-amp; one formula
    (Av = −RF/R1) answers five questions — the best return-on-formula in the pool.
  - **E9-1** (3: E9B01–E9B03 → ch09) — azimuth pattern, "Free-Space Pattern": 50°
    beamwidth, 18 dB front-to-back, 14 dB front-to-side.
  - **E9-2** (3: E9B04–E9B06 → ch09) — elevation pattern, "Over Real Ground": 28 dB
    front-to-back, peak at 7.5° elevation; stem prints "Figure E92" (typo, preserved).
  - **E9-3** (2: E9G06, E9G07 → ch09) — the Smith chart, post-errata orientation (∞
    right, 0 left); the outer circle is the reactance axis, the single straight line
    the resistance axis; **wavelength scales are absent in the published figure — do
    not invent them.**

## 4. Chapter / subelement map (canon §5)

One subelement per chapter, E1→ch01 … E0→ch10, with ch00 the capstone upgrade
welcome. Every one of the 599 pool questions is answerable after its mapped chapter; a
chapter teaches its subelement, and only that chapter quotes those questions in its
Exam Focus. Exam weight (one question per group) is the stakes: E6–E0 supply 30 of the
50 exam seats (E7+E9 alone are 16), and every group is guaranteed exactly one seat on
every exam, so no group may be skipped.

| Chapter | Title | Pool subelement | Groups owned | Pool questions | Exam questions |
|---|---|---|---|---:|---:|
| ch00 | The Last Upgrade: Why Extra, and How This Book Works | — (upgrade logistics, canon §2.6) | — | — | — |
| ch01 | The Rules at Extra Depth | E1 | E1A–E1F | 68 | 6 |
| ch02 | Operating beyond the General Bands: Satellites, TV, Digital, DX | E2 | E2A–E2E | 60 | 5 |
| ch03 | Propagation beyond the Ordinary | E3 | E3A–E3C | 39 | 3 |
| ch04 | The Workbench: Instruments, Receivers, Interference | E4 | E4A–E4E | 63 | 5 |
| ch05 | Electrical Principles: Complex Impedance and Resonance | E5 | E5A–E5D | 49 | 4 |
| ch06 | Components and Devices at Extra Depth | E6 | E6A–E6F | 68 | 6 |
| ch07 | Practical Circuits | E7 | E7A–E7H | 99 | 8 |
| ch08 | Signals and Emissions at Extra Depth | E8 | E8A–E8D | 48 | 4 |
| ch09 | Antennas and Transmission Lines at Extra Depth | E9 | E9A–E9H | 93 | 8 |
| ch10 | RF Exposure and Safety at Extra Depth | E0 | E0A | 12 | 1 |
| Appendix A | The Complete 2024–2028 Amateur Extra Question Pool | all 599 verbatim + one-line why | all 50 | 599 | 50 |
| Appendix B | Glossary & Formulas | — (canon §3, §4) | — | — | — |

Binding notes:

- **ch00 teaches no pool questions** — it covers the capstone upgrade logistics of
  canon §2.6 (Element 4 structure 50/37, CSCE, §97.9(b) immediacy with the /AE
  indicator, fees and the upgrade exemption, what Extra opens, CEPT as a real Extra
  benefit, series completion) and carries the checklist adaptation of the format laws
  (no Exam Focus; the audit enforces this — **only ch00 is exempt**, and ch10 is a
  full teaching chapter because E0 is a real subelement).
- **The ten pool figures live in their owning chapters** (§3 above): E5-1 → ch05;
  E6-1/E6-2/E6-3 → ch06; E7-1/E7-2/E7-3 → ch07; E9-1/E9-2/E9-3 → ch09. The 28 figure
  questions appear in those chapters' Exam Focus blocks with the binding
  question→position maps of canon §1.4.
- **The three interior numbering gaps are taught, not hidden:** ch04 notes E4D05's
  withdrawal (errata 4), ch06 notes E6D07's (errata 3), ch09 notes E9E10's (errata 1),
  and ch02 notes E2A ended at E2A12 (errata 2) — one sentence each; deleted questions
  are never quoted.
- **ch10 treats RF exposure and tower/grounding safety as the pool's single group
  demands** — E0A mixes MPE rules (Part 1 territory, §10.5) with climbing practice; no
  MPE computation is required by any question, and the power-density illustration is
  flagged as enrichment (its numeric pin is §10.8 below).
- **ch05 carries the heaviest math flag in the book:** the E5 formula family is exam
  math, and the three Figure E5-1 plotting questions are taught as a *plotting* skill
  — E5-1 is a chart, not a circuit (§10.4).

## 5. Format laws

### 5.1 Chapter skeleton (audit check #7)

Every teaching chapter (ch01–ch10) follows one fixed skeleton so parallel writers
produce one coherent book:

1. First line exactly `## <N>. <Title>`.
2. **Opener** — one short plain-language paragraph (a concrete capstone scenario plus
   "in this chapter you'll learn …").
3. **Teaching sections** (`### …`) — plain language, figures as `{{fig:id}}` on their
   own line, inline math `$…$` only where needed; optional
   `> **The math, if you want it:**` sidebars for derivations.
4. **≥1 `> **Worked example:**` blockquote** — **a real calculation worked end to end
   with pool-relevant numbers** (complex impedance, Smith-chart values, MPE math, link
   budgets); arithmetic-only is a defect at this level.
5. **`### Exam Focus`** — opens with the coverage line (subelement, groups, question
   counts, exam weight), then 5–10 verbatim pool questions with correct answer and a
   one-line plain-language why (quote format in §5.4).
6. **`### Key Takeaways`** — 4–8 bullets.
7. **3–5 `**FACT:** <sentence>` lines** as standalone plain paragraphs (never inside
   blockquotes — the audit's FACT regex won't see them there), copied **byte-exact**
   from `accuracy-canon.md`.

**Only ch00 is exempt** from the Exam Focus / worked-example rules — it gets the "Your
upgrade checklist" adaptation. Banned phrases everywhere: *"little did they know"*,
*"in that moment"*, *"a testament to"*. Nonfiction integrity: no fabricated
quotations; anecdotes are plainly framed as illustrative scenarios, never attributed
to real people. Depth law (span-auditor enforced): assumes Book 3 knowledge — no more,
no less; peer-level with an experienced General, exam-aligned — nothing taught beyond
what the pool tests plus one sidebar; **E5/E7/E9 are the textbook-drift risk
chapters**.

### 5.2 Appendix A format (audit check #8 parses this exactly)

All 599 active questions, exactly once each, in canonical pool order (subelements
E1…E9 then E0; group A→last; ascending number, **skipping the four deletions** — the
audit's `pool_sort_key`, subelement 0 sorting as 10). One `###` section per subelement
with the published title and counts; optional `####` group lines. Every entry is one
blockquote in exactly this shape, followed by one plain line carrying the published ID
line:

```
> **E1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: D** — <one-line why, naming the teaching chapter: "… — taught in chapter 1.">

Published ID line: `E1A01 (D) [97.305, 97.307(b)]`
```

The published ID line rides on a **separate plain-text line after the blockquote, in
backticks** — never inside the quote itself (the audit would read it as part of the
question text). The ID lines preserve the published citation forms verbatim (the 66 E1
tags, including the stale `[97.303(h)(1)]` and the errata-1 `[97.509(m)]` /
`[97.509(i)]`); the 533 non-E1 questions are published as bare `E2A01 (D)`. Redrawn
pool figures are embedded on the line before their first referencing quote and named
thereafter. The appendix was assembled from **per-subelement fragments**
(`appendices/pool-fragments/E1.md` … `E0.md`) concatenated in canonical order; every
quote was **script-extracted** from the canonical files, never hand-typed. Appendix A
is **print-only — never narrated** in the audiobook (series decision).

### 5.3 Appendix B format

Glossary as a **two-column pipe table** (502 terms, the canon's §4 definitions
verbatim) — which **renders as a real HTML table** via the builder's pipe-table
support — then the formula set: **42 formulas** (the Extra set — reactance, resonance
and Q in depth, time constants, complex impedance rectangular↔polar, admittance,
real vs reactive power, Γ/SWR/return loss, noise floor vs bandwidth, dBm↔watts, link
budget and margin, ERP/EIRP and dBi/dBd, op-amp gain, series-regulator dissipation,
ADC resolution and Nyquist, modulation index and deviation ratio, CW/FSK bandwidths,
transmission-line length and the Q-section, plus the series carry-overs such as Ohm's
law, the wavelength shortcut, and the prefix ladder), each with a plain statement and
one worked example using the pool's own numbers, plus a notation-and-units subsection
(V/× prose convention, the pinned complex-number conventions, unit case, c, f = 1/T,
the hobby's customary units). The S = ERP/(4πR²) micro-example is flagged **enrichment
only** — no E0A question requires it — and carries the §10.8 units.

### 5.4 Build-dialect constraints (what `tools/build_book.py` actually parses)

The builder parses a small fixed markdown dialect; writers must stay inside it:

- **Consecutive non-blank lines join into one paragraph.** Therefore bullets (Key
  Takeaways, checklists) are **blank-line-separated** — each `-` item stands alone
  between blank lines, or the parser would merge them into a single paragraph.
- **A blockquote is consecutive `>` lines joined with spaces.** The six-line Exam
  Focus / Appendix A quote block works because of this; any `>` line directly adjacent
  to it would be absorbed into the same block. Blockquote classes: a quote starting
  `**The math, if you want it:**` renders as a sidebar; `**Worked example:**` as a
  worked example; anything else as a plain quote.
- **Inline math is `$…$`, rendered to SVG at build time** (`tools/mathsvg.py`). Keep
  it to **at most one `$…$` span per paragraph** and never use a literal `$` (e.g.
  "$35") inside a math paragraph — write "35 dollars" in prose. The renderer's subset
  was **extended for this book** beyond Book 3's (subscripts, π, √, fractions) to
  cover the Extra formula set: Greek letters ($\Gamma$, $\tau$, $\omega$, $\phi$),
  $\angle$, magnitude bars, and the complex-impedance forms.
- **Pipe tables are supported:** consecutive `| … |` lines whose second line is a
  `|---|`-style separator parse as a table and render as a real
  `<table class="md-table">`; lines that fail the separator test fall back to the old
  join-into-paragraph behavior. This exists so Appendix B's 502-row glossary renders
  as a table.
- Figures are `{{fig:id}}` on their own line, resolved against `figures/figures.json`;
  `***` is a section rule; `####` headings render as anchored `<h4>`s (Appendix A
  group headings) and never enter the TOC; emphasis is `**bold**` / `*italic*`.
- The audit's Exam Focus quote regex (`> **E#X##** <text>` + `**Answer: L**`, letter
  class A–H) is the exact contract for every pool quote in chapters and appendices.

## 6. Figures

**39 original figures** (`figures/figures.json` is the registry — a dict keyed by
figure id; `figures/*.svg` the assets — one SVG per registry entry). Distribution:
ch00:2, ch01:2, ch02:3, ch03:4, ch04:3, ch05:5, ch06:4, ch07:6, ch08:3, ch09:6,
ch10:1.

- **Hand-authored themeable SVG schematics/diagrams** using `currentColor` so they
  render correctly in both light and dark themes — e.g. `ch00-what-extra-opens.svg`,
  `ch02-linear-transponder.svg`, `ch07-sdr-iq.svg`, `ch09-phased-array.svg`.
- **Matplotlib-plotted curves**, generated by paired `_gen_<id>.py` scripts, committed
  as static SVG and **post-processed black → `currentColor`** — e.g.
  `ch05-q-bandwidth.svg`, `ch05-swr-gamma.svg`, `ch08-modulation-index.svg`,
  `ch10-mpe-math.svg`.
- **The ten NCVEC pool figures redrawn as original SVGs** (`ch05-pool-fig-e51.svg`,
  `ch06-pool-fig-e61/e62/e63.svg`, `ch07-pool-fig-e71/e72/e73.svg`,
  `ch09-pool-fig-e91/e92/e93.svg`): same components, same labels, same numbered
  positions as the official graphics — never copies. Each is registered as
  `kind:"original"` with the source note "redrawn from NCVEC pool figure EX-N"; canon
  §1.4 is the binding component-by-component redraw specification (§3 above). The pool
  is public domain, so this is both safe and faithful; the redraw rule keeps the
  book's visual style consistent and themeable. **Smith-chart discipline:** E9-3 is
  drawn in its post-errata-1 orientation (conventional horizontal, **infinity on the
  right**, 0 on the left), geometrically faithful (constant-resistance circles tangent
  at ∞, reactance arcs terminating on the outer circle, axis labels per the official),
  with **no invented wavelength scales** — the published figure has none.

**Verification discipline (binding):** every figure XML-parses, renders to PNG under
headless Chrome, and is eyeballed with the image-reading tool, defects fixed in place.
Every pool-figure redraw additionally gets a **side-by-side content comparison against
the official figure** (the files in `canon/source/`) and a **per-question
cross-check** — each keyed answer's component, point, or trace feature sits where the
redraw puts it. The redraws' question→position maps in canon §1.4 were themselves
derived from close reads of the published art (300-dpi renders with close-up crops,
cross-checked against the official SVG set).

Every registry entry carries id, chapter, number (in **first-reference order within
each chapter** — never authoring order, so late insertions don't scramble the book),
caption, kind, source, file, and a one-line **spoken** description (used by the
narration transform so figures degrade gracefully in audio). Every figure is embedded
inline in the built HTML. `figreg`'s `validate()` enforces existence, copyright tags,
and the protected-years rule, and the audit checks figure integrity (#1) and
copyright tags (#2) at build time.

## 7. Tooling inventory

All Python 3, stdlib-first (`matplotlib` for plots, `edge-tts` + `ffmpeg` for audio,
headless Chromium/Chrome → weasyprint for best-effort PDF). Every runnable script
keeps the repo-root `sys.path` bootstrap so it works both as `python3 tools/<x>.py`
and as an imported module.

- **`tools/build_book.py`** — parses the fixed dialect and produces the self-contained
  single-file **HTML** edition (inline SVG figures, inline math SVG, linked TOC,
  light/dark themes, **series book-switcher bar**, no external references), the plain
  **TXT** edition (math spoken as words, figures as `[Figure: ID]`), and the
  best-effort **PDF** (probe order chromium/chromium-browser/google-chrome/
  google-chrome-stable → weasyprint → skip). Also holds `SERIES_BOOKS` /
  `SERIES_CURRENT` (§8). Markdown pipe-table support (Appendix B's 502-row glossary
  renders as a real table) and h4 support carried from Book 3.
- **`tools/audit_book.py`** — the verification gate; exits non-zero on any failure.
  **8 checks:** (1) figure integrity, (2) copyright tags, (3) TOC/anchor consistency,
  (4) math rendering (every `$…$` span renders), (5) canon cross-check of every
  `**FACT:**` line, (6) no `UNVERIFIED` markers left in the canon, (7) format laws
  (skeleton + banned phrases; **only ch00 exempt**), (8) **pool fidelity** — see
  §7.1.
- **`tools/mathsvg.py`** — inline `$…$` → embedded SVG; **extended for this book**
  with the Extra Greek and complex forms ($\Gamma$, $\tau$, $\omega$, $\phi$,
  $\angle$, magnitude bars) so the whole Extra formula set renders (audit check #4 is
  the backstop).
- **`tools/figreg.py`** — loads/validates `figures/figures.json`; protected-years set
  (1968–1983) unchanged from Book 1.
- **`tools/narration.py`** / **`tools/make_audiobook.py`** — the 8-voice edge-tts
  audiobook pipeline (US/British/Australian/Irish × male/female), **chapters 00–10
  only** (the verbatim pool appendix is never narrated); ID3 `artist=Claude Opus 4.8`,
  `album=Your Last Ham License`. `speak_math`'s formula-token table was **extended for
  this book** with the Extra Greek (Γ→"gamma", ρ→"rho", τ→"tau", ω→"omega", φ→"phi")
  and ∠→"angle" on top of the carried set (π, Ω, ×, ≈, √, fractions, subscripts); the
  j-operator and magnitude bars speak sanely as themselves. **`tools/make_intro.py`**
  generates the spoken introduction (the capstone welcome).
  `docker/audiobook-index.html` is the player (§8).
- **`tools/make_exam.py`** — the practice-exam generator:
  `python3 tools/make_exam.py [--seed N] [--out build/] [--pool canon/pool-extra.json]`
  draws exactly **one question per NCVEC group** (50 groups → a valid 50-question
  exam), uniform random within group, reproducible with `--seed`; writes
  `build/practice-exam.md` (questions + choices A–D, **never the answers**) and
  `build/practice-exam-key.md` (letters + subelement tally). The Element 4 structure
  is **parameterized, not hardcoded**: the exam size is whatever the pool's group
  count is (one draw per group, driven by the JSON), and the pass threshold is the
  `PASS_SCORE` constant (**37 of 50** — Technician/General were 26 of 35). The group
  model **tolerates the deleted-ID gaps** — one uniform-random draw per group from
  whatever ids exist (E4D draws from 13, not 14).
- **`tests/`** — **107 pytest tests** covering all tooling (including the four
  check-#8 fixture tests: a correct quote passes; a one-word-off quote fails; a wrong
  answer letter fails; missing pool → skip — with a pool fixture that carries a
  **deleted-ID gap** so the coverage check is proven to tolerate non-contiguous
  numbering) plus a relative-links test on the built HTML.

### 7.1 Pool-fidelity rules (audit check #8)

- Question text, choice text, and answer letters are quoted **byte-exact** from
  `canon/pool-extra.*` (the audit compares whitespace-normalized against the `.json`).
  Published Unicode punctuation is preserved; never paraphrase a question; never
  retype pool text by hand — quotes are pulled from the canonical files with script
  assistance.
- Every quoted id must exist in the pool (id regex `E\d[A-H]\d\d` — the letter class
  reaches **H** for E7/E9); every stated choice line and answer letter must match the
  pool key; Appendix A must contain **all 599 active ids exactly once, in canonical
  pool order** (E1…E9 then E0, subelement 0 sorting as 10), skipping the four
  deletions exactly as the canonical files do. The audit mechanically verifies 599/599
  coverage, every quote, and every letter — it is the backstop that makes silent pool
  drift impossible.
- The **fully-errata'd 4th-errata form** is the only form used — the canonical files
  already carry it; quote, don't retype.
- The published quirks are reproduced as published in every quotation, never silently
  repaired:
  - the three **figure-stem typos** — E7G02's "the circuit in E7-3" (no "Figure"),
    E7G07's "Figure E73", E9B04's "Figure E92" (missing hyphens; genuine docx-vs-pdf
    content differences, docx authoritative);
  - the **on/in variance** — E5C10/E5C12 print "point on Figure E5-1", E5C11 prints
    "point in Figure E5-1";
  - the **E8B04 interior double space** ("…modulating frequency  is 2 kHz…") and
    **E2D04's double space after the choice-D label** (`D.  PACTOR III`) — interior
    whitespace is never normalized;
  - **E1C10 choice A's `- 43 dB`** (interior space after the minus sign);
  - the 66 **E1 Part-97 ID-line tags** in their published form — including E1A06's
    superseded `[97.303(h)(1)]` (the rule moved to (h)(3); §10.1) and the
    errata-1-corrected `[97.509(m)]` (E1E10) / `[97.509(i)]` (E1E11);
  - the **UTC naming split** — the pool prints "Utilities Technology Council (UTC)"
    (E1C03, E1C07) while the current rule text §97.303(g)(2) reads "Utilities Telecom
    Council (UTC)"; pool quotes keep the pool's form, rule quotes keep the rule's
    form, never blended in a single quotation (§10.6);
  - the E0 banner casing quirk and the headings' plain hyphens; the release-page
    quirks (the 2nd-errata "G8C/15 questions" misprint — the affected group is E2A —
    and the 3rd-errata date disagreement) are cataloged in the canon, never
    propagated.
- The four deleted questions are never quoted; Appendix A's coverage simply skips the
  deleted numbers.
- Check #8 **skips gracefully** (printed note, not failure) when the pool JSON is
  absent, so the audit still gates a bare scaffold.

## 8. Series-site machinery

The book is the last of three in the *Your First Ham License* series (Technician /
General / Extra) and carries the shared machinery. **This book ships with all three
books live and Extra current — it completes the series site.**

- **Book-switcher bar** — a slim series bar in both the generated book HTML
  (`tools/build_book.py`, driven by `SERIES_BOOKS = [("Technician","/tech/",True),
  ("General","/general/",True), ("Extra","/extra/",True)]` and `SERIES_CURRENT =
  "Extra"`) and the audiobook player. All three books are links; the current book is
  highlighted; no "coming soon" labels remain anywhere in the series machinery.
- **Stable sub-paths** — the books mount at `/tech/`, `/general/`, `/extra/` behind a
  series nginx proxy. **Book HTML uses only relative/anchor links** (enforced by a
  build test; the only absolute links allowed are the three series paths), so
  sub-path proxying needs no response rewriting.
- **`series/`** — `series/nginx.conf` (proxy: `=` `/` → landing page; `/tech/` → the
  tech container, active; `/general/` → the general container, active; `/extra/` →
  the extra container, **active — this book, completing the site**),
  `series/index.html` (the landing page: three cover-style cards — Technician live,
  General live, Extra **live + current highlight**).
  **`series-docker-compose.yml`** wires the three book images plus the proxy (the only
  published port, host :8080); **all three services are live — no `future` profile
  remains anywhere**. Each book's standalone image (`docker-compose.yml`, also :8080)
  runs fine alone.
- **Audiobook player** (`docker/audiobook-index.html`) — themed page with 12 tracks
  (intro + 11 chapters), a **voice switcher** grouped by accent (8 voices: Andrew,
  Ava, Ryan, Sonia, William, Natasha, Connor, Emily), continuous chapter-to-chapter
  playback, a live visualizer, and **resume** (voice/track/position/auto-next
  persisted in `localStorage` under **`ylhl-audio`** — this book's key; Book 2 uses
  `yfhl-audio`, Book 3 `ynhl-audio`). The **"Auto-play next chapter" toggle** (default
  ON, persisted alongside; when OFF, playback stops at each chapter end) is kept from
  Books 2–3 — the `ended` handler auto-advances only when the toggle is on.
- **Hosting/CI** — `Dockerfile` (nginx serving `build/index.html`, the TXT/PDF,
  `chapters/`, and `audiobook/` with the player at `/audiobook/`); GitHub Actions
  (`.github/workflows/build.yml`, push to `master`/`main` or `workflow_dispatch`,
  GitHub-only — no Gitea path) fetches the audiobook from **release v1.0** (intro +
  8 voices × 11 chapters; the fetch loop stays `seq -f "%02g" 0 10`), rebuilds the
  book, and pushes `ghcr.io/atvriders/your-last-ham-license:latest`. **Audio ships on
  the release, not in git.**
- **Series completion (binding ship procedure):** this repo ships with Extra live
  everywhere in its own machinery. The **Technician and General repos flip Extra live
  as two separate tiny commits** — each its own commit (series-bar flag in
  `tools/build_book.py` plus the landing-page card, rebuild, pytest + audit green),
  each **human-approved at that moment, never assumed, never bundled** with each other
  or with anything else. Those two commits are the only approved exceptions to the
  one-commit ship rule.

## 9. Copyright ledger summary

- **Prose is always original.** Nothing is copied from any study guide, handbook, or
  web page.
- **47 CFR Part 97 is public domain** (US Government work, 17 U.S.C. §105) and is
  quoted verbatim with section pinpoints (eCFR issue date 2026-07-28 ≡ 2026-07-20).
  FCC Public Notice DA 16-1048 is likewise a US Government work.
- **The NCVEC 2024–2028 Extra pool is public domain** (released as such by the NCVEC
  Question Pool Committee; statement captured in `canon/source/release-page.html`,
  fetched 2026-07-30): questions, choices, answer keys, and figure *content* may be
  reproduced verbatim.
- **All ten pool figures are redrawn, not copied** (§6).
- **Bare facts, frequencies, and formulas are not copyrightable**; all exam-prep
  explanations are written fresh.
- **ARRL Handbook ledger (carried from Book 1, governs any optional archival
  figure):** of the 13 owned editions (1927–1983), **7 are public domain and
  reproducible** (1927, 1931, 1933, 1936, 1940, 1941, 1951 — each affirmatively
  evidenced) and **6 are protected and never reproduced in any form** (1968, 1974,
  1976, 1977, 1981, 1983). `figreg.validate()` mechanically rejects any figure tagged
  with a protected-year source. This book ships with **zero archival images** — every
  figure is original.

## 10. Resolved uncertainties — the headline rulings (canon §7)

Every research flag was closed to a sourced value or a deliberately careful wording
(12 subsections in the canon). The rulings a future editor must not undo:

### 10.1 The 60 m rule change (91 FR 1430) — the pool kept its 60 m questions

The FCC's WRC-15 Report & Order (WT Docket 23-83, published as 91 FR 1430/1431,
effective 2026-01-14) replaced the channelized 60 m rules the 2023 pool was written
against. **Current text** (verified 2026-07-30 against the eCFR, issue date
2026-07-28 ≡ 2026-07-20): amateurs may transmit (1) anywhere in the contiguous
**5351.5–5366.5 kHz** segment at **9.15 W ERP**, and (2) on **four** of the five old
channels — **5332, 5348, 5373, 5405 kHz** — at **100 W ERP**; the ≤ 2.8 kHz bandwidth
cap now applies to all 60 m spectrum; the CW-at-channel-center rule survives in
§97.303(h)(3). Unlike the General pool (whose 6th errata withdrew its two conflicted
questions), **the Extra pool's four errata never revised E1**: both surviving Extra
60 m questions remain literally correct under current text — **E1A06** (CW at the
center frequency of the channel; the rule moved from §97.303(h)(1) to §97.303(h)(3),
so **E1A06's printed citation `[97.303(h)(1)]` is stale** — preserved verbatim in
quotes, never "repaired") and **E1C01** (2.8 kHz maximum bandwidth, correct under both
texts). **Binding:** drill the keyed answers exactly as published; chapters cite the
CURRENT renumbered sections (§97.303(h)(3), §97.313(i)) when explaining; teach the
two-part structure (segment plus four channels, 9.15 W ERP / 100 W ERP, USB phone, 2.8
kHz maximum bandwidth). **No prose may describe 60 m as "five channels, 100 W ERP" —
that rule is dead.**

### 10.2 Upgrade immediacy — §97.9(b) plus the /AE indicator

A General who passes Element 4 and properly submits Form 605 to the administering VEs
may exercise Extra privileges **immediately** — "until final disposition of the
application or until 365 days following the passing of the examination, whichever
comes first" (§97.9(b)) — appending the indicator **AE** to the call sign
(**§97.119(f)(3)** — NOT (f)(2); (f)(2) is AG, for upgrades to General), separated by
the slant mark or any suitable word (§97.119(c)). In one VEC's practice, say
"temporary AE" (or "Interim" / "Alpha Echo") on phone and sign call/AE on CW or
digital, dropping the suffix once ULS shows Amateur Extra (Laurel VEC FAQ, extracted
2026-07-30). Contrast with new licensees: a first-time candidate has NO authority
until the grant appears in ULS — the immediacy rule is for existing licensees only.
**Wording law (binding): never write "transmit as soon as you pass" without both
conditions (Form 605 properly submitted to the VEs + CSCE in hand) and the /AE
identification requirement in the same breath — §97.9(b) is conditional authority,
never unconditional.**

### 10.3 Pass-threshold phrasing — print "37 of 50"

§97.503(c) pins a count, not a percentage: "The minimum passing score is 37 questions
answered correctly." The book prints "**37 of 50**" as the authoritative figure
everywhere (cover copy, ch00, exam products). "74%" is derived arithmetic (37/50 =
0.74); when it appears at all it is flagged as derived — e.g., "37 of 50 (74%, derived
arithmetic)". The same discipline the series applied to "26 of 35."

### 10.4 Figure E5-1 is a chart, not a circuit

Figure E5-1 is a rectangular-coordinate **impedance graph** — axes −600 to +600 Ω on
both scales, horizontal = resistance, vertical = reactance, eight labeled points
(P1–P8) — **not** an R-L-C schematic (the R, L, and C live in the question stems; the
figure is the plane on which the computed impedance is plotted). The keyed answers are
P4 (E5C10, 400 − j300), P3 (E5C11, 300 + j400), and P1 (E5C12, 300 − j400); points 5
and 7 have negative resistance (impossible for a passive series circuit — auto-wrong)
and points 6 and 8 sit on the axis as distractors. ch05 teaches the figure as a
plotting exercise per the E5C09 axis convention; the redraw spec is canon §1.4.

### 10.5 Pool-vs-practice teaching tensions (canon §7.6), in one line each

- **E3B11 sporadic-E timing:** the pool keys sporadic E as "between sunrise and
  sunset" (a solar-ionization mechanism) while 6 m operators also work plenty of
  evening Es — teach the pool answer with its mechanism; **never print "Es ends at
  sunset."**
- **E2C01 remote-control ID:** the pool keys "no additional indicator is required" for
  US remote-control operation (§97.119(c) permits but does not require indicators) —
  teach it flatly; many Generals remember otherwise.
- **E2C03 30 m contest exclusion:** "generally excluded" is a long-standing convention
  (the WARC truce), not an FCC rule — chapters say "convention, not regulation" in the
  same breath.
- **E5A04 parallel-resonance impedance:** the keyed answer assumes the parallel-R
  model — flag the model assumption when teaching; do not "fix" the pool.
- **E5D10 electrical length vs diameter:** a larger-diameter conductor has a *longer*
  electrical length — counterintuitive and keyed that way; pin it as written.
- **PRB-1 status (E1B07/E1B11):** a declaratory ruling referenced in §97.15(b)'s
  parenthetical, binding only state/local regulation — **not** homeowners'
  associations (the classic wrong answer; HOAs are private contracts).
- **E1F06 STA nuance:** §1.931 is the generic WTB STA provision and never mentions the
  amateur service; teach the pool answer and present §1.931 as the FCC's general STA
  mechanism — do not cite it as amateur-specific, and do not hunt for a Part 97 STA
  section (none exists — resolved wording, not an open question).
- **E0 rests on Part 1 territory:** the E0A02/A04/A09/A10 answers rest on
  §§1.1307/1.1310/2.1091/2.1093 and OET Bulletin 65, pointed to by §97.13(c)(1) — no
  Part 97 citation should be invented for them.
- **"All these choices are correct"** is the keyed answer **16 times** in this pool
  and a wrong decoy **34 times** (script-verified full-pool counts) — chapters teach
  content, never pattern-guessing.

### 10.6 UTC naming and the citation tags (canon §7.7)

The pool prints "**Utilities Technology Council (UTC)**" (E1C03, E1C07 — quoted
byte-exact); the current rule text §97.303(g)(2) reads "**Utilities Telecom Council
(UTC)**" (quoted byte-exact in the canon's §2.2). Both forms are recorded; pool quotes
keep the pool's form, rule quotes keep the rule's form, and ch01 notes the discrepancy
in one sentence. **Never blend the two in a single quotation.** The E1E10/E1E11
citation tags ride in their errata-1-corrected form (`[97.509(m)]` / `[97.509(i)]`),
and E1A06's `[97.303(h)(1)]` rides stale-but-preserved (§10.1).

### 10.7 The remaining resolutions (canon §7.2, §7.8–§7.10), in one line each

- **§7.2 Other post-pool Part 97 amendments:** space-station post-mission disposal is
  now **5 years** for LEO below 2000 km (89 FR 65223, replacing the pool-era 25 — not
  tested by any active E1D question, but satellite prose must say 5 years, not 25);
  the 90 FR 57712 housekeeping (§97.315(b)(2), §97.521(b), §§97.27–97.29 → Reserved)
  and the 5.9 GHz and 70 cm restructures have **zero answer impact**; the pool-era
  text already carried the 2.8 kHz HF bandwidth standard, so the pool was written to
  the amended rule — chapters never resurrect 300 baud as an exam fact (it survives
  only on 2200/630 m).
- **§7.8 E2B and APRS deliberate color exclusions:** the research notes deliberately
  supplied no added color for E2B (television) or the APRS internals — the canon's §2
  FACTs are the complete reservoir for those groups; chapter writers must not seek
  color that does not exist.
- **§7.9 Ingestion-level flags:** the stale syllabus counts (§3 above); the `- 43 dB`
  quirk attribution is corrected to **E1C10 choice A** (the ingestion report's §3
  misattributed it to E1B03 — recorded correctly in canon §1.2/§7.9, preserved
  byte-exactly either way); the docx-vs-pdf figure-ID typos; no ARRL mirror — the
  docx-vs-pdf double parse is the cross-check of record; whitespace normalizations
  were paragraph-edge only; no 5th errata as of 2026-07-30; the 3rd-vs-4th cross-check
  shows zero content differences among the 599 common questions; the release-page
  quirks are cataloged, never propagated.
- **§7.10 Book 2/3 wording laws, adopted unchanged:** the /AE upgrade law (§10.2
  restated as series law); grant timing is "your ULS record typically updates within
  days," never a promised day count; remote exams are never promised — availability is
  the VE team's call (Laurel runs in-person only); CORES/FRN registration "carries no
  fee and no exam requirement," never "free of charge"; Laurel VEC is larc-vec.org
  (laurelvec.com 307-redirects there); multiple elements in one session — the VEC
  transmits one application reflecting the highest class earned, so a Technician may
  in principle test straight through to Extra in one session.

### 10.8 The ch10 MPE illustration's units and averaging window (canon §7.12)

Two defects in the enrichment-only MPE illustration (ch10's worked example, the
`ch10-mpe-math` figure, and Appendix B's S = ERP/(4πR²) micro-example) were caught at
technical audit on 2026-07-31 and fixed in place; this is the numeric pin of record:

- **Power-density units (was wrong by 10×):** S = ERP/(4πR²) for 100 W ERP at 10 m is
  ≈ 0.08 **W/m²** = 0.008 mW/cm²; the draft's "0.08 mW/cm²" conflated the two units.
  **Binding:** peak S ≈ **0.08 W/m² (0.008 mW/cm²)**; ≈ 0.016 W/m² after SSB speech
  duty; ≈ 0.008 W/m² across the window; the uncontrolled 30–300 MHz floor is **2 W/m²
  (= 0.2 mW/cm²)**, so the peak sits ≈ 25× under the limit. The MPE limits themselves
  stay in mW/cm² (OET Bulletin 65's own units); the station's computed densities are
  W/m², with the mW/cm² equivalent named at first use.
- **Averaging window (was the wrong regime):** OET 65's windows are **6 minutes
  controlled / 30 minutes uncontrolled**; the worked example's scenario is the
  neighbor's lot line — uncontrolled territory — so its window is **30 minutes** (the
  draft used the 6-minute controlled value). ch10 teaches both windows explicitly; the
  worked example, the figure's bottom panel, and Appendix B all use the 30-minute
  uncontrolled window.
- **Superseded mirrors:** `chapters/specs/ch10.spec.md` §5 and the `figures.json`
  caption/spoken fields for `ch10-mpe-math` still carry the old wording (outside the
  audit's edit scope) — refresh both at the next spec/figures maintenance pass; canon
  §7.12 governs until then.

## 11. Time-sensitive register (canon §7.11)

Each value is pinned in the canon with its verification date (**all verified
2026-07-30**, except the Laurel address 2026-07-23) and must be **re-verified at the
stated trigger before any reprint or new edition**:

| Item | Pinned value | Re-verify trigger |
|---|---|---|
| **Pool currency (the big one)** | 2024–2028 Extra pool valid for exams 2024-07-01 → **2028-06-30**; 4th errata (2026-02-04) incorporated; no 5th errata | Each reprint; **check ncvec.org from late 2027 for the 2028–2032 successor pool** (expected late 2027 by analogy with the 2026 Technician cycle, but NCVEC has announced no date — never print a release date as fact) |
| FCC application fee | $35 (new license, renewal, rule waiver, vanity), effective 2022-04-19; **upgrades EXEMPT** | Before each reprint (fees change by FCC fiscal-year order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 under 18 (calendar-2026 figures) | Each January |
| NCVEC Form 605 | 2022 edition | Before publication and each reprint |
| Part 97 rule text | eCFR current issue 2026-07-28 (byte-identical to 2026-07-20); includes the 60 m amendment 91 FR 1430/1431 and housekeeping 90 FR 57712 | Re-pull every cited section before any reprint |
| Satellite fleet | Named birds are time-sensitive: FalconSAT-3 re-entered January 2023; SO-50 and QO-100 status shifts month to month; the pool tests concepts only, never specific satellites — keep the book that way | Before print, check amsat.org/status/ and drop or demote any bird that has gone quiet |
| 6 m digital frequencies | FT8 50.313 (50.323 intercontinental), FT4 50.318, MSK144 calling 50.260 — all convention, not band plan | Before print, against the current WSJT-X default frequency table and ARRL band plan |
| WSPR sensitivity | −31 dB SNR in 2500 Hz (WSJT-X 2.7 guide); older documentation says −28 dB | Before print, against the current User Guide |
| Doppler magnitudes | ±3.5 kHz (2 m) / ±10 kHz (70 cm), typical-LEO order-of-magnitude | Present as order-of-magnitude practice, never constants |
| EME path loss | ≈252 dB at 144 MHz, ≈271 dB at 1296 MHz — band-specific | Never generalized as "EME path loss is 252 dB" without the band |
| QO-100 footprint | Brazil-to-Thailand; of the Americas only northeast Brazil — the geostationary *example*, not a US opportunity | Before print; always note continental-US readers cannot reach it |
| CEPT country lists | DA 16-1048's participating-country lists are dated 2016-09-16 and change over time | Before travel-related reprints, check the European Communications Office |
| fcc.gov HTML pages | Amateur Service facts lifted from 2026-07-23/24 verifications (pages 403 to curl — bot protection) | Re-verify in a browser before publication |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com 307-redirects there) | Before each reprint |

**Contained-swap procedure for the 2028–2032 pool (binding, canon §7.11):** the
book's teaching content is durable by design — only the pool-facing artifacts change
with a new pool. On release of the successor pool: (1) ingest it into `canon/` with a
new ingestion report (new canonical files, sha256s, errata ledger, deleted-ID list);
(2) update the canon's §1 (files, counts, validity window) and any §2 FACT or §7
resolution whose rule or frequency changed; (3) refresh each chapter's Exam Focus
question picks and Appendix A's verbatim pool against the new canonical files; (4)
re-run the build audit and the full test suite to green; (5) nothing else changes —
notation, glossary, chapter map, teaching prose, and figures stay as pinned. **Any
printing of this book after mid-2028 must state which pool exams actually use.**

## 12. How to extend

This book is the capstone — there is no Book 5 in the program. The template itself is
the inheritance, for a successor-pool edition of any series book or a future course:

1. Copy the repo scaffold: `tools/`, `tests/`, Docker/CI, `series/` machinery,
   `docker/audiobook-index.html` — retarget constants (titles, `SERIES_CURRENT`,
   image names, chapter count in the CI audio-fetch loop, the player's `localStorage`
   key, the exam's `PASS_SCORE`).
2. Ingest the target pool into `canon/pool-*.txt/json` (same double-parse discipline;
   record sha256s and provenance in the new canon; pin the group list — it fixes the
   ID-regex letter class and the exam size).
3. Rebuild `accuracy-canon.md` for that pool (pinned facts, notation, glossary,
   chapter map); write chapters against the same format laws; the same 8-check audit
   gates everything, including check #8 against the new pool.
4. Flip the book's flag in `SERIES_BOOKS`, activate its block in `series/nginx.conf`,
   and drop its `future` profile in `series-docker-compose.yml` when it ships.

**A pool swap within this book** (an NCVEC errata, or the 2028–2032 pool): follow the
contained-swap procedure in §11 — replace the `canon/pool-extra.*` pair, update the
canon, re-run `python3 tools/audit_book.py` (check #8 mechanically flags every
chapter and appendix quote whose text or answer letter drifted, and any coverage
gap), patch the affected quotes (script-assisted, never retyped), update any FACT
lines the canon change invalidates, rebuild.

## 13. Production history

Built 2026-07-29 → 2026-07-31 by a **multi-agent workflow** (~50 subagent launches
across the tooling, canon, figures, chapters, appendix, and audit phases — estimate —
plus retries after transient engine errors), reusing Book 3's production machinery:
the scaffold (toolchain, tests, Docker/CI, series machinery, player) was copied
wholesale from the General repo — the newest base — and retargeted at constants level,
then extended where the Extra material demanded it. New in this book: the
`make_exam.py` parameterization to the **50-question / 37-to-pass** Element 4
structure (exam size driven by the JSON's group set); the E-ID regex letter class
widened to **A–H** (E7/E9 groups reach H); the `mathsvg` and `speak_math` extensions
for the Extra formula set (Γ, ρ, τ, ω, φ, ∠, magnitude bars, complex-impedance
forms); **ten pool-figure redraws** with side-by-side geometric verification against
the official NCVEC art, including the E9-3 Smith chart in its post-errata rotated
form; the largest Appendix A in the series (599 verbatim quotes, 47,998 words); and
the **series-site completion** — this book ships with all three books live and Extra
current, and its ship flips Extra live in the Technician and General repos as two
tiny human-approved commits. The gate the content was written into: **107 pytest
tests, 8 audit checks** (including mechanical verification of all 599/599 pool quotes
and answer keys), full HTML/PDF/TXT build. This runtime does not meter subagent
tokens, so no measured token total exists; the README's stats block carries a
clearly-labeled estimate instead.

## 14. Commands

**Regenerate the book:**
```
python3 tools/build_book.py --html --txt --pdf --out build/
```

**Verify (the accuracy/format/pool gate):**
```
python3 tools/audit_book.py
```

**Run the tooling test suite:**
```
python3 -m pytest -q
```

**Draw a practice exam:**
```
python3 tools/make_exam.py --seed 7 --out build/
```

## 15. Guidance for AI models extending this book

- **Obey `accuracy-canon.md` exactly.** It is the single source of truth for pool
  wording, dates, values, notation, glossary wording, the chapter map, and copyright
  status. Never re-date an event, restate a rule, or reword a question from memory —
  trace every fact back to the canon, and quote the pool only from
  `canon/pool-extra.*`. If the canon needs a new entry, add it there first, sourced,
  before touching chapter prose.
- **Never paraphrase a pool question, repair a published quirk, or quote a deleted
  question.** Byte-exact quotes, the 4th-errata form always; the stem typos ("in
  E7-3", "Figure E73", "Figure E92"), the on/in variance, the E8B04 and E2D04 double
  spaces, E1C10's `- 43 dB`, the stale `[97.303(h)(1)]`, and the `[97.509(m)]` /
  `[97.509(i)]` tags preserved; E9E10, E2A13, E6D07, E4D05 exist only as numbering
  gaps. Extract quotes script-assisted — never retype pool text by hand.
- **Teach current rules where the rule moved after the pool was written.** 60 m is
  the segment-plus-four-channels structure under 91 FR 1430 (never "five channels,
  100 W ERP"); satellite post-mission disposal is 5 years, not the pool-era 25; HF
  digital is the 2.8 kHz bandwidth standard (never 300 baud as an exam fact); the
  keyed answers are drilled exactly as published — the canon carries both halves of
  that split.
- **Keep the notation law.** Prose uses V and ×; unit case (kHz, MHz, mA, µV, pF) is
  load-bearing; complex impedances use the j-operator, the house minus, and ∠θ in
  degrees ("50 − j25 Ω", "55.9 ∠−26.6° Ω") — and verbatim pool quotes keep the pool's
  ASCII forms byte-exact.
- **Keep the careful wordings.** The /AE upgrade law (both conditions plus the
  §97.119(f)(3) indicator), "37 of 50" (never a bare "74%"), the UTC naming split,
  "Es ends at sunset" never printed, the MPE illustration's enrichment flag and its
  §7.12 numbers, fees, timing promises, and remote exams use exactly the hedged forms
  the canon resolved (§10) — do not strengthen them.
- **Never reproduce a protected Handbook image.** The 1968–1983 editions are under
  copyright — no scans, no traced reproductions, no quoted running text. This book
  needs none.
- **Run `python3 tools/audit_book.py` before considering any change done.** It is the
  mechanical enforcement of everything above (facts, format laws, figure tags, math,
  TOC, and 599/599 pool fidelity) — a change that doesn't pass it is not finished,
  regardless of how it reads.
