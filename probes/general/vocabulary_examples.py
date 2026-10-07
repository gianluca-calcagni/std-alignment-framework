"""The examples behind the vocabulary of CORE-GENERAL.md section 15: fudging a threshold, rounding readings, a
narrow exploit, acting for the camera. Exploratory, not checks."""
import numpy as np
from math import log, sqrt, erf
from scipy.stats import lognorm, norm

# 1. Fudging a threshold. Waiting times: lognormal, median 150 min, 16% beyond 240 min. The actor pulls breaches up to
#    60 min late to land in the last b minutes before 240. Misalignment under the target as declared is the
#    within-cell departure ([P7](ii)), at a record of bins of width w aligned on the threshold.
s = log(240 / 150) / norm.ppf(0.84); q = lognorm(s, scale=150)
c, R = 240.0, 60.0
moved = q.cdf(c + R) - q.cdf(c)
def M_at(w, b):
    edges = np.concatenate([np.arange(0, c + 600, w), [np.inf]])
    qb = np.diff(q.cdf(edges))
    lo, hi = np.maximum(edges[:-1], c - b), np.minimum(edges[1:], c)
    land = np.clip(hi - lo, 0, None) / b * moved
    gone = np.diff(np.clip(q.cdf(np.clip(edges, c, c + R)) - q.cdf(c), 0, None))
    ph, below = qb + land - gone, edges[1:] <= c
    tot = 0.0
    for cell in (below, ~below):
        P, Q = ph[cell], qb[cell]; k = P > 0
        tot += P[k].sum() * np.sum((P[k] / P[k].sum()) * np.log((P[k] / P[k].sum()) / (Q[k] / Q.sum())))
    return tot
x = np.linspace(0, 3000, 600001); F = q.cdf(x); dx = x[1] - x[0]; pass1 = q.cdf(c) + moved
a, b_ = pass1 / q.cdf(c), (1 - pass1) / q.sf(c)
Ft = np.where(x < c, a * F, pass1 + b_ * (F - q.cdf(c)))
Fg = np.where(x < c, F, np.where(x < c + R, q.cdf(c + R), F))
print(f"1. pass rate {q.cdf(c):.3f} -> {pass1:.3f}; minutes moved per patient: honest tilt {np.sum(np.abs(Ft - F)) * dx:.1f}, "
      f"fudging {np.sum(np.abs(Fg - F)) * dx:.1f}")
for b in (5.0, 1.0, 0.01):
    print(f"   landing in the last {b:g} min: " + ", ".join(f"w={w:g}: {M_at(w, b):.3f}" for w in (20, 10, 5, 1, 0.1, 0.01)))

# 2. Rounding readings: manual readings to 2 mmHg, five end digits, 20% expected to end in 0
for share, where in ((0.328, "New Zealand, manual"), (0.64, "England, IHD patients (baseline assumed 20%)")):
    rest = (1 - share) / 4
    k = share * log(share / 0.2) + 4 * rest * log(rest / 0.2)
    print(f"2. {where}: {share:.1%} zeros -> {k:.3f} nats per reading, about {1 / k:.0f} readings per nat")

# 3. A narrow exploit: a spike of height h on a region of default probability eta = width^d
for h, d in ((1.0, 1), (1.0, 10), (3.0, 10)):
    eta = 1e-3 ** d; tstar = log((1 - eta) / eta) / h
    print(f"3. h={h:g}, d={d}: found at intensity {tstar:.1f}; the 10%-90% switch takes {2 * log(9) / h:.2f} ({2 * log(9) / h / tstar:.1%} of it)")

# 4. Acting for the camera: the view of test-likeness c is N(c, sigma^2); the largest possible change of behaviour
#    between two conditions is the total variation between their views
for sig in (0.05, 0.1, 0.3, 0.5):
    print(f"4. sigma={sig}: deployment vs test at most {erf(1 / (2 * sig) / sqrt(2)):.4f}; "
          f"deployment vs halfway at most {erf(0.5 / (2 * sig) / sqrt(2)):.4f}")
