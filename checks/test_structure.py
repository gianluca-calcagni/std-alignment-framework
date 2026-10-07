"""Checks of P39 (coordination), P40 (attention), P41 (reversibility) and P42 (several principals). Each claim is
computed by a helper below, so that breaking a helper on purpose makes its checks fail."""
import itertools
import numpy as np
from scipy.optimize import minimize
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt, log_normalizer
from .test_misalignment import misalignment


def marginals(p, shape):
    P = p.reshape(shape)
    return [P.sum(axis=tuple(j for j in range(len(shape)) if j != i)) for i in range(len(shape))]


def product(factors):
    out = factors[0]
    for f in factors[1:]:
        out = np.multiply.outer(out, f)
    return out.ravel()


def coordination(p, shape):
    """K(p) = KL(p || product of its marginals)."""
    return kl(p, product(marginals(p, shape)))


def midpoint(F):
    """m = (F + F^T)/2, the reversible behaviour nearest to F."""
    return (F + F.T) / 2


def nearest_reversible_chain(P, pi):
    """R(x, y) = m(x, y)/pi(x), with m the midpoint of the flux pi(x)·P(x, y)."""
    return midpoint(pi[:, None] * P) / pi[:, None]


def pooled(q, Fs, ts, w):
    """The compromise of principals with declared intensities: the pursuit of G = sum_k w_k t_k F_k at intensity 1."""
    return tilt(q, sum(wk * tk * F for wk, tk, F in zip(w, ts, Fs)))


def test_coordination_splits_misalignment():
    """P39(i), (ii): KL to a product splits into coordination plus the actors' own divergences; under independent
    pursuit, misalignment is coordination plus the actors' own misalignments, found here by minimizing over all
    intensities jointly; coordination is zero exactly on products."""
    r = rng(3901)
    done = 0
    for _ in range(300):
        shape = tuple(int(r.integers(2, 4)) for _ in range(int(r.integers(2, 4))))
        n = int(np.prod(shape))
        p = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        rs = [simplex_interior(r, s) for s in shape]
        lhs = kl(p, product(rs))
        rhs = coordination(p, shape) + sum(kl(pi, ri) for pi, ri in zip(marginals(p, shape), rs))
        assert abs(lhs - rhs) <= EXACT * (1 + lhs)
        assert coordination(product(rs), shape) <= EXACT                              # zero on products
        qs = [simplex_interior(r, s) for s in shape]; Fs = [r.normal(0, 1, s) for s in shape]
        ms = marginals(p, shape)
        if any(m @ F >= F.max() - 1e-6 for m, F in zip(ms, Fs)) or len(shape) > 2:
            continue                                                                  # interior cases, two actors
        own = sum(misalignment(m, q, F)[0] for m, q, F in zip(ms, qs, Fs))
        joint = lambda z: kl(p, product([tilt(q, zi * zi * F) for zi, q, F in zip(z, qs, Fs)]))   # t = z² >= 0
        best = min(joint(np.array(z0)) for z0 in itertools.product((0.0, 1.0), repeat=2))
        for z0 in itertools.product((0.3, 1.0, 2.0), repeat=2):
            best = min(best, minimize(joint, np.array(z0), method="Nelder-Mead",
                                      options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 4000}).fun)
        target = coordination(p, shape) + own
        assert best >= target - 1e-9 * (1 + target)                                  # nothing jointly does better
        assert best <= target + 1e-6 * (1 + target)                                  # and the split is reached
        done += 1
    assert done >= 50


def test_coordination_can_hide_in_time():
    """P39(iii): the two-round construction has coordination 0 in each round and 2·log 2 over both; and two
    tit-for-tat players with 5% errors, in their stationary law, show none within a round and some across rounds."""
    # z1, z2 fair coins; actor 1 plays (z1, z2), actor 2 plays (z2, z1). Index a joint outcome by (a1, a2) over rounds.
    joint_two = np.zeros((4, 4))
    for z1, z2 in itertools.product((0, 1), repeat=2):
        joint_two[2 * z1 + z2, 2 * z2 + z1] += 0.25
    round1 = np.zeros((2, 2)); round2 = np.zeros((2, 2))
    for z1, z2 in itertools.product((0, 1), repeat=2):
        round1[z1, z2] += 0.25; round2[z2, z1] += 0.25
    assert coordination(round1.ravel(), (2, 2)) <= EXACT and coordination(round2.ravel(), (2, 2)) <= EXACT
    assert abs(coordination(joint_two.ravel(), (4, 4)) - 2 * np.log(2)) <= EXACT
    eps = 0.05; S = list(itertools.product((0, 1), (0, 1))); P = np.zeros((4, 4))
    for i, (a1, a2) in enumerate(S):
        for j, (b1, b2) in enumerate(S):
            P[i, j] = (1 - eps if b1 == a2 else eps) * (1 - eps if b2 == a1 else eps)
    pi = np.full(4, 0.25)                                                             # P is doubly stochastic
    assert np.abs(pi @ P - pi).max() <= EXACT
    assert coordination(pi, (2, 2)) <= EXACT                                          # within a round: none
    two = np.zeros((4, 4))                                                            # (a1_t, a1_t+1) x (a2_t, a2_t+1)
    for i, (a1, a2) in enumerate(S):
        for j, (b1, b2) in enumerate(S):
            two[2 * a1 + b1, 2 * a2 + b2] += pi[i] * P[i, j]
    assert coordination(two.ravel(), (4, 4)) > 0.1                                    # across two rounds: some


