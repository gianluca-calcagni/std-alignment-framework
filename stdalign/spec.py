"""The MVP's quantities (`mvp/CORE.md`): misalignment against a declared specification, its bets and tests, the
certificate for an average, and the splits along the record's resolution and along what the actor could do.

Outcomes are finite and indexed 0..n-1. A behaviour is an array of n masses. The world's part (D1) is given as
`world`, an array of n condition labels, or None when the world chooses nothing. A per-decision requirement is a list of
`Limit`s, linear limits on averages (R6): E_a[g · 1_cell] ≤ b · a(cell), where `cell` is a condition label, or None for
the whole outcome space. Since the behaviours compared share the actor's law on the conditions (D5), a limit inside a
condition is linear in a. Misalignment is computed by convex optimization and returned with two numerical bounds: the
upper end is the divergence to a behaviour that meets the requirement, the lower end the growth of a payoff scaled into a
bet that the requirement calls fair (R2(i)), its cost checked by a linear program. Both hold to the solvers' tolerance, not
exactly: the behaviour behind the upper end meets each limit to 1e-8, so either end can be off by about that.
"""
from dataclasses import dataclass, field
import numpy as np
from scipy.optimize import linprog, minimize, brentq, minimize_scalar

TOL = 1e-9          # feasibility tolerance of the linear programs and of the solver's constraints
TINY = 1e-12        # a charged cell that no acceptable behaviour can give more than this is treated as forbidden
INVERSION = 1e-7    # bounds crossing by more than this flag a solver error; less is the linear programs' tolerance


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
            if labels is None or not np.any(labels == lim.cell):
                raise ValueError(f"limit {lim.name!r} names the condition {lim.cell!r}, which `world` does not have")
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
    """M_A at a resolution, with numerical bounds [lower, upper] (to the solvers' tolerance), the nearest acceptable
    behaviour found, and the best bet, constant on the resolution's cells (R2, R12). `value` is `upper`; `inverted` when
    the lower end exceeds the upper by more than 1e-9, a sign of solver error; `infinite` when no acceptable behaviour
    charges every cell that p charges; `consistent` False when no acceptable behaviour shares p's law at all."""
    value: float
    lower: float
    upper: float
    nearest: np.ndarray = field(repr=False)
    bet: np.ndarray = field(repr=False)
    infinite: bool = False
    consistent: bool = True
    inverted: bool = False


def misalignment(p, limits, world=None, cells=None):
    """M_A^𝒢(p) of D5 and D8: the least KL between p's and an acceptable behaviour's masses on the cells of `cells`
    (an array of n cell labels refining `world`; None for the finest partition), over the acceptable behaviours that
    share p's law on `world`.

    Computed as the growth of the best bet constant on the cells (R2, R12): maximize E_P[log k] over cell payoffs k
    whose largest cost under the requirement is at most 1, that cost written by linear-programming duality. The payoff
    found is then scaled by its exact largest cost (a linear program), so its growth is a lower bound. The upper bound
    is the divergence to an acceptable behaviour recovered from the bet, by a linear program that keeps every charged
    cell's mass positive."""
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
    if lp.x[-1] <= TINY:
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
    # candidates: the bet's own target, when the cells are outcomes (R2(ii): a* = p/h*); the target completed on the
    # uncharged outcomes at the least relative deviation; the nearest point in total deviation; the interior point of
    # the feasibility program. The best feasible one that starves no charged
    # cell gives the upper bound, after a descent that keeps only feasible points.
    candidates = [lp.x[:n], _nearest(GS, target, A_ub, b_ub, A_eq, b_eq, n, lp.x[:n])]
    done = _completed(GS, target, A_ub, b_ub, A_eq, b_eq, n)
    if done is not None:
        candidates.insert(0, done)
    if cells is None:
        t = np.zeros(n)
        t[S] = target
        candidates[:0] = [t, _repaired(t, lp.x[:n], A_ub, b_ub, A_eq, b_eq)]
    div = lambda x: float(PS @ np.log(PS / (Gm @ x)[S])) if np.all((Gm @ x)[S] > 0) else np.inf
    ok = [x for x in candidates if _feasible(x, A_ub, b_ub, A_eq, b_eq) and np.isfinite(div(x))]
    a = min(ok, key=div) if ok else lp.x[:n]
    a = _polish(a, GS, PS, A_ub, b_ub, A_eq, b_eq)
    upper = max(div(a), 0.0)                                  # a divergence; rounding can leave −1e−17
    lower = max(lower, 0.0)
    inverted = bool(lower > upper + INVERSION)
    if not inverted:                                          # a crossing within tolerance is the solvers' rounding
        lower = min(lower, upper)
    return Misalignment(upper, lower, upper, a, h, inverted=inverted)


