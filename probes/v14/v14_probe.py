"""The numbers of v14/: each result of evidence.md, constraints.md and order.md computed on random or chosen
instances. Probed, not tested: the results are proved in their files, and no prediction was registered. Numerical
minimizations (SLSQP from several starts) stand in for the exact minimum where no closed form exists.
Run from the repository's root: python3 probes/v14/v14_probe.py   (a few minutes)
"""
from math import comb, log
import numpy as np
from scipy.optimize import minimize, minimize_scalar, brentq

rng = np.random.default_rng(20261015)


def kl(p, a):
    m = p > 0
    if np.any(a[m] <= 0):
        return np.inf
    return float(np.sum(p[m] * np.log(p[m] / a[m])))


def kl2(x, y):
    return kl(np.array([x, 1 - x]), np.array([y, 1 - y]))


def isotonic(y, w):
    """Weighted least-squares non-decreasing fit (pool adjacent violators), as in checks/test_misalignment.py."""
    out = []
    for s, ww in zip(y * w, w):
        out.append([s, ww, 1])
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            s2, w2, k2 = out.pop(); out[-1][0] += s2; out[-1][1] += w2; out[-1][2] += k2
    return np.concatenate([[s / ww] * k for s, ww, k in out])


def nearest_cone(p, q):
    """The nearest behaviour to p in v13's ordinal specification, for F with distinct levels in index order ([P36])."""
    return q * isotonic(p / q, q)


def min_kl_linear(p, A, b, starts=20):
    """inf KL(p‖a) over behaviours a with A·a ≤ b, numerically."""
    n, best = len(p), np.inf
    for _ in range(starts):
        r = minimize(lambda a: kl(p, np.maximum(a, 1e-300)), rng.dirichlet(np.ones(n)), method="SLSQP",
                     bounds=[(1e-12, 1)] * n,
                     constraints=[{"type": "eq", "fun": lambda a: a.sum() - 1},
                                  {"type": "ineq", "fun": lambda a: b - A @ a}],
                     options={"ftol": 1e-14, "maxiter": 2000})
        if r.success and np.all(A @ r.x <= b + 1e-8):
            best = min(best, r.fun)
    return best


def tilt(q, H):
    w = q * np.exp(H - H.max())
    return w / w.sum()


def section(name):
    print(f"\n{name}")


section("VE1  the best bet against a convex set: h* = p/a* is a bet, and E_p[log h*] = M")
worst_bet, worst_val = -np.inf, 0.0
for _ in range(300):
    n = int(rng.integers(3, 8))
    q, p = rng.dirichlet(np.ones(n)), rng.dirichlet(np.ones(n))
    a = nearest_cone(p, q); h = p / a
    for f in range(n):                                   # the extreme points of the ordinal cone: q given F ≥ f
        e = np.where(np.arange(n) >= f, q, 0.0); e /= e.sum()
        worst_bet = max(worst_bet, e @ h - 1)
    worst_val = max(worst_val, abs(p @ np.log(h) - kl(p, a)))
print(f"  ordinal cone, 300 instances: largest E_a[h*] − 1 over its extreme points {worst_bet:.1e}; "
      f"|E_p log h* − M| at most {worst_val:.1e}")

section("VE2  records hold an actor to the convex hull")
n_out = 4; q4 = np.full(n_out, 0.25); F4 = np.arange(n_out, dtype=float)
ray = lambda t: tilt(q4, t * F4)
mixture = 0.5 * ray(0.0) + 0.5 * ray(3.0)
r = minimize_scalar(lambda t: kl(mixture, ray(t)), bounds=(0, 30), method="bounded", options={"xatol": 1e-12})
print(f"  half intensity 0, half intensity 3: misalignment against the ray {r.fun:.4f} (t = {r.x:.3f}); "
      f"against the ordinal cone {kl(mixture, nearest_cone(mixture, q4)):.1e}")


def bet_from(counts):
    smooth = (counts + 0.5) / (counts + 0.5).sum()
    return smooth / nearest_cone(smooth, q4)


