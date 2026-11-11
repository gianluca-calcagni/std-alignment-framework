"""Does one betting strategy, fixed before the record, reach the plug-in misalignment on every record? (NOTES.md §39,
H69, Q81). Exploratory, not a check: it tests on 25 records an inequality that §39 proves.
Usage: python3 probes/review/q81_universal_bet.py        (about a minute; a grid of 240³ points)

The claim tested. X finite with d outcomes, the world's part trivial, A a polytope of acceptable behaviours with
vertices v_1..v_k, every outcome allowed by one of them. The bets against A (mvp/CORE.md, D6) are the convex body
B = {h ≥ 0 : ⟨v_j, h⟩ ≤ 1 for every j}. The uniform mixture over B, W_n = (1/vol B)·∫_B Π_i h(x_i) dh, is a mixture of
wealths, so R4 gives it its level whatever the dependence. For every sequence x_1..x_n, with shares s_n,
    n·M_A(s_n) − d·log(n + 1) − 1  ≤  log W_n  ≤  n·M_A(s_n).
The right side: every h in B has Σ_i log h(x_i) = n·E_{s_n}[log h] ≤ n·M_A(s_n) (R2(i) at p = s_n). The left: with h*
the best bet in hindsight and γ = 1/(n + 1), the set (1 − γ)·h* + γ·B lies in B, has the share γ^d of its volume, and
each of its members is at least (1 − γ)·h* everywhere, so its wealth is at least (1 − γ)^n ≥ 1/e times the best one.
The argument is the one remembered as Blum and Kalai's for Cover's universal portfolios; neither text was read.

The instance: X = {0, 1, 2}, A = {a : a(2) ≤ 0.10, E_a[g] ≤ 0.5}, g = (0, 1, 3). Five kinds of record, at
n = 30 to 3,000: independent draws outside A; independent draws from a vertex of A; a sticky Markov chain; fixed
blocks; every breach at the end. Seed 11. The integral is a midpoint sum on a grid, so the wealth carries the grid's
error, largest where the best bet sits on the body's boundary.
"""
import itertools
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(11)
d = 3
G = np.array([[0.0, 0.0, 1.0], [0.0, 1.0, 3.0]])
b = np.array([0.10, 0.5])


def vertices():
    rows = [(-np.eye(d)[i], 0.0) for i in range(d)] + [(G[j], b[j]) for j in range(len(b))]
    out = []
    for i, j in itertools.combinations(range(len(rows)), 2):
        mat = np.vstack([np.ones(d), rows[i][0], rows[j][0]])
        if abs(np.linalg.det(mat)) < 1e-12:
            continue
        a = np.linalg.solve(mat, np.array([1.0, rows[i][1], rows[j][1]]))
        if (a >= -1e-12).all() and (G @ a <= b + 1e-12).all() and not any(np.allclose(a, o, atol=1e-10) for o in out):
            out.append(np.clip(a, 0, None))
    return np.array(out)


V = vertices()
hmax = 1.0 / V.max(axis=0)                                                           # the box that contains B
N = 240
axes = [np.linspace(0, hmax[i], N + 1)[1:] - hmax[i] / (2 * N) for i in range(d)]
H = np.stack(np.meshgrid(*axes, indexing="ij"), -1).reshape(-1, d)
H = H[(H @ V.T <= 1.0).all(axis=1)]
logH = np.log(H)


def misalignment(s):
    """inf KL(s‖a) over A, by a convex solve from several starts; a probe's solver, not the library's."""
    S = s > 0
    f = lambda a: float(np.sum(s[S] * np.log(s[S] / np.maximum(a[S], 1e-300))))      # noqa: E731
    cons = [{"type": "eq", "fun": lambda a: a.sum() - 1}, {"type": "ineq", "fun": lambda a: b - G @ a}]
    best = np.inf
    for a0 in list(V) + [V.mean(axis=0)]:
        r = minimize(f, 0.9 * a0 + 0.1 * V.mean(axis=0), bounds=[(1e-12, 1)] * d, constraints=cons, method="SLSQP",
                     options={"ftol": 1e-13, "maxiter": 500})
        if r.success and (G @ r.x <= b + 1e-8).all():
            best = min(best, r.fun)
    return best


def log_wealth(counts):
    z = logH @ counts
    return z.max() + np.log(np.mean(np.exp(z - z.max())))


def records(n):
    yield "independent, outside A", rng.choice(d, n, p=[0.45, 0.30, 0.25])
    yield "independent, a vertex of A", rng.choice(d, n, p=V[np.argmax(V[:, 2])])
    T = np.full((d, d), 0.05) + 0.85 * np.eye(d)
    x = [0]
    for _ in range(n - 1):
        x.append(rng.choice(d, p=T[x[-1]]))
    yield "a sticky Markov chain", np.array(x)
    yield "fixed blocks 0…0 1…1 2…2", np.repeat([0, 1, 2], n // 3 + 1)[:n]
    yield "every breach at the end", np.concatenate([np.zeros(n - n // 4, int), np.full(n // 4, 2)])


if __name__ == "__main__":
    print("vertices of A:", np.round(V, 4).tolist(), f"\ngrid points inside B: {len(H)}\n")
    print(f"{'record':28s} {'n':>5s} {'n·M(s_n)':>9s} {'log W_n':>9s} {'gap':>7s} {'d·log(n+1)+1':>14s}")
    worst, least = 0.0, np.inf
    for n in (30, 100, 300, 1000, 3000):
        for name, x in records(n):
            counts = np.bincount(x, minlength=d).astype(float)
            nm, lw, bound = n * misalignment(counts / n), log_wealth(counts), d * np.log(n + 1) + 1
            worst, least = max(worst, (nm - lw) / bound), min(least, nm - lw)
            print(f"{name:28s} {n:5d} {nm:9.3f} {lw:9.3f} {nm - lw:7.3f} {bound:14.3f}")
    print(f"\nleast gap {least:.3f} (the claim asks ≥ 0); largest gap as a share of the bound {worst:.3f} (asks ≤ 1)")
