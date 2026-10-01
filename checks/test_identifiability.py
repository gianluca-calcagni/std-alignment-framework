"""Checks of P11 (the misaligned share at the start of any change away from the default is sin²θ, or 1 against the
objective), P12 (what an intervention reveals: pass-through is identified from behaviour alone; a change outside
span{u, 1} shows the intervention moved more than it added; revealed objectives certify an actor's distinctions) and
P13 (the objective's average moves at the covariance rate; at the start, the gain per unit of departure is cos θ times
the objective's spread, and the shortfall is 1 − cos θ times it)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt, kl_tilts, random_partition
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
