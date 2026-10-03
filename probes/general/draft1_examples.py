"""The examples cited in CORE-GENERAL.md draft 1 (GD3, GD5, section 12), reproduced. Exploratory, not checks."""
import numpy as np
from math import lgamma, log, sqrt, pi
from scipy.stats import norm
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad

kl = lambda p, r: float(np.sum(p[p > 0] * np.log(p[p > 0] / r[p > 0])))
tilt = lambda r, g: r * np.exp(g - g.max()) / np.sum(r * np.exp(g - g.max()))

# 1. [P15]'s unavoidable part as a large-deviation rate: exact multinomial sums on three outcomes
p0 = np.array([0.5, 0.3, 0.2]); f = np.array([0.0, 1.0, 2.0]); a = 1.1
pstar = tilt(p0, brentq(lambda th: tilt(p0, th * f) @ f - a, 0, 50) * f)
print(f"1. I-projection {pstar.round(4)}, KL(p*||p0) = {kl(pstar, p0):.4f}")
for n in (50, 200, 800):
    logs, joint = [], np.zeros(3)
    for k1 in range(n + 1):
        for k2 in range(n + 1 - k1):
            k0 = n - k1 - k2
            if k1 + 2 * k2 < a * n: continue
            lp = (lgamma(n + 1) - lgamma(k0 + 1) - lgamma(k1 + 1) - lgamma(k2 + 1)
                  + k0 * log(p0[0]) + k1 * log(p0[1]) + k2 * log(p0[2]))
            logs.append(lp); joint += np.exp(lp) * np.array([k0, k1, k2]) / n
    L = np.logaddexp.reduce(logs)
    print(f"   n={n}: rate {-L / n:.3f}; law of one draw given the event {(joint / np.exp(L)).round(4)}")

# 2. The on-target controller: q = N(0,1), F = -x^2, pursuit N(0, 1/(1+2t)); a deterministic actor at x0
def binned(x0, w, offset):
    lo = np.floor((x0 - offset) / w) * w + offset
    r = minimize_scalar(lambda s: -norm.logcdf(0) * 0 - np.log(max(norm.cdf(lo + w, scale=np.exp(s)) - norm.cdf(lo, scale=np.exp(s)), 1e-300)),
                        bounds=(-40, 0), method="bounded")
    return r.fun
for x0 in (0.0, 1e-3):
    print(f"2. x0={x0:g}: " + "; ".join(f"w={w:g}: centred {binned(x0, w, -w / 2):.2f}, edge {binned(x0, w, 0.0):.2f}"
                                       for w in (1e-2, 1e-4, 1e-6)))

# 3. Best-of-n: an evaluator without atoms against five tied levels
for n in (2, 4, 16):
    cont = quad(lambda u: n * u ** (n - 1) * np.log(n * u ** (n - 1)), 0, 1)[0]
    cdf = np.cumsum(np.full(5, 0.2)); bon = cdf ** n - np.concatenate([[0], cdf[:-1]]) ** n
    print(f"3. n={n}: {cont:.6f} (formula {log(n) - (n - 1) / n:.6f}); five tied levels {kl(bon, np.full(5, 0.2)):.6f}")

# 4. A ray that stops: default density proportional to e^{-x}/(1+x)^3 on x >= 0, F = x
d = lambda x, t: np.exp(-(1 - t) * x) / (1 + x) ** 3
I = lambda g, t: sum(quad(lambda x: g(x) * d(x, t), lo, hi, limit=400)[0] for lo, hi in ((0, 10), (10, 1e3), (1e3, np.inf)))
print("4. average of the ray: " + ", ".join(f"t={t}: {I(lambda x: x, t) / I(lambda x: 1.0, t):.3f}" for t in (0, 0.5, 0.9, 0.99, 0.999, 1.0)))
print("   divergence of an exponential behaviour of mean 2 to the ray, up to a constant: "
      + ", ".join(f"t={t}: {-2 * t + log(I(lambda x: 1.0, t)):.4f}" for t in (0.5, 0.9, 0.99, 1.0)))

# 5. Past the end of the ray: half a nat more departure, the extra probability placed near L
c = 1 / sum(quad(lambda x: np.exp(-x) / (1 + x) ** 3, lo, hi)[0] for lo, hi in ((0, 10), (10, np.inf)))
g1 = lambda x: 2 / (1 + x) ** 3; logq = lambda x: log(c) - x - 3 * np.log1p(x); Dmax = 1 + log(2 / c)
out = []
for L in (10, 100, 1000, 10000):
    norm_ = quad(lambda s: np.exp(-s) / (1 + L + s) ** 3, 0, 1)[0]
    h = lambda x: np.exp(-(x - L)) / (1 + x) ** 3 / norm_
    G = quad(g1, L, L + 1)[0]
    off = lambda e: (1 - e) * (log(1 - e) * (1 - G) + (1 + log(2 / c)) - quad(lambda x: g1(x) * (x + log(2 / c)), L, L + 1)[0])
    cell = lambda e: quad(lambda x: ((1 - e) * g1(x) + e * h(x)) * (np.log((1 - e) * g1(x) + e * h(x)) - logq(x)), L, L + 1)[0]
    eps = brentq(lambda e: off(e) + cell(e) - Dmax - 0.5, 1e-12, 0.5)
    out.append(f"L={L}: {eps * (quad(lambda x: x * h(x), L, L + 1)[0] - 1):.3f}")
print(f"5. D_max = {Dmax:.3f}; half a nat more buys " + ", ".join(out) + " (bound 0.5)")

# 6. Closure is necessary: densities (1 + sin(kx)/2)/(2 pi) on a circle against the uniform behaviour
def cells(k, m):
    e = np.linspace(0, 2 * pi, m + 1)
    pk = (np.diff(e) + (np.cos(k * e[:-1]) - np.cos(k * e[1:])) / (2 * k)) / (2 * pi)
    return kl(np.full(m, 1 / m), pk)
print(f"6. KL(u||p_k) = {-log((1 + sqrt(0.75)) / 2):.3f} for every k; at 100 cells: "
      + ", ".join(f"k={k}: {cells(k, 100):.1e}" for k in (7, 77, 7777)))

# 7. Masking without a gap: two actors with densities 1 + a(x - 1/2) on [0, 1], incentive u(x) = x
a1, a2 = 1.5, -1.0
lim = ((a1 / (1 + a1 / 2)) - (a2 / (1 + a2 / 2))) ** 2 / 2
def masked_kl(k):
    ys = np.linspace(0, 1, 200001)
    def loglaw(a):                                      # in log space: e^{k(y-1)} underflows far from y = 1
        lw = np.log1p(a * (ys - 0.5)) + k * (ys - 1)
        return lw - np.log(np.trapezoid(np.exp(lw - lw.max()), ys)) - lw.max()
    lP, lQ = loglaw(a1), loglaw(a2)
    return np.trapezoid(np.exp(lP) * (lP - lQ), ys)
print(f"7. limit {lim:.3f}; κ²·KL: " + ", ".join(f"κ={k}: {k * k * masked_kl(k):.3f}" for k in (10, 30, 100, 300, 1000)))
