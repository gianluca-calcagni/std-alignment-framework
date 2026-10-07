"""T4. Log-linear learning: reversible iff the game has a potential; entropy production at low intensity; and the
misalignment against reversible chains."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(3)

def chain(U1, U2, t):
    m1, m2 = U1.shape; n = m1 * m2; P = np.zeros((n, n))
    for a in range(m1):
        for b in range(m2):
            i = a * m2 + b
            w = np.exp(t * (U1[:, b] - U1[:, b].max())); w /= w.sum()
            for a2 in range(m1): P[i, a2 * m2 + b] += 0.5 * w[a2]
            w = np.exp(t * (U2[a, :] - U2[a, :].max())); w /= w.sum()
            for b2 in range(m2): P[i, a * m2 + b2] += 0.5 * w[b2]
    ev, V = np.linalg.eig(P.T); pi = np.real(V[:, np.argmin(abs(ev - 1))]); pi /= pi.sum()
    return P, pi

def ep(P, pi):
    F = pi[:, None] * P; n = len(pi)
    return sum((F[i, j] - F[j, i]) * np.log(F[i, j] / F[j, i]) for i in range(n) for j in range(i + 1, n) if F[i, j] > 0)

# (i) exact potential games: U_i = Phi + a term the player cannot change
worst = 0.0
for m in (2, 3):
    for _ in range(20):
        Phi = rng.normal(size=(m, m)); U1 = Phi + rng.normal(size=(1, m)); U2 = Phi + rng.normal(size=(m, 1))
        for t in (0.5, 2.0, 5.0):
            worst = max(worst, ep(*chain(U1, U2, t)))
print(f"T4 (i): largest entropy production over 120 potential-game cases {worst:.2e}  (predicted < 1e-12)")

# (ii) random 2x2 games at t = 0.01
t = 0.01; ratios = []
for _ in range(50):
    U1, U2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
    C = (U1[1, 0] - U1[0, 0]) + (U2[1, 1] - U2[1, 0]) + (U1[0, 1] - U1[1, 1]) + (U2[0, 0] - U2[0, 1])
    ratios.append(ep(*chain(U1, U2, t)) / (t * C) ** 2)
ratios = np.array(ratios)
print(f"T4 (ii): EP/(t·C)^2 over 50 random 2x2 games: mean {ratios.mean():.6f}, CV {ratios.std() / ratios.mean():.2e}  (predicted CV < 1%)")

# (iii) misalignment against all reversible chains on the same transitions, for matching pennies
def m_rev(P, pi):
    n = len(pi); edges = [(i, j) for i in range(n) for j in range(i, n) if P[i, j] > 0 or P[j, i] > 0]
    def rate(z):
        W = np.zeros((n, n))
        for (i, j), v in zip(edges, np.exp(z)): W[i, j] = W[j, i] = v
        R = W / W.sum(1, keepdims=True); mask = P > 0
        return float(np.sum((pi[:, None] * P)[mask] * np.log(P[mask] / R[mask])))
    best = min((minimize(rate, rng.normal(size=len(edges)), method="BFGS", options={"gtol": 1e-12}) for _ in range(5)),
               key=lambda r: r.fun)
    return best.fun
U1 = np.array([[1.0, -1.0], [-1.0, 1.0]]); U2 = -U1
for t in (0.01, 0.1, 2.0):
    P, pi = chain(U1, U2, t); e = ep(P, pi); m = m_rev(P, pi)
    print(f"T4 (iii): matching pennies, t={t}: EP {e:.4e}, misalignment against reversible chains {m:.4e}, ratio {m / e:.4f}"
          f"  (predicted <= 0.5; about 0.25 at t = 0.01)")
