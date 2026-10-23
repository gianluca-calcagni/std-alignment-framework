"""The MVP's quantities (`mvp/CORE.md`): misalignment against a declared specification, its bets and tests, the
certificate for an average, and the splits along the record's resolution and along what the actor could do.

Outcomes are finite and indexed 0..n-1. A behaviour is an array of n masses. The world's part (D1) is given as
`world`, an array of n condition labels, or None when the world chooses nothing. A per-decision requirement is a list of
`Limit`s, linear limits on averages (R6): E_a[g · 1_cell] ≤ b · a(cell), where `cell` is a condition label, or None for
the whole outcome space. Since the behaviours compared share the actor's law on the conditions (D5), a limit inside a
condition is linear in a. Misalignment is computed by convex optimization and returned with a certified interval: the
upper end is the divergence to a behaviour that meets the requirement, the lower end the growth of a bet that the
requirement calls fair (R2(i)), checked by a linear program.
"""
from dataclasses import dataclass, field
import numpy as np
from scipy.optimize import linprog, minimize, brentq, minimize_scalar

TOL = 1e-9          # feasibility tolerance of the linear programs and of the solver's constraints


# ----------------------------------------------------------------------------------------------- declarations (D4)

@dataclass(frozen=True)
class Limit:
    """E_a[g on `cell`] ≤ b · a(cell): a budget inside one condition, or on the whole outcome space when cell is None."""
    g: tuple
    b: float
    cell: object = None
    name: str = ""


def rate_limit(C, eps, n=None, cell=None, name=""):
    """At most a share `eps` of outcomes in C (an index list or a boolean mask), within `cell` if given (D4)."""
    mask = _mask(C, n)
    return Limit(tuple(mask.astype(float)), float(eps), cell, name or f"rate of {list(np.flatnonzero(mask))} ≤ {eps}")


def forbidden(C, n=None, cell=None, name=""):
    """Never an outcome in C (D4): a rate limit at zero."""
    return rate_limit(C, 0.0, n, cell, name or f"never {list(np.flatnonzero(_mask(C, n)))}")


def budget(g, b, cell=None, name=""):
    """E_a[g] ≤ b, within `cell` if given (D4)."""
    return Limit(tuple(np.asarray(g, float)), float(b), cell, name or "budget")


def no_worse_than(r, criteria, name=""):
    """E_a[G_j] ≥ E_r[G_j] for every criterion G_j (R9), as budgets on −G_j."""
    r = np.asarray(r, float)
    return [Limit(tuple(-np.asarray(G, float)), float(-r @ np.asarray(G, float)), None, name or f"criterion {j}")
            for j, G in enumerate(criteria)]


def _mask(C, n):
    C = np.asarray(C)
    if C.dtype == bool:
        return C
    if n is None:
        raise ValueError("give n, the number of outcomes, when C is a list of indices")
    m = np.zeros(n, bool)
    m[C] = True
    return m


# ------------------------------------------------------------------------------------------------------- basics

def kl(p, a):
    """KL(p‖a) on finite outcomes, natural logarithms, +∞ when a gives 0 where p does not."""
    p, a = np.asarray(p, float), np.asarray(a, float)
    s = p > 0
    if np.any(a[s] <= 0):
        return np.inf
    return float(np.sum(p[s] * np.log(p[s] / a[s])))


def kl_binary(u, v):
    """kl(u‖v) between (u, 1 − u) and (v, 1 − v)."""
    return kl(np.array([u, 1 - u]), np.array([v, 1 - v]))


def _cells(world, n):
    if world is None:
        return [np.arange(n)]
    world = np.asarray(world)
    return [np.flatnonzero(world == c) for c in dict.fromkeys(world.tolist())]


