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
    general when h merges level sets."""
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
