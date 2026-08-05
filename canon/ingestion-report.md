# Ingestion report — 2024–2028 NCVEC Extra (Element 4) question pool

Date: 2026-07-30 (UTC). Operator: automated ingestion (Kimi Code CLI).
Status: **all verification checks passed; audit exit 0; pytest exit 0.**

## 1. Source files

Landing page: <https://ncvec.org/index.php/2024-2028-extra-class-question-pool-release>
(verified working 2026-07-30). Downloaded 2026-07-30 into `canon/source/`
(curl with a browser User-Agent; no 403s):

| file | bytes | sha256 |
|---|---:|---|
| `source/ncvec-2024-2028-extra-pool-4th-errata-feb4-2026.docx` | 674,155 | `581ff3aa4c98bb2a6fcc303fe1ce19beb29bc7d3d02ff7fe5c6162c4c26ce4f7` |
| `source/ncvec-2024-2028-extra-pool-4th-errata-feb4-2026.pdf` | 952,745 | `9cc63ae0c1c9ee63a617824555d5b4e73da8c8edb91566f97a66770eb200f517` |
| `source/ncvec-2024-2028-extra-pool-3rd-errata-sept25-2025.docx` | 673,424 | `e24c58d10b92c0d3e9e2a91bc4400aa7979cd299accb1459fed77b7a99a064ad` |
| `source/ncvec-2024-2028-extra-pool-3rd-errata-sept25-2025.pdf` | 951,138 | `f668b1fd9ddf7ba1cefacc3bd73767ebb6f2e1b5e9a3015f52977ab6c160c64e` |
| `source/Extra_Figures_2024-2028-1.pdf` | 78,505 | `591bb4c9fc9a9267e298b3ee23c93ab54ba3813f8ea3730123f9ccda1e4b80f2` |
| `source/2024-2028 Amateur Extra Class Pool Diagrams_Page_1.jpg` | 142,593 | `fff1411a04c35aa58262e64d8188f75778fbd00cabe7997f9d8eae298df9a2cb` |
| `source/2024-2028 Amateur Extra Class Pool Diagrams_Page_2.jpg` | 168,703 | `6b085fb7461331899b33c24a0e9eb690bc0d555e00775086538cd5b8742931a9` |
| `source/2024-2028 Amateur Extra Class Pool Diagrams_Page_3_V2.jpg` | 120,970 | `b67ea1b4109f04b7a9142254e7ec0d944e4a36736f0ed8dce54f9b10abb53ba9` |
| `source/e4_2024-svgs.zip` | 30,740 | `baf46fe88b6914f971f446bfdc1550622d0dcf89d1bfb938ef0dfdcaa85aa558` |
| `source/release-page.html` | 26,364 | `6a18e7265fd62bd39dbd5175eaff90107fe6eab5f365b7e24db3b5fc51a1d2f5` |

