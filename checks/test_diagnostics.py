"""Checks of P43 (misalignment at any intensity), P44 (named objectives), P45 (drift across runs), P46 (runs in two
conditions), P47 (the cost of reweighting), P48 (an uncertain target), P49 (outer and inner misalignment), P50
(tampering) and P51 (what signals, audits and re-measurements reveal of it). Each claim is computed by the library's
functions (stdalign/diagnostics.py), so that breaking one on purpose makes its checks fail (tools/mutants/)."""
import itertools
import numpy as np
from scipy.optimize import minimize, minimize_scalar, brentq
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt, kl_tilts
from .test_misalignment import misalignment, nearest, ray_minimizer
from .test_feasibility import project_linear
from .test_identifiability import actor, extreme, var, cov
from stdalign.diagnostics import (intensity_terms, min_over_intensity as shared_intensity,         # noqa: F401
                                  named_pursuit, drift, condition_split, reweighting_moments, most_charitable,
                                  outer_misalignment as outer, inner_split, pairs, tampering, grounded_pursuit,
                                  least_tampering, most_tampering, remeasured)
import stdalign


def intensity_split(terms, q, F, t):
    """P43(i): the three terms of KL(p || p_{F,t}) at t, from the library's IntensityTerms (q and F are in them)."""
    return terms.at(t)


def with_intensity(r, q, F, tau, n):
    """A full-support behaviour whose revealed intensity is tau, with a random misaligned part: tilt(q, aF + G), with
    a chosen so that its average of F is that of the pursuit at tau."""
    G = r.normal(0, 1.5, n); target = tilt(q, tau * F) @ F
    a = brentq(lambda a: tilt(q, a * F + G) @ F - target, -200, 200, xtol=1e-14)
    return tilt(q, a * F + G)


def test_misalignment_at_any_intensity():
    """P43(i): KL(p || p_{F,t}) = M + KL(p° || p_{F,t}) + t·[E_q F − E_p F]⁺ at every t, in all three cases of P5(iv);
    the mismatch is 0 at t = t* and positive elsewhere; at the matched intensity it is P9(ii)."""
    r = rng(4301); seen = set()
    for _ in range(600):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = np.round(r.normal(0, 1, n), 1)
        if F.max() == F.min():
            continue
        u = r.random()
        if u < 0.15:                                                               # all mass on A, split its own way
            A = F == F.max(); p = np.zeros(n); p[A] = r.dirichlet(np.ones(A.sum()))
        elif u < 0.35:
            p = with_zeros(r, n)
        else:
            p = simplex_interior(r, n)
        ts = ray_minimizer(p, q, F); terms = intensity_terms(p, q, F)
        seen.add("inf" if np.isinf(ts) else ("zero" if ts == 0 else "interior"))
        for t in (0.0, 0.4, 1.3, 5.0, float(r.uniform(0, 8))):
            lhs = kl(p, tilt(q, t * F)); M, mismatch, anti = intensity_split(terms, q, F, t)
            assert abs(lhs - (M + mismatch + anti)) <= EXACT * (1 + lhs)
            if np.isfinite(ts) and abs(t - ts) > 0.05:
                assert mismatch > 1e-6                                             # zero only at t*
        if np.isfinite(ts):
            assert intensity_split(terms, q, F, ts)[1] <= EXACT
    assert seen == {"inf", "zero", "interior"}


