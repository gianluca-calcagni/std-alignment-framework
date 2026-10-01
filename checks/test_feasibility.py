"""Checks of P15: the best feasible behaviour exists, is unique and has full support; convex limits give the Pythagorean
inequality and linear limits the equality, with the exponential form; the split is the accounting of net value; and
misalignment splits into avoidable and unavoidable parts. For the Notes: contexts, a coarse actor and a random
environment are linear limits, and a curved (non-convex) limit can break the split."""
import itertools
import numpy as np
from scipy.optimize import minimize
from .common import EXACT, rng, simplex_interior, kl, tilt, log_normalizer, random_partition
from .test_misalignment import misalignment


def project_linear(r, A, b):
    """argmin over {p in Δ : A p = b} of KL(p || r). By (iii) it is tilt(r, Aᵀθ), with θ minimizing the convex dual
    log E_r[exp(Aᵀθ)] − θ·b; solved by BFGS, then polished by damped Newton steps."""
    dual = lambda th: log_normalizer(r, A.T @ th) - th @ b
    grad = lambda th: A @ tilt(r, A.T @ th) - b
    th = minimize(dual, np.zeros(A.shape[0]), jac=grad, method="BFGS", options={"gtol": 1e-13, "maxiter": 10000}).x
    for _ in range(30):
        p = tilt(r, A.T @ th)
        H = (A * p) @ A.T - np.outer(A @ p, A @ p)
        step = np.linalg.lstsq(H, grad(th), rcond=None)[0]
        lam = 1.0
        while dual(th - lam * step) > dual(th) + 1e-15 and lam > 1e-8:
            lam /= 2
        th = th - lam * step
    return tilt(r, A.T @ th)


def a_member(r, A, b):
    """A random full-support behaviour in {p : A p = b}: the projection of a random behaviour."""
    return project_linear(simplex_interior(r, A.shape[1]), A, b)


def random_linear(r, n):
    m = int(r.integers(1, n - 1)); A = r.normal(0, 1, (m, n))
    return A, A @ simplex_interior(r, n)                                           # contains a full-support behaviour


def gap(p, r_, star):
    return kl(p, r_) - kl(p, star) - kl(star, r_)


def test_linear_limits_split_exactly():
    """P15(i), (iii): the projection on a linear set has full support and the form tilt(r, Σ θ_i f_i), and
    KL(p || r) = KL(p || p*) + KL(p* || r) for every feasible p."""
    r = rng(1501)
    for _ in range(200):
        n = int(r.integers(3, 10)); r_ = simplex_interior(r, n); A, b = random_linear(r, n)
        star = project_linear(r_, A, b)
        assert np.abs(A @ star - b).max() <= 1e-9 * (1 + np.abs(b).max())          # feasible
        assert star.min() > 0
        B = np.vstack([A, np.ones(n)]).T; g = np.log(star / r_)                      # exponential form
        assert np.linalg.norm(g - B @ np.linalg.lstsq(B, g, rcond=None)[0]) <= 1e-8 * (1 + np.abs(g).max())
        for _ in range(5):
            p = a_member(r, A, b)
            assert abs(gap(p, r_, star)) <= 1e-8 * (1 + kl(p, r_))


def test_convex_limits_give_an_inequality():
    """P15(ii): on the convex set {p : p(x₀) <= c}, KL(p || r) >= KL(p || p*) + KL(p* || r), strictly for some p."""
    r = rng(1502); strict = 0
    for _ in range(300):
        n = int(r.integers(3, 8)); r_ = simplex_interior(r, n); c = r_[0] * r.uniform(0.2, 0.8)
        star = r_.copy(); star[0] = c; star[1:] *= (1 - c) / r_[1:].sum()          # the projection, in closed form
        for _ in range(10):
            p = simplex_interior(r, n)
            if p[0] > c:
                continue
            d = gap(p, r_, star)
            assert d >= -EXACT * (1 + kl(p, r_))
            strict += d > 1e-6
    assert strict >= 100


def test_curved_limits_can_break_the_split():
    """P15 Notes: on a curved family {tilt(q₀, s·G) : s ∈ ℝ}, which is not convex, the inequality of (ii) fails for
    some members: limits of capacity give no split."""
    from scipy.optimize import minimize_scalar
    r = rng(1503); broken = 0
    for _ in range(100):
        n = int(r.integers(3, 8)); q0 = simplex_interior(r, n); G = r.normal(0, 1, n); r_ = simplex_interior(r, n)
        s0 = minimize_scalar(lambda s: kl(tilt(q0, s * G), r_), bounds=(-20, 20), method="bounded",
                             options={"xatol": 1e-12}).x
        star = tilt(q0, s0 * G)
        broken += any(gap(tilt(q0, s * G), r_, star) < -1e-6 for s in np.linspace(-5, 5, 21))
    assert broken >= 20


def test_the_split_is_the_accounting_of_net_value():
    """P15(iv): with r = p_{F,t}, no feasible behaviour has more net value than p*; t (J_t(p*) − J_t(p)) = KL(p || p*)
    on a linear set; and t (J_t(p_{F,t}) − J_t(p*)) = KL(p* || p_{F,t})."""
    r = rng(1504)
    for _ in range(200):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t = float(r.uniform(0.2, 3))
        pt = tilt(q, t * F); A, b = random_linear(r, n); star = project_linear(pt, A, b)
        J = lambda p: p @ F - kl(p, q) / t
        scale = 1 + np.abs(F).max() + kl(star, q) / t
        assert abs(t * (J(pt) - J(star)) - kl(star, pt)) <= 1e-9 * t * scale
        for _ in range(5):
            p = a_member(r, A, b)
            assert J(p) <= J(star) + 1e-9 * scale
            assert abs(t * (J(star) - J(p)) - kl(p, star)) <= 1e-8 * t * scale


