# Your Last Ham License — Implementation Plan

> **For agentic workers:** implement this plan task-by-task (subagent-driven development recommended). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce *Your Last Ham License: The Extra Course (2024–2028)* — an ~50–65k-word (chapters), ~30–40-figure capstone course + exam-prep book aligned to the **2024–2028 NCVEC Amateur Extra pool (Element 4)** — expected **~599 active questions** (603 at release − 4 withdrawn as of 2026-07-30; the parse is authoritative) across 10 subelements (E1–E9, E0) and **~50 groups**, exact counts **verified at ingestion**; the exam is **50 questions, one per group, 37 to pass** — as self-contained HTML/PDF/TXT editions plus Docker site, practice-exam generator (50-question Extra exams), and 8-voice audiobook, built by a multi-agent workflow against a verified accuracy canon that carries the pool verbatim. Appendix A is the largest yet (~45k+ words verbatim). Shipping this book activates `/extra/` and **completes the three-book series site**.

**Architecture:** Same two tracks as Books 2–3. **(A) Tooling** — the **General repo's** toolchain copied wholesale (it is the newest base: h4 support, markdown pipe-table support, `speak_math` formula tokens, series machinery, 79-test suite, 8-check audit incl. pool fidelity) and retargeted at constants level only, plus TDD extensions where the Extra material demands them (`mathsvg` + `speak_math` for the Extra formula set; `make_exam.py` parameterized to the **50-question / 37-to-pass** structure — General/Tech were 35/26). **(B) Content** — canon (incl. verbatim pool) → figures (incl. every pool figure redrawn + the Smith-chart family) → 11 chapters + 2 appendices, produced by parallel writer/figure/auditor agents and gated by the Track-A harness. Track A first so Track B writes into a green gate. Spec phase letters: A = spec/plan (done) · B = scaffold (Phases 0–1) · C1 = canon (Phase 2) · C2 = figures (Phase 3) · C3 = chapters (Phase 4) · D = front matter (Phase 5) · E = verify & ship (Phase 6).

**Tech Stack:** Python 3 (stdlib + `edge-tts`, `matplotlib`), headless `google-chrome` for PDF, `ffmpeg` for audio, nginx/Docker, GitHub Actions → GHCR. Base for all copying: `/home/kasm-user/your-next-ham-license/` ("Book 3", the General repo — the newest toolchain; **NOT** `your-first-ham-license` and **NOT** `200-meters-and-down`). Design spec: `docs/superpowers/specs/2026-07-29-your-last-ham-license-design.md` (approved).

## Global Constraints

- **ONE commit at the very end**, after full verification (pytest green + `audit_book.py` exit 0 + real build + spot-reads). No per-task/phase commits. The only allowed exceptions are the **two** cross-repo series-bar touches at ship (Phase 6: the Technician repo *and* the General repo each flip Extra live) — each its **own tiny commit, approved by the human at that moment, never assumed**, never bundled with each other or with anything else.
- **Parallel fan-out when building**: figures, chapters, appendix annotations, audits run as parallel agents.
- **All repos/packages public.** Repo `Atvriders/your-last-ham-license`, branch `master`, GitHub-primary (no Gitea CI — dead path; do not copy `.gitea/`). Push only after the ship gate.
- **Never the `gh` CLI** — GitHub REST API via curl with the token from `~/.config/gh/hosts.yml`.
- **Pool fidelity is law:** question text, choices, and answer letters are quoted only from `canon/pool-extra.*`, byte-exact. Never paraphrase a question; never repair a published quirk; **never retype pool text by hand** — quotes are pulled from the canonical files with script assistance (grep/awk/python extraction) and pasted mechanically. The four deleted questions (E9E10, E2A13, E6D07, E4D05 — §Phase 2) are never quoted; they exist only as numbering gaps and in the errata ledger.
- **Pool expiry is prominent:** this pool is valid 2024-07-01 → **2028-06-30**. The README carries the currency notice + swap procedure; the canon's time-sensitive register pins the expiry; the canon design keeps the pool as a single replaceable file pair so the 2028–2032 swap is contained (replace `canon/pool-extra.*`, re-audit, patch drifted quotes script-assisted).
- **Prose original; facts/Part 97/pool free.** No fabricated quotations; anecdotes framed as illustrative scenarios, never attributed to real people. Pool figures are **redrawn as original SVGs** (same content, never copies of the published graphics).
- **Depth law:** the book **assumes Book 3 (General) knowledge — no more, no less**, calibrated **peer-level with an experienced General, exam-aligned**: nothing taught beyond what the pool tests plus one sidebar. Concepts beyond General scope are taught before use; General-scope material gets at most a one-line refresher + pointer to Book 3. Span auditors enforce this per chapter (Task 4.4); **E5/E7/E9 are the textbook-drift risk chapters** — read them hardest.
- **Self-contained output:** inline SVG figures, math pre-rendered to inline SVG, inline CSS; no external refs (`src="http"`, `<link rel="stylesheet">`, `@import` are failures; SVG `xmlns` URIs are fine). Book HTML uses only relative/anchor links; the only absolute links allowed are the three series paths.
- **Environment:** `python3` (not `python`); `matplotlib`, `edge-tts`, `ffmpeg`, `google-chrome` present; no local Docker (CI builds the image).
- **Naming:** title *Your Last Ham License: The Extra Course (2024–2028)* (US spelling); audio ID3 `artist=Kimi K3`, `album=Your Last Ham License`; GHCR image `ghcr.io/atvriders/your-last-ham-license`; audiobook player `localStorage` key **`ylhl-audio`**; series mount path `/extra/`.
- **sys.path gotcha:** every runnable script keeps `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))`.
- **CI gotcha:** copy the General repo's *fixed* workflow (`seq -f "%02g"`, not `seq -w`), then adjust repo/image names and release URLs.
- **Notation law (series consistency):** identical to Books 2–3 — prose uses V and ×, verbatim pool quotes keep the pool's own forms, unit case (kHz, MHz, mA, µV, pF) is load-bearing, λ(m) = 300 / f(MHz) taught as the approximation of c = f·λ. Extra adds complex-number notation; canon §3 pins the conventions (j-operator, $Z = R + jX$ rectangular/polar, ∠ phase, Γ reflection coefficient) before any chapter is written.