def test_one_intensity_for_several_conditions():
    """P43(ii): at every t, Σρ KL(p_c || p_{c,t}) = ΣρM_c + Σρ[mismatch_c(t) + t·a_c], so the minima agree; the excess
    is unchanged when a condition's misaligned part changes but its t* and a_c do not; and it is 0 exactly when all the
    t*_c are equal."""
    r = rng(4302); positive = 0
    for _ in range(80):
        C = int(r.integers(2, 5)); rho = r.dirichlet(np.ones(C)); n = int(r.integers(4, 8))
        qs = [simplex_interior(r, n) for _ in range(C)]; F = r.normal(0, 1, n)
        ps = [simplex_interior(r, n) for _ in range(C)]
        direct = lambda t, ps=ps: sum(rc * kl(pc, tilt(qc, t * F)) for rc, pc, qc in zip(rho, ps, qs))
        own = sum(rc * misalignment(pc, qc, F)[0] for rc, pc, qc in zip(rho, ps, qs))

        def excess_of(ps):
            terms = [intensity_terms(pc, qc, F) for pc, qc in zip(ps, qs)]
            return lambda t: sum(rc * sum(intensity_split(tc, qc, F, t)[1:]) for rc, tc, qc in zip(rho, terms, qs))
        excess = excess_of(ps)
        for t in (0.0, 0.3, 1.1, 4.0):
            assert abs(direct(t) - (own + excess(t))) <= EXACT * (1 + direct(t))
        assert abs(shared_intensity(direct) - (own + shared_intensity(excess))) <= 1e-9
        si = stdalign.shared_intensity(ps, qs, [F] * C, rho)                        # the library's whole quantity
        assert abs(si.misalignment - shared_intensity(direct)) <= 1e-12 and abs(si.own - own) <= 1e-9
        assert abs(si.excess - shared_intensity(excess)) <= 1e-9
        # another behaviour in condition 0 with the same t* (hence the same average of F) and the same a_0
        ts0 = ray_minimizer(ps[0], qs[0], F)
        if 0 < ts0 < np.inf:
            alt = [with_intensity(r, qs[0], F, ts0, n)] + ps[1:]
            assert abs(misalignment(alt[0], qs[0], F)[0] - misalignment(ps[0], qs[0], F)[0]) > 1e-4   # it differs
            ex_alt = excess_of(alt)
            for t in (0.0, 0.7, 2.5):
                assert abs(ex_alt(t) - excess(t)) <= 1e-9
        # all conditions at one revealed intensity: no excess; at different ones: some
        tau = float(r.uniform(0.2, 2.0))
        ex_same = excess_of([with_intensity(r, qc, F, tau, n) for qc in qs])
        assert ex_same(tau) <= 1e-9 and shared_intensity(ex_same) <= 1e-9
        e = shared_intensity(excess_of([with_intensity(r, qc, F, tau * (1 + c), n) for c, qc in enumerate(qs)]))
        assert e > 1e-6; positive += e > 1e-3
    assert positive >= 40


def member(r, q, F, Gs, p):
    """A random full-support behaviour with p's averages of F and Gs (the projection of a random behaviour)."""
    A = np.vstack([F, *Gs])
    return project_linear(simplex_interior(r, q.size), A, A @ p)


def test_named_objectives_split_misalignment():
    """P44(i)-(iii): the named pursuit is a tilt of q by a combination of F and the Gs (its log-ratio to q lies in their
    span), lies in the linear set, is nearer to p° than any other member, and has p's t* and p°; misalignment splits
    into unexplained plus named; the unexplained part is 0 exactly for a tilt of q by such a combination; naming more
    objectives moves misalignment from one part to the other."""
    r = rng(4401); visible = 0
    for _ in range(150):
        n = int(r.integers(6, 12)); k = int(r.integers(1, 3))
        q = simplex_interior(r, n); F = r.normal(0, 1, n); Gs = list(r.normal(0, 1, (k + 1, n)))
        p = simplex_interior(r, n)
        M, ts = misalignment(p, q, F); pt = named_pursuit(p, q, F, Gs[:k])
        B = np.column_stack([np.ones(n), F, *Gs[:k]])
        lr = np.log(pt / q); assert np.linalg.norm(lr - B @ np.linalg.lstsq(B, lr, rcond=None)[0]) <= 1e-8
        A = np.vstack([F, *Gs[:k]]); assert np.abs(A @ pt - A @ p).max() <= 1e-10
        pn = nearest(p, q, F)
        for _ in range(3):
            other = member(r, q, F, Gs[:k], p)
            assert abs(kl(other, pn) - kl(other, pt) - kl(pt, pn)) <= 1e-9 and kl(other, pn) >= kl(pt, pn) - 1e-12
        Mt, tt = misalignment(pt, q, F)
        assert abs(tt - ts) <= 1e-9 * (1 + ts) and np.abs(nearest(pt, q, F) - pn).max() <= 1e-10
        assert abs(M - (kl(p, pt) + Mt)) <= 1e-9
        visible += kl(p, pt) > 1e-3
        exact = tilt(q, r.normal(0, 1) * F + sum(r.normal(0, 1) * G for G in Gs[:k]))   # a tilt of q in the span
        assert kl(exact, named_pursuit(exact, q, F, Gs[:k])) <= 1e-10
        pt2 = named_pursuit(p, q, F, Gs)                                               # one more objective named
        assert abs(kl(p, pt) - (kl(p, pt2) + kl(pt2, pt))) <= 1e-9
        assert abs(misalignment(pt2, q, F)[0] - (Mt + kl(pt2, pt))) <= 1e-9
    assert visible >= 100


