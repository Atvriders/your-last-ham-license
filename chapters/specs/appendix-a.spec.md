# Writer Spec — Appendix A. The Complete 2024–2028 Extra Pool

**Output file:** `appendices/pool.md` (built from `appendices/pool-fragments/E1.md` … `E0.md`)
**Target length:** excluded from the book's ~50–65k prose target — it is the verbatim pool, 599 question blocks (~45k+ words).
**Pool coverage:** **all 599 questions, exactly once each, in canonical pool order** — the audit's check #8 (`check_appendix_pool_coverage`) mechanically requires: every pool id present exactly once, every id a real pool question, the sequence in pool order, and every answer letter matching the key.

## 1. Purpose

Appendix A carries the full 2024–2028 Amateur Extra (Element 4) pool the same way the chapters' Exam Focus sections carry samples: every question verbatim, choices A–D verbatim, correct answer marked, plus a **one-line plain-language "why"** that names the chapter teaching it. Print-only — this appendix is **not narrated** in the audiobook (decision locked, design §2/§4).

## 2. Structure

- First line: `## Appendix A: The Complete 2024–2028 Extra Question Pool` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC; the colon form mirrors the series' shipped appendices).
- One short intro paragraph: what this is (the verbatim NCVEC 2024–2028 Extra pool, released into the public domain by the NCVEC QPC — "The NCVEC Question Pool Committee hereby releases into public domain the 2024-2028 Element 4 Extra Class Question Pool" — valid for exams 2024-07-01 → 2028-06-30, incorporating all four errata through 2026-02-04 — 599 active questions; the four withdrawn questions — E9E10, E2A13, E6D07, E4D05 — simply do not appear, exactly as the canonical files omit them), how to use it (read the mapped chapter, then drill its group here), and the key to the entry format.
- Then **one `###` section per subelement, in pool order E1 → E9 → E0**, using the normalized published title + counts (title case, em dash — the series' normalization; the published banners are all-caps, and E0's banner carries the casing quirk `SUBELEMENT E0 - SAFETY - [1 exam question - 1 group]` — normalize it like the rest; canon §1.3 records the quirk):

  | Heading line |
  |---|
  | `### E1 — Commission Rules (68 questions, 6 on the exam)` |
  | `### E2 — Operating Procedures (60 questions, 5 on the exam)` |
  | `### E3 — Radio Wave Propagation (39 questions, 3 on the exam)` |
  | `### E4 — Amateur Practices (63 questions, 5 on the exam)` |
  | `### E5 — Electrical Principles (49 questions, 4 on the exam)` |
  | `### E6 — Circuit Components (68 questions, 6 on the exam)` |
  | `### E7 — Practical Circuits (99 questions, 8 on the exam)` |
  | `### E8 — Signals and Emissions (48 questions, 4 on the exam)` |
  | `### E9 — Antennas and Transmission Lines (93 questions, 8 on the exam)` |
  | `### E0 — Safety (12 questions, 1 on the exam)` |

