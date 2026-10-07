"""B4: heavy tails under a KL budget and a chi-squared budget. B5: the alignment plane. B6: a robustness degree."""
import numpy as np
from math import log, sqrt, exp
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import norm

# B4 (a) Pareto(alpha = 3, minimum 1), F = x: a KL budget of 0.1, the extra probability placed on [L, L+1]
al = 3.0; q = lambda x: al / x ** (al + 1); mean = al / (al - 1); var = al / ((al - 1) ** 2 * (al - 2))
for L in (10.0, 1e2, 1e3, 1e4, 1e6):
    qL = L ** -al - (L + 1) ** -al
    mL = quad(lambda x: x * q(x), L, L + 1)[0] / qL
    kl = lambda e: (1 - e) * log(1 - e) * (1 - qL) + ((1 - e) * qL + e) * log((1 - e) + e / qL)
    e = brentq(lambda e: kl(e) - 0.1, 1e-15, 0.9)
    print(f"B4a: L={L:8.0e}: gain in F {e * (mL - mean):8.3f}")
# (b) a chi-squared budget of 0.1: the Cauchy-Schwarz optimum p = q·(1 + c(F - mean)), c = sqrt(B/Var)
c = sqrt(0.1 / var)
chi2 = quad(lambda x: q(x) * (c * (x - mean)) ** 2, 1, np.inf)[0]
gain = quad(lambda x: q(x) * (1 + c * (x - mean)) * x, 1, np.inf)[0] - mean
print(f"B4b: chi-squared budget used {chi2:.6f}; gain {gain:.6f}; sqrt(0.1·Var) = {sqrt(0.1 * var):.6f}; "
      f"positive everywhere: {1 + c * (1 - mean) > 0}")
# (c) independent Exp(1) coordinates, target x, proxy G = x + y, rho = 1/sqrt(2), sd(x) = 1
for B in (0.1, 0.3, 0.5):
    cc = sqrt(B / 2.0)                                                   # Var G = 2
    g_chi = dblquad(lambda y, x: exp(-x - y) * (1 + cc * (x + y - 2)) * x, 0, 60, 0, 60)[0] - 1
    t = brentq(lambda t: 2 * (log(1 - t) - 1 + 1 / (1 - t)) - B, 1e-9, 0.999)     # KL of the pursuit of G
    print(f"B4c: B={B}: chi-squared gain {g_chi:.9f} vs sqrt(B)·rho·sd = {sqrt(B) / sqrt(2):.9f}; "
          f"KL pursuit gain {t / (1 - t):.4f} vs sqrt(2B)·rho·sd = {sqrt(2 * B) / sqrt(2):.4f} (ratio {t / (1 - t) / sqrt(B):.4f})")
t = brentq(lambda t: 2 * (log(1 - t) - 1 + 1 / (1 - t)) - 1.0, 1e-9, 0.999)
print(f"B4c: B=1 (chi-squared infeasible beyond B = 0.5): KL pursuit gain {t / (1 - t):.4f} vs {1.0:.4f}")

# B5 Gaussian default N(0, S), linear target f and proxy g: gain per sqrt(departure), and M = departure·sin^2
rng = np.random.default_rng(5)
worst = 0.0
for _ in range(50):
    A = rng.normal(size=(3, 3)); S = A @ A.T + 0.1 * np.eye(3); f, g = rng.normal(size=3), rng.normal(size=3)
    cos = f @ S @ g / sqrt((f @ S @ f) * (g @ S @ g)); Si = np.linalg.inv(S)
    for t in (0.1, 1.0, 10.0):
        mu = t * S @ g; dep = mu @ Si @ mu / 2
        res = minimize_scalar(lambda s: (mu - s * S @ f) @ Si @ (mu - s * S @ f) / 2, bounds=(0, 1e3), method="bounded",
                              options={"xatol": 1e-14})
        M = min(res.fun, dep)
        want = dep * (1 - cos ** 2) if cos >= 0 else dep
        worst = max(worst, abs(M - want) / dep, abs(t * f @ S @ g / sqrt(dep) - sqrt(2 * f @ S @ f) * cos))
print(f"B5 Gaussian: largest relative error over 150 cases {worst:.1e}  (predicted < 1e-9)")
# exponential product default, target x1, proxy x1 + x2 (as registered); then a mixed default (exploratory)
for t in (0.1, 0.5, 0.9):
    dep = 2 * (log(1 - t) - 1 + 1 / (1 - t)); M = log(1 - t) - 1 + 1 / (1 - t)
    print(f"B5 exponential product, t={t}: M/departure {M / dep:.6f}, sin^2 = 0.5   (registered: departs by >1% at t = 2; t_max = 1)")
for t in (0.05, 0.2, 0.5):
    k1 = log(1 - t) - 1 + 1 / (1 - t); M = t * t / 2       # x1 ~ Exp(1), x2 ~ N(0,1); proxy x1 + x2; target x1
    print(f"B5 exploratory, Exp x Normal, t={t}: M/departure {M / (k1 + M):.4f}, sin^2 = 0.5")

# B6 deterministic aim r inside a threshold, Gaussian noise sigma; intended: pass with probability at least 1 - alpha
alpha = 0.05
def M(r, sig):
    pp = norm.cdf(r / sig)
    if pp >= 1 - alpha: return 0.0
    return pp * log(pp / (1 - alpha)) + (1 - pp) * log((1 - pp) / alpha)
grid = [(r, sg) for r in np.linspace(-1, 1, 41) for sg in (0.1, 0.3, 1.0)]
same = max(abs(M(r, sg) - M(r * 2, sg * 2)) for r, sg in grid)
mono = all(M(r1, 0.3) >= M(r2, 0.3) - 1e-15 for r1, r2 in zip(np.linspace(-1, 1, 200)[:-1], np.linspace(-1, 1, 200)[1:]))
zero = abs(M(0.3 * norm.ppf(1 - alpha), 0.3)) + (M(0.3 * norm.ppf(1 - alpha) - 1e-6, 0.3) > 0)
print(f"B6: depends on r/sigma only (max gap {same:.1e}); non-increasing in r: {mono}; zero from r = sigma·Phi^-1(1-alpha): "
      f"{zero == 1}")
