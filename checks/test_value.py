"""Checks of P3: KL is the value lost against a pursuit; every behaviour is the optimum of its own objective; the chain
rule; merging outcomes never increases KL. And, for the Notes: three other divergences break the chain rule."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt, random_partition, coarse


def J(p, F, q, t):
    return p @ F - kl(p, q) / t


def test_value_identity():
    r = rng(301)
    for _ in range(1000):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 2, n); t = float(np.exp(r.uniform(-3, 3)))
        star = tilt(q, t * F)
        p = with_zeros(r, n) if r.random() < 0.5 else simplex_interior(r, n)
        lhs, rhs = J(star, F, q, t) - J(p, F, q, t), kl(p, star) / t
        assert abs(lhs - rhs) <= EXACT * (1 + abs(J(star, F, q, t)) + abs(J(p, F, q, t)))
        assert rhs >= 0


def test_every_behaviour_is_an_optimum():
    """P4(ii): at intensity 1, r is the optimum for the objective log(r/q), and KL(p||r) is exactly the value p loses."""
    r = rng(302)
    for _ in range(300):
        n = int(r.integers(2, 13)); q, target = simplex_interior(r, n), simplex_interior(r, n)
        F = np.log(target / q)                                                   # the objective the target pursues
        assert np.max(np.abs(tilt(q, F) - target)) <= EXACT
        best = J(target, F, q, 1.0)
        for _ in range(20):
            p = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
            loss = best - J(p, F, q, 1.0)
            assert abs(loss - kl(p, target)) <= EXACT * (1 + abs(best) + abs(J(p, F, q, 1.0)))


def chain_gap(D, p, rr, labels):
    """D(p||r) minus [D(coarse) + sum_C p(C) D(conditionals)], for a divergence D."""
    pc, rc = coarse(p, labels), coarse(rr, labels); within = 0.0
    for c in range(labels.max() + 1):
        m = labels == c
        if pc[c] > 0:
            within += pc[c] * D(p[m] / pc[c], rr[m] / rc[c])
    return D(p, rr) - (D(pc, rc) + within)


def test_chain_rule():
    r = rng(303)
    for _ in range(1000):
        n = int(r.integers(3, 13)); labels = random_partition(r, n); rr = simplex_interior(r, n)
        p = with_zeros(r, n) if r.random() < 0.5 else simplex_interior(r, n)
        assert abs(chain_gap(kl, p, rr, labels)) <= EXACT * (1 + kl(p, rr))


def test_merging_never_increases():
    r = rng(304)
    for _ in range(1000):
        n = int(r.integers(3, 13)); labels = random_partition(r, n); rr = simplex_interior(r, n); p = simplex_interior(r, n)
        gap = kl(p, rr) - kl(coarse(p, labels), coarse(rr, labels))
        assert gap >= -EXACT * (1 + kl(p, rr))
        spread = max(np.ptp(np.log(p / rr)[labels == c]) for c in range(labels.max() + 1))
        if spread > 0.1:                                                         # p/r not constant on some cell
            assert gap > 1e-12
        # equality case: r' = p times a factor constant on each cell
        f = np.exp(r.normal(0, 1, labels.max() + 1))[labels]; r2 = p * f / (p * f).sum()
        assert abs(kl(p, r2) - kl(coarse(p, labels), coarse(r2, labels))) <= EXACT * (1 + kl(p, r2))


def test_other_divergences_break_the_chain_rule():
    chi2 = lambda p, rr: float(np.sum((p - rr) ** 2 / rr))
    hellinger2 = lambda p, rr: float(np.sum((np.sqrt(p) - np.sqrt(rr)) ** 2))
    tv = lambda p, rr: float(0.5 * np.abs(p - rr).sum())
    r = rng(305)
    for D in (chi2, hellinger2, tv):
        worst = 0.0
        for _ in range(200):
            n = int(r.integers(3, 13)); labels = random_partition(r, n)
            worst = max(worst, abs(chain_gap(D, simplex_interior(r, n), simplex_interior(r, n), labels)))
        assert worst > 1e-2