def accused(step, n=400, records=2000, alpha=0.05, seed=1):
    """Shares of records accused: a bet against the ordinal cone refitted before each decision (VE3); [P55]'s count
    test against the ordinal cone; and against the ray."""
    gen = np.random.default_rng(seed)
    thr = log(comb(n + n_out - 1, n_out - 1) / alpha)
    hits = np.zeros(3)
    for _ in range(records):
        counts, wealth, hit, last = np.zeros(n_out), 1.0, False, None
        for _ in range(n):
            h = bet_from(counts)
            x = gen.choice(n_out, p=step(last, gen))
            wealth *= h[x]; counts[x] += 1; last = x
            hit = hit or wealth >= 1 / alpha
        s = counts / n
        m_ray = minimize_scalar(lambda t: kl(s, ray(t)), bounds=(0, 30), method="bounded").fun
        hits += [hit, n * kl(s, nearest_cone(s, q4)) >= thr, n * m_ray >= thr]
    return hits / records


cases = [("each decision intensity 0 or 3, at random", lambda last, g: ray(0.0) if g.random() < 0.5 else ray(3.0), 2000),
         ("intensity 8 after the best outcome, else 0", lambda last, g: ray(8.0) if last == 3 else ray(0.0), 2000),
         ("pursues −F at intensity 1", lambda last, g: ray(-1.0), 300)]
print("  share of records of 400 decisions accused at level 0.05: bet vs cone, count test vs cone, count test vs ray")
for name, step, records in cases:
    a, b, c = accused(step, records=records)
    print(f"    {name:45s} {a:.4f}  {b:.4f}  {c:.4f}   ({records} records)")

section("VK2  rate limit a(C) ≤ ε: M = kl(p(C)‖ε) when p(C) > ε")
worst = 0.0
for _ in range(40):
    n = int(rng.integers(3, 7)); p = rng.dirichlet(np.ones(n)); C = rng.random(n) < 0.5
    if not C.any() or C.all():
        continue
    eps = rng.uniform(0, p[C].sum())
    worst = max(worst, abs(min_kl_linear(p, C.astype(float)[None, :], np.array([eps])) - kl2(p[C].sum(), eps)))
print(f"  largest |numerical minimum − kl(p(C)‖ε)|: {worst:.1e}")

section("VK3  budget E_a[g] ≤ b: M = max over 0 ≤ λ ≤ 1/(b − min g) of E_p[log(1 + λ(g − b))]")


def budget(p, g, b):
    if p @ g <= b:
        return 0.0, p.copy()
    lam_max, s = 1 / (b - g.min()), p > 0
    r = minimize_scalar(lambda lam: -np.sum(p[s] * np.log(np.maximum(1 + lam * (g[s] - b), 1e-300))),
                        bounds=(0, lam_max), method="bounded", options={"xatol": 1e-15})
    h = 1 + r.x * (g - b)
    a = np.where(s, p / np.where(h > 0, h, 1), 0.0)
    a[np.argmin(g)] += max(0.0, 1 - a.sum())
    return -r.fun, a


worst, worst_a, edge = 0.0, 0.0, 0
for _ in range(80):
    n = int(rng.integers(3, 7)); p = rng.dirichlet(np.ones(n)); g = rng.normal(size=n)
    if rng.random() < 0.4:
        p[0] = 0; p /= p.sum(); g[0] = g.min() - 3            # a cheap outcome the actor never uses
    if p @ g <= g.min() + 1e-3:
        continue
    b = rng.uniform(g.min() + 1e-3, p @ g)
    m, a = budget(p, g, b)
    worst = max(worst, abs(m - min_kl_linear(p, g[None, :], np.array([b]))))
    worst_a = max(worst_a, abs(kl(p, a) - m), max(0.0, a @ g - b), abs(a.sum() - 1))
    edge += bool(p[np.argmin(g)] == 0 and a[np.argmin(g)] > 1e-9)
