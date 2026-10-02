"""Tests of tools/obsidian.py: the view covers every item, its links resolve, it is fresh, and it leaves alone what it
does not own."""
import re
from pathlib import Path
import lint
import obsidian

ROOT = Path(__file__).resolve().parent.parent


def section(text, heading):
    return text.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]


def test_every_item_has_a_note_and_every_link_resolves():
    notes = obsidian.build(ROOT)
    _, summary = lint.lint(ROOT)
    items = [p for p in notes if p.startswith(("Core/", "Derived/")) and " — " in p]
    assert len(items) == summary["items"]
    assert obsidian.broken_links(notes) == []
    assert any("[[References|@" in text for text in notes.values())                  # citations are links too


def test_dependencies_are_lints():
    """A note depends on what its Statement, Why and Proof cite, as lint R5 says; a citation in Notes is not a
    dependency. P33 cites P29 in its Statement, and P30 and C3 only in its Notes."""
    notes = obsidian.build(ROOT)
    p33 = next(t for p, t in notes.items() if p.split("/")[-1].startswith("P33 — "))
    p29 = next(t for p, t in notes.items() if p.split("/")[-1].startswith("P29 — "))
    assert "|P29]]" in section(p33, "Depends on")
    assert "|P30]]" not in section(p33, "Depends on") and "|C3]]" not in section(p33, "Depends on")
    assert "|P33]]" in section(p29, "Used by")


def test_anchors_follow_github():
    assert obsidian.anchor("P34 — Choosing by the evaluator from a common candidate set") == \
        "p34--choosing-by-the-evaluator-from-a-common-candidate-set"
    assert obsidian.anchor("D3 — Specification, declaration and misalignment") == \
        "d3--specification-declaration-and-misalignment"


def test_the_committed_view_is_fresh():
    """CI fails when a source changed and obsidian/ was not regenerated: run python3 tools/obsidian.py."""
    assert obsidian.build(ROOT) == obsidian.on_disk(ROOT / "obsidian")


def test_writing_keeps_settings_and_annotations(tmp_path):
    (tmp_path / ".obsidian").mkdir(); (tmp_path / ".obsidian" / "app.md").write_text("settings")
    (tmp_path / "Annotations").mkdir(); (tmp_path / "Annotations" / "mine.md").write_text("my note")
    (tmp_path / "Old").mkdir(); (tmp_path / "Old" / "gone.md").write_text("a note whose source is gone")
    notes = obsidian.build(ROOT)
    obsidian.write(notes, tmp_path)
    assert (tmp_path / ".obsidian" / "app.md").read_text() == "settings"
    assert (tmp_path / "Annotations" / "mine.md").read_text() == "my note"
    assert not (tmp_path / "Old").exists()
    assert obsidian.on_disk(tmp_path) == notes


def test_a_broken_link_is_found():
    notes = {"a.md": "see [[b|B]] and [[a]]", "Folder/c.md": "[[a#Heading]]\n| [[d\\|D]] | [[a\\|A]] |"}
    assert obsidian.broken_links(notes) == ["b", "d"]


def test_links_in_tables_do_not_split_cells():
    """Inside a table row, a link's '|' must be written '\\|', or Obsidian reads it as a cell boundary (v7.10 shipped
    41 malformed tables this way)."""
    notes = obsidian.build(ROOT)
    rows = [line for text in notes.values() for line in text.split("\n") if line.lstrip().startswith("|")]
    linked = [row for row in rows if "[[" in row]
    assert len(linked) > 100                                                        # the case is exercised
    assert not [row for row in linked if re.search(r"\[\[[^\]]*(?<!\\)\|", row)]
    prose = [line for text in notes.values() for line in text.split("\n") if line.startswith("- [[")]
    assert prose and all("\\|" not in line for line in prose)                       # outside tables, a plain '|'
