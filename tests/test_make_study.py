import json
import pathlib
import re

import pytest

from tools import make_study

FIX = pathlib.Path("tests/fixtures")
FIXTURE_IDS = {"E1A01", "E1A02", "E1B01", "E2A01", "E5A01", "E9G06"}

REAL_POOL = pathlib.Path("canon/pool-extra.json")
REAL_APPENDIX = pathlib.Path("appendices/pool.md")
REAL_POOL_TXT = pathlib.Path("canon/pool-extra.txt")
REAL_FIGURES = pathlib.Path("figures")


def load_fixture_inputs():
    pool = make_study.load_pool(FIX / "study_pool.json")
    whys = make_study.parse_whys((FIX / "study_appendix.md").read_text(encoding="utf-8"))
    pool_txt = (FIX / "study_pool.txt").read_text(encoding="utf-8")
    return pool, whys, pool_txt


def build_fixture_records():
    pool, whys, pool_txt = load_fixture_inputs()
    return make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def fixture_figures():
    return {"E9-3": '<svg viewBox="0 0 10 10"><title>fixture figure E9-3</title></svg>'}


def assert_self_contained(html):
    """The pages must work under a strict CSP: nothing external, ever."""
    assert 'src="http' not in html and "src='http" not in html
    assert 'href="http' not in html and "href='http" not in html
    assert "<script src" not in html
    assert "<link" not in html
    assert "<img" not in html


def assert_fully_rendered(html):
    """No template tokens survive; the audiobook theme is in place."""
    assert not re.findall(r"__[A-Z_]+__", html)
    assert "--paper:" in html and "--beam:" in html  # lantern/scope CSS variables
    assert 'class="series-bar"' in html


# ---------- parsers ----------


def test_parse_group_headings_reads_only_heading_lines():
    _, _, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    assert headings == {
        "E1A": "Frequency privileges; signal frequency range; stations aboard ships or aircraft",
        "E1B": "Station restrictions and special operations: restrictions on station location; RACES operations",
        "E2A": "Amateur radio in space: amateur satellites; orbital mechanics; frequencies and modes",
        "E5A": "Resonance and Q: characteristics of resonant circuits; series and parallel resonance",
        "E9G": "The Smith chart",
        "E0A": "Safety: RF radiation hazards; hazardous materials; grounding",
    }


def test_parse_subelement_titles():
    _, _, pool_txt = load_fixture_inputs()
    titles = make_study.parse_subelement_titles(pool_txt)
    assert titles == {
        "E1": "COMMISSION RULES",
        "E2": "OPERATING PROCEDURES",
        "E5": "ELECTRICAL PRINCIPLES",
        "E9": "ANTENNAS AND TRANSMISSION LINES",
        # E0's published banner quirk — "SUBELEMENT E0 - SAFETY - [1 exam
        # question - 1 group]" — loses the trailing hyphen and still parses.
        "E0": "SAFETY",
    }


def test_parse_whys_maps_letter_and_text_for_every_entry():
    _, whys, _ = load_fixture_inputs()
    assert set(whys) == FIXTURE_IDS
    letter, why = whys["E5A01"]
    assert letter == "B"
    assert why == "current is measured in amperes — taught in chapter 5."


# ---------- chapter map (accuracy-canon.md §5) ----------


@pytest.mark.parametrize(
    "subelement,group,chapter",
    [
        ("E1", "E1F", 1),
        ("E2", "E2C", 2),
        ("E3", "E3A", 3),
        ("E4", "E4B", 4),
        ("E5", "E5D", 5),
        ("E6", "E6A", 6),
        ("E7", "E7H", 7),   # E7 runs to group H
        ("E8", "E8D", 8),
        ("E9", "E9H", 9),   # E9 runs to group H
        ("E0", "E0A", 10),  # E0 is taught by ch10
    ],
)
def test_chapter_for_matches_canon_map(subelement, group, chapter):
    assert make_study.chapter_for(subelement, group) == chapter


# ---------- record assembly ----------


def test_build_records_assembles_every_field():
    records = build_fixture_records()
    assert [r["id"] for r in records] == ["E1A01", "E1A02", "E1B01", "E2A01", "E5A01", "E9G06"]
    rec = records[0]
    assert rec["group"] == "E1A"
    assert rec["subelement"] == "E1"
    assert rec["question"].startswith("Which operator class")
    assert set(rec["choices"]) == {"A", "B", "C", "D"}
    assert rec["answer"] == "D"
    assert rec["why"] == "the Extra class conveys all available privileges — taught in chapter 1."
    assert rec["groupTheme"].startswith("Frequency privileges")
    assert rec["chapter"] == 1
    assert "figure" not in rec  # figure key only present on figure questions


def test_build_records_marks_only_the_figure_question():
    records = build_fixture_records()
    with_fig = {r["id"]: r["figure"] for r in records if "figure" in r}
    assert with_fig == {"E9G06": "E9-3"}