def _constraints(limits, p, world, n):
    """The linear constraints of a per-decision requirement on behaviours sharing p's law on the conditions."""
    A_ub, b_ub, A_eq, b_eq = [], [], [np.ones(n)], [1.0]
    labels = None if world is None else np.asarray(world)
    for lim in limits:
        g = np.asarray(lim.g, float)
        if lim.cell is None:
            A_ub.append(g)
            b_ub.append(lim.b)
        else:
            inside = labels == lim.cell
            A_ub.append(np.where(inside, g, 0.0))
            b_ub.append(lim.b * p[inside].sum())
    if world is not None:
        for idx in _cells(world, n):
            row = np.zeros(n)
            row[idx] = 1.0
            A_eq.append(row)
            b_eq.append(p[idx].sum())
    A_ub = np.array(A_ub).reshape(-1, n)
    return A_ub, np.array(b_ub, float), np.array(A_eq), np.array(b_eq, float)


# ------------------------------------------------------------------------------------------- misalignment (D5, D8)

@dataclass
class Misalignment:
    """M_A at a resolution, with a certified interval [lower, upper], the nearest acceptable behaviour found, and the
    best bet, constant on the resolution's cells (R2, R12). `value` is `upper`; `infinite` when no acceptable behaviour
    charges every cell that p charges; `consistent` False when no acceptable behaviour shares p's law at all."""
    value: float
    lower: float
    upper: float
    nearest: np.ndarray = field(repr=False)
    bet: np.ndarray = field(repr=False)
    infinite: bool = False
    consistent: bool = True


def misalignment(p, limits, world=None, cells=None):
    """M_A^𝒢(p) of D5 and D8: the least KL between p's and an acceptable behaviour's masses on the cells of `cells`
    (an array of n cell labels refining `world`; None for the finest partition), over the acceptable behaviours that
    share p's law on `world`.

    Computed as the growth of the best bet constant on the cells (R2, R12): maximize E_P[log k] over cell payoffs k
    whose largest cost under the requirement is at most 1, that cost written by linear-programming duality, so every
    point the solver visits is a bet and its growth a certified lower bound. The upper bound is the divergence to an
    acceptable behaviour recovered from the bet, by a linear program."""
    p = np.asarray(p, float)
    n = p.size
    A_ub, b_ub, A_eq, b_eq = _constraints(limits, p, world, n)
    groups = [np.arange(n)[[i]] for i in range(n)] if cells is None else _cells(cells, n)
    Gm = np.zeros((len(groups), n))
    for k, idx in enumerate(groups):
        Gm[k, idx] = 1.0
    P = Gm @ p
    S = P > 0
    nan = (np.full(n, np.nan), np.full(len(groups), np.nan))
    # the largest t such that every charged cell can get mass ≥ t: 0 means infinite misalignment; infeasible means
    # no acceptable behaviour shares p's law on the conditions
    c = np.zeros(n + 1)
    c[-1] = -1.0
    lp = linprog(c, A_ub=np.vstack([np.hstack([A_ub, np.zeros((A_ub.shape[0], 1))]),
                                     np.hstack([-Gm[S], np.ones((S.sum(), 1))])]),
                 b_ub=np.r_[b_ub, np.zeros(S.sum())], A_eq=np.hstack([A_eq, np.zeros((A_eq.shape[0], 1))]),
                 b_eq=b_eq, bounds=[(0, None)] * n + [(0, 1)], method="highs")
    if lp.status != 0:
        return Misalignment(np.inf, np.inf, np.inf, *nan, infinite=True, consistent=False)
    if lp.x[-1] <= TOL:
        return Misalignment(np.inf, np.inf, np.inf, *nan, infinite=True)
    # the bet: payoffs k on the charged cells, dual variables y ≥ 0 (limits) and z (equalities), with
    # A_ub^T y + A_eq^T z ≥ G_S^T k outcome by outcome and b_ub·y + b_eq·z ≤ 1
    GS, PS = Gm[S], P[S]
    mS, r, e = GS.shape[0], A_ub.shape[0], A_eq.shape[0]
    M = np.hstack([-GS.T, A_ub.T, A_eq.T])                   # n rows, ≥ 0
    cost = np.r_[np.zeros(mS), b_ub, b_eq]                   # ≤ 1

    def f(v):
        return -float(PS @ np.log(np.maximum(v[:mS], 1e-300)))

    def df(v):
        g = np.zeros_like(v)
        g[:mS] = -PS / np.maximum(v[:mS], 1e-300)
        return g

    v0 = np.r_[np.ones(mS), np.zeros(r), 1.0, np.zeros(e - 1)]
    cons = [{"type": "ineq", "fun": lambda v: M @ v, "jac": lambda v: M},
            {"type": "ineq", "fun": lambda v: 1.0 - cost @ v, "jac": lambda v: -cost[None, :]}]
    bounds = [(1e-12, None)] * mS + [(0, None)] * r + [(None, None)] * e
    best = v0
    for start in (v0,):
        res = minimize(f, start, jac=df, constraints=cons, bounds=bounds, method="SLSQP",
                       options={"ftol": 1e-15, "maxiter": 3000})
        if f(res.x) < f(best):
            best = res.x
    k = np.maximum(best[:mS], 1e-300)
    # every bet's growth is a lower bound once its cost is checked: scale k so that its exact largest cost is 1
    h = np.zeros(len(groups))
    h[S] = k
    lower = bet_lower_bound(p, h @ Gm, limits, world)
    # the nearest acceptable behaviour: cell masses P/k on the charged cells, as nearly as the requirement allows
    target = PS / k
    a = _nearest(GS, target, A_ub, b_ub, A_eq, b_eq, n, lp.x[:n])
    q = Gm @ a
    upper = float(PS @ np.log(PS / np.maximum(q[S], 1e-300))) if np.all(q[S] > 0) else np.inf
    upper = max(upper, 0.0)                                   # a divergence; rounding can leave −1e−17
    return Misalignment(upper, min(max(lower, 0.0), upper), upper, a, h)


