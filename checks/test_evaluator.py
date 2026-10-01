"""Checks of P18 (through the evaluator, only the regression counts: the residual averages to zero for every behaviour
that sees outcomes only through the evaluator; the covariance form of the target's gain; invariance under injective
transformations of the evaluator), P19 (a monotone regression rules out overoptimization) and P20 (where
overoptimization starts, and how it ends at high intensity)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt


def evaluator_instance(r, monotone=None):
    """Outcomes grouped into k level sets of an evaluator F̂ with values v₁ < … < v_k; a target F = m + R, where the
    regression m is increasing in F̂ when monotone is True, and R has zero q-average in every level set."""
    k = int(r.integers(3, 7)); n = int(r.integers(k + 1, 13))
    labels = r.permutation(np.concatenate([np.arange(k), r.integers(0, k, n - k)]))
    v = np.sort(r.normal(0, 1, k)); Fh = v[labels]; q = simplex_interior(r, n)
    mv = np.sort(r.normal(0, 1, k)) if monotone else r.normal(0, 1, k)
    R0 = r.normal(0, 1, n)
    cell = lambda f: np.array([q[labels == c] @ f[labels == c] / q[labels == c].sum() for c in range(k)])
    R = R0 - cell(R0)[labels]
    return q, Fh, labels, v, mv[labels] + R, cell


def test_through_the_evaluator_only_the_regression_counts():
    """P18: E_q[R] = 0; for p limited to the level sets of F̂, E_p[R] = 0 and E_p[F] = E_p[m]; for any p,
    E_p[F] − E_q[F] = Cov_q(p/q, m) + Cov_q(p/q, R); m and R are unchanged when F̂ becomes h(F̂), h injective, and change in
    general when h merges level sets; with distinct values on distinct outcomes, m = F (D10, Notes)."""
    r = rng(1801); changed = 0
    for _ in range(300):
        q, Fh, labels, v, F, cell = evaluator_instance(r)
        m = cell(F)[labels]; R = F - m; scale = 1 + np.abs(F).max()
        assert abs(q @ R) <= EXACT * scale
        p = tilt(q, r.normal(0, 2, labels.max() + 1)[labels])                       # limited to the level sets
        assert abs(p @ R) <= EXACT * scale and abs(p @ F - p @ m) <= EXACT * scale
        p = simplex_interior(r, q.size); w = p / q                                   # any behaviour
        cov = lambda a, b: q @ (a * b) - (q @ a) * (q @ b)
        assert abs((p @ F - q @ F) - (cov(w, m) + cov(w, R))) <= 1e-9 * scale
        assert abs(cov(w, R) - p @ R) <= 1e-9 * scale                                # the residual's gain
        for h in (np.exp, lambda x: x ** 3 - 2 * x, lambda x: -x):                   # injective transformations
            G = h(Fh)
            levels = np.unique(G, return_inverse=True)[1]
            m2 = np.array([q[levels == c] @ F[levels == c] / q[levels == c].sum() for c in range(levels.max() + 1)])
            assert np.abs(m2[levels] - m).max() <= EXACT * scale
        merged = np.where(labels == 1, 0, labels)                                    # a map that is not injective
        m3 = np.array([q[merged == c] @ F[merged == c] / q[merged == c].sum() if np.any(merged == c) else 0.0
                       for c in range(labels.max() + 1)])[merged]
        changed += np.abs(m3 - m).max() > 1e-6
        distinct = np.arange(q.size)                                                 # distinct values: m = F, R = 0
        m4 = np.array([q[distinct == c] @ F[distinct == c] / q[distinct == c].sum() for c in range(q.size)])
        assert np.abs(m4 - F).max() <= EXACT * scale
    assert changed >= 250                                                            # merging level sets changes m


def nondecreasing(values, scale):
    return bool(np.all(np.diff(values) >= -1e-12 * scale))


def test_a_monotone_regression_rules_out_overoptimization():
    """P19: with m non-decreasing in F̂, the target's average never decreases along paths from q whose revealed
    objectives are non-decreasing functions of F̂: the pursuit of F̂, of increasing transformations of it, a curved
    path, and best-of-n in a real n ≥ 1, whose revealed objective is checked to be non-decreasing in F̂ (Notes); nor as
    a threshold on F̂ rises (Notes); with a non-monotone regression, some such paths do decrease."""
    r = rng(1802); ts = np.linspace(0, 12, 1201); decreasing_without = 0
    for trial in range(300):
        q, Fh, labels, v, F, cell = evaluator_instance(r, monotone=True)
        scale = 1 + np.abs(F).max()
        assert nondecreasing(cell(F), scale)                                         # the regression is monotone
        ranks = labels.astype(float)
        for g in (Fh, np.exp(Fh), ranks, np.cbrt(Fh)):                              # non-decreasing functions of F̂
            assert nondecreasing(np.array([tilt(q, t * g) @ F for t in ts]), scale)
        g1, g2 = np.exp(Fh), ranks                                                   # curved: F_s = g1 + 2s·g2
        assert nondecreasing(np.array([tilt(q, s * g1 + s * s * g2) @ F for s in ts / 4]), scale)
        qv = np.array([q[labels == c].sum() for c in range(v.size)])
        A = np.minimum(np.cumsum(qv), 1.0); B = A - qv                              # q(F̂ ≤ v), q(F̂ < v) per level set
        for n in (1.0, 2.5, 7.0, 40.0):                                              # best-of-n's revealed objective
            BlogB = np.where(B > 0, B ** n * np.log(np.where(B > 0, B, 1)), 0.0)
            assert nondecreasing((A ** n * np.log(A) - BlogB) / (A ** n - B ** n), 1.0)
        best = lambda n: q * ((A ** n - B ** n) / qv)[labels]                        # the best of n draws from q
        assert abs(best(3.0).sum() - 1) <= EXACT
        assert nondecreasing(np.array([best(n) @ F for n in np.linspace(1, 60, 600)]), scale)
        above = [q[labels >= j] @ F[labels >= j] / qv[j:].sum() for j in range(v.size)]
        assert nondecreasing(np.array(above), scale)                                 # a rising threshold
        q, Fh, labels, v, F, cell = evaluator_instance(r, monotone=False)
        values = np.array([tilt(q, t * Fh) @ F for t in ts])
        decreasing_without += not nondecreasing(values, 1 + np.abs(F).max())
    assert decreasing_without >= 100                                                 # the hypothesis matters


def test_overoptimization_starts_where_correlation_ends_and_ends_at_the_top():
    """P20: d/dt E_{p_t}[F] = Cov_{p_t}(F̂, m) along the pursuit of F̂ (complex step); E_{p_t}[F] tends to m(v_top);
    and at large intensity the sign of the derivative is the sign of m(v_top) − m(v_next), shown in log space on the
    dominant term of the pairwise form of the covariance."""
    r = rng(1803); H = 1e-30
    for _ in range(300):
        q, Fh, labels, v, F, cell = evaluator_instance(r)
        mv = cell(F); m = mv[labels]; scale = 1 + np.abs(F).max()
        for t in r.uniform(0, 5, 3):
            z = np.log(q) + (t + 1j * H) * Fh; z = z - z.real.max()
            p = np.exp(z) / np.exp(z).sum()
            rate = np.imag(p @ F) / H; ps = p.real
            assert abs(rate - (ps @ (Fh * m) - (ps @ Fh) * (ps @ m))) <= EXACT * scale * (1 + np.abs(Fh).max())
        qv = np.array([q[labels == c].sum() for c in range(v.size)])
        t_far = 40 / (v[-1] - v[-2])
        assert abs(tilt(q, t_far * Fh) @ F - mv[-1]) <= 1e-9 * scale + np.abs(mv).max() * (qv[-2] / qv[-1]) * np.exp(-40) * 10
        t = 1e6 / (v[-1] - v[-2])
        logw = np.log(qv) + t * (v - v[-1]); terms = (v - v[-1]) * (mv - mv[-1])
        j = np.argmax(np.where(terms != 0, logw, -np.inf))
        assert (terms[j] < 0) == (mv[-1] < mv[-2])


def sign_changes(values):
    s = np.sign([x for x in values if x != 0])
    return int(np.sum(s[1:] != s[:-1]))


def level_set_instance(r, shape):
    """Like evaluator_instance, with the regression on the level sets drawn as 'any', 'single-peaked' or 'increasing'."""
    k = int(r.integers(2, 7)); n = int(r.integers(k + 1, 13))
    labels = r.permutation(np.concatenate([np.arange(k), r.integers(0, k, n - k)]))
    v = np.sort(r.normal(0, 1, k)); q = simplex_interior(r, n)
    if shape == "increasing":
        mv = np.sort(r.normal(0, 1, k))
    elif shape == "single-peaked":
        j = int(r.integers(0, k)); up = np.sort(r.normal(0, 1, j + 1))
        mv = np.concatenate([up, np.minimum(np.sort(r.normal(0, 1, k - j - 1))[::-1], up[-1])])
    else:
        mv = r.normal(0, 1, k)
    R0 = r.normal(0, 1, n)
    cellmean = lambda f: np.array([q[labels == c] @ f[labels == c] / q[labels == c].sum() for c in range(k)])
    F = mv[labels] + R0 - cellmean(R0)[labels]
    qv = np.array([q[labels == c].sum() for c in range(k)])
    return q, v[labels], labels, v, qv, mv, F


def no_valley(values, scale):
    """No t1 < t2 < t3 with values[t2] < min(values[t1], values[t3]), up to rounding."""
    left = np.maximum.accumulate(values); right = np.maximum.accumulate(values[::-1])[::-1]
    return bool(np.all(np.minimum(left, right) - values <= 1e-12 * scale))


def test_the_target_curve_turns_no_more_often_than_the_regression():
    """P25: (i) along tilt(q, t·F̂), t real, E_{p_t}[F] − c changes sign at most as often as m(v_1) − c, …, m(v_k) − c,
    with the signs of its first and last non-zero terms at the ends (equality attained often); (ii) increasing m gives a
    non-decreasing curve; (iii) single-peaked m gives a curve with no valley, which can still fall; arbitrary m can give
    a valley. Notes: for best-of-n, E_n[F] − c = (m_k − c) + Σ_{j<k} (m_j − m_{j+1})·A_j^n, and (iii) holds along n."""
    r = rng(2501); cases = attained = valleys = falls = 0
    for _ in range(300):
        q, Fh, labels, v, qv, mv, F = level_set_instance(r, "any")
        scale = 1 + np.abs(F).max(); far = 40 / np.diff(v).min()
        ts = np.linspace(-far, far, 4001)
        for c in r.uniform(mv.min() - 0.5, mv.max() + 0.5, 3):
            if np.abs(mv - c).min() < 0.05:
                continue
            def numerator(t):                                                        # the sign of E_{p_t}[F] − c
                z = np.log(q) + t * Fh; return float(np.exp(z - z.max()) @ (F - c))
            vals = [numerator(t) for t in ts]
            vals = [x for x in vals if abs(x) > 1e-12 * scale]
            bound = sign_changes(mv - c); cases += 1
            assert sign_changes(vals) <= bound
            attained += sign_changes(vals) == bound
            nz = np.sign((mv - c)[mv != c])
            assert np.sign(numerator(-far)) == nz[0] and np.sign(numerator(far)) == nz[-1]
    assert attained >= cases // 2                                                    # the bound is not loose
    ts = np.linspace(-12, 12, 2401)
    for _ in range(300):
        for shape in ("increasing", "single-peaked", "any"):
            q, Fh, labels, v, qv, mv, F = level_set_instance(r, shape)
            scale = 1 + np.abs(F).max()
            E = np.array([tilt(q, t * Fh) @ F for t in ts])
            if shape == "increasing":
                assert nondecreasing(E, scale)
            elif shape == "single-peaked":
                assert no_valley(E, scale)
                falls += not nondecreasing(E, scale)
                ns = np.linspace(1, 200, 800); A = np.minimum(np.cumsum(qv), 1.0); B = A - qv
                En = np.array([q @ (F * ((A ** n - B ** n) / qv)[labels]) for n in ns])  # best of n draws from q
                c = r.normal()
                tele = (mv[-1] - c) + (A[:-1, None] ** ns * (mv[:-1] - mv[1:])[:, None]).sum(axis=0)
                assert np.abs((En - c) - tele).max() <= 1e-9 * scale
                assert no_valley(En, scale)
            else:
                valleys += not no_valley(E, scale)
    assert falls >= 50 and valleys >= 30                                             # the hypotheses matter


def test_binned_evaluators():
    """P26: for an evaluator with distinct values, G = h(F̂) grouping its values into bins of spread at most w, with
    D the largest spread of F in a bin: |E_{p_t}[F] − E_{p_t}[m_G]| ≤ t·w·D/4 along tilt(q, t·F̂), attained to first
    order by a two-outcome bin; with m_G increasing, E_{p_u}[F] ≥ E_{p_s}[F] − (s + u)·w·D/4; with m_G single-peaked,
    E_{p_t}[m_G] has no valley."""
    r = rng(2601); ts = np.linspace(0, 10, 201); falls = 0
    bound = lambda t, w, D: t * w * D / 4
    for trial in range(300):
        n = int(r.integers(12, 120)); q = simplex_interior(r, n); Fh = r.normal(0, 1, n)
        nb = int(r.integers(2, 10)); cuts = np.sort(r.uniform(Fh.min(), Fh.max(), nb - 1))
        b = np.searchsorted(cuts, Fh); used = np.unique(b); b = np.searchsorted(used, b)   # bins 0..k−1, in order
        k = used.size
        if trial % 3 == 0:
            F = 0.7 * Fh + r.normal(0, 1, n) * r.uniform(0.2, 1.5)                 # a noisy target
        else:                                                                        # m_G increasing or single-peaked
            mono = np.sort(r.normal(0, 1, k))
            if trial % 3 == 2:
                j = int(r.integers(0, k - 1)); down = np.sort(r.normal(0, 1, k - j - 1))[::-1]
                mono = np.concatenate([mono[:j + 1], np.minimum(down, mono[j])])
            R0 = r.normal(0, 1, n)
            R0 = R0 - np.array([q[b == c] @ R0[b == c] / q[b == c].sum() for c in range(k)])[b]
            F = mono[b] + R0
        mG = np.array([q[b == c] @ F[b == c] / q[b == c].sum() for c in range(k)])[b]
        w = max(np.ptp(Fh[b == c]) for c in range(k)); D = max(np.ptp(F[b == c]) for c in range(k))
        scale = 1 + np.abs(F).max()
        EF = np.array([tilt(q, t * Fh) @ F for t in ts]); EG = np.array([tilt(q, t * Fh) @ mG for t in ts])
        assert np.all(np.abs(EF - EG) <= bound(ts, w, D) + 1e-12 * scale)
        if trial % 3 == 1:                                                            # for s ≤ u
            for i in range(0, ts.size, 10):
                u = slice(i, None)
                assert np.all(EF[u] - EF[i] >= -bound(ts[i] + ts[u], w, D) - 1e-12 * scale)
        if trial % 3 == 2:
            assert no_valley(EG, scale)
            falls += not nondecreasing(EG, scale)
    assert falls >= 20                                                               # single-peaked curves do fall
    q = np.array([0.5, 0.5]); Fh = np.array([0.0, 1.0]); F = np.array([-1.0, 1.0])   # one bin: w = 1, D = 2, m_G = 0
    for t in (1e-4, 1e-3):
        gap = abs(tilt(q, t * Fh) @ F)
        assert 0.999 * bound(t, 1, 2) <= gap <= bound(t, 1, 2)                       # attained to first order
