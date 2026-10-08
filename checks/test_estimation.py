"""Checks of P21 (the expected evidence per decision is the KL divergence, so misalignment is the slowest rate of
evidence against the specification), P22 (detection: the Chernoff information is at most either KL), P23 (the
estimated misalignment of an actor that does pursue F is asymptotically χ² with |X| − 2 degrees of freedom; a light
simulation), P24 (the evaluation gap) and P37 (a strong incentive masks the actor, and can fake alignment)."""
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


def kl_stable(la, lb):
    """KL(a || b) from log-masses la, lb, as Σ b·h(la − lb) with h(d) = d·e^d − (e^d − 1) ≥ 0, accurate when a ≈ b."""
    d = la - lb
    h = np.where(np.abs(d) < 1e-4, d ** 2 / 2 + d ** 3 / 3, d * np.exp(d) - np.expm1(d))
    return float((np.exp(lb) * h).sum())


def log_tilt(lp, f):
    z = lp + f
    return z - (z.max() + np.log(np.exp(z - z.max()).sum()))


def test_a_strong_incentive_masks_the_actor_and_can_fake_alignment():
    """P37: under an intervention u with a unique largest outcome and gap γ, two actors' behaviours after it,
    tilt(p_i, φ·u), differ by KL = O(e^{−φγ}), with (1/φ)·log KL → −γ when their ratios differ at a runner-up; where u
    and F share their unique best outcome, misalignment tends to 0 as φ grows, while unevaluated conditions keep the
    actor's own; and where u's best outcome is not among F's, misalignment tends to −log sup_t p_{F,t}(x_u) > 0."""
    from scipy.optimize import minimize_scalar
    r = rng(3701)
    for _ in range(200):
        n = int(r.integers(3, 9)); u = r.normal(0, 1, n); xs = int(np.argmax(u))
        gamma = u[xs] - np.max(np.delete(u, xs)); d = u[xs] - u; others = np.arange(n) != xs
        p1, p2 = simplex_interior(r, n), simplex_interior(r, n)
        a1, a2 = p1 / p1[xs], p2 / p2[xs]; c = a1 * np.log(a1 / a2) - a1 + a2
        for kg in (40, 80):                                                          # the leading form
            k = kg / gamma
            K = kl_stable(log_tilt(np.log(p1), k * u), log_tilt(np.log(p2), k * u))
            lead = (np.exp(-k * d[others]) * c[others]).sum()
            assert abs(K - lead) <= 1e-9 * lead
        k = 400 / gamma                                                              # (1/φ)·log KL → −γ
        K = kl_stable(log_tilt(np.log(p1), k * u), log_tilt(np.log(p2), k * u))
        assert abs(np.log(K) / k + gamma) <= 0.05 * gamma
    for _ in range(100):                                                                 # fake alignment
        n = int(r.integers(3, 8)); q = simplex_interior(r, n); F = r.normal(0, 1, n); own = simplex_interior(r, n)
        u = r.normal(0, 1, n); best = int(np.argmax(F)); u[best] = u.max() + r.uniform(0.5, 2)  # shared best outcome
        def mis(kappa):                                                              # M, by a stable search over t
            lph = log_tilt(np.log(own), kappa * u)
            f = lambda z: float(np.exp(lph) @ (lph - log_tilt(np.log(q), np.exp(z) * F)))
            return min(f(-np.inf), minimize_scalar(f, bounds=(-10, 12), method="bounded",
                                                   options={"xatol": 1e-10}).fun)
        assert abs(mis(2.0) - misalignment(tilt(own, 2.0 * u), q, F)[0]) <= 1e-7      # agrees with the helper
        Ms = [mis(k) for k in (5.0, 50.0, 500.0)]
        assert Ms[1] <= Ms[0] + 1e-12 and Ms[2] <= Ms[1] + 1e-12 and Ms[2] <= 1e-3    # → 0 as φ grows
    for _ in range(100):                                                                 # reward hacking shows
        n = int(r.integers(3, 8)); q = simplex_interior(r, n); F = r.normal(0, 1, n); own = simplex_interior(r, n)
        u = r.normal(0, 1, n); xu = int(np.argmin(F)) if r.random() < 0.5 else int(np.argsort(F)[-2])
        u[xu] = u.max() + 2.0
        f = lambda t: -tilt(q, t * F)[xu]
        sup = max(-minimize_scalar(f, bounds=(0, 50), method="bounded", options={"xatol": 1e-12}).fun, q[xu])
        limit = -np.log(sup)
        M, _ = misalignment(tilt(own, 25.0 * u), q, F)
        assert limit > 0 and abs(M - limit) <= 1e-3 * (1 + limit)


def _root(dphi, R, hi=50.0, iters=90):
    """For each of R replicates, the s in [0, hi] where an increasing function dphi(s) crosses zero; 0 if dphi(0) >= 0
    (vectorized bisection: dphi maps an array of R values of s to R derivatives)."""
    lo, up = np.zeros(R), np.full(R, hi)
    for _ in range(iters):
        mid = 0.5 * (lo + up); neg = dphi(mid) < 0
        lo, up = np.where(neg, mid, lo), np.where(neg, up, mid)
    s = 0.5 * (lo + up)
    return np.where(dphi(np.zeros(R)) >= 0, 0.0, s)


