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
    assert m["certified"][1] - m["certified"][0] < 1e-6
    iface = rep["interface"]
    assert iface["wrong_answers"]["unavoidable"] < 1e-9
    assert iface["wrong_answers"]["culpable_at_margin"]
    assert iface["leaks"]["culpable_at_any_margin"]
