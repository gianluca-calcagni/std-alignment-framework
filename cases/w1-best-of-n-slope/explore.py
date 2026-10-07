"""Case W1, exploratory: computed after the verdict of run.py, not registered. Does the refutation come from ties?

The proxy scores identical answers alike, and many prompts repeat answers. Then best-of-n's KL is below the formula
log n - (n - 1)/n that the registered axis uses, and the curve is drawn against too large a `d`. This script recomputes
each prompt's curve as run.py does, keeps them, and compares D on prompts without ties and with ties, and against the
exact KL of best-of-n for each prompt, computed from the tied blocks.
Usage: python3 explore.py <folder holding validation/split_*.json>   (writes explore.json)
"""
import json, sys
from pathlib import Path
import numpy as np
import run as R
from train_proxy import features


def exact_kl(blocks, n):
    """KL(best-of-n || q) for one prompt whose sorted proxy scores form tied blocks of the given sizes, ties broken at
    random: each block's probability under best-of-n is (Q^n - Q_-^n), spread evenly over the block."""
    Q = np.cumsum(blocks) / R.N
    Qm = np.r_[0.0, Q[:-1]]
    mass = Q ** n - Qm ** n
    q = blocks / R.N
    keep = mass > 0
    return float(np.sum(mass[keep] * np.log(mass[keep] / q[keep])))


def main(folder):
    weights = np.load(R.HERE / "proxy.npz")["weights"]
    curves, c, tied, kls, k = [], [], [], [], 0
    for j in range(1, 11):
        for rec in json.loads((Path(folder) / "validation" / f"split_{j}.json").read_text()):
            F = np.asarray(rec["gold_scores"], dtype=float)
            r = features(rec["answers"]) @ weights
            perm = np.random.default_rng(R.SEED + k).permutation(R.N)
            order = perm[np.argsort(r[perm], kind="stable")]
            Fs = F[order]
            c.append(float(np.mean(R.G * (Fs - Fs.mean())) / R.SG)); curves.append(R.W @ Fs)
            _, blocks = np.unique(np.sort(r), return_counts=True)
            tied.append(float(np.sum(blocks[blocks > 1]) / R.N))
            kls.append([exact_kl(blocks, n) for n in R.GRID])
            k += 1
        print(f"split_{j}", flush=True)
    curves, c, tied, kls = np.array(curves), np.array(c), np.array(tied), np.array(kls)

    def D_of(sel, use_exact=False):
        g = curves[sel].mean(0)
        if use_exact:          # fit against the mean exact d of the selected prompts
            d = np.sqrt(kls[sel].mean(0))
            A = np.c_[d[1:], -d[1:] ** 2]
            a = np.linalg.lstsq(A, g[1:] - g[0], rcond=None)[0][0]
        else:
            a = R.fit(g)[0]
        return float(a - np.sqrt(2) * c[sel].mean()), float(a), float(np.sqrt(2) * c[sel].mean())

    groups = {"all": np.ones(len(c), bool), "no ties": tied == 0, "ties under 10%": (tied > 0) & (tied < 0.1),
              "ties 10% or more": tied >= 0.1}
    out = {}
    for name, sel in groups.items():
        out[name] = {"prompts": int(sel.sum()), "D_formula_axis": D_of(sel), "D_exact_axis": D_of(sel, True)}
        print(name, out[name], flush=True)
    out["share_of_answers_tied_median"] = float(np.median(tied))
    (R.HERE / "explore.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