print(f"  largest |dual − numerical minimum| {worst:.1e}; the constructed a* is a behaviour within the budget and "
      f"attains it within {worst_a:.1e}; {edge} instances at the edge λ* = 1/(b − min g)")

section("VK4  several budgets: the best affine bet against the numerical minimum")
worst = 0.0
for _ in range(30):
    n = int(rng.integers(4, 7)); p = rng.dirichlet(np.ones(n)); G = rng.normal(size=(2, n))
    b = np.array([rng.uniform(G[j].min() + 0.2, max(G[j].min() + 0.3, p @ G[j])) for j in range(2)])
    num = min_kl_linear(p, G, b)
    if not np.isfinite(num):
        continue

    def neg(lam):
        h = 1 + lam @ (G - b[:, None])
        return 1e9 if np.any(h < 0) or np.any(lam < 0) else -np.sum(p * np.log(np.maximum(h, 1e-300)))
    best = min(minimize(neg, rng.uniform(0, 0.1, 2), method="Nelder-Mead",
                        options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000}).fun for _ in range(10))
    worst = max(worst, abs(-best - num))
print(f"  two budgets, 30 instances: largest |best affine bet − numerical minimum| {worst:.1e}")

section("VK5  the constrained optimizer is tilt(q, t·(F − ν·g)), and ν is the budget's shadow price")
worst, worst_price = 0.0, 0.0
for _ in range(30):
    n = int(rng.integers(3, 7)); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); g = rng.normal(size=n)
    t = rng.uniform(0.5, 4)
    opt = lambda nu: tilt(q, t * (F - nu * g))
    if opt(0) @ g <= g.min() + 0.1:
        continue
    b = rng.uniform(g.min() + 0.05, opt(0) @ g)
    nu_of = lambda bb: brentq(lambda v: opt(v) @ g - bb, 0, 200)
    nu = nu_of(b)
    value = lambda a: a @ F - kl(a, q) / t
    best = None
    for _ in range(10):
        r = minimize(lambda a: -value(np.maximum(a, 1e-300)), rng.dirichlet(np.ones(n)), method="SLSQP",
                     bounds=[(1e-12, 1)] * n,
                     constraints=[{"type": "eq", "fun": lambda a: a.sum() - 1},
                                  {"type": "ineq", "fun": lambda a: b - a @ g}],
                     options={"ftol": 1e-15, "maxiter": 3000})
        if r.success and (best is None or r.fun < best.fun):
            best = r
    worst = max(worst, abs(-best.fun - value(opt(nu))))
    d = 1e-5
    slope = (value(opt(nu_of(b + d))) - value(opt(nu_of(b - d)))) / (2 * d)
    worst_price = max(worst_price, abs(slope - nu))
print(f"  largest |numerical optimum − value of the tilt| {worst:.1e}; largest |d value/d b − ν| {worst_price:.1e}")
q5 = rng.dirichlet(np.ones(5)); F5 = rng.normal(size=5); C5 = np.array([0, 0, 1, 0, 1.0])
allowed = np.where(C5 == 0, q5 * np.exp(2 * F5), 0); allowed /= allowed.sum()
print(f"  forbidden set: total variation between tilt(q, 2(F − 40·1_C)) and the pursuit on the allowed outcomes "
      f"{0.5 * np.abs(tilt(q5, 2 * (F5 - 40 * C5)) - allowed).sum():.1e}")

section("VO3  three verdicts: a decoder always at level 8 of 10 levels, uniform reference")
ref = np.full(10, 0.1); dec = np.zeros(10); dec[8] = 1
upper = lambda a: np.array([a[f:].sum() for f in range(10)])
print(f"  better for every reading: {bool(np.all(upper(dec) >= upper(ref) - 1e-12))}; "
      f"worse for every reading: {bool(np.all(upper(dec) <= upper(ref) + 1e-12))}; "
      f"its rank's average {dec @ np.arange(10) / 9:.3f} against the reference's {ref @ np.arange(10) / 9:.3f}")
