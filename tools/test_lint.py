"""Tests of tools/lint.py: a valid framework passes, and each rule fires on a document built to break it."""
import textwrap
from pathlib import Path
import pytest
from lint import lint

CORE = textwrap.dedent("""\
    # The core

    ## Premises

    ### A1 — Finite
    **Statement.** Only finitely many outcomes are considered.
    **In plain terms.** Only finitely many different things can happen in any one decision.
    **Why this choice.** Finite sums can be checked exactly [@cover2006].
    **Lineage.** New.

    ## Definitions

    ### D1 — Outcomes
    **Statement.** A finite set `X`, with a full-support reference `q`, as [A1] allows.
    **In plain terms.** The things that can happen, and how often they happen by default.
    **Why this choice.** Finite first, so that every claim can be checked exactly.
    **Lineage.** New.

    ### D2 — Objectives
    **Statement.** A function `F` on `X`.
    **In plain terms.** What the principal wants, written as a score for each outcome.
    **Why this choice.** Every behaviour is a reweighting of the default by some function, as [P1] shows.
    **Lineage.** New.
    """)
DERIVED = textwrap.dedent("""\
    # Derived — tilts

    ### P1 — A fact about [D1]
    **Statement.** Every full-support `p` on `X` is `q·e^F` for some `F`, by [D1].
    **In plain terms.** Any way of behaving can be described as a reweighting of the default.
    **Proof.** Take `F = log(p/q)`.

    ```python
    # a code comment is not a heading
    **Proof.** nor is this a field
    ```
    **Checks.** checks/test_a.py::test_tilt
    **Lineage.** v7.10: Def 1.
    """)
ORDER = "# Derived results\n\n| Reading order | File |\n|---|---|\n| 1 | `a.md` |\n"
STANDARD = "# The reporting standard\n\n| Field | Core |\n|---|---|\n| Outcomes | [D1] |\n| Objective | [D2] |\n"
REFS = "# References\n\n- [@cover2006] Cover and Thomas (2006), *Elements of Information Theory*.\n"
TEST = "def test_tilt():\n    assert True\n"


def make(tmp_path, core=CORE, derived=DERIVED, order=ORDER, standard=STANDARD, refs=REFS, test=TEST, extra=None):
    (tmp_path / "CORE.md").write_text(core); (tmp_path / "REFERENCES.md").write_text(refs)
    (tmp_path / "derived").mkdir(exist_ok=True)
    (tmp_path / "derived" / "a.md").write_text(derived); (tmp_path / "derived" / "README.md").write_text(order)
    if standard is not None:
        (tmp_path / "STANDARD.md").write_text(standard)
    (tmp_path / "checks").mkdir(exist_ok=True); (tmp_path / "checks" / "test_a.py").write_text(test)
    for name, text in (extra or {}).items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True); (tmp_path / name).write_text(text)
    return lint(tmp_path)


def codes(errors):
    return {e.split(" R")[1].split()[0] for e in errors if " R" in e}


def test_good_framework_passes(tmp_path):
    errors, summary = make(tmp_path)
    assert errors == [], errors
    assert summary["items"] == 4 and summary["premise"] == 1 and summary["definition"] == 2
    assert summary["proposition"] == 1 and summary["checks"] == 1