def regression_r2(H, q, *X):
    """The squared multiple correlation of H with the columns X under q (least squares with an intercept)."""
    B = np.column_stack([np.ones_like(H), *X]); w = np.sqrt(q)
    beta = np.linalg.lstsq(B * w[:, None], H * w, rcond=None)[0]
    return 1 - q @ (H - B @ beta) ** 2 / var(q, H)


def test_named_shares_at_the_start():
    """P44(iv): along p_s = tilt(q, sH + s²K) with Cov_q(H, F) > 0, the unexplained share tends to 1 − R²_{F,G} and
    the named share to R²_{F,G} − R²_F, at first order in s."""
    r = rng(4402); used = 0
    for _ in range(80):
        n = int(r.integers(6, 11)); q = simplex_interior(r, n)
        F, H, K = r.normal(0, 1, n), r.normal(0, 1, n), r.normal(0, 1, n); Gs = list(r.normal(0, 1, (2, n)))
        if cov(q, H, F) / np.sqrt(var(q, H) * var(q, F)) < 0.1:
            continue
        RF, RFG = regression_r2(H, q, F), regression_r2(H, q, F, *Gs)
        if RFG - RF < 0.02:
            continue                                                                   # the named share is visible
        errs = []
        for s in (1e-2, 1e-3):
            a = s * H + s * s * K; ps = tilt(q, a); pt = named_pursuit(ps, q, F, Gs)
            dep = kl_tilts(q, a, np.zeros(n))
            errs.append((abs(kl(ps, pt) / dep - (1 - RFG)), abs(misalignment(pt, q, F)[0] / dep - (RFG - RF))))
        for j in range(2):
            assert errs[1][j] <= 5e-3 and errs[1][j] <= 0.2 * errs[0][j] + 1e-6
        used += 1
    assert used >= 30


