import json
import pathlib

import pytest

from tools.audit_book import (
    check_appendix_pool_coverage,
    check_banned_phrases,
    check_figure_integrity,
    check_format_laws,
    check_pool_quotes,
    extract_pool_quotes,
    main,
    pool_sort_key,
)

POOL_PATH = "tests/fixtures/pool_sample.json"
POOL = json.loads(pathlib.Path(POOL_PATH).read_text(encoding="utf-8"))

CH_SAMPLE = pathlib.Path("tests/fixtures/ch_sample.md").read_text(encoding="utf-8")


# --- Book 1 carry-overs ---------------------------------------------------

def test_banned_phrases_flagged():
    errs = check_banned_phrases("…and little did they know it would grow.")
    assert errs and "little did they know" in errs[0]

def test_banned_phrases_clean():
    assert check_banned_phrases("The lamp is lit and the exam begins.") == []

def test_figure_integrity_missing():
    errs = check_figure_integrity(["{{fig:ghost}}"], registry={})
    assert any("ghost" in e for e in errs)

def test_figure_integrity_ok():
    reg = {"tank": {"id":"tank","chapter":1,"number":"1.1","caption":"c","kind":"original","source":"authored","file":"figures/tank.svg"}}
    assert check_figure_integrity(["see {{fig:tank}}"], registry=reg) == []


# --- Format laws (spec §5 skeleton) ----------------------------------------

def test_format_laws_accept_teaching_chapter_fixture():
    assert check_format_laws("ch01", CH_SAMPLE) == []

def test_format_laws_require_exam_focus_in_teaching_chapters():
    text = CH_SAMPLE.replace("### Exam Focus", "### Focus")
    assert any("Exam Focus" in e for e in check_format_laws("ch01", text))

def test_format_laws_forbid_exam_focus_only_in_ch00():
    # only the ch00 welcome is exempt; ch10 owns subelement E0 in this book
    assert any("Exam Focus" in e for e in check_format_laws("ch00", CH_SAMPLE))

def test_format_laws_treat_ch10_as_teaching_chapter():
    text = CH_SAMPLE.replace("## 1.", "## 10.")
    assert check_format_laws("ch10", text) == []
    no_focus = text.replace("### Exam Focus", "### Focus")
    assert any("Exam Focus" in e for e in check_format_laws("ch10", no_focus))
    no_example = text.replace("> **Worked example:**", "> **Example:**")
    assert any("worked example" in e.lower() for e in check_format_laws("ch10", no_example))

def test_format_laws_require_worked_example_in_teaching_chapters():
    text = CH_SAMPLE.replace("> **Worked example:**", "> **Example:**")
    assert any("worked example" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_require_key_takeaways():
    text = CH_SAMPLE.replace("### Key Takeaways", "### Takeaways")
    assert any("Key Takeaways" in e for e in check_format_laws("ch01", text))

def test_format_laws_heading_number_must_match_file():
    assert any("heading" in e.lower() for e in check_format_laws("ch03", CH_SAMPLE))

def test_format_laws_require_opener_paragraph():
    text = CH_SAMPLE.replace(
        "Your General ticket taught you reactance as a single number; at Extra "
        "depth impedance becomes a complex quantity with a magnitude and a "
        "phase angle. In this chapter you'll learn how the rectangular and "
        "polar forms describe the same impedance, and how little extra math "
        "you actually need.\n\n",
        "",
    )
    assert any("opener" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_fact_line_count():
    text = CH_SAMPLE.replace("**FACT:** Impedance combines resistance and reactance as the square root of the sum of their squares.\n", "")
    assert any("FACT" in e for e in check_format_laws("ch01", text))

def test_format_laws_exempt_preface():
    # the preface is front matter, not a teaching chapter: it is exempt from
    # ALL chapter format laws — no numbered heading, no opener rule, no
    # Exam Focus / worked-example / Key Takeaways / FACT requirements
    preface = ("## Preface — Why & How This Book Was Made\n\n"
               "Plain front-matter prose, none of the chapter apparatus.\n")
    assert check_format_laws("preface", preface) == []


# --- Check #8: pool fidelity -----------------------------------------------

def _quote(qid, question, letter, choices):
    lines = [f"> **{qid}** {question}"]
    lines += [f"> {k}. {v}" for k, v in choices.items()]
    lines.append(f"> **Answer: {letter}** — because the fixture says so.")
    return "\n".join(lines)


def test_pool_quote_correct_passes():
    entry = POOL["E5B02"]
    text = _quote("E5B02", entry["question"], entry["answer"], entry["choices"])
    assert check_pool_quotes(extract_pool_quotes(text), POOL) == []

def test_pool_quote_one_word_off_fails():
    entry = POOL["E5B02"]
    bad = entry["question"].replace("30 ohms", "35 ohms")
    text = _quote("E5B02", bad, entry["answer"], entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "E5B02" in errs[0]

def test_pool_quote_wrong_answer_letter_fails():
    entry = POOL["E5B02"]
    wrong = "A" if entry["answer"] != "A" else "B"
    text = _quote("E5B02", entry["question"], wrong, entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "answer" in errs[0].lower()

def test_pool_quote_unknown_id_fails():
    # E9H01 matches the (wider) E-shaped id regex but is not in the fixture pool
    text = _quote("E9H01", "Not a real pool question?", "A", POOL["E5B02"]["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "E9H01" in errs[0]

def _appendix_text(ids):
    return "\n\n".join(
        _quote(qid, POOL[qid]["question"], POOL[qid]["answer"], POOL[qid]["choices"])
        for qid in ids
    )

def test_appendix_coverage_complete_and_in_order_passes():
    # note the deleted-ID gap in group E1A: 01, 03 (no 02) — coverage must
    # tolerate non-contiguous numbering; the count is JSON-driven (100 here)
    ordered = sorted(POOL, key=pool_sort_key)
    assert len(ordered) == 100
    assert check_appendix_pool_coverage(_appendix_text(ordered), POOL) == []

def test_appendix_coverage_missing_id_fails():
    ids = [qid for qid in POOL if qid != "E2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("E2A02" in e and "missing" in e for e in errs)

def test_appendix_coverage_duplicate_id_fails():
    ids = sorted(POOL) + ["E2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("E2A02" in e and "once" in e for e in errs)

def test_appendix_coverage_out_of_order_fails():
    ids = sorted(POOL)
    ids[0], ids[1] = ids[1], ids[0]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("order" in e for e in errs)

def test_pool_sort_key_orders_e0_after_e9():
    assert pool_sort_key("E1A01") < pool_sort_key("E9H12")
    assert pool_sort_key("E9H12") < pool_sort_key("E0A01")
    assert pool_sort_key("E0E10") > pool_sort_key("E0A01")


# --- Check #8 on the empty scaffold: skip, not fail -------------------------

def test_audit_main_skips_pool_check_on_empty_scaffold(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main() == 0
    out = capsys.readouterr().out.lower()
    assert "pool" in out and "skip" in out
