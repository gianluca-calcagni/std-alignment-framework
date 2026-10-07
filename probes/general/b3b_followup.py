"""B3b. The atom count at new values of beta, and the critical beta, after B3's count prediction failed."""
import numpy as np
from math import sqrt
s = np.linspace(0, 1, 1001); rho = np.full(s.size, 1 / s.size); a = np.linspace(0, 1, 1001)
L = (a[None, :] - s[:, None]) ** 2
def ba(beta, iters):
    K = np.exp(-beta * L); pa = np.full(a.size, 1 / a.size)
    for _ in range(iters):
        pa = pa * ((rho / (K @ pa)) @ K)
    return pa
def peaks(pa):
    mass = np.convolve(pa, np.ones(41), mode="same")
    return [i for i in range(1, a.size - 1) if pa[i] >= pa[i - 1] and pa[i] > pa[i + 1] and mass[i] > 1e-4]
for beta in (50.0, 200.0):
    pa = ba(beta, 100_000)
    print(f"beta={beta}: {len(peaks(pa))} atoms, predicted between {sqrt(beta / 6):.1f} and {2 * sqrt(beta / 6):.1f}")
for beta in (5.85, 6.15):
    pa = ba(beta, 100_000)
    print(f"beta={beta}: spread of the default {np.sqrt(pa @ (a - pa @ a) ** 2):.4f}")