def test_drift_splits_shared_misalignment():
    """P45(i), (ii): Σ w_i KL(p_i || r) = KL(p̄ || r) + D for every r; the shared misalignment under the standard
    specification, found by minimizing over the ray, is M(p̄) + D and at least the average own misalignment;
    0 <= D <= H(w), with D = 0 for equal runs and D = H(w) for runs with disjoint supports."""
    r = rng(4501); visible = 0
    for _ in range(200):
        n = int(r.integers(3, 10)); m = int(r.integers(2, 5)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ps = [simplex_interior(r, n) if r.random() < 0.8 else with_zeros(r, n) for _ in range(m)]
        w = r.dirichlet(np.ones(m)); D, pbar = drift(ps, w); H = -w @ np.log(w)
        for _ in range(3):
            rr = simplex_interior(r, n); lhs = sum(wi * kl(pi, rr) for wi, pi in zip(w, ps))
            assert abs(lhs - (kl(pbar, rr) + D)) <= EXACT * (1 + lhs)
        shared = shared_intensity(lambda t: sum(wi * kl(pi, tilt(q, t * F)) for wi, pi in zip(w, ps)))
        assert abs(shared - (misalignment(pbar, q, F)[0] + D)) <= 1e-8
        assert sum(wi * misalignment(pi, q, F)[0] for wi, pi in zip(w, ps)) <= shared + 1e-12
        assert -EXACT <= D <= H + EXACT; visible += D > 1e-3
        assert drift([ps[0]] * m, w)[0] <= EXACT                                      # equal runs: no drift
        cut = np.array_split(r.permutation(n + m)[: n + m], m)                         # disjoint supports
        disjoint = [np.where(np.isin(np.arange(n + m), c), r.random(n + m), 0.0) for c in cut]
        disjoint = [d / d.sum() for d in disjoint]
        assert abs(drift(disjoint, w)[0] - H) <= EXACT
    assert visible >= 150


def expected_over_draws(values, probs, m, f):
    """E[f(draws)] over m independent draws from a random behaviour with finitely many values."""
    return sum(np.prod([probs[i] for i in tup]) * f([values[i] for i in tup])
               for tup in itertools.product(range(len(values)), repeat=m))


def test_drift_from_few_runs():
    """P45(iii), (iv): E[D] = D_∞ − E[KL(p̄ || p̄_∞)] exactly, with 0 <= E[KL(p̄ || p̄_∞)] <= E[χ²(P || p̄_∞)]/m; and for
    small drift E[D]/D_∞ → 1 − 1/m, at first order."""
    r = rng(4502)
    for _ in range(40):
        n = int(r.integers(3, 7)); K = int(r.integers(2, 4)); m = int(r.integers(2, 4))
        values = [simplex_interior(r, n) for _ in range(K)]; probs = r.dirichlet(np.ones(K))
        mean = sum(a * v for a, v in zip(probs, values))
        D_inf = sum(a * kl(v, mean) for a, v in zip(probs, values))
        chi = sum(a * np.sum((v - mean) ** 2 / mean) for a, v in zip(probs, values))
        ED = expected_over_draws(values, probs, m, lambda ps: drift(ps, np.full(m, 1 / m))[0])
        EK = expected_over_draws(values, probs, m, lambda ps: kl(sum(ps) / m, mean))
        assert abs(ED - (D_inf - EK)) <= EXACT and -EXACT <= EK <= chi / m + EXACT
        assert ED <= D_inf + EXACT
    for _ in range(20):                                                                # small drift
        n = int(r.integers(4, 8)); K = 4; base = simplex_interior(r, n)
        V = r.normal(0, 1, (K, n)); V -= V.mean(1, keepdims=True); V -= V.mean(0, keepdims=True)
        probs = np.full(K, 1 / K); m = int(r.integers(2, 4)); errs = []
        for eps in (1e-2, 1e-3):                                                       # inside the first-order regime
            values = [base + eps * base.min() * v for v in V]
            D_inf = sum(a * kl(v, base) for a, v in zip(probs, values))
            ED = expected_over_draws(values, probs, m, lambda ps: drift(ps, np.full(m, 1 / m))[0])
            errs.append(abs(ED / D_inf - (1 - 1 / m)))
        assert errs[1] <= 2e-4 and errs[1] <= 0.2 * errs[0] + 1e-7


def test_runs_split_differences_between_conditions():
    """P46(i), (iii), (iv): the average divergence between conditions is the reproducible plus the run-specific
    difference; the gap in shared misalignment is the gap of the averages plus the gap of the drifts; and from few runs
    the reproducible difference is, on average, at least that of the means."""
    r = rng(4601); both = 0
    for _ in range(200):
        n = int(r.integers(3, 9)); m = int(r.integers(2, 5)); w = r.dirichlet(np.ones(m))
        pe = [simplex_interior(r, n) for _ in range(m)]
        pu = [simplex_interior(r, n) if r.random() < 0.8 else with_zeros(r, n) for _ in range(m)]
        lhs = sum(a * kl(x, y) for a, x, y in zip(w, pu, pe)); rep, spec = condition_split(pe, pu, w)
        assert abs(lhs - (rep + spec)) <= EXACT * (1 + lhs) and rep >= -EXACT and spec >= -EXACT
        both += rep > 1e-3 and spec > 1e-3
        q = simplex_interior(r, n); F = r.normal(0, 1, n)
        shared = lambda ps: shared_intensity(lambda t: sum(a * kl(x, tilt(q, t * F)) for a, x in zip(w, ps)))
        (De, be), (Du, bu) = drift(pe, w), drift(pu, w)
        gap = shared(pu) - shared(pe)
        assert abs(gap - ((misalignment(bu, q, F)[0] - misalignment(be, q, F)[0]) + (Du - De))) <= 2e-8
    assert both >= 100
    for _ in range(40):                                                                # (iv), exactly over the draws
        n = int(r.integers(3, 6)); K = int(r.integers(2, 4)); m = int(r.integers(2, 4))
        pairs = [(simplex_interior(r, n), simplex_interior(r, n)) for _ in range(K)]; probs = r.dirichlet(np.ones(K))
        me = sum(a * e for a, (e, _) in zip(probs, pairs)); mu = sum(a * u for a, (_, u) in zip(probs, pairs))
        E = expected_over_draws(pairs, probs, m, lambda d: kl(sum(u for _, u in d) / m, sum(e for e, _ in d) / m))
        assert E >= kl(mu, me) - EXACT


def test_average_of_runs_stays_within_the_leak():
    """P46(ii): runs that respond through views with leaks ε_i give an average whose combined view has KL ε̄ = Σ w_i ε_i;
    so KL(p̄_u || p̄_e) <= ε̄, and the average of F in use lies within P17's bounds from p̄_e at ε̄."""
    r = rng(4602); used = []
    for _ in range(500):
        m = int(r.integers(2, 4)); w = r.dirichlet(np.ones(m)); nx = int(r.integers(2, 7))
        runs = []
        for _ in range(m):
            W_a, W_d, K, pi = actor(r, int(r.integers(2, 6)), int(r.integers(2, 6)), nx)
            runs.append((W_a @ K, W_d @ K, pi))                                        # views in e and u, behaviours π_z
        pe = [V_e @ pi for V_e, _, pi in runs]; pu = [V_u @ pi for _, V_u, pi in runs]
        eps = [kl(V_u, V_e) for V_e, V_u, _ in runs]; eps_bar = float(w @ eps)
        Ve = np.concatenate([a * V_e for a, (V_e, _, _) in zip(w, runs)])             # the combined view: signals (i, z)
        Vu = np.concatenate([a * V_u for a, (_, V_u, _) in zip(w, runs)])
        assert abs(kl(Vu, Ve) - eps_bar) <= EXACT * (1 + eps_bar)
        be, bu = sum(a * x for a, x in zip(w, pe)), sum(a * x for a, x in zip(w, pu))
        assert kl(bu, be) <= eps_bar * (1 + EXACT) + EXACT
        F = r.normal(0, 1, nx); hi, lo = extreme(be, F, eps_bar), -extreme(be, -F, eps_bar)
        assert lo - 1e-9 <= bu @ F <= hi + 1e-9
        used.append(kl(bu, be) / eps_bar if eps_bar > 0 else 0.0)
    assert max(used) > 0.2                                                             # the bound is not vacuous


def test_reweighting_costs_exponentially():
    """P47(i), (ii): E_p[w] = 1, E_p[w²] = 1 + χ²(r || p) >= e^{KL(r || p)}, with equality when r is p restricted to
    a set; and the relative variance of the average of e^{tF} under q is χ²(p_{F,t} || q) per draw."""
    r = rng(4701)
    for _ in range(1000):
        n = int(r.integers(2, 12)); p = simplex_interior(r, n) if r.random() < 0.8 else with_zeros(r, n)
        rr = np.where(p > 0, simplex_interior(r, n), 0.0); rr /= rr.sum()
        m1, m2 = reweighting_moments(p, rr); s = p > 0
        assert abs(m1 - 1) <= EXACT and abs(m2 - (1 + np.sum((rr[s] - p[s]) ** 2 / p[s]))) <= EXACT * m2
        assert m2 >= np.exp(kl(rr, p)) * (1 - EXACT)
        S = s & (r.random(n) < 0.6)
        if S.any():
            cond = np.where(S, p, 0.0) / p[S].sum()
            assert abs(reweighting_moments(p, cond)[1] - np.exp(kl(cond, p))) <= EXACT * reweighting_moments(p, cond)[1]
        q = simplex_interior(r, n); F = r.normal(0, 1, n); t = float(r.uniform(0, 3)); pt = tilt(q, t * F)
        ex = np.exp(t * F); rel_var = (q @ ex ** 2 - (q @ ex) ** 2) / (q @ ex) ** 2
        assert abs(rel_var - (reweighting_moments(q, pt)[1] - 1)) <= 1e-9 * (1 + rel_var)


def test_an_uncertain_target_gives_an_interval():
    """P48: no principal whose objective lies in the span of Phi finds less misalignment than KL(p || p̃), the
    principal at p̃'s combination finds exactly that, and the Pythagorean identity behind it holds for every
    combination; the largest misalignment over the span is the departure, reached by F' or by −F'; when p has q's
    averages of Phi every principal finds the departure; and with Phi = (F, G...) the lower end is P44's unexplained
    misalignment."""
    r = rng(4801); positive = 0
    for _ in range(100):
        n = int(r.integers(6, 11)); k = int(r.integers(2, 4)); q = simplex_interior(r, n); p = simplex_interior(r, n)
        Phi = r.normal(0, 1, (k, n)); pt, c = most_charitable(p, q, Phi); low, dep = kl(p, pt), kl(p, q)
        assert np.abs(Phi @ pt - Phi @ p).max() <= 1e-10
        assert abs(misalignment(p, q, c @ Phi)[0] - low) <= 1e-9 * (1 + low)          # attained
        for d in r.normal(0, 1, (40, k)):
            M = misalignment(p, q, d @ Phi)[0]
            assert low - 1e-9 <= M <= dep + 1e-9                                       # inside the interval
            assert abs(max(M, misalignment(p, q, -d @ Phi)[0]) - dep) <= 1e-9 * (1 + dep)   # F' or −F'
            tl = tilt(q, d @ Phi)
            assert abs(kl(p, tl) - low - kl(pt, tl)) <= 1e-9 * (1 + kl(p, tl))       # the identity behind (i)
        positive += low > 1e-3
        assert abs(low - kl(p, named_pursuit(p, q, Phi[0], list(Phi[1:])))) <= 1e-9    # (iii): P44's named pursuit
        pq = project_linear(p, Phi, Phi @ q)                                           # p with q's averages of Phi
        assert kl(pq, most_charitable(pq, q, Phi)[0]) - kl(pq, q) <= 1e-9
        for d in r.normal(0, 1, (10, k)):
            assert abs(misalignment(pq, q, d @ Phi)[0] - kl(pq, q)) <= 1e-9 * (1 + kl(pq, q))
    assert positive >= 80


def test_outer_and_inner_misalignment():
    """P49: outer misalignment is 0 at every intensity for a positively rescaled target and positive otherwise, with
    the small-intensity limit of P11; the principal's and the trainer's misalignments share the strict inner part U
    exactly, which no principal in the span undercuts; a perfect optimizer of the training objective is all outer, and
    a rescaled target makes all misalignment inner."""
    r = rng(4901); positive = 0
    for _ in range(120):
        n = int(r.integers(5, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        Fh = 0.6 * F + 0.8 * r.normal(0, 1, n); a, c = float(r.uniform(0.2, 3)), float(r.normal())
        for t in (0.3, 1.0, 4.0):
            assert outer(q, F, a * F + c, t) <= EXACT                                  # a rescaled target
            assert outer(q, F, Fh, t) > 1e-8                                           # any other evaluator
        cos = cov(q, Fh, F) / np.sqrt(var(q, Fh) * var(q, F))
        target = 1 - cos ** 2 if cos >= 0 else 1.0
        e3, e4 = (abs(outer(q, F, Fh, t) / kl(tilt(q, t * Fh), q) - target) for t in (1e-3, 1e-4))
        assert e4 <= 2e-3 and (e4 <= 0.5 * e3 + 1e-6 or cos < 0)                    # converging as t shrinks
        p = simplex_interior(r, n)
        U, in_P, in_T = inner_split(p, q, F, Fh); MP, MT = misalignment(p, q, F)[0], misalignment(p, q, Fh)[0]
        assert abs(MP - (U + in_P)) <= 1e-9 * (1 + MP) and abs(MT - (U + in_T)) <= 1e-9 * (1 + MT)
        positive += U > 1e-3
        for d in r.normal(0, 1, (20, 2)):                                              # no principal in the span below U
            assert misalignment(p, q, d[0] * F + d[1] * Fh)[0] >= U - 1e-9
        t = float(r.uniform(0.2, 3)); pe = tilt(q, t * Fh)                             # a perfect optimizer
        U_e, _, _ = inner_split(pe, q, F, Fh)
        assert U_e <= 1e-10 and misalignment(pe, q, Fh)[0] <= EXACT
        assert abs(misalignment(pe, q, F)[0] - outer(q, F, Fh, t)) <= EXACT
        assert abs(misalignment(p, q, a * F + c)[0] - MP) <= 1e-9 * (1 + MP)          # all inner when Fh rescales F
    assert positive >= 100


def random_channel(r, W, S, zeros=False):
    """A channel from W worlds to S signals: each row a distribution on the signals, with full support unless zeros."""
    return np.array([with_zeros(r, S) if zeros else simplex_interior(r, S) for _ in range(W)])


def test_tampering_splits_the_departure():
    """P50: the departure from any grounded behaviour splits into the world's departure and the tampering; a target on
    the world is misaligned by exactly its misalignment in the world plus the tampering; the trainer's optimum on a
    signal evaluator tampers at every positive intensity, with share 1 − R² at the start, and the small-intensity limit
    of P49 splits accordingly; the best grounded behaviour pursues the expected signal score, is the I-projection of the
    trainer's optimum, and gives up exactly the difference of log-normalizers."""
    r = rng(5001); world_share_seen = {True: 0, False: 0}
    for _ in range(100):
        W, S = int(r.integers(2, 6)), int(r.integers(2, 6))
        qW = simplex_interior(r, W); K = random_channel(r, W, S); q = pairs(qW, K)
        p = (with_zeros(r, W * S) if r.random() < 0.3 else simplex_interior(r, W * S)).reshape(W, S); pW = p.sum(1)
        T = tampering(p, K); p2 = simplex_interior(r, W)
        assert abs(kl(p.ravel(), pairs(p2, K).ravel()) - (kl(pW, p2) + T)) <= EXACT * (1 + T)       # (i)
        assert abs(kl(p.ravel(), q.ravel()) - (kl(pW, qW) + T)) <= EXACT * (1 + T)
        F = r.normal(0, 1, W); FX = np.repeat(F, S)                                             # (ii)
        for t in (0.0, 0.7, 3.0):
            assert np.abs(tilt(q.ravel(), t * FX) - pairs(tilt(qW, t * F), K).ravel()).max() <= EXACT
        MX = misalignment(p.ravel(), q.ravel(), FX)[0]
        assert abs(MX - (misalignment(pW, qW, F)[0] + T)) <= 1e-9 * (1 + MX)
        Fh = r.normal(0, 1, S); FhX = np.tile(Fh, W); m = K @ Fh                                 # (iii)
        for t in (0.5, 2.0):
            assert tampering(tilt(q.ravel(), t * FhX).reshape(W, S), K) > 1e-10
        R2 = var(qW, m) / var(q.ravel(), FhX)
        share = lambda t: (lambda pt: tampering(pt.reshape(W, S), K) / kl(pt, q.ravel()))(tilt(q.ravel(), t * FhX))
        e2, e3 = abs(share(1e-2) - (1 - R2)), abs(share(1e-3) - (1 - R2))                       # float64 below
        assert e3 <= 1e-3 and e3 <= 0.5 * e2 + 1e-7                                              # converging
        cos = cov(q.ravel(), FX, FhX) / np.sqrt(var(q.ravel(), FX) * var(q.ravel(), FhX))
        cos_W = cov(qW, F, m) / np.sqrt(var(qW, F) * var(qW, m))
        assert abs((1 - cos ** 2) - ((1 - R2) + R2 * (1 - cos_W ** 2))) <= 1e-12                # sin²θ splits
        target = R2 * (1 - cos_W ** 2) if cos >= 0 else R2
        world = lambda t: (lambda pt: misalignment(pt.reshape(W, S).sum(1), qW, F)[0] / kl(pt, q.ravel()))(
            tilt(q.ravel(), t * FhX))
        w2, w3 = abs(world(1e-2) - target), abs(world(1e-3) - target)
        assert w3 <= 2e-3 and (w3 <= 0.5 * w2 + 1e-6 or cos < 0)
        world_share_seen[bool(cos >= 0)] += 1
        t = float(r.uniform(0.3, 3)); pt = tilt(q.ravel(), t * FhX); O = misalignment(pt, q.ravel(), FX)[0]
        assert abs(O - (misalignment(pt.reshape(W, S).sum(1), qW, F)[0] + tampering(pt.reshape(W, S), K))) \
            <= 1e-9 * (1 + O)                                                                    # outer splits too
        pg = grounded_pursuit(qW, K, Fh, t).ravel()                                              # (iv)
        J = lambda x: x @ FhX - kl(x, q.ravel()) / t
        for pw in (simplex_interior(r, W) for _ in range(10)):
            x = pairs(pw, K).ravel()
            assert abs(t * (J(pg) - J(x)) - kl(x, pg)) <= 1e-9 * (1 + kl(x, pg))
            assert abs(kl(x, pt) - (kl(x, pg) + kl(pg, pt))) <= 1e-9 * (1 + kl(x, pt))
        gain = np.log(q.ravel() @ np.exp(t * FhX)) - np.log(qW @ np.exp(t * m))
        assert abs(t * (J(pt) - J(pg)) - gain) <= 1e-9 * (1 + gain) and abs(kl(pg, pt) - gain) <= 1e-9 * (1 + gain)
    assert min(world_share_seen.values()) >= 10


def test_signals_and_audits_bound_tampering():
    """P51: from signals alone, tampering is at least L(p_S), which the constructed joint attains, with the certificate
    of (i); at most the largest tampering of a joint in which every signal comes from one world, which is positive for
    every p_S; an audit through a channel the actor cannot influence tightens the lower end, up to T itself for an
    exact audit; and a re-measurement splits the evaluator's gain into an honest and a channel part, bounded by T."""
    r = rng(5101); outside, above_constant = 0, 0
    for k in range(120):
        W, S = int(r.integers(2, 5)), int(r.integers(2, 5))
        K = random_channel(r, W, S); p = simplex_interior(r, W * S).reshape(W, S); pS = p.sum(0); T = tampering(p, K)
        L, gap, joint = least_tampering(pS, K)
        assert 0 <= gap <= 1e-8 and L - gap <= T + EXACT                                       # (i) the bound
        assert np.abs(joint.sum(0) - pS).max() <= EXACT
        assert L - gap - EXACT <= tampering(joint, K) <= L + EXACT                               # attained
        for pw in (simplex_interior(r, W) for _ in range(10)):
            assert L - gap <= kl(pS, pw @ K) + EXACT                                             # the minimum
            c = K @ (pS / (pw @ K))
            assert L >= kl(pS, pw @ K) - np.log(c.max()) - EXACT                                 # the certificate
        honest = simplex_interior(r, W) @ K
        assert least_tampering(honest, K)[0] <= 1e-8                                             # in the hull
        outside += L > 1e-3
        U = most_tampering(pS, K)                                                                # (ii)
        assert U >= max(kl(pS, K[w]) for w in range(W)) - EXACT and U > 0
        above_constant += U > max(kl(pS, K[w]) for w in range(W)) + 1e-6
        for _ in range(30):                                                                      # near the vertices
            x = np.array([pS[s] * r.dirichlet(np.full(W, 0.05)) for s in range(S)]).T
            assert tampering(x, K) <= U + 1e-9
        assert most_tampering(honest, K) > 0                                                     # even the default's
        same = np.tile(pS, (W, 1)); assert most_tampering(pS, same) > 0                          # rows all equal p_S
        Ka = random_channel(r, W, int(r.integers(2, 5)), zeros=True)                              # (iii) an audit
        C = np.einsum("ws,wv->wsv", K, Ka).reshape(W, -1); pSA = np.einsum("ws,wv->sv", p, Ka).ravel()
        La, gap_a, _ = least_tampering(pSA, C)
        assert gap_a <= 1e-8 and La - gap_a >= L - 1e-9 and La - gap_a <= T + EXACT              # L <= La <= T
        Ex = np.einsum("ws,wv->wsv", K, np.eye(W)).reshape(W, -1); pSE = np.einsum("ws,wv->sv", p, np.eye(W)).ravel()
        assert abs(least_tampering(pSE, Ex)[0] - T) <= 1e-9                                     # an exact audit
        Fh = r.normal(0, 1, S); qW = simplex_interior(r, W)                                      # (iv)
        honest_gain, channel_gain, again = remeasured(p, K, Fh, qW)
        first, second = again.sum(1) @ Fh, again.sum(0) @ Fh
        assert abs(second - p.sum(1) @ (K @ Fh)) <= EXACT
        assert abs((first - pairs(qW, K).sum(0) @ Fh) - (honest_gain + channel_gain)) <= EXACT
        assert abs(channel_gain) <= (Fh.max() - Fh.min()) * np.sqrt(T / 2) + EXACT
        assert kl(again.sum(1), again.sum(0)) <= T + EXACT
        n = int(r.integers(2, 6)); order = np.argsort(Fh)                                       # re-rolls
        below = np.cumsum(K[:, order], 1); best = np.zeros_like(K)
        best[:, order] = below ** n - np.c_[np.zeros(W), below[:, :-1]] ** n
        reroll = pairs(qW, best / best.sum(1, keepdims=True)); hg, cg, _ = remeasured(reroll, K, Fh, qW)
        assert abs(hg) <= EXACT and cg > 0 and tampering(reroll, K) >= 2 * cg ** 2 / (Fh.max() - Fh.min()) ** 2
    assert outside >= 30 and above_constant >= 10
