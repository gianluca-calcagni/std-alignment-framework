"""Checks of P7 (a specification stated at a coarser resolution depends only on cell masses, and removes exactly the
within-cell departure) and P8 (an actor that cannot tell the outcomes inside a cell apart: its behaviours, its best
effort, the misalignment it cannot remove, and how its misalignment starts to grow with effort)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt, random_partition, coarse
from .test_misalignment import misalignment


def cell_average(F, q, labels):
    """E_q[F | cells]: on each cell, the default's average of F there."""
    out = np.empty_like(F, dtype=float)
    for c in range(labels.max() + 1):
        m = labels == c
        out[m] = q[m] @ F[m] / q[m].sum()
    return out


def lift(masses, splits, labels):
    """The behaviour with these cell masses and these within-cell splits (splits[c] sums to 1 on cell c)."""
    p = np.empty(labels.size)
    for c in range(labels.max() + 1):
        p[labels == c] = masses[c] * splits[c]
    return p


def var(q, G):
    return q @ G ** 2 - (q @ G) ** 2


def test_indifference_depends_only_on_cell_masses():
    """P7(i): against intended behaviours constrained only on cell masses, the best within-cell split is the actor's own,
    so misalignment is computed on cell masses."""
    r = rng(501)
    for _ in range(300):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1
        ph = simplex_interior(r, n); qc = simplex_interior(r, k); Fc = r.normal(0, 1, k)
        pc = tilt(qc, float(r.uniform(0, 3)) * Fc)                                # an intended point on the cell ray
        own = [ph[labels == c] / ph[labels == c].sum() for c in range(k)]
        best = kl(ph, lift(pc, own, labels))
        assert abs(best - kl(coarse(ph, labels), pc)) <= EXACT * (1 + best)     # the actor's own split: cell term only
        for _ in range(10):                                                      # any other split does no better
            other = [simplex_interior(r, int((labels == c).sum())) for c in range(k)]
            assert kl(ph, lift(pc, other, labels)) >= best - EXACT * (1 + best)
        # two behaviours with the same cell masses get the same misalignment
        ph2 = lift(coarse(ph, labels), [simplex_interior(r, int((labels == c).sum())) for c in range(k)], labels)
        qcells = coarse(np.full(n, 1 / n), labels)                               # a default on the cells
        m1, _ = misalignment(coarse(ph, labels), qcells, Fc)
        m2, _ = misalignment(coarse(ph2, labels), qcells, Fc)
        assert abs(m1 - m2) <= EXACT * (1 + m1)


def test_indifference_removes_the_within_cell_departure():
    """P7(ii): for an objective constant on cells, M_fine = M_coarse + W, with W the within-cell departure."""
    r = rng(502)
    for _ in range(500):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); q = simplex_interior(r, n)
        Fc = r.normal(0, 1, labels.max() + 1); F = Fc[labels]
        if np.ptp(Fc) < 1e-3:
            continue
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        if ph @ F >= F.max() - 1e-9:
            continue
        m_fine, _ = misalignment(ph, q, F)
        m_coarse, _ = misalignment(coarse(ph, labels), coarse(q, labels), Fc)
        W = kl(ph, q) - kl(coarse(ph, labels), coarse(q, labels))
        assert W >= -EXACT
        assert abs(m_fine - (m_coarse + W)) <= 1e-9 * (1 + m_fine)