def test_misalignment_splits_into_avoidable_and_unavoidable():
    """P15(v): for p̂ in a linear feasible set, with p° its nearest intended behaviour and p*° the projection of p°,
    M(p̂) = KL(p̂ || p*°) + KL(p*° || p°)."""
    r = rng(1505); seen = 0
    for _ in range(300):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); A, b = random_linear(r, n)
        ph = a_member(r, A, b)
        M, ts = misalignment(ph, q, F)
        if not np.isfinite(ts):
            continue
        seen += 1
        po = tilt(q, ts * F); star = project_linear(po, A, b)
        assert abs(M - kl(ph, star) - kl(star, po)) <= 1e-8 * (1 + M)
    assert seen >= 250


def test_contexts_and_coarse_actors_are_linear_limits():
    """P15 Notes: with fixed context masses, the best feasible pursuit is pursuit within each context at the shared
    intensity, and the unavoidable part is KL(q_𝒞 || (p_{F,t})_𝒞); for an actor limited to 𝒜 (fixed ratios inside
    cells) it is tilt(q, t·F̄), the best effort of [P8](ii)."""
    r = rng(1506)
    for _ in range(200):
        n = int(r.integers(3, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t = float(r.uniform(0.2, 3))
        pt = tilt(q, t * F); labels = random_partition(r, n); k = labels.max() + 1
        A = np.array([(labels == c).astype(float) for c in range(k)]); b = A @ q        # contexts: fixed masses
        star = project_linear(pt, A, b)
        within = np.zeros(n)
        for c in range(k):
            m = labels == c
            within[m] = q[m].sum() * tilt(q[m] / q[m].sum(), t * F[m])
        assert np.abs(star - within).max() <= 1e-9
        assert abs(kl(star, pt) - kl(b, A @ pt)) <= 1e-9 * (1 + kl(star, pt))
        rows = []                                                                      # coarse: fixed within-cell ratios
        for c in range(k):
            idx = np.flatnonzero(labels == c)
            for i, j in zip(idx[:-1], idx[1:]):
                f = np.zeros(n); f[i], f[j] = q[j], -q[i]; rows.append(f)
        if rows:
            Fbar = (A @ (q * F) / (A @ q))[labels]
            assert np.abs(project_linear(pt, np.array(rows), np.zeros(len(rows))) - tilt(q, t * Fbar)).max() <= 1e-9


def trajectories(p1, p2, P1, P2):
    """The distribution of (a₁, s₁, a₂, s₂) from a policy (p1[a₁], p2[a₁, s₁, a₂]) and transitions P1, P2."""
    out = np.zeros((2, 2, 2, 2))
    for a1, s1, a2, s2 in itertools.product(range(2), repeat=4):
        out[a1, s1, a2, s2] = p1[a1] * P1[a1, s1] * p2[a1, s1, a2] * P2[a1, s1, a2, s2]
    return out.ravel()


def best_policy(pi1, pi2, P1, P2, V):
    """The projection of tilt(q, V) on the policies: a backward recursion that averages over the environment's moves
    and reweights the default policy by e^Q at each step (the maximum-entropy policy)."""
    Q2 = (P2 * V).sum(-1)
    s2 = pi2 * np.exp(Q2); V2 = np.log(s2.sum(-1)); s2 = s2 / s2.sum(-1, keepdims=True)
    Q1 = (P1 * V2).sum(-1)
    s1 = pi1 * np.exp(Q1); s1 = s1 / s1.sum()
    return s1, s2


def test_a_random_environment_is_a_linear_limit():
    """P15 Notes: trajectory distributions with fixed transition probabilities form a linear set; the maximum-entropy
    policy is the projection (the split is exact and no policy has more net value); the unavoidable part is positive
    in a random environment and zero in a deterministic one."""
    r = rng(1507)
    pol = lambda: (r.dirichlet(np.ones(2)), r.dirichlet(np.ones(2), size=(2, 2)))
    unavoidable = []
    for _ in range(200):
        P1 = r.dirichlet(np.ones(2), size=2); P2 = r.dirichlet(np.ones(2), size=(2, 2, 2))
        pi1, pi2 = pol(); q = trajectories(pi1, pi2, P1, P2); R = r.normal(0, 1, 16); t = float(r.uniform(0.3, 3))
        pt = tilt(q, t * R)
        star = trajectories(*best_policy(pi1, pi2, P1, P2, (t * R).reshape(2, 2, 2, 2)), P1, P2)
        J = lambda p: t * (p @ R) - kl(p, q)
        for _ in range(5):
            ph = trajectories(*pol(), P1, P2)
            assert abs(gap(ph, pt, star)) <= 1e-9 * (1 + kl(ph, pt))
            assert J(ph) <= J(star) + 1e-9
        unavoidable.append(kl(star, pt))
    assert min(unavoidable) > 1e-4
    for _ in range(50):                                                                # deterministic environment
        P1 = np.eye(2)[r.integers(0, 2, 2)]; P2 = np.eye(2)[r.integers(0, 2, (2, 2, 2))]
        pi1, pi2 = pol(); q = trajectories(pi1, pi2, P1, P2); R = r.normal(0, 1, 16)
        m = q > 0; pt = np.zeros(16); pt[m] = tilt(q[m], R[m])
        star = trajectories(*best_policy(pi1, pi2, P1, P2, R.reshape(2, 2, 2, 2)), P1, P2)
        assert kl(star[m], pt[m]) <= 1e-12