def test_attention_is_mutual_information():
    """P40: the compensation identity; the minimizer over condition-free behaviours is the average behaviour, found
    here by direct minimization; the value is the mutual information of the pair behaviour; zero when every condition
    gets the same behaviour."""
    r = rng(4001)
    for _ in range(100):
        C, n = int(r.integers(2, 6)), int(r.integers(2, 7))
        rho = simplex_interior(r, C); Ps = np.array([simplex_interior(r, n) for _ in range(C)])
        avg = rho @ Ps
        att = float(sum(rc * kl(pc, avg) for rc, pc in zip(rho, Ps)))
        for _ in range(3):
            rr = simplex_interior(r, n)
            lhs = float(sum(rc * kl(pc, rr) for rc, pc in zip(rho, Ps)))
            assert abs(lhs - att - kl(avg, rr)) <= EXACT * (1 + lhs)
        obj = lambda z: float(sum(rc * kl(pc, tilt(np.full(n, 1 / n), z)) for rc, pc in zip(rho, Ps)))
        found = minimize(obj, r.normal(0, 1, n), method="BFGS", options={"gtol": 1e-12})
        assert abs(found.fun - att) <= 1e-9 * (1 + att)
        joint = (rho[:, None] * Ps).ravel()
        assert abs(kl(joint, product([rho, avg])) - att) <= EXACT * (1 + att)        # mutual information
        same = np.tile(Ps[0], (C, 1))
        assert sum(rc * kl(pc, rho @ same) for rc, pc in zip(rho, same)) <= EXACT
        assert att > 1e-6                                                              # the case is exercised


def test_reversibility_misalignment_is_jensen_shannon():
    """P41(i): for every reversible W, KL(F || W) = KL(F || m) + KL(m || W); direct minimization over reversible
    behaviours finds KL(F || m); and KL(F || m) is the Jensen-Shannon divergence between F and its reversal."""
    r = rng(4101)
    for _ in range(100):
        s = int(r.integers(2, 6)); n = s * s
        F = (with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)).reshape(s, s)
        m = midpoint(F)
        for _ in range(3):
            W = simplex_interior(r, n).reshape(s, s); W = (W + W.T) / 2
            lhs = kl(F.ravel(), W.ravel())
            assert abs(lhs - kl(F.ravel(), m.ravel()) - kl(m.ravel(), W.ravel())) <= EXACT * (1 + lhs)
        iu = np.triu_indices(s)
        def obj(z):
            W = np.zeros((s, s)); W[iu] = np.exp(z); W = W + W.T - np.diag(np.diag(W))
            return kl(F.ravel(), (W / W.sum()).ravel())
        found = min((minimize(obj, r.normal(0, 1, len(iu[0])), method="BFGS", options={"gtol": 1e-12})
                     for _ in range(2)), key=lambda res: res.fun)
        target = kl(F.ravel(), m.ravel())
        assert found.fun >= target - 1e-9 * (1 + target)
        assert found.fun <= target + 1e-7 * (1 + target)
        js = 0.5 * kl(F.ravel(), m.ravel()) + 0.5 * kl(F.T.ravel(), m.ravel())
        assert abs(js - target) <= EXACT * (1 + target)


