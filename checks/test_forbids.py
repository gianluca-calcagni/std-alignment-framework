"""Checks of the corollaries in derived/forbids.md that need a check of their own: C1 (no ranking of errors holds at
every budget: the worst cases cross), C3 (an error confined to one region costs bounded nats), C5 (the first effect of
optimization depends on the optimizer: softmax policy gradient first pursues q·(F̂ − E_q F̂); the end of pursuit is
set by where the evaluator's top values fall) and C9 (grouping outcomes never shows more misalignment)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, kl, tilt, kl_tilts, random_partition, coarse
from .test_feasibility import rise
from .test_misalignment import misalignment


def width(q, E, delta):
    return rise(q, E, delta) + rise(q, -E, delta)


def test_no_ranking_of_errors_holds_at_every_budget():
    """C1: if Var_q(E₁) > Var_q(E₂) and the range of E₁ is smaller than that of E₂, the worst cases cross: w_δ(E₁) >
    w_δ(E₂) at small budgets, and w_δ(E₁) < w_δ(E₂) once both budgets reach their ends."""
    r = rng(4101); crossed = 0
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n)
        E1 = r.uniform(-1, 1, n)                                                     # spread out, moderate range
        x = int(np.argmin(q)); E2 = np.zeros(n); E2[x] = r.uniform(2.5, 6)            # a spike on a rare outcome
        V1, V2 = q @ (E1 - q @ E1) ** 2, q @ (E2 - q @ E2) ** 2
        if not (V1 > V2 and np.ptp(E1) < np.ptp(E2)):
            continue
        ends = max(-np.log(q[E <= E.min()].sum()) for E in (E1, E2, -E1, -E2)) * 1.01
        assert width(q, E1, 1e-7) > width(q, E2, 1e-7)
        assert width(q, E1, ends) < width(q, E2, ends)
        crossed += 1
    assert crossed >= 100


def test_an_error_confined_to_one_region_costs_bounded_nats():
    """C3: for p̂ = p_{F + M·1_A, t}, M(p̂) ≤ KL(p̂ || p_{F,t}) = kl(p̂(A) || p_{F,t}(A)) ≤ max(log 1/a, log 1/(1 − a)),
    with a = p_{F,t}(A), for every M; and the bound is approached as M → ±∞."""
    r = rng(4301)
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t = r.uniform(0.1, 3)
        A = np.zeros(n, bool); A[r.choice(n, int(r.integers(1, n)), replace=False)] = True
        a = tilt(q, t * F)[A].sum(); cap = max(np.log(1 / a), np.log(1 / (1 - a)))
        for M in (-1e3, -10.0, -1.0, 1.0, 10.0, 1e3):
            G = t * (F + M * A)
            d = kl_tilts(q, G, t * F)
            pa = tilt(q, G)[A].sum()
            binary = sum(u * np.log(u / v) for u, v in ((pa, a), (1 - pa, 1 - a)) if u > 0)
            assert abs(d - binary) <= 1e-9 * (1 + cap) and d <= cap + 1e-9
            if abs(M) <= 10:
                Mis, _ = misalignment(tilt(q, G), q, F)
                assert Mis <= d + 1e-9
        up, down = kl_tilts(q, t * (F + 1e3 * A), t * F), kl_tilts(q, t * (F - 1e3 * A), t * F)
        assert abs(up - np.log(1 / a)) <= 1e-6 * (1 + cap) and abs(down - np.log(1 / (1 - a))) <= 1e-6 * (1 + cap)


def test_the_first_effect_depends_on_the_optimizer():
    """C5: one step of softmax policy gradient on E_p[F̂] from logits log q is the tilt of q by η·q·(F̂ − E_q F̂), so
    the target's average starts at the rate Σ_x q(x)²·(F̂(x) − E_q F̂)·(F(x) − E_q F) (complex step), whose sign can
    differ from that of Cov_q(F̂, F); and along the pursuit of F̂ the average tends to E_q[F | F̂ largest], which is
    max F exactly when the largest values of F̂ fall on largest values of F."""
    r = rng(4501); opposite = 0; H = 1e-30
    for _ in range(400):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); Fh = F + r.normal(0, 1.5, n)
        g = q * (Fh - q @ Fh)                                                        # the gradient of E_p[F̂] at p = q
        z = np.log(q) + 1j * H * g; z = z - z.real.max(); p = np.exp(z) / np.exp(z).sum()
        rate = np.imag(p @ F) / H
        assert abs(rate - (q ** 2 * (Fh - q @ Fh)) @ (F - q @ F)) <= EXACT * (1 + np.abs(F).max() + np.abs(Fh).max())
        cov = q @ ((Fh - q @ Fh) * (F - q @ F))
        opposite += (rate * cov < 0) and min(abs(rate), abs(cov)) > 1e-6
    assert opposite >= 10                                                            # the sign can flip
    for _ in range(200):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        top = np.zeros(n, bool); top[r.choice(n, int(r.integers(1, 3)), replace=False)] = True
        Fh = np.where(top, 5.0, r.normal(0, 1, n))
        end = tilt(q, 60 * Fh) @ F; target = q[top] @ F[top] / q[top].sum()
        assert abs(end - target) <= 1e-9 * (1 + np.abs(F).max())
        assert (abs(target - F.max()) <= EXACT) == bool(np.all(F[top] >= F.max() - EXACT))


def test_grouping_never_shows_more_misalignment():
    """C9: for any specification, here a finite set of full-support intended behaviours, the misalignment read from the
    cell masses of a resolution, min over p in the set of KL(p̂_ℬ || p_ℬ), is at most the misalignment M(p̂)."""
    r = rng(4901)
    for _ in range(400):
        n = int(r.integers(3, 10)); labels = random_partition(r, n); ph = simplex_interior(r, n)
        intended = [simplex_interior(r, n) for _ in range(int(r.integers(1, 6)))]
        fine = min(kl(ph, p) for p in intended)
        cells = min(kl(coarse(ph, labels), coarse(p, labels)) for p in intended)
        assert cells <= fine + EXACT * (1 + fine)
