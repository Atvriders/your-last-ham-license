"""The intro is narrated in all eight voices, named like the chapter tracks:
the default voice (Ryan) is intro.mp3, every other voice <voice>-intro.mp3,
so the player's voice switcher can treat the intro as a normal track.
"""

from tools.make_audiobook import DEFAULT_VOICE, VOICES
from tools.make_intro import dest_name

OTHER_VOICES = ("sonia", "andrew", "ava", "william", "natasha", "connor", "emily")


def test_dest_name_default_voice_is_plain_intro():
    assert DEFAULT_VOICE == "ryan"
    assert dest_name("ryan") == "intro.mp3"


def test_dest_name_other_voices_are_prefixed():
    for v in OTHER_VOICES:
        assert dest_name(v) == f"{v}-intro.mp3"


def test_dest_name_covers_every_voice_exactly_once():
    names = {dest_name(v) for v in VOICES}
    assert len(VOICES) == 8
    assert names == {"intro.mp3"} | {f"{v}-intro.mp3" for v in OTHER_VOICES}


def test_dest_name_matches_chapter_scheme():
    # the intro must slot into the same naming scheme the player derives from
    # the chapters: bare stem for the default voice, <voice>-<stem> otherwise
    from tools.make_audiobook import dest_name as section_dest_name
    for v in VOICES:
        assert dest_name(v) == section_dest_name(v, "intro")