## File Structure

```
your-last-ham-license/
├── accuracy-canon.md                 # THE BIBLE: pinned facts, notation, glossary, copyright ledger
├── canon/
│   ├── pool-extra.txt                # the 2024–2028 Extra pool, byte-exact (human-readable)
│   ├── pool-extra.json               # structured: id → {group, subelement, question, choices{A-D}, answer, figure?}
│   ├── source/                       # original NCVEC downloads (docx/pdf + figure graphics) + errata pages
│   └── ingestion-report.md           # double-parse evidence, counts, errata ledger, figure list, quirks
├── AI-CONTEXT.md                     # full machine context dump (Phase 5)
├── README.md                         # overview + formats + stats block + POOL-CURRENCY NOTICE (Phase 5/6)
├── requirements.txt  .gitignore  docker-compose.yml  Dockerfile
├── chapters/
│   ├── ch00.md … ch10.md             # 11 chapters (ch00 capstone welcome + ch01–ch10 ↔ E1–E0)
│   └── specs/ch00.spec.md … ch10.spec.md
├── figures/
│   ├── <id>.svg  +  _gen_*.py        # original SVGs + matplotlib generators (incl. Smith-chart grids)
│   ├── figure-plan.md                # the figure list (Phase 3)
│   └── figures.json                  # id, chapter, number (first-reference order), caption, kind, source, spoken
├── appendices/
│   ├── pool-fragments/               # Appendix A build: one fragment per subelement (E1.md … E0.md)
│   ├── pool.md                       # Appendix A: the full Extra pool verbatim + one-line why (~45k+ words)
│   └── glossary-and-formulas.md      # Appendix B: glossary + Extra formula set
├── tools/                            # copied from the General repo, retargeted
│   ├── narration.py  figreg.py       # as-is (protected-years set unchanged, 1968–1983); speak_math extended (Task 1.4)
│   ├── mathsvg.py                    # copied + probed/EXTENDED for the Extra formula set (Task 1.4)
│   ├── build_book.py                 # retargeted titles/colophon; SERIES_CURRENT="Extra"; all three books live
│   ├── audit_book.py                 # E-IDs + E-sort-key + pool-driven coverage count; same 8 checks
│   ├── make_audiobook.py             # chapters 00–10 only; retargeted ID3/headings
│   ├── make_intro.py                 # new INTRO text (the capstone welcome)
│   └── make_exam.py                  # PARAMETERIZED: 50-question exam, 37 to pass (Task 1.6)
├── docker/audiobook-index.html       # retargeted player (12 tracks; STORE key ylhl-audio; Extra highlighted)
├── series/                           # nginx.conf + index.html: all three books live, Extra current
├── series-docker-compose.yml         # tech + general + extra live (extra drops `future` profile)
├── .github/workflows/build.yml       # copied fixed version, retargeted
├── tests/                            # the 79-test suite, retargeted fixtures (E-IDs, deleted-ID gap, 50-group exam)
│   └── fixtures/                     # ch_sample.md, ch_h4_sample.md, appendix_sample.md, fig_sample.svg, pool_sample.txt/json
└── docs/superpowers/{specs,plans}/…  # spec + this plan
```

---

## PHASE 0 — Scaffold (spec Phase B, part 1)