def test_entropy_production_bounds_and_the_quarter_law():
    """P41(ii), (iii): misalignment against reversibility is at most half the entropy production, and the ratio tends
    to 1/4 as the asymmetry vanishes."""
    r = rng(4102)
    for _ in range(200):
        s = int(r.integers(2, 6)); F = simplex_interior(r, s * s).reshape(s, s)
        M, e = kl(F.ravel(), midpoint(F).ravel()), kl(F.ravel(), F.T.ravel())
        assert M <= e / 2 + EXACT * (1 + e)
        assert M < e / 2 - 1e-6                                                       # strict on generic instances
    for _ in range(50):
        s = int(r.integers(2, 6)); base = simplex_interior(r, s * s).reshape(s, s); m = (base + base.T) / 2
        A = r.normal(0, 1, (s, s)); A = A - A.T
        A *= 0.5 / np.abs(A / m).max()                                                # |h·A/m| <= h/2: positive for h <= 1
        # The odd terms cancel (A is antisymmetric, m symmetric): the ratio is 1/4·(1 − h²·S4/(6·S2)) + O(h⁴), with
        # S2 = Σ A²/m and S4 = Σ A⁴/m³. A is scaled relative to m, so the h² term stays far above rounding.
        ratios = [kl((m + h * A).ravel(), m.ravel()) / kl((m + h * A).ravel(), (m - h * A).ravel()) for h in (0.3, 0.03)]
        assert abs(ratios[-1] - 0.25) <= 1e-3
        assert abs(ratios[-1] - 0.25) <= 0.05 * abs(ratios[0] - 0.25) + 1e-9           # shrinking like h²


def test_the_nearest_reversible_chain():
    """P41(iv): direct minimization of the KL rate over chains reversible with respect to some distribution finds
    KL(F || m), and the chain with flux m attains it."""
    r = rng(4103)
    for _ in range(40):
        s = int(r.integers(3, 6))                                                     # every 2-state chain is reversible
        P = np.array([simplex_interior(r, s) for _ in range(s)])
        ev, V = np.linalg.eig(P.T); pi = np.real(V[:, np.argmin(np.abs(ev - 1))]); pi = pi / pi.sum()
        F = pi[:, None] * P; target = kl(F.ravel(), midpoint(F).ravel())
        rate = lambda R: float(np.sum(F * np.log(P / R)))
        R = nearest_reversible_chain(P, pi)
        assert np.abs(R.sum(1) - 1).max() <= EXACT
        assert np.abs(pi[:, None] * R - (pi[:, None] * R).T).max() <= EXACT          # reversible w.r.t. pi
        assert abs(rate(R) - target) <= EXACT * (1 + target)
        iu = np.triu_indices(s)
        def obj(z):
            W = np.zeros((s, s)); W[iu] = np.exp(z); W = W + W.T - np.diag(np.diag(W))
            return rate(W / W.sum(1, keepdims=True))
        found = min((minimize(obj, r.normal(0, 1, len(iu[0])), method="BFGS", options={"gtol": 1e-12})
                     for _ in range(3)), key=lambda res: res.fun)
        assert found.fun >= target - 1e-9 * (1 + target)
        assert found.fun <= target + 1e-7 * (1 + target)
        assert target > 1e-6                                                           # the case is exercised


def test_gridlock():
    """P42(i): the default has misalignment 0 under every standard specification, while behaviours off the rays are
    misaligned for some principal."""
    r = rng(4201)
    for _ in range(100):
        n = int(r.integers(3, 9)); K = int(r.integers(2, 5))
        q = simplex_interior(r, n); Fs = [r.normal(0, 1, n) for _ in range(K)]; w = simplex_interior(r, K)
        assert sum(wk * misalignment(q, q, F)[0] for wk, F in zip(w, Fs)) <= EXACT
        p = simplex_interior(r, n)
        if any(p @ F >= F.max() - 1e-6 for F in Fs):
            continue
        assert sum(wk * misalignment(p, q, F)[0] for wk, F in zip(w, Fs)) > 1e-6


def test_pooling_with_declared_intensities():
    """P42(ii): the identity for every behaviour, and the pooled pursuit as the minimizer, found by direct
    minimization."""
    r = rng(4202)
    for _ in range(100):
        n = int(r.integers(3, 9)); K = int(r.integers(2, 5))
        q = simplex_interior(r, n); Fs = [r.normal(0, 1, n) for _ in range(K)]
        ts = r.uniform(0, 3, K); w = simplex_interior(r, K)
        pk = [tilt(q, t * F) for t, F in zip(ts, Fs)]
        G = sum(wk * tk * F for wk, tk, F in zip(w, ts, Fs))
        const = sum(wk * log_normalizer(q, tk * F) for wk, tk, F in zip(w, ts, Fs)) - log_normalizer(q, G)
        best = pooled(q, Fs, ts, w)
        for _ in range(3):
            p = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
            lhs = sum(wk * kl(p, pp) for wk, pp in zip(w, pk))
            assert abs(lhs - kl(p, best) - const) <= EXACT * (1 + lhs)
        obj = lambda z: sum(wk * kl(tilt(q, z), pp) for wk, pp in zip(w, pk))
        found = minimize(obj, r.normal(0, 1, n), method="BFGS", options={"gtol": 1e-12})
        assert abs(found.fun - const) <= 1e-9 * (1 + const)
        assert np.abs(tilt(q, found.x) - best).max() <= 1e-5