@pytest.mark.parametrize("where,old,new,rule", [
    ("core", "# The core", "The core", "1"),                                                   # no title
    ("core", "### D1 — Outcomes", "### Outcomes", "1"),                                        # a heading, not an item
    ("core", "### D2 — Objectives", "### P2 — Objectives", "1"),                               # a result in the core
    ("derived", "### P1 — A fact", "### D3 — A fact", "1"),                                     # a definition in derived/
    ("core", "### D2 — Objectives", "### D1 — Objectives", "2"),                               # duplicate id
    ("core", "### D1 — Outcomes", "### D3 — Outcomes", "2"),                                   # D3 before D2
    ("core", "**Why this choice.** Finite first", "**Lineage.** New.\n**Why this choice.** Finite first", "3"),
    ("core", "**In plain terms.** The things that can happen, and how often they happen by default.\n", "", "4"),
    ("core", "**Why this choice.** Finite sums can be checked exactly [@cover2006].\n", "", "4"),  # a premise needs a why
    ("derived", "**Proof.** Take `F = log(p/q)`.", "", "4"),                                     # a result needs a proof
    ("core", "Every behaviour is a reweighting", "Every behaviour, by [P7], is a reweighting", "5"),  # names no item
    ("core", "as [A1] allows.", "as [P1] shows.", "5"),                                         # a core Statement uses a result
    ("core", "**Statement.** A finite set `X`", "**Statement.** With `F` of [D2], a finite set `X`", "5"),  # a later item
    ("derived", "for some `F`, by [D1].", "for some `F`, by [D2].", "5"),                       # a cycle: D2 → P1 → D2
    ("derived", "checks/test_a.py::test_tilt", "checks/test_a.py::test_other", "6"),            # no such check
    ("derived", "**Checks.** checks/test_a.py::test_tilt", "**Checks.** see the tests", "6"),   # a result without checks
])
def test_each_rule_fires(tmp_path, where, old, new, rule):
    src = CORE if where == "core" else DERIVED
    changed = src.replace(old, new)
    assert changed != src
    errors, _ = make(tmp_path, **({"core": changed} if where == "core" else {"derived": changed}))
    assert rule in codes(errors), errors


def test_a_core_statement_may_not_use_a_result(tmp_path):
    core = CORE.replace("**Statement.** A function `F` on `X`.", "**Statement.** A function `F` on `X`, as in [P1].")
    errors, _ = make(tmp_path, core=core)                                          # no cycle: P1 uses only D1
    assert any("D2: R5 its Statement uses [P1], which is not an earlier core item" in e for e in errors), errors
    assert not any("cycle" in e for e in errors), errors


def test_a_cycle_is_named(tmp_path):
    errors, _ = make(tmp_path, derived=DERIVED.replace("by [D1].", "by [D2]."))
    assert any("cycle" in e and "D2" in e and "P1" in e for e in errors), errors


def test_a_result_may_not_use_a_later_result(tmp_path):
    later = DERIVED.replace("### P1 — A fact about [D1]", "### P2 — Another fact").replace(
        "checks/test_a.py::test_tilt", "checks/test_a.py::test_two")
    first = DERIVED.replace("by [D1].", "by [D1] and [P2].")
    errors, _ = make(tmp_path, derived=first, order=ORDER + "| 2 | `b.md` |\n", test=TEST + "\ndef test_two():\n    assert True\n",
                     extra={"derived/b.md": later})
    assert any("R5" in e and "later in the reading order" in e for e in errors), errors


def test_the_reading_order_must_list_every_file(tmp_path):
    errors, _ = make(tmp_path, extra={"derived/b.md": "# Derived — b\n"})
    assert any("b.md is not listed" in e for e in errors), errors
    errors, _ = make(tmp_path, order=ORDER + "| 2 | `c.md` |\n")
    assert any("c.md is listed but does not exist" in e for e in errors), errors


def test_orphan_check_fires(tmp_path):
    errors, _ = make(tmp_path, test=TEST + "\ndef test_unclaimed():\n    assert True\n")
    assert any("R7 test_unclaimed" in e for e in errors), errors


def test_bibliography_rules_fire(tmp_path):
    errors, _ = make(tmp_path, refs=REFS + "- [@unused2020] Nobody (2020).\n- [@cover2006] Again.\n")
    assert any("R8 [@unused2020] is cited nowhere" in e for e in errors) and any("listed twice" in e for e in errors)
    errors, _ = make(tmp_path, refs="# References\n")
    assert any("R8 [@cover2006] is not in REFERENCES.md" in e for e in errors), errors


def test_a_source_cited_only_in_a_derived_file_counts(tmp_path):
    core = CORE.replace(" [@cover2006]", "")
    errors, _ = make(tmp_path, core=core, derived=DERIVED.replace("**Proof.** Take", "**Proof.** [@cover2006] Take"))
    assert errors == [], errors


