# Accuracy Canon — Your Last Ham License: The Extra Course (2024–2028)

**This file is LAW.** It is the single, binding source of truth for *Your Last Ham License: The Extra Course (2024–2028)*. Every chapter writer, figure author, appendix writer, and auditor conforms to it exactly: pool wording, numbers, dates, notation, terminology, chapter mapping, and copyright reproducibility are governed here and nowhere else. Where a claim was ever contested during research, this file states the one resolved value the book will use and cites it; disagreements with any draft chapter are resolved in favour of this canon, not the chapter. Every uncertainty flagged during research has been closed to a sourced value or a deliberately careful wording in **§7 Resolved Uncertainties** — there are no open placeholders in this document, and the automated build audit greps this file to confirm it.

Companion canonical data (part of this canon by reference): `canon/pool-extra.txt` and `canon/pool-extra.json` — the verified 599-question NCVEC 2024–2028 Extra (Element 4) pool. Question text, choices, and answer letters are quoted from those two files only, never from memory, web mirrors, or third-party study guides.

Series note: this is Book 4 in the series — the last rung of the license ladder — written for readers who hold the General license Book 3 (*Your Next Ham License: The General Course (2023–2027)*) teaches to, which in turn built on Book 2 (*Your First Ham License: The Technician Course (2026–2030)*). Notation, units, and shared glossary terms are identical to Books 2 and 3 wherever they overlap (§3, §4); where the Extra material legitimately deepens a convention (complex-number impedance is exam math here, the Smith chart is a pool figure rather than a sidebar), the difference is stated explicitly rather than silently changed.

---

## 1. Pool Summary & Revision Record

### 1.1 Canonical pool files (the only quoting sources)

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-extra.txt` | 175,707 | `a03fb3c8b4a8401a196057c34199bd1d355931170c1fef9625fbdd9421f48d0e` |
| `canon/pool-extra.json` | 267,486 | `6fdf1cae68793c94dd2965dfac02a4e614e0ee2d825009ef4cd76fe06a8bfa50` |

Both hashes recomputed at canon assembly (2026-07-30) and byte-identical to `canon/ingestion-report.md` §2 and `canon/source/sha256sums.txt`. The `.txt` is the human-readable, byte-exact rendering (ID lines `E1A01 (D) [97.305, 97.307(b)]`, one line per question and per choice, `~~` separators, published subelement/group headings — printed by NCVEC with plain hyphens, unlike the General pool's en dashes, preserved not normalized — a `#`-comment provenance header, and the published tail lines `~~~end of question pool text~~~` and `NOTE: The graphics required for certain questions in sections E5, E6, E7, and E9 are included on the following pages.`). The `.json` is the structured form: top-level object keyed by question id; each entry has `group`, `subelement`, `question`, `choices` (exactly "A"–"D"), `answer` (one of "A"–"D"), `figure` (null, or one of the ten published figure ids "E5-1" … "E9-3"). Part 97 references live only on the `.txt` ID lines — 66 questions carry one, **all in subelement E1** (every E1 question except E1C04 and E1C06; 58 single refs, 8 comma-separated multi refs); the other 533 are published as bare `E2A01 (D)`.

### 1.2 Provenance (verified source downloads)

Landing page: <https://ncvec.org/index.php/2024-2028-extra-class-question-pool-release> ("2024-2028 Extra Class Question Pool Release"; verified working 2026-07-30). Downloaded 2026-07-30 into `canon/source/` (curl with a browser User-Agent; no 403s):

| File | Bytes | sha256 |
|---|---:|---|
| `canon/source/ncvec-2024-2028-extra-pool-4th-errata-feb4-2026.docx` | 674,155 | `581ff3aa4c98bb2a6fcc303fe1ce19beb29bc7d3d02ff7fe5c6162c4c26ce4f7` |
| `canon/source/ncvec-2024-2028-extra-pool-4th-errata-feb4-2026.pdf` | 952,745 | `9cc63ae0c1c9ee63a617824555d5b4e73da8c8edb91566f97a66770eb200f517` |
| `canon/source/ncvec-2024-2028-extra-pool-3rd-errata-sept25-2025.docx` | 673,424 | `e24c58d10b92c0d3e9e2a91bc4400aa7979cd299accb1459fed77b7a99a064ad` |
| `canon/source/ncvec-2024-2028-extra-pool-3rd-errata-sept25-2025.pdf` | 951,138 | `f668b1fd9ddf7ba1cefacc3bd73767ebb6f2e1b5e9a3015f52977ab6c160c64e` |
| `canon/source/Extra_Figures_2024-2028-1.pdf` | 78,505 | `591bb4c9fc9a9267e298b3ee23c93ab54ba3813f8ea3730123f9ccda1e4b80f2` |
| `canon/source/2024-2028 Amateur Extra Class Pool Diagrams_Page_1.jpg` | 142,593 | `fff1411a04c35aa58262e64d8188f75778fbd00cabe7997f9d8eae298df9a2cb` |
| `canon/source/2024-2028 Amateur Extra Class Pool Diagrams_Page_2.jpg` | 168,703 | `6b085fb7461331899b33c24a0e9eb690bc0d555e00775086538cd5b8742931a9` |
| `canon/source/2024-2028 Amateur Extra Class Pool Diagrams_Page_3_V2.jpg` | 120,970 | `b67ea1b4109f04b7a9142254e7ec0d944e4a36736f0ed8dce54f9b10abb53ba9` |
| `canon/source/e4_2024-svgs.zip` | 30,740 | `baf46fe88b6914f971f446bfdc1550622d0dcf89d1bfb938ef0dfdcaa85aa558` |
| `canon/source/release-page.html` | 26,364 | `6a18e7265fd62bd39dbd5175eaff90107fe6eab5f365b7e24db3b5fc51a1d2f5` |

The canonical document is the **4th-errata release** ("2024-2028 Extra Class Question Pool and Syllabus Public Release with 4th Errata Feb 4 2026"), the file at the top of the release page; its front matter carries all four errata sheets in full and the pool body already incorporates every change (verified during ingestion). The 3rd-errata release is kept as the pre-4th baseline: re-parsed with the same strict parser (600 active + 3 deleted placeholders, 0 anomalies), it differs from the 4th only by the removal of E4D05, with **zero content differences among the 599 common questions** and all 60 subelement/group heading lines identical. `release-page.html` is the fetched release page itself — the errata-ledger and public-domain-statement source (including the "G8C" misprint, §1.3).

**Pool figures (10 graphics, all obtained):** the Extra pool ships ten figures — E5-1, E6-1, E6-2, E6-3, E7-1, E7-2, E7-3, E9-1, E9-2, E9-3 — published in three independent forms, all downloaded: the figures PDF (`Extra_Figures_2024-2028-1.pdf`, 3 pages), three JPG diagram pages (page 1: E5-1/E6-1/E6-2/E6-3; page 2: E7-1/E7-2/E7-3/E9-1; **page 3 is the "V2" file**: E9-2/E9-3 — the re-issue incorporating the 1st-errata Smith-chart rotation), and `e4_2024-svgs.zip` (all ten figures as SVG; each file verified as well-formed XML). The .docx embeds the same ten graphics as PNG media. All three forms were inspected; **E9-3 is confirmed in its post-errata form** — the Smith chart in conventional horizontal orientation, **infinity on the right**, 0 on the left.