def test_ties_are_forgiven_when_merged():
    """P7, example: a maximizer that picks one of two tied best outcomes is charged at the finest resolution and aligned
    once the principal declares indifference between them."""
    r = rng(503)
    for _ in range(200):
        n = int(r.integers(3, 12)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        top = np.argsort(F)[-2:]; F[top[0]] = F[top[1]]
        labels = np.arange(n); labels[top[0]] = labels[top[1]]; labels = np.unique(labels, return_inverse=True)[1]
        Fc = np.array([F[labels == c][0] for c in range(labels.max() + 1)])
        pick = np.eye(n)[top[1]]
        assert misalignment(pick, q, F)[0] > 1e-6                                 # charged when ties are distinguished
        assert misalignment(coarse(pick, labels), coarse(q, labels), Fc)[0] <= EXACT   # aligned once they are merged


def test_limited_behaviours_are_tilts_by_cell_functions():
    """P8(i): an actor-limited behaviour of full support is tilt(q, G) with G constant on cells, and E_p[F] = E_p[F̄]."""
    r = rng(504)
    for _ in range(300):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1; q = simplex_interior(r, n)
        masses = simplex_interior(r, k)
        p = lift(masses, [q[labels == c] / q[labels == c].sum() for c in range(k)], labels)
        G = np.log(masses / coarse(q, labels))[labels]
        assert np.max(np.abs(tilt(q, G) - p)) <= EXACT
        F = r.normal(0, 1, n)
        assert abs(p @ F - p @ cell_average(F, q, labels)) <= EXACT * (1 + np.abs(F).max())


def test_best_effort_pursues_the_cell_average():
    """P8(ii): among actor-limited behaviours, tilt(q, t F̄) has the highest net value."""
    r = rng(505)
    for _ in range(300):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1; q = simplex_interior(r, n)
        F = r.normal(0, 1, n); t = float(np.exp(r.uniform(-2, 2))); Fb = cell_average(F, q, labels)
        J = lambda p: p @ F - kl(p, q) / t
        best = J(tilt(q, t * Fb))
        for _ in range(20):
            G = r.normal(0, 2, k)[labels]
            assert J(tilt(q, G)) <= best + EXACT * (1 + abs(best))


def test_irreducible_misalignment_is_a_jensen_gap():
    """P8(iii): against a single intended behaviour p*, the least misalignment of an actor-limited behaviour is
    -log E_q[exp(E_q[b | cells])], b = log(p*/q), reached by tilt(q, E_q[b | cells]); zero iff p* is actor-limited."""
    r = rng(506)
    for _ in range(300):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1; q = simplex_interior(r, n)
        pstar = simplex_interior(r, n); b = np.log(pstar / q); bb = cell_average(b, q, labels)
        gap = -np.log(q @ np.exp(bb))
        reached = kl(tilt(q, bb), pstar)
        assert abs(reached - gap) <= EXACT * (1 + gap)
        assert gap >= -EXACT
        for _ in range(20):
            assert kl(tilt(q, r.normal(0, 2, k)[labels]), pstar) >= gap - EXACT * (1 + gap)
        # zero exactly when p* splits each cell as the default does
        limited = tilt(q, r.normal(0, 1, k)[labels]); bl = np.log(limited / q)
        assert -np.log(q @ np.exp(cell_average(bl, q, labels))) <= EXACT
        spread = max(np.ptp(b[labels == c]) for c in range(k))
        if spread > 0.1:
            assert gap > 1e-9


def test_coarse_pursuit_is_misaligned_at_every_effort():
    """P8(iv): the best effort tilt(q, t F̄) is on the pursuit ray of F for every t iff F is constant on cells or F̄ is
    constant; otherwise its misalignment is positive at every t > 0."""
    r = rng(507)
    for _ in range(300):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); k = labels.max() + 1; q = simplex_interior(r, n)
        F = r.normal(0, 1, n); Fb = cell_average(F, q, labels)
        if np.ptp(Fb) < 1e-2 or np.ptp(F - Fb) < 1e-2:
            continue
        for t in (0.1, 1.0, 5.0):
            assert misalignment(tilt(q, t * Fb), q, F)[0] > 0
        Fc = r.normal(0, 1, k)[labels]                                          # an objective the actor can see
        for t in (0.1, 1.0, 5.0):
            assert misalignment(tilt(q, t * cell_average(Fc, q, labels)), q, Fc)[0] <= 1e-9
    # an actor that sees no difference between its cells (F̄ constant) stays at the default, which is intended
    q = np.full(4, 0.25); labels = np.array([0, 0, 1, 1]); F = np.array([1.0, -1.0, 1.0, -1.0])
    Fb = cell_average(F, q, labels)
    assert np.ptp(Fb) <= EXACT and misalignment(tilt(q, 3.0 * Fb), q, F)[0] <= EXACT


def test_coarse_misalignment_starts_quadratic_and_need_not_keep_growing():
    """P8(iv): M(tilt(q, t F̄)) / t^2 -> Var(F̄)(1 - Var(F̄)/Var(F))/2 as t -> 0; and a case where it later falls to 0."""
    r = rng(508)
    for _ in range(100):
        n = int(r.integers(3, 12)); labels = random_partition(r, n); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        Fb = cell_average(F, q, labels); vb, vf = var(q, Fb), var(q, F)
        if vb < 1e-3 or vf - vb < 1e-3:
            continue
        limit = 0.5 * vb * (1 - vb / vf)
        e1, e2 = (abs(misalignment(tilt(q, t * Fb), q, F)[0] / t ** 2 - limit) for t in (1e-2, 1e-3))
        assert e2 <= 1e-2 * limit                                                # close at small effort
        assert e2 <= e1 + 1e-12                                                  # and closer as effort shrinks
    # not monotone: the actor's best cell is the single best outcome, so high effort becomes aligned again. Intensities
    # stay where float64 represents the mass off the best outcome (beyond t ~ 30 it underflows to 0)
    q = np.array([0.3, 0.3, 0.4]); labels = np.array([0, 1, 1]); F = np.array([2.0, 1.5, -1.0])
    Fb = cell_average(F, q, labels)
    Ms = [misalignment(tilt(q, t * Fb), q, F)[0] for t in (0.0, 2.0, 10.0)]
    assert Ms[0] <= EXACT and Ms[1] > 1e-2 and Ms[2] < Ms[1] / 100