def test_glossary_rule_fires(tmp_path):
    core = CORE.replace("**Statement.** A finite set `X`, with", "**Statement.** A finite set `X` of **outcomes**, with")
    errors, _ = make(tmp_path, core=core)
    assert any("R9 the term 'outcomes' has no entry" in e for e in errors), errors
    (tmp_path / "TERMS.md").write_text("| Term | Meaning |\n|---|---|\n| **outcome** | what can happen, see [D1] |\n")
    errors, _ = make(tmp_path, core=core)
    assert not any("R9" in e for e in errors), errors                       # plural and case are matched
    (tmp_path / "TERMS.md").write_text("| Term | Meaning |\n|---|---|\n| **outcome** | see [D7] |\n")
    errors, _ = make(tmp_path, core=core)
    assert any("R9 [D7] names no item" in e for e in errors), errors


def test_terms_defined_in_derived_files_count(tmp_path):
    derived = DERIVED.replace("**Statement.** Every full-support", "**Statement.** Every **full-support**")
    errors, _ = make(tmp_path, derived=derived)
    assert any("R9 the term 'full-support'" in e for e in errors), errors


def test_part_labels_are_not_terms(tmp_path):
    derived = DERIVED.replace("**Statement.** Every full-support", "**Statement.** **Universality.** Every full-support")
    errors, _ = make(tmp_path, derived=derived)
    assert not any("R9" in e for e in errors), errors


def test_the_survey_of_related_theories_is_checked(tmp_path):
    related = "# Related theories\n\n- shares [D1] and [P1] [@cover2006]\n"
    errors, _ = make(tmp_path, core=CORE.replace(" [@cover2006]", ""), extra={"RELATED.md": related})
    assert errors == [], errors                                                    # its citation counts for R8
    errors, _ = make(tmp_path, extra={"RELATED.md": related + "- and [P9]\n"})
    assert any("RELATED.md:4: R12 [P9] names no item" in e for e in errors), errors
    errors, _ = make(tmp_path, extra={"RELATED.md": related + "- [@nobody1900]\n"})
    assert any("RELATED.md: R8 [@nobody1900] is not in REFERENCES.md" in e for e in errors), errors


def test_the_import_map_names_only_existing_items(tmp_path):
    ledger = "# Import\n\n| Thm 1 | regret is a divergence | in core | [P1] |\n"
    errors, _ = make(tmp_path, extra={"IMPORT.md": ledger})
    assert errors == [], errors
    errors, _ = make(tmp_path, extra={"IMPORT.md": ledger + "| Thm 5 | the width | derive | [P9] |\n"})
    assert any("IMPORT.md:4: R12 [P9] names no item" in e for e in errors), errors


def test_the_general_core_names_only_existing_items(tmp_path):
    """CORE-GENERAL.md is a draft: its GA and GD items are not the core's items, but every core item or result it names
    must exist, and its citations count for R8."""
    general = "# The general core\n\n### GD1 — Behaviours\n**Statement.** As [D1], on events [@cover2006].\n"
    errors, _ = make(tmp_path, core=CORE.replace(" [@cover2006]", ""), extra={"CORE-GENERAL.md": general})
    assert errors == [], errors
    errors, _ = make(tmp_path, extra={"CORE-GENERAL.md": general + "Extends [P9].\n"})
    assert any("CORE-GENERAL.md:5: R12 [P9] names no item" in e for e in errors), errors


def test_the_general_results_name_only_existing_items(tmp_path):
    """general/*.md, the general core's results, are checked like CORE-GENERAL.md: every item they name exists, and their
    citations count for R8."""
    note = "# General results\n\n- carries [P1] [@cover2006]\n"
    errors, _ = make(tmp_path, core=CORE.replace(" [@cover2006]", ""), extra={"general/transfer.md": note})
    assert errors == [], errors
    errors, _ = make(tmp_path, extra={"general/transfer.md": note + "- and [P9]\n"})
    assert any("general/transfer.md:4: R12 [P9] names no item" in e for e in errors), errors