The canonical document is the **4th-errata release** ("2024-2028 Extra Class
Question Pool and Syllabus Public Release with 4th Errata Feb 4 2026"), the
file at the top of the release page. Its front matter carries all four errata
sheets in full, and the pool body already incorporates every change (verified
in §5.2/§5.3). The pool is **public domain** — the release page states twice:
"The NCVEC Question Pool Committee hereby releases into public domain the
2024-2028 Element 4 Extra Class Question Pool." Effective for exams
2024-07-01 … 2028-06-30.

The 3rd-errata release (docx+pdf) is kept as the pre-4th baseline for the
errata cross-check in §5.3. `release-page.html` is the fetched release page
itself (the errata ledger source, including the "G8C" misprint, §5.2).
`source/sha256sums.txt` records the same hashes.

**Post-fourth-errata check:** the release page (fetched 2026-07-30) lists the
4th errata (2026-02-04) as the newest entry; there is **no 5th errata**. The
page's own errata history and the document's front matter agree exactly.

**Pool figures (10 graphics, all obtained):** the Extra pool ships ten figures
— E5-1, E6-1, E6-2, E6-3, E7-1, E7-2, E7-3, E9-1, E9-2, E9-3 — published in
three independent forms, all downloaded: the figures PDF
(`Extra_Figures_2024-2028-1.pdf`, 3 pages), three JPG diagram pages (page 1:
E5-1/E6-1/E6-2/E6-3; page 2: E7-1/E7-2/E7-3/E9-1; **page 3 is the "V2" file**:
E9-2/E9-3 — the re-issue incorporating the 1st-errata Smith-chart rotation),
and `e4_2024-svgs.zip` (all ten figures as SVG; each file verified as
well-formed XML). The .docx embeds the same ten graphics as PNG media. All
three JPG pages and the SVG zip were inspected visually/content-wise; **E9-3
is confirmed in its post-errata form** — the Smith chart in conventional
horizontal orientation, **infinity on the right**, 0 on the left.

### ARRL cross-check mirror — not available as a separate file

<https://www.arrl.org/question-pools> does **not** host its own copy of the
2024–2028 Extra pool: its "EXTRA POOL" link points back to the NCVEC release
page above (confirmed by fetching the ARRL page HTML 2026-07-30). Therefore no
NCVEC-vs-ARRL content diff is possible. As a substitute cross-check with equal
evidentiary value, the two independent NCVEC renderings (.docx vs .pdf) were
parsed separately and diffed — see §4.

## 2. Outputs

| file | bytes | sha256 |
|---|---:|---|
| `canon/pool-extra.txt` | 175,707 | `a03fb3c8b4a8401a196057c34199bd1d355931170c1fef9625fbdd9421f48d0e` |
| `canon/pool-extra.json` | 267,486 | `6fdf1cae68793c94dd2965dfac02a4e614e0ee2d825009ef4cd76fe06a8bfa50` |

`pool-extra.json` matches `tests/fixtures/pool_sample.json` schema exactly:
top-level object keyed by question id; each entry has, in fixture key order,
`group` ("E1A"), `subelement` ("E1"), `question` (single string), `choices`
(object with exactly "A".."D"), `answer` (one of "A".."D"), `figure` (null, or
the published figure id, e.g. "E7-3"). No extra keys (the Part 97 references
are kept only in the .txt, which preserves the published ID-line format).

`pool-extra.txt` follows `tests/fixtures/pool_sample.txt` layout and the
series convention: `E1A01 (D) [97.305, 97.307(b)]` ID line (answer in
parentheses, Part 97 ref(s) in brackets where published), question text,
`A.`–`D.` choice lines, `~~` block separator. Subelement (`SUBELEMENT E1 -
COMMISSION RULES [6 Exam Questions - 6 Groups]`) and group (`E1A Frequency
privileges; …`) headings are preserved as published — the Extra pool prints
them with plain hyphens, unlike the General pool's en dashes (preserved, not
normalized). A `#`-comment header documents provenance and the normalization
rules; the file ends with the published tail marker `~~~end of question pool
text~~~` and the published `NOTE: The graphics required for certain questions
in sections E5, E6, E7, and E9 are included on the following pages.` line,
both verbatim.

## 3. Converter and normalization rules

Tooling probe: `pandoc` absent, `python-docx` absent, `pdftotext` present.
Chosen converter: **the .docx, parsed directly** with python3 `zipfile` +
`xml.etree.ElementTree` over `word/document.xml` (no third-party packages —
same approach as the Tech/General builds). The docx carries logical
paragraphs, so wording is byte-exact with no line-wrap artifacts.

Normalization rules (also in the .txt header):

1. Each question/choice printed as one line, exactly as the docx paragraph;
   no re-wrap or reflow. Every one of the 599 questions parsed as exactly one
   question paragraph plus 4 single-paragraph choices (**0 anomalies** from
   the strict parser; any deviation raised an error).
