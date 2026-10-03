"""W4's estimates for one context, from the pooled draws of three behaviours whose log-probabilities are all known:
A (the run judged), B (the other run) and R (the reference, the default). Pure numpy, so that the rehearsal tests
exactly the code the run uses.

Inputs, one entry per pooled draw: src (0 for A's draws, 1 for B's, 2 for R's, the same number of each), lA, lB, lR
(log-probabilities under A, B and R), fA (the reward A was tuned on) and fB (the reward B was tuned on).

Averages under A and B come from their own draws, with no reweighting. Averages under a tilt of R are estimated by
reweighting the pooled draws, whose density is the mixture m = (A + B + R)/3: E_R[g] = E_m[(R/m)·g] ([P47] gives the
cost). Within this estimate, the tilts of R by c·Φ form an exponential family on the pooled draws, so the named
pursuits of [P44] are found by Newton's method on its convex dual.
"""
import numpy as np
from scipy.special import logsumexp

TOL = 1e-12


def family(base, Phi, c):
    """log Z(c) = log of the average of exp(base + c·Phi), and the normalized weights of the tilt."""
    s = base + c @ Phi
    lz = logsumexp(s) - np.log(s.size)
    w = np.exp(s - logsumexp(s))
    return lz, w


def match(base, Phi, target, iters=200):
    """The coefficients c of the tilt of R whose averages of Phi equal target, with log Z, the weights, and the largest
    moment error left. Each row of Phi is first centred and scaled over the pooled draws, so that a named objective with
    extreme values (a log-probability far below the rest) does not overflow; a row that does not vary gets coefficient
    0. The coefficients are returned for the rows as given."""
    mu, sd = Phi.mean(1), Phi.std(1)
    keep = sd > TOL * (1 + np.abs(mu))
    cs, lz, w, err = _match((Phi[keep] - mu[keep, None]) / sd[keep, None], base, (target[keep] - mu[keep]) / sd[keep], iters)
    c = np.zeros(Phi.shape[0]); c[keep] = cs / sd[keep]
    return c, lz + float(c @ mu), w, float(np.max(np.abs(Phi @ w - target)))


def _match(Phi, base, target, iters):
    """Damped Newton on the convex dual log Z(c) − c·target, for rows of comparable scale."""
    c = np.zeros(Phi.shape[0])
    if c.size == 0:
        lz, w = family(base, np.zeros((1, base.size)), np.zeros(1))
        return c, lz, w, 0.0
    dual = lambda c: family(base, Phi, c)[0] - c @ target
    for _ in range(iters):
        lz, w = family(base, Phi, c)
        mean = Phi @ w
        g = mean - target
        if np.max(np.abs(g)) < 1e-11:
            break
        H = (Phi * w) @ Phi.T - np.outer(mean, mean)
        step = np.linalg.lstsq(H + 1e-12 * np.eye(len(c)), g, rcond=None)[0]
        lam, d0 = 1.0, dual(c)
        while dual(c - lam * step) > d0 + 1e-14 and lam > 1e-10:
            lam /= 2
        c = c - lam * step
    lz, w = family(base, Phi, c)
    return c, lz, w, float(np.max(np.abs(Phi @ w - target)))


def ray(base, f, target):
    """The revealed intensity t* >= 0 of a behaviour whose average of f is target ([P5](iv)), on the pooled draws:
    0 if target does not exceed R's average, inf if it reaches the largest value drawn, else the matching tilt."""
    if np.ptp(f) <= TOL:
        return 0.0, family(base, f[None], np.zeros(1))[0]
    lz0, w0 = family(base, f[None], np.zeros(1))
    if target <= f @ w0:
        return 0.0, lz0
    if target >= f.max() - TOL * (1 + abs(f.max())):
        return float("inf"), float("nan")
    c, lz, _, _ = match(base, f[None], np.array([target]))
    return float(c[0]), lz


def misalignment_parts(base, own, l_own, lR, f, named):
    """For the behaviour whose own draws are flagged by own: its departure, revealed intensity and misalignment under
    the standard specification of f ([P6]); then, for each prefix of the named objectives, the named pursuit's
    coefficients and the unexplained and named misalignments ([P44](ii), (iii)), with the effective number of draws
    behind each named pursuit ([P47])."""
    dep = float(np.mean(l_own[own] - lR[own]))
    target_f = float(np.mean(f[own]))
    t, lz = ray(base, f, target_f)
    out = {"departure": dep, "t_star": t, "M": float("nan"), "named": []}
    if not np.isfinite(t):
        return out
    out["M"] = dep - (t * target_f - lz)
    for k in range(1, len(named) + 1):
        Phi = np.vstack([f] + named[:k])
        target = Phi[:, own].mean(1)
        c, lz, w, err = match(base, Phi, target)
        unexplained = float(np.mean(l_own[own] - lR[own] - c @ Phi[:, own]) + lz)
        out["named"].append({"coef": [float(x) for x in c], "unexplained": unexplained,
                             "named": out["M"] - unexplained, "moment_error": err,
                             "effective_draws": float(1.0 / np.sum(w ** 2))})
    return out


def context_estimates(src, lA, lB, lR, fA, fB):
    """Every W4 quantity for one context: departures, divergences between the runs, the drift of [P45] for two runs,
    and the parts of each run's misalignment against its own reward, naming in turn the reference's log-probability
    (sharpening), the other run's reward and the other run's revealed objective."""
    src, lA, lB, lR, fA, fB = (np.asarray(x, float) for x in (src, lA, lB, lR, fA, fB))
    a, b = src == 0, src == 1
    lm = logsumexp(np.vstack([lA, lB, lR]), axis=0) - np.log(3)
    base = lR - lm                                                                 # log of the weights R/m
    l2 = np.logaddexp(lA, lB) - np.log(2)
    out = {
        "kl_A_B": float(np.mean(lA[a] - lB[a])), "kl_B_A": float(np.mean(lB[b] - lA[b])),
        "drift": float(0.5 * np.mean(lA[a] - l2[a]) + 0.5 * np.mean(lB[b] - l2[b])),
        "A": misalignment_parts(base, a, lA, lR, fA, [lR, fB, lB - lR]),
        "B": misalignment_parts(base, b, lB, lR, fB, [lR, fA, lA - lR]),
        "flat_reward": bool(np.ptp(fA) <= TOL or np.ptp(fB) <= TOL),
        "repeated_draws": int(len(lR) - len(np.unique(np.round(np.vstack([lA, lB, lR]), 12), axis=1).T)),
    }
    return out
