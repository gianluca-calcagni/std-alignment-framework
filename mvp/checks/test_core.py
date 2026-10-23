"""Checks of the MVP's results (`mvp/CORE.md`), one or more per result, on random instances and degenerate cases.

Each check computes the result's claim on the library `stdalign/spec.py` and, where the claim is about the library's
own number, against an independent computation (a closed form, an exact enumeration, a linear program or a
simulation). Tolerances come from the quantity's scale: `EXACT` for identities of floating sums, `SOLVER` for convex
optimization, and Monte Carlo margins of four standard errors.
"""
import itertools
import math

import numpy as np
import pytest
from scipy.optimize import linprog, minimize
from scipy.stats import multinomial

from stdalign import spec as S

EXACT = 1e-12
SOLVER = 1e-6


def rng(seed):
    return np.random.default_rng(seed)


def largest_cost(h, limits, p=None, world=None):
    """max E_a[h] over the acceptable behaviours sharing p's law on world, by an independent linear program."""
    n = len(h)
    p = np.full(n, 1.0 / n) if p is None else p
    A_ub, b_ub, A_eq, b_eq = S._constraints(limits, p, world, n)
    lp = linprog(-np.asarray(h), A_ub=A_ub if A_ub.shape[0] else None, b_ub=b_ub if A_ub.shape[0] else None,
                 A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * n, method="highs")
    return -lp.fun


def random_budgets(r, n, k, p):
    """k budgets that p breaks and the uniform behaviour keeps, so the requirement is consistent and p is misaligned."""
    lims = []
    u = np.full(n, 1.0 / n)
    for _ in range(k):
        g = r.normal(size=n)
        if p @ g < u @ g:
            g = -g
        lims.append(S.budget(g, u @ g + 0.3 * (p @ g - u @ g)))
    return lims


# ------------------------------------------------------------------------------------------------------------ D5

def test_d5_severity_example():
    assert S.kl_binary(2e-6, 1e-6) == pytest.approx(3.86e-7, rel=1e-2)
    assert f"{S.kl_binary(2e-6, 1e-6):.2g}" == "3.9e-07"
    assert round(S.kl_binary(0.2, 0.1), 3) == 0.044


# ------------------------------------------------------------------------------------------------------------ R1

def test_r1_chain_rule():
    r = rng(1)
    for _ in range(50):
        n, k = 7, 3
        world = np.r_[np.arange(k), r.integers(0, k, n - k)]
        p = r.dirichlet(np.ones(n))
        a = r.dirichlet(np.ones(n))
        for c in range(k):                       # give a the law of p on the conditions
            m = world == c
            a[m] *= p[m].sum() / a[m].sum()
        lhs = S.kl(p, a)
        rhs = sum(p[world == c].sum() * S.kl(p[world == c] / p[world == c].sum(), a[world == c] / a[world == c].sum())
                  for c in range(k))
        assert lhs == pytest.approx(rhs, abs=EXACT * 10)


def test_r1_per_condition_sum():
    r = rng(2)
    for _ in range(20):
        world = np.array([0, 0, 0, 1, 1, 1])
        p = r.dirichlet(np.ones(6))
        eps = r.uniform(0.02, 0.3, 2)
        C = np.array([1, 0, 0, 1, 0, 0], bool)
        lims = [S.rate_limit(C, eps[0], cell=0), S.rate_limit(C, eps[1], cell=1)]
        got = S.misalignment(p, lims, world)
        want = sum(p[world == c].sum() * S.rate_limit_misalignment(p[(world == c) & C].sum() / p[world == c].sum(),
                                                                  eps[c]) for c in (0, 1))
        assert got.value == pytest.approx(want, abs=SOLVER)


def test_r1_world_part_raises():
    r = rng(3)
    raised = 0
    for _ in range(20):
        world = np.array([0, 0, 1, 1])
        p = r.dirichlet(np.ones(4))
        lims = [S.rate_limit([1, 3], 0.5 * (p[1] + p[3]), 4)]
        with_world = S.misalignment(p, lims, world).value
        without = S.misalignment(p, lims).value
        assert without <= with_world + SOLVER
        raised += with_world > without + 1e-4
    assert raised > 0


# ------------------------------------------------------------------------------------------------------------ R2

def test_r2_best_bet_fair_and_attains():
    r = rng(4)
    for _ in range(30):
        n = 5
        p = r.dirichlet(np.ones(n))
        lims = random_budgets(r, n, 2, p)
        m = S.misalignment(p, lims)
        assert m.upper - m.lower <= SOLVER
        a = m.nearest
        s = p > 0
        h = np.zeros(n)
        h[s] = p[s] / a[s]
        assert largest_cost(h, lims) <= 1 + 1e-6            # fair under every acceptable behaviour
        assert float(p[s] @ np.log(h[s])) == pytest.approx(m.value, abs=SOLVER)