def _feasible(a, A_ub, b_ub, A_eq, b_eq):
    return (np.all(a >= -TOL) and np.allclose(A_eq @ a, b_eq, atol=10 * TOL)
            and (A_ub.shape[0] == 0 or np.all(A_ub @ a <= b_ub + 10 * TOL)))


def _repaired(t, interior, A_ub, b_ub, A_eq, b_eq):
    """The least mixture of t with a feasible interior point that is feasible, by bisection on the mixing weight."""
    if _feasible(t, A_ub, b_ub, A_eq, b_eq):
        return t
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if _feasible((1 - mid) * t + mid * interior, A_ub, b_ub, A_eq, b_eq):
            hi = mid
        else:
            lo = mid
    return (1 - hi) * t + hi * interior


def _polish(a, GS, PS, A_ub, b_ub, A_eq, b_eq):
    """Lower the divergence from a feasible a by a direct minimization, keeping the result only if it is feasible and
    better: the upper bound must come from a behaviour that meets the requirement."""
    def obj(x):
        return float(PS @ np.log(PS / np.maximum(GS @ x, 1e-300)))

    def grad(x):
        return -(PS / np.maximum(GS @ x, 1e-300)) @ GS

    cons = [{"type": "eq", "fun": lambda x: A_eq @ x - b_eq, "jac": lambda x: A_eq}]
    if A_ub.shape[0]:
        cons.append({"type": "ineq", "fun": lambda x: b_ub - A_ub @ x, "jac": lambda x: -A_ub})
    try:
        r = minimize(obj, a, jac=grad, constraints=cons, bounds=[(0, 1)] * a.size, method="SLSQP",
                     options={"ftol": 1e-15, "maxiter": 500})
    except ValueError:
        return a
    x = np.clip(r.x, 0, None)
    if _feasible(x, A_ub, b_ub, A_eq, b_eq) and np.all(GS @ x > 0) and obj(x) < obj(a):
        return x
    return a


def _nearest(GS, target, A_ub, b_ub, A_eq, b_eq, n, fallback):
    """An acceptable behaviour whose masses on the charged cells are as near `target` as possible (least total
    deviation, by a linear program); `fallback` if the program fails."""
    mS = GS.shape[0]
    # variables: a (n), s+ (mS), s- (mS); minimize Σ s; G a − s+ + s- = target; and G a ≥ target/2, so that no
    # charged cell is left with zero mass
    c = np.r_[np.zeros(n), np.ones(2 * mS)]
    Aeq = np.vstack([np.hstack([GS, -np.eye(mS), np.eye(mS)]), np.hstack([A_eq, np.zeros((A_eq.shape[0], 2 * mS))])])
    beq = np.r_[target, b_eq]
    floor = np.hstack([-GS, np.zeros((mS, 2 * mS))])
    Aub = np.vstack([np.hstack([A_ub, np.zeros((A_ub.shape[0], 2 * mS))]), floor])
    bub = np.r_[b_ub, -target / 2]
    lp = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * (n + 2 * mS), method="highs")
    return lp.x[:n] if lp.status == 0 else fallback


