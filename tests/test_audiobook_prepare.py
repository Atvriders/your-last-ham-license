import re
from pathlib import Path

from tools.make_audiobook import (
    CHAPTER_COUNT, dest_name, sections_for, spoken_heading, prepare, prepare_text,
    parse_chapters,
)

FIXTURES = Path(__file__).parent / "fixtures"

def test_spoken_heading_numbered_chapter():
    assert spoken_heading("4. Antennas & Feedlines") == \
        "Chapter Four. Antennas & Feedlines."

def test_spoken_heading_chapter_zero():
    assert spoken_heading("0. The Last License: Why Extra & How This Book Works") == \
        "Chapter Zero. The Last License: Why Extra & How This Book Works."

def test_spoken_heading_preface():
    assert spoken_heading("Preface — Why & How This Book Was Made") == \
        "Preface: Why and How This Book Was Made."

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

def test_dest_name_preface_default_voice():
    assert dest_name("ryan", "preface") == "preface.mp3"

def test_dest_name_preface_other_voices():
    for v in ("sonia", "andrew", "ava", "william", "natasha", "connor", "emily"):
        assert dest_name(v, "preface") == f"{v}-preface.mp3"

def test_dest_name_chapters_unchanged():
    assert dest_name("ryan", 0) == "ch00.mp3"
    assert dest_name("ryan", 10) == "ch10.mp3"
    assert dest_name("ava", 3) == "ava-ch03.mp3"

def test_sections_for_default_is_preface_plus_chapters():
    assert sections_for(None, list(range(CHAPTER_COUNT))) == \
        ["preface"] + list(range(CHAPTER_COUNT))

def test_sections_for_only_preface():
    assert sections_for("preface", list(range(CHAPTER_COUNT))) == ["preface"]

def test_sections_for_only_chapters():
    assert sections_for("chapters", [0, 4]) == [0, 4]

def test_prepare_preface_fixture():
    title, text = prepare(FIXTURES / "preface.md", "preface")
    assert title == "Preface: Why and How This Book Was Made."
    assert text.startswith(title + "\n\n")
    # no markdown headings or emphasis leak into the narration
    assert "##" not in text and "**" not in text
    # ### subheads drop to plain lines, body prose is kept
    assert "Why This Book Exists" in text
    assert "plain prose, no chapter number" in text
    # the book-title intro is reserved for chapter 0, not the preface
    assert "Your Last Ham License. The Extra Course" not in text
