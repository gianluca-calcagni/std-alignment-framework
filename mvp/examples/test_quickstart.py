"""CI runs the MVP's quickstart: it must finish, keep its declaration, and reach the verdicts its simulated truth
implies."""
import importlib.util
from pathlib import Path


def load():
    spec = importlib.util.spec_from_file_location("quickstart", Path(__file__).with_name("quickstart.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_quickstart_runs_and_reaches_its_verdicts():
    q = load()
    rep = q.run(seed=0)
    assert rep["declaration"]["alpha"] == 0.05
    assert rep["forbidden"]["verdict"] == "convicted"
    lo, hi = rep["pooled_wrong_rate"]["interval"]
    assert lo <= rep["pooled_wrong_rate"]["true_average"] <= hi
    assert rep["pooled_wrong_rate"]["verdict"] == "convict"
    m = rep["misalignment_outside_forbidden"]
    assert m["bounds"][1] - m["bounds"][0] < 1e-6
    iface = rep["interface"]
    assert iface["wrong_answers"]["unavoidable"] < 1e-9
    assert iface["wrong_answers"]["culpable_at_margin"]
    assert iface["wrong_answers"]["plug_in_culpable_at_margin"]
    assert abs(iface["wrong_answers"]["plug_in_excess"] - iface["wrong_answers"]["avoidable_excess"]) < 0.05
    assert iface["leaks"]["deployed"] == "infinite"
    assert iface["leaks"]["culpable_at_any_margin"]


def test_readme_example_runs_as_written():
    import re
    from pathlib import Path
    text = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
    code = re.search(r"```python\n(.*?)```", text, re.S).group(1)
    scope = {}
    exec(code, scope)
    assert round(scope["m"].value, 4) == 0.0413
    assert scope["verdict"] == "convict"