def _nearest(GS, target, A_ub, b_ub, A_eq, b_eq, n, fallback):
    """An acceptable behaviour whose masses on the charged cells are as near `target` as possible (least total
    deviation, by a linear program); `fallback` if the program fails."""
    mS = GS.shape[0]
    # variables: a (n), s+ (mS), s- (mS); minimize Σ s; G a − s+ + s- = target
    c = np.r_[np.zeros(n), np.ones(2 * mS)]
    Aeq = np.vstack([np.hstack([GS, -np.eye(mS), np.eye(mS)]), np.hstack([A_eq, np.zeros((A_eq.shape[0], 2 * mS))])])
    beq = np.r_[target, b_eq]
    Aub = np.hstack([A_ub, np.zeros((A_ub.shape[0], 2 * mS))]) if A_ub.shape[0] else None
    lp = linprog(c, A_ub=Aub, b_ub=b_ub if A_ub.shape[0] else None, A_eq=Aeq, b_eq=beq,
                 bounds=[(0, None)] * (n + 2 * mS), method="highs")
    return lp.x[:n] if lp.status == 0 else fallback


def bet_lower_bound(p, h, limits, world=None):
    """R2(i): any payoff h ≥ 0 gives a lower bound on misalignment once scaled into a bet. Its largest cost m under the
    acceptable behaviours sharing p's law (a linear program) makes h/m a bet, whose growth E_p[log h] − log m is at
    most M_A(p). Use it to certify the evidence of a bet chosen in any way."""
    p, h = np.asarray(p, float), np.asarray(h, float)
    n = p.size
    A_ub, b_ub, A_eq, b_eq = _constraints(limits, p, world, n)
    m = _largest_cost(h, A_ub, b_ub, A_eq, b_eq, n)
    s = p > 0
    if np.any(h[s] <= 0):
        return -np.inf
    return float(p[s] @ np.log(h[s])) - float(np.log(m))