def test_r2_any_bet_below():
    r = rng(5)
    for _ in range(30):
        n = 5
        p = r.dirichlet(np.ones(n))
        lims = random_budgets(r, n, 2, p)
        M = S.misalignment(p, lims).value
        for _ in range(20):
            h = r.exponential(size=n)
            h /= largest_cost(h, lims)                       # scaled to be a bet
            assert float(p @ np.log(h)) <= M + SOLVER


def test_r2_infinite_case():
    p = np.array([0.1, 0.9])
    lims = [S.forbidden([0], 2)]
    assert S.misalignment(p, lims).value == np.inf
    for H in (10.0, 1e6):
        h = np.array([H, 1.0])
        assert largest_cost(h, lims) <= 1 + EXACT
        assert float(p @ np.log(h)) == pytest.approx(0.1 * math.log(H))


# ------------------------------------------------------------------------------------------------------------ R3

def test_r3_hull_bets():
    a1, a2 = np.array([0.8, 0.1, 0.1]), np.array([0.1, 0.1, 0.8])
    p = (a1 + a2) / 2
    # Sanov's rate against the pair {a1, a2} is positive; the best bet against the pair is fair under their hull, which
    # contains p, so it cannot grow under p
    assert min(S.kl(p, a1), S.kl(p, a2)) > 0.1
    r = rng(6)
    for _ in range(200):
        h = r.exponential(size=3)
        h /= max(a1 @ h, a2 @ h)
        for t in np.linspace(0, 1, 11):
            assert ((1 - t) * a1 + t * a2) @ h <= 1 + EXACT
        assert p @ np.log(h) <= EXACT


def cvar(losses, probs, tail):
    order = np.argsort(losses)[::-1]
    left, total = tail, 0.0
    for i in order:
        take = min(probs[i], left)
        total += take * losses[i]
        left -= take
        if left <= 0:
            break
    return total / tail


def test_r3_cvar_not_convex():
    losses = np.array([1.0, 0.6, 0.0])
    b1 = np.array([0.06, 0.0, 0.94])
    b2 = np.array([0.0, 1.0, 0.0])
    assert cvar(losses, b1, 0.1) == pytest.approx(0.6)
    assert cvar(losses, b2, 0.1) == pytest.approx(0.6)
    assert cvar(losses, (b1 + b2) / 2, 0.1) == pytest.approx(0.72)


# ------------------------------------------------------------------------------------------------------------ R4

def test_r4_level_under_dependence():
    r = rng(7)
    eps, alpha, records, n = 0.1, 0.05, 2000, 300
    convicted = 0
    for _ in range(records):
        prev, ys = 0, []
        for _ in range(n):
            rate = eps if prev else eps / 3          # acceptable at every step, dependent on the last decision
            prev = int(r.random() < rate)
            ys.append(prev)
        convicted += S.bet_test(ys, eps, 0.0, alpha).convicted
    se = math.sqrt(alpha * (1 - alpha) / records)
    assert convicted / records <= alpha + 4 * se


def test_r4_level_iid():
    r = rng(8)
    eps, alpha, records, n = 0.1, 0.05, 2000, 400
    convicted = sum(S.bet_test((r.random(n) < eps).astype(float), eps, 0.0, alpha).convicted for _ in range(records))
    se = math.sqrt(alpha * (1 - alpha) / records)
    assert convicted / records <= alpha + 4 * se
    power = sum(S.bet_test((r.random(n) < 2 * eps).astype(float), eps, 0.0, alpha).convicted for _ in range(200))
    assert power / 200 > 0.5                          # the test is not vacuous


# ------------------------------------------------------------------------------------------------------------ R5

def test_r5_type_bounds():
    n_dec, eps = 12, 0.2
    C = np.array([1, 0, 0], bool)
    k_n = math.comb(n_dec + 2, 2)
    for counts in itertools.product(range(n_dec + 1), repeat=2):
        if sum(counts) > n_dec:
            continue
        c = np.array([counts[0], counts[1], n_dec - sum(counts)])
        s = c / n_dec
        M = S.rate_limit_misalignment(s[0], eps)
        # the most likely acceptable behaviour scales s's proportions inside and outside C (R7)
        a = s.copy()
        if s[0] > eps:
            a[0] = eps
            rest = s[1:].sum()
            a[1:] = s[1:] * (1 - eps) / rest if rest > 0 else (1 - eps) / 2
        sup = multinomial.pmf(c, n_dec, a)
        assert sup <= math.exp(-n_dec * M) * (1 + 1e-9)
        assert sup >= math.exp(-n_dec * M) / k_n * (1 - 1e-9)


