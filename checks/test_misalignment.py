"""Checks of P5 (misalignment is attained for full-support behaviour, zero exactly on the closure of the intended set, at
most the departure from the default when the default is intended; its closed form on the pursuit ray in all three cases;
the deviance identity of its Notes), of P6 (the departure from the default splits into pursuit and misalignment), of
P35 (floors and caps) and of P36 (ordinal objectives)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt


def ray_minimizer(ph, q, F):
    """t* of P5(iv): 0 if E_ph F <= E_q F; inf if E_ph F = max F; otherwise the root of E_{p_t} F = E_ph F (bisection;
    E_{p_t} F increases in t)."""
    target = ph @ F
    if target <= q @ F:
        return 0.0
    if target >= F.max() - 1e-12 * (1 + np.abs(F).max()):
        return np.inf
    lo, hi = 0.0, 1.0
    while tilt(q, hi * F) @ F < target:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tilt(q, mid * F) @ F < target else (lo, mid)
    return 0.5 * (lo + hi)


def best_outcomes_limit(q, F):
    """q conditioned on the outcomes where F is largest: the limit of the ray as t -> inf."""
    A = F >= F.max()
    return np.where(A, q, 0.0) / q[A].sum()


def misalignment(ph, q, F):
    ts = ray_minimizer(ph, q, F)
    return (kl(ph, best_outcomes_limit(q, F)) if np.isinf(ts) else kl(ph, tilt(q, ts * F))), ts


def test_minimum_on_the_ray_is_attained_at_the_closed_form():
    r = rng(401)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        if ph @ F >= F.max() - 1e-9:
            continue                                                              # the third case: its own check
        m, ts = misalignment(ph, q, F)
        assert 0 <= ts < np.inf                                                   # the minimizer is on the half-ray
        grid = np.concatenate([np.linspace(0, 2 * ts + 5, 2001), [10 * ts + 50]])
        values = np.array([kl(ph, tilt(q, t * F)) for t in grid])
        assert m <= values.min() + EXACT * (1 + m)                               # nothing on the grid does better
        assert values[-1] > m + 1e-6                                              # far along the ray is worse: attained
        if ts > 0:                                                                # first-order condition: means match
            assert abs(tilt(q, ts * F) @ F - ph @ F) <= 1e-9 * (1 + np.abs(F).max())
        else:
            assert ph @ F <= q @ F


def test_best_outcomes_case():
    """P5(iv), third case: behaviour on the best outcomes. KL decreases along the ray to KL(ph || q(.|best)), not attained;
    zero for a maximizer that splits ties as q does, positive for one that splits them differently."""
    r = rng(405)
    for _ in range(300):
        n = int(r.integers(3, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        top = np.argsort(F)[-2:]; F[top[0]] = F[top[1]]                           # two tied best outcomes
        A = F >= F.max(); gap = F.max() - F[~A].max(); lim = best_outcomes_limit(q, F)
        for ph, zero in ((lim, True), (np.eye(n)[top[1]], False)):               # ties as q splits them; one only
            m, ts = misalignment(ph, q, F)
            assert np.isinf(ts)
            assert (m <= EXACT) == zero
            path = [kl(ph, tilt(q, t * F)) for t in (0.0, 1.0, 5.0, 50.0 / gap)]
            assert all(a >= b - EXACT for a, b in zip(path, path[1:]))           # decreasing along the ray
            assert all(v >= m - EXACT for v in path)                              # never below the limit
            assert path[-1] - m <= (1 - q[A].sum()) / q[A].sum() * np.exp(-50.0) + EXACT   # and approaches it
        # a unique best outcome: the deterministic maximizer is aligned
        F2 = r.normal(0, 1, n); m, _ = misalignment(np.eye(n)[np.argmax(F2)], q, F2)
        assert m <= EXACT


def test_zero_exactly_on_the_intended_set():
    r = rng(402)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t0 = float(r.uniform(0, 3))
        on = tilt(q, t0 * F)
        assert misalignment(on, q, F)[0] <= 1e-9
        off = tilt(q, t0 * F + r.normal(0, 0.5, n))                             # a transverse departure
        if np.linalg.matrix_rank(np.stack([np.log(off / q) - np.log(off / q).mean(), F - F.mean()]), tol=1e-3) == 2:
            assert misalignment(off, q, F)[0] > 1e-6
        # a behaviour with zeros that is not on the closure of the ray is misaligned
        z = with_zeros(r, n)
        if np.abs(z - best_outcomes_limit(q, F)).sum() > 1e-3:
            assert misalignment(z, q, F)[0] > 1e-9


def test_bounded_by_departure_from_default():
    r = rng(403)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        m, _ = misalignment(ph, q, F)
        assert m <= kl(ph, q) + EXACT * (1 + kl(ph, q))


def test_the_ray_leaves_every_compact_set():
    """P5(iv), closedness: the mass at an outcome where F is smallest obeys the bound, so it tends to 0 along the ray."""
    r = rng(404)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        lo, hi = int(np.argmin(F)), int(np.argmax(F)); osc = F[hi] - F[lo]
        for t in (0.0, 1.0, 10.0, 100.0):
            mass, bound = tilt(q, t * F)[lo], q[lo] / q[hi] * np.exp(-t * osc)
            assert mass <= bound * (1 + EXACT) + 1e-300
        # far enough along, as small as we like (the bound is tight for two outcomes: same relative margin as above)
        assert tilt(q, 100.0 / osc * F)[lo] <= q[lo] / q[hi] * np.exp(-100.0) * (1 + EXACT)


def nearest(ph, q, F):
    """The nearest intended behaviour on the closure of the ray: q, p_{F,t*}, or q(.|A)."""
    ts = ray_minimizer(ph, q, F)
    return best_outcomes_limit(q, F) if np.isinf(ts) else tilt(q, ts * F)


def test_departure_splits_into_pursuit_and_misalignment():
    """P6: KL(ph || q) = KL(p° || q) + M(ph), in all three cases of P5(iv)."""
    r = rng(406)
    cases = {"below": 0, "between": 0, "best": 0}
    for _ in range(600):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        kind = r.integers(0, 3)
        if kind == 0:
            ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        elif kind == 1:
            ph = tilt(q, float(r.uniform(0, 3)) * F + r.normal(0, 0.7, n))
        else:
            ph = np.zeros(n); A = F >= F.max(); ph[A] = r.dirichlet(np.ones(A.sum()))
        m, ts = misalignment(ph, q, F); po = nearest(ph, q, F)
        cases["below" if ts == 0 else "best" if np.isinf(ts) else "between"] += 1
        departure, pursuit = kl(ph, q), kl(po, q)
        assert abs(departure - (pursuit + m)) <= 1e-9 * (1 + departure)
        assert -EXACT <= m <= departure + EXACT
        if ph @ F <= q @ F:
            assert abs(m - departure) <= EXACT * (1 + departure)                # all of it is misalignment
    assert min(cases.values()) >= 50                                           # every case exercised


def test_deviance_identity():
    """P5 Notes: for counts with frequencies ph, the log-likelihood ratio of the unrestricted multinomial against the best
    pursuit of F equals n * M(ph)."""
    r = rng(407)
    for _ in range(300):
        k = int(r.integers(2, 13)); q = simplex_interior(r, k); F = r.normal(0, 1, k)
        counts = r.multinomial(int(r.integers(20, 500)), simplex_interior(r, k)); n = counts.sum(); ph = counts / n
        m, ts = misalignment(ph, q, F)
        if np.isinf(ts):
            continue
        loglik = lambda p: float(np.sum(counts[counts > 0] * np.log(p[counts > 0])))
        best_on_ray = max(loglik(tilt(q, t * F)) for t in np.linspace(0, 3 * ts + 3, 1001))
        llr = loglik(ph) - loglik(tilt(q, ts * F))
        assert abs(llr - n * m) <= 1e-9 * (1 + n * m)
        assert loglik(tilt(q, ts * F)) >= best_on_ray - EXACT * n * (1 + np.abs(np.log(q)).max())   # t* is the best fit



def full_ray_point(ph, q, F):
    """t̂ ∈ ℝ with E_{p_{F,t̂}}[F] = E_ph[F], for ph of full support (bisection on the full ray)."""
    target = ph @ F; lo, hi = -1.0, 1.0
    while tilt(q, lo * F) @ F > target:
        lo *= 2
    while tilt(q, hi * F) @ F < target:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tilt(q, mid * F) @ F < target else (lo, mid)
    return 0.5 * (lo + hi)


def test_floors_and_caps():
    """P35: under the intended segment {p_{F,t} : r ≤ t ≤ s}, M = KL(p̂ || p_{F,t̂}) + KL(p_{F,t̂} || p_{F,t°}), with
    t° = min(max(t̂, r), s), as a direct minimization confirms; a floor is a minimum average of F; the threshold floor
    of a fine makes the default itself misaligned; and the KL-regularized imitation of p_T runs along the capped
    segment."""
    from scipy.optimize import minimize_scalar
    from .common import kl_tilts
    r = rng(3501)
    for _ in range(300):
        n = int(r.integers(2, 9)); q = simplex_interior(r, n); F = r.normal(0, 1, n); ph = simplex_interior(r, n)
        lo, hi = np.sort(r.uniform(0, 4, 2)); hi = np.inf if r.random() < 0.3 else hi
        th = full_ray_point(ph, q, F); to = min(max(th, lo), hi)
        formula = kl(ph, tilt(q, th * F)) + kl_tilts(q, th * F, to * F)
        top = hi if np.isfinite(hi) else max(lo, th) + 20
        f = lambda t: kl(ph, tilt(q, t * F))
        direct = min(minimize_scalar(f, bounds=(lo, top), method="bounded", options={"xatol": 1e-12}).fun,
                     f(lo), f(top))                                                  # minima on the boundary, exactly
        assert abs(formula - direct) <= 1e-8 * (1 + direct)
        vmin = tilt(q, lo * F) @ F
        for t in r.uniform(0, 5, 5):
            assert (t >= lo) == (tilt(q, t * F) @ F >= vmin - 1e-15)
    for _ in range(100):                                                             # a threshold floor
        n = int(r.integers(2, 9)); q = simplex_interior(r, n)
        H = np.zeros(n, bool); H[r.choice(n, int(r.integers(1, n)), replace=False)] = True
        F = -H.astype(float); qH = q[H].sum(); eps = r.uniform(0.05, 0.95) * qH
        floor = np.log(qH * (1 - eps) / (eps * (1 - qH)))
        assert floor > 0 and abs(tilt(q, floor * F)[H].sum() - eps) <= EXACT
        assert kl(q, tilt(q, floor * F)) > 0
    for _ in range(100):                                                             # imitation runs along the segment
        n = int(r.integers(2, 7)); q = simplex_interior(r, n); pT = simplex_interior(r, n); t = r.uniform(0.1, 5)
        F = np.log(pT / q); star = tilt(q, t / (1 + t) * F)
        J = lambda p: -kl(p, pT) - kl(p, q) / t
        for _ in range(10):
            p = simplex_interior(r, n)
            assert J(p) <= J(star) + 1e-12


def isotonic(y, w):
    """Weighted least-squares non-decreasing fit of y with weights w (pool adjacent violators)."""
    blocks = [[y[i] * w[i], w[i], 1] for i in range(len(y))]
    out = []
    for b in blocks:
        out.append(b)
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            s, ww, k = out.pop(); out[-1][0] += s; out[-1][1] += ww; out[-1][2] += k
    return np.concatenate([[s / ww] * k for s, ww, k in out])


def test_ordinal_objectives():
    """P36: under the ordinal specification C_F = {p : p/q non-decreasing in F}, the nearest intended behaviour is
    q·r°, r° the q-weighted isotonic regression of the level ratios; M_ord = Σ_B p̂(B)·KL(p̂(·|B) || q(·|B)) over the
    pooled blocks; KL(p̂ || p) ≥ M_ord + KL(p° || p) on C_F, with equality at q; M ≥ M_ord + M(p°); M_ord is unchanged by
    increasing maps of F; and best-of-n by F is ordinally intended."""
    r = rng(3601); strict = 0
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n)
        F = r.integers(0, int(r.integers(2, n + 1)), n).astype(float) + 0.0
        if np.ptp(F) == 0:
            F[0] += 1
        ph = simplex_interior(r, n); levels = np.unique(F)
        qL = np.array([q[F == v].sum() for v in levels]); pL = np.array([ph[F == v].sum() for v in levels])
        rc = isotonic(pL / qL, qL); po = q * rc[np.searchsorted(levels, F)]
        assert abs(po.sum() - 1) <= EXACT and np.all(np.diff(rc) >= -EXACT)          # p° is in C_F
        Mord = kl(ph, po)
        blocks = np.unique(np.round(rc, 12), return_inverse=True)[1][np.searchsorted(levels, F)]
        cond = lambda v, b: v[blocks == b] / v[blocks == b].sum()
        bsum = sum(ph[blocks == b].sum() * kl(cond(ph, b), cond(q, b)) for b in np.unique(blocks))
        assert abs(Mord - bsum) <= 1e-10 * (1 + Mord)
        assert abs(kl(ph, q) - (Mord + kl(po, q))) <= 1e-10 * (1 + kl(ph, q))
        for _ in range(10):                                                          # random members of C_F
            ratios = np.sort(np.exp(r.normal(0, 1, len(levels))))
            p = q * ratios[np.searchsorted(levels, F)]; p /= p.sum()
            assert kl(ph, p) >= Mord + kl(po, p) - 1e-10 * (1 + kl(ph, p))
        M, _ = misalignment(ph, q, F); Mpo, _ = misalignment(po, q, F)
        assert M >= Mord + Mpo - 1e-9 * (1 + M)
        strict += M > Mord + 1e-6
        phi = np.exp(F) + F ** 3                                                     # an increasing map of F
        lv2 = np.unique(phi)
        qL2 = np.array([q[phi == v].sum() for v in lv2]); pL2 = np.array([ph[phi == v].sum() for v in lv2])
        rc2 = isotonic(pL2 / qL2, qL2)
        assert abs(kl(ph, q * rc2[np.searchsorted(lv2, phi)]) - Mord) <= 1e-12 * (1 + Mord)
        A = np.cumsum(qL); B = A - qL                                                 # best-of-n by F
        for m in (2.0, 7.0):
            bon = q * ((A ** m - B ** m) / qL)[np.searchsorted(levels, F)]
            Lb = np.array([bon[F == v].sum() for v in levels])
            rcb = isotonic(Lb / qL, qL)
            assert kl(bon, q * rcb[np.searchsorted(levels, F)]) <= 1e-12
    assert strict >= 100                                                             # the cardinal adds a shape term
