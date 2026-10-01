"""Checks of P21 (the expected evidence per decision is the KL divergence, so misalignment is the slowest rate of
evidence against the specification), P22 (detection: the Chernoff information is at most either KL), P23 (the
estimated misalignment of an actor that does pursue F is asymptotically χ² with |X| − 2 degrees of freedom; a light
simulation) and P24 (the evaluation gap)."""
import numpy as np
from scipy.optimize import minimize_scalar
from .common import EXACT, rng, simplex_interior, kl, tilt
from .test_misalignment import misalignment


def test_expected_evidence_is_misalignment():
    """P21: E_p[log(p/r)] = KL(p || r); against the ray of F, the expected evidence per decision is at least M(p̂), with
    equality at the nearest intended behaviour; and a sample's evidence per decision approaches it (light simulation)."""
    r = rng(2101)
    for _ in range(300):
        n = int(r.integers(2, 10)); p, q = simplex_interior(r, n), simplex_interior(r, n); F = r.normal(0, 1, n)
        assert abs(p @ np.log(p / q) - kl(p, q)) <= EXACT * (1 + kl(p, q))
        M, ts = misalignment(p, q, F)
        if not np.isfinite(ts):
            continue
        po = tilt(q, ts * F)
        assert abs(p @ np.log(p / po) - M) <= 1e-9 * (1 + M)
        for t in r.uniform(0, 5, 5):
            assert p @ np.log(p / tilt(q, t * F)) >= M - 1e-9 * (1 + M)
    for _ in range(20):                                                            # light simulation
        n = int(r.integers(3, 7)); p, q = simplex_interior(r, n), simplex_interior(r, n); F = r.normal(0, 1, n)
        M, ts = misalignment(p, q, F); po = tilt(q, ts * F)
        x = r.choice(n, size=4000, p=p); ev = np.log(p[x] / po[x])
        assert abs(ev.mean() - M) <= 5 * ev.std() / np.sqrt(x.size) + 1e-12


def chernoff(a, b):
    res = minimize_scalar(lambda lam: np.log(np.sum(a ** lam * b ** (1 - lam))), bounds=(0, 1), method="bounded",
                          options={"xatol": 1e-12})
    return -res.fun


def test_detection_is_capped_by_misalignment():
    """P22(ii), (iii): C(p̂, p) <= min(KL(p̂ || p), KL(p || p̂)); with p the nearest intended behaviour, C <= M(p̂);
    and the bound is nearly attained by a nearly deterministic actor."""
    r = rng(2201)
    for _ in range(300):
        n = int(r.integers(2, 10)); a, b = simplex_interior(r, n), simplex_interior(r, n)
        C = chernoff(a, b)
        assert 0 <= C + 1e-12 and C <= min(kl(a, b), kl(b, a)) * (1 + EXACT) + 1e-12
        q, F = simplex_interior(r, n), r.normal(0, 1, n)
        M, ts = misalignment(a, q, F)
        if np.isfinite(ts):
            assert chernoff(a, tilt(q, ts * F)) <= M * (1 + EXACT) + 1e-12
    for _ in range(50):                                          # the bound is sharp for a nearly deterministic actor
        n = int(r.integers(2, 8)); b = simplex_interior(r, n); x = int(r.integers(n))
        a = np.full(n, 1e-100); a[x] = 1.0; a /= a.sum()                       # the approach is slow, in log(1/ε)
        assert chernoff(a, b) >= 0.9 * min(kl(a, b), kl(b, a))


def test_estimated_misalignment_is_chi_squared():
    """P23 (light simulation): for an actor on the ray at an interior intensity, 2n·M(p̂_n) has mean close to
    |X| − 2, the mean of χ² with |X| − 2 degrees of freedom."""
    r = rng(2301)
    for k in (3, 5):
        q = simplex_interior(r, k); F = r.normal(0, 1, k); p = tilt(q, 0.8 * F); n = 2000
        stats = []
        for _ in range(300):
            ph = r.multinomial(n, p) / n
            stats.append(2 * n * misalignment(ph, q, F)[0])
        stats = np.array(stats); df = k - 2
        assert abs(stats.mean() - df) <= 5 * np.sqrt(2 * df / stats.size)


def test_the_evaluation_gap():
    """P24: on condition–outcome pairs, the misalignment at frequencies ρ is Σ_c ρ(c)·M_c (the frequencies cancel), and
    the expected evidence per decision at ρ_ev equals it; deployment exceeds evaluation by Γ = Σ_c (ρ_dep − ρ_ev)·M_c.
    Notes: under one shared intensity, misalignment is at least Σ_c ρ(c)·M_c, concave in ρ, and Γ misses the gap."""
    r = rng(2401); missed = 0
    for _ in range(200):
        nc, n = int(r.integers(2, 6)), int(r.integers(2, 8))
        rho_ev, rho_dep = simplex_interior(r, nc), simplex_interior(r, nc)
        qs, ps, Fs, pos, Ms = [], [], [], [], []
        for _ in range(nc):
            q, p, F = simplex_interior(r, n), simplex_interior(r, n), r.normal(0, 1, n)
            M, ts = misalignment(p, q, F)                                             # ts is finite: p ∈ Δ°
            qs.append(q); ps.append(p); Fs.append(F); pos.append(tilt(q, ts * F)); Ms.append(M)
        Ms = np.array(Ms); tol = 1e-9 * (1 + Ms.max())
        for rho in (rho_ev, rho_dep):
            joint = np.concatenate([rho[c] * ps[c] for c in range(nc)])               # pairs (c, x)
            nearest = np.concatenate([rho[c] * pos[c] for c in range(nc)])
            assert abs(kl(joint, nearest) - rho @ Ms) <= tol
            assert abs(joint @ np.log(joint / nearest) - rho @ Ms) <= tol             # the expected evidence
            other = np.concatenate([rho[c] * tilt(qs[c], r.uniform(0, 3) * Fs[c]) for c in range(nc)])
            assert kl(joint, other) >= rho @ Ms - tol                                 # no intended pair does better
        gap = rho_dep @ Ms - rho_ev @ Ms
        assert abs(gap - (rho_dep - rho_ev) @ Ms) <= EXACT * (1 + Ms.max())
        def shared(rho):                                                              # one intensity for all conditions
            f = lambda t: sum(rho[c] * kl(ps[c], tilt(qs[c], t * Fs[c])) for c in range(nc))
            return min(minimize_scalar(f, bounds=(0, 200), method="bounded", options={"xatol": 1e-12}).fun, f(0.0))
        s_ev, s_dep, s_mid = shared(rho_ev), shared(rho_dep), shared(0.5 * (rho_ev + rho_dep))
        assert s_ev >= rho_ev @ Ms - tol and s_dep >= rho_dep @ Ms - tol
        assert s_mid >= 0.5 * (s_ev + s_dep) - 1e-7
        missed += abs((s_dep - s_ev) - gap) > 1e-4
    assert missed >= 100                                                              # Γ does not give the shared gap