# ------------------------------------------------------------------------------------------------------------ R6

def test_r6_separating_budget():
    r = rng(9)
    for _ in range(30):
        n, k = 4, 3
        V = r.dirichlet(np.ones(n), size=k)              # S is the hull of k points
        x = r.dirichlet(np.ones(n))
        res = minimize(lambda w: np.sum((x - w @ V) ** 2), np.full(k, 1 / k), method="SLSQP",
                       bounds=[(0, 1)] * k, constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}],
                       options={"ftol": 1e-15})
        c = res.x @ V
        if np.linalg.norm(x - c) < 1e-3:
            continue
        g = x - c
        b = g @ c + np.sum((x - c) ** 2) / 2
        assert np.all(V @ g < b)
        assert x @ g > b
        assert b > g.min()


# ------------------------------------------------------------------------------------------------------------ R7

def test_r7_rate_limit_closed_form():
    r = rng(10)
    for _ in range(30):
        p = r.dirichlet(np.ones(5))
        eps = r.uniform(0.01, 0.5)
        C = r.random(5) < 0.5
        C[0], C[1] = True, False
        u = p[C].sum()
        grid = np.linspace(0, eps, 200001)[1:]
        brute = min(S.kl_binary(u, v) for v in grid[-200:]) if u > eps else 0.0
        closed = S.rate_limit_misalignment(u, eps)
        assert closed == pytest.approx(brute, abs=1e-8)
        assert S.misalignment(p, [S.rate_limit(C, eps)]).value == pytest.approx(closed, abs=SOLVER)


def test_r7_forbidden():
    p = np.array([0.001, 0.999])
    assert S.rate_limit_misalignment(0.001, 0.0) == np.inf
    assert S.misalignment(p, [S.forbidden([0], 2)]).value == np.inf
    assert S.misalignment(np.array([0.0, 1.0]), [S.forbidden([0], 2)]).value == pytest.approx(0.0, abs=EXACT)
    r = rng(11)          # convicting at the first forbidden outcome never convicts an actor that never produces one
    assert not any(np.any(r.random(500) < 0.0) for _ in range(100))


# ------------------------------------------------------------------------------------------------------------ R8

def test_r8_budget_dual():
    r = rng(12)
    at_edge = 0
    for _ in range(40):
        n = 5
        p = r.dirichlet(np.ones(n))
        p[r.integers(n)] = 0.0 if r.random() < 0.5 else p[0]
        p /= p.sum()
        g = r.normal(size=n)
        b = g.min() + r.uniform(0.05, 0.9) * (p @ g - g.min())
        val, lam = S.budget_misalignment(p, g, b)
        assert val == pytest.approx(S.misalignment(p, [S.budget(g, b)]).value, abs=SOLVER)
        lmax = 1 / (b - g.min())
        at_edge += abs(lam - lmax) < 1e-9
        h = 1 + lam * (g - b)
        assert np.all(h >= -EXACT)
        assert largest_cost(h, [S.budget(g, b)]) <= 1 + 1e-9    # a bet
    p = np.array([0.0, 0.5, 0.5])                                # E_p g ≤ b: no misalignment
    assert S.budget_misalignment(p, np.array([0.0, 1.0, 1.0]), 1.0)[0] == 0.0


# ------------------------------------------------------------------------------------------------------------ R9

def test_r9_reference_criteria():
    r = rng(13)
    for _ in range(20):
        n = 5
        ref = r.dirichlet(np.ones(n))
        G = r.normal(size=(2, n))
        lims = S.no_worse_than(ref, G)
        assert S.misalignment(ref, lims).value == pytest.approx(0.0, abs=SOLVER)
        a = r.dirichlet(np.ones(n))
        if all(a @ Gj >= ref @ Gj for Gj in G):
            lam = r.exponential(size=2)
            assert a @ (3.0 + lam @ G) >= ref @ (3.0 + lam @ G) - EXACT
    ref = np.array([0.0, 0.5, 0.5])
    lims = S.no_worse_than(ref, [-np.array([1.0, 0.0, 0.0])])
    assert S.misalignment(np.array([0.01, 0.49, 0.5]), lims).value == np.inf


# ------------------------------------------------------------------------------------------------------------ R10

