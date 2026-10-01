"""Checks of P9: the matched pursuit gets the most of F from the actor's departure; the shortfall splits into
misalignment, under-pursuit and anti-pursuit; rescaling F moves the stakes, not misalignment; zero stakes."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt, log_normalizer, kl_tilts
from .test_misalignment import misalignment, ray_minimizer, best_outcomes_limit


def departure_on_ray(q, F, t):
    """d(t) = KL(p_{F,t} || q) = t E_{p_t}[F] - Λ(tF), computed stably."""
    return float(t * (tilt(q, t * F) @ F) - log_normalizer(q, t * F))


def matched_intensity(ph, q, F):
    """λ = inf{t >= 0 : d(t) >= KL(ph || q)}; inf when the departure reaches -log q(A)."""
    d = kl(ph, q); cap = -np.log(q[F >= F.max()].sum())
    if d <= 0:
        return 0.0
    if d >= cap:
        return np.inf
    lo, hi = 0.0, 1.0
    while departure_on_ray(q, F, hi) < d:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if departure_on_ray(q, F, mid) < d else (lo, mid)
    return 0.5 * (lo + hi)


def shortfall(ph, q, F):
    lam = matched_intensity(ph, q, F)
    best = F.max() if np.isinf(lam) else tilt(q, lam * F) @ F
    return float(best - ph @ F), lam


def instance(r):
    n = int(r.integers(2, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
    ph = with_zeros(r, n) if r.random() < 0.3 else tilt(q, r.normal(0, 1.5, n))
    return n, q, F, ph


def test_matched_pursuit_gets_the_most_from_the_departure():
    """P9(i): the matched departure is reached exactly; no behaviour with no more departure gets more of F; S >= 0."""
    r = rng(601); cases = {"finite": 0, "infinite": 0}
    for _ in range(800):
        n, q, F, ph = instance(r)
        S, lam = shortfall(ph, q, F)
        assert S >= -EXACT * (1 + np.abs(F).max())
        if np.isinf(lam):
            cases["infinite"] += 1
            assert kl(ph, q) >= -np.log(q[F >= F.max()].sum()) - EXACT
            continue
        cases["finite"] += 1
        assert abs(departure_on_ray(q, F, lam) - kl(ph, q)) <= 1e-9 * (1 + kl(ph, q))
        best = tilt(q, lam * F) @ F
        for _ in range(10):
            p = tilt(q, r.normal(0, 1.5, n))
            if kl(p, q) <= kl(ph, q):
                assert p @ F <= best + EXACT * (1 + np.abs(F).max())
    assert min(cases.values()) >= 50                                            # both cases exercised


def test_stakes_split_into_three_causes():
    """P9(ii): λ S = M + KL(p° || p_{F,λ}) + λ [E_q F - E_ph F]^+, for 0 < λ < inf."""
    r = rng(602); anti = 0
    for _ in range(800):
        n, q, F, ph = instance(r)
        S, lam = shortfall(ph, q, F)
        if not 0 < lam < np.inf or ph @ F > F.max() - 1e-6:
            continue                                                            # float64 cannot tell the third case apart
        M, ts = misalignment(ph, q, F)
        under = kl_tilts(q, ts * F, lam * F)                                    # p° = p_{F,t*} (t* = 0: p° = q)
        against = lam * max(q @ F - ph @ F, 0.0)
        anti += against > 0
        assert ts <= lam + 1e-9 * (1 + lam)                                     # the actor never out-pursues its budget
        assert abs(lam * S - (M + under + against)) <= 1e-8 * (1 + lam * S)
        assert abs(lam * S - kl(ph, tilt(q, lam * F))) <= 1e-8 * (1 + lam * S) or np.any(tilt(q, lam * F) == 0)
    assert anti >= 50                                                           # the anti-pursuit term is exercised


def test_rescaling_moves_stakes_not_misalignment():
    """P9(iii): F -> aF + c (a > 0) leaves M unchanged and multiplies S by a."""
    r = rng(603)
    for _ in range(300):
        n, q, F, ph = instance(r)
        a, c = float(np.exp(r.uniform(-2, 2))), float(r.normal(0, 3))
        M1, _ = misalignment(ph, q, F); M2, _ = misalignment(ph, q, a * F + c)
        S1, _ = shortfall(ph, q, F); S2, _ = shortfall(ph, q, a * F + c)
        assert abs(M1 - M2) <= 1e-9 * (1 + M1)
        assert abs(S2 - a * S1) <= 1e-9 * (1 + a * abs(S1) + abs(c))


def test_zero_stakes():
    """P9(iv): S = 0 on the ray and on the best outcomes; S = 0 < M when ties are split differently from the default;
    S > 0 off the ray when the departure stays below the cap."""
    r = rng(604)
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        on = tilt(q, float(r.uniform(0.1, 3)) * F)
        assert abs(shortfall(on, q, F)[0]) <= 1e-9
        top = np.argsort(F)[-2:]; F[top[0]] = F[top[1]]                          # two tied best outcomes
        pick = np.eye(n)[top[1]]
        S, lam = shortfall(pick, q, F); M, _ = misalignment(pick, q, F)
        assert np.isinf(lam) and abs(S) <= EXACT and M > 1e-6
        off = tilt(q, r.normal(0, 1, n))
        S, lam = shortfall(off, q, F); M, _ = misalignment(off, q, F)
        if lam < np.inf and M > 1e-6:
            assert S > 0
