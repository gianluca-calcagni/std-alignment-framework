"""B1: misalignment against reversible chains is the Jensen-Shannon divergence between forward and backward flux.
B2: entropy production is cycle flux x cycle affinity; at low intensity the flux is affinity / series resistance."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(11)

def chain(U1, U2, t, r1=0.5):
    m1, m2 = U1.shape; n = m1 * m2; P = np.zeros((n, n))
    for a in range(m1):
        for b in range(m2):
            i = a * m2 + b
            w = np.exp(t * (U1[:, b] - U1[:, b].max())); w /= w.sum()
            for a2 in range(m1): P[i, a2 * m2 + b] += r1 * w[a2]
            w = np.exp(t * (U2[a, :] - U2[a, :].max())); w /= w.sum()
            for b2 in range(m2): P[i, a * m2 + b2] += (1 - r1) * w[b2]
    ev, V = np.linalg.eig(P.T); pi = np.real(V[:, np.argmin(abs(ev - 1))]); pi /= pi.sum()
    return P, pi

def ep(P, pi):
    F = pi[:, None] * P; m = F > 0
    return float(np.sum(F[m] * np.log(F[m] / F.T[m])))

def jsd(P, pi):
    F = pi[:, None] * P; M = (F + F.T) / 2; m = F > 0
    return float(np.sum(F[m] * np.log(F[m] / M[m])))

def m_rev(P, pi):
    n = len(pi); edges = [(i, j) for i in range(n) for j in range(i, n) if P[i, j] > 0 or P[j, i] > 0]
    def rate(z):
        W = np.zeros((n, n))
        for (i, j), v in zip(edges, np.exp(z)): W[i, j] = W[j, i] = v
        R = W / W.sum(1, keepdims=True); mask = P > 0
        return float(np.sum((pi[:, None] * P)[mask] * np.log(P[mask] / R[mask])))
    return min((minimize(rate, rng.normal(size=len(edges)), method="BFGS", options={"gtol": 1e-12}) for _ in range(4)),
               key=lambda r: r.fun).fun

print("B1: misalignment against reversible chains, optimized, against the Jensen-Shannon divergence of the fluxes")
pen = np.array([[1.0, -1.0], [-1.0, 1.0]])
worst = 0.0
for t in (0.01, 0.1, 2.0):
    P, pi = chain(pen, -pen, t); a, b = m_rev(P, pi), jsd(P, pi); worst = max(worst, abs(a - b) / b)
    print(f"    matching pennies t={t}: optimum {a:.10e}, JS {b:.10e}, EP {ep(P, pi):.4e}")
for _ in range(10):
    P, pi = chain(rng.normal(size=(3, 3)), rng.normal(size=(3, 3)), 1.0)
    a, b = m_rev(P, pi), jsd(P, pi); worst = max(worst, abs(a - b) / b)
print(f"    largest relative gap over the 13 cases: {worst:.1e}  (predicted < 1e-6)")

print("B2: EP = cycle flux x cycle affinity; low-intensity constant from the edge fluxes")
for t in (0.5, 2.0):
    U1, U2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
    C = (U1[1, 0] - U1[0, 0]) + (U2[1, 1] - U2[1, 0]) + (U1[0, 1] - U1[1, 1]) + (U2[0, 0] - U2[0, 1])
    P, pi = chain(U1, U2, t); F = pi[:, None] * P
    J = F[0, 2] - F[2, 0]                               # flux on the edge (0,0) -> (1,0), player 1 deviating
    print(f"    t={t}: EP {ep(P, pi):.10e}, J·t·C {J * t * C:.10e}, ratio {ep(P, pi) / (J * t * C):.12f}  (predicted 1)")
t = 0.001; ratios = []
for _ in range(20):
    U1, U2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
    C = (U1[1, 0] - U1[0, 0]) + (U2[1, 1] - U2[1, 0]) + (U1[0, 1] - U1[1, 1]) + (U2[0, 0] - U2[0, 1])
    ratios.append(ep(*chain(U1, U2, t, r1=0.7)) / (t * C) ** 2)
print(f"    revision probabilities 0.7 and 0.3: EP/(t·C)^2 = {np.mean(ratios):.6f} ± {np.std(ratios):.1e}, "
      f"predicted {1 / (2 / 0.0875 + 2 / 0.0375):.6f}")