def _largest_cost(h, A_ub, b_ub, A_eq, b_eq, n):
    """max E_a[h] over the acceptable behaviours, by a linear program."""
    lp = linprog(-h, A_ub=A_ub if A_ub.shape[0] else None, b_ub=b_ub if A_ub.shape[0] else None,
                 A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * n, method="highs")
    return float(-lp.fun) if lp.status == 0 else np.inf


def rate_limit_misalignment(u, eps):
    """R7: kl(u‖eps) if u > eps, else 0; infinite for a forbidden set breached."""
    if u <= eps:
        return 0.0
    if eps == 0:
        return np.inf
    return kl_binary(u, eps)


def budget_misalignment(p, g, b):
    """R8: max over 0 ≤ λ ≤ 1/(b − min g) of E_p[log(1 + λ(g − b))], and the best λ."""
    p, g = np.asarray(p, float), np.asarray(g, float)
    if p @ g <= b:
        return 0.0, 0.0
    lmax = 1.0 / (b - g.min())
    s = p > 0

    def neg(lam):
        h = 1 + lam * (g[s] - b)
        return np.inf if np.any(h <= 0) else -float(p[s] @ np.log(h))
    r = minimize_scalar(neg, bounds=(0.0, lmax), method="bounded", options={"xatol": 1e-13})
    lam = r.x
    edge = neg(lmax)
    if edge < r.fun:
        lam, val = lmax, -edge
    else:
        val = -r.fun
    return float(val), float(lam)


def _v(theta, u):
    return ((theta + 1) - np.sqrt((theta + 1) ** 2 - 4 * theta * u)) / (2 * theta)


def overall_rate_limit(w, u, eps):
    """R10: misalignment against an overall rate limit eps when the world fixes the conditions' law w and the actor's
    breach rate in condition E is u[E]; returns (value, θ, the nearest acceptable rates)."""
    w, u = np.asarray(w, float), np.asarray(u, float)
    if w @ u <= eps:
        return 0.0, 0.0, u.copy()
    f = lambda th: w @ _v(th, u) - eps
    hi = 1.0
    while f(hi) > 0:
        hi *= 2
    theta = brentq(f, 1e-12, hi, xtol=1e-15, rtol=1e-15, maxiter=500)
    v = _v(theta, u)
    return float(sum(wi * kl_binary(ui, vi) for wi, ui, vi in zip(w, u, v))), float(theta), v


# --------------------------------------------------------------------------------------- tests and verdicts (D6, D7)

@dataclass
class BetTest:
    """The wealth of a sequence of bets against a budget (R4, R8), with the first decision at which it convicts."""
    wealth: np.ndarray = field(repr=False)
    convicted: bool
    at: int | None
    alpha: float


def bet_test(costs, b, cost_min, alpha=0.05):
    """Bet against "E[g] ≤ b at every decision" on the record's costs g(x_i), with a fraction λ_i of wealth chosen from
    the earlier decisions only (R4), in [0, 1/(2(b − cost_min))]; convicts when the wealth reaches 1/alpha. For a rate
    limit, costs are the breach indicators, b the rate and cost_min 0."""
    y = np.asarray(costs, float)
    lcap = 0.5 / (b - cost_min)
    W, w, at = np.empty(y.size), 1.0, None
    s1, s2 = 0.0, 0.0
    for i, yi in enumerate(y):
        k = i + 1.0
        mean = (s1 + b) / k                      # a prior pseudo-observation at the budget keeps early bets small
        var = (s2 + (b - cost_min) ** 2 / 4) / k - mean ** 2 + 1e-12
        lam = float(np.clip((mean - b) / (var + (mean - b) ** 2), 0.0, lcap))
        w *= 1 + lam * (yi - b)
        W[i] = w
        if at is None and w >= 1 / alpha:
            at = i + 1
        s1 += yi
        s2 += yi * yi
    return BetTest(W, at is not None, at, alpha)