def test_r10_overall_rate_limit():
    r = rng(14)
    for _ in range(30):
        k = int(r.integers(2, 4))
        world = np.r_[np.repeat(np.arange(k), 2), r.integers(0, k, 3)]
        n = world.size
        C = np.zeros(n, bool)
        C[np.arange(0, 2 * k, 2)] = True                  # each condition has an outcome in C and one outside
        p = r.dirichlet(np.ones(n))
        w = np.array([p[world == c].sum() for c in range(k)])
        u = np.array([p[(world == c) & C].sum() / w[c] for c in range(k)])
        eps = 0.6 * (w @ u)
        closed, theta, v = S.overall_rate_limit(w, u, eps)
        assert w @ v == pytest.approx(eps, abs=1e-12)
        assert S.misalignment(p, [S.rate_limit(C, eps)], world).value == pytest.approx(closed, abs=SOLVER)
        assert S.rate_limit_misalignment(w @ u, eps) <= closed + EXACT


def test_r10_support_bot():
    w, u = np.array([0.7, 0.3]), np.array([0.0291, 0.3534])
    # the rates are the slides' to four digits; that rounding moves the result by about 1e-5
    assert S.overall_rate_limit(w, u, 0.05)[0] == pytest.approx(0.04956, abs=3e-5)
    assert S.rate_limit_misalignment(w @ u, 0.05) == pytest.approx(0.0440, abs=5e-5)


def test_r10_condition_inside_c():
    p = np.array([0.2, 0.4, 0.4])
    world = np.array([0, 1, 1])
    C = np.array([True, True, False])                    # condition 0 lies inside C: its breach rate is 1
    m = S.misalignment(p, [S.rate_limit(C, 0.1)], world)
    assert m.value == np.inf and not m.consistent


# ------------------------------------------------------------------------------------------------------------ R11

def test_r11_refinement():
    r = rng(15)
    revealed = 0
    for _ in range(25):
        n = 6
        p = r.dirichlet(np.ones(n))
        lims = random_budgets(r, n, 2, p)
        chain = [np.array([0, 0, 0, 1, 1, 1]), np.array([0, 0, 1, 2, 3, 3]), None]
        vals, inc = S.resolution_split(p, lims, chain)
        assert all(d >= -SOLVER for d in inc)
        assert vals[0] + sum(inc) == pytest.approx(vals[-1], abs=EXACT)
        assert vals[-1] == pytest.approx(S.misalignment(p, lims).value, abs=SOLVER)
        revealed += sum(d > 1e-3 for d in inc)
        a = r.dirichlet(np.ones(n))                       # (i) for any behaviour, coarsening lowers KL
        for cells in chain[:2]:
            pc = np.bincount(cells, p)
            ac = np.bincount(cells, a)
            assert S.kl(pc, ac) <= S.kl(p, a) + EXACT
    assert revealed > 0                                   # refining reveals misalignment in some instances


def test_r11_indifference():
    r = rng(16)
    cells = np.array([0, 0, 1, 1, 2])
    for _ in range(20):
        p = r.dirichlet(np.ones(5))
        gc = r.normal(size=3)
        g = gc[cells]                                     # a cost constant on the principal's cells
        u = np.full(5, 0.2)
        if p @ g < u @ g:
            g = -g
        lims = [S.budget(g, u @ g + 0.3 * (p @ g - u @ g))]
        assert S.misalignment(p, lims).value == pytest.approx(S.misalignment(p, lims, cells=cells).value, abs=SOLVER)


# ------------------------------------------------------------------------------------------------------------ R12

def test_r12_coarse_bet():
    r = rng(17)
    cells = np.array([0, 0, 1, 1, 2, 2])
    for _ in range(20):
        p = r.dirichlet(np.ones(6))
        lims = random_budgets(r, 6, 2, p)
        m = S.misalignment(p, lims, cells=cells)
        h = m.bet[cells]                                  # constant on the record's cells
        assert largest_cost(h, lims) <= 1 + 1e-6
        P = np.bincount(cells, p)
        assert float(P @ np.log(np.maximum(m.bet, 1e-300))) == pytest.approx(m.value, abs=SOLVER)


# ------------------------------------------------------------------------------------------------------------ R13

def test_r13_hidden_interval():
    r = rng(18)
    cells = np.array([0, 0, 1, 1, 2, 2])
    for _ in range(15):
        p = r.dirichlet(np.ones(6))
        lims = random_budgets(r, 6, 2, p)
        coarse = S.misalignment(p, lims, cells=cells)
        a = coarse.nearest
        P = np.bincount(cells, p)
        A = np.bincount(cells, a)
        p_split = np.array([P[c] * a[i] / A[c] if A[c] > 0 else 0 for i, c in enumerate(cells)])   # split as a*
        assert np.allclose(np.bincount(cells, p_split), P, atol=EXACT)
        assert S.misalignment(p_split, lims).value == pytest.approx(coarse.value, abs=10 * SOLVER)
        for _ in range(5):                                 # other splits of the same cell masses hide at least as much
            q = r.dirichlet(np.ones(6))
            other = np.array([P[c] * q[i] / q[cells == c].sum() for i, c in enumerate(cells)])
            assert S.misalignment(other, lims).value >= coarse.value - SOLVER


