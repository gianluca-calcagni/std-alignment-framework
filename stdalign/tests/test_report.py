"""Tests of the report as data (stdalign/report.py): W1's report keeps the standard, and each thing the standard says a
report must not do is caught."""
import copy
from pathlib import Path
import pytest
from stdalign import report

W1 = Path(__file__).resolve().parents[2] / "cases" / "w1-best-of-n-slope" / "standard-report.json"


@pytest.fixture
def good():
    return report.load(W1)


def test_w1_keeps_the_standard(good):
    assert report.validate(good) == []


def test_the_fields_are_those_of_the_standard():
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
    import lint
    tables = lint.standard_tables((Path(__file__).resolve().parents[2] / "STANDARD.md").read_text(encoding="utf-8"))
    assert (report.DECLARATION, report.OBSERVATIONS, report.RESULTS) == (
        tables["declaration"], tables["observations"], tables["results"])


def broken(good, change):
    r = copy.deepcopy(good)
    change(r)
    return " | ".join(report.validate(r))


def test_each_rule_fires(good):
    first = lambda r: r["results"]["Misalignment"]["entries"][0]
    assert "'Access' is missing" in broken(good, lambda r: r["declaration"].pop("Access"))
    assert "is not a field of the standard" in broken(good, lambda r: r["observations"].update({"Mood": "fine"}))
    assert "'Drift': missing" in broken(good, lambda r: r["results"].pop("Drift"))
    assert "needs its interval" in broken(good, lambda r: first(r).pop("interval"))
    assert "outside its interval" in broken(good, lambda r: first(r).update({"value": 99.0}))
    assert "not identified, so give its bounds" in broken(good, lambda r: r["results"]["Misalignment"].update(
        {"identified": False}))
    assert "on what basis it is exact" in broken(good, lambda r: first(r).update({"exact": True}))
    assert "cannot be confirmatory" in broken(good, lambda r: r.update({"confirmatory": True}))
    assert "exactly one of" in broken(good, lambda r: r["results"]["Drift"].update({"text": "also"}))
    assert "is empty" in broken(good, lambda r: r["results"]["Drift"].update({"not_reported": " "}))
    assert "bounds must be two numbers" in broken(good, lambda r: r["results"]["Misalignment"]["entries"].append(
        {"label": "a set", "bounds": [2.0, 1.0]}))
    assert "say what the result assumes" in broken(good, lambda r: r["results"]["Misalignment"].pop("assumptions"))


def test_a_quantity_not_identified_is_reported_by_its_bounds(good):
    r = copy.deepcopy(good)
    r["results"]["Unobserved conditions"] = {"identified": False, "assumptions": "a view with ε = 0.1",
                                             "entries": [{"label": "average of F there", "bounds": [0.2, 0.9]}]}
    assert report.validate(r) == []
