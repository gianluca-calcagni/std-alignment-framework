"""Checks of P21 (the expected evidence per decision is the KL divergence, so misalignment is the slowest rate of
evidence against the specification), P22 (detection: the Chernoff information is at most either KL), P23 (the
estimated misalignment of an actor that does pursue F is asymptotically χ² with |X| − 2 degrees of freedom; a light
simulation), P24 (the evaluation gap), P37 (a strong incentive masks the actor, and can fake alignment), P54
(dependence and drift only add evidence) and P55 (what a record of counts certifies, at every size)."""
from itertools import product
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gammaln
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt
from .test_misalignment import misalignment, isotonic, best_outcomes_limit
import stdalign


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


def _counts_rows(C, q, F):
    """P52(i) by the library, for each row of counts in C: the estimated misalignment and revealed intensity."""
    est = [stdalign.from_counts(c, q, F) for c in C]
    return np.array([e.value for e in est]), np.array([e.revealed_intensity for e in est])


def _draws(row):
    """The draws counted in a row, as outcome indices."""
    return np.repeat(np.arange(row.size), row.astype(int))


def by_log_ratios(C, l, F):
    """P52(ii) by the library, for each row of counts in C, with log-ratios l and objective F per outcome."""
    return np.array([stdalign.from_log_ratios(l[x], F[x]).value for x in map(_draws, C)])


def by_two_samples(C, Cq, l, F):
    """P52(iii) by the library, for each row of C and the matching row of the default's counts Cq."""
    return np.array([stdalign.from_two_samples(l[x], F[x], F[y]).value for x, y in zip(map(_draws, C), map(_draws, Cq))])


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
        MA, tA = _counts_rows(C, q, F)
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


def marginals(P, n, K):
    """The marginals of a joint behaviour P on sequences of n outcomes from K, as an n × K array."""
    J = P.reshape((K,) * n)
    return np.array([J.sum(axis=tuple(j for j in range(n) if j != i)) for i in range(n)])


def product_of(rows):
    """The joint behaviour of independent decisions with the given marginals, flattened."""
    out = np.ones(1)
    for row in rows:
        out = np.outer(out, row).ravel()
    return out


def test_dependence_and_drift_only_add():
    """P54: (1/n) KL(P || p^n) = KL(p̄ || p) + δ + κ for every p; against the ray of F the least of it is M(p̄) + δ + κ,
    at p̄'s nearest intended behaviour; δ = 0 for identically distributed decisions and κ = 0 for independent ones, and
    each is positive otherwise; the expected empirical behaviour is p̄."""
    r = rng(5401); seen = {"iid": 0, "exchangeable": 0, "independent": 0, "generic": 0}
    for trial in range(400):
        n = int(r.integers(2, 4)); K = int(r.integers(2, 5 if n == 2 else 4)); kind = list(seen)[trial % 4]
        if kind == "iid":
            P = product_of([simplex_interior(r, K)] * n)
        elif kind == "exchangeable":                                            # a mixture of i.i.d. behaviours
            rows = [simplex_interior(r, K) for _ in range(3)]; w = r.dirichlet(np.ones(3))
            P = sum(wi * product_of([ri] * n) for wi, ri in zip(w, rows))
        elif kind == "independent":
            P = product_of([simplex_interior(r, K) for _ in range(n)])
        else:
            P = simplex_interior(r, K ** n)
        seen[kind] += 1
        m = marginals(P, n, K); pbar = m.mean(axis=0)
        delta = np.mean([kl(mi, pbar) for mi in m]); kappa = kl(P, product_of(m)) / n
        for _ in range(5):
            pp = simplex_interior(r, K)
            lhs = kl(P, product_of([pp] * n)) / n
            assert abs(lhs - (kl(pbar, pp) + delta + kappa)) <= EXACT * (1 + lhs)
        q = simplex_interior(r, K); F = r.normal(0, 1, K)
        M, ts = misalignment(pbar, q, F)
        if np.isfinite(ts):                                                       # (ii) against the ray
            po = tilt(q, ts * F)
            assert abs(kl(P, product_of([po] * n)) / n - (M + delta + kappa)) <= 1e-9 * (1 + M)
            for t in r.uniform(0, 4, 4):
                assert kl(P, product_of([tilt(q, t * F)] * n)) / n >= M + delta + kappa - 1e-9 * (1 + M)
        if kind in ("iid", "exchangeable"):
            assert delta <= EXACT
        else:
            assert delta > 1e-6
        if kind in ("iid", "independent"):
            assert kappa <= EXACT
        else:
            assert kappa > 1e-6
        seqs = np.array(list(product(range(K), repeat=n)))                       # (iii) the expected shares
        shares = np.array([np.bincount(x, minlength=K) / n for x in seqs])
        assert np.abs(P @ shares - pbar).max() <= EXACT
    assert min(seen.values()) >= 100


