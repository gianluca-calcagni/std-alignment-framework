"""Checks of P4 (KL is the value lost against a pursuit; every behaviour is the optimum of its own objective; the chain
rule; merging outcomes never increases KL; and, for the Notes, three other divergences break the chain rule) and P14
(the cost of departing from the default can only be KL)."""
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


# ---- P14: the cost is forced -------------------------------------------------------------------------------------
# The best trade-off at p is stationary there: for every tangent v, Σ_x (t·F(x) − ∂_x c(p))·v(x) = 0, that is,
# t·F − ∇c(p) is constant across outcomes. The gradients below are those of each cost, as a function of p.
GRADIENTS = {
    "KL": lambda p, q: np.log(p / q) + 1,
    "reverse KL": lambda p, q: -q / p,
    "chi squared": lambda p, q: 2 * (p - q) / q,
    "squared Hellinger": lambda p, q: 1 - np.sqrt(q / p),
}


def spread(v):
    return float(np.ptp(v))


def residual_from_span(g, F):
    """The distance of g from span{F, 1}, by least squares."""
    B = np.stack([F, np.ones_like(F)], 1)
    return float(np.linalg.norm(g - B @ np.linalg.lstsq(B, g, rcond=None)[0]))


def test_the_cost_is_forced():
    """P14: at the pursuit p_{F,t}, t·F − ∇c is constant for the KL cost, and for no cost that differs from KL by a
    non-constant gradient; χ², reverse KL and squared Hellinger are not stationary at any point of the ray (n >= 3)."""
    r = rng(1401)
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t = float(r.uniform(0.2, 4))
        p = tilt(q, t * F); scale = 1 + t * np.abs(F).max()
        assert spread(t * F - GRADIENTS["KL"](p, q)) <= 1e-9 * scale              # KL: the pursuit is stationary
        h = r.normal(0, 1, n)                                                      # KL + E_p[h]: it is not
        assert spread(t * F - (GRADIENTS["KL"](p, q) + h)) >= 0.5 * spread(h)
        bend = residual_from_span(F ** 2, F)                                       # how far F is from two-valued
        for name in ("reverse KL", "chi squared", "squared Hellinger"):
            for s in np.linspace(0.05, 6, 25):                                     # nowhere on the ray
                g = GRADIENTS[name](tilt(q, s * F), q)
                # these costs agree with KL to second order at q, so the gap grows like s²; the margin is 60-fold
                assert residual_from_span(g, F) > 1e-4 * s * s * bend, (name, s)


def test_a_function_of_kl_moves_only_the_intensity():
    """P14 Notes: with the cost KL + KL², the best trade-off at price 1/t is still on the ray, at the intensity t' with
    t' (1 + 2 KL(p_{F,t'} || q)) = t; so only the reading of t as the inverse price singles out KL."""
    from scipy.optimize import minimize
    r = rng(1402)
    for _ in range(40):
        n = int(r.integers(3, 7)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t = float(r.uniform(0.5, 3))
        soft = lambda z: np.exp(z - z.max()) / np.exp(z - z.max()).sum()
        cost = lambda p: kl(p, q) + kl(p, q) ** 2
        z = minimize(lambda z: -(soft(z) @ F - cost(soft(z)) / t), np.log(q), method="BFGS",
                     options={"gtol": 1e-12, "maxiter": 5000}).x
        p = soft(z)
        t_prime = t / (1 + 2 * kl(p, q))
        assert kl(p, tilt(q, t_prime * F)) <= 1e-9                                 # on the ray, at t'
        assert t_prime < t * (1 - 1e-3) or kl(p, q) < 1e-4                        # and not at t