Extraction and cross-check (full evidence in `canon/ingestion-report.md`): the canonical text was parsed from the `.docx` (logical paragraphs, byte-exact wording; python3 `zipfile` + `ElementTree`, no third-party packages) and independently re-parsed from the `.pdf` with `pdftotext -layout`; the two agreed on all 599 questions, all 2,396 choices, all answer letters, all Part 97 refs, and all 60 headings, with exactly 12 field differences — ten PDF-side hyphen-wrap artifacts plus one PDF-side heading wrap (docx authoritative in each case) and **two genuine content differences**: the published figure-ID typos `Figure E73` (E7G07) and `Figure E92` (E9B04), which the PDF hyphenates as `Figure E7-3`/`Figure E9-2`; the .docx is authoritative and the canonical files carry the typo forms byte-exactly (the JSON `figure` fields carry the real published ids). ARRL hosts no separate copy of this pool (its question-pools page links back to NCVEC, confirmed 2026-07-30), so the docx-vs-pdf double parse is the cross-check of record. Normalization preserved published Unicode punctuation byte-exactly (curly apostrophe U+2019 ×60, curly quotes U+201C/U+201D ×16 each — the only non-ASCII characters in the pool text; the headings are pure ASCII) and the published ID-line and choice-label forms verbatim (all 2,396 choice lines are published in the exact form `L. text` — no choice-label quirks in this pool, and no trailing-space ID-line quirk either; contrast the General pool's G2E02/G9C01). The only whitespace normalization applied anywhere is paragraph-edge stripping: E1C12's entire block (ID line, question, 4 choices, `~~`, plus two blank lines) carried a leading **double tab** in the .docx, and 20 pool-body paragraphs carried a single trailing space — edges, never content. Interior whitespace is untouched, including the published **double space inside E8B04's question** ("…modulating frequency  is 2 kHz…") and `A. - 43 dB` (**E1C10** choice A, interior space after the minus sign — mis-attributed to E1B03 in the ingestion report; see §7.9). None of these quirks is ever "fixed" in quotation (§1.5).

### 1.3 Structure, counts, and revision record

- **Total: 599 active questions** (603 published IDs minus 4 withdrawn), 10 subelements (E1–E9, E0), **50 groups**. No duplicate ids; document order == canonical pool order; every question has exactly 4 choices A–D and one keyed answer (answer-letter sanity: A×150, B×150, C×150, D×149). Group letters run E1 A–F, E2 A–E, E3 A–C, E4 A–E, E5 A–D, E6 A–F, **E7 A–H**, E8 A–D, **E9 A–H**, E0 A — the letter class reaches **H** (E7/E9), which the build audit's `E\d[A-H]\d\d` id regex already accommodates.
- **The exam: 50 questions, one drawn from each of the 50 groups; 37 correct answers required to pass** (47 CFR §97.503(c); pool structure per canonical counts). Print "**37 of 50**" as the authoritative figure — the rule pins the count ("The minimum passing score is 37 questions answered correctly"), not a percentage; "74%" is derived arithmetic and is flagged as such wherever it appears (§7.4).
- **Validity: exams from 2024-07-01 through 2028-06-30. THIS POOL EXPIRES MID-2028.** The successor Extra pool takes effect 2028-07-01 (four-year rotation: Technician 2026–2030, General 2023–2027, Extra 2024–2028; no pools updated or released in 2025 or 2029). Every printing, chapter, exam product, and web page derived from this book must state the 2024–2028 validity window; any printing after mid-2028 must state which pool exams actually use. The contained-swap procedure for the successor pool is pinned in §7.11.
- **Public domain:** the NCVEC Question Pool Committee released the 2024–2028 Extra (Element 4) pool into the public domain — "The NCVEC Question Pool Committee hereby releases into public domain the 2024-2028 Element 4 Extra Class Question Pool," stated twice on the release page (captured in `canon/source/release-page.html`, fetched 2026-07-30). Initial release 2023-12-07 (603 questions); the current document is the 4th-errata release of 2026-02-04.
- **Errata ledger (all four; from the document's front-matter errata sheets, cross-checked against the release page):**

| Errata | Issued | Changes |
|---|---|---|
| Errata 1 | 2024-01-31 | **Diagram E9-3 (Smith chart) rotated 90°** to the conventional horizontal orientation, infinity on the right; all pool documents (PDF, JPG, Word) updated. 5 questions modified: E1D07 ("group of"→"of the following"), E1F03 (answer D replaced), E4D12 ("100 W"→"10 W"), E4D13 ("100 W"→"10 W"), E6A06 (answer B gains "The change in"). Citation-only fixes: E1E10 → `[97.509(m)]`, E1E11 → `[97.509(i)]`. **1 withdrawn: E9E10** (E9E not renumbered, 10 remain). |
| 2nd errata | 2024-11-08 | **1 withdrawn: E2A13** (E2A not renumbered, 12 remain). |
| 3rd errata | 2025-09-24 (release page) / sheet dated 2025-09-25 | **1 withdrawn: E6D07** ("more than one correct answer"; E6D not renumbered, 11 remain). |
| 4th errata | 2026-02-04 | **1 withdrawn: E4D05** (E4D not renumbered, 13 remain). |

All five published text modifications and both citation fixes (errata 1) were verified present in the final pool text byte-exactly during ingestion. There is **no 5th errata** as of 2026-07-30 (release page and document front matter agree exactly); re-check the release page before each reprint.

- **The four deleted IDs: E9E10, E2A13, E6D07, E4D05.** Numbering rule (binding): IDs are contiguous within every group from 01 up **except exactly these deletions** — the questions were withdrawn without renumbering, each printed in the source as `EnX## Question Deleted (section not renumbered)` (E9E10's placeholder carries a double space; the other three a single space — placeholders are not carried into the canonical files). Three of the four leave an interior numbering gap; **E2A13 leaves no gap** because it was the last question of E2A (the group now ends at E2A12) and is known only from the deleted placeholder and the errata sheets. The canonical files carry the active pool only; **deleted questions are never quoted, taught, or referenced as exam content anywhere in the book** — they appear only as numbering gaps and in this ledger.
- **Syllabus reconciliation:** the syllabus printed in the final document claims E1:68, E2:61, E3:39, E4:64, E5:49, E6:68, E7:99, E8:48, E9:94, E0:12 (sum 602). Seven subelements match the parse exactly; the printed **E2 (61), E4 (64), and E9 (94) counts are stale** — not updated for the 2nd (E2A13), 4th (E4D05), and 1st (E9E10) errata withdrawals respectively (the bodies hold 60, 63, 93). The per-group active counts match each errata sheet's own "leaving N questions" statements exactly. The parse, not the syllabus, is authoritative (§7.9).
- **Published quirks cataloged (never propagated, never repaired):** the release page's 2nd-errata note reads "The remaining questions in **G8C** were not renumbered, leaving 15 questions" — the affected group is of course **E2A** (12 remain); "G8C/15" is a copy-paste slip from the General pool's 5th errata, a quirk of the *page* (the document's own errata sheet correctly says E2A). Also: the release page gives the 3rd errata's release date as September 24, 2025 while the document sheet and file names say September 25, 2025 — both dates are recorded in the ledger above.

Per-subelement counts (exam weight = one question per group; titles as published, plain hyphens preserved):

| Subelement | Title (as published) | Questions | Groups | Per-group counts | Exam questions |
|---|---|---:|---:|---|---:|
| E1 | COMMISSION RULES | 68 | 6 | E1A:11 E1B:11 E1C:12 E1D:12 E1E:11 E1F:11 | 6 |
| E2 | OPERATING PROCEDURES | 60 | 5 | E2A:12 E2B:12 E2C:12 E2D:11 E2E:13 | 5 |
| E3 | RADIO WAVE PROPAGATION | 39 | 3 | E3A:14 E3B:13 E3C:12 | 3 |
| E4 | AMATEUR PRACTICES | 63 | 5 | E4A:11 E4B:11 E4C:14 E4D:13 E4E:14 | 5 |
| E5 | ELECTRICAL PRINCIPLES | 49 | 4 | E5A:13 E5B:12 E5C:12 E5D:12 | 4 |
| E6 | CIRCUIT COMPONENTS | 68 | 6 | E6A:12 E6B:11 E6C:11 E6D:11 E6E:12 E6F:11 | 6 |
| E7 | PRACTICAL CIRCUITS | 99 | 8 | E7A:11 E7B:12 E7C:11 E7D:15 E7E:11 E7F:14 E7G:12 E7H:13 | 8 |
| E8 | SIGNALS AND EMISSIONS | 48 | 4 | E8A:11 E8B:11 E8C:15 E8D:11 | 4 |
| E9 | ANTENNAS AND TRANSMISSION LINES | 93 | 8 | E9A:12 E9B:11 E9C:14 E9D:12 E9E:10 E9F:12 E9G:11 E9H:11 | 8 |
| E0 | SAFETY - | 12 | 1 | E0A:12 | 1 |
| **Total** | | **599** | **50** | | **50** |

(Published heading casing quirk, preserved: E0's subelement banner reads `SUBELEMENT E0 - SAFETY - [1 exam question - 1 group]` — trailing hyphen and lowercase bracket where the other nine read `[6 Exam Questions - 6 Groups]`.)

### 1.4 The ten pool figures (28 questions) and the redraw rule

Twenty-eight questions reference the pool's ten graphics (§1.2); the other 571 carry `"figure": null`. All references are capitalized "Figure" where the word appears, with three published phrasing quirks preserved byte-exactly and never repaired: **E7G02 prints "the circuit in E7-3"** (no "Figure"), **E7G07 prints "Figure E73"** (missing hyphen), **E9B04 prints "Figure E92"** (missing hyphen) — the latter two are genuine docx-vs-pdf content differences (§1.2). E5C10/E5C12 print "point **on** Figure E5-1" while E5C11 prints "point **in** Figure E5-1" — the on/in difference is published and preserved. The book **redraws every figure as an original SVG conveying exactly the official content — same components, same labels, same numbered positions — never copies the published graphic**. Each redraw is registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure EX-N". The pool is public domain, so this is both safe and faithful; the redraw rule exists so the book's visual style stays consistent and themeable. All pool figures are black line-art on white; each figure title "Figure EX-N" is centered above its drawing (E5-1's title placement per the published art). In the published art the ground symbols are classic three-stroke shrinking horizontal lines; the book may substitute its slanted-stroke house style (content-neutral, as in the earlier books' redraws).

The binding specifications below are r3's and r4's close reads of the published graphics (PDF rendered at 300 dpi with close-up crops of every symbol and label, cross-checked against the SVG set in `canon/source/e4_2024-svgs.zip`; every keyed answer on a figure question was re-derived from the drawing itself). **Question→position maps are binding** for the Exam Focus blocks of the owning chapters (§5).

#### Figure E5-1 — rectangular-coordinate impedance chart (3 questions: E5C10, E5C11, E5C12) → ch05

**What it is:** a rectangular-coordinate **impedance graph — not a circuit schematic** (the R, L, and C live in the questions; the figure is the plane on which the computed impedance is plotted — any early framing of E5-1 as an R-L-C circuit figure is wrong; see §7.5). Verified three ways: `canon/source/e4_2024-svgs.zip → E5-1.svg` (authoritative vector, viewBox 276×277; chart origin at SVG (138.2, 146.9); scale ≈ 0.164 units/ohm horizontal, ≈ 0.160 vertical), page 1 of `Extra_Figures_2024-2028-1.pdf`, and Diagrams_Page_1.jpg.

- **Frame:** square plot box; bold X and Y axes through the origin extending slightly past the box; axis tips labeled "+X" (right), "−X" (left), "+Y" (top), "−Y" (bottom); title "Figure E5-1" centered above.
- **Scales:** both axes −600 to +600 ohms; numeric tick labels every 100 Ω (X below the horizontal axis, Y left of the vertical axis); light gridlines every 200 Ω. Horizontal = resistance R, vertical = reactance jX (per pool E5C09; the figure itself carries only the ±X/±Y tip labels, no R/jX axis titles).
- **Eight points** (small filled dots, each labeled "Point N"): Point 1 (+300, −400); Point 2 (+400, +300); Point 3 (+300, +400); Point 4 (+400, −300); Point 5 (−400, −300); Point 6 (+400, ≈0 — dot on the +X axis, the SVG puts it a hair below at ≈ −10 Ω); Point 7 (−300, −400); Point 8 (+300, ≈0 — dot on the +X axis, the SVG puts it a hair above at ≈ +30 Ω).
- **Question→position map:** E5C10 (400 Ω + 38 pF at 14 MHz → X_C ≈ 300 → 400−j300) → **Point 4** (keyed B); E5C11 (300 Ω + 18 µH at 3.505 MHz → X_L ≈ 400 → 300+j400) → **Point 3** (keyed B); E5C12 (300 Ω + 19 pF at 21.2 MHz → X_C ≈ 400 → 300−j400) → **Point 1** (keyed A). All keyed points sit in the right half-plane; the negative-resistance points (5, 7 — impossible for a passive series circuit, so any answer naming them is auto-wrong) and the on-axis points (6, 8) exist purely as distractors.
- **Redraw checklist:** square frame, axis tips ±X/±Y, both axes −600…+600 with 100 Ω ticks and 200 Ω gridlines, the eight labeled dots at the coordinates above. Watch the notation collision in teaching: the figure's axis tips "+X/−X/+Y/−Y" name *coordinate axes*, while E5C09's "X" names *reactance* — the horizontal axis is resistance; capacitive points plot in the lower half.

#### Figure E6-1 — six FET schematic symbols (2 questions: E6A10, E6A11) → ch06

**Overall:** grid of 6 circled transistor symbols, 2 rows × 3 columns, each numbered beneath (top row 1, 2, 3; bottom row 4, 5, 6). Gate lead(s) enter from the left labeled G (G2 over G1 on the dual-gate parts); drain exits top-right labeled D; source exits bottom-right labeled S. Every symbol: a circle enclosing a vertical channel bar; D and S connect to the top and bottom of that bar.

- **1** — JFET: single gate line from G ending in a filled arrowhead pointing AWAY from the channel (arrow points left, out of the device) = **P-channel junction FET**. Asked by E6A11 (keyed).
- **2** — MOSFET: gate separated from the channel bar by a gap (insulated gate; the L-shaped gate line runs parallel to the bar without touching); internal arrow on the substrate/source connection points IN toward the channel; a connection dot ties the internal source node to the S lead = **N-channel single-gate MOSFET**.
- **3** — same construction as 2 but the internal arrow points OUT (away from the channel) = **P-channel single-gate MOSFET**.
- **4** — like 2 but with TWO insulated gate lines on the left labeled G2 (top) and G1 (bottom); internal arrow points IN = **N-channel dual-gate MOSFET**. Asked by E6A10 (keyed).
- **5** — like 4 (G2 over G1) with the internal arrow pointing OUT = **P-channel dual-gate MOSFET**.
- **6** — JFET: single gate line with a filled arrowhead pointing INTO the channel (arrow points right) = **N-channel junction FET**.

**Question→position map:** E6A10 (N-channel dual-gate MOSFET) → **4**; E6A11 (P-channel junction FET) → **1**. Option pools: E6A10 {2, 4, 5, 6}; E6A11 {1, 2, 3, 6}. **Teaching strategy (binding for ch06):** drill the three independent discriminators — (1) JFET vs MOSFET: the JFET's arrow sits ON the gate lead (1, 6); the MOSFET's gate is insulated and the arrow is internal on the source/substrate (2–5); (2) arrow-in = N-channel, arrow-out = P-channel; (3) dual-gate = G1/G2 labels (4, 5). With those three rules every option in both questions resolves mechanically.

#### Figure E6-2 — eight diode symbols (1 question: E6B10) → ch06

**Overall:** grid of 8 symbols, 2 rows × 4 columns, numbered beneath (top row 1–4, bottom row 5–8). All are horizontal two-lead devices: a filled triangle against a cathode bar unless noted.

- **1** — diode with a separate curved (bowed) line sweeping across the triangle near the cathode, like a second capacitor plate (varactor-style symbol).
- **2** — two diode triangles point-to-point sharing a central T-shaped double bar (bidirectional / back-to-back pair).
- **3** — diode whose cathode bar carries angled hooks bent at BOTH ends (the "Z" wings) = Zener-style symbol.
- **4** — plain junction diode (triangle + straight bar).
- **5** — diode with two small arrows pointing away, upward-right (light leaving) = LED.
- **6** — diode whose cathode-bar ends bend back in squared S-hooks (a hook at each end curling back toward the bar) = **Schottky diode**.
- **7** — diode inside a circle, with an angled external lead ("whisker") entering the circle from the upper right and touching the cathode region (point-contact-style device).
- **8** — circle enclosing TWO opposed diodes (one triangle up, one down, sharing the central bar) plus the same angled whisker lead at upper right.

**Question→position map:** E6B10 (Schottky) → **6**. Options {1, 2, 3, 6}. Only 6 is exam-relevant; 7 and 8 are described structurally because no pool question names them. The distractor set is well chosen: 1 (varactor-style bow), 2 (back-to-back pair), and 3 (Zener wings) all have "something extra on the cathode bar" — the Schottky's tell is the pair of squared S-hooks at both bar ends.

#### Figure E6-3 — six logic gate symbols (3 questions: E6C08, E6C10, E6C11) → ch06

**Overall:** grid of 6 gate symbols, 2 rows × 3 columns, numbered beneath (top row 1–3, bottom row 4–6). Two inputs enter from the left (single input on 5 and 6), one output exits right.

- **1** — flat-left, round-right "D" body, no output bubble = **AND**.
- **2** — same D body WITH a small output bubble = **NAND**.
- **3** — curved-input, pointed-output body, no bubble = **OR**.
- **4** — OR body WITH output bubble = **NOR**.
- **5** — triangle WITH output bubble = **NOT (inverter)**.
- **6** — triangle without bubble (swept sides) = **buffer**.

**Question→position map:** E6C08 (NAND) → **2**; E6C10 (NOR) → **4**; E6C11 (NOT) → **5**. Option pools: E6C08 {1, 2, 3, 4}; E6C10 {1, 2, 3, 4}; E6C11 {2, 4, 5, 6} — E6C11's options deliberately mix bubbles from both families (2, 4) with the triangle pair (5, 6). **Teaching strategy (binding for ch06):** the 2×2 matrix — D-shape = AND family, curved-input = OR family; bubble = negation; triangle = buffer/inverter decided by the bubble.

#### Figure E7-1 — transistor amplifier stage (3 questions: E7B10, E7B11, E7B12) → ch07

**Overall:** single NPN transistor in a circle (emitter arrow pointing outward, down-right — "Not Pointing iN" = NPN). Positive supply rail across the top to an open-circle terminal "+"; signal enters at open-circle "IN" (left) and leaves at open-circle "OUT" (right). Three ground symbols (bottoms of R2, R3, C3).

- **C1** — series coupling capacitor from IN to the base node.
- **R1** — from the + rail down to the base node.
- **R2** — from the base node to ground.
- (unlabeled resistor) — from the + rail to the collector (collector load).
- **C2** — series coupling capacitor from the collector to OUT.
- **R3** — from the emitter to ground.
- **C3** — in parallel with R3 (emitter bypass capacitor, drawn to the right of R3, both tying the emitter node to ground).

**Question→position map:** E7B10 (purpose of R1 and R2) → **voltage divider bias**; E7B11 (purpose of R3) → **self bias** (R3 carries the full emitter current, giving emitter-degeneration self bias; C3 bypasses it for AC only — note E7B11's distractor "emitter bypass" names C3's job, not R3's, the classic misread to warn about); E7B12 (circuit type) → **common emitter** (input at base, output at collector, emitter common to both). Options: E7B10 {load resistors, voltage divider bias, self bias, feedback}; E7B11 {fixed bias, emitter bypass, output load resistor, self bias}; E7B12 {common base, common collector, common emitter, emitter follower}.

#### Figure E7-2 — linear voltage regulator (3 questions: E7D06, E7D07, E7D08) → ch07

**Overall:** left-to-right DC regulator schematic. Open-circle input terminal "+25" (top left); open-circle output terminal "+12" (top right). Ground symbols under C1, C2, D1, C3, R2.

- **C1** — labeled "4000" (electrolytic, one straight one curved plate), input rail to ground (input/brute-force filter).
- **R1** — from the +25 rail down to the base node.
- **Q1** — NPN series-pass transistor in a circle: collector to the +25 rail, emitter to the +12 output rail, base straight down to the base node.
- **C2** — labeled "4000" (electrolytic), from the base node to ground.
- **D1** — Zener diode in a circle (cathode bar with the "Z" wings, pointing up), from the base node to ground; C2 and D1 are in PARALLEL from the base node to ground.
- **C3** — labeled "0.01", output rail to ground.
- **R2** — output rail to ground (the load).

**Question→position map:** E7D06 (purpose of Q1) → **it controls the current to keep the output voltage constant** (series-pass element, NOT a chopper — that's the switching-regulator distractor); E7D07 (purpose of C2) → **it bypasses rectifier-output ripple around D1** (C2 parallels D1, keeping the Zener reference clean); E7D08 (circuit type) → **linear voltage regulator**. Circuit story for the caption: D1 holds the base at its Zener voltage; Q1's emitter follows one B-E drop below it (+12); R1 feeds the Zener from the raw +25; C1/C2 are 4000 (µF implied) electrolytics; C3 0.01 kills output transients; R2 is the load. The same figure's numbers drive E7D13's dissipation math: (25 − 12) V × 1 A = 13 W in Q1 (§2.13).

#### Figure E7-3 — inverting op-amp (5 questions: E7G02, E7G07, E7G09, E7G10, E7G11) → ch07

**Overall:** op-amp triangle pointing right. **R1** from the open-circle input terminal (left) to the inverting (−) input; **RF** feedback resistor from the output back to the − input, drawn across the top; non-inverting (+) input grounded; output to an open-circle terminal at the right; a separate ground symbol sits near the output terminal.

**Question→position map and math (gain law Av = −RF/R1; Vout = −(RF/R1)·Vin):** E7G07 (RF 470 / R1 10) → **47**; E7G09 (−(10,000/1,000) × 0.23 V) → **−2.3 V** (sign matters; +2.3 V is the distractor); E7G10 (68 k/1.8 k = 37.8) → **≈38**; E7G11 (47 k/3.3 k = 14.2) → **≈14**; E7G02 (capacitor added across RF → feedback impedance falls as frequency rises) → **low-pass filter**. All four numeric answers recompute exactly from the drawing's topology. **Stem-typo ledger (preserve byte-exact in quotes):** E7G02 prints "in E7-3" (no "Figure"); E7G07 prints "Figure E73" (missing hyphen). **Teaching strategy (binding for ch07):** one formula answers five questions — the best return-on-formula in the whole pool; compute RF/R1 exactly, because the distractors are arithmetic slips (24, 4700, 76, 28).

#### Figure E9-1 — azimuth radiation pattern, "Free-Space Pattern" (3 questions: E9B01, E9B02, E9B03) → ch09

**Overall:** full-circle polar plot. Angular labels: 0° at right, 30 and 60 upper right, 120 and 150 upper left, 180° at left, −150 and −120 lower left, −60 and −30 lower right (radial spokes every 15°; the top/bottom spokes carry no numerals). Concentric dB rings labeled outer→in: −3, −6, −12, −24; the outer circle is the 0 dB reference. Caption text "Free-Space Pattern" at upper right. A single heavy trace shows the antenna pattern.

**Trace:** main lobe centered on 0°, touching the outer ring and crossing the −3 dB ring at ≈ ±25°; sidelobes near ±50–60° at ≈ −12 dB; deep nulls (below −24 dB) near ±70–80° and flanking the rear; rear lobe at 180° at ≈ −18 dB; trace level at ±90° ≈ −14 dB.

**Question→position map:** E9B01 (3 dB beamwidth) → 2 × 25° = **50°**; E9B02 (front-to-back) → 0 − (−18) = **18 dB**; E9B03 (front-to-side) → **14 dB**. Distractor anatomy: 75°/30°/25° in E9B01 come from reading null-to-null or one-sided widths; 12 dB in E9B03 is the sidelobe level, not the 90° level. **Redraw checklist:** 15° spoke spacing; ring labels −3/−6/−12/−24 stacked near the top; 0° reference at right; the trace's five features (main lobe, two sidelobes, two null pairs, rear lobe) at the bearings above.

#### Figure E9-2 — elevation radiation pattern, "Over Real Ground" (3 questions: E9B04, E9B05, E9B06) → ch09

**Overall:** semicircular polar plot above a horizontal baseline (the ground). Baseline runs 180° (left) to 0° (right); 90° at zenith; labeled radials 0, 30, 60, 90, 120, 150, 180 with finer subdivision spokes (7.5° spacing visible). Concentric dB arcs labeled along the baseline right of center, outer→in: −10, −20, −30, −40; the outer semicircle is 0 dB. Caption text "Over Real Ground" at upper right.

**Trace:** largest lobe hugs the horizon, peaking at ≈ 7.5° elevation and reaching the outer arc; successively smaller lobes at ≈ 22°, ≈ 38°, ≈ 52°; a cluster of small rear lobes toward 150–180° down ≈ −28 to −40 dB.

**Question→position map:** E9B04 (front-to-back) → main lobe 0 dB vs rear ≈ −28 dB = **28 dB** (stem prints "Figure E92" — typo ledger, preserve); E9B05 (pattern type) → **elevation** (the semicircle-above-ground format is the tell; "azimuth" is the distractor); E9B06 (peak elevation angle) → **7.5°** (distractors 45/75/25 read the wrong lobes). **Redraw checklist:** semicircle + baseline; radial labels 0/30/60/90/120/150/180; dB arc labels −40/−30/−20/−10 along the baseline (the published order prints "-40 -30 -20 -10" left to right toward the 0° end); four forward lobes decreasing with angle; small rear-lobe cluster.

#### Figure E9-3 — Smith chart (2 questions: E9G06, E9G07) → ch09

**Overall:** a simplified normalized Smith chart — one large circle, no peripheral wavelength scales. **Infinity (∞) is at the RIGHT end of the horizontal diameter** (the open-circuit point); **0 is at the LEFT end** (short circuit) — this is the post-errata-1 orientation, rotated 90° from the initial release into the conventional horizontal form (the V2 JPG page 3 is the re-issue that incorporates the rotation; §1.3). The horizontal diameter is the chart's only straight line and carries the resistance-circle labels 0, 0.2, 0.5, 1.0, 2.0, 5.0, 20 left→right; the 1.0 point at mid-chart is the prime center (the normalized system impedance, e.g., 50 Ω). Constant-resistance circles are all tangent at the ∞ point, bulging left. Constant-reactance arcs sweep from the rim into the ∞ point, labeled 0.2, 0.5, 1.0, 2.0, 5.0 above the axis (inductive, +jX) and the same magnitudes below (capacitive, −jX); every reactance arc terminates on the large outer circle.

**Question→position map:** E9G06 (name of the large outer circle on which the reactance arcs terminate) → **reactance axis**; E9G07 (the only straight line) → **resistance axis**. The two questions share an option pool ({prime axis, reactance axis, impedance axis, polar axis} / {reactance axis, current axis, voltage axis, resistance axis}), so "reactance axis" is correct in one and a distractor in the other — the naming pair is the whole lesson. **Redraw checklist (the tested features are mandatory):** ∞ at right, 0 at left; resistance labels 0.2–20 ascending left→right along the single straight horizontal axis; reactance arcs terminating on the outer circle with matching +/− magnitudes above/below; prime center at 1.0. **Wavelength scales are absent in the published figure — do not invent them.**

### 1.5 Quoting discipline (audit-enforced)

- Question text, choice text, and answer letters are quoted **only** from the two canonical pool files, byte-exact (the audit compares whitespace-normalized). Published Unicode punctuation (curly apostrophes/quotes) is preserved, never converted to ASCII.
- Chapter and appendix pool quotes use this exact block markup (the audit parses it):

```
> **E1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: D** — one-line why.
```

- Every quoted id must exist in the pool; every stated choice line and the stated answer letter must match the pool key. Appendix A quotes all 599 ids exactly once, in canonical pool order (E1…E9, E0; group A→last; number), skipping exactly the four deleted numbers (§1.3).
- The pool's own published quirks are reproduced as published, never silently repaired: the three figure-stem typos (`the circuit in E7-3`, `Figure E73`, `Figure E92`), the on/in variance between E5C10/E5C12 ("point on Figure E5-1") and E5C11 ("point in Figure E5-1"), the E8B04 interior double space, the E1C10 choice-A `- 43 dB` interior space, and the 66 E1 Part-97 ID-line tags in their published form (including E1A06's superseded `[97.303(h)(1)]` — see §7.1).
- The four deleted questions (§1.3) are never quoted; Appendix A's coverage simply skips the deleted numbers, exactly as the canonical files do.
- Part 97 rule quotations in prose are verbatim from the eCFR **current** text (issue date 2026-07-28, byte-identical to 2026-07-20; pool-era comparisons against the 2024-07-01 issue), pulled 2026-07-30 (research notes r1/r2); re-pull every cited section before any reprint (§7.11). Where a rule quotation is embedded mid-sentence, the initial letter's case and the terminal punctuation may be adjusted to fit the host sentence (standard embedded-quote convention); the quoted words themselves are verbatim from the cited section.

---

## 2. Pinned Facts with Sources

The book's fact reservoir. Each line is `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers copy the sentence **verbatim** into their chapters (the build audit greps each chapter's `**FACT:**` lines for an exact match in this file); a chapter may add explanation around it but may never alter the sentence. Every sentence stands alone, needs no surrounding context to be true, and is safe for an upgrading General to memorize. Rule quotations inside FACT sentences are verbatim from the eCFR current text of 47 CFR Part 97 (issue date 2026-07-28 ≡ 2026-07-20; pool-era comparisons against the 2024-07-01 issue; pre-change §97.307(f) verified at 2023-07-01), pulled 2026-07-30 (research notes r1/r2); re-pull every cited section before any reprint — see §7.11. Where current rule text differs from the pool-era text the 2023 pool was written against, the FACT pins the current text and §7.1/§7.2 carry the difference — the only such hazard areas are 60 m and the post-pool amendments, both resolved below.

### 2.1 Extra-class frequency privileges and the band-edge math (rules)

- **FACT:** The §97.301 frequency bands apply to "an amateur station located within 50 km of the Earth's surface, within the specified ITU Region, and outside any area where the amateur service is regulated by any authority other than the FCC." — Source: 47 CFR §97.301 preamble; pool E1 (section-wide)
- **FACT:** Amateur Extra MF/HF/LF allocations (all-Regions unless noted): 2200 m 135.7–137.8 kHz; 630 m 472–479 kHz; 160 m 1800–2000 kHz (1810–1850 kHz in Region 1); 80 m 3.500–3.600 MHz; 75 m 3.600–4.000 MHz (3.600–3.800 Region 1, 3.600–3.900 Region 3); 60 m 5.3515–5.3665 MHz plus four discrete channels (current text — see §7.1); 40 m 7.000–7.300 MHz (7.000–7.200 Regions 1/3); 30 m 10.100–10.150 MHz; 20 m 14.000–14.350 MHz; 17 m 18.068–18.168 MHz; 15 m 21.000–21.450 MHz; 12 m 24.890–24.990 MHz; 10 m 28.000–29.700 MHz. — Source: 47 CFR §97.301(b) table (current text)
- **FACT:** The Extra-only HF segments (in §97.301(b) but absent from the General table §97.301(d)) are exactly 3.500–3.525 MHz, 3.600–3.800 MHz, 7.000–7.025 MHz, 7.125–7.175 MHz (Region 2), 14.000–14.025 MHz, 14.150–14.225 MHz, 21.000–21.025 MHz, and 21.200–21.275 MHz — Extra-exclusive spectrum exists only on 80, 75, 40, 20, and 15 meters. — Source: 47 CFR §97.301(b) vs §97.301(d); research note r5 §7
- **FACT:** The legacy Advanced class sits between Extra and General: 80 m 3.525–3.600 MHz, 75 m 3.700–4.000 MHz (Region 2), 40 m 7.025–7.300 MHz (Region 2), 20 m 14.025–14.150 and 14.175–14.350 MHz, 15 m 21.025–21.200 and 21.225–21.450 MHz — so the slices exclusive to Extra alone are 3.500–3.525, 3.600–3.700, 7.000–7.025, 14.000–14.025, 14.150–14.175, 21.000–21.025, and 21.200–21.225 MHz, including the DX-heavy bottom of the 20 m phone band. — Source: 47 CFR §97.301(c) table vs §97.301(b)
- **FACT:** "Except as specified elsewhere in this part, an amateur station may transmit a CW emission on any frequency authorized to the control operator." — Source: 47 CFR §97.305(a)
- **FACT:** The §97.305(c)(3) HF emission-segment edges for an Extra control operator are: 75 m phone/image the entire band (3.600–4.000 MHz in Region 2); 40 m RTTY/data 7.000–7.125 MHz and phone/image 7.125–7.300 MHz; 30 m RTTY/data the entire band with no phone and no image; 20 m RTTY/data 14.00–14.15 MHz and phone/image 14.15–14.35 MHz; 15 m RTTY/data 21.0–21.2 MHz and phone/image 21.20–21.45 MHz; 10 m RTTY/data 28.0–28.3 MHz and phone/image 28.3–29.7 MHz. — Source: 47 CFR §97.305(c)(3)(i)–(xx)
- **FACT:** A USB signal occupies roughly carrier to carrier + 3 kHz and an LSB signal roughly carrier − 3 kHz to carrier, and §97.307(b) requires emissions to be "confined to the band or segment available to the control operator" — so a USB carrier at 14.348 MHz with 3 kHz bandwidth puts energy to 14.351 MHz and the upper 1 kHz is outside the 20 m band. — Source: 47 CFR §97.307(b), §97.301(b); pool E1A01
- **FACT:** With a carrier-displaying transceiver, the lowest LSB carrier frequency that keeps the whole signal inside the band is 3 kHz above the lower band edge. — Source: 47 CFR §97.301, §97.305, §97.307(b); pool E1A02
- **FACT:** The 20 m RTTY/data segment ends at 14.15 MHz, so the highest carrier for a 2.8 kHz wide USB data signal there is 14.150 − 0.0028 = 14.1472 MHz. — Source: 47 CFR §97.305(c)(3)(ix), §97.307(b), (f)(3); pool E1A03
- **FACT:** The Extra 75 m phone segment starts at 3.600 MHz, so an LSB carrier displayed at 3.601 MHz puts sideband energy down to about 3.598 MHz — outside the segment — while "not permitted below 3.610 MHz" is false because Extra phone begins at 3.600 MHz. — Source: 47 CFR §97.301(b), §97.305(c)(3)(ii); pool E1A04
- **FACT:** "A station in a secondary service must not cause harmful interference to, and must accept interference from, stations in a primary service." — Source: 47 CFR §97.303 preamble
- **FACT:** Amateur stations transmitting in the 70 cm, 33 cm, 23 cm, 5 cm, or 3 cm bands or the 24.05–24.25 GHz segment "must not cause harmful interference to, and must accept interference from, stations authorized by the United States Government in the radiolocation service" — which is why a 70 cm repeater interfering with radiolocation must cease or mitigate. — Source: 47 CFR §97.303(b); pool E1B04
- **FACT:** "No amateur station shall transmit from north of Line A in the 420-430 MHz segment," and Line A runs roughly parallel to and south of the US–Canada border (it "begins at Aberdeen, WA, running by great circle arc to the intersection of 48° N, 120° W, thence along parallel 48° N, to the intersection of 95° W, thence by great circle arc through the southernmost point of Duluth, MN …"). — Source: 47 CFR §97.303(m)(1), §97.3(a)(30); pool E1F04, E1F05

### 2.2 Special bands, power limits, and stations aboard ships or aircraft (rules)

- **FACT:** "An amateur station must use the minimum transmitter power necessary to carry out the desired communications," and "No station may transmit with a transmitter power exceeding 1.5 kW PEP." — Source: 47 CFR §97.313(a), (b)
- **FACT:** On 2200 m (135.7–137.8 kHz), "No station may transmit in the 135.7-137.8 kHz (2200 m) band with a transmitter power exceeding 1.5 kW PEP or a radiated power exceeding 1 W EIRP." — Source: 47 CFR §97.313(k); pool E1A07 (keyed 1 W EIRP)
- **FACT:** On 630 m (472–479 kHz), "No station may transmit in the 472-479 kHz (630 m) band with a transmitter power exceeding 500 W PEP or a radiated power exceeding 5 W EIRP, except that in Alaska, stations located within 800 kilometers of the Russian Federation may not transmit with a radiated power exceeding 1 W EIRP." — Source: 47 CFR §97.313(l); pool E1A09 (keyed 5 W EIRP "except in some parts of Alaska")
- **FACT:** On 630 m, phone and image emissions are authorized on the entire band 472–479 kHz. — Source: 47 CFR §97.305(c)(2)(ii); pool E1C12 (keyed "The entire band")
- **FACT:** 2200/630 m operation is fixed-location only, and amateurs "shall not operate within a horizontal distance of one kilometer from a transmission line that conducts a power line carrier (PLC) signal" in those bands. — Source: 47 CFR §97.303(g)(1); pool E1C03 context
- **FACT:** Before operating on 2200 or 630 m, operators "shall notify the Utilities Telecom Council (UTC) of their intent to operate by submitting their call signs, intended band or bands of operation, and the coordinates of their antenna's fixed location," and may commence operations after the 30-day period unless UTC warns the location is within one kilometer of PLC systems on the same or overlapping frequencies. — Source: 47 CFR §97.303(g)(2) (rule text prints "Utilities Telecom Council"; the pool prints "Utilities Technology Council" — see §7.7); pool E1C03 (keyed 30 days / 1 km), E1C07 (keyed UTC + call sign + coordinates)
- **FACT:** "Antennas used to transmit in the 2200 m and 630 m bands must not exceed 60 meters in height above ground level." — Source: 47 CFR §97.15(c)
- **FACT:** Current 60 m text: "In the 5330.5-5406.4 kHz band (60 m band), amateur stations may transmit only in the 5351.5-5366.5 kHz band and on the four center frequencies specified in the table below" — centers 5332, 5348, 5373, and 5405 kHz — and "for CW emissions (emission designator 150HA1A), the carrier frequency is set to the center frequency." — Source: 47 CFR §97.303(h)(3) (current; pool E1A06's keyed answer "at the center frequency of the channel" remains correct — see §7.1)
- **FACT:** Current 60 m power: "No station may transmit on the frequencies 5.332, 5.348, 5.373, and 5.405 MHz in the 60 m band with a radiated power exceeding 100 W ERP. No station may transmit in the 5.3515-5.3665 MHz band with a radiated power exceeding 9.15 W ERP." — Source: 47 CFR §97.313(i) (amended effective 2026-01-14; not tested by E1 — see §7.1)
- **FACT:** "The installation and operation of an amateur station on a ship or aircraft must be approved by the master of the ship or pilot in command of the aircraft." — Source: 47 CFR §97.11(a); pool E1A10
- **FACT:** Any holder of an FCC amateur operator/primary station grant (or §97.107 alien reciprocal authority) may be the control operator of an amateur station aboard a US-documented vessel or craft, within 50 km of the Earth's surface or above it — Part 97 has no special ship or aircraft endorsement. — Source: 47 CFR §97.5(a), (c); pool E1A05, E1A11
- **FACT:** The shipboard or aircraft amateur station "must be separate from and independent of all other radio apparatus installed on the ship or aircraft, except a common antenna may be shared with a voluntary ship radio installation," and it must not constitute a hazard to safety of life or property. — Source: 47 CFR §97.11(b), (c)

### 2.3 Emission standards (rules)

- **FACT:** A spurious emission is "an emission, or frequencies outside the necessary bandwidth of a transmission, the level of which may be reduced without affecting the information being transmitted" — the definition contains no dB figure. — Source: 47 CFR §97.3(a)(43); pool E1B01
- **FACT:** Bandwidth (necessary bandwidth) is "the width of a frequency band outside of which the mean power of the transmitted signal is attenuated at least 26 dB below the mean power of the transmitted signal within the band." — Source: 47 CFR §97.3(a)(8)
- **FACT:** "No amateur station transmission shall occupy more bandwidth than necessary for the information rate and emission type being transmitted, in accordance with good amateur practice." — Source: 47 CFR §97.307(a)
- **FACT:** For transmitters installed after January 1, 2003 and operating below 30 MHz, "the mean power of any spurious emission from a station transmitter or external RF power amplifier transmitting on a frequency below 30 MHz must be at least 43 dB below the mean power of the fundamental emission." — Source: 47 CFR §97.307(d); pool E1C10 (keyed −43 dB, printed "- 43 dB")
- **FACT:** Between 30 and 225 MHz the spurious limit is "at least 60 dB below the mean power of the fundamental," with transmitters of mean power up to 25 W instead held to spurious at the antenna line of no more than 25 µW and at least 40 dB down, "but need not be reduced below the power of 10 µW." — Source: 47 CFR §97.307(e)
- **FACT:** "No angle-modulated emission may have a modulation index greater than 1 at the highest modulation frequency." — Source: 47 CFR §97.307(f)(1); pool E1C09 (keyed 1.0 — the standard applies where (f)(1) is cited, the phone/image segments below 29 MHz)
- **FACT:** "No non-phone emission shall exceed the bandwidth of a communications quality phone emission of the same modulation type" — which is why about 3 kHz is an acceptable bandwidth for HF digital voice or SSTV. — Source: 47 CFR §97.307(f)(2); pool E1B02
- **FACT:** The current HF data standard: "Only a RTTY or data emission using a specified digital code listed in § 97.309(a) may be transmitted. The authorized bandwidth is 2.8 kHz except in the 2200 m band and 630 m band. In the 2200 m band and the 630 m band the symbol rate must not exceed 300 bauds, or for frequency-shift keying, the frequency shift between mark and space must not exceed 1 kHz." — Source: 47 CFR §97.307(f)(3) ((f)(4) is Reserved; the pre-December-2023 300-baud/1200-baud caps were replaced by 88 FR 85127 before the pool was written — see §7.2)
- **FACT:** The VHF data standard is a symbol rate of at most 19.6 kilobauds and authorized bandwidth 20 kHz, and the UHF-and-up standard is at most 56 kilobauds and 100 kHz. — Source: 47 CFR §97.307(f)(5), (f)(6)
- **FACT:** On 60 meters (current text): "A station may transmit only phone, RTTY, data, and CW emissions. RTTY or data emissions must meet the digital code specifications listed in § 97.309. Emissions must not exceed a bandwidth of 2.8 kilohertz." — Source: 47 CFR §97.307(f)(14)(i); pool E1C01 (keyed 2.8 kHz, correct under both pool-era and current text — see §7.1)
- **FACT:** A station transmitting RTTY/data using a specified digital code "may use any technique whose technical characteristics have been documented publicly, such as CLOVER, G-TOR, or PacTOR, for the purpose of facilitating communications," while unspecified codes "must not be transmitted for the purpose of obscuring the meaning of any communication." — Source: 47 CFR §97.309(a)(4), (b)
- **FACT:** Spread spectrum first appears in the §97.305(c) table at the 1.25 m row (222–225 MHz) and then in every UHF/SHF/EHF row — SS is authorized only on amateur frequencies above 222 MHz, never on 6 m or 2 m. — Source: 47 CFR §97.305(c)(4)(v), (c)(5)–(7); pool E1F01
- **FACT:** Spread-spectrum transmissions are authorized "only for communications between points within areas where the amateur service is regulated by the FCC" (plus countries that permit SS), "must not be used for the purpose of obscuring the meaning of any communication," and "No station may transmit with a transmitter output exceeding 10 W PEP when the station is transmitting a SS emission type." — Source: 47 CFR §97.311(a)–(c), §97.313(j)

### 2.4 Special operations: location restrictions, auxiliary, repeater, beacon, space, Earth, telecommand, automatic digital (rules)

- **FACT:** "A station within 1600 m (1 mile) of an FCC monitoring facility must protect that facility from harmful interference," on pain of operating restrictions under §97.121. — Source: 47 CFR §97.13(b); pool E1B03 (keyed 1 mile)
- **FACT:** "Owners of certain antenna structures more than 60.96 meters (200 feet) above ground level at the site or located near or at a public use airport must notify the Federal Aviation Administration and register with the Commission as required by part 17 of this chapter." — Source: 47 CFR §97.15(a); pool E1B06
- **FACT:** "State and local regulation of a station antenna structure must not preclude amateur service communications. Rather, it must reasonably accommodate such communications and must constitute the minimum practicable regulation to accomplish the state or local authority's legitimate purpose. See PRB-1, 101 FCC 2d 952 (1985) for details." — Source: 47 CFR §97.15(b); pool E1B07 (keyed "state and local zoning"), E1B11 (PRB-1 binds state/local regulation only, not homeowners' associations — see §7.6)
- **FACT:** If an amateur station causes general interference to domestic broadcast reception "when receivers of good engineering design … are used," it "shall not be operated during the hours from 8 p.m. to 10:30 p.m., local time, and on Sunday for the additional period from 10:30 a.m. until 1 p.m., local time, upon the frequency or frequencies used when the interference is created" — quiet hours on the interfering frequencies, not a full ban. — Source: 47 CFR §97.121(a); pool E1B08
- **FACT:** The National Radio Quiet Zone is "the area in Maryland, Virginia and West Virginia Bounded by 39°15′ N on the north, 78°30′ W on the east, 37°30′ N on the south and 80°30′ W on the west" — it surrounds the National Radio Astronomy Observatory at Green Bank, WV, and an automatically controlled beacon there requires written notification to the NRAO Interference Office. — Source: 47 CFR §97.3(a)(33), §97.203(e); pool E1B05
- **FACT:** "Any amateur station licensed to a holder of a Technician, General, Advanced or Amateur Extra Class operator license may be an auxiliary station," and such a holder "may be the control operator of an auxiliary station, subject to the privileges of the class of operator license held." — Source: 47 CFR §97.201(a); pool E1F10 (Technician or higher — "General or higher" is the trap)
- **FACT:** "An auxiliary station may transmit only on the 2 m and shorter wavelength bands, except the 144.0-144.5 MHz, 145.8-146.0 MHz, 219-220 MHz, 222.00-222.15 MHz, 431-433 MHz, and 435-438 MHz segments"; it "may be automatically controlled" and "may transmit one-way communications." — Source: 47 CFR §97.201(b), (d), (e)
- **FACT:** A repeater may operate only on the 10 m and shorter wavelength bands except the 28.0–29.5, 50.0–51.0, 144.0–144.5, 145.5–146.0, 222.00–222.15, 431.0–433.0, and 435.0–438.0 MHz segments; "A repeater may be automatically controlled"; and "the control operator of a repeater that retransmits inadvertently communications that violate the rules in this part is not accountable for the violative communications." — Source: 47 CFR §97.205(b), (d), (g)
- **FACT:** A beacon's transmitter power "must not exceed 100 W," automatic control is permitted only on 28.20–28.30, 50.06–50.08, 144.275–144.300, 222.05–222.06, 432.300–432.400 MHz or the 33 cm and shorter bands, and "a beacon may transmit one-way communications." — Source: 47 CFR §97.203(c), (d), (g)
- **FACT:** "A space station must be capable of effecting a cessation of transmissions by telecommand whenever such cessation is ordered by the FCC." — Source: 47 CFR §97.207(b)
- **FACT:** Space-station authorized frequencies are "the 17 m, 15 m, 12 m, and 10 m bands, 6 mm, 4 mm, 2 mm and 1 mm bands; and … the 7.0-7.1 MHz, 14.00-14.25 MHz, 144-146 MHz, 435-438 MHz, 2400-2450 MHz, 5.83-5.85 GHz, 10.45-10.50 GHz, and 24.00-24.05 GHz segments" — so among the pool's choices the fully authorized HF set is 40/20/15/10 m (the WARC bands are excluded as segments), the only listed VHF band is 2 m, and the listed UHF bands are 70 cm and 13 cm (33 cm is not listed). — Source: 47 CFR §97.207(c); pool E1D07 (keyed 40/20/15/10 m), E1D08 (keyed 2 m), E1D09 (keyed 70 cm and 13 cm)
- **FACT:** "A space station may transmit one-way communications," may "automatically retransmit the radio signals of Earth stations and other space stations," and space telemetry "may consist of specially coded messages intended to facilitate communications or related to the function of the spacecraft." — Source: 47 CFR §97.207(d), (e), (f)
- **FACT:** "Any amateur station may be an Earth station. A holder of any class operator license may be the control operator of an Earth station, subject to the privileges of the class of operator license held by the control operator." — Source: 47 CFR §97.209(a); pool E1D11
- **FACT:** "Any amateur station designated by the licensee of a space station is eligible to transmit as a telecommand station for that space station, subject to the privileges of the class of operator license held by the control operator." — Source: 47 CFR §97.211(a); pool E1D10
- **FACT:** "A telecommand station may transmit special codes intended to obscure the meaning of telecommand messages to the station in space operation" — the only amateur transmission lawfully encrypted. — Source: 47 CFR §97.211(b); pool E1D02
- **FACT:** One-way transmissions are the province of space, beacon, and telecommand stations. — Source: 47 CFR §97.207(e), §97.203(g), §97.211(d); pool E1D12
- **FACT:** Telecommand of a station on or within 50 km of the Earth's surface requires a radio or wireline control link (a radio control link must use an auxiliary station), provisions "to limit transmission by the station to a period of no more than 3 minutes in the event of malfunction in the control link," protection against unauthorized transmissions, and a photocopy of the station license plus a label with the licensee's name, address, and telephone number and at least one designated control operator posted conspicuously at the station location. — Source: 47 CFR §97.213(a)–(d); pool E1C08 (keyed 3 minutes), E1D05 (keyed "all these choices")
- **FACT:** Model-craft telecommand needs no station ID for transmissions directed only to the model craft if a call-sign/licensee label is affixed to the transmitter, the control signals are not codes or ciphers, and "the transmitter power must not exceed 1 W." — Source: 47 CFR §97.215(a)–(c); pool E1D06
- **FACT:** "Telemetry transmitted by an amateur station on or within 50 km of the Earth's surface is not considered to be codes or ciphers intended to obscure the meaning of communications," and telemetry is "a one-way transmission of measurements at a distance from the measuring instrument." — Source: 47 CFR §97.217, §97.3(a)(46); pool E1D01
- **FACT:** A space telecommand station is "an amateur station that transmits communications to initiate, modify or terminate functions of a space station" — the pool deliberately swaps this against the telemetry definition. — Source: 47 CFR §97.3(a)(45); pool E1D03
- **FACT:** "Each amateur station, except a space station or telecommand station, must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication" — so a balloon-borne telemetry station (within 50 km of Earth, hence not a space station) must ID with its call sign. — Source: 47 CFR §97.119(a); pool E1D04
- **FACT:** In a message-forwarding system, "the control operator of the station originating a message is primarily accountable for any violation of the rules in this part contained in the message"; forwarding stations that inadvertently retransmit violations are not accountable, except the first forwarding station must authenticate the sender or accept accountability. — Source: 47 CFR §97.219(b)–(d); pool E1A08
- **FACT:** Automatically controlled digital stations may transmit RTTY or data on the 6 m and shorter wavelength bands and on the 28.120–28.189, 24.925–24.930, 21.090–21.100, 18.105–18.110, 14.0950–14.0995, 14.1005–14.112, 10.140–10.150, 7.100–7.105, and 3.585–3.600 MHz segments; elsewhere a station may be automatically controlled only when "responding to interrogation by a station under local or remote control" with bandwidth no more than 500 Hz. — Source: 47 CFR §97.221(a)–(c); pool E1C05 (citation half)
- **FACT:** "No station may transmit third party communications while being automatically controlled except a station transmitting a RTTY or data emission." — Source: 47 CFR §97.115(c); pool E1C05 (keyed answer)
- **FACT:** External RF power amplifiers manufactured or imported for amateur use "must be certificated for use in the amateur service in accordance with subpart J of part 2," and "no amplifier capable of operation below 144 MHz may be constructed or modified by a non-amateur service licensee without a grant of certification from the FCC" — but certification is not required if "the amplifier is constructed or modified by an amateur radio operator for use at an amateur station." — Source: 47 CFR §97.315(a), (b)(1); pool E1F03 (pool-era §97.315(b)(2) is now Reserved — see §7.2)
- **FACT:** Amplifier certification standards include satisfying the §97.307(d) or (e) spurious standards "when the amplifier is operated at the lesser of 1.5 kW PEP or its full output power and when the amplifier is placed in the 'standby' or 'off' positions while connected to the transmitter," gain of no more than 15 dB, and no amplification (0 dB gain) between 26 MHz and 28 MHz. — Source: 47 CFR §97.317(a)(1)–(3); pool E1F11
- **FACT:** Special Temporary Authority under §1.931 is the FCC's general Wireless Telecommunications Services mechanism for "immediate or temporary use of station," filed electronically at least 10 days before proposed operation — the provision never mentions the amateur service, and the pool keys STA "to provide for experimental amateur communications" on FCC practice, not amateur-specific rule text. — Source: 47 CFR §1.931(a)(1); pool E1F06 (see §7.6)

### 2.5 RACES, emergency, international, reciprocal, and third-party (rules)

- **FACT:** "No station may transmit in RACES unless it is an FCC-licensed primary, club, or military recreation station and it is certified by a civil defense organization as registered with that organization. No person may be the control operator of an amateur station transmitting in RACES unless that person holds a FCC-issued amateur operator license and is certified by a civil defense organization as enrolled in that organization." — Source: 47 CFR §97.407(a); pool E1B09
- **FACT:** "The frequency bands and segments and emissions authorized to the control operator are available to stations transmitting communications in RACES on a shared basis with the amateur service"; only if the President's War Emergency Powers (47 U.S.C. 606) are invoked are RACES stations confined to segments authorized under Part 214. — Source: 47 CFR §97.407(b); pool E1B10
- **FACT:** RACES stations may communicate only upon authorization of the responsible civil defense official, with amateur stations registered with the same or another civil defense organization and with FCC-regulated services when authorized by the FCC, carrying messages concerning public safety and national defense during emergencies and relief. — Source: 47 CFR §97.407(c), (d)
- **FACT:** "No provision of these rules prevents the use by an amateur station of any means of radiocommunication at its disposal to provide essential communication needs in connection with the immediate safety of human life and immediate protection of property when normal communication systems are not available." — Source: 47 CFR §97.403 (stations in distress may use any means to attract attention, §97.405; Alaska stations may use J3E/R3E on 5.1675 MHz for emergency communications at up to 150 W PEP, §97.401)
- **FACT:** Canadian-licensed operators in the US operate under the US–Canada Convention (TIAS No. 2508), "the operating terms and conditions of the amateur service license issued by the Government of Canada," and Part 97, "but not to exceed the control operator privileges of an FCC-granted Amateur Extra Class operator license" — the same ceiling applies to other reciprocal countries. — Source: 47 CFR §97.107(a)–(c); pool E1F02
- **FACT:** "Transmissions to a different country, where permitted, shall be limited to communications incidental to the purposes of the amateur service and to remarks of a personal character." — Source: 47 CFR §97.117; pool E1C02
- **FACT:** Third-party messages to foreign stations are allowed only where the foreign administration "has made arrangements with the United States to allow amateur stations to be used for transmitting international communications on behalf of third parties," or for emergency or disaster relief — and the prohibition never applies to a message for a third party eligible to be the station's control operator. — Source: 47 CFR §97.115(a)(2)
- **FACT:** A CEPT radio amateur license is "a license issued by a country belonging to the European Conference of Postal and Telecommunications Administrations (CEPT) that has adopted Recommendation T/R 61-01 (Nice 1985, Paris 1992, Nicosia 2003)" — the arrangement that lets US amateurs operate in many European countries and vice versa. — Source: 47 CFR §97.3(a)(12); pool E1C11 (keyed CEPT)
- **FACT:** An IARP is "a document issued pursuant to the terms of the Inter-American Convention on an International Amateur Radio Permit by a country signatory to that Convention, other than the United States. Montrouis, Haiti. AG/doc.3216/95" — a permit for operation in certain countries of the Americas. — Source: 47 CFR §97.3(a)(24); pool E1C04 (map: CEPT→Europe, IARP→Americas)
- **FACT:** Under FCC Public Notice DA 16-1048 ("Amateur Service Operation in CEPT Countries," released 2016-09-16), "when the privileges authorized by the FCC license grant are Advanced or Amateur Extra Class operator privileges, the U.S. citizen is granted CEPT Radio Amateur License privileges, in accordance with CEPT Recommendation T/R 61-01 (as amended)" — full CEPT — while a General grant earns only CEPT Novice privileges under ECC Recommendation (05)06. — Source: FCC Public Notice DA 16-1048, https://docs.fcc.gov/public/attachments/DA-16-1048A1.pdf (verbatim; PDF fetched and text-extracted 2026-07-30)
- **FACT:** A US Amateur Extra or Advanced operator operating in a CEPT country must carry three documents: "a copy of this Public Notice, proof of U.S. citizenship, and evidence of the FCC license grant" — no "/CEPT" suffix and no local-language ID requirement exists. — Source: FCC Public Notice DA 16-1048 (2026-07-30); pool E1C06 (keyed "You must have a copy of FCC Public Notice DA 16-1048")
- **FACT:** A CEPT radio-amateur license (like an IARP) is issued "by the country of which the person is a citizen," and the holder must not be a US citizen or resident alien, must not hold an FCC amateur grant, and must not be under FCC enforcement sanction. — Source: 47 CFR §97.5(d), (e)
- **FACT:** "No amateur station shall transmit: … Communications for hire or for material compensation, direct or indirect, paid or promised, except as otherwise provided in these rules." — Source: 47 CFR §97.113(a)(2); pool E1F08
- **FACT:** Also prohibited are "communications in which the station licensee or control operator has a pecuniary interest, including communications on behalf of an employer," with narrow exceptions (employer disaster drills, occasional apparatus-sale notices, paid teachers using the station in classroom instruction, club-station telegraphy-practice/bulletin control operators) — a business message is permissible only when neither the amateur nor the employer has a pecuniary interest. — Source: 47 CFR §97.113(a)(3)(i)–(iv); pool E1F07
- **FACT:** Also prohibited: "music using a phone emission except as specifically provided elsewhere in this section; communications intended to facilitate a criminal act; messages encoded for the purpose of obscuring their meaning, except as otherwise provided herein; obscene or indecent words or language; or false or deceptive messages, signals or identification" — encrypting to obscure meaning is barred even on a mesh network. — Source: 47 CFR §97.113(a)(4); pool E1F09
- **FACT:** "An amateur station shall not engage in any form of broadcasting, nor may an amateur station transmit one-way communications except as specifically provided in these rules…." — Source: 47 CFR §97.113(b)

### 2.6 The exam, the VE system, and the upgrade: 50 questions, 37 to pass, /AE, fees

- **FACT:** "Element 4: 50 questions concerning the privileges of an Amateur Extra Class operator license. The minimum passing score is 37 questions answered correctly." — Source: 47 CFR §97.503(c) (verified 2026-07-30); print "37 of 50," not "74%" — see §7.4
- **FACT:** "Amateur Extra Class operator: Elements 2, 3, and 4" — and "each applicant must pass an examination for a new amateur operator license grant and for each change in operator class." — Source: 47 CFR §97.501(a) and intro (verified 2026-07-30)
- **FACT:** A General upgrading to Extra needs Element 4 only: an unexpired (or in-grace-period) General license earns Elements 2 and 3 examination credit, so Elements 2 and 3 are not re-tested. — Source: 47 CFR §97.505(a)(2) (verified 2026-07-30)
- **FACT:** The 2024–2028 Element 4 exam is built as 50 questions drawn one per group from the pool's 50 groups, out of a 599-question active pool across 10 subelements E1–E9 and E0 (E7 and E9 reach group letter H). — Source: `canon/pool-extra.json` (counts re-verified by parse 2026-07-30); `canon/ingestion-report.md` §5.1
- **FACT:** "All VECs must cooperate in maintaining one question pool for each written examination element. Each question pool must contain at least 10 times the number of questions required for a single examination. Each question pool must be published and made available to the public prior to its use for making a question set." — Source: 47 CFR §97.523; pool E1E02 (keyed "The VECs" — not the FCC, not "the ARRL")
- **FACT:** A VEC is an organization that "has entered into a written agreement with the FCC," exists "for the purpose of furthering the amateur service," and agrees to coordinate exams for any operator class without discrimination. — Source: 47 CFR §97.521 (former paragraph (b), the VEC-region requirement, is Reserved and Appendix 2 "VEC Regions" deleted — 90 FR 57712; see §7.2); pool E1E03
- **FACT:** A VEC must confirm that a VE applicant meets FCC requirements to serve as an examiner, and no VEC may accredit a person who fails minimum qualifications, whose services the FCC won't accept, whom the VEC finds incompetent, or whose integrity is in doubt. — Source: 47 CFR §97.525(a); pool E1E04
- **FACT:** Each exam "must be administered by a team of at least 3 VEs at an examination session coordinated by a VEC," and to administer an Amateur Extra exam each VE must hold an Amateur Extra Class license ("Amateur Extra Class in order to administer an Amateur Extra Class operator license examination"), be VEC-accredited, at least 18, and never have had an amateur license revoked or suspended. — Source: 47 CFR §97.509(a), (b)(3)(iii) (verified 2026-07-30)
- **FACT:** "Each administering VE must observe the examinee throughout the entire examination. The administering VEs are responsible for the proper conduct and necessary supervision of each examination. The administering VEs must immediately terminate the examination upon failure of the examinee to comply with their instructions." — Source: 47 CFR §97.509(c); pool E1E06, E1E07 (§97.511: "Each examinee must comply with the instructions given by the administering VEs.")
- **FACT:** "No VE may administer an examination to his or her spouse, children, grandchildren, stepchildren, parents, grandparents, stepparents, brothers, sisters, stepbrothers, stepsisters, aunts, uncles, nieces, nephews, and in-laws." — Source: 47 CFR §97.509(d); pool E1E08
- **FACT:** "No VE may administer or certify any examination by fraudulent means or for monetary or other consideration including reimbursement in any amount in excess of that permitted. Violation of this provision may result in the revocation of the grant of the VE's amateur station license and the suspension of the grant of the VE's amateur operator license." — Source: 47 CFR §97.509(e); pool E1E09
- **FACT:** "When the examinee does not score a passing grade on an examination element, the administering VEs must return the application document to the examinee and inform the examinee of the grade"; passing examinees get a CSCE. — Source: 47 CFR §97.509(j), (l); pool E1E05
- **FACT:** When all elements are credited, "3 VEs must certify that the examinee is qualified for the license grant and that the VEs have complied with these administering VE requirements," and they are "jointly and individually accountable." — Source: 47 CFR §97.509(i); pool E1E11 (citation tag `[97.509(i)]` fixed by errata 1)
- **FACT:** "After the administration of a successful examination for an amateur operator license, the administering VEs must submit the application document to the coordinating VEC according to the coordinating VEC's instructions" — VEs never issue licenses nor file with the FCC directly; the VEC screens, resolves discrepancies, and forwards data electronically to the FCC, retaining records at least 15 months. — Source: 47 CFR §97.509(m), §97.519(b); pool E1E10 (citation tag `[97.509(m)]` fixed by errata 1)
- **FACT:** "VEs and VECs may be reimbursed by examinees for out-of-pocket expenses incurred in preparing, processing, administering, or coordinating an examination for an amateur operator license" — teaching and study materials are not reimbursable. — Source: 47 CFR §97.527; pool E1E01
- **FACT:** Each question set "must be prepared by a VE holding an Amateur Extra Class operator license" (Element 3 also by Advanced; Element 2 also by Advanced or General) using questions from the applicable pool. — Source: 47 CFR §97.507(a), (b)
- **FACT:** "The classes of amateur operator license grants are: Novice, Technician, General, Advanced, and Amateur Extra" — but the FCC currently issues new licenses in only three classes (Technician, General, Amateur Extra), so Amateur Extra is the top of the US license structure with no higher class and no element beyond Element 4. — Source: 47 CFR §97.9(a), §97.501 (verified 2026-07-30)
- **FACT:** "The person named in an operator license grant of Novice, Technician, General or Advanced Class, who has properly submitted to the administering VEs a FCC Form 605 document requesting examination for an operator license grant of a higher class, and who holds a CSCE indicating that the person has completed the necessary examinations within the previous 365 days, is authorized to exercise the rights and privileges of the higher operator class until final disposition of the application or until 365 days following the passing of the examination, whichever comes first." — Source: 47 CFR §97.9(b) (verbatim, verified 2026-07-30)
- **FACT:** §97.9(b) covers General→Extra upgrades exactly as it covers Technician→General: both conditions (Form 605 properly submitted to the administering VEs + CSCE in hand) are normally satisfied at the exam session, so the new Extra privileges are legal to use immediately — before the VEC files anything and before ULS changes. — Source: 47 CFR §97.9(b) (verified 2026-07-30; wording law in §7.3)
- **FACT:** While operating under §97.9(b), "an indicator must be included after the call sign as follows: … (3) For a control operator who has requested a license modification from Novice, Technician, General, or Advanced Class to Amateur Extra Class: AE" — the AE indicator is paragraph (f)(3); paragraph (f)(2) is AG for General. — Source: 47 CFR §97.119(f)(3) (verbatim, verified 2026-07-30)
- **FACT:** "Each indicator must be separated from the call sign by the slant mark (/) or by any suitable word that denotes the slant mark." — Source: 47 CFR §97.119(c) (verified 2026-07-30)
- **FACT:** In practice (one VEC's instructions, not rule text): on phone say your call sign followed by the words "temporary" or "Interim" AE or Alpha Echo (e.g., "This is KX9ABC temporary AE"), on CW or digital modes sign KX9ABC/AE, and once your upgrade shows in the FCC ULS database, drop the suffix. — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php (extracted 2026-07-30; see §7.3)
- **FACT:** The §97.9(b) interim authority ends at "final disposition of the application" — normally the grant appearing in ULS — or 365 days after passing, whichever comes first; after the grant shows, the authority rests on the license itself under §97.9(a). — Source: 47 CFR §97.9(a)–(b) (verified 2026-07-30)
- **FACT:** A brand-new licensee has no operating authority until the license grant appears in the FCC's ULS database — the wait-for-the-grant rule applies to new licenses only, while an existing licensee upgrading operates immediately under §97.9(b). — Source: FCC, Amateur Radio Service, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service (verified 2026-07-24; page 403s to curl — re-check in a browser before publication, §7.11); 47 CFR §97.9(b)
- **FACT:** If a candidate passes multiple exam elements at one session, the VEC transmits one application to the FCC reflecting the highest license class earned — so a Technician may in principle test straight through to Extra in one session (Elements 2, 3, and 4). — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-30); 47 CFR §97.505
- **FACT:** "The administering VEs must give credit to an examinee holding a CSCE for each element the CSCE indicates the examinee passed within the previous 365 days," and each CSCE is individually valid for 365 days from its issue date — no subsequently issued CSCE renews another's validity period. — Source: 47 CFR §97.505(b); ARRL Volunteer Examiner Manual, CSCE section (re-verified 2026-07-30)
- **FACT:** You keep your call sign when you upgrade: "The station is reassigned its same call sign upon renewal or modification of its license, unless the licensee applies for a change to a new sequentially assigned or vanity call sign on FCC Form 605." — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems (verified 2026-07-24; page 403s to curl — re-check in a browser, §7.11)
- **FACT:** An amateur service license "is normally granted for a 10-year term," and Amateur Extra licensees are eligible for the Group A vanity call-sign formats (1×2, 2×1, and 2×2 with an A-first prefix) — the only call-sign group reserved to Extra class. — Source: 47 CFR §97.25; FCC, Amateur Call Sign Systems (verified 2026-07-24); 47 CFR §97.19(d)
- **FACT:** "The Amateur Extra class license conveys all available U.S. Amateur Radio operating privileges on all bands and all modes," and earning it "requires passing a thorough 50 question examination." — Source: ARRL, Getting Licensed, http://www.arrl.org/getting-licensed (verbatim, re-verified 2026-07-30)
- **FACT:** No Morse code exam exists for any US license class — the FCC dropped the Morse code requirement effective February 23, 2007, so Extra today is a written-exam-only step up. — Source: Laurel VEC FAQ, "Do I have to pass a Morse code exam?", https://larc-vec.org/faq.php (verified 2026-07-23)
- **FACT:** The FCC's $35 application fee (effective April 19, 2022) applies per application to new-license, renewal, rule-waiver, and vanity-call-sign applications — and "modification applications to upgrade an amateur radio licensee's operator class … are exempt from fees," so a General→Extra upgrader has no FCC payment step and no 10-day payment window. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-30; re-verify before each reprint — §7.11)
- **FACT:** The 2026 ARRL VEC exam session fee is $15.00 and pays for one attempt at each of the three exam elements; candidates younger than 18 pay a reduced $5.00 fee ("The Youth Exam Fee For 2026 is $5.00"); Laurel VEC charges no fees for any licensing-related services. — Source: ARRL VEC Exam Fees, http://www.arrl.org/arrl-vec-exam-fees (calendar-2026 figures, re-verified 2026-07-30; re-verify each January — §7.11); Laurel VEC FAQ, https://larc-vec.org/faq.php (verified 2026-07-23)
- **FACT:** VECs and VE teams must not collect the $35 FCC fee at exam sessions; when a fee is due it is paid online directly to the FCC through CORES, never to the VE team. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-30)
- **FACT:** The current NCVEC Form 605 is the 2022 edition, and the Quick-Form 605 is the standard exam-session application: the applicant completes Section 1 (email address and FRN are mandatory), the three administering VEs print, sign, and date Section 2, and the form goes to the coordinating VEC — never directly to the FCC. — Source: NCVEC, https://www.ncvec.org/downloads/NCVEC_Form_605_2022.pdf (HTTP 200 application/pdf, re-verified 2026-07-30); ARRL, NCVEC 605 Instructions, http://www.arrl.org/605-instructions
- **FACT:** An FRN (FCC Registration Number) is a 10-digit number assigned by the FCC in CORES, required before exam day and available immediately on registration; the Social Security number is given inside CORES rather than on the exam form, and a valid email address is mandatory because the FCC sends all correspondence by email. — Source: FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html; ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** Registering in CORES to get your FRN carries no fee and no exam requirement. — Source: series-canonical safe wording (no payment step exists in the CORES registration flow; FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html; never print "free of charge" — §7.10)
- **FACT:** Exam candidates must present one legal photo ID (or two forms of non-photo ID if none), and every applicant must answer the Basic Qualification Question (felony conviction status) on the application form. — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** Under ARRL VEC retest policy, a failed element may be retaken at the same session only if the team has a different version of that element the applicant has not taken, the team has the time, resources, and willingness, and the applicant pays an additional test fee — nothing in FCC rules entitles a failed candidate to an immediate retest. — Source: ARRL Volunteer Examiner Manual, "Retesting," http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf; Laurel VEC FAQ, https://larc-vec.org/faq.php
- **FACT:** Amateur exams are offered both in person and as remote video-supervised online sessions, availability of remote testing depends entirely on the individual VE team (Laurel runs in-person only), and both ARRL's session finder and HamStudy.org's session page list in-person and remote sessions from many VE teams. — Source: ARRL, Find an Amateur Radio License Exam Session, http://www.arrl.org/find-an-amateur-radio-license-exam-session (HTTP 200, re-verified 2026-07-30); https://hamstudy.org/sessions (HTTP 200, re-verified 2026-07-30); Laurel VEC FAQ
- **FACT:** "EXTRA Class (Element 4) Pool is effective July 1, 2024 and is valid until June 30, 2028," and question pools rotate on a four-year cycle (Technician 2026–2030; General 2023–2027; Extra 2024–2028; "No question pools will be updated or released in 2025 or 2029") — the next Extra pool takes effect 2028-07-01. — Source: ARRL, Question Pools, http://www.arrl.org/question-pools (verbatim, re-verified 2026-07-30); NCVEC release page (fetched 2026-07-30)
- **FACT:** The NCVEC Question Pool Committee released the 2024–2028 Extra (Element 4) pool into the public domain: "The NCVEC Question Pool Committee hereby releases into public domain the 2024-2028 Element 4 Extra Class Question Pool" (stated twice on the release page). — Source: NCVEC release page, https://ncvec.org/index.php/2024-2028-extra-class-question-pool-release (captured in `canon/source/release-page.html`, fetched 2026-07-30)
- **FACT:** The 2024–2028 Extra pool carries a four-errata history — Errata 1 (2024-01-31: five questions modified, citation fixes on E1E10/E1E11, E9E10 withdrawn, diagram E9-3 rotated), 2nd errata (2024-11-08: E2A13 withdrawn), 3rd errata (2025-09-24/25: E6D07 withdrawn), 4th errata (2026-02-04: E4D05 withdrawn) — four withdrawals total, never renumbered, and the 4th-errata release is the current document with no 5th errata as of 2026-07-30. — Source: `canon/ingestion-report.md` §5.2 (errata sheets cross-checked against the NCVEC release page and the pool body)
- **FACT:** The three-book arc maps one-to-one onto the license ladder: Technician (Element 2, 35 questions, 26 to pass) → General (Element 3, 35 questions, 26 to pass) → Extra (Element 4, 50 questions, 37 to pass). — Source: 47 CFR §97.503(a)–(c) (verbatim, re-verified 2026-07-30)
- **FACT:** An Amateur Extra licensee may serve as a Volunteer Examiner for all three exam levels, including administering Element 4 itself. — Source: 47 CFR §97.509(b)(3) (verified 2026-07-30)
- **FACT:** ARRL publishes graphical frequency-allocation charts by license class — the canonical visual reference for the band-by-band detail. — Source: ARRL, Graphical Frequency Allocations, https://www.arrl.org/graphical-frequency-allocations (HTTP 200, re-verified 2026-07-30)

---

### 2.7 Satellite and EME operating values

- **FACT:** A satellite's "mode" is its uplink/downlink band pair — not FM-vs-SSB and not an orbit class — and the mode letters specify the uplink and downlink frequency ranges, uplink first: V = 2 m, U = 70 cm, L = 23 cm, S = 13 cm. — Source: pool E2A04, E2A05, E2A09; the V/U convention documented across study guides (hamstudy.org E2A browse page) and the ARRL band plan satellite subbands
- **FACT:** The US band plan's satellite segments are 145.80–146.00 MHz (OSCAR subband, 2 m), 435–438 MHz (satellite only, 70 cm), 1260–1270 MHz (satellite uplinks, 23 cm = L band), and 2400–2410 MHz (amateur satellite, 13 cm = S band). — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-30)
- **FACT:** An ascending pass travels south to north (crossing the equator going up), Keplerian elements are the orbit-defining parameter set tracking software eats (distributed as TLEs), and a geostationary satellite appears fixed in the sky. — Source: pool E2A01, E2A06, E2A10; amsat.org/keplerian-elements-resources (2026-07-30)
- **FACT:** A linear transponder is a bent-pipe frequency translator — the uplink is mixed with a local oscillator and the difference product retransmitted — so being linear it relays any mode: FM, CW, SSB, SSTV, PSK, or packet. — Source: pool E2A03, E2A07
- **FACT:** On an inverting transponder all three hold at once: the sidebands swap (USB becomes LSB), band positions reverse, and uplink and downlink Doppler move in opposite directions so the Doppler shift partially cancels. — Source: pool E2A02 (all-of-the-above)
- **FACT:** A linear transponder's downlink power is shared, so excessive uplink ERP captures the transponder's AGC and steals downlink power from every other user — run uplink power so your downlink is about as strong as the satellite's beacon. — Source: pool E2A08; Technician-pool beacon-strength rule (series canon)
- **FACT:** LEO Doppler is a few kHz on VHF and tens of kHz on UHF — about ±3.5 kHz on 2 m and ±10 kHz on 70 cm as typical-LEO magnitudes (order-of-magnitude practice, not constants): tune the link with the bigger Doppler, the higher-frequency one — on U/v birds adjust the uplink, on V/u birds (e.g., SO-50) adjust the downlink. — Source: orbitalradar.com Doppler explainer (2026-07-30); N8HM "Getting Started on FM Satellites" AMSAT deck (2026-07-30); AMSAT station-and-operating-hints page ("The One True Rule for Doppler Tuning")
- **FACT:** Circular polarization at the ground station mitigates spin modulation and Faraday rotation. — Source: pool E2A11
- **FACT:** Store-and-forward is the orbiting mailbox that holds digital messages for later download — flown literally by FalconSAT-3 (9600 baud, 145.840 up / 435.103 down) until it re-entered in January 2023, a reminder that every named satellite is a time-sensitive fact (§7.11). — Source: pool E2A12; amsat.org (2017); arrl.org news (2023-01-20)
- **FACT:** QO-100 (Es'hail-2), launched 2018-11-15 and parked at 25.9°E, carries the first amateur transponders in geostationary orbit — 2.4 GHz uplink / 10 GHz downlink, one narrowband (SSB/CW/FT8) and one wideband DATV transponder — but its footprint runs Brazil-to-Thailand, so it is the geostationary example, not a US operating opportunity. — Source: radarc.org "Operating on QO-100"; amsat-uk.org QO-100 pages (2026-07-30); jeremyclark.ca QO-100 planning notes (footprint edge, 2026-07-30); pool E2A10 (concept)
- **FACT:** The EME round-trip delay is about 2.5 seconds at the Moon's average 384,400 km distance (about 2.4–2.8 s as lunar distance varies) — WSJT-X's Echo mode exists so you can listen for your own echo. — Source: moonbounce.dk "What is EME"; bobatkins.com Q65-15 EME notes (2026-07-30); WSJT-X 2.7 User Guide §1 (fetched 2026-07-30)
- **FACT:** EME path loss is ≈252 dB at 144 MHz and ≈271 dB at 1296 MHz, and the lunar surface reflects only about 6 percent of the power that reaches it — band-specific figures, never generalized (§7.11). — Source: electronics-notes.com EME page (2026-07-30); Chalmers EME thesis (1296 MHz figure, 2026-07-30)
- **FACT:** Perigee versus apogee is worth about 2 dB round trip — path loss to the Moon and back is roughly 2 dB less at perigee, which is exactly why the least EME path loss occurs at perigee. — Source: N1BUG EME notes via g1ogy.com (2026-07-30); electronics-notes.com (2026-07-30); Ham Radio magazine Feb 1981 (1.14 dB one-way); pool E3A03
- **FACT:** Any two stations with the Moon mutually visible can attempt EME, up to about 12,000 miles apart measured along the Earth's surface. — Source: pool E3A01
- **FACT:** Libration fading is the fluttery, irregular fading caused by multipath off the Moon's rough, curved, wobbling face. — Source: pool E3A02; Barron, "Amsats and Hamsats" (2026-07-30)
- **FACT:** On VHF bands and higher, digital-mode QSOs (EME, scatter, and other propagation types) are possible "at signal levels 10 to 15 dB below those required for CW." — Source: WSJT-X 2.7 User Guide §1 (fetched 2026-07-30)
- **FACT:** JT65 was designed for EME and decodes very-low-SNR signals using multitone AFSK (65 tones), while Q65 — which averages multiple receive cycles where JT65 does not — is effective for EME and fast-fading paths (tropospheric scatter, rain scatter, ionospheric scatter, TEP). — Source: pool E2D03, E2D05, E2D09, E2E07; WSJT-X 2.7 User Guide §1 (fetched 2026-07-30)
- **FACT:** EME runs on time-synchronous transmit/receive alternation — the discipline WSJT automates: JT4/JT9/JT65 use 1-minute T/R sequences (a minimal QSO takes 4–6 minutes, one station on odd UTC minutes, the other on even), and Q65 offers 15/30/60/120/300-second sequences. — Source: pool E2D06; WSJT-X 2.7 User Guide §1 (fetched 2026-07-30); bobatkins.com (2026-07-30)
- **FACT:** The ARRL band plan's EME segments are 144.00–144.05 (CW), 432.00–432.07, and 1295.8–1296.08 MHz, and 2 m is the most active EME band. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-30); AB1OC/N1FD "Getting Started in EME" deck (2026-07-30)

### 2.8 Weak-signal VHF+, digital-mode, and contest/DX values

- **FACT:** The national weak-signal calling frequencies are 50.125 MHz (6 m SSB), 144.200 MHz (2 m), 222.100 MHz (1.25 m), and 432.100 MHz (70 cm) — the geography behind the pool's VHF/UHF-contest answer: the SSB/CW crowd sits in the weak-signal segment of the band, with most of the activity near the calling frequency. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-30); pool E2C06
- **FACT:** The band-plan weak-signal segments are 50.0–50.1 MHz (CW/beacons) and 50.1–50.3 (SSB/CW) on 6 m, 144.00–144.05 (EME), 144.05–144.10 (CW/weak), 144.10–144.20 (EME/weak-signal SSB) on 2 m, 222.0–222.15 (weak signal) on 1.25 m, and 432.00–432.10 (EME/CW) and 432.10–432.30 (weak-signal work) on 70 cm — custom says raise a station on the calling frequency, then move up the band. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-30)
- **FACT:** The propagation beacon segments are 50.060–50.080, 144.275–144.300, 222.05–222.06, and 432.30–432.40 MHz — tune the beacon segment, not the white space, to know a band is open. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-30)
- **FACT:** VHF contests exchange grid squares, not signal reports: ARRL January/June/September VHF contests use the 4-character grid on 50/144/222/432 MHz and up, the 222 MHz and Up and 10 GHz and Up distance contests use 6-character grids, and that is exactly why FT8/FT4 in a VHF contest exchanges a grid square in place of the SNR report. — Source: ARRL contest rules (verified 2026-07-30); pool E2D02
- **FACT:** MSK144 is the digital mode designed for meteor scatter: 144-bit frames at 2000 baud make a complete message every 72 ms repeated through a 15 s T/R sequence, it decodes to −8 dB SNR in 2500 Hz, and a 20 ms short format exists for the shorter 2 m pings — because meteor pings are milliseconds long, with the rare long trails lasting several seconds and ping duration scaling as 1/f² (pings at 144 MHz run about 1/8 as long as at 50 MHz). — Source: pool E2D01; Franke & Taylor, "The MSK144 Protocol for Meteor-Scatter Communication," QEX Sept/Oct 2017 (arrl.org, fetched 2026-07-30)
- **FACT:** Meteor trails ionize at E-region height, the best meteor-scatter range is 28–148 MHz (which is why 6 m and 2 m dominate), and modern digital meteor scatter works pings shorter than 0.1 s any day of the year out to about 1,300 miles. — Source: pool E3A08, E3A09; Franke & Taylor QEX Sept/Oct 2017 (2026-07-30)
- **FACT:** The 6 m digital dial by convention (not band plan): FT8 on 50.313 MHz with 50.323 the intercontinental convention, FT4 on 50.318, and MSK144 calling on 50.260 MHz by informal convention — all drift with usage; re-verify before print (§7.11). — Source: OnAllBands "FT8: Frequencies, Decibels, and Message Meanings" (2026-07-30); hamdeck.com digital-frequency reference (2026-07-30); Franke & Taylor QEX Sept/Oct 2017
- **FACT:** WSJT-X timing is synchronized computer clocks — sync to UTC within ±1 second (the built-in Windows time sync is usually not adequate), and a waterfall full of signals with zero decodes means check the clock. — Source: pool E2E02; WSJT-X 2.7 User Guide §2 (fetched 2026-07-30)
- **FACT:** Sequence lengths as the operator lives them: FT8 15 seconds, FT4 7.5 seconds (built for contesting), JT65/JT9 1 minute, MSK144 selectable 5/10/15/30 seconds. — Source: pool E2E06; WSJT-X 2.7 User Guide §1 (fetched 2026-07-30)
- **FACT:** WSPR is beacon-only — no keyboard-to-keyboard — sending call sign, grid locator, and power in dBm in 2-minute sequences, decodable to −31 dB SNR in 2500 Hz per the current WSJT-X guide (older WSPR documentation says −28 dB; attribute that figure to "earlier WSPR documentation" if it ever appears), with reports auto-uploaded to WSPRnet's map. — Source: pool E2E05; WSJT-X 2.7 User Guide §1 (fetched 2026-07-30)
- **FACT:** FT8 has the narrowest bandwidth of the listed modes at about 50 Hz — dozens of stations share one waterfall at different audio offsets. — Source: pool E2E10, E8C06
- **FACT:** APRS runs on AX.25, its beacons use Unnumbered Information (UI) frames (connectionless, no acknowledgment), relays are packet digipeaters, and a WIDE3-1 path requests three digipeater hops with one remaining — the counter decrements per digipeater. — Source: pool E2D07, E2D08, E2D10, E2D11
- **FACT:** Contest-free by convention: 30 meters — the WARC-band truce is long-standing custom, not an FCC rule (the pool's own wording is "generally excluded"). — Source: pool E2C03; "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.8.6 (see §7.6)
- **FACT:** Remote operation of a US transmitter requires no additional station-identification indicator beyond normal Part 97 ID — §97.119(c) permits but does not require indicators, and none is prescribed for remote control. — Source: pool E2C01; 47 CFR §97.119 (research note r1 W9; see §7.6)
- **FACT:** Latency is the delay between a control action and the resulting change in the transmitted signal. — Source: pool E2C12
- **FACT:** ADIF is the log-data interchange format, Cabrillo is the contest-log submission format, LoTW confirms special-event, DX, and WAS contacts alike, and a QSL manager handles a DX station's confirmations. — Source: pool E2C02, E2C07, E2C08, E2C05
- **FACT:** Split operation serves all three purposes at once: it keeps callers off the DX station's transmit frequency, improves efficiency, and lets stations call where they are licensed — and in a pileup you send your full call sign once or twice. — Source: pool E2C10 (all-of-the-above), E2C11
- **FACT:** Keep the split listening range tight — no more than 30 kHz on SSB and 10 kHz is more than enough on CW. — Source: N7NG, ARRL/INDEXA "DXpeditioning Basics," arrl.org/files/file/DXCC/dx-basics.pdf (fetched 2026-07-30)
- **FACT:** Mesh networks run on channels shared with unlicensed Part 15 data services using wireless routers with custom firmware (e.g., AREDN), with nodes forming the network via discovery and link-establishment protocols — not store-and-forward digipeating. — Source: pool E2C04, E2C09, E8C14, E8C15
- **FACT:** NTSC fast-scan television is 525 lines per frame, interlaced — odd lines one field, even lines the next. — Source: pool E2B02, E2B03
- **FACT:** Vestigial sideband is AM with one full sideband plus a vestige of the other — it cuts bandwidth while preserving low-frequency video fidelity. — Source: pool E2B05, E2B06
- **FACT:** In analog SSTV, brightness is encoded by tone frequency, color is sent as sequential color lines, the VIS code announces the SSTV mode so software can auto-select it, and specific tone frequencies trigger each new line. — Source: pool E2B10, E2B04, E2B11, E2B12
- **FACT:** DRM-protocol SSTV is receivable on an ordinary SSB receiver, and 70 cm fast-scan ATV is watchable on analog cable-ready TVs by using frequencies shared with cable channels. — Source: pool E2B09, E2B08
- **FACT:** In digital television, a coding rate of 3/4 means 25 percent of the transmitted data is forward-error-correction overhead, and amateur DVB-T uses QAM and QPSK. — Source: pool E2B01, E2B07
- **FACT:** Below 30 MHz data emissions use FSK; direct FSK shifts the transmitter VFO itself, while AFSK feeds audio tones into an SSB rig. — Source: pool E2E01, E2E11
- **FACT:** PSK31 uses a variable-length varicode (common letters get short codes), PACTOR transfers binary files on HF, PACTOR IV has the highest throughput of the listed modes in clear conditions, and ALE constantly scans a frequency list and activates on the designated call sign. — Source: pool E2E09, E2E08, E2E13, E2E12
- **FACT:** FST4 uses four-tone Gaussian FSK with variable T/R periods and seven tone spacings (all three clauses true), and FT4's "4" names its four-tone continuous-phase FSK. — Source: pool E2E04 (all-of-the-above), E2E03

### 2.9 Propagation values (E3)

- **FACT:** The E and H fields of a radio wave are at right angles to each other, the wave propagates at right angles to both, its speed through a medium is set by the medium's index of refraction, and circular polarization means the field rotates as the wave advances. — Source: pool E3A04, E3A05, E3A10, E3A14
- **FACT:** When darkness drops the MUF below your band, move to a lower-frequency band. — Source: pool E3A06
- **FACT:** Microwave tropospheric ducts form over large bodies of water, with a typical range of 100 to 300 miles. — Source: pool E3A07, E3A11
- **FACT:** Auroral propagation follows severe geomagnetic storms; the signals arrive phase-distorted (the moving curtain spreads a carrier into a buzz a few kHz wide), so CW is the most usable mode — beam north first, both stations pointing at the curtain rather than at each other. — Source: pool E3A12, E3A13; VHF/UHF DX Book via qsl.net (2026-07-30); WorldRadio June 1999 via worldradiohistory.org (2026-07-30)
- **FACT:** Transequatorial propagation works between stations about 2,000–3,000 miles apart on a path roughly perpendicular to the geomagnetic equator (practice: about 1,500–2,500 miles north and south of it, crossing within ±20° of right angles), with a maximum range of about 5,000 miles, most likely in the afternoon or early evening, ducting between the two equatorial-anomaly electron peaks with no intermediate ground reflection. — Source: pool E3B01, E3B02, E3B03; Ham Radio magazine July 1984 via worldradiohistory.org; N5DUX VHF-UHF primer (2026-07-30)
- **FACT:** The ionosphere splits waves into independently propagating, elliptically polarized ordinary and extraordinary waves. — Source: pool E3B04
- **FACT:** Long-haul 160 m propagation needs a path entirely in darkness (D-region absorption kills sunlit paths), long path is most frequent on 40 and 20 meters, and a lower takeoff angle means longer hops. — Source: pool E3B05, E3B06, E3B07
- **FACT:** Ground-wave propagation needs vertical polarization, and its maximum range decreases as frequency rises — which is why 160 m ground wave outreaches 10 m. — Source: pool E3B13, E3B08
- **FACT:** Sporadic E peaks around the solstices, especially the summer solstice, and the pool keys it as a daytime mode — most likely between sunrise and sunset (see §7.6 for the evening-Es operating lore). — Source: pool E3B09, E3B11
- **FACT:** Chordal hop is successive ionospheric refraction without an intermediate ground reflection — skipping the lossy ground bounce means less loss than ordinary multi-hop. — Source: pool E3B12, E3B10
- **FACT:** Sudden short-term HF blackouts come from solar flares (the X-rays ionize the sunlit D region), and a sudden broadband rise in HF background noise likewise means a flare or CME impact. — Source: pool E3C01, E3C12
- **FACT:** A rising A- or K-index means increasing geomagnetic disturbance, and elevated indices hammer paths through the auroral oval with absorption. — Source: pool E3C02, E3C03
- **FACT:** Bz is the north–south component of the interplanetary magnetic field, and a southward Bz couples solar-wind energy into the magnetosphere, producing disturbed conditions. — Source: pool E3C04, E3C05
- **FACT:** Flare classes ascend A→B→C→M→X with X strongest, while geomagnetic storms use the G scale with G5 extreme — two scales, two top letters. — Source: pool E3C07, E3C08
- **FACT:** The VHF/UHF radio horizon is approximately 15 percent farther than the geographic horizon because of atmospheric refraction. — Source: pool E3C06
- **FACT:** Reporting networks such as PSK Reporter, WSPRNet, and the Reverse Beacon Network report digital-mode and CW sightings — the practical way to see where your signal is being heard right now. — Source: pool E3C09
- **FACT:** The 304A index measures solar UV emissions at 304 angstroms, correlated to the solar flux index, and VOACAP models HF propagation. — Source: pool E3C10, E3C11

### 2.10 Amateur practices and test equipment (E4)

- **FACT:** A digital oscilloscope's highest accurate frequency is set by its ADC sampling rate, and undersampling produces aliasing — a false, jittery low-frequency copy of the signal. — Source: pool E4A01, E4A06
- **FACT:** Compensate a ×10 scope probe on the calibrator square wave until the flat tops are flat, keep the probe ground lead short, and use line triggering to lock to the AC line — the stable choice for viewing power-supply ripple. — Source: pool E4A04, E4A09, E4A10
- **FACT:** A spectrum analyzer displays amplitude (vertical) versus frequency (horizontal) — the tool for transmitter spurs and intermod products — while an oscilloscope displays amplitude versus time. — Source: pool E4A02, E4A03
- **FACT:** A prescaler divides high frequencies into a frequency counter's range, and counter accuracy is dominated by time-base accuracy. — Source: pool E4A05, E4B01
- **FACT:** An antenna analyzer computes SWR and impedance directly and can measure velocity factor, cable length, and tuned-circuit resonance, and SWR is measurable with a directional wattmeter, a VNA, or an antenna analyzer — all three. — Source: pool E4A07, E4A11, E4A08 (all-of-the-above)
- **FACT:** A meter's ohms-per-volt rating times its full-scale voltage gives its input impedance — 20 kΩ/V × 10 V = 200 kΩ. — Source: pool E4B02
- **FACT:** S parameters describe a two-port network with subscripts naming the ports measured: S21 is forward gain (into port 2 from port 1), and S11 is input return loss/reflection coefficient, equivalent to VSWR. — Source: pool E4B07, E4B03, E4B04
- **FACT:** A two-port VNA can measure filter frequency response, input and output impedance, and reflection coefficient, and VNA calibration uses short, open, and 50 Ω loads. — Source: pool E4B09, E4B11, E4B05
- **FACT:** Absorbed power equals forward minus reflected power — 100 W forward and 25 W reflected delivers 75 W to the load. — Source: pool E4B06
- **FACT:** The Q of a series-tuned circuit comes from the bandwidth of its frequency response: Q = f/BW (the inverse of the E5 half-power-bandwidth formula). — Source: pool E4B08
- **FACT:** A transmitter IMD test feeds two non-harmonically related audio tones into the microphone input and observes the RF output on a spectrum analyzer. — Source: pool E4B10
- **FACT:** Noise figure is the dB ratio of a receiver's noise to the theoretical minimum, the reference noise floor is −174 dBm in a 1 Hz bandwidth at room temperature, and MDS means minimum discernible signal. — Source: pool E4C04, E4C05, E4C07
- **FACT:** Receiver noise scales with bandwidth: widening from 50 Hz to 1,000 Hz raises the noise floor by 10·log₁₀(1000/50) = 13 dB. — Source: pool E4C06
- **FACT:** Reciprocal mixing is LO phase noise mixing with a strong adjacent signal and dumping noise onto the desired signal — the same mechanism that makes SDR master-clock phase noise dangerous — and SDR overload means input peaks exceeding the ADC reference voltage. — Source: pool E4C13, E4C01, E4C08
- **FACT:** A high first IF eases image rejection, a front-end preselector removes strong out-of-band signals before they can intermod, selectable bandwidths match the mode for best SNR, a narrow roofing filter improves blocking dynamic range by attenuating strong close-in signals early, and IF Shift slides the passband away from adjacent interference. — Source: pool E4C09, E4C02, E4C10, E4C12, E4C14
- **FACT:** On the low HF bands front-end attenuation costs almost nothing, because atmospheric noise still exceeds the receiver's internal noise. — Source: pool E4C11
- **FACT:** The capture effect: in FM the stronger co-channel signal suppresses the weaker one. — Source: pool E4C03
- **FACT:** Blocking dynamic range is the dB span from the noise floor to the level causing 1 dB of gain compression, poor dynamic range shows up as cross-modulation and desensitization from strong adjacent signals, and desensitization is tamed by attenuation before the first RF stage. — Source: pool E4D01, E4D02, E4D06, E4D07
- **FACT:** Intermodulation is born in nonlinear circuits — two close repeaters intermod when their signals mix in a final amplifier — a properly terminated circulator on the transmitter output isolates it, and a preselector raises out-of-band rejection. — Source: pool E4D08, E4D03, E4D04, E4D09
- **FACT:** Odd-order intermodulation products matter because two in-band signals yield odd-order products that also land in-band, for example 2f1 − f2. — Source: pool E4D11
- **FACT:** A third-order intercept point of 40 dBm is the extrapolated point where two 40 dBm inputs would produce third-order products equal to the inputs — an extrapolation, not a working level. — Source: pool E4D10
- **FACT:** Link budgets are pure dB bookkeeping — received power = transmit power + antenna gains − losses − path loss: 40 dBm + 6 dB + 3 dB − 100 dB = −51 dBm received (each distractor omits exactly one gain). — Source: pool E4D13
- **FACT:** Link margin = received power − MDS − required SNR: with 40 dBm + 10 dB − 3 dB − 136 dB = −89 dBm received, −89 − (−103) = 14 dB over MDS, and 14 − 6 = +8 dB of margin after the SNR reserve. — Source: pool E4D12
- **FACT:** −100 dBm is 10⁻¹³ W = 0.1 picowatt, from P(W) = 10^((dBm−30)/10). — Source: pool E4D14
- **FACT:** The noise-tool map: a noise blanker attacks impulse noise (ignition, power-line), DSP noise reduction attacks broadband white, ignition, and power-line noise (all three), an automatic notch filter hunting a carrier can notch out your own CW signal, and a blanker can distort strong signals so they appear to cause spurious emissions. — Source: pool E4E03, E4E02 (all-of-the-above), E4E01, E4E09
- **FACT:** The RFI cures: alternator/charging noise yields to ferrite chokes on the charging leads, and AC-motor RFI yields to a brute-force AC-line filter in series with the motor leads. — Source: pool E4E04, E4E05
- **FACT:** The RFI signatures: network equipment radiates unstable modulated or unmodulated signals at specific frequencies, switch-mode power supplies radiate carriers at regular intervals across a wide range, arcing thermostats/doorbell transformers/flickering displays cause intermittent roaring or buzzing (all three), and corroded metal joints near broadcast sites mix and re-radiate signals — the rusty-bolt effect. — Source: pool E4E06, E4E12, E4E10 (all-of-the-above), E4E11
- **FACT:** Common-mode current flows equally on all conductors and is what makes shielded cables radiate or pick up interference — chokes kill it without touching the differential signal. — Source: pool E4E08, E4E07
- **FACT:** Surge protectors mount on the single point ground panel, whose job is ensuring all lightning protectors fire simultaneously, preventing lethal chassis-to-chassis potentials. — Source: pool E4E13, E4E14

### 2.11 Electrical principles (E5)

- **FACT:** At resonance X_L = X_C and the reactances cancel: in a series RLC circuit the impedance drops to approximately R (minimum impedance, maximum line current, voltage and current in phase), while in a parallel RLC circuit the impedance rises to a maximum and the input current is minimum even though the circulating current inside the L–C loop is maximum. — Source: pool E5A03, E5A08, E5A06, E5A07
- **FACT:** A parallel resonant circuit's impedance at resonance is approximately equal to the circuit resistance — the pool's model assumes the parallel-R form (see §7.6). — Source: pool E5A04
- **FACT:** At series resonance the voltages across L and C can each exceed the applied voltage by roughly Q, so raising series Q raises internal voltages — why tank capacitors arc. — Source: pool E5A01, E5A13
- **FACT:** Series Q = X/R and parallel Q = R/X, and a higher-Q matching network has a narrower matching bandwidth. — Source: pool E5A09, E5A05
- **FACT:** The resonant frequency is f₀ = 1/(2π√(LC)) — 50 µH with 40 pF gives 3.56 MHz and 50 µH with 10 pF gives 7.12 MHz; the resistor in those questions is a decoy, because R never enters the resonance formula. — Source: pool E5A02, E5A10
- **FACT:** Half-power bandwidth is BW = f₀/Q — 7.1 MHz with Q 150 gives 47.3 kHz, and 3.7 MHz with Q 118 gives 31.4 kHz. — Source: pool E5A11, E5A12
- **FACT:** One time constant τ = RC (or L/R) charges a capacitor to 63.2% of the applied voltage or discharges it to 36.8% of its initial voltage — 440 µF into 500 kΩ gives τ = 220 s (combine the paralleled components first). — Source: pool E5B01, E5B04
- **FACT:** Admittance is Y = 1/Z = G + jB in siemens — conductance G is the real part, susceptance the imaginary part, letter B — and in polar form |Y| = 1/|Z| with the angle negated; a pure reactance converts to a susceptance of reciprocal magnitude. — Source: pool E5B02, E5B06, E5B12, E5B03, E5B05
- **FACT:** ELI the ICE man: in an inductor voltage (E) leads current (I) by 90°, and in a capacitor current leads voltage by 90°. — Source: pool E5B10, E5B09
- **FACT:** The series RLC phase angle is θ = atan((X_L − X_C)/R) — positive means net inductive and voltage leads, negative means capacitive and voltage lags: atan((250−500)/1000) = −14.0° (lags), atan((100−300)/100) = −63° (lags), atan((75−25)/100) = +27° (leads). — Source: pool E5B07, E5B08, E5B11
- **FACT:** Rectangular impedance is Z = R ± jX with +j inductive and −j capacitive — a pure capacitive reactance of 100 Ω is written 0 − j100, and 50 − j25 means 50 Ω resistance in series with 25 Ω capacitive reactance. — Source: pool E5C01, E5C06
- **FACT:** Polar notation states magnitude and phase angle — a pure inductance sits at +90° and a pure capacitance at −90° — and conversions run |Z| = √(R² + X²), θ = atan(X/R), and back via R = |Z|cos θ, X = |Z|sin θ (50 − j25 → 55.9 ∠−26.6° Ω). — Source: pool E5C02, E5C03, E5C06
- **FACT:** On rectangular impedance coordinates the horizontal axis is resistance and the vertical axis is reactance, a pure resistance plots on the horizontal axis, polar coordinates display magnitude and phase directly, a phasor diagram shows phase relationships among impedances at one frequency, and frequency-response graphs use a logarithmic vertical axis. — Source: pool E5C09, E5C07, E5C08, E5C05, E5C04
- **FACT:** The Figure E5-1 plotting answers: 400 Ω + 38 pF at 14 MHz (X_C ≈ 300) → 400 − j300 → Point 4; 300 Ω + 18 µH at 3.505 MHz (X_L ≈ 400) → 300 + j400 → Point 3; 300 Ω + 19 pF at 21.2 MHz (X_C ≈ 400) → 300 − j400 → Point 1. — Source: pool E5C10, E5C11, E5C12; canon §1.4 Figure E5-1
- **FACT:** Skin effect crowds RF current toward the conductor surface, so conductor resistance rises with frequency — and it is also the primary RF loss mechanism in film capacitors. — Source: pool E5D01, E5D08
- **FACT:** Component leads are parasitic inductance — keep VHF-and-up leads short to minimize inductive reactance, and at microwave frequencies short connections also reduce phase shift. — Source: pool E5D02, E5D04
- **FACT:** A conductor's electrical length increases with diameter — the counterintuitive direction (see §7.6). — Source: pool E5D10
- **FACT:** Electrolytic capacitors carry too much series inductance for RF use, an inductor's inter-turn capacitance creates self-resonance (nominal plus parasitic reactances combining), and above self-resonance an inductor turns capacitive. — Source: pool E5D05, E5D06, E5D07
- **FACT:** Reactive power means V and I 90° out of phase — ideal inductors and capacitors store energy in fields and return it, dissipating nothing — hence "wattless, nonproductive power," and only resistance consumes real power: 1 A through 100 Ω + j100 Ω dissipates I²R = 100 W, not 141 or 200 W. — Source: pool E5D03, E5D09, E5D12, E5D11
- **FACT:** The reflection coefficient is Γ = (Z_L − Z₀)/(Z_L + Z₀) with |Γ| = √(P_refl/P_fwd), SWR = (1+|Γ|)/(1−|Γ|), and return loss = −20·log₁₀|Γ| — so 100 W forward and 25 W reflected gives |Γ| = 0.5, SWR = 3:1, and return loss ≈ 6 dB. — Source: pool E4B06, E4B04 (S11↔VSWR equivalence); standard transmission-line relations per research note r3 §E5

### 2.12 Circuit components (E6)

- **FACT:** Donor impurities add free electrons (N-type), acceptor impurities add holes (P-type), and reverse bias pulls carriers away from the junction and widens the depletion region so no current flows. — Source: pool E6A02, E6A04, E6A03
- **FACT:** Gallium arsenide's higher electron mobility suits it to microwave circuits, and gallium nitride supports the highest MMIC operating frequency of the listed materials. — Source: pool E6A01, E6E01, E6E03
- **FACT:** A FET's DC input impedance is far higher than a BJT's because the gate is insulated (MOSFET) or reverse-biased (JFET), and a depletion-mode FET conducts source-to-drain with zero gate voltage while an enhancement-mode device does not. — Source: pool E6A05, E6A09
- **FACT:** Beta is ΔIc/ΔIb (current gain), a forward-biased silicon base-emitter junction drops about 0.6–0.7 V, and alpha cutoff frequency is where the grounded-base current gain falls to 0.7 of its 1 kHz value. — Source: pool E6A06, E6A07, E6A08
- **FACT:** A MOSFET's gate-protection Zener diodes protect against static damage, not overheating or bias referencing. — Source: pool E6A12
- **FACT:** A Zener diode holds a constant voltage drop across varying current (the reference/regulator use), and junction diodes fail from excessive junction temperature — current kills via heat. — Source: pool E6B01, E6B07
- **FACT:** A Schottky diode is a metal-semiconductor junction — low forward drop and fast recovery, good as a VHF/UHF mixer or detector and as an efficient power-supply rectifier (the rectifier advantage is the lower forward drop, not higher reverse breakdown). — Source: pool E6B02, E6B08, E6B06
- **FACT:** An LED's forward voltage is set by the semiconductor band gap, a varactor is a voltage-controlled capacitor, and a PIN diode's RF resistance is set by its forward DC bias current with its low junction capacitance making it a good RF switch. — Source: pool E6B03, E6B04, E6B05, E6B11
- **FACT:** A point-contact diode is an RF detector, not a high-voltage rectifier. — Source: pool E6B09
- **FACT:** Hysteresis stops input noise from chattering a comparator's output, and the comparator flips its output state when the input crosses the threshold voltage. — Source: pool E6C01, E6C02
- **FACT:** Tri-state logic has three output states — 0, 1, and high-impedance (for bus sharing) — and a pull-up or pull-down resistor establishes a defined voltage on an input or output that would otherwise be open-circuit. — Source: pool E6C03, E6C07
- **FACT:** CMOS has the lowest power consumption of the listed logic families and its input switches at about half the supply voltage (hence wide noise margins); BiCMOS combines CMOS's high input impedance with bipolar's low output impedance. — Source: pool E6C05, E6C06, E6C04
- **FACT:** FPGAs are configured in a hardware description language (HDL). — Source: pool E6C09
- **FACT:** Piezoelectricity is two-way — the material generates a voltage when stressed and flexes when a voltage is applied — and a quartz crystal models as a series RLC motional arm in parallel with a shunt capacitance. — Source: pool E6D01, E6D03, E6D02
- **FACT:** Laminations reduce eddy-current power loss, core permeability determines inductance, ferrite needs fewer turns for a given inductance than powdered iron, but powdered iron has the better temperature stability of the listed core materials. — Source: pool E6D04, E6D06, E6D05, E6D08
- **FACT:** A toroid confines most of its magnetic field inside the core (less stray coupling, less pickup), inserting brass into a coil decreases its inductance, and saturation means operation at excessive magnetic flux. — Source: pool E6D10, E6D11, E6D12
- **FACT:** Ferrite beads serve as VHF/UHF parasitic suppressors at transistor amplifier terminals. — Source: pool E6D09
- **FACT:** MMICs are 50-ohm-in/50-ohm-out blocks with controlled gain, low noise figure, and constant input/output impedance over their specified range, bias is supplied through a resistor and/or RF choke on the output lead, and microstrip is the usual MMIC interconnect. — Source: pool E6E06, E6E04, E6E08, E6E07
- **FACT:** A typical low-noise UHF preamplifier noise figure is 0.5 dB. — Source: pool E6E05
- **FACT:** Surface-mount parts have the least parasitic inductance and capacitance above HF (smaller area, shorter traces, less parasitics — all true), while the DIP (dual in-line package, two rows of pins on opposite sides) is the through-hole veteran whose lead length is why it disappears at UHF and above. — Source: pool E6E09, E6E10 (all-of-the-above), E6E02, E6E11, E6E12
- **FACT:** Photons are the particles absorbed in a photovoltaic cell, the photovoltaic effect converts light to electrical energy, PV efficiency is the fraction of light converted to current, and a fully illuminated silicon PV cell gives about 0.5 V open-circuit with silicon the common power-generating PV material. — Source: pool E6F01, E6F04, E6F09, E6F11, E6F10
- **FACT:** Light decreases the resistance of photoconductive material (a crystalline semiconductor is the common one), an optoisolator is an LED-plus-phototransistor pair giving electrical isolation between a control circuit and a 120 VAC switched circuit, a solid-state relay implements relay functions in semiconductors, and a shaft encoder detects rotation by interrupting a light source with a patterned wheel. — Source: pool E6F02, E6F06, E6F03, E6F08, E6F07, E6F05

### 2.13 Practical circuits (E7)

- **FACT:** A flip-flop is bistable (two stable states) and one stage divides a pulse train by 2 — N cascaded stages divide by 2ⁿ, so dividing by 16 takes 4 flip-flops — and a decade counter emits one output pulse per 10 input pulses. — Source: pool E7A01, E7A03, E7A04, E7A02
- **FACT:** An astable multivibrator free-runs between two states with no clock, a monostable flips to its alternate state for a set time then returns, and positive logic assigns high voltage = 1 and low = 0. — Source: pool E7A05, E7A06, E7A11
- **FACT:** NAND is 0 only when all inputs are 1, OR is 1 if any input is 1, and XNOR is 0 when exactly one input is 1 (an equality detector — the XOR truth table is the distractor). — Source: pool E7A07, E7A08, E7A09, E7A10
- **FACT:** The amplifier conduction-angle ladder: class A conducts the entire 360° (operating point about halfway between saturation and cutoff), class AB each push-pull device conducts more than 180° but less than 360°, class B exactly 180°, class C less than 180° (high efficiency, nonlinear — on SSB it produces signal distortion and excessive bandwidth), and class D is a switching amplifier efficient because the device sits at saturation or cutoff most of the time and requiring an output filter to remove harmonic content. — Source: pool E7B04, E7B01, E7B07, E7B02, E7B08, E7B03
- **FACT:** Kill unwanted RF power-amplifier oscillation with parasitic suppressors and/or neutralization, a grounded-grid amplifier has low input impedance, and an emitter follower (common collector) keeps input and output in phase. — Source: pool E7B05, E7B06, E7B09
- **FACT:** Figure E7-1's bias answers: R1 and R2 form voltage divider bias, R3 provides self bias (C3 bypasses it for AC), and the circuit is a common-emitter amplifier. — Source: pool E7B10, E7B11, E7B12; canon §1.4 Figure E7-1
- **FACT:** A low-pass Pi-network is shunt C at input and output with a series L between them, a T-network with series capacitors and a shunt inductor is a high-pass, and a Pi-L adds a series output inductor to a Pi for greater harmonic suppression. — Source: pool E7C01, E7C02, E7C03, E7C07
- **FACT:** A matching network cancels the reactive part of an impedance and transforms the resistive part to the desired value. — Source: pool E7C04
- **FACT:** The filter-family ladder: Butterworth is maximally flat (no ripple), Chebyshev trades passband ripple for a sharp cutoff, and elliptical gives an extremely sharp cutoff with one or more stop-band notches; helical filters are the common VHF/UHF band-pass/notch filters, crystal lattice filters are low-level quartz-crystal filters, and cavity filters serve repeater duplexers — while shape factor measures adjacent-channel rejection. — Source: pool E7C05, E7C06, E7C08, E7C09, E7C10, E7C11
- **FACT:** A linear regulator varies the conduction of a control element to hold the output constant, while a switchmode regulator varies the duty cycle of pulses fed to a filter — high-frequency switching allows much smaller transformers and filter components for the same power, hence lighter and cheaper. — Source: pool E7D01, E7D02, E7D10
- **FACT:** A Zener diode is the stable voltage reference, a three-terminal regulator is a series regulator, a shunt regulator loads the unregulated source, dropout voltage is the minimum input-to-output differential needed to stay in regulation, and a step-start circuit lets filter capacitors charge gradually. — Source: pool E7D03, E7D04, E7D05, E7D12, E7D15
- **FACT:** Figure E7-2's regulator answers: Q1 controls the current to keep the output voltage constant, C2 bypasses rectifier-output ripple around D1, and the circuit is a linear voltage regulator — and series-regulator dissipation is P = (Vin − Vout) × Iout = (25 − 12) × 1 = 13 W in Q1. — Source: pool E7D06, E7D07, E7D08, E7D13; canon §1.4 Figure E7-2
- **FACT:** Battery operating time is amp-hour capacity divided by average current, equal-value resistors across series filter capacitors equalize voltage AND discharge the capacitors AND provide a minimum load (all three), and a solar-panel inverter converts DC to AC. — Source: pool E7D09, E7D14 (all-of-the-above), E7D11
- **FACT:** FM phone is generated by reactance modulation of a local oscillator (never "of the final amplifier"), a discriminator detects FM, and SSB is made by a balanced modulator (cancels carrier) followed by a filter (removes one sideband). — Source: pool E7E01, E7E02, E7E03, E7E04
- **FACT:** Pre-emphasis boosts the higher audio frequencies at the transmitter and de-emphasis in the receiver restores response (keeping compatibility with phase modulation), and baseband is the frequency range the message occupies before modulation. — Source: pool E7E05, E7E06, E7E07
- **FACT:** A mixer outputs the two input frequencies plus their sum and difference, overdriven mixer inputs generate spurious mixer products, an AM envelope detector works by rectification and filtering of the RF, and SSB demodulation needs a product detector. — Source: pool E7E08, E7E09, E7E10, E7E11
- **FACT:** Direct sampling digitizes incoming RF with an ADC — no local oscillator, no mixer — the Hilbert-transform (phasing) method generates SSB by combining signals in quadrature, and an adaptive filter removes unwanted noise from a received SSB signal. — Source: pool E7F01, E7F03, E7F04, E7F02
- **FACT:** Nyquist: sample at least twice the highest frequency component; the FFT converts time domain to frequency domain; decimation reduces the effective sample rate by removing samples, and an anti-alias low-pass must remove the high-frequency components first or they reappear as false low-frequency components. — Source: pool E7F05, E7F07, E7F08, E7F09
- **FACT:** Sample rate sets an SDR's maximum receive bandwidth, while the reference voltage and the sample width in bits set the minimum detectable signal — 1 V range at 1 mV resolution needs 1000 codes, so 10 bits (2¹⁰ = 1024). — Source: pool E7F10, E7F11, E7F06
- **FACT:** FIR filters can delay all frequency components equally (linear phase / constant group delay), the taps provide the incremental delays, and more taps give a sharper filter. — Source: pool E7F12, E7F13, E7F14
- **FACT:** An op-amp is a high-gain, direct-coupled differential amplifier with very high input impedance and very low output impedance; input offset voltage is the differential input voltage needed to bring the open-loop output to zero; gain-bandwidth is the frequency at which the open-loop gain falls to one; an ideal op-amp's gain does not vary with frequency; and ringing in an op-amp audio filter is prevented by restricting both gain and Q. — Source: pool E7G12, E7G01, E7G03, E7G04, E7G06, E7G08, E7G05
- **FACT:** The inverting op-amp gain law is Av = −RF/R1: RF 470/R1 10 → gain 47; −(10,000/1,000) × 0.23 V → −2.3 V out; 68 k/1.8 k → ≈38; 47 k/3.3 k → ≈14; and a capacitor across RF makes the stage a low-pass filter. — Source: pool E7G07, E7G09, E7G10, E7G11, E7G02; canon §1.4 Figure E7-3
- **FACT:** The three common oscillator circuits are Colpitts, Hartley, and Pierce (the Taft/Fenner/Beane names are invented distractors): Colpitts feedback is a capacitive divider and Pierce feedback runs through a quartz crystal. — Source: pool E7H01, E7H04, E7H05
- **FACT:** A PLL is an electronic servo loop — phase detector + low-pass filter + VCO + stable reference oscillator — and it can perform frequency synthesis and FM demodulation. — Source: pool E7H03, E7H06
- **FACT:** A DDS is a phase accumulator + lookup table (amplitude values representing the desired waveform) + DAC + low-pass anti-alias filter, and its spectral impurities are spurious signals at discrete frequencies. — Source: pool E7H09, E7H10, E7H11
- **FACT:** Microphonics is oscillator frequency change caused by mechanical vibration (cured by mechanically isolating the circuit from its enclosure), NP0 capacitors reduce thermal drift, a crystal runs on its specified frequency when given the specified parallel load capacitance, and GPS references, rubidium references, and temperature-controlled dielectric resonators all serve microwave stability (all three). — Source: pool E7H02, E7H07, E7H08, E7H12, E7H13 (all-of-the-above)

### 2.14 Signals and emissions (E8)

- **FACT:** Fourier analysis shows a square wave is a sine plus its odd harmonics, time domain means amplitude at different times, and a true-RMS meter measures RMS for sinusoidal and non-sinusoidal signals alike. — Source: pool E8A01, E8A03, E8A05
- **FACT:** Successive approximation is a type of analog-to-digital conversion, dither is a small amount of noise added to the input to reduce quantization noise, flash (direct) converters serve SDRs because their very high speed digitizes high frequencies, the DAC output low-pass filter removes spurious sampling artifacts, and total harmonic distortion measures ADC quality. — Source: pool E8A02, E8A04, E8A08, E8A10, E8A11
- **FACT:** An 8-bit ADC encodes 2⁸ = 256 input levels. — Source: pool E8A09
- **FACT:** Unprocessed SSB phone has a PEP-to-average power ratio of about 2.5:1, determined by speech characteristics. — Source: pool E8A06, E8A07
- **FACT:** Modulation index = frequency deviation ÷ modulating frequency (3000/1000 = 3 and 6000/2000 = 3), deviation ratio = maximum carrier deviation ÷ highest modulating frequency (5 kHz/3 kHz = 1.67 and 7.5 kHz/3.5 kHz = 2.14), and a phase-modulated emission's index does not depend on the RF carrier frequency — every calculation question offers the inverted ratio as a distractor. — Source: pool E8B01, E8B03, E8B04, E8B09, E8B05, E8B06, E8B02
- **FACT:** OFDM is a digital modulation using subcarriers at frequencies chosen to avoid intersymbol interference, FDM divides the transmitted signal into separate frequency bands each carrying a different data stream, and digital TDM gives two or more signals discrete time slots of one transmission. — Source: pool E8B07, E8B08, E8B10, E8B11
- **FACT:** QAM transmits data by modulating the amplitude of two carriers of the same frequency 90° out of phase, and a constellation diagram shows the possible phase and amplitude states for each symbol. — Source: pool E8C01, E8C13
- **FACT:** Symbol rate is the rate at which the waveform changes to convey information, and symbol rate and baud are the same thing. — Source: pool E8C02, E8C11
- **FACT:** Changing PSK phase at the RF zero crossing minimizes bandwidth, and PSK31 uses sinusoidal data pulses for the same reason. — Source: pool E8C03, E8C04
- **FACT:** CW bandwidth is set by keying speed and rise/fall shape (not power or modulation index) — approximately 4 × WPM, so 13 WPM ≈ 52 Hz. — Source: pool E8C05, E8C12
- **FACT:** An FT8 signal's bandwidth is 50 Hz, and FSK/data bandwidth ≈ (1.2 × frequency shift) + baud — 1.2 × 4800 + 9600 = 15.36 kHz. — Source: pool E8C06, E8C07
- **FACT:** ARQ corrects errors by requesting retransmission when errors are detected, Gray code changes only one bit between sequential code values, and a more efficient digital code raises the data rate without more bandwidth. — Source: pool E8C08, E8C09, E8C10
- **FACT:** Spread-spectrum receivers suppress signals not using the spreading algorithm (hence the interference resistance): direct sequence uses a high-speed binary bit stream to shift the phase of an RF carrier, and frequency hopping rapidly varies the carrier frequency per a pseudorandom sequence — "phase" = direct sequence, "frequency" = hopping. — Source: pool E8D01, E8D02, E8D03
- **FACT:** Extremely short rise and fall times on CW generate key clicks — the cure is increasing the rise and fall times, not output filters. — Source: pool E8D04, E8D05
- **FACT:** Parity bits let some error types be detected (not corrected), the common cause of AFSK overmodulation is excessive transmit audio level (evaluated as intermodulation distortion), and the acceptable maximum IMD for an idling PSK signal is about −30 dB. — Source: pool E8D06, E8D07, E8D08, E8D09
- **FACT:** Baudot carries 5 data bits per character with 2 letters/figures shift codes, while ASCII uses 7 or 8 bits with no shift codes and can transmit both upper- and lowercase text. — Source: pool E8D10, E8D11

### 2.15 Antennas and transmission lines (E9)

- **FACT:** The isotropic radiator is a hypothetical, lossless antenna with equal radiation in all directions — the reference for gain — and a half-wave dipole's gain over isotropic is 2.15 dB, so dBd = dBi − 2.15 (6 dBi = 3.85 dBd). — Source: pool E9A01, E9A12
- **FACT:** ERP is the total radiated-power figure that accounts for all gains and losses, computed ERP = TPO × 10^((gains − losses)/10): 150 W with −2 dB feed line, −2.2 dB duplexer, +7 dBd antenna → net +2.8 dB → 150 × 1.905 ≈ 286 W; 200 W with −4 −3.2 −0.8 dB, +10 dBd → net +2 dB → ≈317 W. — Source: pool E9A03, E9A02, E9A06
- **FACT:** EIRP pairs with dBi where ERP pairs with dBd: 200 W with −2 −2.8 −1.2 dB losses and +7 dBi gain → net +1 dB → 200 × 1.259 ≈ 252 W. — Source: pool E9A07
- **FACT:** Antenna height affects feed-point impedance (line length, tuner settings, and power level do not), ground gain is increased signal strength from ground reflections near the antenna, and the higher the frequency the smaller the first Fresnel zone (5.8 GHz is smallest of the listed bands). — Source: pool E9A04, E9A05, E9A08
- **FACT:** Antenna efficiency is radiation resistance divided by total resistance, a ground radial system improves a ground-mounted quarter-wave vertical, and soil conductivity determines HF vertical ground losses. — Source: pool E9A09, E9A10, E9A11
- **FACT:** Directivity redirects power, it does not create it — a lossless gain antenna and an isotropic radiator driven by the same power radiate the same total power — and the far field is the region where the pattern shape no longer varies with distance. — Source: pool E9B07, E9B08
- **FACT:** Antenna modeling commonly uses the Method of Moments: a wire is modeled as a series of segments each carrying a uniform current, and dropping below about 10 segments per half-wavelength can make the computed feed-point impedance wrong. — Source: pool E9B09, E9B10, E9B11
- **FACT:** Reading Figure E9-1 (free-space azimuth pattern): −3 dB crossings at ±25° give a 50° beamwidth, the 180° response of about −18 dB gives front-to-back 18 dB, and the 90° response of about −14 dB gives front-to-side 14 dB. — Source: pool E9B01, E9B02, E9B03; canon §1.4 Figure E9-1
- **FACT:** Reading Figure E9-2 (elevation pattern over real ground): the pattern type is elevation, the main lobe peaks at 7.5° elevation, and the rear at about −28 dB gives front-to-back 28 dB. — Source: pool E9B05, E9B06, E9B04; canon §1.4 Figure E9-2
- **FACT:** The two-vertical phased-array table: two λ/4 verticals spaced λ/2 and fed 180° out of phase give a figure-eight along the array axis (end-fire); spaced λ/4 and fed 90° out of phase give a cardioid; spaced λ/2 and fed in phase give a figure-eight broadside to the array axis. — Source: pool E9C01, E9C02, E9C03
- **FACT:** Lengthening an unterminated long wire forms additional lobes that align increasingly with the wire axis, and a terminating resistor makes a rhombic or long-wire pattern unidirectional (bidirectional otherwise). — Source: pool E9C04, E9C06
- **FACT:** An OCFD is fed off-center to create a similar feed-point impedance on multiple bands, a folded dipole is a λ/2 dipole with an additional parallel wire connecting its ends and presents about 300 Ω, a G5RV is a center-fed wire through a specific length of open-wire line to a balun and coax, a Zepp is an end-fed half-wavelength antenna, and an extended double Zepp is a center-fed 1.25λ antenna. — Source: pool E9C05, E9C07, E9C08, E9C09, E9C10, E9C12
- **FACT:** Mounting an antenna over seawater increases low-angle radiation versus soil, raising a horizontally polarized antenna lowers its lowest-lobe takeoff angle, and a long downhill slope lowers the main-lobe takeoff angle in the downhill direction. — Source: pool E9C11, E9C13, E9C14
- **FACT:** Doubling the operating frequency increases an ideal parabolic reflector's gain by 6 dB (the dish is twice as many wavelengths across). — Source: pool E9D01
- **FACT:** Circular polarization from linear Yagis takes two Yagis on the same axis, perpendicular to each other, driven elements at the same point on the boom, fed 90° out of phase. — Source: pool E9D02
- **FACT:** The most efficient loading-coil location on a short whip is near the center of the radiator, loading coils should have a high reactance-to-resistance ratio to maximize efficiency, a loading coil cancels the short antenna's capacitive reactance to resonate it — but Q rises and SWR bandwidth decreases. — Source: pool E9D03, E9D04, E9D09, E9D06, E9D08
- **FACT:** Top loading improves radiation efficiency, below resonance a base-fed whip's radiation resistance decreases, a Yagi's driven element is approximately a half wavelength, two-element Yagis favor a reflector over a director for higher gain, and parasitic elements are made longer or shorter than resonance to control phase shift. — Source: pool E9D07, E9D10, E9D05, E9D11, E9D12
- **FACT:** A gamma match connects the coax shield to the element center and the center conductor (through a series capacitor that cancels the gamma section's inductive reactance) to a point a fraction of a wavelength off-center — it is also the match used to shunt-feed a grounded tower at its base. — Source: pool E9E02, E9E04, E9E09
- **FACT:** A beta (hairpin) match needs a driven element electrically shorter than λ/2 (capacitive feed-point impedance) and requires the element insulated from the boom, and a stub match is a short length of transmission line in parallel with the feed line at or near the feed point. — Source: pool E9E01, E9E05, E9E03
- **FACT:** A quarter-wave Q-section's impedance is the geometric mean Z₀ = √(Z_line × Z_load) — √(50 × 100) = 70.7 Ω, so 75 Ω line is the suitable choice. — Source: pool E9E06
- **FACT:** The reflection coefficient describes the interaction of a load and a transmission line, a Wilkinson divider splits power equally between two 50 Ω loads while maintaining a 50 Ω input impedance, and multiple driven elements connected through phasing lines control the antenna's radiation pattern. — Source: pool E9E07, E9E08, E9E11
- **FACT:** Velocity factor is the wave velocity in the line divided by the velocity of light in a vacuum, the dielectric insulating material has the biggest effect on it, and electrical length exceeds physical length because waves move slower in the line — a λ/2 air-insulated parallel line at 14.10 MHz is about 10.6 m long (λ/2 ≈ 150 × VF / f(MHz) with air VF ≈ 1.0). — Source: pool E9F01, E9F02, E9F03, E9F06
- **FACT:** Open-wire parallel line has lower loss than plastic-dielectric coax, and foam versus solid dielectric coax (all else equal) has lower safe operating voltage AND lower loss per length AND higher velocity factor — all three. — Source: pool E9F07, E9F08 (all-of-the-above)
- **FACT:** Microstrip is precision PCB conductors above a ground plane, giving constant-impedance interconnects at microwave frequencies. — Source: pool E9F05
- **FACT:** The transmission-line transformation table: a λ/2 line repeats its termination (shorted far end → very low impedance at the input); a λ/4 line inverts its termination (shorted → very high impedance, open → very low); a λ/8 line converts to reactance (shorted → inductive, open → capacitive). — Source: pool E9F04, E9F09, E9F12, E9F10, E9F11
- **FACT:** A Smith chart plots normalized impedance on a coordinate system of resistance circles and reactance arcs — it is used to calculate impedance along transmission lines and impedance/SWR values, and its classic use is determining the length and position of an impedance-matching stub. — Source: pool E9G01, E9G03, E9G05, E9G10
- **FACT:** Normalizing on a Smith chart means reassigning the prime center's impedance value to the system impedance (1.0 = 50 Ω), a third family of constant-SWR circles centered on the prime center is added during matching-network design, and the rim's wavelength scales are calibrated in fractions of transmission-line electrical wavelength. — Source: pool E9G08, E9G09, E9G11
- **FACT:** On Figure E9-3, the large outer circle on which the reactance arcs terminate is the reactance axis, and the only straight line (the horizontal diameter) is the resistance axis. — Source: pool E9G06, E9G07; canon §1.4 Figure E9-3
- **FACT:** A Beverage should be at least one wavelength long, its terminating resistor absorbs signals arriving from the reverse direction, and the correct termination value is indicated by minimum SWR variation over the desired frequency range. — Source: pool E9H01, E9H06, E9H07
- **FACT:** On 160 and 80 meters atmospheric noise is so high that directivity matters far more than losses in a receiving antenna, and the receiving directivity factor (RDF) is peak antenna gain compared to average gain over the hemisphere around and above the antenna. — Source: pool E9H02, E9H03
- **FACT:** An electrostatic shield around a small DF loop eliminates unbalanced capacitive coupling to the surroundings (improving null depth), a small wire loop's DF challenge is its bidirectional null pattern (180° ambiguity), a sense antenna modifies the DF pattern to provide a null in only one direction, a terminated single-turn loop such as a pennant is cardioid, and more turns and/or more enclosed area increases a multiturn loop's output voltage. — Source: pool E9H04, E9H05, E9H08, E9H09, E9H10, E9H11

### 2.16 Safety and RF exposure (E0)

- **FACT:** The primary function of an external earth connection (ground rod) is lightning charge dissipation. — Source: pool E0A01
- **FACT:** A neighbor's home is general-population territory, so the station's signals there must meet the uncontrolled MPE limits. — Source: pool E0A02
- **FACT:** FCC human-body RF exposure (MPE) limits are most restrictive over 30–300 MHz — the body-resonance region. — Source: pool E0A03
- **FACT:** At a multi-transmitter site, every transmitter producing 5 percent or more of its MPE limit in an area where the total limit is exceeded shares responsibility for mitigation. — Source: pool E0A04
- **FACT:** The microwave hazard is that the commonly used high-gain antennas can produce high exposure levels, and below 300 MHz separate E- and H-field limits exist because the body reacts to both fields and their intensity peaks can occur at different locations (both clauses true). — Source: pool E0A05, E0A06 (all-of-the-above)
- **FACT:** SAR (specific absorption rate) measures the rate at which RF energy is absorbed by the body. — Source: pool E0A08
- **FACT:** Hand-held transceivers sold before May 3, 2021 are exempt from RF exposure evaluations, and on 80 meters an RF exposure evaluation must always be performed. — Source: pool E0A09, E0A10 (these rest on Part 1/2 text — §1.1307/§1.1310 and OET Bulletin 65 — not Part 97; see §7.6)
- **FACT:** 100% tie-off means at least one lanyard is attached to the tower at all times, lanyards attach to tower legs, and a shock-absorbing lanyard anchors above the climber's head level. — Source: pool E0A07, E0A11, E0A12
- **FACT:** The pool requires no MPE computation — all twelve E0A questions are conceptual/regulatory (any far-field power-density illustration S = ERP/(4πR²) in ch10 must be flagged as enrichment, not exam math). — Source: research note r4 §E0A (full read of the group)

---

## 3. Notation & Units

One consistent style for the whole book — identical to Books 2 and 3 wherever the three overlap. Frequencies are in hertz with kHz/MHz/GHz as convenient; wavelength in meters; metric throughout, with US-conventional ham units only where the hobby genuinely uses them (feet for antenna lengths and tower clearances, miles for propagation path lengths — the Extra pool itself prints "12,000 miles," "10.6 meters," "approximately 2,000 miles to 3,000 miles").

| Symbol | Quantity | Unit | Canonical relation / note |
|---|---|---|---|
| V | Voltage (EMF) | volt (V) | **V = I × R** (Ohm's law); prose uses V, never E (see below) |
| I | Current | ampere (A) | I = V / R; the flow of electrons |
| R | Resistance | ohm (Ω) | R = V / I; dissipates power (the only element that does) |
| P | Power | watt (W) | **P = V × I = I² × R = V² / R**; real (average) power |
| Q | Reactive power ("wattless") | var | Q = V × I × sin θ; stored and returned, never dissipated |
| f | Frequency | hertz (Hz; kHz, MHz, GHz) | Cycles per second; f = 1 / T |
| f₀ | Resonant frequency | hertz | **f₀ = 1/(2π√(LC))** |
| λ | Wavelength | meter (m) | **λ = c / f**; the band-name basis |
| c | Speed of light | m/s | ≈ 3×10⁸ m/s = 300,000 km/s (working value); 299,792,458 m/s (exact) |
| C | Capacitance | farad (F) | Energy stored in an electric field |
| L | Inductance | henry (H) | Energy stored in a magnetic field |
| X | Reactance | ohm (Ω) | Opposition to AC from L or C; **X_L = 2πfL**, **X_C = 1/(2πfC)** |
| Z | Impedance | ohm (Ω) | Complex: **Z = R ± jX** rectangular; **\|Z\| = √(R² + X²)**, θ = atan(X/R) polar |
| j | The j-operator | — | j rotates a phasor +90°; **+j inductive, −j capacitive** (E5C01, E5C03) |
| ∠ | Phase-angle marker | degree (°) | polar form **\|Z\| ∠θ** (e.g., 55.9 ∠−26.6° Ω); degrees always |
| Y | Admittance | siemens (S) | **Y = 1/Z = G + jB**; \|Y\| = 1/\|Z\|, ∠Y = −∠Z |
| G | Conductance | siemens (S) | The real part of admittance |
| B | Susceptance | siemens (S) | The imaginary part of admittance — the letter is B |
| τ | Time constant | second (s) | **τ = R × C** or **τ = L / R**; 63.2% charge / 36.8% discharge per τ |
| ω | Angular frequency | rad/s | ω = 2πf; appears inside X_L = ωL, X_C = 1/(ωC) forms |
| Q (quality) | Figure of merit | — | series **Q = X/R**, parallel **Q = R/X**; **BW = f₀/Q** |
| Γ | Reflection coefficient | — | **Γ = (Z_L − Z₀)/(Z_L + Z₀)**; \|Γ\| = √(P_refl/P_fwd); SWR = (1+\|Γ\|)/(1−\|Γ\|) |
| SWR | Standing wave ratio | — | Always ≥ 1, larger number first ("3:1") |
| N | Turns (transformer) | — | V_s = V_p × (N_s/N_p); Z_p/Z_s = (N_p/N_s)² |

**The wavelength shortcut:** the book states, as the pool's own formula family, **λ(m) = 300 / f(MHz)** — an approximation of c = f·λ with c ≈ 3×10⁸ m/s, never an exact identity (series-identical to Books 2 and 3; the Extra pool's own line-length math, E9F06's 10.6 m at 14.10 MHz, is this shortcut with velocity factor 1.0: L(λ/2, m) ≈ 150 × VF / f(MHz)).

**Decibels:** anchors first, series-identical to Books 2 and 3 — **3 dB ≈ double power, 6 dB ≈ four times power (so −6 dB ≈ one quarter), 10 dB = ten times power, 20 dB = 100 times power, one S unit ≈ 6 dB, and a 1 dB loss leaves 0.794 of the power (−20.6%)**. As in Book 3, the defining formula **dB = 10·log₁₀(P₂/P₁)** is first-class exam math here (E4C06, E4D12–E4D14, E9A02–E9A07), taught with worked pool numbers. Extra additions, stated openly: **dBm** is decibels relative to 1 milliwatt (0 dBm = 1 mW; 30 dBm = 1 W), with P(W) = 10^((dBm−30)/10) — the receiver noise floor is −174 dBm in 1 Hz at room temperature, and −100 dBm = 0.1 pW; and ratios of *amplitudes* (not powers) use 20·log₁₀, as in return loss = −20·log₁₀|Γ|.

**Complex-number conventions (new to the series at Extra depth, binding):** impedance is a complex quantity written **rectangular** (Z = R ± jX: resistance plus signed reactance, +j inductive and −j capacitive) or **polar** (|Z| ∠θ: magnitude and phase angle in degrees). Conversions: |Z| = √(R² + X²), θ = atan(X/R); back via R = |Z|cos θ, X = |Z|sin θ. The **j-operator** marks the 90° rotation between resistance and reactance (the book uses j, the engineering convention, never the mathematician's i). Admittance mirrors it: Y = G + jB in siemens, with the polar angle negated. The 2024–2028 Extra pool prints complex impedances in ASCII j-form ("0 - j100", "50 - j25 ohms") with a hyphen minus; prose writes 0 − j100 and 50 − j25 Ω with the house minus sign and the Ω symbol — and verbatim pool quotes always keep the pool's own typography byte-exact.

**Pool-notation equivalence (binding, series-consistent):** prose in this book uses **V** for voltage and **×** as the multiplication sign (V = I × R, P = V × I), exactly as Books 2 and 3 do. The 2024–2028 Extra pool states electrical quantities in words ("a 400-ohm resistor and a 38-picofarad capacitor") and prints angles and the j-operator in ASCII ("90 degrees", "0 - j100") — the only non-ASCII characters anywhere in the pool text are its curly apostrophes and quotes (§1.2), so verbatim pool quotes never conflict with the prose convention. Where the book refers back to Book 2's E-notation equivalence ("E and V both mean volts"), a single parenthetical suffices.

**The Extra formula set (canonical relations — Appendix B reproduces this table; each formula is used at least once in its chapter with pool numbers):**

| Formula | Name | Pool worked example |
|---|---|---|
| X_L = 2πfL | Inductive reactance | 18 µH at 3.505 MHz ≈ 400 Ω (E5C11) |
| X_C = 1/(2πfC) | Capacitive reactance | 38 pF at 14 MHz ≈ 300 Ω (E5C10); 19 pF at 21.2 MHz ≈ 400 Ω (E5C12) |
| f₀ = 1/(2π√(LC)) | Resonant frequency | 50 µH + 40 pF → 3.56 MHz (E5A02); 50 µH + 10 pF → 7.12 MHz (E5A10) |
| X_L = X_C at resonance | Resonance condition | Series RLC → minimum impedance; parallel → maximum (E5A03–E5A08) |
| BW = f₀/Q | Half-power bandwidth | 7.1 MHz/150 = 47.3 kHz (E5A11); 3.7 MHz/118 = 31.4 kHz (E5A12); inverse Q = f/BW (E4B08) |
| series Q = X/R; parallel Q = R/X | Circuit Q | Definition (E5A09); loaded Q always lower than unloaded |
| V_L = V_C ≈ Q × V_applied | Resonant voltage rise | Concept (E5A01, E5A13) |
| τ = R × C; τ = L/R | Time constant | 440 µF × 500 kΩ = 220 s (E5B04) |
| 63.2% charge / 36.8% discharge per τ | RC percentages | Definition (E5B01) |
| \|Z\| = √(R² + X²); θ = atan(X/R) | Rectangular → polar | 50 − j25 → 55.9 ∠−26.6° Ω (E5C06) |
| R = \|Z\|cos θ; X = \|Z\|sin θ | Polar → rectangular | Same family |
| θ = atan((X_L − X_C)/R) | Series RLC phase angle | −14.0° lags (E5B07); −63° lags (E5B08); +27° leads (E5B11) |
| Y = 1/Z = G + jB; \|Y\| = 1/\|Z\|, ∠Y = −∠Z | Admittance | Definitions (E5B02, E5B03, E5B05, E5B06, E5B12) |
| P_real = I²R = VI·cos θ; Q = VI·sin θ | Real vs reactive power | 1 A × 100 Ω → 100 W, the j100 term adds zero (E5D11) |
| Γ = (Z_L − Z₀)/(Z_L + Z₀); \|Γ\| = √(P_r/P_f) | Reflection coefficient | √(25/100) = 0.5 (E4B06 numbers) |
| SWR = (1+\|Γ\|)/(1−\|Γ\|) | SWR from Γ | 0.5 → 3:1 |
| return loss = −20·log₁₀\|Γ\| | Return loss | 0.5 → ≈6.0 dB |
| P_load = P_fwd − P_refl | Absorbed power | 100 − 25 = 75 W (E4B06) |
| ΔdB = 10·log₁₀(BW₂/BW₁) | Noise floor vs bandwidth | 50 Hz → 1,000 Hz = 13 dB (E4C06) |
| P(W) = 10^((dBm−30)/10) | dBm ↔ watts | −100 dBm = 10⁻¹³ W = 0.1 pW (E4D14) |
| P_rx = P_tx + G_tx + G_rx − losses − path loss | Link budget | 40 + 6 + 3 − 100 = −51 dBm (E4D13) |
| margin = P_rx − MDS − required SNR | Link margin | −89 − (−103) − 6 = +8 dB (E4D12) |
| Z_in = (Ω/V) × full-scale voltage | Voltmeter input impedance | 20 kΩ/V × 10 V = 200 kΩ (E4B02) |
| ERP = TPO × 10^((gains − losses)/10) | ERP / EIRP | 286 W (E9A02); 317 W (E9A06); 252 W EIRP (E9A07) |
| dBd = dBi − 2.15 | Gain units | 6 dBi = 3.85 dBd (E9A12) |
| Av = −RF/R1; Vout = −(RF/R1)·Vin | Inverting op-amp gain | 47 (E7G07); −2.3 V (E7G09); ≈38 (E7G10); ≈14 (E7G11) |
| P = (V_in − V_out) × I_out | Series-regulator dissipation | (25 − 12) V × 1 A = 13 W (E7D13) |
| operating time = amp-hours / average current | Battery time | Concept (E7D09) |
| n bits → 2ⁿ levels | ADC resolution | 8 bits = 256 levels (E8A09); 1 V at 1 mV → 10 bits (E7F06) |
| sample rate ≥ 2 × highest component | Nyquist rate | ≥ 30 kHz for a 15 kHz signal (E7F05) |
| index = Δf / f_mod | Modulation index | 3000/1000 = 3 (E8B03); 6000/2000 = 3 (E8B04) |
| deviation ratio = max Δf / max f_mod | Deviation ratio | 5/3 = 1.67 (E8B05); 7.5/3.5 = 2.14 (E8B06) |
| BW ≈ 4 × WPM | CW bandwidth | 13 WPM ≈ 52 Hz (E8C05) |
| BW ≈ (1.2 × shift) + baud | FSK/data bandwidth | 1.2 × 4800 + 9600 = 15.36 kHz (E8C07) |
| L(λ/2, m) ≈ 150 × VF / f(MHz) | Physical line length | 10.6 m at 14.10 MHz, VF ≈ 1.0 (E9F06) |
| Z₀ = √(Z_line × Z_load) | Q-section (λ/4 transformer) | √(50 × 100) = 70.7 → 75 Ω (E9E06) |
| λ(m) = 300 / f(MHz) | Wavelength shortcut | Series-identical (underlies E9F06) |
| S = ERP / (4πR²) | Far-field power density | **Enrichment only** — no E0A question requires it (flag in ch10) |

**Unit style rules (series-identical to Books 2 and 3, with Extra additions):**

- Case is load-bearing: **kHz** (lowercase k), **MHz** and **GHz** (capital M/G), always capital **H**; **mA**, **µV**, **pF**, **nF**, **kV** follow the same prefix case rules. Never "KHZ," "mhz," or "Mhz."
- Prefix ladder for conversions: pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); moving toward a smaller unit multiplies, toward a larger unit divides. (The E5C figure questions are the pool's own pF/µH drills.)
- Band names take the meter spelling with a numeral ("40 meters," "70 centimeters," "23 cm" in tables); frequency ranges are written with an en dash and units once ("14.150–14.225 MHz").
- Power limits are written "200 W PEP," "1.5 kW PEP," "1500 watts," "100 W ERP," "9.15 W ERP," "1 W EIRP," "5 W EIRP" matching the rules' and pool's own phrasing where quoted.
- Antenna lengths from the 468/f and 234/f formulas come out in **feet** and are stated as approximate; transmission-line electrical/physical lengths from the 150 × VF / f formula come out in **meters** (the pool's own E9F06 unit).
- Coax loss is quoted in **dB per 100 feet**; antenna gains in **dBi** or **dBd** with the reference always named.
- SWR is always written with the larger number first — "3:1," "4:1," never "1:3."
- Complex impedances are written with the house minus sign and the j attached to the number — "400 − j300 Ω", "50 − j25 Ω" — and polar form with the angle marker and degrees: "55.9 ∠−26.6° Ω" (quotes from the pool keep the pool's ASCII forms byte-exact).
- SSB dial readings are suppressed-carrier frequencies; sideband occupancy is written "the signal occupies 14.347–14.350 MHz," not by edge-frequency shorthand alone.
- Subscripts are set as subscripts in prose and math alike: X_L, X_C, f₀, Z₀, P_fwd, P_refl, S21, S11.
- Inline math in chapters uses the `$…$` renderer (matplotlib mathtext); at most one `$…$` span per paragraph and no literal `$` inside a math paragraph (write "35 dollars" in prose). The renderer's subset supports subscripts ($X_L$), Greek letters ($\Gamma$, $\tau$, $\omega$), $\pi$, $\sqrt{}$, and fractions — the whole Extra formula set above.

---

## 4. Glossary

Canonical plain-language one-line definitions, consolidated from the r3/r4/r5 vocabulary lists. These are binding — a chapter may expand a definition but must not contradict it — and this table feeds Appendix B directly. Series law: where a term also appears in Book 2's or Book 3's canon §4, the definition below is the earlier book's **verbatim** (the only exceptions are pool-specific cross-reference tails — figure and comparison parentheticals — which point at this book's pool figures and pool facts). Terms new to the Extra course carry new definitions in the same style.

| Term | Definition |
|---|---|
| 100% tie-off | Tower-climbing discipline in which at least one lanyard is attached to the tower at all times. |
| 304A index | The solar UV flux measured at 304 angstroms, correlated to the solar flux index. |
| A-index | The long-term (daily) index of geomagnetic stability. |
| AC (alternating current) | Current that alternates between positive and negative directions. |
| Acceptor impurity | A dopant that adds holes, making P-type semiconductor. |
| Adaptive filter | A DSP filter that adjusts itself to remove unwanted noise from a received signal. |
| ADIF | Amateur Data Interchange Format — the standard log-data exchange format. |
| Admittance | The reciprocal of impedance — how easily AC flows. |
| AFSK | Audio frequency-shift keying — digital data sent as shifting audio tones into a voice transmitter. |
| AGC (automatic gain control) | Receiver circuit that automatically turns gain down on strong signals to keep audio level. |
| ALC (automatic level control) | The transmitter feedback circuit that limits drive to prevent overload — set it so it just begins to work on peaks. |
| ALE | Automatic Link Establishment — a system that constantly scans a frequency list and activates on the designated call sign. |
| Aliasing | The false low-frequency copy produced when a scope or ADC undersamples a signal. |
| Allocation | A frequency band assignment made to a radio service by regulation. |
| Alpha cutoff frequency | The frequency where a transistor's grounded-base current gain falls to 0.7 of its 1 kHz value. |
| AM (amplitude modulation) | Impressing information on a carrier by varying its amplitude; SSB is a form of AM. |
| Amateur Extra | The highest US license class, conveying all available US amateur privileges on all bands and modes. |
| Ampere (A) | The unit of electric current. |
| Ampere-hour (Ah) | A battery capacity unit: one ampere flowing for one hour. |
| AND gate | A digital gate whose output is high only when both inputs are high. |
| Antenna analyzer | An instrument that tells whether an antenna is resonant at a chosen frequency. |
| Antenna tuner (coupler/transmatch) | A device that matches the antenna system impedance to the transceiver's 50-ohm output. |
| Anode | The diode electrode current enters in the forward direction. |
| AOS / LOS | Acquisition and loss of signal — the rise and set of a satellite pass. |
| APRS | Automatic Packet Reporting System — AX.25 UI-frame beacons for position and telemetry, relayed by digipeaters. |
| AREDN | Amateur Radio Emergency Data Network — high-speed mesh data networking on microwave amateur allocations for emergencies and community events. |
| ARQ (automatic repeat request) | Error recovery in which the receiver detects errors and requests retransmission. |
| ARES | Amateur Radio Emergency Service — licensed amateurs who voluntarily registered their qualifications and equipment for public-service duty. |
| Ascending pass | A satellite pass traveling south to north, crossing the equator going up. |
| ASCII | The 7- or 8-bit text code needing no letters/figures shift — it sends upper- and lowercase alike. |
| Astable multivibrator | A circuit that free-runs between two states with no clock. |
| Attenuator (receiver) | A switchable pad that reduces incoming signal strength to prevent receiver overload. |
| Auroral backscatter | VHF signals returned by the aurora, distorted with a characteristic raspy sound. |
| Automatic control | Operation of a transmitting station by devices and procedures without the control operator present at a control point. |
| Auxiliary station | An amateur station transmitting point-to-point communications within a system of cooperating stations, such as a repeater's remote link. |
| Average power | Power averaged over a full modulation cycle — what heats the finals; PEP measures the crest instead. |
| AX.25 | The amateur packet protocol APRS runs on. |
| Balanced modulator | The circuit that produces double-sideband suppressed-carrier RF — the first step in making SSB. |
| Band gap | The semiconductor energy gap that sets an LED's forward voltage (and color). |
| Band plan | A voluntary community guideline for which modes and activities live where within a band. |
| Bandwidth | The width of spectrum a signal occupies (e.g., ≈3 kHz for SSB voice). |
| Baseband | The frequency range a message occupies before modulation. |
| Baud | The symbol rate of a digital signal — symbols per second. |
| Baudot code | The 5-bit RTTY code sent with start and stop bits (45.45 baud on HF). |
| Beacon (propagation) | An amateur station transmitting for observation of propagation and reception (on HF, 28.200–28.300 MHz on 10 m). |
| Beam antenna | A directional antenna that concentrates signals in one direction. |
| Beamwidth | The angular width of an antenna's main lobe, measured between its −3 dB points. |
| Beta (β) | A bipolar transistor's current gain, ΔIc/ΔIb. |
| Beta match (hairpin) | A shorted stub at the antenna feed point used for matching. |
| Beverage antenna | A long low wire used as a directional receiving antenna on MF and low HF. |
| BiCMOS | A logic family combining CMOS's high input impedance with bipolar's low output impedance. |
| Bidirectional null | The 180°-ambiguous two-way null of a small DF loop. |
| Bistable | Having two stable states — the defining property of a flip-flop. |
| BJT (bipolar junction transistor) | A transistor family whose electrodes are emitter, base, and collector. |
| Bleeder resistor | The resistor that discharges a power supply's filter capacitors when power is removed — a safety device. |
| Blocking dynamic range | The dB span from a receiver's noise floor to the level causing 1 dB of gain compression. |
| Bonding | Electrically connecting equipment and ground rods with low-inductance conductors so everything sits at the same potential. |
| Boom | The longitudinal spine of a Yagi that the elements mount on. |
| Broadside | The direction perpendicular to a dipole's wire, where it radiates strongest. |
| Broadcasting | Transmissions intended for reception by the general public — prohibited in the amateur service. |
| Brute-force line filter | A heavy AC-line filter wired in series with a noise source's leads (the AC-motor RFI cure). |
| Butterworth filter | The maximally flat filter family — no passband ripple. |
| Bypass capacitor | A capacitor that shunts RF to ground, curing RFI in audio circuits. |
| Bz | The north–south component of the interplanetary magnetic field; southward Bz couples solar-wind energy into the magnetosphere. |
| Cabrillo | The standard format for submitting a contest log. |
| Calling frequency | The customary meeting frequency of a band or mode (50.125, 144.200, 222.100, 432.100 MHz on the VHF/UHF weak-signal bands) — raise a station there, then move up the band. |
| Capacitance | The ability to store energy in an electric field; unit farad. |
| Capacitor | A component that stores energy in an electric field — two conductive plates separated by a dielectric. |
| Capture effect | The FM receiver behavior in which the stronger co-channel signal suppresses the weaker. |
| Cardioid pattern | A heart-shaped antenna pattern with a single deep null — from phased verticals, a terminated pennant loop, or a sense-antenna-equipped DF loop. |
| Carrier | The unmodulated RF signal onto which information is impressed. |
| Cathode | The diode electrode current exits in the forward direction; the package end is often marked with a stripe. |
| Cavity filter | A high-Q resonant-cavity filter — the building block of repeater duplexers. |
| CEPT | The European conference whose Recommendation T/R 61-01 lets US Extra and Advanced licensees operate in participating countries (carry Public Notice DA 16-1048, proof of citizenship, and evidence of the FCC grant). |
| Charge controller | The regulator between a solar panel and a battery; lithium iron phosphate batteries require one. |
| Chebyshev filter | The filter family that trades passband ripple for a sharp cutoff. |
| Chordal hop | Successive ionospheric refractions with no intermediate ground reflection — less loss than ordinary multi-hop. |
| Circular polarization | A wave whose field rotates as it advances — from crossed Yagis fed 90° out of phase; fights spin modulation and Faraday rotation on satellite paths. |
| Circulating current | The large current inside a parallel-resonant L–C loop at resonance, even as input current falls to a minimum. |
| Circulator | A one-way RF junction device; properly terminated on a transmitter output, it isolates the amplifier from returning energy. |
| Class A amplifier | An amplifier conducting 100% of the cycle — linear but inefficient. |
| Class AB amplifier | The push-pull class in which each device conducts more than 180° but less than 360° of the cycle. |
| Class B amplifier | The push-pull class in which each device conducts exactly 180° of the cycle. |
| Class C amplifier | The highest-efficiency amplifier class — constant-envelope modes only (FM yes; SSB and AM no). |
| Class D amplifier | A switching amplifier, efficient because the device sits at saturation or cutoff; needs an output filter to strip harmonics. |
| CMOS | The digital IC family that beats TTL on power consumption. |
| Coaxial cable (coax) | A shielded feed line with a center conductor inside a cylindrical braid; amateur coax is usually 50 ohms. |
| Colpitts oscillator | The oscillator whose feedback path is a capacitive divider. |
| Common-mode current | RF current flowing on the outside of a cable shield — choked with a ferrite bead. |
| Comparator | The IC that flips its output state when the input crosses a threshold voltage. |
| Conductance (G) | The real part of admittance; unit siemens. |
| Conductor | A material that carries current easily because it has many free electrons. |
| Constellation diagram | The display of a digital signal's possible phase and amplitude states for each symbol. |
| Contest exchange | The minimum information that scores a contest contact: call sign, signal report, plus the sponsor's defined fields. |
| Control operator | The licensed amateur designated by the station licensee to be responsible for the station's transmissions. |
| Control point | The location at which the control operator function is performed. |
| Controlled environment | The RF-exposure category for people aware of and able to control their exposure (occupational-level limits; may apply to household members). |
| CORES | The FCC's COmmission REgistration System, where you register to get an FRN. |
| Coronal mass ejection (CME) | A burst of solar particles that reaches Earth in 15 hours to several days and disturbs the geomagnetic field. |
| Cross-modulation | Modulation of a desired signal by a strong undesired one — a symptom of poor dynamic range. |
| Crystal lattice filter | A narrow band-pass filter for low-level signals, built from quartz crystals. |
| CSCE | Certificate of Successful Completion of Examination — the VEs' proof you passed, valid 365 days for element credit. |
| Current | The flow of electrons in a circuit; unit ampere. |
| Cut numbers | CW contest shorthand where letters stand in for digits (N for 9, T for 0) — "599" sent as "5NN." |
| Cutoff | The fully-off endpoint of a switching transistor's operation. |
| Cutoff frequency | The half-power point of a low-pass filter. |
| CW | Continuous wave — a carrier keyed on and off; simply another name for a Morse code transmission. |
| D region | The lowest ionospheric region — the daytime absorber of the low HF bands, fading at night. |
| dBd | Antenna gain relative to a half-wave dipole. |
| dBi | Antenna gain relative to an isotropic radiator — dBi = dBd + 2.15. |
| dBm | Decibels relative to 1 milliwatt (0 dBm = 1 mW) — the unit of receiver noise floors and link budgets. |
| DC (direct current) | Current that flows steadily in one direction. |
| DDS (direct digital synthesis) | A frequency-generation technique giving variable frequency with crystal-oscillator stability. |
| Decade counter | A counter emitting one output pulse per 10 input pulses. |
| Decibel (dB) | A logarithmic ratio unit: +3 dB ≈ double power, +10 dB = ten times power. |
| Decimation | Reducing the effective sample rate by removing samples — with an anti-alias filter first. |
| De-emphasis | The receiver-side treble cut that restores response after the transmitter's pre-emphasis. |
| Depletion-mode FET | A FET that conducts source-to-drain with zero gate voltage. |
| Depletion region | The carrier-free zone at a reverse-biased PN junction. |
| Desensitization | Receiver sensitivity loss caused by a strong nearby signal. |
| Deviation | The peak amount an FM carrier's frequency swings with modulation; too much is over-deviation. |
| Deviation ratio | Maximum carrier deviation divided by the highest modulating frequency — the worst-case sibling of the modulation index. |
| Dielectric | The insulating material between a capacitor's plates (or inside a coaxial cable). |
| Differential-mode current | The ordinary signal current flowing out on one conductor and back on the other — the opposite of common-mode. |
| Digipeater | A packet-radio relay station; APRS paths count its hops (WIDE3-1 = three requested, one remaining). |
| Digital mode | A mode carrying data rather than analog voice — packet radio, FT8, even IEEE 802.11 under amateur rules. |
| Diode | A semiconductor that lets current flow in only one direction. |
| DIP (dual in-line package) | The classic through-hole IC package, two rows of pins on opposite sides — its lead length is why it disappears at UHF. |
| Dipole | A straight antenna, usually a half wavelength long, fed at the center. |
| Direct sampling | Digitizing incoming RF with an ADC — no local oscillator, no mixer. |
| Direct sequence | The spread-spectrum technique that shifts an RF carrier's phase with a high-speed binary bit stream. |
| Direction finding (DF) | Locating a transmitter with directional receiving antennas and null readings. |
| Director | The Yagi element shorter than the driven element, sitting in the direction of maximum radiation. |
| Directional wattmeter | An instrument reading forward and reflected power, used to determine SWR. |
| Discriminator | The FM detector. |
| Dither | A small amount of noise added to a converter's input to reduce quantization noise. |
| Donor impurity | A dopant that adds free electrons, making N-type semiconductor. |
| Doppler shift | The frequency shift from relative motion between station and satellite — a few kHz on VHF, tens of kHz on UHF for LEO. |
| Driven element | The Yagi element connected to the feed line, approximately a half wavelength long. |
| Dropout voltage | The minimum input-to-output differential a regulator needs to stay in regulation. |
| DSP (digital signal processing) | Signal manipulation in software — DSP filters realize bandwidths and shapes analog filters cannot. |
| Dual-gate MOSFET | A MOSFET with two insulated gates (G1, G2) — symbols 4 and 5 in pool Figure E6-1. |
| Duplexer | The cavity-filter assembly that lets a repeater transmit and receive on one antenna at once. |
| Duty cycle | The percentage of time that a transmitter is transmitting during the averaging time for RF exposure. |
| DVB-T | The digital TV standard amateur DATV uses, with QAM and QPSK modulation. |
| E region | The ionospheric region above the D region — one-hop reach about 1,200 miles. |
| Eddy currents | Circulating core currents whose power loss laminations reduce. |
| EIRP | Effective radiated power computed relative to an isotropic antenna — how the 2200 m/630 m limits are stated. |
| Electric field | The field between points at different voltages; a radio wave's polarization is defined by this field's orientation. |
| Electrical length | A conductor's length measured in wavelengths — it increases with diameter and exceeds physical length on a feed line. |
| Electrolytic capacitor | A polarized capacitor packing high capacitance into a small volume — leaky, loose-tolerance, not for RF. |
| Electromagnetic wave | A traveling pair of electric and magnetic fields at right angles — a radio wave. |
| Electrostatic shield | The shield around a DF loop that kills unbalanced capacitive coupling and deepens the null. |
| Element credit | Examination credit for a written element, earned by a license grant or a CSCE per §97.505. |
| Elevation pattern | An antenna's radiation pattern plotted against angle above the horizon (pool Figure E9-2). |
| Elliptical filter | The filter family with an extremely sharp cutoff and one or more stop-band notches. |
| EME (Earth-Moon-Earth) | Bouncing signals off the Moon to reach distant stations. |
| Emission bandwidth | The width of spectrum an emission occupies — capped at 2.8 kHz on 60 m and for HF data modes. |
| Emission mode | The type of signal a transmitter produces (CW, phone, data, image, and so on). |
| Emitter follower | The common-collector stage — input and output in phase, high input impedance, low output impedance. |
| End-fed half-wave | A half-wave antenna fed at one end — its feed-point impedance is very high. |
| End-fire | A phased-array pattern firing along the array's own axis (two λ/4 verticals at λ/2 spacing fed 180° out of phase). |
| Enhancement-mode FET | A FET that stays off at zero gate voltage — the opposite of depletion-mode. |
| Envelope detector | The AM detector — rectification and filtering of the RF. |
| ERP (effective radiated power) | Transmitter PEP times antenna gain relative to a half-wave dipole — how the 60 m limits are stated. |
| Extended double Zepp | A center-fed wire antenna 1.25 wavelengths long. |
| Fading | Signal strength rising and falling, usually from multipath combining. |
| Far field | The region where an antenna's pattern shape no longer varies with distance. |
| Faraday rotation | The rotation of a wave's polarization as it crosses the ionosphere — one reason satellite stations use circular polarization. |
| Fast-scan TV | Full-motion amateur television; the NTSC standard is 525 interlaced lines per frame. |
| FEC (forward error correction) | Sending redundant information with the data so the receiver can fix errors without a repeat. |
| Feed line | The cable that carries RF between the transceiver and the antenna. |
| Feed-point impedance | The impedance at the antenna's feed terminals — what the feed line sees. |
| Ferrite bead | A clip-on ferrite cylinder that chokes RF current on a cable — and a VHF/UHF parasitic suppressor at amplifier terminals. |
| Ferrite choke | A clip-on ferrite core on a cable that blocks unwanted RF current on the outside of the cable. |
| Ferrite mix | The material formulation of a ferrite core that sets its working frequency range. |
| FET (field-effect transistor) | A transistor family whose electrodes are gate, drain, and source. |
| FFT | The fast Fourier transform — the algorithm converting time domain to frequency domain. |
| Figure-eight pattern | The dipole's free-space radiation pattern — strongest broadside, nulls off the ends. |
| FIR filter | The finite-impulse-response digital filter — it can delay all frequencies equally, and more taps make it sharper. |
| First Fresnel zone | The ellipsoid around a path that should stay clear; it shrinks as frequency rises (smallest at 5.8 GHz among the pool's listed bands). |
| Flash (direct) converter | The very high-speed ADC architecture used in SDRs. |
| Flat-topping | Envelope clipping from excessive drive or speech levels — audible distortion and splatter. |
| Flip-flop | A bistable digital element — one stage divides a pulse train by 2. |
| FM (frequency modulation) | Impressing information on a carrier by varying its frequency. |
| Folded dipole | A half-wave dipole with an additional parallel wire connecting its ends — about 300 Ω feed impedance. |
| Form 605 | The FCC/NCVEC application form used at exam sessions and for license changes. |
| Forward power | The power traveling from transmitter toward antenna, as read by a directional wattmeter. |
| Fourier analysis | The decomposition of a waveform into sinusoids — a square wave is a sine plus its odd harmonics. |
| FPGA | A field-programmable gate array, configured in a hardware description language (HDL). |
| Free space | Ideal empty space, where every radio wave travels at the speed of light. |
| Frequency | The number of complete cycles per second; unit hertz. |
| Frequency hopping | The spread-spectrum technique that rapidly varies the carrier frequency per a pseudorandom sequence. |
| Frequency-division multiplexing (FDM) | Sharing one transmission by dividing it into separate frequency bands, each carrying a different data stream. |
| FRN | FCC Registration Number — a 10-digit identifier for all your FCC business, obtained free in CORES before exam day. |
| Front-to-back ratio | The ratio of power radiated in the main lobe to power radiated in the opposite direction. |
| Front-to-side ratio | The ratio of power radiated in the main lobe to power radiated at 90° to it. |
| FST4 | A WSJT mode using four-tone Gaussian FSK with variable T/R periods and seven tone spacings. |
| FT8 | A weak-signal digital mode exchanging minimal messages in timed 15-second sequences. |
| G5RV | A center-fed wire antenna run through a specific length of open-wire line to a balun and coax. |
| Gain (amplifier) | Output compared to input — of voltage, current, or power. |
| Gain (antenna) | The increase in signal strength in a specified direction compared to a reference antenna, achieved by focusing. |
| Gain-bandwidth product | The frequency at which an op-amp's open-loop gain falls to one. |
| Gamma match | A Yagi feed-point matching device needing no insulation of the driven element from the boom. |
| Geomagnetic equator | The equator of Earth's magnetic field — transequatorial paths cross it near right angles. |
| Geomagnetic storm | A temporary disturbance of Earth's magnetic field that degrades high-latitude HF paths. |
| Giga- | Metric prefix for 10⁹ (GHz = gigahertz). |
| Grace period | The two years after expiration during which a license may still be renewed — with no transmitting until the renewal is granted. |
| Gray code | A code in which only one bit changes between sequential values. |
| Grid locator | A letter-number designator for a geographic location in the Maidenhead system (e.g., "FN31"). |
| Ground gain | Increased signal strength from ground reflections near the antenna. |
| Ground plane | A vertical antenna working against radials — omnidirectional in azimuth. |
| Ground rod | A metal rod driven into the earth for safety and lightning grounds; amateur towers use eight-foot rods, bonded together. |
| Ground wave | The along-the-surface propagation mode — vertical polarization only, range shrinking as frequency rises. |
| Grounded-grid amplifier | A (usually tube) amplifier with the grid at RF ground — low input impedance. |
| Group delay | The frequency-by-frequency delay of a filter — constant in a linear-phase FIR filter. |
| Half-power point | The frequency where a filter's response falls to half power — band-pass bandwidth is measured between the upper and lower ones. |
| Harmful interference | Interference that seriously degrades, obstructs, or repeatedly interrupts a radio service. |
| Hartley oscillator | The oscillator whose feedback path is a tapped coil. |
| Helical filter | The common band-pass/notch filter family at VHF and UHF. |
| Hertz (Hz) | The unit of frequency: one cycle per second. |
| HF | High frequency: 3–30 MHz — the long-distance "shortwave" amateur bands. |
| Hilbert transform | The phasing method that generates SSB by combining signals in quadrature. |
| Hysteresis | Snap-action feedback that stops input noise from chattering a comparator's output. |
| I and Q signals | The in-phase and quadrature SDR signal pair, 90 degrees apart — software can turn them into any modulation type. |
| IARP | The Inter-American permit letting US amateurs operate in certain countries of the Americas. |
| IF (intermediate frequency) | The fixed frequency a superhet converts signals to; the image response sits twice the IF away. |
| IF Shift | The receiver control that slides the passband away from adjacent interference. |
| Image response | A superhet's unwanted response, twice the IF away from the desired signal. |
| Impedance | The opposition to AC current flow — resistance plus reactance; unit ohm. |
| Impedance matching | Making a load look like the source's design impedance — by transformer, pi-network, or transmission-line section. |
| Impulse noise | Short-pulse noise (ignition, power-line) — the noise blanker's target. |
| Inductance | The ability to store energy in a magnetic field; unit henry. |
| Inductor | A component that stores energy in a magnetic field — a coil of wire. |
| Input impedance | The load a measuring device presents — voltmeters use high input impedance to avoid disturbing the circuit. |
| Input offset voltage | The differential input voltage that brings an op-amp's open-loop output to zero. |
| Insertion loss | A filter's attenuation inside its own passband. |
| Integrated circuit (IC) | Many semiconductors and other components built into one package — a "chip." |
| Interlaced scanning | Painting odd lines in one field and even lines in the next — the NTSC frame structure. |
| Intermodulation | Spurious products spawned when signals combine in a non-linear circuit; odd-order products land closest to the originals. |
| Interplanetary magnetic field (IMF) | The Sun's magnetic field carried by the solar wind; its Bz component drives geomagnetic disturbance. |
| Intersymbol interference | Smearing of one digital symbol into the next — OFDM's subcarrier spacing is chosen to avoid it. |
| Inverter | A converter from DC to AC — the box between a solar battery bank and household wiring. |
| Inverting transponder | A linear satellite transponder whose output sideband is inverted from its input — sidebands swap, band positions reverse, and Doppler partially cancels. |
| Ionosphere | The charged upper-atmosphere region that reflects HF radio waves back to earth. |
| IP3 (third-order intercept point) | The extrapolated input level where third-order intermodulation products would equal the inputs — a figure of merit, not a working level. |
| Isotropic radiator | A hypothetical, lossless antenna radiating equally in all directions — the gain reference (0 dBi). |
| ITU | The International Telecommunication Union, the UN agency coordinating global radio spectrum. |
| ITU Region 2 | The ITU region covering the Americas — the United States, Puerto Rico, and the US Virgin Islands. |
| j-operator | The imaginary unit of engineering (√−1): it rotates a phasor 90°, +j inductive and −j capacitive. |
| JT65 | The multitone-AFSK WSJT mode designed for EME, decoding very-low-SNR signals. |
| K-index | The short-term (3-hour) index of geomagnetic stability. |
| Keplerian elements | The orbit-defining parameter set (distributed as TLEs) that tracking software turns into pass predictions. |
| Key clicks | Splatter from CW with too-short rise and fall times — cured by increasing them. |
| Kilo- | Metric prefix for 10³ (kHz = kilohertz, kW = kilowatt, km = kilometer). |
| Ladder line | Open parallel-conductor feed line — approximately 450 ohms (also "window line"). |
| Latency | The delay between a control action and the resulting change in the transmitted signal. |
| LED (light-emitting diode) | A diode that emits light when forward current flows — the standard visual indicator component. |
| Libration fading | The fluttery, irregular EME fading from multipath off the Moon's rough, wobbling face. |
| Linear amplifier | An amplifier that preserves the input waveform — required for SSB. |
| Linear transponder | A bent-pipe satellite frequency translator — it relays any mode across its passband. |
| Link budget | The accounting that adds transmit power and antenna gains and subtracts all losses, as seen at the receiver. |
| Link margin | The received level minus the minimum the receiver needs. |
| Load capacitance | The specified parallel capacitance that makes a crystal run on its marked frequency. |
| Loading (antenna) | Electrically lengthening an antenna by inserting inductors (coils) in the radiating elements. |
| Loading coil | The inductor that cancels a short antenna's capacitive reactance — most efficient near the radiator's center. |
| Local oscillator | The oscillator that sets a superheterodyne receiver's tuned frequency. |
| Long path | The great-circle path the long way around — point the beam 180 degrees from the short-path heading. |
| LoTW | Logbook of The World — the ARRL database where submitted electronic logs cross-match into confirmations. |
| Main lobe | The direction of maximum radiated field of a directional antenna. |
| Mark and space | The two tones of an FSK signal (RTTY's 170 Hz shift separates them). |
| MDS (minimum discernible signal) | The weakest signal a receiver can detect. |
| Mega- | Metric prefix for 10⁶ (MHz = megahertz). |
| Mesh network | An amateur data network built from commercial Wi-Fi gear with modified firmware on amateur frequencies. |
| Meteor scatter | Bouncing VHF signals off meteor ionization trails; best on 6 meters. |
| Method of Moments | The antenna-modeling method that treats a wire as current-carrying segments (about 10 per half-wavelength or more). |
| Micro- | Metric prefix for 10⁻⁶ (µV = microvolt). |
| Microphonics | Oscillator frequency changes caused by mechanical vibration — cured by mechanical isolation. |
| Microstrip | Precision PCB conductors above a ground plane — constant-impedance interconnects at microwave frequencies. |
| Milli- | Metric prefix for 10⁻³ (mA = milliampere). |
| Mixer | A circuit that converts a signal from one frequency to another. |
| MMIC | Monolithic Microwave Integrated Circuit. |
| Mode designator | The satellite uplink/downlink letter pair, uplink first: V = 2 m, U = 70 cm, L = 23 cm, S = 13 cm. |
| Modulation | Combining speech or data with an RF carrier signal. |
| Modulation index | Frequency deviation divided by the modulating frequency — capped at 1 for angle modulation below 29 MHz. |
| Monostable multivibrator | A circuit that flips to its alternate state for a set time, then returns. |
| MOSFET | A field-effect transistor whose gate is insulated from the channel by a thin insulating layer. |
| MPE (maximum permissible exposure) | The FCC's RF exposure limit, which varies with frequency (most restrictive at 30–300 MHz). |
| MSK144 | The WSJT mode designed for meteor scatter — 72 ms messages inside a 15-second sequence. |
| MUF (maximum usable frequency) | The highest frequency that propagates by skywave between two specific points. |
| Multipath | The same signal arriving over multiple paths, combining in or out of phase to cause fading. |
| Multitone AFSK | Sending data as many simultaneous audio tones — JT65's 65-tone scheme. |
| Nano- | Metric prefix for 10⁻⁹. |
| Necessary bandwidth | The width of band outside of which a signal's mean power is attenuated at least 26 dB — spurious emissions live outside it. |
| Neutralization | Canceling an amplifier's internal feedback to eliminate self-oscillation. |
| Noise blanker | A receiver circuit that mutes receiver gain during each noise pulse. |
| Noise figure | The dB ratio of a receiver's noise to the theoretical minimum. |
| Noise floor | The theoretical −174 dBm thermal noise in 1 Hz at room temperature, scaled up by bandwidth and noise figure. |
| Normalized impedance | Impedance re-scaled so the Smith chart's prime center equals the system impedance (1.0 = 50 Ω). |
| NP0 / C0G | The near-zero-temperature-coefficient capacitor dielectric used to fight thermal drift. |
| NRQZ | The National Radio Quiet Zone around the National Radio Astronomy Observatory, Green Bank, WV. |
| NTSC | The analog fast-scan TV standard: 525 interlaced lines per frame. |
| NVIS | Near vertical incidence skywave — high-angle, short-distance MF/HF propagation, the emcomm workhorse for regional coverage. |
| Nyquist rate | Sample at least twice the highest frequency component to capture a signal. |
| OCFD (off-center-fed dipole) | A dipole fed off-center to present a similar feed-point impedance on multiple bands. |
| Odd-order product | An intermodulation product whose mixing-coefficient sum is odd — these land closest to the original frequencies. |
| OET Bulletin 65 | The FCC's RF-exposure evaluation guidance (Supplement B for the amateur service). |
| OFDM | A digital modulation using many subcarriers spaced to avoid intersymbol interference. |
| Ohm (Ω) | The unit of resistance and impedance. |
| Ohm's law | E = I × R (equivalently V = I × R): voltage equals current times resistance. |
| Omnidirectional | Radiating equally in all azimuth directions. |
| Op-amp | The analog operational-amplifier integrated circuit. |
| Optoisolator | An LED-plus-phototransistor pair giving electrical isolation between a control circuit and a switched circuit. |
| Ordinary and extraordinary waves | The two elliptically polarized waves the ionosphere splits a signal into. |
| Oscillator | A circuit that generates a signal at a specific frequency. |
| Oscilloscope | The instrument that draws waveforms — horizontal and vertical channel amplifiers inside. |
| Overmodulation | Too much modulation — splatter into excessive bandwidth, showing as vertical side-lines on the waterfall. |
| Packet radio | Digital data sent in addressed frames with a header, checksum, and ARQ error recovery. |
| PACTOR | An HF digital protocol whose connections are strictly two-station ARQ links. |
| Parabolic reflector | A dish antenna — doubling frequency adds 6 dB of gain. |
| Parallel circuit | A circuit where components share the same two nodes, so the voltage is the same across all of them. |
| Parasitic suppressor | The small R-L network that kills unwanted VHF/UHF oscillation in an RF power amplifier. |
| Parity bit | An added bit that lets some error types be detected (not corrected). |
| Part 97 | The FCC's amateur service rules (47 CFR Part 97). |
| Passband ripple | The up-and-down response variation inside a filter's passband (the Chebyshev trade). |
| Peak | The maximum instantaneous value of a waveform. |
| Pennant antenna | A terminated single-turn receiving loop with a cardioid pattern. |
| PEP (peak envelope power) | The average power during one RF cycle at the crest of the modulation envelope — how amateur power limits are stated. |
| Perigee / apogee | The Moon's nearest and farthest points — EME path loss is about 2 dB better at perigee. |
| Phase | The timing relationship between AC voltage and current — voltage leads current in an inductor and lags in a capacitor. |
| Phase accumulator | The DDS block that steps through waveform phase at a programmed rate. |
| Phase detector | The PLL block that compares the VCO against the reference and produces the error signal. |
| Phase-locked loop (PLL) | An electronic servo loop — phase detector, low-pass filter, VCO, stable reference — used for frequency synthesis and FM demodulation. |
| Phased array | Multiple driven elements fed with controlled spacing and phase to shape the pattern. |
| Phasor | The rotating vector picture of an AC quantity's magnitude and phase. |
| Photoconductive | Changing resistance with light (the light-detecting counterpart to photovoltaic). |
| Photovoltaic cell | A solar cell — one silicon cell gives about 0.5 V open-circuit in full sun. |
| Pi-L network | A Pi-network with an additional series output inductor — greater harmonic suppression. |
| Pi-network | The shunt-C / series-L / shunt-C matching or low-pass network. |
| Pico- | Metric prefix for 10⁻¹² (pF = picofarad). |
| Pierce oscillator | The oscillator whose feedback path runs through a quartz crystal. |
| PIN diode | A diode whose RF resistance is set by its forward DC bias current — a good RF switch or attenuator. |
| PM (phase modulation) | Impressing information on a carrier by varying its phase — a close cousin of FM. |
| Point-contact diode | The cat's-whisker diode — an RF detector, not a rectifier. |
| Polar coordinates | Describing an impedance by magnitude and phase angle. |
| Polarization | The orientation of a radio wave's electric field — vertical whip, vertical polarization. |
| Positive logic | The convention high voltage = 1, low = 0. |
| Powdered iron | The most temperature-stable of the pool's listed core materials. |
| Power | The rate at which electrical energy is used; unit watt. |
| Power density | The RF field strength per unit area — one of the three exposure variables. |
| Power factor | The fraction of apparent power that is real power — cos θ. |
| PRB-1 | The 1985 FCC declaratory ruling: local antenna regulation must reasonably accommodate amateur communications and use the minimum practicable regulation. |
| Pre-emphasis | The transmitter-side treble boost that de-emphasis later undoes. |
| Prescaler | The divider that brings high frequencies into a counter's range. |
| Preselector | A front-end filter that removes strong out-of-band signals before they can intermod. |
| Primary service | The service with priority on shared spectrum — secondary services must protect it and accept its interference. |
| Prime center | The Smith chart's center point — reassigned to the system impedance when normalizing. |
| Probe compensation | Trimming a ×10 scope probe on the calibrator square wave until the flat tops are flat. |
| Product detector | The SSB/CW receiver detector that recovers the audio. |
| Pseudorandom sequence | The deterministic-but-noiselike sequence that drives frequency hopping. |
| PSK | Phase shift keying — digital data carried by phase changes of the carrier. |
| PSK31 | A narrow-band keyboard-to-keyboard digital mode using Varicode — it hangs out at 14.070 MHz on 20 m. |
| Pull-up / pull-down resistor | The resistor that pins an otherwise open-circuit input or output to a defined voltage. |
| Q (figure of merit) | The quality factor of a resonant circuit or component: series Q = X/R, parallel Q = R/X, and BW = f₀/Q. |
| Q-section | A quarter-wave transmission-line transformer, Z₀ = √(Z_line × Z_load). |
| Q65 | The WSJT mode built for EME and fast-fading scatter paths — it averages multiple receive cycles. |
| QAM | Modulating the amplitude of two same-frequency carriers 90° out of phase to send data. |
| QPSK | Quadrature phase shift keying — 0°/90°/180°/270° shifts, two bits per symbol. |
| Quantization noise | The error from rounding a signal to discrete ADC levels — dither reduces it. |
| RACES | Radio Amateur Civil Emergency Service — the Part 97 civil-defense service requiring certification by a civil defense agency. |
| Radials | The ground-plane conductors of a vertical antenna — slope them downward to raise the feed point toward 50 Ω. |
| Radiation resistance | The part of an antenna's feed-point resistance that represents radiated power. |
| Radio horizon | The refraction-extended VHF/UHF horizon — about 15 percent farther than the geographic horizon. |
| RDF (receiving directivity factor) | Peak antenna gain compared to average gain over the hemisphere around and above the antenna. |
| Reactance | The opposition to AC from capacitance and inductance — the non-resistive part of impedance. |
| Reactance axis | The Smith chart's large outer circle, on which the reactance arcs terminate (pool Figure E9-3). |
| Reactance modulator | A stage that varies an oscillator's effective reactance — attached after the oscillator, it produces phase modulation. |
| Real power | The power actually dissipated — I²R, touching resistance only. |
| Reactive power | The "wattless" power shuttled between source and reactance — VI·sin θ. |
| Reciprocal mixing | LO phase noise mixing with a strong adjacent signal and dumping noise onto the desired signal. |
| Rectifier | A circuit (usually diodes) that changes AC into varying DC. |
| Rectangular coordinates | Describing an impedance as R ± jX — resistance on the horizontal axis, reactance on the vertical. |
| Reflected power | Power bounced back from a mismatched antenna feed point toward the transmitter. |
| Reflection coefficient (Γ) | The ratio describing a load's interaction with a transmission line: Γ = (Z_L − Z₀)/(Z_L + Z₀). |
| Reflector | The Yagi element longer than the driven element, sitting behind it. |
| Remote control | Operation with the control operator manipulating the station indirectly through a control link. |
| Repeater | A station that simultaneously retransmits another station's signal on a different channel to extend range. |
| Resistance | The opposition to current flow of every kind — DC, AC, and RF; unit ohm. |
| Resistance axis | The Smith chart's only straight line — the horizontal diameter (pool Figure E9-3). |
| Resistor | A component whose job is to oppose (limit) current flow. |
| Resonance | The condition X_L = X_C, where the inductive and capacitive reactances cancel. |
| Resonant circuit | An inductor plus a capacitor forming a frequency-selecting tuned circuit. |
| Resonant frequency | The frequency at which an antenna (or tuned circuit) naturally responds best. |
| Resonant voltage rise | The Q-multiplied voltage across L and C at series resonance — why tank capacitors arc. |
| Return loss | −20·log₁₀\|Γ\| — how many dB down the reflected power is. |
| Reverse beacon network | An internet network of automated receivers showing where your signal is being heard. |
| RF (radio frequency) | Signals in the radio part of the spectrum — and shorthand for radio energy generally. |
| RFI | Radio-frequency interference — your RF getting into consumer electronics (SSB sounds like distorted speech; CW like on-and-off humming or clicking). |
| RMS | Root-mean-square — the AC value that heats a resistor exactly like the same-value DC. |
| Roofing filter | A narrow first-IF filter that improves blocking dynamic range by attenuating strong close-in signals early. |
| Rusty-bolt effect | Corroded metal joints near broadcast sites mixing and re-radiating signals. |
| S parameters | The two-port scattering parameters: S21 forward gain, S11 input return loss/reflection coefficient. |
| Sampling rate | How fast an ADC reads the signal — it sets the highest accurate (and maximum receive) frequency. |
| SAR (specific absorption rate) | The rate at which RF energy is absorbed by body tissue. |
| Saturation | The fully-on endpoint of a switching transistor's operation. |
| Scatter | Weak multi-path propagation that fills the skip zone with fluttery, distorted signals. |
| Schematic | An electrical diagram drawn with standard component symbols, showing how components connect. |
| Schottky diode | A metal-semiconductor-junction diode — low forward drop, fast recovery, good VHF/UHF mixer/detector (symbol 6 in pool Figure E6-2). |
| SDR (software-defined radio) | A radio whose filtering, detection, and modulation all happen in software. |
| Secondary service | A service that must not interfere with, and must accept interference from, the primary service on shared spectrum. |
| Selectivity | A receiver's ability to discriminate between nearby signals. |
| Self-resonant frequency | The frequency where a component's parasitics resonate — above it, an inductor turns capacitive. |
| Sense antenna | The omni element added to a DF loop to collapse its bidirectional null into one direction. |
| Sensitivity | A receiver's ability to detect weak signals. |
| Series circuit | A circuit where the same current flows through every component in turn. |
| Shape factor | A filter's adjacent-channel rejection figure. |
| Shock-absorbing lanyard | The fall-arrest lanyard that anchors above the climber's head level. |
| Short path | The direct great-circle heading to a distant station. |
| Shunt feed | Feeding a grounded tower at its base with a gamma match. |
| Shunt regulator | A regulator that holds voltage by loading the unregulated source. |
| Sideband convention | LSB below 10 MHz (160/75/40 m), USB at 10 MHz and above (20–10 m and VHF/UHF) — custom, not law; AFSK RTTY uses LSB while FT8/JT modes use USB on every band. |
| Siemens (S) | The unit of admittance, conductance, and susceptance. |
| Single point ground panel | The entry panel where all protectors mount so every lightning protector fires simultaneously. |
| 60-meter band | The 5 MHz band: a contiguous 5351.5–5366.5 kHz segment at 9.15 W ERP plus four discrete channels (5332, 5348, 5373, 5405 kHz) at 100 W ERP, USB phone, 2.8 kHz maximum bandwidth. |
| Skin effect | The crowding of RF current toward a conductor's surface — resistance rises with frequency. |
| Smith chart | A chart of normalized impedance on resistance-circle and reactance-arc coordinates — the classic tool for designing stub matches (pool Figure E9-3). |
| Solar flux index | The measure of 10.7 cm (2800 MHz) solar radio emission — the everyday solar-activity number. |
| Solid-state relay (SSR) | A semiconductor implementation of relay functions — no coil, no contacts. |
| Space station | An amateur station located more than 50 km above the Earth's surface. |
| Spectrum analyzer | The instrument that draws amplitude versus frequency — the spur and intermod hunter. |
| Spin modulation | Fading from a spinning satellite's changing antenna orientation — mitigated by circular polarization. |
| Split operation | Transmitting on one frequency while listening on another — the DX announces "listening 5 to 10 up." |
| Sporadic E (Es) | Patchy E-region ionization — solstice-peaking, daylight-favoring, the 6 m summer magic. |
| Spread spectrum | A wide-band emission technique limited to 10 W PEP output. |
| Spurious emission | Any unwanted emission outside the necessary bandwidth, such as a harmonic. |
| SSB (single sideband) | A bandwidth-efficient voice mode transmitting one sideband of an AM signal with the carrier suppressed. |
| Step-start circuit | The power-supply circuit that lets filter capacitors charge gradually at turn-on. |
| Store-and-forward | The orbiting (or terrestrial) mailbox that holds digital messages for later download. |
| Stub match | A short length of transmission line in parallel with the feed line at or near the feed point. |
| Subcarrier | One of the many carriers inside an OFDM or multiplexed signal. |
| Successive approximation | A common type of analog-to-digital conversion. |
| Superheterodyne | A receiver that converts signals to a fixed intermediate frequency by varying its local oscillator. |
| Suppressed carrier | The carrier frequency an SSB rig displays while transmitting no carrier — the speech energy sits about 3 kHz to one side. |
| Surge protector | The device on the single point ground panel that clamps lightning and line surges. |
| Susceptance (B) | The imaginary part of admittance — the letter is B, the unit siemens. |
| Switchmode power supply | A supply that chops the input at high frequency — what allows smaller, lighter components. |
| SWR (standing wave ratio) | A measure of how well a load is matched to a transmission line — 1:1 is perfect. |
| Symbol rate | The digital signaling speed in symbols per second — higher symbol rates need wider bandwidth. |
| T-network | The three-element network that becomes a high-pass with series capacitors and a shunt inductor. |
| Takeoff angle | The elevation angle at which an antenna launches its main radiation. |
| Tank circuit | The parallel LC combination that sets an oscillator's or amplifier's frequency. |
| Tap (FIR) | One delay element of a digital filter — more taps, sharper filter. |
| Telecommand | One-way transmissions to initiate, modify, or terminate functions of a device at a distance (e.g., a space station). |
| Telemetry | Measurements sent back by radio, such as a satellite's health data. |
| Terminating resistor | The resistor that makes a long-wire or Beverage pattern unidirectional by absorbing the reverse wave. |
| Third-party agreement | A treaty arrangement letting US amateurs pass third-party traffic with a given country. |
| Third-party communications | A message passed from one control operator to another on behalf of a non-licensed person. |
| Time constant (τ) | The charge/discharge clock of an RC or RL circuit — 63.2% charged or 36.8% remaining after one τ. |
| Time-division multiplexing (TDM) | Sharing one transmission by giving each signal discrete time slots. |
| Top loading | Capacitance added at the top of a short vertical — it improves radiation efficiency. |
| Toroid | A donut-shaped ferrite core giving large inductance with a self-contained field. |
| Total harmonic distortion (THD) | The distortion figure that measures ADC quality. |
| Transequatorial propagation (TEP) | Chordal ducting across the geomagnetic equator between equatorial anomalies — afternoon/early-evening paths to about 5,000 miles. |
| Transceiver | A receiver and a transmitter combined in one unit. |
| Transformer | A component that changes AC voltage up or down — never to DC. |
| Transistor | A three-region semiconductor device that works as an electronic switch or an amplifier. |
| Tri-state logic | Outputs with three states — 0, 1, and high-impedance — for bus sharing. |
| True RMS | A meter that reads RMS correctly for sinusoidal and non-sinusoidal signals alike. |
| Truth table | The input-by-input listing of a gate's output. |
| TTL | The classic digital IC family — CMOS beats it on power consumption. |
| Two-tone test | Feeding two non-harmonically related audio tones into an SSB transmitter to analyze linearity. |
| UHF | Ultra high frequency: 300–3000 MHz. |
| UI frame | The Unnumbered Information frame — connectionless, unacknowledged; the APRS beacon's frame type. |
| ULS | The FCC's Universal Licensing System — the database whose entry for your grant is your operating authority. |
| Uncontrolled environment | The RF-exposure category for the general public (general-population limits). |
| Uplink / downlink | The ground-to-satellite path and the satellite-to-ground path (U/V mode = up on 70 cm, down on 2 m). |
| UTC (Utilities Technology Council) | The utilities body you notify before operating on 2200 or 630 m — 30 days, unless told you are within 1 km of PLC systems. |
| Vanity call sign | A call sign you request by choice rather than receiving from the sequential system. |
| Varactor | A voltage-variable capacitor made from a reverse-biased diode. |
| Varicode | PSK31's variable-length code — common letters get short codes, so uppercase letters take longer. |
| VE (volunteer examiner) | An accredited amateur who administers license exams as part of a team of at least three. |
| VEC (volunteer examiner coordinator) | The FCC-recognized organization that coordinates exam sessions and forwards results to the FCC. |
| Velocity factor | Wave speed in a feed line as a fraction of the speed of light — set mostly by the dielectric. |
| Vestigial sideband (VSB) | AM with one full sideband plus a vestige of the other — analog TV's bandwidth saver. |
| VHF | Very high frequency: 30–300 MHz. |
| VIS code | The tone header that announces the SSTV mode so software can auto-select it. |
| VNA (vector network analyzer) | The instrument measuring S parameters — calibrated with short, open, and 50 Ω loads. |
| VOACAP | The standard HF propagation-prediction model. |
| Volt (V) | The unit of electric potential (voltage). |
| Voltage | The electrical "pressure" whose difference drives electron flow. |
| WARC bands | 30, 17, and 12 meters — the 1979-conference bands where contests are avoided by long-standing truce. |
| Waterfall | The scrolling display with frequency horizontal, time vertical, and signal strength as brightness. |
| Watt (W) | The unit of electrical power. |
| Wavelength | The distance a wave travels in one cycle — inversely related to frequency. |
| Weak-signal segment | The bottom-of-band SSB/CW territory on the VHF/UHF bands, near the calling frequency. |
| Wilkinson divider | The power splitter that feeds two 50 Ω loads equally while keeping a 50 Ω input. |
| WSPR | Weak Signal Propagation Reporter — a 2-minute-sequence beacon mode whose reception reports map at WSPRnet. |
| WSJT-X | The free software suite home of FT8, also supporting EME, weak-signal beacons, and meteor scatter. |
| XNOR gate | The equality detector — output 0 when exactly one input is 1. |
| Yagi | A directional beam antenna with a driven element plus parasitic elements. |
| Zener diode | A diode used as a voltage reference or regulator (symbol 3 in pool Figure E6-2; D1 in pool Figure E7-2). |
| Zepp antenna | An end-fed half-wavelength wire antenna. |

---

## 5. Subelement → Chapter Map

The mapping is one subelement per chapter, E1→ch01 … E0→ch10, with ch00 the capstone upgrade welcome (no pool). Every one of the 599 pool questions is answerable after its mapped chapter; the mapping below is the ownership contract — a chapter teaches its subelement, and only that chapter quotes those questions in its Exam Focus. Exam weight (one question per group) is shown so writers see the stakes: E6–E0 supply 30 of the 50 exam seats (E7+E9 alone are 16), and every group is guaranteed exactly one seat on every exam, so no group may be skipped.

| Chapter | Title | Pool subelement | Groups owned | Pool questions | Exam questions |
|---|---|---|---|---:|---:|
| ch00 | The last upgrade: why Extra, and how this book works | — (upgrade logistics, canon §2.6) | — | — | — |
| ch01 | The rules at Extra depth | E1 | E1A–E1F | 68 | 6 |
| ch02 | Operating beyond the General bands: satellites, TV, digital, DX | E2 | E2A–E2E | 60 | 5 |
| ch03 | Propagation beyond the ordinary | E3 | E3A–E3C | 39 | 3 |
| ch04 | The workbench: instruments, receivers, interference | E4 | E4A–E4E | 63 | 5 |
| ch05 | Electrical principles: complex impedance and resonance | E5 | E5A–E5D | 49 | 4 |
| ch06 | Components and devices at Extra depth | E6 | E6A–E6F | 68 | 6 |
| ch07 | Practical circuits | E7 | E7A–E7H | 99 | 8 |
| ch08 | Signals and emissions at Extra depth | E8 | E8A–E8D | 48 | 4 |
| ch09 | Antennas and transmission lines at Extra depth | E9 | E9A–E9H | 93 | 8 |
| ch10 | RF exposure and safety at Extra depth | E0 | E0A | 12 | 1 |
| Appendix A | The complete 2024–2028 Extra pool | all 599 verbatim + one-line "why" | all 50 | 599 | 50 |
| Appendix B | Glossary & formulas | — (canon §3, §4) | — | — | — |
| **Total (ch01–ch10)** | | | **50** | **599** | **50** |

Per-group ownership and counts (binding):

- **ch01 (E1, 68 q):** E1A frequency privileges, band-edge arithmetic, ships/aircraft, 2200/630 m power (11); E1B station restrictions, spurious emissions, antenna structures, RACES (11); E1C automatic/remote control, foreign operation, emission standards, 60 m (12); E1D space and Earth stations, telemetry, telecommand, one-way rules (12); E1E the volunteer examiner program (11); E1F amplifiers, prohibited communications, spread spectrum, auxiliary, reciprocal, STA (11).
- **ch02 (E2, 60 q):** E2A amateur satellites (12); E2B television practices, fast-scan and slow-scan (12); E2C contest and DX operating, remote operation, log formats, mesh (12); E2D digital modes for VHF/UHF: WSJT, APRS, EME, meteor scatter (11); E2E digital modes for HF (13).
- **ch03 (E3, 39 q):** E3A electromagnetic waves and specialized propagation: EME, meteor scatter, ducts, aurora (14); E3B transequatorial, long-path, ordinary/extraordinary waves, chordal hop, sporadic E, ground wave (13); E3C propagation prediction and reporting, space weather (12).
- **ch04 (E4, 63 q):** E4A test equipment: oscilloscopes, spectrum analyzers, counters, antenna analyzers (11); E4B measurement technique, S parameters, VNA (11); E4C receiver performance: noise, selectivity, phase noise, overload (14); E4D dynamic range, intermodulation, link budgets (13 — E4D05 deleted); E4E noise and interference: DSP noise tools, RFI, grounding (14).
- **ch05 (E5, 49 q):** E5A resonance and Q (13); E5B time constants, phase relationships, admittance and susceptance (12); E5C coordinate systems and phasors, Figure E5-1 (12); E5D RF effects: skin effect, real and reactive power, electrical length (12).
- **ch06 (E6, 68 q):** E6A semiconductor materials and devices, Figure E6-1 (12); E6B diodes, Figure E6-2 (11); E6C digital ICs, Figure E6-3 (11); E6D inductors and piezoelectricity (11 — E6D07 deleted); E6E semiconductors and packages for RF (12); E6F electro-optical technology (11).
- **ch07 (E7, 99 q):** E7A digital circuits (11); E7B amplifiers, Figure E7-1 (12); E7C filters and matching networks (11); E7D power supplies and regulators, Figure E7-2 (15); E7E modulation and demodulation (11); E7F software-defined radio fundamentals (14); E7G operational amplifiers, Figure E7-3 (12); E7H oscillators and signal sources (13).
- **ch08 (E8, 48 q):** E8A Fourier analysis, RMS, average power and PEP, A/D conversion (11); E8B modulation index, deviation ratio, multiplexing (11); E8C digital signals: modes, codes, bandwidths (15); E8D keying defects, digital codes, spread spectrum (11).
- **ch09 (E9, 93 q):** E9A basic antenna parameters, ERP/EIRP (12); E9B antenna patterns and modeling, Figures E9-1/E9-2 (11); E9C practical wire antennas, phased arrays (14); E9D Yagis, dishes, loading (12); E9E impedance matching (10 — E9E10 deleted); E9F transmission lines (12); E9G the Smith chart, Figure E9-3 (11); E9H receiving and DF antennas (11).
- **ch10 (E0, 12 q):** E0A safety: RF exposure, grounding, tower climbing (12).

Notes (binding):

- **ch00 teaches no pool questions** — it covers the capstone upgrade logistics of canon §2.6 (Element 4 structure 50/37, CSCE, §97.9(b) immediacy with /AE, fees and the upgrade exemption, what Extra opens, CEPT as a real Extra benefit, series completion) and carries the checklist adaptation of the format laws (no Exam Focus; the audit enforces this — ch00 is the only exempt chapter, and ch10 is a full teaching chapter here because E0 is a real subelement).
- **The ten pool figures live in their owning chapters** (§1.4): E5-1 → ch05 (group E5C); E6-1, E6-2, E6-3 → ch06 (groups E6A, E6B, E6C); E7-1, E7-2, E7-3 → ch07 (groups E7B, E7D, E7G); E9-1, E9-2, E9-3 → ch09 (groups E9B, E9B, E9G). Each redrawn SVG follows §1.4's binding spec, and the 28 figure questions appear in those chapters' Exam Focus blocks with the question→position maps pinned in §1.4.
- **The three interior numbering gaps are taught, not hidden:** ch04 notes E4D05's withdrawal (errata 4), ch06 notes E6D07's (errata 3), ch09 notes E9E10's (errata 1), and ch02 notes E2A ended at E2A12 (errata 2) — one sentence each, pointing at §1.3's ledger; deleted questions are never quoted (§1.3).
- **ch10 treats RF exposure and tower/grounding safety as the pool's single group demands** — E0A mixes MPE rules (Part 1 territory, §7.6) with climbing practice; no MPE computation is required by any question, and any power-density illustration is flagged as enrichment (§2.16).
- **ch05 carries the heaviest math flag in the book:** the E5 formula family (canon §3) is exam math, and the three Figure E5-1 plotting questions are taught as a *plotting* skill per §1.4 — E5-1 is a chart, not a circuit (§7.5).
- Appendix A quotes all 599 ids exactly once in canonical pool order (audit check #8 enforces it); Appendix B is built from canon §3 and §4 only.

---

## 6. Copyright Ledger

**This book's standing rules (identical to Books 2 and 3, adapted for this pool):**

1. **Prose is always original.** Nothing is copied from any study guide, handbook, or web page.
2. **47 CFR Part 97 is public domain** (a work of the United States Government, 17 U.S.C. §105) and may be quoted verbatim; the FACT sentences in §2 quote it with section pinpoints. FCC Public Notice DA 16-1048 is likewise a US Government work.
3. **The NCVEC 2024–2028 Extra question pool is public domain** — "The NCVEC Question Pool Committee hereby releases into public domain the 2024-2028 Element 4 Extra Class Question Pool" (stated twice on the pool's release page, captured in `canon/source/release-page.html`, fetched 2026-07-30) — so questions, choices, answer keys, and figure *content* may be reproduced verbatim.
4. **All ten pool figures are redrawn, not copied**: original SVGs conveying exactly the official content (same components, same labels, same numbered positions), each registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure EX-N" (see §1.4).
5. **Bare facts, frequencies, and formulas are not copyrightable**; exam-prep explanations are always written fresh.
6. **Archival ARRL Handbook material is optional seasoning only**, governed by the ledger below (carried over unchanged from Book 1's accuracy canon, where each status was affirmatively determined, and already governing Books 2 and 3). The book works with zero archival images.

**ARRL *Radio Amateur's Handbook* ledger (carried over — governs any optional archival figure in this book too):** determinations rest on the US Copyright Office Public Records System and the official Catalog of Copyright Entries renewal volumes; public-domain findings are affirmatively evidenced (registration age, or confirmed absence of renewal within the 28-year window), not assumed.

| Edition (year) | Status | Basis | Reproducible? |
|---|---|---|---|
| 1927 | PUBLIC DOMAIN | Published 1927; pre-1928 works are public domain under the 95-year term (entered PD 1 Jan 2023); age alone controls. | YES |
| 1931 | PUBLIC DOMAIN | 8th Edition, first published 25 Apr 1931; renewal window 1958–1959; no renewal found in the USCO ARRL-claimant RE-class search or CCE renewal volumes. Not renewed. | YES |
| 1933 | PUBLIC DOMAIN | 10th Edition, first published 4 Jan 1933; renewal window 1960–1961; zero renewal matches. Not renewed. | YES |
| 1936 | PUBLIC DOMAIN | 13th Edition, first published 13 Nov 1935 (cover-dated 1936); renewal window 1963–1964; zero renewal matches. Not renewed. | YES |
| 1940 | PUBLIC DOMAIN | 17th Edition, first published 20 Nov 1939; renewal window 1967–1968; zero renewal matches. Not renewed. | YES |
| 1941 | PUBLIC DOMAIN | 18th Edition, first published 15 Nov 1940; renewal window 1968–1969; zero renewal matches. Not renewed. | YES |
| 1951 | PUBLIC DOMAIN | 28th Edition; renewal window ~1978–1979; the comprehensive USCO ARRL-claimant RE-class query shows no Handbook renewal in any year. Not renewed. | YES |
| 1968 | PROTECTED | Published 1964–1977: renewal became automatic by statute; protected 95 years from publication. | NO |
| 1974 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1976 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1977 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1981 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |
| 1983 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |

**Ledger summary:** 7 of the 13 owned Handbook editions are reproducible (public domain): 1927, 1931, 1933, 1936, 1940, 1941, 1951. The 6 protected editions — 1968, 1974, 1976, 1977, 1981, 1983 — are **never reproduced** in any form: no figures, no text excerpts, no scans. `figreg.validate()` mechanically rejects any figure tagged with a protected-year source. Separately and independently of that table: FCC Part 97 and the NCVEC question pools are public domain as stated in rules 2–3 above, and everything else in this book is original prose or original SVG.

---

## 7. Resolved Uncertainties

Every uncertainty flagged during research (notes r1–r5 and the ingestion report) is closed here, with the value or wording the book will use and its source. **No open uncertainty markers remain in this canon.**

### 7.1 The 60 m rule change (91 FR 1430) — same doctrine as the General canon, adapted: RESOLVED — teach current text, drill keyed answers

**What changed.** The FCC's WRC-15 Report & Order in WT Docket 23-83 (published in the Federal Register as 91 FR 1430/1431, effective 2026-01-14) replaced the channelized 60 m rules. Pool-era text (in force at the pool's 2024-07-01 effective date): §97.303(h)(1) authorized 60 m operation "only on the five center frequencies" 5332, 5348, 5358.5, 5373, 5405 kHz, CW carrier at channel center, emissions ≤ 2.8 kHz, flat 100 W ERP cap. **Current text** (verified 2026-07-30 against the eCFR, issue date 2026-07-28 ≡ 2026-07-20): amateurs may transmit (1) anywhere in the contiguous **5351.5–5366.5 kHz** segment at **9.15 W ERP**, and (2) on **four** of the five old channels — **5332, 5348, 5373, 5405 kHz** — at **100 W ERP**; the old 5358.5 kHz channel is gone as a discrete assignment (it lies inside the new segment); the ≤ 2.8 kHz bandwidth cap now applies to all 60 m spectrum (§97.307(f)(14)(i), with the frequency list in §97.303(h)(3)); and the CW-at-channel-center rule survives in §97.303(h)(3). The §97.301 tables now list "5.3515-5.3665" instead of "See §97.303(h)".

**Pool impact.** Unlike the General pool (whose 6th errata withdrew its two conflicted 60 m questions), the Extra pool's four errata **did not revise E1** (verified: errata 1–4 touched E1D07 wording, E1F03 choice D, and the E1E10/E1E11 citation tags only — §1.3). Both surviving Extra 60 m questions remain literally correct under current text: **E1A06** (CW transmit frequency "at the center frequency of the channel" — the rule moved from §97.303(h)(1) to §97.303(h)(3), and (h)(1) now holds the fixed/mobile interference paragraph, so **E1A06's printed citation `[97.303(h)(1)]` is stale**) and **E1C01** (maximum data bandwidth 2.8 kHz, correct under both texts).

**Binding resolution:** drill the pool's keyed answers exactly as published; chapters cite the CURRENT renumbered sections — §97.303(h)(3) for the channel/CW rules and §97.313(i) for the two power limits — when explaining these answers, and note E1A06's printed `[97.303(h)(1)]` as the superseded cite (preserved verbatim in quotes, never "repaired" — §1.5). Teach current 60 m practice as the two-part structure (contiguous segment plus four channels, 9.15 W ERP in the segment and 100 W ERP on the channels, USB phone, 2.8 kHz maximum bandwidth). No prose may describe 60 m as "five channels, 100 W ERP" — that rule is dead. This mirrors the General canon's §7.1 resolution, adjusted for a pool that kept its 60 m questions.

### 7.2 Other post-pool Part 97 amendments: RESOLVED — zero answer impact, recorded

- **Space-station post-mission disposal (89 FR 65223, 2024-08-09 — after the pool's effective date):** §97.207(g)(1)(vii)(D)(1) now requires disposal "as soon as practicable, but no later than five years following completion of the mission" for LEO below 2000 km, replacing the pool-era "atmospheric re-entry of the spacecraft within 25 years or less." **Not tested by any active E1D question** (they test §97.207(c) bands and (e) one-way), but any satellite-operations prose must say 5 years, not 25.
- **Deregulatory housekeeping (90 FR 57712, effective 2025-12-12):** §97.315(b)(2) (pre-April-28-1978 amplifier marketing waiver) → Reserved; §97.521(b) (VEC-region service requirement) → Reserved and Appendix 2 "VEC Regions" deleted wholesale; §§97.27–97.29 → Reserved. **Zero answer impact** — E1F03 tests (b)(1) (amateur-built exemption, and its choice D was itself rewritten by errata 1) and E1E03 tests the §97.521 preamble; the §2.6 FACTs cite both with the reservations noted.
- **5.9 GHz wording (89 FR 100855, 2024-12-13):** the §97.303 sharing note for 5.850–5.925 GHz now reads "operations in the Intelligent Transportation System radio service." Not tested by E1.
- **70 cm power-limit restructure (91 FR 1431):** §97.313(f) reordered (the 435–438 MHz 611 W ERP Earth/telecommand allowance stated first; the 50 W PEP US270-footnote-area limit now cites §2.106(c)(270)(i)) — same substance, new citation path; not tested by E1.
- **Symbol-rate history (88 FR 85127, 2023-12-07):** the pre-change §97.307(f)(3) capped HF data at 300 bauds and (f)(4) capped 10 m data at 1200 bauds; the pool-era (2024-07-01) text already carried the 2.8 kHz authorized-bandwidth standard, so the pool was written to the amended rule (E1A03's "2.8 kHz wide USB data signal", E1C01's keyed 2.8 kHz). No tension — historical context only; the 300-baud / 1 kHz-shift limit survives only on 2200 m and 630 m. Chapters never resurrect 300 baud as an exam fact.
- A full pool-era (2024-07-01) vs current (2026-07-28) diff confirms every other E1-cited section (§§97.301 tables aside from the W1 rows, 97.303 other paragraphs, 97.305, 97.307 other paragraphs, 97.309, 97.311, 97.313 other paragraphs, 97.315 other paragraphs, 97.317, 97.201–97.221, 97.115, 97.117, 97.119, 97.401–97.407, 97.501–97.527, 97.9, 97.5, 97.7, 97.11, 97.13, 97.15, 97.3, 97.107, 97.113, 97.121, 1.931) is textually identical.

### 7.3 The /AE indicator and §97.9(b) immediacy: RESOLVED with wording law

A General who passes Element 4 and properly submits Form 605 to the administering VEs may exercise Extra privileges **immediately** — before the VEC files anything and before ULS changes — "until final disposition of the application or until 365 days following the passing of the examination, whichever comes first" (§97.9(b), verbatim in §2.6). While doing so the station must append the indicator **AE** to the call sign — "**(3)** For a control operator who has requested a license modification from Novice, Technician, General, or Advanced Class to Amateur Extra Class: **AE**" (**§97.119(f)(3)** — NOT (f)(2); (f)(2) is AG, for upgrades to General), separated from the call sign by the slant mark (/) or any suitable word denoting it (§97.119(c)). Signing practice (one VEC's instructions, not rule text): on phone say the call sign followed by "temporary" or "Interim" AE or Alpha Echo (e.g., "This is KX9ABC temporary AE"); on CW or digital modes sign KX9ABC/AE; drop the suffix once ULS shows Amateur Extra (Laurel VEC FAQ, extracted 2026-07-30). **Contrast with new licensees:** a first-time candidate has NO authority until the grant appears in ULS — the immediacy rule is for existing licensees only. **Wording law (binding): never write "transmit as soon as you pass" without both conditions (Form 605 properly submitted to the administering VEs + CSCE in hand) and the /AE identification requirement in the same breath — §97.9(b) is conditional authority, never unconditional.**

### 7.4 Pass-threshold phrasing: RESOLVED — print "37 of 50"

§97.503(c) pins a count, not a percentage: "The minimum passing score is 37 questions answered correctly." The book prints "**37 of 50**" as the authoritative figure everywhere (cover copy, ch00, exam products). "74%" is derived arithmetic (37/50 = 0.74); when it appears at all, it is flagged as derived — e.g., "37 of 50 (74%, derived arithmetic)". The same discipline the series applied to "26 of 35" applies here.

### 7.5 Figure E5-1 is a chart, not a circuit: RESOLVED

Figure E5-1 is a rectangular-coordinate **impedance graph** — axes −600 to +600 Ω on both scales, horizontal = resistance, vertical = reactance, with eight labeled points (P1–P8) — **not** an R-L-C schematic. Any early framing of E5-1 as a circuit figure (the R, L, and C live in the question stems; the figure is the plane on which the computed impedance is plotted) is explicitly corrected here. The keyed answers are P4 (E5C10, 400 − j300), P3 (E5C11, 300 + j400), and P1 (E5C12, 300 − j400); points 5 and 7 have negative resistance (impossible for a passive series circuit — auto-wrong) and points 6 and 8 sit on the axis as distractors. The binding redraw spec is §1.4; ch05 teaches the figure as a plotting exercise per the E5C09 axis convention.

### 7.6 Pool-vs-practice teaching tensions: RESOLVED with sourced wording

- **E3B11 sporadic-E timing:** the pool keys sporadic E as "between sunrise and sunset" — a solar-ionization mechanism — while 6 m operators also work plenty of evening Es. Teach the pool answer with its mechanism; r5's "summer Es season" color is compatible; **never print "Es ends at sunset."**
- **E2C01 remote-control ID:** the pool keys "no additional indicator is required" for US remote-control operation, and r1's W9 corroborates from the rules: §97.119(c) permits but does not require indicators, and none is prescribed for remote control (the question carries no [97.x] tag). Teach it flatly — many Generals remember otherwise.
- **E2C03 30 m contest exclusion:** the pool's own wording is "generally excluded" — a long-standing convention (the WARC truce per "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.8.6), not an FCC rule. Chapters say "convention, not regulation" in the same breath.
- **E5A04 parallel-resonance impedance:** the keyed "approximately equal to circuit resistance" assumes the parallel-R model of the circuit; a series-model swap confuses strong readers. Flag the model assumption when teaching; do not "fix" the pool.
- **E5D10 electrical length vs diameter:** a larger-diameter conductor has a *longer* electrical length — counterintuitive and keyed that way ("It increases"). Pin it as written; the mechanism (diameter changes the wave's propagation along the conductor) belongs in the chapter aside.
- **PRB-1 status (E1B07/E1B11):** PRB-1 (101 FCC 2d 952 (1985)) is a declaratory ruling referenced in §97.15(b)'s parenthetical, not itself a CFR section, and it binds only state/local regulation — **not** homeowners' associations (the classic wrong answer; HOAs are private contracts).
- **E1F06 STA nuance:** §1.931 is the generic Wireless Telecommunications Services STA provision and never mentions the amateur service; the pool's keyed answer ("to provide for experimental amateur communications") matches FCC practice of granting amateur STAs rather than any amateur-specific rule text. Teach the pool answer; present §1.931 as the FCC's general STA mechanism; do not cite it as amateur-specific, and do not hunt for a Part 97 STA section (none exists — that is the resolved wording, not an open question).
- **E0 rests on Part 1 territory:** the E0A02/A04/A09/A10 answers (uncontrolled MPE at neighbors, the 5% aggregate rule, pre-May-3-2021 hand-held exemptions, 80 m evaluation always required) rest on §§1.1307/1.1310/2.1091/2.1093 and OET Bulletin 65, pointed to by §97.13(c)(1) — outside Part 97's own text. The §2.16 FACTs cite the pool IDs plus the Part 1 pointer; no contradiction exists, and no Part 97 citation should be invented for them.
- **"All these choices are correct" is the keyed answer 16 times** in this pool (E1D05, E2A02, E2A07, E2C08, E2C10, E2E04, E4A08, E4A11, E4B11, E4E02, E4E10, E6E10, E7D14, E7H13, E9F08, E0A06) **and a wrong decoy 34 times** (script-verified full-pool counts; e.g., E6C04, E6F06, E8A08, E8C03, E8C12, E9A10, E9H05, E9H10). Chapters teach content, never pattern-guessing.
- **Stem-typo ledger:** E7G02 prints "in E7-3", E7G07 prints "Figure E73", E9B04 prints "Figure E92" — published, preserved byte-exact in quotes (§1.4, §1.5), never repaired.

### 7.7 UTC naming — "Technology" (pool) vs "Telecom" (rule text): RESOLVED

The pool prints "Utilities Technology Council (UTC)" (E1C03, E1C07 — quoted byte-exact), while the current rule text §97.303(g)(2) reads "Utilities Telecom Council (UTC)" (quoted byte-exact in §2.2). Both forms are recorded; pool quotes keep the pool's form, rule quotes keep the rule's form, and ch01 may note the discrepancy in one sentence. Never blend the two in a single quotation.

### 7.8 E2B and APRS deliberate color exclusions: RESOLVED — recorded so nobody hunts

r5 (operating color) deliberately supplied **no** added color for E2B (television — standards trivia with no on-air practice beyond r3's teaching) and none for the APRS internals (E2D04, E2D07, E2D08, E2D10, E2D11), leaving both to r3's syllabus notes; E2C01/E2C12 (remote control/latency) and the E2E HF-digital mechanics are likewise r3-owned, with HF operating color owned by the General book's notes. Chapter writers must not seek r5-style color that does not exist for these groups — the FACTs in §2.8 (sourced to the pool and r3) are the complete reservoir for them.

### 7.9 Ingestion-level flags (ingestion report): RESOLVED

- **Stale syllabus counts:** the printed syllabus claims E2:61, E4:64, E9:94 (sum 602); the parse-authoritative counts are 60, 63, 93 — the syllabus was not updated for the 2nd/4th/1st errata withdrawals. The parse, not the syllabus, is authoritative (§1.3).
- **The `- 43 dB` quirk attribution:** the ingestion report §3 rule 2 attributes the interior-space choice `A. - 43 dB` to E1B03; the actual carrier is **E1C10 choice A** (verified by direct read of the canonical `.txt` — E1B03's choice A is "1 mile"). Recorded correctly here and in §1.2; the quirk itself is preserved byte-exactly either way.
- **docx-vs-pdf figure-ID typos:** `Figure E73` (E7G07) and `Figure E92` (E9B04) are genuine content differences (the PDF hyphenates them); the .docx is authoritative and the canonical files carry the typo forms — the only two of the 12 extraction differences that are not PDF wrap artifacts.
- **No ARRL mirror:** arrl.org hosts no separate copy of this pool (its link points back to NCVEC), so no NCVEC-vs-ARRL diff was possible; the two independent NCVEC renderings (.docx vs .pdf) were parsed separately and diffed instead — the cross-check of record.
- **Whitespace normalizations:** E1C12's entire block carried a leading double tab in the .docx (stripped — indentation, not content); 20 pool-body paragraphs carried a single trailing space (stripped); interior whitespace untouched, including E8B04's published double space.
- **Errata currency:** the 4th errata (2026-02-04) is the newest; there is no 5th errata as of 2026-07-30 (release page and document front matter agree). Re-check the release page before each reprint.
- **3rd-vs-4th cross-check:** the only difference between the 3rd-errata parse (600 active + 3 deleted) and the 4th (599 + 4) is the removal of E4D05 — zero content differences among the 599 common questions, all 60 heading lines identical.
- **Release-page quirks:** the 2nd-errata "G8C/15 questions" misprint (the affected group is E2A, 12 remain) and the 3rd-errata date disagreement (page: September 24; sheet and file names: September 25, 2025) are cataloged in §1.3 — never propagated.

### 7.10 Wording laws lifted from Books 2 and 3 (r2 watch items): RESOLVED — adopted unchanged

- **Upgrade immediacy:** never write "you may transmit as soon as you pass" — the authority requires both the Form 605 properly submitted to the VEs and the CSCE in hand (§97.9(b)), and every transmission under the new privileges must carry the AE indicator (§97.119(f)(3)) until ULS shows Amateur Extra (§97.119(c) governs the "/" or "suitable word" form). For brand-new licenses the opposite rule holds: no transmitting until the grant appears in ULS. (This is §7.3's law, restated as the series-level wording law.)
- **Grant timing:** no official FCC-wide guarantee exists, and upgrades have no fee step — do not print any day count as a promise; the safe line is "your ULS record typically updates within days."
- **Remote exams:** availability depends entirely on the individual VE team (Laurel runs in-person only); chapters point readers at ARRL's session finder and hamstudy.org/sessions and never promise remote testing.
- **CORES "free":** no primary sentence states FRN registration is free, and no payment step exists in the flow — the book says "carries no fee and no exam requirement" and never prints "free of charge."
- **Laurel VEC web address:** larc-vec.org (the legacy laurelvec.com domain 307-redirects there; verified 2026-07-23). The "temporary AE"/"Interim"/"Alpha Echo" phone phrasing is one VEC's practical instruction, not rule text — the rule requires only the AE indicator separated by "/" or a suitable word (§97.119(f)(3), (c)).
- **Multiple elements, one session:** if a candidate passes multiple elements at one session, the VEC transmits one application reflecting the highest class earned — a Technician may in principle test straight through to Extra in one session.

### 7.11 Time-sensitive values — verification dates, re-verify triggers, and the pool-swap procedure: RESOLVED with this register

Each value below is pinned in §2 with its verification date. **Every one must be re-verified at the stated trigger before any reprint or new edition**, and the canon updated with the new verification date:

| Item | Pinned value | Verified | Re-verify trigger |
|---|---|---|---|
| **Pool currency (the big one)** | 2024–2028 Extra pool valid for exams 2024-07-01 → **2028-06-30**; 4th errata (2026-02-04) incorporated; no 5th errata | 2026-07-30 (ncvec.org release page; `canon/ingestion-report.md`) | Each reprint; **check ncvec.org from late 2027 for the 2028–2032 successor pool** (expected late 2027 by analogy with the 2026 Technician cycle, but NCVEC has announced no date — never print a release date as fact) |
| FCC application fee | $35 (new license, renewal, rule waiver, vanity request), effective 2022-04-19; **upgrades EXEMPT** | 2026-07-30 (arrl.org/fcc-application-fee) | Before each reprint (fees are set by FCC order and can change in any fiscal-year fee order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 for candidates under 18 | 2026-07-30 (arrl.org/arrl-vec-exam-fees — explicitly calendar-2026 figures) | Each January |
| NCVEC Form 605 edition | 2022 edition | 2026-07-30 (ncvec.org, HTTP 200 application/pdf) | Before publication and each reprint (the form's mandatory fields drive ch00's session instructions) |
| Part 97 rule text | eCFR current issue 2026-07-28 (byte-identical to 2026-07-20); pool-era comparisons against the 2024-07-01 issue; includes the 60 m amendment 91 FR 1430/1431 and housekeeping 90 FR 57712 | 2026-07-30 (eCFR versioner API; all §2 rule quotes copied from those retrievals) | Re-pull every cited section before any reprint |
| Satellite fleet | Named birds are time-sensitive: FalconSAT-3 re-entered January 2023; SO-50 and QO-100 status shifts month to month; the pool tests concepts only, never specific satellites — keep the book that way | 2026-07-30 (amsat.org; arrl.org news 2023-01-20) | Before print, check amsat.org/status/ and drop or demote any bird that has gone quiet |
| 6 m digital frequencies | FT8 50.313 (50.323 intercontinental), FT4 50.318, MSK144 calling 50.260 — all convention, not band plan | 2026-07-30 (OnAllBands; hamdeck.com; QEX MSK144 paper) | Before print, against the current WSJT-X default frequency table and ARRL band plan |
| WSPR sensitivity | −31 dB SNR in 2500 Hz (WSJT-X 2.7 guide); older documentation says −28 dB | 2026-07-30 (WSJT-X 2.7 User Guide §1) | Before print, against the current User Guide; attribute any −28 mention to "earlier WSPR documentation" |
| Doppler magnitudes | ±3.5 kHz (2 m) / ±10 kHz (70 cm), typical-LEO order-of-magnitude | 2026-07-30 (orbitalradar.com; club decks) | Present as order-of-magnitude practice, never constants |
| EME path loss | ≈252 dB at 144 MHz, ≈271 dB at 1296 MHz — band-specific | 2026-07-30 (electronics-notes.com; Chalmers thesis) | Never generalized as "EME path loss is 252 dB" without the band |
| QO-100 footprint | Brazil-to-Thailand; of the Americas only northeast Brazil — the geostationary *example*, not a US opportunity | 2026-07-30 (radarc.org; amsat-uk.org; jeremyclark.ca) | Before print; always note continental-US readers cannot reach it |
| CEPT country lists | DA 16-1048's participating-country lists are dated 2016-09-16 and change over time | 2026-07-30 (docs.fcc.gov PDF) | Before travel-related reprints, check the European Communications Office |
| fcc.gov HTML pages | Amateur Service and Amateur Call Sign Systems facts lifted from the 2026-07-23/24 verifications (pages 403 to curl — bot protection) | 2026-07-24 | Re-verify in a browser before publication |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com 307-redirects there) | 2026-07-23 | Before each reprint |

**Contained-swap procedure for the 2028–2032 pool (binding):** the book's teaching content is durable by design — only the pool-facing artifacts change with a new pool. On release of the successor pool: (1) ingest it into `canon/` with a new ingestion report (new canonical files, sha256s, errata ledger, deleted-ID list); (2) update this canon's §1 (files, counts, validity window) and any §2 FACT or §7 resolution whose rule or frequency changed; (3) refresh each chapter's Exam Focus question picks and Appendix A's verbatim pool against the new canonical files; (4) re-run the build audit and the full test suite to green; (5) nothing else changes — notation, glossary, chapter map, teaching prose, and figures stay as pinned here. Any printing of this book after mid-2028 must state which pool exams actually use.

### 7.12 The ch10 MPE illustration's units and averaging window: RESOLVED — W/m² and the 30-minute uncontrolled window

Two defects in the enrichment-only MPE illustration (ch10's worked example, the `ch10-mpe-math` figure, and Appendix B's S = ERP/(4πR²) micro-example) were caught at technical audit on 2026-07-31 and fixed in place. This canon had pinned no numeric value for the illustration before (the only prior pin is the formula itself, §2.16's enrichment FACT), so this resolution is the numeric pin of record.

- **Power-density units (was wrong by 10×):** S = ERP/(4πR²) for 100 W ERP at 10 m is 100/(4π × 10²) ≈ 0.08 **W/m²** = 0.008 mW/cm²; the draft's "0.08 mW/cm²" conflated the two units. **Corrected pin (binding for ch10, Appendix B, and the figure):** peak S ≈ **0.08 W/m² (0.008 mW/cm²)**; ≈ **0.016 W/m²** after SSB speech duty (0.2 while keyed); ≈ **0.008 W/m²** across the window (key down half of it); the uncontrolled 30–300 MHz floor is **2 W/m² (= 0.2 mW/cm²)**, so the peak sits ≈ **25×** under the limit and the window average ≈ 250× under. The MPE limits themselves stay in mW/cm² (OET Bulletin 65's own units — 100 below 1.34 MHz, 180/f² to 30 MHz, 0.2 across 30–300 MHz, f/1500 to 1.0 above 1,500 MHz, controlled 5× higher); the station's computed densities are W/m², with the mW/cm² equivalent named at first use.
- **Averaging window (was the wrong regime):** OET Bulletin 65's averaging windows are **6 minutes for controlled exposure and 30 minutes for uncontrolled**. The worked example's scenario is the neighbor's lot line — uncontrolled territory (E0A02) — so its window is **30 minutes**; the draft's "6-minute averaging window" was the controlled value misapplied to an uncontrolled scenario. ch10 now teaches both windows explicitly (6 controlled / 30 uncontrolled), and the worked example, the figure's bottom panel, and Appendix B all use the 30-minute uncontrolled window.
- **Superseded mirrors:** `chapters/specs/ch10.spec.md` §5 and the `figures/figures.json` caption/spoken fields for `ch10-mpe-math` still carry the old "0.08 mW/cm²" / 6-minute wording (outside the audit's edit scope) — refresh both at the next spec/figures maintenance pass; this section governs until then.

---

*End of canon. Every claim in this book traces to this file, to `canon/pool-extra.*`, or to original prose. If a chapter disagrees with this file, the chapter is wrong.*