- Within each subelement section, optionally one `####` line per group with the **published group heading verbatim** from `canon/pool-extra.txt` (e.g. `#### E1A Frequency privileges; signal frequency range; automatic message forwarding; stations aboard ships or aircraft; power restriction on 630- and 2200-meter bands`) — the published wording is preserved byte-exactly (note: the Extra pool's group lines use a plain space after the group letter, no dash); `####` group lines render as anchored h4s, never in the TOC. Then that group's questions in ascending number order, **skipping the deleted numbers** (E2A ends at 12; E4D has no 05; E6D has no 07; E9E has no 10).
- **The ten pool-figure redraws are embedded once each, on the line immediately before the first referencing question's quote block**, and referenced by name ("the redrawn Figure E7-3, above") in the why lines of that figure's remaining questions:

  | Embed line | Placed immediately before | Figure's questions |
  |---|---|---|
  | `{{fig:ch05-pool-fig-e51}}` | E5C10 | E5C10–E5C12 |
  | `{{fig:ch06-pool-fig-e61}}` | E6A10 | E6A10, E6A11 |
  | `{{fig:ch06-pool-fig-e62}}` | E6B10 | E6B10 |
  | `{{fig:ch06-pool-fig-e63}}` | E6C08 | E6C08, E6C10, E6C11 |
  | `{{fig:ch07-pool-fig-e71}}` | E7B10 | E7B10–E7B12 |
  | `{{fig:ch07-pool-fig-e72}}` | E7D06 | E7D06–E7D08 |
  | `{{fig:ch07-pool-fig-e73}}` | E7G02 | E7G02, E7G07, E7G09–E7G11 |
  | `{{fig:ch09-pool-fig-e91}}` | E9B01 | E9B01–E9B03 |
  | `{{fig:ch09-pool-fig-e92}}` | E9B04 | E9B04–E9B06 |
  | `{{fig:ch09-pool-fig-e93}}` | E9G06 | E9G06, E9G07 |

## 3. Entry format (audit check #8 parses this exactly)

Every one of the 599 entries is one blockquote in exactly this shape, followed by one plain line carrying the published ID line:

```
> **E1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: D** — <one-line why, ending with the teaching chapter: "… — taught in chapter 1.">

Published ID line: `E1A01 (D) [97.305, 97.307(b)]`
```

Rules (all mechanically enforced or canon law):

- **Question and choice text byte-exact** from `canon/pool-extra.json` (the audit compares whitespace-normalized). Published Unicode punctuation (curly apostrophes/quotes) is preserved, never converted to ASCII.
- **All four choice lines A–D always present**, in order. The `**Answer: X**` letter must match the pool key exactly.
- **Order:** canonical pool order = subelements E1…E9 then E0; group A→H within each subelement; ascending number within each group, skipping exactly the four deletions (§1.3). (This is the published order and the audit's `pool_sort_key`; iterating `sorted(pool, key=pool_sort_key)` over `canon/pool-extra.json` yields it.)
- **The published ID line** (answer letter + Part 97 reference as printed in `canon/pool-extra.txt`) rides on a **separate plain-text line after the blockquote, in backticks** — never inside the `> **EnXnn** …` line itself (the audit would read it as part of the question text and fail the quote). 66 questions carry Part 97 citations, all in E1 (E1C04 and E1C06 are the only E1 questions without one); the other 533 print `EnXnn (L)` with no bracket. Published quirks stay verbatim, never repaired:
  - `E1A06 (B) [97.303(h)(1)]` — the printed citation is **stale** under the current 60 m rules (the channel rules moved to §97.303(h)(3); canon §7.1); the ID line is preserved as printed and the why line cites §97.303(h)(3).
  - `E1E10 (C) [97.509(m)]` and `E1E11 (B) [97.509(i)]` — these are the **errata-1-fixed** citations and are the current published form; print them as-is (never "revert" them to anything else).
  - **E1C10's choice-A interior space:** the published text prints `A. - 43 dB` (space after the minus) — reproduce it byte-exactly in the quote block's choice line (canon §1.5).
  - **The figure-stem typos:** E7G02 prints "the circuit in E7-3" (no "Figure"); E7G07 prints "Figure E73" (missing hyphen); E9B04 prints "Figure E92" (missing hyphen) — all three quoted byte-exactly, never repaired (canon §1.4/§7.6).
  - **The on/in variance:** E5C10 and E5C12 print "point on Figure E5-1" while E5C11 prints "point in Figure E5-1" — preserve each as published (canon §1.4).
  - **E8B04's interior double space** — preserve byte-exactly (canon §1.5).
- **The one-line "why"** is original prose: a plain sentence (or two short ones max) giving the reason the keyed answer is correct in colleague language, and naming the teaching chapter ("taught in chapter 3"). Never paraphrase the question back; never contradict the canon; where the canon carries the fact, the why echoes it. The 28 figure-question whys reference the redraw by name ("the redrawn Figure E9-3, above") and may lean on the canon §1.4 question→position maps (e.g., E7G09's why notes the sign — "−2.3 V, and the sign is the answer").
- Deleted questions are never quoted, and no placeholder marks their absence (canon §1.3: they appear only as numbering gaps).

## 4. Chapter-mapping table (for the "why" lines — binding, from canon §5)

| Pool groups | Teaching chapter |
|---|---|
| E1A–E1F | chapter 1 |
| E2A–E2E | chapter 2 |
| E3A–E3C | chapter 3 |
| E4A–E4E | chapter 4 |
| E5A–E5D | chapter 5 |
| E6A–E6F | chapter 6 |
| E7A–E7H | chapter 7 |
| E8A–E8D | chapter 8 |
| E9A–E9H | chapter 9 |
| E0A | chapter 10 |

## 5. Production method (fragment-per-subelement, then assemble)

The 599-block assembly is mechanical — script it, never hand-type pool text:

1. **Ten fragment agents (E1–E0), one per subelement.** Each emits one fragment file (`appendices/pool-fragments/E1.md` … `E0.md`) containing its subelement's `###` heading line, optional `####` group lines, and every active question block + Published ID line, in canonical order. The "why" lines are authored per subelement (colleague language, one line each, ending "— taught in chapter N." per §4) — everything else is verbatim pool or the published ID lines.
2. **Generation:** load `canon/pool-extra.json`; iterate `sorted(pool, key=pool_sort_key)` (import `pool_sort_key` from `tools/audit_book.py`); for each id emit the six blockquote lines from the JSON fields (`question`, `choices` A–D, `answer`), then the published ID line parsed from `canon/pool-extra.txt` (match `^EnXnn (L)( \[…\])?$` — remember the two citation-less E1 questions E1C04/E1C06 and the 533 citation-less IDs elsewhere). Merge the authored whys by id; regenerate mechanically — never hand-edit the generated question text.
3. **Assemble** the fragments in canonical order (E1…E9 then E0), normalize each `###` heading to the §2 table, and splice the ten `{{fig:…}}` embeds onto the lines before their first referencing questions (§2 table).
4. **Byte-exact gate (per-fragment at handoff and book-wide at the end):** re-extract every question from the assembled `appendices/pool.md` and diff mechanically against `canon/pool-extra.json` — run `python3 tools/audit_book.py`; check #8 must report 0 errors for `appendices/pool.md` (all 599 quoted once, in order, letters matching the key).

## 6. Integrity notes

- Public domain: the NCVEC QPC released this pool into the public domain (release page captured in `canon/source/release-page.html`); the intro paragraph says so in one sentence with the validity window **2024-07-01 → 2028-06-30** and the four-errata record (no 5th errata as of 2026-07-30; re-check the release page before each reprint).
- No `**FACT:**` lines required in appendices (exempt from the format laws); no Key Takeaways; no banned phrases anywhere ("little did they know", "in that moment", "a testament to").
- The "why" lines are the only original prose in the appendix — everything else is verbatim pool or the published ID lines.
- The 60 m entries (E1A06, E1C01) drill the keyed answers exactly as published; their whys explain with the current rule sections (§97.303(h)(3), §97.307(f)(14)(i)) per canon §7.1 — never teach the withdrawn wording as current, and never "repair" E1A06's printed `[97.303(h)(1)]` ID line.
- The release page's 2nd-errata "G8C/15 questions" misprint (the affected group is E2A, 12 remain) is a quirk of the *page* — cataloged in canon §1.3, never propagated anywhere in this book.
- "All these choices are correct" is the keyed answer 16 times (E1D05, E2A02, E2A07, E2C08, E2C10, E2E04, E4A08, E4A11, E4B11, E4E02, E4E10, E6E10, E7D14, E7H13, E9F08, E0A06) — the whys for those entries state *why each clause is true*, never "it's all of the above" as a guess heuristic (canon §7.6).
