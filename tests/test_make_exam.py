import json
import pathlib

from tools.make_exam import PASS_SCORE, draw_exam, load_pool, pool_sort_key, render_exam, render_key

POOL_PATH = pathlib.Path("tests/fixtures/pool_sample.json")
POOL = json.loads(POOL_PATH.read_text(encoding="utf-8"))
# 50 groups x 2 questions in the fixture (group E1A carries a deleted-ID
# gap: 01, 03 — no 02), E7 reaches group H (the wider E-shaped letter class)
GROUPS = {entry["group"] for entry in POOL.values()}


def test_load_pool_returns_all_entries():
    pool = load_pool(POOL_PATH)
    assert len(pool) == 100
    entry = pool["E5B02"]
    assert entry["group"] == "E5B"
    assert entry["subelement"] == "E5"
    assert set(entry["choices"]) == {"A", "B", "C", "D"}
    assert entry["answer"] in "ABCD"


def test_fixture_spans_fifty_groups_including_h_letter_groups():
    assert len(GROUPS) == 50
    assert "E7H" in GROUPS  # group letters reach H on the Extra pool


def test_draw_exam_picks_exactly_one_question_per_group():
    exam = draw_exam(load_pool(POOL_PATH), seed=1)
    assert len(exam) == len(GROUPS) == 50  # one per group: a 50-question Extra exam
    assert {q.group for q in exam} == GROUPS


def test_draw_exam_tolerates_deleted_id_gaps():
    # group E1A in the fixture has a deleted-ID gap (01, 03 — no 02);
    # every draw from that group must still be a real pool question
    for seed in range(25):
        exam = draw_exam(load_pool(POOL_PATH), seed=seed)
        picked = [q.id for q in exam if q.group == "E1A"]
        assert len(picked) == 1 and picked[0] in {"E1A01", "E1A03"}


def test_draw_exam_is_reproducible_with_seed():
    first = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    second = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    assert first == second


def test_draw_exam_only_draws_pool_questions_in_order():
    exam = draw_exam(load_pool(POOL_PATH), seed=7)
    ids = [q.id for q in exam]
    assert all(qid in POOL for qid in ids)
    # canonical pool order (E1 … E9, then E0 — plain string sort would
    # put E0 first, so compare against pool_sort_key order)
    assert ids == sorted(ids, key=pool_sort_key)


def test_render_exam_has_questions_and_choices_but_no_answers():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    sheet = render_exam(exam)
    for q in exam:
        assert q.question in sheet
        for text in q.choices.values():
            assert text in sheet
    # nothing on the exam sheet may reveal the key
    lowered = sheet.lower()
    assert "answer" not in lowered
    assert "key" not in lowered
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" not in sheet  # no "1. D"-style key rows


def test_render_exam_header_states_50_questions_and_37_to_pass():
    sheet = render_exam(draw_exam(load_pool(POOL_PATH), seed=3))
    assert "Extra Class Practice Exam" in sheet
    assert "50 questions" in sheet
    assert f"{PASS_SCORE} correct to pass" in sheet
    assert PASS_SCORE == 37  # Element 4: 37 of 50 (Technician/General were 26 of 35)


def test_render_key_lists_correct_letters_and_subelement_tally():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    key = render_key(exam)
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" in key
    assert f"{PASS_SCORE} correct to pass" in key
    # fixture tally: E1–E6 x5 groups, E7 x8, E8 x4, E9 x6, E0 x2 (= 50)
    assert "E1: 5" in key
    assert "E7: 8" in key
    assert "E9: 6" in key
    assert "E0: 2" in key
    # E0 tallies after E9 in canonical order
    assert key.index("E9: 6") < key.index("E0: 2")


def test_cli_writes_exam_and_key(tmp_path):
    from tools.make_exam import main
    rc = main(["--seed", "5", "--pool", str(POOL_PATH), "--out", str(tmp_path)])
    assert rc == 0
    exam_md = (tmp_path / "practice-exam.md").read_text(encoding="utf-8")
    key_md = (tmp_path / "practice-exam-key.md").read_text(encoding="utf-8")
    assert "E1" in exam_md and "answer" not in exam_md.lower()
    assert "50 questions" in exam_md and "37 correct to pass" in exam_md
    assert "E1: 5" in key_md
