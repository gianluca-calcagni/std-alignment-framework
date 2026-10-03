"""Case W3, exploratory: computed after the verdicts of run.py, not registered. The registered R² pools, within each
prompt, 32 continuations of the reference and 32 of the tuned model, which differ in both the revealed objective and the
reward; this recomputes S1's and S2's statistics within each model's own continuations, with the same resampling.

Reads the per-context rows that run.py saved outside the repository (W3_SCRATCH). Usage: python3 explore.py   (writes
explore.json next to this file, aggregates only)
"""
import json, pickle
from pathlib import Path
import numpy as np
import run as R


def sums(rows, sel, key):
    """Per-context residual and total sums of squares of z on rows[key], over the continuations `sel`."""
    ssr, sst = [], []
    for w in rows:
        _, a, b = R.fit(w["z"][sel], w[key][sel])
        ssr.append(a); sst.append(b)
    return np.array(ssr), np.array(sst)


def main():
    rows = pickle.loads((R.SCRATCH / "w3_rows.pkl").read_bytes())
    rng = np.random.default_rng(R.SEED)
    idx = [rng.integers(0, len(rows), len(rows)) for _ in range(R.BOOT)]
    out = {}
    for name, sel in [("reference", slice(0, R.K)), ("tuned", slice(R.K, 2 * R.K)), ("both", slice(0, 2 * R.K))]:
        a, sst = sums(rows, sel, "r")
        b, _ = sums(rows, sel, "p")
        r2 = lambda ssr, i: 1 - ssr[i].sum() / sst[i].sum()
        boots = np.array([(r2(a, i), r2(a, i) - r2(b, i)) for i in idx])
        out[name] = {"R2_r": r2(a, slice(None)), "R2_p": r2(b, slice(None)),
                     "R2_r_interval_95": [float(x) for x in np.percentile(boots[:, 0], [2.5, 97.5])],
                     "difference": r2(a, slice(None)) - r2(b, slice(None)),
                     "difference_interval_95": [float(x) for x in np.percentile(boots[:, 1], [2.5, 97.5])]}
    out["z_gap_tuned_minus_reference"] = float(np.mean([w["z"][R.K:].mean() - w["z"][:R.K].mean() for w in rows]))
    out["r_gap_tuned_minus_reference"] = float(np.mean([w["r"][R.K:].mean() - w["r"][:R.K].mean() for w in rows]))
    (R.HERE / "explore.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