def _completed(GS, target, A_ub, b_ub, A_eq, b_eq, n):
    """An acceptable behaviour whose charged cells' masses are all within a common relative deviation η of `target`,
    with η least (a linear program): the uncharged outcomes take the mass the target leaves, and the divergence it
    gives exceeds the target's by at most about η. None if the program fails."""
    mS = GS.shape[0]
    # variables: a (n), η; target(1 − η) ≤ G a ≤ target(1 + η); minimize η
    c = np.r_[np.zeros(n), 1.0]
    Aub = np.vstack([np.hstack([A_ub, np.zeros((A_ub.shape[0], 1))]),
                     np.hstack([GS, -target[:, None]]), np.hstack([-GS, -target[:, None]])])
    bub = np.r_[b_ub, target, -target]
    lp = linprog(c, A_ub=Aub, b_ub=bub, A_eq=np.hstack([A_eq, np.zeros((A_eq.shape[0], 1))]), b_eq=b_eq,
                 bounds=[(0, None)] * n + [(0, 0.5)], method="highs")
    return lp.x[:n] if lp.status == 0 else None


def bet_lower_bound(p, h, limits, world=None):
    """R2(i): any payoff h ≥ 0 gives a lower bound on misalignment once scaled into a bet. Its largest cost m under the
    acceptable behaviours sharing p's law (a linear program) makes h/m a bet, whose growth E_p[log h] − log m is at
    most M_A(p). Use it to bound the evidence of a bet chosen in any way."""
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
    u = np.clip(u, 0.0, 1.0)                                  # mixtures can land a rounding error outside [0, 1]
    return ((theta + 1) - np.sqrt(np.maximum((theta + 1) ** 2 - 4 * theta * u, 0.0))) / (2 * theta)


def overall_rate_limit(w, u, eps):
    """R10: misalignment against an overall rate limit eps when the world fixes the conditions' law w and the actor's
    breach rate in condition E is u[E]; returns (value, θ, the nearest acceptable rates)."""
    w, u = np.asarray(w, float), np.clip(np.asarray(u, float), 0.0, 1.0)
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
    """D7 and R16 for a pooled limit "average of the conditional means of y over the horizon ≤ limit", read at the
    declared horizon (the record's length if none is declared): 'certify' when the upper bound there is at most the
    limit, 'convict' when the lower bound is above it, 'neither' otherwise, and 'pending' before the horizon."""
    y = np.asarray(y, float)
    N = horizon or y.size
    bd = average_bounds(y, alpha, N)
    if y.size < N:
        return "pending", bd
    if bd.upper[N - 1] <= limit:
        return "certify", bd
    if bd.lower[N - 1] > limit:
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
    misalignment of a mixture, by minimizing over the mixture weights; returns (value, weights). A vertex of infinite
    misalignment makes every mixture that weighs it infinite (it charges an outcome no acceptable behaviour may), so the
    search runs over the others. The value is a numerical minimum: an upper bound on m(𝓕), to the solvers' tolerance."""
    V = np.asarray(vertices, float)
    k = V.shape[0]
    single = np.array([misalignment(V[j], limits, world).value for j in range(k)])
    finite = np.flatnonzero(np.isfinite(single))
    if finite.size == 0:
        return np.inf, np.eye(k)[0]
    j0 = finite[np.argmin(single[finite])]
    best = (float(single[j0]), np.eye(k)[j0])
    if finite.size == 1 or best[0] <= TOL:                    # misalignment is never negative: 0 is the minimum
        return best
    Vf = V[finite]
    f = lambda wt: misalignment(np.clip(wt, 0, None) / max(np.clip(wt, 0, None).sum(), 1e-300) @ Vf,
                                limits, world).value
    kf = finite.size
    starts = [np.full(kf, 1.0 / kf)] + [np.eye(kf)[i] * 0.5 + np.eye(kf)[j] * 0.5
                                         for i in range(kf) for j in range(i + 1, kf)]
    for x0 in starts:
        r = minimize(f, x0, method="SLSQP", bounds=[(0, 1)] * kf,
                     constraints=[{"type": "eq", "fun": lambda wt: wt.sum() - 1}], options={"ftol": 1e-13})
        for cand in (np.clip(r.x, 0, None), x0):
            wt = cand / cand.sum()
            val = f(wt)
            if val < best[0]:
                full = np.zeros(k)
                full[finite] = wt
                best = (float(val), full)
        if best[0] <= TOL:
            break
    return best


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
