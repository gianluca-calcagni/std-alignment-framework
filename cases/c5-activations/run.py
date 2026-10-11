"""C5's test: exactly what REGISTRATION.md says, on the test's seeds, with the thresholds of rehearsal.json.
Usage: python3 cases/c5-activations/run.py, from the repository's root. Per-instance rows go outside the repository
(CASE_SCRATCH); the aggregates and verdicts go to output.json."""
import json, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / "tools"))
import net                                                                          # noqa: E402
from casekit import save_rows, write_record                                         # noqa: E402

N = 200
SEEDS = {"linear": 50000, "xor": 60000}
AT_LEAST = 192                                       # of 200: the rehearsal's 200 of 200, by the rule of three, less 3 SE


def main():
    sigma = json.loads((HERE / "rehearsal.json").read_text())["sigma"]
    rows = {s: [net.measure(SEEDS[s] + k, s) for k in range(N)] for s in SEEDS}
    save_rows(rows, "c5-test")
    tol = lambda v: 1e-12 * (1 + abs(v))
    out = {"sigma": sigma, "instances_per_arm": N, "seeds": SEEDS, "at_least": AT_LEAST, "verdicts": {}, "numbers": {}}
    v, num = out["verdicts"], out["numbers"]
    allr = rows["linear"] + rows["xor"]
    n_v1 = sum(r["kl_behaviour"] <= r["kl_view"] + tol(r["kl_view"]) and r["kl_view"] <= r["kl_input"] + tol(r["kl_input"])
               for r in allr)
    n_v2 = sum(r["F_use"] >= r["bound_true"] - 1e-12 for r in allr)
    num["V1"], num["V2"] = n_v1, n_v2
    v["V1"], v["V2"] = n_v1 == 2 * N, n_v2 == 2 * N
    eps = lambda s, k: np.array([r[f"eps_{k}"] for r in rows[s]])
    thr = lambda s, k: 3 * sigma[f"{s}/{k}"]
    num["S1"] = int(np.sum(eps("linear", "linear") > thr("linear", "linear")))
    num["S2"] = int(np.sum(eps("xor", "linear") <= thr("xor", "linear")))
    num["S3"] = int(sum(r["F_use"] < r["bound_linear"] - 1e-12 for r in rows["xor"]))
    num["S4"] = int(np.sum(eps("xor", "quadratic") > thr("xor", "quadratic")))
    num["S6"] = int(sum(r["F_use"] >= r["bound_linear"] - 1e-12 for r in rows["linear"]))
    for k in ("S1", "S2", "S3", "S4", "S6"):
        v[k] = num[k] >= AT_LEAST
    s5 = {}
    for s in SEEDS:
        for k in ("linear", "quadratic"):
            d = eps(s, k) - np.array([r["kl_view"] for r in rows[s]])
            m, se = float(d.mean()), float(d.std(ddof=1) / np.sqrt(N))
            s5[f"{s}/{k}"] = {"mean": m, "se": se, "held": m <= 2 * se}
    num["S5"] = s5; v["S5"] = all(x["held"] for x in s5.values())
    num["kl_view"] = sorted({round(r["kl_view"], 12) for r in allr})
    num["gap_min"] = float(min(r["F_eval"] - r["F_use"] for r in allr))
    for s in SEEDS:
        for k in ("linear", "quadratic"):
            e = eps(s, k); num[f"eps {s}/{k}: min, mean, max"] = [float(e.min()), float(e.mean()), float(e.max())]
    write_record(HERE / "output.json", out)
    for k in ("V1", "V2", "S1", "S2", "S3", "S4", "S5", "S6"):
        print(k, "held" if v[k] else "FAILED", num[k] if k != "S5" else s5)


if __name__ == "__main__":
    main()
