"""Tests of tools/lint.py: a valid core passes, and each rule fires on a document built to break it."""
import textwrap
from pathlib import Path
import pytest
from lint import lint

GOOD = textwrap.dedent("""\
    # The core

    ## Setting

    ### D1 — Outcomes
    **Statement.** A finite set `X`, with a full-support reference `q`.
    **In plain terms.** The things that can happen, and how often they happen by default.
    **Why this choice.** Finite first, so that every claim can be checked exactly [@cover2006].
    **Lineage.** New.

    ### P1 — A fact about [D1]
    **Statement.** Every full-support `p` on `X` is `q·e^F` for some `F`, by [D1].
    **In plain terms.** Any way of behaving can be described as a reweighting of the default.
    **Proof.** Take `F = log(p/q)`.

    ```python
    # a code comment is not a heading
    **Proof.** nor is this a field
    ```
    **Checks.** checks/test_a.py::test_tilt
    **Lineage.** main: Def 1.
    """)
REFS = "# References\n\n- [@cover2006] Cover and Thomas (2006), *Elements of Information Theory*.\n"
TEST = "def test_tilt():\n    assert True\n"


def make(tmp_path, core=GOOD, refs=REFS, test=TEST):
    (tmp_path / "CORE.md").write_text(core); (tmp_path / "REFERENCES.md").write_text(refs)
    (tmp_path / "checks").mkdir(exist_ok=True); (tmp_path / "checks" / "test_a.py").write_text(test)
    return lint(tmp_path)


def codes(errors): return {e.split(": R")[1][0] if ": R" in e else "?" for e in errors}


def test_good_core_passes(tmp_path):
    errors, summary = make(tmp_path)
    assert errors == []
    assert summary["items"] == 2 and summary["definition"] == 1 and summary["proposition"] == 1 and summary["checks"] == 1


@pytest.mark.parametrize("old,new,rule", [
    ("# The core", "The core", "1"),                                                    # no title
    ("### D1 — Outcomes", "### Outcomes", "1"),                                         # a heading that is not an item
    ("### P1 — A fact", "### D1 — A fact", "2"),                                         # duplicate id
    ("**Why this choice.** Finite first", "**Lineage.** New.\n**Why this choice.** Finite first", "3"),  # order
    ("**In plain terms.** The things that can happen, and how often they happen by default.\n", "", "4"),
    ("**Why this choice.** Finite first, so that every claim can be checked exactly [@cover2006].\n", "", "4"),
    ("**Proof.** Take `F = log(p/q)`.", "", "4"),                                          # a result without a proof
    ("Any way of behaving can be described as a reweighting of the default.", "Too short to say.", "4"),
    ("by [D1].", "by [D2].", "5"),                                                        # names no item
    ("Finite first, so that", "Finite first, as [P1] needs, so that", "5"),               # uses a later item
    ("checks/test_a.py::test_tilt", "checks/test_a.py::test_other", "6"),                # no such check
    ("**Checks.** checks/test_a.py::test_tilt", "**Checks.** see the tests", "6"),       # a result without a check
])
def test_each_rule_fires(tmp_path, old, new, rule):
    core = GOOD.replace(old, new)
    assert core != GOOD
    errors, _ = make(tmp_path, core=core)
    assert rule in codes(errors), errors


def test_orphan_check_fires(tmp_path):
    errors, _ = make(tmp_path, test=TEST + "\ndef test_unclaimed():\n    assert True\n")
    assert any("R7 test_unclaimed" in e for e in errors), errors


def test_bibliography_rules_fire(tmp_path):
    errors, _ = make(tmp_path, refs=REFS + "- [@unused2020] Nobody (2020).\n- [@cover2006] Again.\n")
    assert any("R8 [@unused2020] is cited nowhere" in e for e in errors) and any("listed twice" in e for e in errors)
    errors, _ = make(tmp_path, refs="# References\n")
    assert any("R8 [@cover2006] is not in REFERENCES.md" in e for e in errors), errors


def test_glossary_rule_fires(tmp_path):
    core = GOOD.replace("**Statement.** A finite set `X`, with", "**Statement.** A finite set `X` of **outcomes**, with")
    errors, _ = make(tmp_path, core=core)
    assert any("R9 the term 'outcomes' has no entry" in e for e in errors), errors
    (tmp_path / "TERMS.md").write_text("| Term | Meaning |\n|---|---|\n| **outcome** | what can happen, see [D1] |\n")
    errors, _ = make(tmp_path, core=core)
    assert not any("R9" in e for e in errors), errors                       # plural and case are matched
    (tmp_path / "TERMS.md").write_text("| Term | Meaning |\n|---|---|\n| **outcome** | see [D7] |\n")
    errors, _ = make(tmp_path, core=core)
    assert any("R9 [D7] names no item" in e for e in errors), errors


def test_part_labels_are_not_terms(tmp_path):
    core = GOOD.replace("**Statement.** Every full-support", "**Statement.** **Universality.** Every full-support")
    errors, _ = make(tmp_path, core=core)
    assert not any("R9" in e for e in errors), errors


def test_the_repository_itself_passes():
    errors, _ = lint(Path(__file__).resolve().parent.parent)
    assert errors == [], errors
