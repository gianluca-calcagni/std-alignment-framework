"""C5's rehearsal: the same pipeline as run.py, on seeds the test does not use. It calibrates the probes' noise on null
instances, where the two conditions are the same, measures every statistic of the predictions on rehearsal instances,
runs the degenerate cases, and times an instance. Writes rehearsal.json; per-instance rows go outside the repository.
Usage: python3 cases/c5-activations/rehearse.py, from the repository's root."""
import sys, time
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / "tools"))
import net                                                                          # noqa: E402
from casekit import save_rows, write_record                                         # noqa: E402

N = 200
SEEDS = {"null-linear": 1000, "null-xor": 2000, "linear": 3000, "xor": 4000}        # the test uses 50000 and 60000


def arm(name):
    structure = name.replace("null-", "")
    p_cue = (0.5, 0.5) if name.startswith("null") else (0.7, 0.3)
    return [net.measure(SEEDS[name] + k, structure, p_cue=p_cue) for k in range(N)]


def main():
    t0 = time.time(); rows = {name: arm(name) for name in SEEDS}; seconds = (time.time() - t0) / (len(SEEDS) * N)
    save_rows(rows, "c5-rehearsal")
    rec = {"instances_per_arm": N, "seeds": SEEDS, "seconds_per_instance": seconds}
    sig = {}
    for s in ("linear", "xor"):                                                     # the noise, from the nulls
        for kind in ("linear", "quadratic"):
            e = np.array([r[f"eps_{kind}"] for r in rows[f"null-{s}"]])
            sig[f"{s}/{kind}"] = float(e.std(ddof=1))
            rec.setdefault("null", {})[f"{s}/{kind}"] = {
                "sd": float(e.std(ddof=1)), "mean": float(e.mean()),
                "rate_at_most_3sd": float(np.mean(e <= 3 * e.std(ddof=1)))}
    rec["sigma"] = sig
    for s in ("linear", "xor"):                                                     # the statistics of the predictions
        R = rows[s]; t = {}
        tol = lambda v: 1e-12 * (1 + abs(v))
        t["V1_holds"] = int(sum(r["kl_behaviour"] <= r["kl_view"] + tol(r["kl_view"]) and
                               r["kl_view"] <= r["kl_input"] + tol(r["kl_input"]) for r in R))
        t["V2_holds"] = int(sum(r["F_use"] >= r["bound_true"] - 1e-12 for r in R))
        t["kl_view"] = sorted({round(r["kl_view"], 12) for r in R})
        t["gap_min"] = float(min(r["F_eval"] - r["F_use"] for r in R))
        t["bound_at_3sd_above_F_use"] = int(sum(net.lower_bound(np.array(r["p_eval"]), 3 * sig[f"{s}/linear"]) > r["F_use"]
                                               for r in R))
        for kind in ("linear", "quadratic"):
            e = np.array([r[f"eps_{kind}"] for r in R]); thr = 3 * sig[f"{s}/{kind}"]
            t[f"{kind}: eps sd"] = float(e.std(ddof=1))
            t[f"{kind}: declared (eps > 3 sd)"] = int(np.sum(e > thr))
            t[f"{kind}: eps min, mean, max"] = [float(e.min()), float(e.mean()), float(e.max())]
            d = e - np.array([r["kl_view"] for r in R])
            t[f"{kind}: eps - truth, mean and se"] = [float(d.mean()), float(d.std(ddof=1) / np.sqrt(len(d)))]
            t[f"{kind}: bound fails"] = int(sum(r["F_use"] < r[f"bound_{kind}"] - 1e-12 for r in R))
        rec[s] = t
    deg = {}                                                                        # the degenerate cases
    r = net.measure(7, "linear", p_cue=(1.0, 0.0)); deg["conditions with no common cue: kl_view"] = r["kl_view"]
    deg["... its bound, the least F"] = r["bound_true"]; deg["... probe finite"] = bool(np.isfinite(r["eps_linear"]))
    inst = net.Instance(8, "linear", 0.7, 0.3); inst.H[:, 2:] = 0                   # units that never fire
    acts = {c: inst.H[inst.rng.choice(64, size=1000, p=w / w.sum())] for c, w in inst.W.items()}
    deg["constant units: probe finite"] = bool(np.isfinite(net.probe_divergence(acts, "quadratic", 500)))
    pa = np.array([0.5, 0.2, 0.3])
    deg["eps 0: bound is E[F]"] = net.lower_bound(pa, 0.0) == float(pa @ net.F)
    deg["eps negative: bound is E[F]"] = net.lower_bound(pa, -0.01) == float(pa @ net.F)
    deg["eps beyond -log p(bad): bound is min F"] = net.lower_bound(pa, -np.log(0.2) + 1e-9) == -1.0
    rec["degenerate_cases"] = deg
    write_record(HERE / "rehearsal.json", rec)
    print(f"{seconds:.3f} s per instance; sigma {sig}")
    for s in ("linear", "xor"):
        print(s, rec[s])


if __name__ == "__main__":
    main()