def test_the_standard_must_cover_every_definition(tmp_path):
    errors, _ = make(tmp_path, standard=None)
    assert any("R11 the reporting standard is missing" in e for e in errors), errors
    errors, _ = make(tmp_path, standard=STANDARD.replace("| Objective | [D2] |\n", ""))
    assert any("R11 the definition D2 is not covered" in e for e in errors), errors
    errors, _ = make(tmp_path, standard=STANDARD + "| Other | [D9] |\n")
    assert any("R11 [D9] names no item" in e for e in errors), errors


ONTO_README = textwrap.dedent("""\
    # Ontologies

    | Slot | Core | Type | What the entry must say |
    |---|---|---|---|
    | **outcomes** | [D1] | a finite set | what one outcome is |
    | **fact** | [P1] | a result | how it is read |
    """)
ONTO = textwrap.dedent("""\
    # Ontology — a discipline

    ## 1. Slots

    | Slot | Core | In this discipline | Observed as | Fit |
    |---|---|---|---|---|
    | **outcomes** | [D1] | the options | records | exact |
    | **fact** | [P1] | a reweighting | records | approximate: rounded |

    ## 2. Known result

    A known finding [@cover2006].

    **Data.** Counts per option, public.

    ## 3. What the core says

    - **Consequence** of [P1]: it follows.
    - **Prediction** (empirical) from [D1], [P1]: data would show it,
      over two lines. *Refuted if* it does not.
    - **Reading** with [D1]: a redescription.

    ## 4. Limits

    - Some.

    ## 5. Open questions

    - Some.
    """)


RECORD = textwrap.dedent("""\
    # Record

    | Ontology | From | Label | State | Where |
    |---|---|---|---|---|
    | a | [D1], [P1] | empirical | untested | `ontologies/a/` |
    """)


def make_ontology(tmp_path, onto=ONTO, readme=ONTO_README, record=RECORD):
    extra = {"ontologies/README.md": readme, "ontologies/a/README.md": onto}
    if record is not None:
        extra["RECORD.md"] = record
    return make(tmp_path, extra=extra)


def test_good_ontology_passes(tmp_path):
    errors, summary = make_ontology(tmp_path)
    assert errors == [] and summary["ontologies"] == 1, errors


@pytest.mark.parametrize("old,new,message", [
    ("# Ontology — a discipline", "# A discipline", "must start with"),                          # title
    ("## 4. Limits\n\n- Some.\n\n", "", "sections must be"),                                    # a missing section
    ("| **fact** | [P1] | a reweighting | records | approximate: rounded |\n", "", "appears 0 times"),
    ("| **outcomes** | [D1] | the options | records | exact |",
     "| **outcomes** | [D1] | the options | records | exact |\n| **outcomes** | [D1] | again | records | exact |",
     "appears 2 times"),
    ("| **fact** | [P1] |", "| **fact** | [D1] |", "must name [P1]"),                             # the wrong item
    ("| records | exact |", "| records | certain |", "Fit of 'outcomes'"),                         # not a fit word
    ("| records | exact |", "| records | |", "fill all"),                                          # an empty cell
    ("| **fact** |", "| **other** |", "not a slot"),                                               # an unknown slot
    ("A known finding [@cover2006].", "A known finding.", "must cite its source"),
    ("**Data.** Counts per option, public.", "Counts per option, public.", "needs a paragraph '**Data.**'"),
    ("- **Consequence** of [P1]: it follows.", "- It follows from [P1].", "must start with a kind"),
    ("- **Reading** with [D1]: a", "- **Reading** with the core: a", "names no item before"),
    (" *Refuted if* it does not.", " It could fail.", "Refuted if"),
    ("**Prediction** (empirical) from", "**Prediction** from", "must be labelled"),               # no label
    ("**Prediction** (empirical) from", "**Prediction** (likely) from", "must start with a kind"),  # not a label
    ("- **Reading** with [D1]: a redescription.",
     "- **Prediction** (empirical) from [P1], [D1]: again. *Refuted if* not.", "two predictions from the same items"),
    ("- **Consequence** of [P1]:", "- **Consequence** of [P9]:", "[P9] names no item"),
    ("A known finding [@cover2006].", "A known finding [@cover2006], [@nobody1900].", "R8 [@nobody1900]"),
    ("## 5. Open questions\n\n- Some.\n", "## 5. Open questions\n", "is empty"),
])
def test_ontology_rule_fires(tmp_path, old, new, message):
    onto = ONTO.replace(old, new)
    assert onto != ONTO
    errors, _ = make_ontology(tmp_path, onto=onto)
    assert any(message in e for e in errors), errors