def compositions(n, K):
    """Every vector of K non-negative counts that add up to n."""
    if K == 1:
        return [(n,)]
    return [(a,) + rest for a in range(n + 1) for rest in compositions(n - a, K - 1)]


def type_log_probs(C, p):
    """log P(counts = c) for a sample of size n from p, for every row c of C."""
    n = C[0].sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(C > 0, C * np.log(p), 0.0)
    return gammaln(n + 1) - gammaln(C + 1).sum(axis=1) + terms.sum(axis=1)


def ordinal_misalignment_of(s, q, F):
    """M_ord of [P36](ii) for s ∈ Δ, from the q-weighted isotonic regression of the level ratios."""
    levels = np.unique(F); at = np.searchsorted(levels, F)
    qL = np.array([q[F == v].sum() for v in levels]); sL = np.array([s[F == v].sum() for v in levels])
    return kl(s, q * isotonic(sL / qL, qL)[at])


def test_what_a_record_certifies():
    """P55: a sample from p shows the empirical behaviour s with probability between e^(−n KL(s||p))/k_n and
    e^(−n KL(s||p)); for intended behaviours on the ray and at its limit, and for the ordinal specification,
    P(n M(p̂_n) ≥ λ) ≤ k_n e^(−λ), computed exactly over every empirical behaviour; the same for n KL(p̂_n || r); the
    bound needs its factor k_n; and the test catches a misaligned actor (seeded simulation)."""
    r = rng(5501); seen = {"beyond one type": 0, "ray": 0, "ordinal": 0}
    lams = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0])
    for _ in range(40):
        K = int(r.integers(2, 6)); n = int(r.integers(3, 13 if K <= 4 else 10))
        C = np.array(compositions(n, K)); S = C / n; k = len(C)
        assert k == round(np.exp(gammaln(n + K) - gammaln(n + 1) - gammaln(K)))
        for _ in range(3):                                                         # (i) and (iv)
            p = simplex_interior(r, K) if r.random() < 0.7 else with_zeros(r, K)
            lp = type_log_probs(C, p); d = np.array([kl(s, p) for s in S]); ok = np.isfinite(d)
            assert np.all(lp[ok] <= -n * d[ok] + 1e-9) and np.all(np.exp(lp[~ok]) == 0)
            assert np.all(lp[ok] >= -n * d[ok] - np.log(k) - 1e-9)
            for lam in lams:
                assert np.exp(lp[n * d >= lam]).sum() <= k * np.exp(-lam) + 1e-12
        q = simplex_interior(r, K); F = r.normal(0, 1, K)
        Mray = np.array([misalignment(s, q, F)[0] for s in S])
        Mord = np.array([ordinal_misalignment_of(s, q, F) for s in S])
        for pp in [tilt(q, t * F) for t in (0.0, 0.3, 1.5, 6.0)] + [best_outcomes_limit(q, F)]:
            lp = type_log_probs(C, pp)                                              # (ii): the ray, and its limit
            assert np.all(np.array([kl(s, pp) for s in S]) >= Mray - 1e-10 * (1 + Mray))   # the step of the proof
            for lam in lams:
                prob = np.exp(lp[n * Mray >= lam - 1e-12]).sum()
                assert prob <= k * np.exp(-lam) + 1e-12
                seen["beyond one type"] += prob > np.exp(-lam)
            seen["ray"] += 1
        for _ in range(3):                                                          # (ii): the ordinal specification
            levels = np.unique(F); ratios = np.sort(np.exp(r.normal(0, 1, len(levels))))
            pp = q * ratios[np.searchsorted(levels, F)]; pp /= pp.sum()
            lp = type_log_probs(C, pp)
            assert np.all(np.array([kl(s, pp) for s in S]) >= Mord - 1e-10 * (1 + Mord))   # the step of the proof
            for lam in lams:
                assert np.exp(lp[n * Mord >= lam - 1e-12]).sum() <= k * np.exp(-lam) + 1e-12
            seen["ordinal"] += 1
    assert seen["beyond one type"] >= 5 and seen["ray"] >= 100 and seen["ordinal"] >= 100
    alpha = 0.05; caught = 0                                                        # (iii), seeded
    q = np.array([0.4, 0.3, 0.2, 0.1]); F = np.array([0.0, 1.0, 2.0, 3.0]); ph = np.array([0.1, 0.5, 0.1, 0.3])
    M, _ = misalignment(ph, q, F); n = 3000; k = np.exp(gammaln(n + 4) - gammaln(n + 1) - gammaln(4))
    assert M > 0.05 and n * M > 4 * np.log(k / alpha)
    for _ in range(100):
        caught += n * misalignment(r.multinomial(n, ph) / n, q, F)[0] >= np.log(k / alpha)
    assert caught >= 99
