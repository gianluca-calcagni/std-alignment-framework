"""Probes for v14/resolution.md (RS1-RS5), v14/targets.md (TG1-TG2, SN1) and v14/constraints.md (VK6, VK7).
Probed, not tested: every result is proved in its file; this script checks the proofs' claims on random instances
and prints the numbers the files quote. Run from the repository's root: python3 probes/v14/resolution.py
"""
import math
import numpy as np
from scipy.optimize import minimize, minimize_scalar, linprog, brentq

rng = np.random.default_rng(20261017)


def kl(p, a):
    p, a = np.asarray(p, float).ravel(), np.asarray(a, float).ravel()
    m = p > 0
    if np.any(a[m] <= 0):
        return np.inf
    return float(np.sum(p[m] * np.log(p[m] / a[m])))


def klb(u, v):
    return kl([u, 1 - u], [v, 1 - v])


def agg(p, cells):
    return np.array([p[c].sum() for c in cells])


def min_kl(obj, n, A_ub=None, b_ub=None, A_eq=None, b_eq=None, starts=6):
    """min over a in the simplex (with linear constraints) of obj(a), by SLSQP from several starts."""
    cons = [{"type": "eq", "fun": lambda a: a.sum() - 1}]
    if A_ub is not None:
        cons.append({"type": "ineq", "fun": lambda a: b_ub - A_ub @ a})
    if A_eq is not None:
        cons.append({"type": "eq", "fun": lambda a: A_eq @ a - b_eq})
    best, arg = np.inf, None
    for _ in range(starts):
        a0 = rng.dirichlet(np.ones(n))
        r = minimize(lambda a: obj(np.maximum(a, 1e-300)), a0, method="SLSQP", bounds=[(1e-12, 1)] * n,
                     constraints=cons, options={"ftol": 1e-15, "maxiter": 4000})
        ok = abs(r.x.sum() - 1) < 1e-8 and (A_ub is None or np.all(A_ub @ r.x <= b_ub + 1e-9)) and \
            (A_eq is None or np.all(np.abs(A_eq @ r.x - b_eq) < 1e-8))
        if (r.success or ok) and r.fun < best:
            best, arg = r.fun, r.x
    return best, arg


def random_budgets(n, k, p):
    """k budgets (g_j, b_j) that the uniform behaviour keeps strictly and p breaks at least one of."""
    G = rng.normal(size=(k, n))
    u = np.ones(n) / n
    b = G @ u + rng.uniform(0.05, 0.4, size=k)
    return G, b


def partitions_chain(n):
    """A chain of partitions of range(n): coarse ⊑ middle ⊑ finest."""
    perm = rng.permutation(n)
    mid = [list(perm[i:i + 2]) for i in range(0, n, 2)]
    coarse = [mid[0] + mid[1]] + mid[2:]
    fine = [[i] for i in range(n)]
    return coarse, mid, fine