@pytest.mark.parametrize("old,new,message", [
    ("| a | [D1], [P1] | empirical | untested | `ontologies/a/` |\n", "", "has no row"),          # a prediction left out
    ("| a | [D1], [P1] |", "| b | [D1], [P1] |", "no prediction of ontologies/b/"),              # an unknown ontology
    ("| a | [D1], [P1] |", "| a | [D1] |", "no prediction of ontologies/a/"),                    # other items
    ("| empirical | untested |", "| verification | untested |", "the label is 'verification'"),
    ("| empirical | untested |", "| empirical | pending |", "the state must start"),
    ("| untested | `ontologies/a/` |", "| untested |", "must fill all"),
    ("| a | [D1], [P1] | empirical | untested | `ontologies/a/` |\n",
     "| a | [D1], [P1] | empirical | untested | `ontologies/a/` |\n| a | [D1], [P1] | empirical | held | twice |\n",
     "listed twice"),
    ("# Record\n", "# Record, after [P9]\n", "R13 [P9] names no item"),
    ("| Ontology | From | Label | State | Where |", "| Ontology | From | Label | State |", "no ledger"),
])
def test_record_rule_fires(tmp_path, old, new, message):
    record = RECORD.replace(old, new)
    assert record != RECORD
    errors, _ = make_ontology(tmp_path, record=record)
    assert any(message in e for e in errors), errors


def test_the_record_is_required_once_an_ontology_predicts(tmp_path):
    errors, _ = make_ontology(tmp_path, record=None)
    assert any("R13 the record" in e and "is missing" in e for e in errors), errors
    without = ONTO.replace("- **Prediction** (empirical) from [D1], [P1]: data would show it,\n"
                           "  over two lines. *Refuted if* it does not.\n", "")
    assert without != ONTO
    errors, _ = make_ontology(tmp_path, onto=without, record=None)
    assert errors == [], errors


def test_a_source_cited_only_in_the_record_counts(tmp_path):
    core = CORE.replace(" [@cover2006]", "")
    onto = ONTO.replace("A known finding [@cover2006].", "A known finding [@cover2006].")
    record = RECORD + "\nThe base rate follows [@cover2006].\n"
    errors, _ = make(tmp_path, core=core, extra={"ontologies/README.md": ONTO_README, "ontologies/a/README.md": onto,
                                                  "RECORD.md": record})
    assert errors == [], errors
    errors, _ = make_ontology(tmp_path, record=RECORD + "\n[@nobody1900]\n")
    assert any("RECORD.md: R8 [@nobody1900] is not in REFERENCES.md" in e for e in errors), errors


def test_ontology_readme_rules_fire(tmp_path):
    errors, _ = make_ontology(tmp_path, readme="# Ontologies\n")
    assert any("no slot table" in e for e in errors), errors
    (tmp_path / "ontologies" / "README.md").unlink()
    errors, _ = make(tmp_path)
    assert any("README.md, with the slot table, is missing" in e for e in errors), errors


def test_an_ontology_lives_in_its_own_folder(tmp_path):
    errors, _ = make(tmp_path, extra={"ontologies/README.md": ONTO_README, "ontologies/loose.md": ONTO})
    assert any("lives in its own folder" in e for e in errors), errors


def test_a_source_cited_only_in_an_ontology_counts(tmp_path):
    core = CORE.replace(" [@cover2006]", "")
    errors, _ = make(tmp_path, core=core, extra={"ontologies/README.md": ONTO_README, "ontologies/a/README.md": ONTO,
                                                  "RECORD.md": RECORD})
    assert errors == [], errors


def test_the_repository_itself_passes():
    errors, _ = lint(Path(__file__).resolve().parent.parent)
    assert errors == [], errors