@dataclass
class AverageBounds:
    """R16: bounds, valid at every n ≤ horizon at once with probability at least 1 − alpha, on the average of the
    conditional means of y (y in [0, 1])."""
    lower: np.ndarray = field(repr=False)
    upper: np.ndarray = field(repr=False)
    alpha: float
    lam: float


def average_bounds(y, alpha=0.05, horizon=None, lam=None):
    """R16, both sides at alpha/2 each, with λ = √(8 log(2/alpha)/horizon) unless declared."""
    y = np.asarray(y, float)
    if np.any(y < 0) or np.any(y > 1):
        raise ValueError("y must lie in [0, 1]: rescale costs to [0, 1] first")
    N = horizon or y.size
    L = np.log(2 / alpha)
    lam = lam or np.sqrt(8 * L / N)
    n = np.arange(1, y.size + 1)
    mean = np.cumsum(y) / n
    margin = lam / 8 + L / (n * lam)
    return AverageBounds(np.clip(mean - margin, 0, 1), np.clip(mean + margin, 0, 1), alpha, float(lam))


def pooled_verdict(y, limit, alpha=0.05, horizon=None):
    """D7 and R16 for a pooled limit "average of the conditional means of y ≤ limit": 'certify' when the upper bound
    at the record's end is at most the limit, 'convict' when the lower bound is above it, else 'neither'."""
    bd = average_bounds(y, alpha, horizon)
    if bd.upper[-1] <= limit:
        return "certify", bd
    if bd.lower[-1] > limit:
        return "convict", bd
    return "neither", bd


# --------------------------------------------------------------------------- splits along resolution and capability

def resolution_split(p, limits, chain, world=None):
    """R11: misalignment at each partition of `chain` (coarse to fine, each an array of cell labels, None for the
    finest), and the increments, which add up to the misalignment at the finest."""
    values = [misalignment(p, limits, world, cells).value for cells in chain]
    return values, list(np.diff(values))


def unavoidable(vertices, limits, world=None):
    """m(𝓕) of D9 for 𝓕 the convex hull of `vertices` (behaviours sharing one law on the conditions): the least
    misalignment of a mixture, by minimizing over the mixture weights; returns (value, weights)."""
    V = np.asarray(vertices, float)
    k = V.shape[0]
    f = lambda wt: misalignment(np.clip(wt, 0, None) / max(np.clip(wt, 0, None).sum(), 1e-300) @ V,
                                limits, world).value
    best = min(((f(np.eye(k)[j]), np.eye(k)[j]) for j in range(k)), key=lambda t: t[0])
    x0 = np.full(k, 1.0 / k)
    if np.isfinite(f(x0)):
        r = minimize(f, x0, method="SLSQP", bounds=[(0, 1)] * k,
                     constraints=[{"type": "eq", "fun": lambda wt: wt.sum() - 1}], options={"ftol": 1e-13})
        wt = np.clip(r.x, 0, None) / np.clip(r.x, 0, None).sum()
        val = f(wt)
        if val < best[0]:
            best = (val, wt)
    return float(best[0]), best[1]


def factorization(p, chain, limits, world=None):
    """R14: for nested feasible sets given as vertex lists (largest first), the terms m_1, the increments, and the
    avoidable excess E(p); they add up to M_A(p)."""
    m = [unavoidable(V, limits, world)[0] for V in chain]
    total = misalignment(p, limits, world).value
    return {"unavoidable": m[0], "increments": list(np.diff(m)), "avoidable_excess": total - m[-1], "total": total}


def culpable(p, vertices, limits, delta, world=None):
    """D9: culpable at care margin delta when the avoidable excess E(p) exceeds delta; returns (verdict, E, m)."""
    m, _ = unavoidable(vertices, limits, world)
    E = misalignment(p, limits, world).value - m
    return bool(E > delta), float(E), float(m)