2. Paragraph-edge whitespace is stripped (indentation/trailing space, never
   content). 32 paragraphs affected, in two classes:
   - **E1C12's entire block** (ID line, question, 4 choices, `~~`, plus two
     blank lines) carries a leading **double tab** in the .docx — indentation,
     not content; stripped. (The block is *not* indented in the PDF.)
   - 20 pool-body paragraphs (question or choice lines) carry a single
     **trailing space**; stripped. (4 further trailing spaces occur in the
     errata front matter, which is not carried.)
   Interior whitespace is untouched: the published **double space inside
   E8B04's question** ("…modulating frequency  is 2 kHz…") is preserved
   byte-exactly, as is `A. - 43 dB` (E1B03 choice A, interior space after the
   minus sign).
3. No U+00A0 no-break spaces, soft hyphens, or fi/fl ligatures occur anywhere;
   none were altered. The only double space in the carried pool text is
   E8B04's (rule 2). (The E9E10 deleted placeholder is published with a
   double space — §5.3; placeholders are not carried.)
4. Published Unicode punctuation preserved byte-exactly: curly apostrophe
   U+2019 (×60), curly quotes U+201C/U+201D (×16 each). These are the only
   non-ASCII characters in the pool text; the headings are pure ASCII.
5. ID lines preserve the published form: 66 questions carry a Part 97 ref
   (**all in subelement E1** — every E1 question except E1C04 and E1C06;
   58 single refs, 8 comma-separated multi refs); the other 533 are published
   as bare `E2A01 (D)`. Both forms kept. No trailing-space ID-line quirk in
   this pool (contrast General's G9C01).
6. Published figure-reference quirks preserved (see §5.4): E7G02 "the circuit
   in E7-3" (no "Figure"), E7G07 "Figure E73" and E9B04 "Figure E92" (missing
   hyphens). Never repaired. The PDF rendering hyphenates the latter two —
   a genuine docx-vs-pdf content difference, cataloged in §4.
7. No choice-label quirks: all 2,396 choice lines are published in the exact
   form `L. text` (contrast General's G2E02 "D.A DX…").
8. The PDF (pdftotext -layout) was parsed fully independently for the diff in
   §4; its wrap artifacts are not in this data.

## 4. Cross-extraction diff (docx vs pdf)

Both parsers produced **599 questions / 50 groups / 10 subelements / 4 deleted
placeholders** with identical id order, all 10 subelement headings equal, and
all 50 group headings equal after whitespace normalization except one wrap
artifact below. Field-by-field diff over question text, all 4 choices per
question, answer letters, Part 97 refs, and ID lines (whitespace-normalized):
**exactly 12 differences**, in two classes:

**Class 1 — PDF hyphen-wrap extraction artifacts (10 fields + 1 group
heading).** pdftotext split hyphenated words at line breaks and the join left
a space; docx is authoritative in every case:

- E1B04 choice B: pdf `…six- character grid locator` vs docx `…six-character grid locator`
- E1C02 choice A: pdf `…non- Government Organization…` vs docx `…non-Government…`
- E2B08 question: pdf `…70- centimeter band` vs docx `…70-centimeter band`
- E3C03 question: pdf `…A- index or K-index…` vs docx `…A-index or K-index…`
- E4C02 question: pdf `…strong out-of- band signals` vs docx `…out-of-band…`
- E8B11 choice C: pdf `…sub- carrier` vs docx `…sub-carrier`
- E9C01 question: pdf `…spaced 1/2- wavelength apart…` vs docx `…1/2-wavelength…`
- E9C02 question: pdf `…spaced 1/4- wavelength apart…` vs docx `…1/4-wavelength…`
- E9C03 question: pdf `…spaced 1/2- wavelength apart…` vs docx `…1/2-wavelength…`
- E9E06 question: pdf `…quarter-wave Q- section…` vs docx `…Q-section…`
- E4C group heading: pdf `…SDR non- linearity…` vs docx `…SDR non-linearity…`

**Class 2 — genuine content differences (2 fields), the published figure-ID
typos.** The .docx prints `Figure E73` (E7G07) and `Figure E92` (E9B04); the
.pdf prints `Figure E7-3` and `Figure E9-2` (verified on unwrapped single
lines in the pdftotext output — not wrap artifacts). The .docx is
authoritative; the canonical files carry `E73`/`E92` byte-exactly, and the
JSON `figure` field carries the real published figure ids (`E7-3`, `E9-2`).

No other differences of any kind (no answer-letter, ref, ID-line, ordering, or
heading differences).

## 5. Verification evidence

### 5.1 Counts and structure (parse-authoritative)

- Total published ID lines in the pool body: **603** = **599 active questions**
  + **4 deleted placeholders**. The active count **599** is the
  parse-authoritative number and matches the plan's expectation (603 at the
  December 7, 2023 release − 4 withdrawn). No duplicate ids; document order ==
  canonical pool order (E1…E9, E0 / group A→last / number), verified in the
  JSON and by re-parsing the .txt.
