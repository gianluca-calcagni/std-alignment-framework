"""Tests of tools/mutate.py on a small repository made here: a mutant the tests catch, one they miss, and an edit that
does not apply."""
import json
import pytest
import mutate


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    (root / "pkg").mkdir(parents=True)
    (root / "pkg" / "f.py").write_text("def double(x):\n    return 2 * x\n\n\ndef unused(x):\n    return x\n")
    (root / "pkg" / "test_f.py").write_text("from f import double\n\n\ndef test_double():\n    assert double(3) == 6\n")
    (root / "pytest.ini").write_text("[pytest]\npythonpath = pkg\n")
    return root


def spec(*mutants):
    return {"tests": ["pkg"], "mutants": list(mutants)}


def test_a_caught_and_a_surviving_mutant(repo):
    results = mutate.run(spec({"name": "triple", "edits": [["pkg/f.py", "return 2 * x", "return 3 * x"]]},
                              {"name": "untested", "edits": [["pkg/f.py", "    return x\n", "    return -x\n"]]}),
                         root=repo)
    assert [(name, caught) for name, caught, _, _ in results] == [("triple", True), ("untested", False)]
    assert (repo / "pkg" / "f.py").read_text().count("return 2 * x") == 1          # the original is never touched


def test_an_edit_that_does_not_apply_is_an_error(repo):
    with pytest.raises(ValueError, match="occurs 0 times"):
        mutate.run(spec({"name": "absent", "edits": [["pkg/f.py", "return 4 * x", "return 5 * x"]]}), root=repo)


def test_the_mutant_lists_are_well_formed():
    for path in sorted((mutate.ROOT / "tools" / "mutants").glob("*.json")):
        s = json.loads(path.read_text(encoding="utf-8"))
        assert s["tests"] and s["mutants"], path.name
        for m in s["mutants"]:
            assert m["name"] and m["edits"], (path.name, m)
            for f, old, new in m["edits"]:
                text = (mutate.ROOT / f).read_text(encoding="utf-8")
                assert old != new and text.count(old) == 1, (path.name, m["name"], f)