print("RS1, RS2, RS3, RS4 on random instances: six outcomes, two budgets, a chain of three partitions")
worst_mono, worst_bet, worst_rs3, worst_rs4, worst_growth, spread = 0.0, 0.0, 0.0, 0.0, 0.0, []
N_INST = 40
for inst in range(N_INST):
    n = 6
    p = rng.dirichlet(np.ones(n) * 0.7)
    G, b = random_budgets(n, 2, p)
    coarse, mid, fine = partitions_chain(n)
    Ms = []
    for cells in (coarse, mid, fine):
        val, arg = min_kl(lambda a, cells=cells: kl(agg(p, cells), agg(a, cells)), n, G, b)
        Ms.append(val)
    worst_mono = min(worst_mono, Ms[1] - Ms[0], Ms[2] - Ms[1])          # RS1: non-negative increments
    # RS2: the best coarse bet k = p_R / a*_R, read on outcomes, costs at most 1 under every acceptable behaviour
    val, astar = min_kl(lambda a: kl(agg(p, coarse), agg(a, coarse)), n, G, b)
    pc, ac = agg(p, coarse), agg(astar, coarse)
    k = np.where(pc > 0, pc / np.maximum(ac, 1e-300), 0.0)
    h = np.zeros(n)
    for j, c in enumerate(coarse):
        h[c] = k[j]
    lp = linprog(-h, A_ub=G, b_ub=b, A_eq=np.ones((1, n)), b_eq=[1], bounds=[(0, 1)] * n)
    worst_bet = max(worst_bet, -lp.fun - 1)
    growth = sum(pc[j] * math.log(k[j]) for j in range(len(coarse)) if pc[j] > 0)
    worst_growth = max(worst_growth, abs(growth - val))
    # RS4: the lower end is attained by splitting p's coarse cells as a* does
    p2 = np.zeros(n)
    for j, c in enumerate(coarse):
        if pc[j] > 0:
            p2[c] = pc[j] * astar[c] / astar[c].sum()
    full2, _ = min_kl(lambda a: kl(p2, a), n, G, b)
    worst_rs4 = max(worst_rs4, abs(full2 - Ms[0]))
    # the hidden part over the fibre: other splits of the same coarse masses
    hs = []
    for _ in range(4):
        p3 = np.zeros(n)
        for j, c in enumerate(coarse):
            p3[c] = pc[j] * rng.dirichlet(np.ones(len(c)))
        hs.append(min_kl(lambda a: kl(p3, a), n, G, b, starts=3)[0] - Ms[0])
    spread.append(max(hs))
    # RS3: a requirement stated at the middle resolution (costs constant on its cells) is judged there
    Gm = np.array([[g[[c for c in mid if i in c][0]].mean() for i in range(n)] for g in G])
    bm = Gm @ (np.ones(n) / n) + rng.uniform(0.02, 0.2, size=2)
    full_m, _ = min_kl(lambda a: kl(p, a), n, Gm, bm)
    at_mid, _ = min_kl(lambda a: kl(agg(p, mid), agg(a, mid)), n, Gm, bm)
    worst_rs3 = max(worst_rs3, abs(full_m - at_mid))
print(f"  RS1: least increment along the chain {worst_mono:.1e} (non-negative up to solver tolerance)")
print(f"  RS2: the best coarse bet costs at most 1 + {worst_bet:.1e} under the acceptable set; "
      f"its growth equals the coarse misalignment within {worst_growth:.1e}")
print(f"  RS3: a requirement stated at the middle resolution: full and middle misalignment agree within "
      f"{worst_rs3:.1e}")
print(f"  RS4: the split of the coarse cells as a* splits them has full misalignment equal to the coarse one within "
      f"{worst_rs4:.1e}; other splits of the same coarse masses hide up to {max(spread):.3f} nats more "
      f"(median over instances {np.median(spread):.3f})")

print("\nRS5 and FA1: an actor's view as a partition of conditions (actions are the outcomes themselves)")
w = np.array([0.5, 0.3, 0.2])
nX = 3
P = rng.dirichlet(np.ones(nX), size=3)                                  # the actor's behaviour per condition
views = {"full": [[0], [1], [2]], "merges 1 and 2": [[0], [1, 2]], "sees nothing": [[0, 1, 2]]}
# the request: on pairs, a budget on a condition-dependent cost; p breaks it
# a cost on pairs whose cheapest outcome differs by condition, and a budget the full view can keep and a view that
# merges conditions 1 and 2 cannot
Gc = np.array([[0., 1., 2.], [2., 0., 1.], [1., 2., 0.]])
full_min = float(sum(w[i] * Gc[i].min() for i in range(3)))
merged_min = float(w[0] * Gc[0].min() + min(w[1] * Gc[1, x] + w[2] * Gc[2, x] for x in range(nX)))
bc = full_min + 0.3 * (merged_min - full_min)


def least_for_view(cells, starts=8):
    """least misalignment over behaviours whose per-condition rows are equal within each cell of the view: one joint
    convex program over the rows (one per cell) and an acceptable behaviour on pairs, KL being jointly convex."""
    k = len(cells)

    def joint(v):
        rows = np.zeros((3, nX))
        for j, c in enumerate(cells):
            rows[c] = v[j * nX:(j + 1) * nX]
        return (w[:, None] * rows).ravel()
    cons = [{"type": "eq", "fun": lambda v, j=j: v[j * nX:(j + 1) * nX].sum() - 1} for j in range(k)]
    cons += [{"type": "eq", "fun": lambda v, i=i: v[k * nX:].reshape(3, nX)[i].sum() - w[i]} for i in range(3)]
    cons.append({"type": "ineq", "fun": lambda v: bc - Gc.ravel() @ v[k * nX:]})
    best = np.inf
    for _ in range(starts):
        v0 = np.concatenate([rng.dirichlet(np.ones(nX), size=k).ravel(),
                             (rng.dirichlet(np.ones(nX), size=3) * w[:, None]).ravel()])
        r = minimize(lambda v: kl(joint(v), np.maximum(v[k * nX:], 1e-300)), v0, method="SLSQP",
                     bounds=[(0, 1)] * (k * nX) + [(1e-12, 1)] * (3 * nX), constraints=cons,
                     options={"ftol": 1e-15, "maxiter": 5000})
        if r.success:
            best = min(best, r.fun)
    return best


