"""v14/factorization.md: (1) v13's [P15](v) "unavoidable" part against the least misalignment of any feasible
behaviour, under the standard specification with one fixed average; (2) FA2, K = E + R, with the ordinal specification and one fixed
average, the joint minimum found by alternating minimization and checked by an independent search; (3) FA3 on nested
linear sets. Probed, not tested. Run from the repository's root: python3 probes/v14/factorization.py   (a few minutes)
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq, minimize
rng = np.random.default_rng(11)
def kl(p, a):
    m = p > 0
    return np.inf if np.any(a[m] <= 0) else float(np.sum(p[m] * np.log(p[m] / a[m])))
def tilt(r, H):
    w = r * np.exp(H - H.max()); return w / w.sum()
def iproj(r, f, a1):
    """I-projection of r onto {p: E_p f = a1}: tilt(r, θ f)."""
    th = brentq(lambda th: tilt(r, th * f) @ f - a1, -200, 200)
    return tilt(r, th * f)
# (1) P15(v): v13's "unavoidable" KL(p*°‖p°) against the least misalignment over the feasible set
over, worst, n_ok = 0, 0.0, 0
for _ in range(200):
    n = 5; q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); f1 = rng.normal(size=n)
    ray = lambda t: tilt(q, t * F)
    ph = rng.dirichlet(np.ones(n)); a1 = ph @ f1
    if ph @ F <= q @ F:
        continue
    t0 = minimize_scalar(lambda t: kl(ph, ray(t)), bounds=(0, 60), method="bounded", options={"xatol": 1e-12}).x
    pstar = iproj(ray(t0), f1, a1); unav13 = kl(pstar, ray(t0))
    best = minimize_scalar(lambda t: kl(iproj(ray(t), f1, a1), ray(t)), bounds=(0, 60), method="bounded",
                           options={"xatol": 1e-12}).fun
    best = min(best, kl(iproj(ray(0.0), f1, a1), ray(0.0)))
    n_ok += 1; over += unav13 > best + 1e-9; worst = max(worst, unav13 - best)
print(f"(1) {n_ok} instances: v13's unavoidable part exceeds the least misalignment any feasible behaviour has "
      f"in {over}; by up to {worst:.4f}")
# (2) convex A (ordinal cone, F = 0..n-1), linear feasible set: M + R = KL(p̂‖f°) + KL(f°‖a°), so K = E + R ≥ E
def isotonic(y, w):
    out = []
    for s, ww in zip(y * w, w):
        out.append([s, ww, 1])
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            s2, w2, k2 = out.pop(); out[-1][0] += s2; out[-1][1] += w2; out[-1][2] += k2
    return np.concatenate([[s / ww] * k for s, ww, k in out])
rev = lambda p, q: q * isotonic(p / q, q)            # nearest behaviour in the ordinal cone
worst_id, worst_min, cnt = 0.0, 0.0, 0
for _ in range(200):
    n = 5; q = rng.dirichlet(np.ones(n)); f1 = rng.normal(size=n)
    ph = rng.dirichlet(np.ones(n)); a1 = ph @ f1
    a = q.copy()
    for _ in range(3000):                             # alternating minimization over 𝓕 × A
        f = iproj(a, f1, a1); a = rev(f, q)
    fo, ao = iproj(a, f1, a1), a
    M = kl(ph, rev(ph, q)); unav = kl(fo, ao); R = kl(ph, ao) - M
    K, E = kl(ph, fo), M - unav
    worst_id = max(worst_id, abs(K - (E + R)))
    # independent check of the least misalignment over 𝓕: minimize M over a parametrization of 𝓕
    mn = np.inf
    for _ in range(8):
        r = minimize(lambda g: kl(np.maximum(g, 1e-300), rev(np.maximum(g, 1e-300), q)), rng.dirichlet(np.ones(n)),
                     method="SLSQP", bounds=[(1e-12, 1)] * n,
                     constraints=[{"type": "eq", "fun": lambda g: g.sum() - 1},
                                  {"type": "eq", "fun": lambda g: g @ f1 - a1}],
                     options={"ftol": 1e-15, "maxiter": 3000})
        if r.success:
            mn = min(mn, r.fun)
    worst_min = max(worst_min, unav - mn); cnt += 1
print(f"(2) {cnt} instances: largest |K − (E + R)| {worst_id:.1e}; "
      f"alternating minimum above an independent search by at most {worst_min:.1e}")
# (3) nested linear sets with a fixed target: KL(f2‖a) = KL(f2‖f1) + KL(f1‖a), f_j the I-projections of a
worst = 0.0
for _ in range(200):
    n = 6; a = rng.dirichlet(np.ones(n)); g1, g2 = rng.normal(size=n), rng.normal(size=n)
    base = rng.dirichlet(np.ones(n)); c1, c2 = base @ g1, base @ g2
    f1 = iproj(a, g1, c1)
    # projection onto {E g1 = c1, E g2 = c2}: tilt(a, θ1 g1 + θ2 g2), solved numerically
    obj = lambda th: np.log(a @ np.exp(th[0] * g1 + th[1] * g2)) - th[0] * c1 - th[1] * c2
    th = minimize(obj, np.zeros(2), method="BFGS", options={"gtol": 1e-12}).x
    f2 = tilt(a, th[0] * g1 + th[1] * g2)
    worst = max(worst, abs(kl(f2, a) - kl(f2, f1) - kl(f1, a)))
print(f"(3) nested linear sets, 200 instances: largest |KL(f2‖a) − KL(f2‖f1) − KL(f1‖a)| {worst:.1e}")
