"""Checks of P11 (the misaligned share at the start of any change away from the default is sin²θ, or 1 against the
objective), P12 (what an intervention reveals: pass-through is identified from behaviour alone; a change outside
span{u, 1} shows the intervention moved more than it added; revealed objectives certify an actor's distinctions) and
P13 (the objective's average moves at the covariance rate; at the start, the gain per unit of departure is cos θ times
the objective's spread, and the shortfall is 1 − cos θ times it), P16 (an actor cannot behave more differently in two
conditions than its view tells them apart) and P17 (what an unobserved condition can hide)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt, kl, kl_tilts, log_normalizer, random_partition
from .test_misalignment import ray_minimizer
from .test_stakes import matched_intensity


def var(q, G):
    return q @ G ** 2 - (q @ G) ** 2


def cov(q, A, B):
    return q @ (A * B) - (q @ A) * (q @ B)


def share(q, a, F):
    """M / KL(p || q) for p = tilt(q, a), with both KLs between tilts computed in closed form."""
    ts = ray_minimizer(tilt(q, a), q, F)
    return kl_tilts(q, a, ts * F) / kl_tilts(q, a, np.zeros_like(a))


def test_initial_share_is_sin_squared():
    """P11: along p_s = tilt(q, sG + s²H), M(p_s)/KL(p_s || q) -> sin²θ if cos θ >= 0 and -> 1 if cos θ < 0, at first
    order in s."""
    r = rng(801); seen = {"with": 0, "against": 0}
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n)
        F, G, H = r.normal(0, 1, n), r.normal(0, 1, n), r.normal(0, 1, n)
        c = cov(q, G, F) / np.sqrt(var(q, G) * var(q, F))
        if abs(c) < 0.05:
            continue
        target = 1 - c ** 2 if c > 0 else 1.0
        e3, e4 = (abs(share(q, s * G + s * s * H, F) - target) for s in (1e-3, 1e-4))
        if c > 0:
            seen["with"] += 1
            assert e4 <= 2e-3                                                    # close at small departures
            assert e4 <= 0.2 * e3 + 1e-9                                         # and closer, at first order
        else:
            seen["against"] += 1
            assert e3 <= 1e-9 and e4 <= 1e-9                                     # exactly 1: all of it is misaligned
    assert min(seen.values()) >= 50


def test_pass_through_is_identified_from_behaviour_alone():
    """P12(i): if p' = tilt(p, φu), the coefficient of u in log(p'/p) is φ and the residual from span{u, 1} is 0; if the
    intervention also moves the objective (p' = tilt(p, φu + δ)), the residual is positive."""
    r = rng(802)
    for _ in range(300):
        n = int(r.integers(3, 12)); p = simplex_interior(r, n); u = r.normal(0, 1, n); phi = float(r.normal(0, 2))
        B = np.stack([u, np.ones(n)], 1)
        change = np.log(tilt(p, phi * u) / p)
        coef, *_ = np.linalg.lstsq(B, change, rcond=None)
        assert abs(coef[0] - phi) <= 1e-9 * (1 + abs(phi))
        assert np.linalg.norm(change - B @ coef) <= 1e-9 * (1 + np.abs(change).max())
        delta = r.normal(0, 0.3, n)
        moved = np.log(tilt(p, phi * u + delta) / p)
        res = moved - B @ np.linalg.lstsq(B, moved, rcond=None)[0]
        exp_res = delta - B @ np.linalg.lstsq(B, delta, rcond=None)[0]       # the part of δ outside span{u, 1}
        assert abs(np.linalg.norm(res) - np.linalg.norm(exp_res)) <= 1e-9
        if np.linalg.norm(exp_res) > 1e-3:
            assert np.linalg.norm(res) > 1e-4


def test_revealed_objectives_certify_distinctions():
    """P12(ii): if every behaviour along a path splits each cell in fixed proportions, every revealed objective is
    constant on the cells; a revealed objective that separates two outcomes means their ratio moved."""
    r = rng(803)
    H = 1e-30
    for _ in range(200):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1
        base = simplex_interior(r, n); a, b = r.normal(0, 1, k), r.normal(0, 1, k)
        path = lambda s: (lambda z: np.exp(z - z.real.max()) / np.exp(z - z.real.max()).sum())(
            np.log(base) + (s * a + s * s * b)[labels])                            # cell-constant tilts of base
        for s in r.uniform(-2, 2, 3):
            Fs = np.imag(np.log(path(s + 1j * H))) / H
            for c in range(k):
                assert np.ptp(Fs[labels == c]) <= EXACT * (1 + np.abs(Fs).max())
            ps = path(s).real
            for c in range(k):                                                   # and the within-cell split is fixed
                m = labels == c
                assert np.max(np.abs(ps[m] / ps[m].sum() - base[m] / base[m].sum())) <= EXACT
        # a path that moves a ratio inside a cell reveals an objective that separates those outcomes
        c = int(np.argmax(np.bincount(labels)))
        idx = np.flatnonzero(labels == c)
        if idx.size >= 2:
            w = np.zeros(n); w[idx[0]] = 1.0
            path2 = lambda s: (lambda z: np.exp(z - z.real.max()) / np.exp(z - z.real.max()).sum())(np.log(base) + s * w)
            Fs = np.imag(np.log(path2(0.3 + 1j * H))) / H
            assert abs(Fs[idx[0]] - Fs[idx[1]]) > 0.5


def test_average_moves_at_the_covariance_rate():
    """P13(i): along any smooth path, d/ds E_{p_s}[F] = Cov_{p_s}(F_s, F), at every s, not only at the start."""
    r = rng(804)
    H = 1e-30
    for _ in range(300):
        n = int(r.integers(2, 12)); q = simplex_interior(r, n); F, G, K = (r.normal(0, 1, n) for _ in range(3))
        a = lambda s: s * G + s * s * K + 0.3 * np.sin(s) * F                    # a curved path through q
        for s in r.uniform(-2, 2, 3):
            z = np.log(q) + a(s + 1j * H); z = z - z.real.max()
            p = np.exp(z) / np.exp(z).sum()
            rate = np.imag(p @ F) / H                                            # d/ds E_{p_s}[F], by complex step
            Fs, ps = np.imag(np.log(p)) / H, p.real                              # the revealed objective at s
            assert abs(rate - cov(ps, Fs, F)) <= EXACT * (1 + abs(rate) + np.abs(F).max())


def test_start_gains_cos_theta_of_the_spread():
    """P13(ii): along p_s = tilt(q, sG + s²H), the gain in F per unit of (2 KL(p_s || q))^{1/2} tends to cos θ σ_q(F),
    and the shortfall per unit tends to (1 − cos θ) σ_q(F), at first order in s."""
    r = rng(805); signs = {"with": 0, "against": 0}
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F, G, K = (r.normal(0, 1, n) for _ in range(3))
        sF = np.sqrt(var(q, F)); c = cov(q, G, F) / np.sqrt(var(q, G) * var(q, F))
        errors = []
        for s in (1e-3, 1e-4):
            a = s * G + s * s * K; p = tilt(q, a); unit = np.sqrt(2 * kl_tilts(q, a, np.zeros(n)))
            lam = matched_intensity(p, q, F)
            assert np.isfinite(lam)
            gain, short = (p @ F - q @ F) / unit, (tilt(q, lam * F) @ F - p @ F) / unit
            errors.append((abs(gain - c * sF), abs(short - (1 - c) * sF)))
        for e3, e4 in zip(*errors):
            assert e4 <= 1e-2 * sF                                               # close at small departures
            assert e4 <= 0.2 * e3 + 1e-9                                         # and closer, at first order
        signs["with" if c > 0 else "against"] += 1
    assert min(signs.values()) >= 100


def actor(r, nw, nz, nx):
    """Random inputs in two conditions (W_a, W_d), a view of the input (a channel K), and behaviours π_z."""
    W_a, W_d = simplex_interior(r, nw), simplex_interior(r, nw)
    K = np.array([simplex_interior(r, nz) for _ in range(nw)])
    pi = np.array([tilt(simplex_interior(r, nx), r.normal(0, 3, nx)) for _ in range(nz)])
    return W_a, W_d, K, pi


def test_identical_views_give_identical_behaviour():
    """P16(i): two conditions whose inputs differ, but which the actor's view does not separate (the channel sends the
    differing inputs to the same signal distribution), give the same behaviour, whatever the behaviours π_z."""
    r = rng(1601)
    for _ in range(300):
        nw, nz, nx = (int(v) for v in r.integers(3, 8, 3))
        W_a, _, K, pi = actor(r, nw, nz, nx)
        K[1] = K[0]                                                                # inputs 0 and 1 look alike
        rest = 0.6 * simplex_interior(r, nw - 2)                                   # inputs 0 and 1 carry 0.4
        W_a = np.concatenate([[0.32, 0.08], rest]); W_d = np.concatenate([[0.08, 0.32], rest])
        assert kl(W_d, W_a) > 0.3                                                  # the conditions do differ
        assert np.abs((W_d @ K) @ pi - (W_a @ K) @ pi).max() <= EXACT


def test_behaviour_differs_no_more_than_views():
    """P16(ii), (iii): KL(p_d || p_a) <= KL(V_d || V_a) <= KL(W_d || W_a), for any behaviours and any channel."""
    r = rng(1602)
    for _ in range(2000):
        W_a, W_d, K, pi = actor(r, *r.integers(2, 8, 3))
        V_a, V_d = W_a @ K, W_d @ K
        assert kl(V_d @ pi, V_a @ pi) <= kl(V_d, V_a) * (1 + EXACT) + EXACT
        assert kl(V_d, V_a) <= kl(W_d, W_a) * (1 + EXACT) + EXACT


def departure_from(p0, G, lam):
    return float(lam * (tilt(p0, lam * G) @ G) - log_normalizer(p0, lam * G))


def extreme(p0, G, eps):
    """The largest E_p[G] over {p : KL(p || p0) <= eps}: the pursuit of G from p0 with departure eps, or max G."""
    if eps >= -np.log(p0[G >= G.max()].sum()):
        return float(G.max())
    lo, hi = 0.0, 1.0
    while departure_from(p0, G, hi) < eps:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if departure_from(p0, G, mid) < eps else (lo, mid)
    return float(tilt(p0, lo * G) @ G)


def test_what_an_unobserved_condition_can_hide():
    """P17(ii): E_{p_d}[F] lies between the pursuits of −F and F from p_a with departure ε = KL(V_d || V_a); the bound
    is attained (an actor that acts out its view, π_z = δ_z, with V_d the pursuit of −F from V_a); and ε = 0 identifies
    the behaviour in d."""
    r = rng(1603); used = []
    for _ in range(2000):
        W_a, W_d, K, pi = actor(r, *r.integers(2, 8, 3))
        V_a, V_d = W_a @ K, W_d @ K
        p_a, p_d = V_a @ pi, V_d @ pi
        eps = kl(V_d, V_a); F = r.normal(0, 1, p_a.size)
        hi, lo = extreme(p_a, F, eps), -extreme(p_a, -F, eps)
        assert lo - 1e-9 <= p_d @ F <= hi + 1e-9
        used.append(max(p_d @ F - p_a @ F, 0) / (hi - p_a @ F) + max(p_a @ F - p_d @ F, 0) / (p_a @ F - lo))
    assert max(used) > 0.9                                                         # random actors come close
    for _ in range(200):                                                           # and one attains it
        n = int(r.integers(2, 8)); V_a = simplex_interior(r, n); F = r.normal(0, 1, n); lam = float(r.uniform(0.1, 3))
        V_d = tilt(V_a, -lam * F); pi = np.eye(n)                                  # the actor acts out its view
        eps = kl(V_d, V_a)
        assert abs((V_d @ pi) @ F + extreme(V_a, -F, eps)) <= 1e-9