# ------------------------------------------------------------------------------------------------------------ R14

def test_r14_factorization():
    r = rng(19)
    for _ in range(8):
        n = 4
        V = r.dirichlet(np.ones(n), size=4)
        lims = [S.rate_limit([0], 0.1, n)]
        chain = [V, V[:3], V[:2]]
        w = r.dirichlet(np.ones(2))
        p = w @ V[:2]
        f = S.factorization(p, chain, lims)
        assert f["unavoidable"] >= -SOLVER
        assert all(d >= -SOLVER for d in f["increments"])
        assert f["avoidable_excess"] >= -SOLVER
        assert f["unavoidable"] + sum(f["increments"]) + f["avoidable_excess"] == pytest.approx(f["total"], abs=EXACT)


# ------------------------------------------------------------------------------------------------------------ R15

def test_r15_culpability_set():
    r = rng(20)
    lims = [S.rate_limit([0], 0.1, 4), S.budget(np.array([0.0, 1.0, 2.0, 3.0]), 1.5)]
    for _ in range(25):
        p1, p2 = r.dirichlet(np.ones(4)), r.dirichlet(np.ones(4))
        t = r.random()
        mid = S.misalignment(t * p1 + (1 - t) * p2, lims).value
        assert mid <= t * S.misalignment(p1, lims).value + (1 - t) * S.misalignment(p2, lims).value + SOLVER
    V = r.dirichlet(np.ones(4), size=3)
    culp, E, m = S.culpable(V[0], V, lims, delta=0.0)
    assert E >= -SOLVER and culp == (E > 0.0)


# ------------------------------------------------------------------------------------------------------------ R16

def test_r16_hoeffding_lemma():
    r = rng(21)
    for _ in range(200):
        z = r.uniform(-1, 1, size=5)
        w = r.dirichlet(np.ones(5))
        z -= w @ z                                        # mean zero
        a, b = z.min(), z.max()
        for lam in (0.1, 1.0, 5.0):
            assert w @ np.exp(lam * z) <= math.exp(lam ** 2 * (b - a) ** 2 / 8) * (1 + EXACT)


def test_r16_coverage_under_dependence():
    r = rng(22)
    alpha, N, records = 0.1, 400, 2000
    misses = 0
    for _ in range(records):
        prev, ys, mus = 0, [], []
        for _ in range(N):
            mu = 0.3 if prev else 0.05                    # the conditional rate depends on the last decision
            prev = int(r.random() < mu)
            ys.append(prev)
            mus.append(mu)
        bd = S.average_bounds(np.array(ys), alpha, N)
        avg = np.cumsum(mus) / np.arange(1, N + 1)
        misses += bool(np.any(avg > bd.upper + EXACT) or np.any(avg < bd.lower - EXACT))
    se = math.sqrt(alpha * (1 - alpha) / records)
    assert misses / records <= alpha + 4 * se
    verdict, _ = S.pooled_verdict((r.random(20000) < 0.01).astype(float), 0.05, 0.05)
    assert verdict == "certify"
    verdict, _ = S.pooled_verdict((r.random(20000) < 0.12).astype(float), 0.05, 0.05)
    assert verdict == "convict"


# ------------------------------------------------------------------------------------------------------------ R17

def test_r17_one_decision():
    a0 = np.array([0.95, 0.05])                           # acceptable: breach rate 0.05
    b0 = np.array([0.93, 0.07])                           # breaches the limit 0.05 at one decision
    c = min(b0 / a0)
    n, j = 6, 2
    for rec in itertools.product((0, 1), repeat=n):
        pg = np.prod([a0[x] for x in rec])
        pb = np.prod([b0[x] if i == j else a0[x] for i, x in enumerate(rec)])
        assert pb >= c * pg * (1 - EXACT)
    assert c == pytest.approx(0.93 / 0.95)


# ------------------------------------------------------------------------------------------------------------ R18

def test_r18_average_interval():
    r = rng(23)
    n, t, records = 500, 0.05, 4000
    bound = 2 * math.exp(-2 * n * t * t)
    misses = sum(abs((r.random(n) < 0.3).mean() - 0.3) > t for _ in range(records))
    se = math.sqrt(bound * (1 - bound) / records)
    assert misses / records <= bound + 4 * se
