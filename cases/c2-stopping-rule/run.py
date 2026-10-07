"""Case C2: does the stopping rule survive practical training? Computes exactly what REGISTRATION.md says.

Not part of CI. Usage: python3 cases/c2-stopping-rule/run.py   (writes output.json next to this file)
"""
import json, time
from pathlib import Path
import numpy as np

N_OUT, INSTANCES, HACKS = 30, 200, 3
GRID_A = 0.25 * np.arange(1, 33)
GRID_C = np.round(0.05 * np.arange(0, 401), 2)
GRID_Q = np.round(0.01 * np.arange(0, 2001), 2)
STEPS_A, STEPS_B, LR, BATCH, EVERY, REVIEW = 4000, 3000, 0.5, 64, 25, 1000


def softmax(theta):
    w = np.exp(theta - theta.max(axis=-1, keepdims=True))
    return w / w.sum(axis=-1, keepdims=True)


def tilt(q, F):
    return softmax(np.log(q) + F)


def instance(k):
    r = np.random.default_rng(5000 + k)
    q = r.dirichlet(np.ones(N_OUT))
    q = np.maximum(q, 1e-3); q /= q.sum()
    F = r.standard_normal(N_OUT)
    Fh = F + 0.5 * r.standard_normal(N_OUT)
    h = r.choice(N_OUT, HACKS, replace=False)
    Fh[h] += 2.5; F[h] -= 1.5
    return q, F, Fh


def qualifies(q, F, Fh):
    curve = tilt(q, GRID_Q[:, None] * Fh) @ F
    j = int(np.argmax(curve))
    gain = curve[j] - curve[0]
    return bool(0 < GRID_Q[j] < 20 and gain > 0 and curve[j] - curve[-1] >= 0.05 * gain), float(GRID_Q[j])


def sample(p, n, r):
    """n draws from each row of p (rows, outcomes), by inverse transform."""
    p = np.atleast_2d(p)
    rows = p.shape[0]
    cdf = np.cumsum(p, axis=1); cdf[:, -1] = 1.0
    u = r.random((rows, n))
    offset = np.arange(rows)[:, None]
    idx = np.searchsorted((cdf + offset).ravel(), (u + offset).ravel(), side="right").reshape(rows, n)
    return np.minimum(idx - offset * N_OUT, N_OUT - 1)


def reinforce(p, Fh, r):
    """The REINFORCE estimate of the gradient of E_p[Fh] in the logits, minibatch mean as baseline, for each row."""
    rows = p.shape[0]
    x = sample(p, BATCH, r)
    adv = Fh[x] - Fh[x].mean(axis=1, keepdims=True)
    flat = (np.arange(rows)[:, None] * N_OUT + x).ravel()
    g = np.bincount(flat, weights=adv.ravel(), minlength=rows * N_OUT).reshape(rows, N_OUT) / BATCH
    return g - p * adv.mean(axis=1, keepdims=True)


def estimated_cov(p, F, Fh, r):
    x = sample(p, REVIEW, r)
    return np.array([np.cov(Fh[row], F[row])[0, 1] for row in x])


def rule(covs):
    """Index of the kept point among points 0 (untuned), 1, ..., n, given the covariances at points 1..n."""
    nonpositive = np.flatnonzero(covs <= 0)
    if len(nonpositive) == 0:
        return len(covs)
    return int(nonpositive[0])            # point i+1 is the first non-positive one, so keep point i


def recovery(values, kept):
    gain = values.max() - values[0]
    return float((values[kept] - values[0]) / gain) if gain > 0 else float("nan")


