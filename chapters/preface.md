## Preface — Why & How This Book Was Made

Every course in this series opens by going straight to the work, and this one does too, starting in Chapter 0 — but a capstone earns a few pages about itself first: why it exists, and how it was made.

### Why This Book Exists

This book exists to carry an experienced General to a passed Amateur Extra exam. The exam is 50 questions drawn one per group from a public pool, and 37 of 50 correct answers passes it; the prize is every operating privilege the FCC grants an amateur, including the Extra-only segments of five HF bands. Extra is the last license class — there is no element beyond Element 4 — and that makes this book the capstone: with it, the series arc completes, Technician to General to Extra.

The series began with *200 Meters and Down*, a technical history of amateur radio, and continued through two course books — *Your First Ham License* for the Technician license and *Your Next Ham License* for the General. This is the third course and the end of the road: everything the service offers, taught to the depth the Extra pool demands.

Like its siblings, the book is aligned to the official question pool — the NCVEC 2024–2028 Extra pool, valid for exams through 2028-06-30. After that date a successor pool takes over, and this book's pool-facing parts were designed from the start to be swapped to meet it.

### How This Book Was Made

The book was built by a multi-agent AI workflow — one orchestrating agent and roughly fifty subagents, all instances of Claude Opus 4.8 running inside the Claude Code tool — working from a single source of truth. The official, public-domain NCVEC pool was ingested verbatim and double-parsed from the two published formats until the parses agreed, and all four errata were incorporated, including the four questions withdrawn across them. Around the pool grew an accuracy canon — the verified facts, notation, and rules that every writer had to obey — and the canon was treated as law.

Against that canon, parallel agents wrote the chapters and drew the figures, while span auditors re-verified every factual claim against the canon and every quoted question against the pool, word by word. An eight-check automated audit gates the whole repository, and its heaviest check is mechanical verbatim-pool fidelity: all 599 active questions quoted exactly, every answer key matching the official key.

The figures follow the same discipline. All 39 are original; the pool's ten official graphics were redrawn as original SVGs, never copied — including the E9-3 Smith chart in its rotated post-errata form — and each redraw was geometrically verified against the official art. The audiobook was produced just as mechanically: the text prepared for narration and synthesized in eight voices, with formulas and figures spoken as words.

### The Production, by the Numbers

- **Words:** 113,805 — 53,537 chapters, 47,998 annotated pool, 12,270 glossary and formulas.

- **Figures:** 39, all original.

- **Pool questions annotated:** 599 of 599 — every active question verbatim, answer keyed, one-line why.

- **Tooling tests:** 107.

- **Audit checks:** 8.

- **Subagent launches:** about 50 (estimate).

- **Calendar span:** 2026-07-29 → 2026-07-31.

- **Subagent tokens:** about 5.8 million (estimate). This runtime does not meter subagent tokens; the estimate models all agent reads of the canonical files plus written output volume at ~4 characters per token — Book 1's metered ~4.7M corroborates the scale.

### What You Can Trust

The integrity rules were simple, and they were enforced. The prose is original, written for this book. Part 97 and the question pools are public domain, and where the pool speaks in this book it speaks verbatim, marked as a quote. No quotation was fabricated. And every claim the exam depends on survived the audit described above — the same audit you can run yourself, from the repository, with one command.