ms = {k: least_for_view(v) for k, v in views.items()}
actual = (w[:, None] * np.tile(P[0], (3, 1))).ravel()                    # an actor that sees nothing, acting as in 0
M_act, _ = min_kl(lambda a: kl(actual, a), 3 * nX, Gc.ravel()[None, :], np.array([bc]),
                  np.kron(np.eye(3), np.ones(nX)), w, starts=16)
print(f"  least misalignment: full view {ms['full']:.5f}; merging conditions 1 and 2 {ms['merges 1 and 2']:.5f}; "
      f"seeing nothing {ms['sees nothing']:.5f}")
print(f"  an actor that sees nothing: misalignment {M_act:.5f} = {ms['full']:.5f} + "
      f"{ms['merges 1 and 2'] - ms['full']:.5f} + {ms['sees nothing'] - ms['merges 1 and 2']:.5f} + "
      f"{M_act - ms['sees nothing']:.5f} (FA1: every term non-negative)")

print("\nTG2: two targets in tension, pursued one at a time, against 'no worse on any target'")
q = np.ones(4) / 4
G1, G2 = np.array([0., 1., 2., 3.]), np.array([3., 2., 0., 1.])
cov = float(q @ (G1 * G2) - (q @ G1) * (q @ G2))
for t in (0.25, 0.5, 1.0):
    a = q * np.exp(t * G1); a /= a.sum()
    print(f"  pursuit of G1 at intensity {t}: E[G1] {a @ G1:.4f} (q: {q @ G1:.4f}), E[G2] {a @ G2:.4f} "
          f"(q: {q @ G2:.4f})")
print(f"  covariance of G1 and G2 under q: {cov:.4f}")
# TG2(iv): v13's misalignment against the pursuits of the cone equals the departure beyond the credit set
worst = 0.0
for inst in range(30):
    qq = rng.dirichlet(np.ones(5) * 2)
    H1, H2 = rng.normal(size=5), rng.normal(size=5)
    ph = rng.dirichlet(np.ones(5))

    def tilt(t):
        a = qq * np.exp(t[0] * H1 + t[1] * H2); return a / a.sum()
    best = np.inf
    for s in range(6):
        r = minimize(lambda t: kl(ph, tilt(np.abs(t))), rng.uniform(0, 2, 2), method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 5000})
        best = min(best, r.fun)
    Aub = -np.vstack([H1, H2]); bub = -np.array([ph @ H1, ph @ H2])
    least, _ = min_kl(lambda a: kl(a, qq), 5, Aub, bub)
    worst = max(worst, abs(best - (kl(ph, qq) - least)))
print(f"  [P53](iv) as TG2(iv): misalignment against the pursuits of a two-target cone equals the departure beyond "
      f"'no worse than the actor on either target', within {worst:.1e} on 30 instances")

print("\nSN1: the most favourable acceptable behaviour's probability of the record's counts, against e^{-nM}")
n_out = 4
p = np.array([0.4, 0.3, 0.2, 0.1])
G, b = np.array([[0., 1., 2., 3.]]), np.array([0.7])
for n in (20, 100, 500):
    counts = np.round(p * n).astype(int); counts[0] += n - counts.sum()
    s = counts / n
    M, astar = min_kl(lambda a: kl(s, a), n_out, G, b)
    logmult = math.lgamma(n + 1) - sum(math.lgamma(c + 1) for c in counts)
    logprob = logmult + sum(c * math.log(astar[i]) for i, c in enumerate(counts) if c > 0)
    kn = math.comb(n + n_out - 1, n_out - 1)
    print(f"  n {n}: log sup probability {logprob:.3f}; -nM {-n * M:.3f}; -nM - log k_n {-n * M - math.log(kn):.3f}")
