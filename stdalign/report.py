"""A report to the standard, as data: the fields of `STANDARD.md`, and a validator for them.

A report is a JSON object with three sections, as in `STANDARD.md`: the declaration and the observations, one text per
field, and the results, one entry per field. A result is either a text (for a field that describes, such as
Uncertainty or Premises), or numbers, or the reason it is not reported:

    {"text": "..."}
    {"identified": true, "assumptions": "...", "entries": [
        {"label": "n = 16", "value": 1.378, "interval": [1.354, 1.401], "unit": "nats"},     # estimated: an interval
        {"label": "median t*", "value": 1.77, "exact": true, "basis": "over the 1,000 prompts reported on"},
        {"label": "...", "bounds": [0.2, 0.9]}]}                                             # not identified: a set
    {"not_reported": "no intervention was applied"}

The top level also says whether the declaration was fixed before the data were seen, and whether the report claims to
be confirmatory. The validator enforces what `STANDARD.md` says a report must not do: give one number for a quantity
that is not identified, give an estimated value without its interval, or call itself confirmatory when its
declaration came after the data. This module uses the standard library only, so that lint can run it anywhere.
"""
import json
import math
from pathlib import Path

DECLARATION = ("Outcomes", "Conditions", "Default", "Principal", "Specification", "Principal's resolution",
               "Feasible set", "View", "Interventions", "Observed conditions", "Objective's units", "Evaluator",
               "Sampling", "Access", "Named objectives", "Runs")
OBSERVATIONS = ("Behaviour", "Interventions applied", "Departures from the declaration")
RESULTS = ("Misalignment", "Uncertainty", "Evidence and detection", "Revealed intensity", "Departure split", "Stakes",
           "Intensity", "Named and unexplained misalignment", "Uncertain target", "Outer and inner misalignment",
           "Tampering", "Drift", "Avoidable and unavoidable misalignment", "Resolution", "Sensitivity", "Evaluator",
           "Pass-through", "Unobserved conditions", "Evaluation gap", "Premises")
TOP = {"case", "declared_before_data", "confirmatory", "declaration", "observations", "results"}


def _number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _texts(section, names, data, errors):
    if not isinstance(data, dict):
        errors.append(f"{section}: must be an object with one text per field")
        return
    for name in names:
        if not isinstance(data.get(name), str) or not data[name].strip():
            errors.append(f"{section}: the field '{name}' is missing or empty")
    for name in sorted(set(data) - set(names)):
        errors.append(f"{section}: '{name}' is not a field of the standard")


def _entry(where, e, identified, errors):
    if not isinstance(e, dict) or not isinstance(e.get("label"), str) or not e["label"].strip():
        errors.append(f"{where}: an entry needs a label")
        return
    where = f"{where}, '{e['label']}'"
    if "bounds" in e:
        b = e["bounds"]
        if not (isinstance(b, list) and len(b) == 2 and all(map(_number, b)) and b[0] <= b[1]):
            errors.append(f"{where}: bounds must be two numbers, the lower first")
        if "value" in e:
            errors.append(f"{where}: give bounds or a value, not both")
        return
    if not identified:
        errors.append(f"{where}: the quantity is not identified, so give its bounds, not one number")
        return
    if not _number(e.get("value")):
        errors.append(f"{where}: a value must be a finite number")
        return
    if e.get("exact") is True:
        if not isinstance(e.get("basis"), str) or not e["basis"].strip():
            errors.append(f"{where}: a value given without an interval must say on what basis it is exact")
        return
    i = e.get("interval")
    if not (isinstance(i, list) and len(i) == 2 and all(map(_number, i))):
        errors.append(f"{where}: an estimated value needs its interval, as [lower, upper]")
    elif not i[0] <= e["value"] <= i[1]:
        errors.append(f"{where}: the value lies outside its interval")


def _results(data, errors):
    if not isinstance(data, dict):
        errors.append("results: must be an object with one entry per field")
        return
    for name in RESULTS:
        r = data.get(name)
        where = f"results, '{name}'"
        if r is None:
            errors.append(f"{where}: missing; if it is not reported, say why with 'not_reported'")
        elif not isinstance(r, dict) or len({"text", "entries", "not_reported"} & set(r)) != 1:
            errors.append(f"{where}: give exactly one of 'text', 'entries' or 'not_reported'")
        elif "text" in r or "not_reported" in r:
            value = r.get("text", r.get("not_reported"))
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{where}: the text or the reason is empty")
        else:
            if not isinstance(r.get("identified"), bool):
                errors.append(f"{where}: say whether the quantity is identified ('identified': true or false)")
            if not isinstance(r.get("assumptions"), str) or not r["assumptions"].strip():
                errors.append(f"{where}: say what the result assumes ('assumptions')")
            if not isinstance(r["entries"], list) or not r["entries"]:
                errors.append(f"{where}: 'entries' must be a non-empty list")
            else:
                for e in r["entries"]:
                    _entry(where, e, r.get("identified", True), errors)
    for name in sorted(set(data) - set(RESULTS)):
        errors.append(f"results: '{name}' is not a field of the standard")


def validate(report):
    """The list of the ways `report` (a dict) breaks the standard; empty if it keeps it."""
    errors = []
    if not isinstance(report, dict):
        return ["a report must be an object"]
    for key in sorted(TOP - set(report)):
        errors.append(f"the report has no '{key}'")
    for key in sorted(set(report) - TOP):
        errors.append(f"'{key}' is not part of a report")
    for key in ("declared_before_data", "confirmatory"):
        if key in report and not isinstance(report[key], bool):
            errors.append(f"'{key}' must be true or false")
    if report.get("confirmatory") is True and report.get("declared_before_data") is not True:
        errors.append("a report whose declaration came after its data were seen cannot be confirmatory")
    _texts("declaration", DECLARATION, report.get("declaration", {}), errors)
    _texts("observations", OBSERVATIONS, report.get("observations", {}), errors)
    _results(report.get("results", {}), errors)
    return errors


def load(path):
    """Read a report from a JSON file."""
    return json.loads(Path(path).read_text(encoding="utf-8"))