- Subelements: **exactly 10** (E1–E9, E0). Groups: **50** (the exam draws one
  question per group → a valid 50-question exam; 37 to pass).
- Group letters: E1 A–F, E2 A–E, E3 A–C, E4 A–E, E5 A–D, E6 A–F, **E7 A–H**,
  E8 A–D, **E9 A–H**, E0 A — the letter class reaches **H** (E7/E9), matching
  the audit's retargeted `E\d[A-H]\d\d` regex (plan Task 1.3).
- Numbering is contiguous within every group from 01 up, **except exactly the
  three interior gaps** E4D05, E6D07, E9E10 — all known deletions. The fourth
  deletion, **E2A13, leaves no numbering gap** (it was the last question of
  E2A; the group now ends at E2A12). Zero unexplained gaps.
- Every question: exactly 4 non-empty choices keyed A–D; answer ∈ {A,B,C,D};
  question text non-empty. (Answer-letter sanity: A×150, B×150, C×150, D×149.)

Per-subelement / per-group counts (authoritative, from the parse):

| subelement | questions | groups | per-group counts |
|---|---:|---|---|
| E1 | 68 | 6 | E1A:11 E1B:11 E1C:12 E1D:12 E1E:11 E1F:11 |
| E2 | 60 | 5 | E2A:12 E2B:12 E2C:12 E2D:11 E2E:13 |
| E3 | 39 | 3 | E3A:14 E3B:13 E3C:12 |
| E4 | 63 | 5 | E4A:11 E4B:11 E4C:14 E4D:13 E4E:14 |
| E5 | 49 | 4 | E5A:13 E5B:12 E5C:12 E5D:12 |
| E6 | 68 | 6 | E6A:12 E6B:11 E6C:11 E6D:11 E6E:12 E6F:11 |
| E7 | 99 | 8 | E7A:11 E7B:12 E7C:11 E7D:15 E7E:11 E7F:14 E7G:12 E7H:13 |
| E8 | 48 | 4 | E8A:11 E8B:11 E8C:15 E8D:11 |
| E9 | 93 | 8 | E9A:12 E9B:11 E9C:14 E9D:12 E9E:10 E9F:12 E9G:11 E9H:11 |
| E0 | 12 | 1 | E0A:12 |
| **total** | **599** | **50** | |