# a set that is not convex: two behaviours; Sanov's rate against the set, the best bet against its hull
a1, a2 = np.array([0.7, 0.1, 0.1, 0.1]), np.array([0.1, 0.1, 0.1, 0.7])
pm = 0.5 * (a1 + a2)
hull = 0.0                                                               # pm is a mixture of a1 and a2
print(f"  two acceptable behaviours, an actor at their midpoint: Sanov's rate against the pair "
      f"{min(kl(pm, a1), kl(pm, a2)):.4f}; the best bet's growth, against their hull, {hull:.4f}")

print("\nVK6: a pooled rate limit with the conditions' frequencies fixed")


def v_of(theta, u):
    return ((theta + 1) - math.sqrt((theta + 1) ** 2 - 4 * theta * u)) / (2 * theta)


def vk6(u, w, eps):
    if w @ u <= eps:
        return 0.0
    th = brentq(lambda t: sum(wc * v_of(t, uc) for wc, uc in zip(w, u)) - eps, 1e-12, 1e12)
    return sum(wc * klb(uc, v_of(th, uc)) for wc, uc in zip(w, u))


worst, gaps = 0.0, []
for inst in range(40):
    k = rng.integers(2, 5)
    w = rng.dirichlet(np.ones(k)); u = rng.uniform(0, 1, k); u[rng.integers(k)] = rng.choice([0.0, 1.0, u[0]])
    eps = rng.uniform(0.02, 0.9) * (w @ u) if w @ u > 0 else 0.1
    # numerical: minimize sum w kl(u_c || v_c) subject to sum w v <= eps
    r = minimize(lambda v: sum(wc * klb(uc, vc) for wc, uc, vc in zip(w, u, v)), np.full(k, eps),
                 method="SLSQP", bounds=[(1e-12, 1 - 1e-12)] * k,
                 constraints=[{"type": "ineq", "fun": lambda v: eps - w @ v}], options={"ftol": 1e-15, "maxiter": 3000})
    worst = max(worst, abs(r.fun - vk6(u, w, eps)))
    gaps.append(vk6(u, w, eps) - klb(w @ u, eps))
print(f"  closed form against numerical minimization: within {worst:.1e} on 40 instances; the pooled formula of VK2 "
      f"is below it by {min(gaps):.1e} to {max(gaps):.4f}")
w_bot = np.array([0.7, 0.3])
# the support bot's wrong-answer rates per condition, recomputed from probes/slides/support_bot.py's model
open_W = 0.97 * 0.03
acc_W = 0.8 * (0.2 * 0.996) + 0.2 * (0.97 * 1.0)
print(f"  the support bot (probes/slides): wrong answers per condition {open_W:.4f}, {acc_W:.4f}; pooled "
      f"{0.7 * open_W + 0.3 * acc_W:.4f}; VK6 {vk6(np.array([open_W, acc_W]), w_bot, 0.05):.5f}; "
      f"VK2's pooled formula {klb(0.7 * open_W + 0.3 * acc_W, 0.05):.5f}")

print("\nVK7: how misalignment moves with the budget")
worst_d, worst_ineq = 0.0, 0.0
for inst in range(30):
    n = 5
    p = rng.dirichlet(np.ones(n))
    g = rng.normal(size=n)
    Ep = p @ g
    b = rng.uniform(g.min() + 0.2 * (Ep - g.min()), Ep - 0.05 * (Ep - g.min()))

    def M_of(bb):
        lam_max = 1 / (bb - g.min())
        f = lambda lam: -np.sum(p * np.log(np.maximum(1 + lam * (g - bb), 1e-300)))
        r = minimize_scalar(f, bounds=(0, lam_max), method="bounded", options={"xatol": 1e-13})
        return -r.fun, r.x
    M0, lam = M_of(b)
    d = 1e-5
    deriv = (M_of(b + d)[0] - M_of(b - d)[0]) / (2 * d)
    worst_d = max(worst_d, abs(deriv + lam))
    for bp in np.linspace(g.min() + 1e-3, Ep + 0.5, 25):
        worst_ineq = min(worst_ineq, M_of(bp)[0] - (M0 - math.log(1 + lam * (bp - b))))
print(f"  the derivative of M in the budget against minus the best stake: within {worst_d:.1e} on 30 instances")
print(f"  M(b') - (M(b) - log(1 + λ*(b' - b))) on a grid of b': least value {worst_ineq:.1e} (non-negative up to "
      f"tolerance)")