def test_build_records_fails_on_missing_why():
    pool, whys, pool_txt = load_fixture_inputs()
    del whys["E2A01"]
    with pytest.raises(ValueError, match="E2A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_answer_letter_mismatch():
    pool, whys, pool_txt = load_fixture_inputs()
    whys["E5A01"] = ("C", whys["E5A01"][1])
    with pytest.raises(ValueError, match="E5A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_missing_group_heading():
    pool, whys, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    del headings["E9G"]
    with pytest.raises(ValueError, match="E9G"):
        make_study.build_records(pool, whys, headings)


# ---------- validation ----------


def test_validate_records_accepts_the_fixture_set():
    records = build_fixture_records()
    make_study.validate_records(records, expected_count=6, figure_ids={"E9G06"})


def test_validate_records_rejects_an_unexpected_figure_reference():
    records = build_fixture_records()
    records[0]["figure"] = "E9-3"  # E1A01 is not one of the known figure questions
    with pytest.raises(ValueError, match="E1A01"):
        make_study.validate_records(records, expected_count=6, figure_ids={"E9G06"})


def test_validate_records_rejects_empty_fields():
    records = build_fixture_records()
    records[1]["why"] = ""
    with pytest.raises(ValueError, match="E1A02"):
        make_study.validate_records(records, expected_count=6, figure_ids={"E9G06"})


def test_validate_records_checks_the_count():
    records = build_fixture_records()
    with pytest.raises(ValueError):
        make_study.validate_records(records[:-1], expected_count=6, figure_ids={"E9G06"})


# ---------- the real canon data ----------


def build_real_records():
    pool = make_study.load_pool(REAL_POOL)
    whys = make_study.parse_whys(REAL_APPENDIX.read_text(encoding="utf-8"))
    headings = make_study.parse_group_headings(REAL_POOL_TXT.read_text(encoding="utf-8"))
    return make_study.build_records(pool, whys, headings)


def test_real_pool_assembles_599_valid_records():
    records = build_real_records()
    assert len(records) == 599
    make_study.validate_records(records)  # defaults: 599 records, the 28 known figure ids


def test_real_pool_figure_refs_land_on_exactly_the_28_known_ids():
    records = build_real_records()
    with_fig = {r["id"] for r in records if "figure" in r}
    assert len(with_fig) == 28
    assert with_fig == make_study.FIGURE_QUESTION_IDS


def test_real_pool_every_why_theme_and_chapter_non_empty():
    records = build_real_records()
    for rec in records:
        assert rec["why"].strip(), rec["id"]
        assert rec["groupTheme"].strip(), rec["id"]
        assert rec["chapter"], rec["id"]


def test_real_pool_subelement_summaries_cover_e1_through_e0():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    subs = make_study.subelement_summaries(records, titles)
    assert [s["id"] for s in subs] == ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E0"]
    assert sum(s["count"] for s in subs) == 599
    assert all(s["title"] for s in subs)
    assert subs[0]["count"] == 68  # E1 — Commission Rules
    assert subs[-1] == {"id": "E0", "title": "SAFETY", "count": 12}


def test_load_figures_reads_the_ten_redrawn_pool_svgs():
    figures = make_study.load_figures(REAL_FIGURES)
    assert set(figures) == {
        "E5-1", "E6-1", "E6-2", "E6-3", "E7-1",
        "E7-2", "E7-3", "E9-1", "E9-2", "E9-3",
    }
    for svg in figures.values():
        assert svg.lstrip().startswith("<svg")


# ---------- page rendering ----------


def test_flashcards_page_embeds_every_record_with_hints_and_marks():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    for qid in FIXTURE_IDS:
        assert qid in html
    assert "ylhl-study" in html            # localStorage namespace for review-later marks
    assert "Hint: this is" in html         # hint line template
    assert "review chapter" in html        # chapter pointer in the hint
    assert "fixture figure E9-3" in html   # figure SVG embedded inline
    assert "COMMISSION RULES" in html      # subelement labels for the filter
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_flashcards_card_has_fixed_height_and_internal_scroll():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    # fixed-height card box: flipping must never move the controls below the card
    assert "height: 28rem" in html
    # the rare longer card scrolls inside the card instead of growing it
    assert "overflow-y: auto" in html


def test_practice_page_states_the_50_37_rule_and_drill_mode():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_practice_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    assert "50 questions" in html
    assert "37 to pass" in html
    assert "New exam" in html
    assert "Drill" in html                 # per-subelement drill mode
    for qid in FIXTURE_IDS:
        assert qid in html                 # pool embedded as JSON
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_flashcards_page_contains_every_real_pool_id():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, make_study.load_figures(REAL_FIGURES),
        make_study.subelement_summaries(records, titles))
    assert len(re.findall(r'"id": "E\d[A-H]\d\d"', html)) == 599
    for qid in ("E1A01", "E5C09", "E0A12", "E9G06", "E9G07"):
        assert qid in html
    assert_self_contained(html)


# ---------- CLI ----------


def test_main_writes_both_pages(tmp_path):
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "6", "--figure-ids", "E9G06",
    ])
    assert rc == 0
    flash = (tmp_path / "flashcards.html").read_text(encoding="utf-8")
    practice = (tmp_path / "practice.html").read_text(encoding="utf-8")
    for qid in FIXTURE_IDS:
        assert qid in flash and qid in practice
    assert "50 questions" in practice and "37 to pass" in practice
    assert "ylhl-study" in flash
    assert_self_contained(flash)
    assert_self_contained(practice)
    assert_fully_rendered(flash)
    assert_fully_rendered(practice)


def test_main_refuses_an_invalid_record_set(tmp_path):
    # expecting 7 records from a 6-question fixture must fail validation
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "7", "--figure-ids", "E9G06",
    ])
    assert rc == 1
    assert not (tmp_path / "flashcards.html").exists()
