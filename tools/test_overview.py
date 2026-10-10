"""Tests of tools/overview.py: the overview copies its items verbatim with the fields it promises, copies whole tables,
rejects a directive it does not know, and the committed OVERVIEW.md is fresh."""
from pathlib import Path
import pytest
import lint
import overview

ROOT = Path(__file__).resolve().parent.parent


def section(text, heading):
    return text.split(heading + "\n", 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]


def test_the_committed_overview_is_fresh():
    """CI fails when an item or the template changed and OVERVIEW.md was not rebuilt: run python3 tools/overview.py."""
    assert overview.build(ROOT) == (ROOT / overview.OUT).read_text(encoding="utf-8")


def test_items_are_copied_verbatim_with_their_fields():
    text, found = overview.build(ROOT), overview.items(ROOT)
    p5 = section(text, "### P5 — " + found["P5"]["title"])
    for label in ("Statement", "In plain terms", "Proof", "Checks"):
        assert f"**{label}.**" + found["P5"]["fields"][label].rstrip() in p5
    assert "**Notes.**" not in p5 and "**Lineage.**" not in p5
    a2, a1 = (section(text, f"### {k} — " + found[k]["title"]) for k in ("A2", "A1"))
    assert "**Why this choice.**" in a2 and "**Why this choice.**" not in a1          # only where the template asks
    assert "**Proof.**" not in a2


def test_tables_are_copied_whole():
    text = overview.build(ROOT)
    cases = [d.name for d in (ROOT / "cases").iterdir() if (d / "REGISTRATION.md").exists()]
    assert cases and all(f"| `{c}/` |" in text for c in cases)
    _, s = lint.lint(ROOT)
    order = overview.table(ROOT / "derived" / "README.md", "| Reading order |")
    assert len(order.splitlines()) == 2 + len(lint.derived_files(ROOT, [])) and order in text
    assert f"{s['proposition']} propositions" in text


def test_the_checks_command_lists_every_check_of_its_items():
    text, found = overview.build(ROOT), overview.items(ROOT)
    command = text.split("```bash\n", 1)[1].split("```", 1)[0]
    for k in ("P1", "P14", "P6"):
        for check in found[k]["fields"]["Checks"].replace("\n", " ").split(","):
            assert check.strip() in command


def test_an_unknown_directive_is_an_error(tmp_path):
    (tmp_path / "tools").mkdir()
    for f in ("CORE.md", "derived", "cases", "stdalign"):
        (tmp_path / f).symlink_to(ROOT / f)
    (tmp_path / overview.TEMPLATE).write_text("# T\n\n{{nonsense}}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="unknown directive"):
        overview.build(tmp_path)