def _weighted(counts, logw, F):
    """Per replicate: log Σ_x counts·e^{logw}, and the mean of F under the weights counts·e^{logw}."""
    a = np.where(counts > 0, np.log(np.maximum(counts, 1)) + logw, -np.inf)
    m = a.max(axis=1, keepdims=True); e = np.exp(a - m)
    return m[:, 0] + np.log(e.sum(axis=1)), (e @ F) / e.sum(axis=1)


def by_counts(C, q, F):
    """P52(i): the misalignment M(p̂) and revealed intensity of each empirical behaviour p̂ = C/n (rows of C)."""
    n = C.sum(axis=1)[:, None]; ph = C / n; R = len(C)
    s = _root(lambda s: _weighted(np.ones_like(ph), np.log(q) + s[:, None] * F, F)[1] - ph @ F, R)
    lw = np.log(q) + s[:, None] * F; lw = lw - _weighted(np.ones_like(ph), lw, F)[0][:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        M = np.where(ph > 0, ph * (np.log(ph) - lw), 0.0).sum(axis=1)
    return M, s


def by_log_ratios(C, l, F):
    """P52(ii): min_{s≥0} [mean ℓ − s·mean F + log mean e^{sF−ℓ}] over the draws counted in each row of C."""
    n = C.sum(axis=1); R = len(C)
    s = _root(lambda s: _weighted(C, s[:, None] * F - l, F)[1] - (C @ F) / n, R)
    return (C @ l) / n - s * (C @ F) / n + _weighted(C, s[:, None] * F - l, F)[0] - np.log(n)


def by_two_samples(C, Cq, l, F):
    """P52(iii): as by_log_ratios, with the normalizer averaged over the reference's draws counted in Cq."""
    n, m = C.sum(axis=1), Cq.sum(axis=1); R = len(C)
    s = _root(lambda s: _weighted(Cq, s[:, None] * F, F)[1] - (C @ F) / n, R)
    return (C @ l) / n - s * (C @ F) / n + _weighted(Cq, s[:, None] * F, F)[0] - np.log(m)


def test_what_a_sample_certifies_by_access():
    """P52: with log-ratios, the estimate is never negative, is exactly zero for an actor on the ray, and is zero only
    if the sampled log-ratios are affine in F; and (light simulation) n·Var of each estimate matches its limit law:
    Var_p(log w) by counts, with Var_p(F)/Var_{p°}(F)² for the revealed intensity; Var_p(w − log w) by log-ratios;
    Var_p(log w) + (n/m)·χ²(p°‖q) with draws of the default, which on the ray is negative about half the time."""
    r = rng(5201)
    for _ in range(200):                                                      # (ii): exact, for any sample
        k = int(r.integers(3, 8)); q = simplex_interior(r, k); F = r.normal(0, 2, k); n = int(r.integers(2, 60))
        on_ray = r.random() < 0.5
        p = tilt(q, r.uniform(0, 2) * F) if on_ray else simplex_interior(r, k); l = np.log(p / q)
        C = r.multinomial(n, p, size=20).astype(float)
        est = by_log_ratios(C, l, F)
        assert est.min() >= -1e-12
        if on_ray:
            assert est.max() <= 1e-12
        away = by_log_ratios(C, np.log(tilt(q, -r.uniform(0.5, 2) * F) / q), F)   # affine, but s < 0: not zero
        assert np.all(away[(C > 0).sum(axis=1) >= 2] > 1e-12)
        for row, e in zip(C, est):                                           # zero only if ℓ is affine in F
            seen = row > 0
            if seen.sum() >= 3:
                A = np.column_stack([np.ones(seen.sum()), F[seen]])
                resid = l[seen] - A @ np.linalg.lstsq(A, l[seen], rcond=None)[0]
                if np.abs(resid).max() > 1e-3:
                    assert e > 1e-12
    R, n = 800, 2000; tol = 5 * np.sqrt(2 / (R - 1))
    for k in (4, 6):                                                          # the laws, off the ray
        while True:
            q = simplex_interior(r, k); F = r.normal(0, 2, k); p = tilt(q, F + r.normal(0, 0.6, k))
            M, ts = misalignment(p, q, F)
            if 0.2 < ts < 3 and 0.02 < M < 0.5:
                break
        po = tilt(q, ts * F); w = po / p; l = np.log(p / q)
        var = lambda g, d: d @ g ** 2 - (d @ g) ** 2
        C = r.multinomial(n, p, size=R).astype(float); Cq = r.multinomial(n, q, size=R).astype(float)
        MA, tA = by_counts(C, q, F)
        assert abs(n * MA.var() / var(np.log(w), p) - 1) <= tol
        for c in (1, 3):                                       # the revealed intensity of c·F is t̂/c: the law scales
            assert abs(n * (tA / c).var() / (var(c * F, p) / var(c * F, po) ** 2) - 1) <= tol
        assert abs(n * by_log_ratios(C, l, F).var() / var(w - np.log(w), p) - 1) <= tol
        assert abs(n * by_two_samples(C, Cq, l, F).var() / (var(np.log(w), p) + var(po / q, q)) - 1) <= tol
    q = simplex_interior(r, 5); F = r.normal(0, 2, 5); p = tilt(q, 0.8 * F); l = np.log(p / q)   # (iii), on the ray
    C = r.multinomial(n, p, size=R).astype(float); Cq = r.multinomial(n, q, size=R).astype(float)
    est = by_two_samples(C, Cq, l, F); chi2 = q @ (p / q) ** 2 - 1
    assert abs(np.mean(est < 0) - 0.5) <= 5 * np.sqrt(0.25 / R)
    assert abs(n * est.var() / chi2 - 1) <= tol
