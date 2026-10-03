"""Case C2, exploratory: computed after the verdicts of run.py, not registered. It explains S3's failure, and splits
arm A's.

1. S3 again on a grid of step 0.001: the recovery of single-peaked instances, and the instances with several peaks.
2. Arm A again, same seeds and code, scored four ways (RESULTS.md, table of S1).
Usage: python3 cases/c2-stopping-rule/explore.py   (needs output.json from run.py)
"""
import json
from pathlib import Path
import numpy as np
import run as R

HERE = Path(__file__).resolve().parent
FINE = np.round(0.001 * np.arange(0, 20001), 3)


def local_maxima(values):
    return [i for i in range(1, len(values) - 1) if values[i] >= values[i - 1] and values[i] > values[i + 1]]


def main():
    qual = [r for r in json.loads((HERE / "output.json").read_text())["instances"] if r["qualifies"]]
    single, multi = [], []
    for r in qual:
        q, F, Fh = R.instance(r["instance"])
        p = R.tilt(q, FINE[:, None] * Fh)
        values, cov = p @ F, (p * Fh * F).sum(1) - (p @ Fh) * (p @ F)
        rec = R.recovery(values, R.rule(cov[1:]))
        (single if len(local_maxima(values)) == 1 else multi).append(rec)
    print(f"S3 on a grid of 0.001: {len(single)} single-peaked, minimum recovery {min(single):.5f}; "
          f"{len(multi)} with several peaks, recoveries {sorted(round(x, 3) for x in multi)}")
    t_peak = np.array([r["t_peak"] for r in qual])
    print(f"t_peak: median {np.median(t_peak):.2f}, share below 0.5 {np.mean(t_peak < 0.5):.2f}")
    grid = np.r_[0.0, R.GRID_A]
    rows = []
    for r in qual:
        k = r["instance"]; q, F, Fh = R.instance(k)
        rng = np.random.default_rng(6000 + k)
        theta = np.tile(np.log(q), (len(R.GRID_A), 1)); beta = (1 / R.GRID_A)[:, None]
        for _ in range(R.STEPS_A):
            p = R.softmax(theta); log_ratio = np.log(p / q); kl = (p * log_ratio).sum(1, keepdims=True)
            theta += R.LR * (R.reinforce(p, Fh, rng) - beta * p * (log_ratio - kl))
        p = R.softmax(theta); est = R.estimated_cov(p, F, Fh, rng)
        exact = (p * Fh * F).sum(1) - (p @ Fh) * (p @ F)
        trained = np.r_[q @ F, p @ F]
        pg = R.tilt(q, grid[:, None] * Fh)
        optima = pg @ F
        optima_cov = (pg * Fh * F).sum(1) - (pg @ Fh) * (pg @ F)
        rows.append({"late": r["t_peak"] >= 1, "registered": R.recovery(trained, R.rule(est)),
                     "exact_cov": R.recovery(trained, R.rule(exact)), "on_optima": R.recovery(optima, R.rule(est)),
                     "exact_pursuit": R.recovery(optima, R.rule(optima_cov[1:])),
                     "scatter": float(np.median(np.abs(trained[1:] - optima[1:]))),
                     "gain": float(optima.max() - optima[0])})
    for label, keep in [("all", lambda x: True), ("t_peak >= 1", lambda x: x["late"])]:
        sel = [x for x in rows if keep(x)]
        keys = ["registered", "exact_cov", "on_optima", "exact_pursuit"]
        shares = {key: np.mean([x[key] >= 0.9 for x in sel]) for key in keys}
        print(f"arm A, {label} (n={len(sel)}): " + ", ".join(f"{k} {v:.2f}" for k, v in shares.items()))
    print(f"median scatter of a trained policy's gold from its optimum {np.median([x['scatter'] for x in rows]):.3f}; "
          f"median best gain {np.median([x['gain'] for x in rows]):.3f}")


if __name__ == "__main__":
    main()