def arm_a(q, F, Fh, k):
    r = np.random.default_rng(6000 + k)
    theta = np.tile(np.log(q), (len(GRID_A), 1))
    beta = (1 / GRID_A)[:, None]
    for _ in range(STEPS_A):
        p = softmax(theta)
        log_ratio = np.log(p / q)
        kl = (p * log_ratio).sum(axis=1, keepdims=True)
        theta += LR * (reinforce(p, Fh, r) - beta * p * (log_ratio - kl))
    p = softmax(theta)
    covs = estimated_cov(p, F, Fh, r)
    values = np.r_[q @ F, p @ F]
    optimum = tilt(q, GRID_A[:, None] * Fh)
    gap = (p * np.log(p / optimum)).sum(axis=1)
    kept = rule(covs)
    exact_peak = int(np.argmax(values))
    return {"recovery": recovery(values, kept), "kept": kept, "best": exact_peak,
            "kl_to_optimum_max": float(gap.max()), "kl_to_optimum_median": float(np.median(gap))}


def arm_b(q, F, Fh, k):
    r = np.random.default_rng(7000 + k)
    theta = np.log(q)[None, :].copy()
    values, covs = [float(q @ F)], []
    for step in range(1, STEPS_B + 1):
        p = softmax(theta)
        theta += LR * reinforce(p, Fh, r)
        if step % EVERY == 0:
            p = softmax(theta)
            values.append(float(p[0] @ F))
            covs.append(estimated_cov(p, F, Fh, r)[0])
    values, covs = np.array(values), np.array(covs)
    kept = rule(covs)
    return {"recovery": recovery(values, kept), "kept_step": kept * EVERY, "best_step": int(np.argmax(values)) * EVERY}


def arm_c(q, F, Fh):
    p = tilt(q, GRID_C[:, None] * Fh)
    values = p @ F
    covs = (p * Fh * F).sum(1) - (p @ Fh) * (p @ F)
    kept = rule(covs[1:])
    return {"recovery": recovery(values, kept), "kept_t": float(GRID_C[kept]), "best_t": float(GRID_C[np.argmax(values)])}


def main():
    start, rows = time.time(), []
    for k in range(1, INSTANCES + 1):
        q, F, Fh = instance(k)
        ok, t_peak = qualifies(q, F, Fh)
        row = {"instance": k, "qualifies": ok, "t_peak": t_peak}
        if ok:
            row["A"], row["B"], row["C"] = arm_a(q, F, Fh, k), arm_b(q, F, Fh, k), arm_c(q, F, Fh)
        rows.append(row)
        if k % 20 == 0:
            print(f"{k} instances, {time.time() - start:.0f}s", flush=True)
    qual = [r for r in rows if r["qualifies"]]
    rec = {arm: np.array([r[arm]["recovery"] for r in qual]) for arm in "ABC"}
    share = lambda x, a: float(np.mean(x >= a))
    verdicts = {
        "qualifying": len(qual),
        "S1": {"share_at_least_0.9": share(rec["A"], 0.9), "held": share(rec["A"], 0.9) >= 0.9},
        "S2": {"share_at_least_0.8": share(rec["B"], 0.8), "held": share(rec["B"], 0.8) >= 0.8},
        "S3": {"min_recovery": float(np.nanmin(rec["C"])), "held": bool(np.all(rec["C"] >= 0.999))},
    }
    summary = {arm: {"median": float(np.nanmedian(rec[arm])), "p10": float(np.nanpercentile(rec[arm], 10)),
                     "min": float(np.nanmin(rec[arm])), "nan": int(np.isnan(rec[arm]).sum())} for arm in "ABC"}
    summary["A"]["early"] = int(sum(r["A"]["kept"] < r["A"]["best"] for r in qual))
    summary["A"]["late"] = int(sum(r["A"]["kept"] > r["A"]["best"] for r in qual))
    summary["A"]["kl_to_optimum_max"] = float(max(r["A"]["kl_to_optimum_max"] for r in qual))
    summary["A"]["kl_to_optimum_median"] = float(np.median([r["A"]["kl_to_optimum_median"] for r in qual]))
    summary["B"]["early"] = int(sum(r["B"]["kept_step"] < r["B"]["best_step"] for r in qual))
    summary["B"]["late"] = int(sum(r["B"]["kept_step"] > r["B"]["best_step"] for r in qual))
    out = {"verdicts": verdicts, "summary": summary, "instances": rows}
    Path(__file__).with_name("output.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({"verdicts": verdicts, "summary": summary}, indent=1))


if __name__ == "__main__":
    main()
