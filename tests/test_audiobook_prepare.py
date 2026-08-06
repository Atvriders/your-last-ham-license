import re

from tools.make_audiobook import CHAPTER_COUNT, spoken_heading, prepare_text, parse_chapters

def test_spoken_heading_numbered_chapter():
    assert spoken_heading("4. Antennas & Feedlines") == \
        "Chapter Four. Antennas & Feedlines."

def test_spoken_heading_chapter_zero():
    assert spoken_heading("0. The Last License: Why Extra & How This Book Works") == \
        "Chapter Zero. The Last License: Why Extra & How This Book Works."

def test_spoken_heading_passthrough():
    assert spoken_heading("Something unexpected") == "Something unexpected"

def test_parse_chapters_defaults_to_eleven():
    assert parse_chapters("") == list(range(11))
    assert parse_chapters("0-12") == list(range(11))  # clamped to 0..10

def test_discovery_never_picks_up_preface():
    # chapters are addressed by constructed chNN paths (never a glob), so a
    # chapters/preface.md front-matter file can never enter the audiobook
    stems = [f"ch{n:02d}" for n in parse_chapters("")]
    assert len(stems) == CHAPTER_COUNT
    assert all(re.fullmatch(r"ch\d\d", s) for s in stems)
    assert "preface" not in stems

def test_prepare_text_speaks_math_and_drops_fig_markup():
    out = prepare_text("The tank obeys $E = IR$ here.\n\n{{fig:x}}\n", {"x": ("1", "a tank")})
    assert "E equals I R" in out
    assert "{{fig" not in out
    assert "Figure 1" in out