### Task 0.1: Repo skeleton + scaffold copy
- [x] Create `~/your-last-ham-license/` with dirs: `tools/ tests/ tests/fixtures/ chapters/ chapters/specs/ figures/ canon/ canon/source/ appendices/ appendices/pool-fragments/ docker/ series/ .github/workflows/ build/ audiobook/ docs/superpowers/specs/ docs/superpowers/plans/` (last two already exist with spec+plan).
- [x] Copy from the **General repo** `/home/kasm-user/your-next-ham-license/` (verbatim, then retarget in Phase 1): `tools/*.py` (incl. `__init__.py`), `tests/` (all 7 test files + fixtures), `pyproject.toml`, `requirements.txt`, `.gitignore`, `docker/audiobook-index.html`, `Dockerfile`, `docker-compose.yml`, `series/`, `series-docker-compose.yml`, `.github/workflows/build.yml`.
- [x] **Do NOT copy:** `chapters/`, `figures/*.svg`, `figures/figures.json`, `accuracy-canon.md`, `canon/`, `AI-CONTEXT.md`, `README.md`, `audiobook/`, `build/`, `appendices/`, `.git/`, `.gitea/` (dead path), `docs/`.
- [x] `git init -b master` (no commits until the end).
- [x] **Verify:** tree matches File Structure; `python3 -m pytest` collects (failures expected until retarget — that's Phase 1).

---

## PHASE 1 — Tooling retarget + extensions (spec Phase B, part 2; TDD)

### Task 1.1: Copy-through modules
- [x] `narration.py`, `figreg.py`: copy unchanged (book-agnostic; protected-years set already 1968–1983). Their tests should pass as-is. (`narration.py`'s `speak_math` may gain tokens in Task 1.4 — copy as-is first, extend with tests.)
- [x] **Verify:** `pytest tests/test_narration.py tests/test_figreg.py` green.

### Task 1.2: `build_book.py` retarget
- [x] Title/colophon/heading constants to this book; chapter glob `ch*.md` (11 chapters); include `appendices/pool.md` + `appendices/glossary-and-formulas.md` as final TOC sections (after ch10), without chapter numbers in headings.
- [x] Series constants: `SERIES_CURRENT = "Extra"`; `SERIES_BOOKS = [("Technician","/tech/",True), ("General","/general/",True), ("Extra","/extra/",True)]` — **all three live, Extra highlighted** (the flag is inert until push; the book is live the moment it ships). Keep `/tech/`, `/general/`, `/extra/` as the only allowed absolute links (relative-links test unchanged).
- [x] Keep: repo-root sys.path bootstrap; self-contained HTML; markdown pipe-table support (Appendix B glossary renders as a real table); h4 support (`####` group lines in Appendix A render as anchored `<h4>`s, never in TOC); PDF probe order `chromium/chromium-browser/google-chrome/google-chrome-stable` → weasyprint → skip.
- [x] Update `tests/test_build_book.py` + fixtures to this book's skeleton (same format laws as Book 3: opener, `### Exam Focus`, `### Key Takeaways`, `**FACT:**`).
- [x] **Verify:** `pytest tests/test_build_book.py` green; fixture builds HTML+TXT; PDF builds via google-chrome.

### Task 1.3: `audit_book.py` retarget (same 8 checks, E-shaped)
- [x] Format-law checks stay the Book 3 skeleton unchanged: `## <N>. <Title>` first line; opener paragraph; ≥1 `> **Worked example:**` in ch01–ch10; `### Exam Focus` in ch01–ch10; `### Key Takeaways`; 3–5 `**FACT:**` lines matching `accuracy-canon.md` verbatim; banned phrases unchanged ("little did they know", "in that moment", "a testament to"); **only ch00 is exempt** from Exam Focus / worked-example (ch10 owns subelement E0 and is a full teaching chapter).
- [x] Check #8 retarget: pool-quote regex `> **E#X##** <text>` + `**Answer: L**`; E-ID regex **`E\d[A-F]\d\d`**; `pool_sort_key` orders subelements **E1…E9 then E0** (subelement 0 sorts as 10), group alphabetical A→last, ascending number; coverage = **all ids in `canon/pool-extra.json` exactly once, in canonical pool order** (count derived from the JSON, not hardcoded — the ingestion fixes the number); answer letters verified against the pool key; skips gracefully with a printed note when the pool JSON is absent.
- [x] **Ingestion-driven adjustment:** if the actual group-letter range exceeds F (expected — E7/E9 historically reach **H**), widen the ID-regex letter class to the observed range (expected `E\d[A-H]\d\d`) and update fixtures to match. The group list pinned at Task 2.1 is authoritative.
- [x] Update fixtures: `tests/fixtures/pool_sample.txt/json` with E-style IDs **including a deleted-ID gap** (e.g. E1A03, E1A05 with no E1A04) so the coverage check tolerates non-contiguous numbering; keep the four #8 fixture tests (correct quote passes; one-word-off fails; wrong letter fails; missing pool → skip).
- [x] **Verify:** `pytest tests/test_audit_book.py` green; `python3 tools/audit_book.py` exits 0 on the empty scaffold (check #8 skipping gracefully).

### Task 1.4: `mathsvg.py` + `speak_math` capability check + extension (TDD)
- [x] The General renderer already covers subscripts ($X_L$), $\pi$, $\sqrt{}$, and fractions; the Extra course adds heavier math. Probe the copied `mathsvg.py` subset AND `narration.py`'s `speak_math` tokens against the Appendix B formula list: complex impedance ($Z = R + jX$, $|Z| = \sqrt{R^2 + X^2}$, phase angle), Q, time constants ($\tau = RC$, $\tau = L/R$), resonance, SWR/reflection ($\Gamma$, $\rho$, $\mathrm{SWR} = (1+|\Gamma|)/(1-|\Gamma|)$), transmission-line transformations, MPE forms, link budgets ($\omega$, dB chains).
- [x] Extend both with tests first (`tests/test_mathsvg.py`, `tests/test_narration.py`): one render test + one spoken-form test per formula above; cover whatever the probe shows missing (expected: $j$, $\Gamma$, $\tau$, $\omega$, $\phi$, $\angle$, magnitude bars, Greek extras). Every printed `$…$` span must render to SVG at build time (audit check #4 is the backstop) **and** speak sanely in the audiobook.
- [x] Keep the writer-facing law unchanged: **at most one `$…$` span per paragraph**, no literal `$` inside a math paragraph (write "35 dollars" in prose).
- [x] **Verify:** `pytest tests/test_mathsvg.py tests/test_narration.py` green incl. the new formula tests.

### Task 1.5: `make_audiobook.py` + `make_intro.py` retarget
- [x] Chapter range 00–10 (11 chapters); `spoken_heading()` for `## <N>. <Title>`; ID3 `album=Your Last Ham License`, `artist=Kimi K3`; exclude `appendices/` from narration (Appendix A is print-only — series decision); keep sys.path bootstrap, chunking/retries, ffmpeg stitch.
- [x] New INTRO text (~1 min spoken): the capstone welcome — for experienced Generals, the last license class, what Extra opens (the Extra-only HF segments, full privileges), how the series fits together; keep `--dry`.
- [x] **Verify:** `pytest tests/test_audiobook_prepare.py` green; `python3 tools/make_intro.py --dry` prints sane text.

### Task 1.6: `make_exam.py` retarget + parameterize to the Extra exam (TDD)
- [x] The Element 4 exam is **50 questions, one drawn from each pool group, 37 correct to pass** (47 CFR §97.503 — the researcher pins the exact paragraph in Task 2.2) — Technician/General were 35/26. Parameterize the exam structure instead of hardcoding: default `--pool canon/pool-extra.json`; E-ID regex + `pool_sort_key` as retargeted in Task 1.3 (same ingestion-driven letter-class rule); exam size = **one uniform-random draw per group, driven by the JSON's group set** (~50 groups → a valid 50-question exam); pass-threshold constant **37** surfaced in the rendered exam header and key text.
- [x] Keep: `--seed` reproducibility; `build/practice-exam.md` (questions + choices A–D, **never the answers**) and `build/practice-exam-key.md` (letters + subelement tally); group model **tolerates the deleted-ID gaps** (one draw per group from whatever ids exist — e.g. E4D has 13, not 14).
- [x] **Verify:** `pytest tests/test_make_exam.py` green — update fixtures to a 50-group E-shaped pool sample so the tests prove: count = one per group (50 on the full fixture), seed reproducibility, no answers in the exam sheet, key correctness + subelement tally, 37-to-pass text.

### Task 1.7: Docker + CI + player retarget
- [x] `Dockerfile`: serve this book's build artifacts; `docker-compose.yml`: image `ghcr.io/atvriders/your-last-ham-license:latest`.
- [x] `docker/audiobook-index.html`: title + 12 track labels (intro + ch00–ch10); **`localStorage` key `ylhl-audio`** (voice/track/position/auto-next); keep resume, visualizer, voice switcher (8 voices), auto-play-next toggle, and the series bar — **Extra highlighted, all three books live**.
- [x] `.github/workflows/build.yml`: copy the General repo's fixed version; repo/image names → this book; audio-fetch loop stays `seq -f "%02g" 0 10` (11 chapters, same count as Books 2–3); release `v1.0` on `Atvriders/your-last-ham-license`.
- [x] **Verify:** `python3 -m pytest` all green; `python3 tools/build_book.py --html --txt --pdf --out build/` succeeds on fixtures.

### Task 1.8: Series-site machinery retarget (series completion)
- [x] `series/nginx.conf`: `/` → landing page; `/tech/` → tech container (active); `/general/` → general container (active); **`/extra/` block uncommented and active — this book ships live and completes the site.**
- [x] `series/index.html`: three cards — Technician **live**, General **live**, Extra **live + current highlight** (no "coming soon" labels remain).
- [x] `series-docker-compose.yml`: tech + general + extra services live (**extra drops the `future` profile**); proxy still the only published port (:8080).
- [x] **Verify:** YAML parses (validate with python — no local Docker); rebuilt fixture HTML shows the bar with Extra highlighted and all three books linked; player page shows bar + toggle (code review or rendered screenshot).

---

## PHASE 2 — Canon workflow (spec Phase C1; content gate 1)

### Task 2.1: Obtain + ingest the pool (serial, first)
- [x] Download the **2024–2028 Amateur Extra pool (Element 4), final document with all errata**, from the top of `https://ncvec.org/index.php/2024-2028-extra-class-question-pool-release` — **verified page** (checked 2026-07-30; the current document at the top is the **4th-errata release of 2026-02-04**, Word **and** PDF). Also grab the **standalone pool-figure graphics** if posted (the 1st errata states figures were updated across "PDF, JPG, and Word" — the JPGs are the side-by-side redraw reference). Cross-check against the ARRL mirror at `https://www.arrl.org/question-pools`. Save originals under `canon/source/` and record sha256s.
- [x] Convert to `canon/pool-extra.txt` (byte-exact human-readable: ID lines `E1A01 (B) [97.301]`, `~~` separators, published headings) and structured `canon/pool-extra.json` (`{id: {group, subelement, question, choices{A–D}, answer, figure}}`). **Double-parse discipline, same as Books 2–3:** parse the `.docx` (authoritative; python3 `zipfile` + `ElementTree`, no third-party packages) and independently re-parse the `.pdf` (`pdftotext -layout`); reconcile every question, choice, answer letter, Part 97 ref, and heading; write `canon/ingestion-report.md` with the full evidence.
- [x] **Errata ledger (pin in canon §1 — verified 2026-07-30 against the NCVEC release page):** released into the public domain by the NCVEC QPC (statement on the release page, capture it into `canon/source/`); effective for exams 2024-07-01. Four errata — **Errata 1 (2024-01-31):** 5 questions modified (E1D07, E1F03, E4D12, E4D13, E6A06), **E9E10 withdrawn** (E9E not renumbered, 10 questions remain), **diagram E9-3 (the Smith chart) modified** — rotated 90° to the conventional horizontal orientation with infinity on the right; citation-only fixes E1E10 → `[97.509(m)]`, E1E11 → `[97.509(i)]`. **2nd errata (2024-11-08):** **E2A13 withdrawn** (not renumbered; the release-page note misprints the affected group as "G8C" — a published quirk of the *page*, cataloged in the ingestion report, never propagated). **3rd errata (2025-09-24):** **E6D07 withdrawn** (more than one correct answer). **4th errata (2026-02-04):** **E4D05 withdrawn** (E4D not renumbered, 13 questions remain). The book always uses the fully-errata'd form. **Deleted IDs were never renumbered:** E9E10, E2A13, E6D07, E4D05.
- [x] **Verify (hard gate):** expected **~599 active questions** (603 at release − 4 withdrawn; the parse produces the authoritative number — record it in the canon and update any derived constants); 10 subelements E1–E9 + E0; **~50 groups total** (record the full group list + per-subelement counts in the canon; the group list fixes the Task 1.3/1.6 regex letter class and the exam size); exam = **50 Q, one per group, 37 to pass**; every active question has exactly 4 choices A–D and one keyed answer; zero parse drops — IDs contiguous within each group **except the four pinned deletions**; **every figure-referencing question identified and flagged with its figure id** (the Extra pool historically ships **several figures** — schematics/diagrams incl. the E9-3 Smith chart confirmed by the 1st errata; the exact figure list and referencing question ids come from the document, not memory); published quirks (typo'd citations, Unicode punctuation, spacing oddities) preserved byte-exactly, cataloged in the ingestion report, never repaired.
- [x] **Confirm at ingestion:** any errata posted **after** 2026-02-04 (the 4th) — check the release page top and the ARRL question-pool news; if a 5th errata exists, fold it in and extend the ledger before any writing starts.

### Task 2.2: Parallel researchers (fan-out)
- [ ] R1: Part 97 pinned facts for Extra — §97.301/§97.305 **Extra-only band segments exact**, §97.307 emission standards, §97.311/§97.313, special operations (automatic control, remote bases, auxiliary stations), CEPT/international operation, with eCFR issue date + pull date recorded. Re-verify Book 3's standing rulings that still apply (60 m current text under 91 FR 1430; the 2.8 kHz HF bandwidth standard) wherever an Extra question touches them.
- [ ] R2: Exam & upgrade logistics — exam structure (**50 Q, 37 pass, one per group**; pin the exact §97.503 paragraph for Element 4), CSCE/upgrade credit (General → Extra via Element 4), the **§97.9(b) upgrade immediacy + /AE indicator** with the same both-conditions wording law as Book 3's /AG ruling, finding sessions, fees (re-verify against Book 3's register: FCC $35, upgrades exempt; ARRL VEC $15/$5; Form 605 2022 edition; Laurel VEC larc-vec.org), pool validity window **2024-07-01 → 2028-06-30** + the four-errata revision record.
- [ ] R3: Per-subelement teaching notes E1–E5 (what an experienced **General** must learn to answer every question in the subelement; common confusions; calibrated to "peer-level with an experienced General, exam-aligned" — flag anything that tempts textbook drift).
- [ ] R4: Per-subelement teaching notes E6–E0 (same).
- [ ] R5: Advanced operating color — satellite orbits/keps, EME path loss basics, weak-signal VHF+, auroral/meteor-scatter/TE operating, contest/DX at depth, digital-mode culture at depth (FT8 internals, spread spectrum).

### Task 2.3: Assembler
- [ ] One agent writes `accuracy-canon.md`: §1 pool record (files, sha256s, provenance, errata ledger, deleted-ID gap list, **per-figure redraw specs** for every pool figure — the binding component-by-component contracts, same discipline as Book 3's §1.4); §2 pinned FACTs with sources; §3 notation & units (carried from Books 2–3 essentially unchanged, **plus the Extra additions**: j-operator, rectangular/polar complex impedance, ∠ phase, Γ/ρ, τ, ω — pinned before any chapter is written); §4 glossary (shared entries stay byte-consistent with Book 3, which kept Book 2's verbatim; new Extra terms in the same style); §5 subelement→chapter map (**finalizes the chapter split from the ingested group sizes** — default: one subelement per chapter, E1→ch01 … E0→ch10; adjust only if a subelement's size demands it, before any chapter spec is written); §6 copyright ledger (carried over; pool PD, Part 97 PD, pool figures redrawn as original SVGs, Handbook protected-years rule); §7 resolved uncertainties — **wording-law approach: every research flag closed to a sourced value or a deliberately careful wording, zero open markers**; time-sensitive register with **pool expiry 2028-06-30 prominent** and fees re-verified at build time.
- [ ] **Verify (gate):** 0 `UNVERIFIED` markers; `python3 tools/audit_book.py` canon checks pass (check #8 now live against the real pool); spot-read the canon.

---

## PHASE 3 — Figures workflow (spec Phase C2; content gate 2)

### Task 3.1: Figure list
- [x] Orchestrator writes `figures/figure-plan.md`: **~30–40 figures** across ch00–ch10 — **Extra-only band charts** (per-band, Extra vs General segments), satellite/EME geometry, **auroral / transequatorial (TE) / meteor-scatter propagation** diagrams, sporadic-E & ducting at depth, **measurement & dynamic-range concepts** (accuracy/resolution, IMD, IP3, blocking), **complex-impedance & phasor diagrams**, Q & resonance curves (matplotlib), semiconductor/digital-logic figures, active-filter/PLL/**DSP-SDR block diagrams** (sampling, aliasing, I/Q), modulation spectra at depth (QAM/OFDM concepts), **transmission-line & stub concepts** (standing waves, λ/4 and λ/2 transformations, Smith-chart matching walk), antenna modeling/pattern concepts, **MPE-math geometry** — **plus every pool figure redrawn as an original SVG** (same components/labels as each NCVEC graphic; canon §1 carries the binding per-figure redraw specs; registered `kind:"original"` with the note "redrawn from NCVEC pool figure …"). Working distribution (finalized against canon §5): ch00:2, ch01:3, ch02:3, ch03:4, ch04:4, ch05:4, ch06:3, ch07:4, ch08:3, ch09:5, ch10:2, **plus the pool redraws** (several expected; the ingestion list is authoritative).
- [x] **Numbering law:** figure display numbers follow **first-reference order within each chapter** (pinned in `figures.json` at assembly, Task 3.4) — never by authoring order, so late insertions don't scramble the book.

### Task 3.2: Parallel figure agents
- [x] One agent per chapter authors that chapter's figures: hand-authored themeable SVG with `currentColor` for schematics/diagrams; matplotlib→SVG for plots (paired `_gen_<id>.py` scripts, post-process black→`currentColor`); each with caption + one-line **spoken** description (audio degradation).

### Task 3.3: The Smith-chart family (dedicated agent — the hardest figures in the series)
- [x] One dedicated figure agent builds the Smith-chart figure set for ch09: geometrically correct **constant-resistance and constant-reactance circle grids generated with matplotlib** (normalized Γ-plane math — constant-R circles center $(r/(r+1), 0)$ radius $1/(r+1)$; constant-X circles center $(1, 1/x)$ radius $1/|x|$, clipped to the unit circle), post-processed black→`currentColor`, paired `_gen_*.py` scripts. The family: the full chart grid, a normalized-impedance reading example, a constant-SWR circle, and a matching-stub solution walk.
- [x] **Side-by-side review against the pool figures:** the redrawn **E9-3 Smith chart** (in its 1st-errata form — horizontal orientation, infinity on the right) and every other pool-figure redraw are compared side-by-side with the official NCVEC graphics for content equality (same components, same labels, same callouts — never copies). Findings recorded in `figures/figure-plan.md` or the ingestion report's figure section.

### Task 3.4: Assembler + verify (gate)
- [x] Assembler writes `figures/figures.json` (id, chapter, number in first-reference order, caption, kind, source, spoken).
- [x] **Verify:** `figreg.validate()` → empty; all SVGs parse (XML); render ≥6 to PNG and **look at them** — including the full Smith-chart family and every pool redraw against its official NCVEC original.

---

## PHASE 4 — Chapters workflow (spec Phase C3; content gate 3)

### Task 4.1: Chapter specs
- [ ] Orchestrator writes `chapters/specs/ch00.spec.md … ch10.spec.md`: per chapter — subelement(s) + pool groups owned (from canon §5), **exact first-line heading string in title case** (`## <N>. <Title>`, taken from the spec §4 table as finalized at 2.3 — writers may not improvise headings; this is what lets 11 parallel writers produce one TOC), required figure IDs (from Phase 3), teaching beats, Exam Focus question selection (5–10 per chapter), worked-example topic (**a real calculation with pool-relevant numbers** — complex impedance, Smith-chart values, MPE math, link budgets — arithmetic-only is a defect at this level), and for ch00 the "Your upgrade checklist" adaptation (no pool, no Exam Focus).
- [ ] **Word targets (working; finalized against ingested subelement sizes at canon §5):** ch00 ~2.5–3k; ch01 (E1) ~5–6k; ch02 (E2) ~4.5–5.5k; ch03 (E3) ~4–5k; ch04 (E4) ~5–6k; ch05 (E5) ~5–6k; ch06 (E6) ~5.5–6.5k; ch07 (E7) ~6–7.5k; ch08 (E8) ~4.5–5.5k; ch09 (E9) ~6–7.5k; ch10 (E0) ~3–4k — **~50–65k words total across the 11 chapters.**

### Task 4.2: Parallel chapter writers (11 agents)
- [ ] Each agent: reads canon + its pool slice + its spec + figure registry; writes `chapters/chNN.md` obeying the format laws (identical skeleton to Book 3): exact heading; opener paragraph (a concrete capstone scenario + "in this chapter you'll learn …"); `###` teaching sections; `{{fig:id}}` on its own line; ≥1 `> **Worked example:**`; optional `> **The math, if you want it:**` sidebars for derivations; `### Exam Focus` (coverage line + 5–10 verbatim questions + answer + one-line why); `### Key Takeaways`; 3–5 `**FACT:**` lines copied **byte-exact** from `accuracy-canon.md` as standalone plain paragraphs (never inside blockquotes).
- [ ] **Build-dialect laws (carry the hard-won lessons — violations break the build):** consecutive non-blank lines join into one paragraph, so bullets are **blank-line-separated**; a blockquote is consecutive `>` lines joined with spaces (six-line quote blocks; no stray adjacent `>` lines); **at most one `$…$` span per paragraph**, no literal `$` in a math paragraph; blockquote classes by prefix (`**Worked example:**`, `**The math, if you want it:**`); pipe tables need the `|---|` separator line; `***` is a section rule; `####` renders as an anchored h4 and never enters the TOC; emphasis `**bold**` / `*italic*` only.
- [ ] **Pool-quote law:** every Exam Focus quote is extracted **script-assisted** from `canon/pool-extra.*` (grep/awk/python — never hand-typed); correct answer letter from the pool key; why lines are one line, plain language, ending **"— taught in chapter N."** where cross-referencing, and never paraphrase the question. The four deleted questions are never quoted.
- [ ] Depth: worked examples are real calculations (complex impedance, Q, SWR/reflection, Smith-chart values, MPE math, link budgets); where a formula appears it is used at least once with pool-relevant numbers; anything beyond General scope is taught before use; General material gets a one-line refresher + pointer to Book 3 at most; **peer-level with an experienced General, exam-aligned** — nothing beyond what the pool tests plus one sidebar.

### Task 4.3: Appendices (parallel)
- [x] **Appendix A, fragment-per-subelement (10 agents, E1–E0) — the LARGEST appendix yet (~45k+ words verbatim):** each agent emits one fragment file (`appendices/pool-fragments/E1.md` … `E0.md`) with its subelement's section — every active question exactly once, in canonical order (group A→last, ascending number, **skipping the four pinned deletions**), each entry one six-line blockquote (`> **E1A01** <verbatim question>` / `> A. …` … / `> **Answer: B** — <one-line why, naming the teaching chapter: "… — taught in chapter 1.">`), followed by the **Published ID line on a separate plain-text line after the blockquote, in backticks** (never inside the quote — the audit would read it as question text); redrawn pool figures embedded on the line before their first referencing quote and named thereafter. All quotes script-extracted, never retyped.
- [x] **Assemble + byte-exact gate:** the assembler concatenates fragments in canonical order (E1…E9 then E0), normalizes each `###` subelement heading to the **published title + counts** (optional `####` group lines render as h4), then runs the **fragment byte-exact gate**: re-extract every question from the assembled `appendices/pool.md` and diff mechanically against `canon/pool-extra.json` (audit check #8 does this book-wide; run it per-fragment at handoff too — with ~600 questions the mechanical gate, not eyeballing, is what makes silent drift impossible). Print-only — never narrated.
- [x] **Appendix B (one agent):** glossary as a two-column pipe table (canon §4 definitions verbatim — renders as a real HTML table via the builder's table support) + the **Extra formula set** — complex impedance (rectangular/polar, magnitude, phase), Q, time constants, resonance in depth, SWR/reflection coefficient, transmission-line transformations (λ/4, λ/2, stubs), link budgets, MPE forms, sampling/Nyquist — plus the series carry-overs (Ohm's law, power, reactance, dB, wavelength shortcut, prefix ladder) — each with a plain statement and one worked micro-example using the pool's own numbers, plus the notation-and-units subsection (V/× prose convention, the pinned complex-number conventions, unit case, c, f = 1/T, the hobby's customary units).

### Task 4.4: Span auditors (parallel, 3–4 agents)
- [ ] Each audits a span of chapters: every fact/value/frequency/privilege against canon; every question quote + letter against the pool (mechanically assisted by check #8); format laws; build-dialect laws; fix surgically in place.
- [ ] **Depth-calibration check (explicit, per chapter):** grade **"peer-level with an experienced General, exam-aligned."** Flag any paragraph that re-teaches General material at length, any that uses post-General theory without teaching it first, and any textbook drift beyond what the pool tests plus one sidebar. **E5/E7/E9 are the risk chapters — read them hardest.**
- [ ] Tone: competent colleague-to-colleague, dense but clear; every formula derived just enough to be believed, then drilled with the pool's own numbers; banned-phrase grep clean.

### Task 4.5: Verify (gate)
- [ ] `python3 tools/audit_book.py` — all 8 checks green (incl. #8: full active-pool coverage in Appendix A exactly once in canonical order, all quotes verbatim, all letters correct).
- [ ] Full build HTML/PDF/TXT; spot-read 1 full chapter + 20 random Appendix A entries against the official NCVEC document; banned-phrase grep clean.

---

## PHASE 5 — Front matter (spec Phase D)

- [ ] `AI-CONTEXT.md`: full machine dump in Book 3's shape (canon summary, outline, pool facts + four-errata revision record + deleted-ID list, figure inventory incl. pool redraws, format laws, build-dialect laws, figure pipeline, tooling, series machinery, time-sensitive register with the **2028-06-30 expiry**, production history; no credentials).
- [ ] `README.md`: overview, formats table, Docker/audiobook instructions, `make_exam.py` usage (50-question Extra exams), **pool-currency notice (prominent): valid 2024-07-01 → 2028-06-30**, plus the swap procedure (replace `canon/pool-extra.*` → re-audit — check #8 flags every drifted quote and coverage gap → patch quotes script-assisted → update FACT lines → rebuild; note that only Exam Focus picks and Appendix A change with the pool — the teaching content is durable), "How it was made" stats block (clearly-labeled token estimate + wall-time; finalized at push).

---

## PHASE 6 — Verify & ship (spec Phase E)

- [ ] Clean rebuild from scratch; `pytest` green; `audit_book.py` exit 0; human-style spot-read.
- [ ] **Ship gate (human confirms before outward actions).**
- [ ] One commit (trailer `Co-Authored-By: Kimi K3 <noreply@moonshot.cn>`).
- [ ] Create GitHub repo via REST API (`POST /user/repos`, `private:false`; token from `~/.config/gh/hosts.yml`; never `gh`); push `master`.
- [ ] Generate audiobook: `make_audiobook.py --all` (8 voices × 11 chapters, chapters only) + `make_intro.py`.
- [ ] Create release **v1.0**; upload audio assets (audio ships on the release, not in git).
- [ ] `workflow_dispatch` the CI; confirm image builds and `ghcr.io/atvriders/your-last-ham-license:latest` is anonymously pullable (`docker pull` unauthenticated or manifest check via curl).
- [ ] **Series completion — Extra goes live:** this repo already ships with Extra highlighted + `/extra/` active + all three books live (Task 1.8); verify the series bar and landing render all three live with Extra current once the image is public. **This completes the three-book series site.**
- [ ] **Two cross-repo touches — each its own tiny commit, each human-approved at that moment, never assumed, never bundled:** (1) in `/home/kasm-user/your-first-ham-license/` (Technician repo), flip Extra's `SERIES_BOOKS` flag to `True` in `tools/build_book.py` (and the player's bar if it carries its own copy), update `series/index.html` so the Extra card shows live, rebuild, run pytest + audit, and commit that change **alone** (message e.g. "Series: Extra is live"); push after its own verification. (2) Same in `/home/kasm-user/your-next-ham-license/` (General repo). These are the only approved exceptions to the one-commit rule and each requires explicit human sign-off at the time.
- [ ] Write final token/time stats into README (amend or second tiny README-only commit if the human allows; otherwise include in the one commit by generating audio before committing).

---

## Tracking & cost notes

- Book 3 cost reference: ~45 subagent launches; this book reuses its toolchain nearly unchanged but adds: a ~40%-larger pool (~600 vs 423) with the largest Appendix A yet (~45k+ words), several pool-figure redraws including the dedicated Smith-chart family, the `make_exam.py` 50/37 parameterization, and the mathsvg/speak_math extensions — budget ~55–70 agents, ~7–9M tokens, ~2.5–3 h wall-time.
- Mark plan checkboxes as tasks complete; keep the human informed at each content gate (2.3, 3.4, 4.5) and the ship gate.