Syllabus reconciliation: the syllabus printed in the final document claims
E1:68, E2:61, E3:39, E4:64, E5:49, E6:68, E7:99, E8:48, E9:94, E0:12 (sum
**602**). Six subelements match the parse exactly (E1, E3, E5, E6, E7, E8,
E0). The printed **E2 (61), E4 (64), and E9 (94) counts are stale**: they
were not updated for the 2nd (E2A13), 4th (E4D05), and 1st (E9E10) errata
withdrawals respectively — the actual bodies hold 60, 63, and 93. (E6's
printed 68 *does* match: it reflects the 3rd errata's E6D07 withdrawal.)
The per-group active counts match each errata sheet's own "leaving N
questions" statements exactly (E9E:10, E2A:12, E6D:11, E4D:13). The parse,
not the syllabus, is authoritative.

### 5.2 Errata ledger (all four; from the document's front-matter errata sheets, cross-checked against the release page)

| errata | issued | changes |
|---|---|---|
| Errata 1 | 2024-01-31 | **Diagram E9-3 (Smith chart) rotated 90°** to the conventional horizontal orientation, infinity on the right; all pool documents (PDF, JPG, Word) updated. 5 questions modified: E1D07 ("group of"→"of the following"), E1F03 (answer D replaced), E4D12 ("100 W"→"10 W"), E4D13 ("100 W"→"10 W"), E6A06 (answer B gains "The change in"). **1 withdrawn: E9E10** (E9E not renumbered, 10 remain). Citation-only fixes: E1E10 → `[97.509(m)]`, E1E11 → `[97.509(i)]`. |
| 2nd errata | 2024-11-08 | **1 withdrawn: E2A13** (E2A not renumbered, 12 remain). |
| 3rd errata | 2025-09-24 (release page) / sheet dated 2025-09-25 | **1 withdrawn: E6D07** ("more than one correct answer"; E6D not renumbered, 11 remain). |
| 4th errata | 2026-02-04 | **1 withdrawn: E4D05** (E4D not renumbered, 13 remain). |

All five published text modifications and both citation fixes (errata 1) were
verified **present in the final pool text byte-exactly**: E1D07 question,
E1F03 choice D, E4D12 question, E4D13 question, E6A06 choice B, and the ID
lines `E1E10 (C) [97.509(m)]`, `E1E11 (B) [97.509(i)]` — all OK.

**Published quirks cataloged (never propagated, never repaired):**

- **The "G8C" misprint:** the release page's 2nd-errata note reads "The
  remaining questions in **G8C** were not renumbered, leaving 15 questions."
  The affected group is of course **E2A** (12 remain) — "G8C/15" is a
  copy-paste slip from the General pool's 5th errata, a quirk of the *page*;
  the document's own errata sheet correctly says E2A. Cataloged; not
  propagated.
- **Date disagreement, 3rd errata:** the release page says "Release date
  September 24 2025" while the document sheet and the file names say
  September 25, 2025. Both dates recorded; the ledger shows both.
- **E9E10 placeholder spacing:** the .docx prints E9E10's deleted placeholder
  with a double space (`E9E10  Question Deleted (section not renumbered)`)
  while the other three placeholders use a single space (the PDF collapses it
  to one). Placeholders are not carried into the canonical files.

### 5.3 Deleted questions — verified

The four withdrawn IDs from the plan were confirmed against the errata sheets
in the document front matter **and** against the release page text **and**
against the pool body, where each appears as a placeholder line
`EnX## Question Deleted (section not renumbered)` (E9E10's with a double
space — §5.2):

- E9E10 (errata 1), E2A13 (errata 2), E6D07 (errata 3), E4D05 (errata 4).

The deleted set from the parse == the plan's list exactly. The canonical
files carry the **active pool only**; the deletions are visible as numbering
gaps (E2A13 as the truncated end of E2A). IDs were never renumbered.

**3rd-vs-4th document cross-check:** the 3rd-errata .docx was parsed with the
same strict parser: 600 active + 3 deleted, 0 anomalies. Diff against the
4th-errata parse: the only difference is the removal of E4D05 (present as a
full question in the 3rd — `E4D05 (A)`, "What transmitter frequencies would
create an intermodulation-product signal in a receiver tuned to 146.70 MHz
when a nearby station transmits on 146.52 MHz?" — a placeholder in the 4th);
**zero content differences among the 599 common questions**, and all 60
subelement/group heading lines identical — the 4th errata changed nothing
else.

### 5.4 Figure-referencing questions (10 pool graphics, 28 questions)

The pool ships ten graphics (sources in §1). 28 questions reference them;
each carries `"figure": "<id>"` in the JSON (the other 571 carry
`"figure": null`):

| figure | questions | published reference form |
|---|---|---|
| E5-1 | E5C10, E5C11, E5C12 | E5C10/E5C12: "point on Figure E5-1"; E5C11: "point in Figure E5-1" |
| E6-1 | E6A10, E6A11 | "In Figure E6-1" |
| E6-2 | E6B10 | "In Figure E6-2" |
| E6-3 | E6C08, E6C10, E6C11 | "In Figure E6-3" |
| E7-1 | E7B10, E7B11, E7B12 | "In Figure E7-1" / "shown in Figure E7-1" |
| E7-2 | E7D06, E7D07, E7D08 | "shown in Figure E7-2" |
| E7-3 | E7G02, E7G07, E7G09, E7G10, E7G11 | E7G02: "the circuit in **E7-3**" (no "Figure"); E7G07: "Figure **E73**" (no hyphen); others "Figure E7-3" |
| E9-1 | E9B01, E9B02, E9B03 | "shown in Figure E9-1" |
| E9-2 | E9B04, E9B05, E9B06 | E9B04: "Figure **E92**" (no hyphen); others "Figure E9-2" |
| E9-3 | E9G06, E9G07 | "the Smith chart shown in Figure E9-3" (the Smith chart — 1st-errata rotated form confirmed visually, infinity on the right) |

All references are capitalized "Figure" where the word appears; the three
phrasing quirks (E7G02's missing "Figure", E7G07's "E73", E9B04's "E92") are
published and preserved byte-exactly — and the latter two are genuine
docx-vs-pdf differences (§4). Detection: regex over question text for the
published figure ids (hyphenated and typo forms); **no figure mentions occur
in any choice text** (choice-text hits for "figure" are "noise figure",
"figure-eight", and "letters/figures shift" — never pool-figure references).
The document's closing NOTE confirms the figure sections: "The graphics
required for certain questions in sections E5, E6, E7, and E9 are included on
the following pages."

### 5.5 Round-trips

- `json.load()` on `pool-extra.json`: OK; schema/key-order/types checked
  against the fixture shape for all 599 entries (`group`, `subelement`,
  `question`, `choices{A..D}`, `answer`, `figure`); `figure` is null or one of
  the ten published figure ids.
- `pool-extra.txt` re-parsed with an **independent** script (shares no code
  with the generator): 599 question blocks, 10 subelement headings, 50 group
  headings, 56 header-comment lines, 2 published tail lines; ids, order,
  answer letters, question texts, and all 2,396 choice texts identical to the
  JSON. 0 mismatches.
- `python3 tools/audit_book.py`: **exit 0** — "Audit PASSED: 0 errors,
  0 warning(s)." Check [8/8] loaded the pool JSON (not skipped), found no
  chapter quotes to check, and printed "appendix coverage skipped (no
  appendices/pool.md)".
- `python3 -m pytest -q`: **exit 0** — 107 passed.

## 6. Notes on schema adaptation

- The audit's check #8 reads only `canon/pool-extra.json`; the fixture schema
  has no field for the Part 97 rule references. Those references are data the
  NCVEC publishes on the ID line, so they are preserved in the .txt ID lines
  (e.g. `E1A01 (D) [97.305, 97.307(b)]`) and omitted from the JSON rather
  than adding a non-fixture key.
- `figure` values use the pool's own labels ("E5-1" … "E9-3") — the
  *published figure ids*, hyphenated even where the referencing question text
  carries the typo'd form (E7G07 "E73" → `"figure": "E7-3"`; E9B04 "E92" →
  `"figure": "E9-2"`; E7G02 "in E7-3" → `"figure": "E7-3"`).
- The four deleted questions are absent from both canonical files by design
  (active pool only); the deletion record lives in this report and in the
  numbering gaps. The audit's coverage check tolerates non-contiguous
  numbering (its own fixture carries a deleted-ID gap), so no tool changes
  were needed.
- No content wording was altered for schema reasons; the only adaptations are
  the normalization rules in §3 (paragraph-edge whitespace: E1C12's
  tab-indented block + 20 trailing spaces).
