"""TR3 of general/transfer.md on two instances: misalignment, the supremum over finite descriptions of the least cell
divergence to an intended behaviour, against the least divergence over the closure of the intended behaviours, which
TR3 says it equals when that closure is compact for the convergence of every event's probability. Probed, not tested:
no prediction was registered, and the theorem is proved in the file. Run: python3 t8_transfer.py   (a few seconds)

circle   Outcomes on the circle [0, 2π), uniform default u. Intended: the behaviours with density 1 + ½·sin(k·x) to u,
         k = 1, 2, …, whose closure adds u itself (every event's probability under them tends to its probability under
         u). The actual behaviour has density 1 + 0.4·sin(x) + 0.1·cos(x). Descriptions: N equal arcs, N = 2 … 4096,
         every one decidable under the circle's usual nearness.
ray      Outcomes in [0, 1]; the default puts ½ on the outcome 1 and spreads ½ uniformly; F(x) = x, so the pursuit ray
         has a limit, the default conditioned on {1}, and with it is compact. The actual behaviour puts 0.95 on 1 and
         spreads 0.05. Descriptions: N equal bins, with {1} its own cell (no nearness), or 1 inside the last bin (the
         usual nearness, under which {1} is not decidable for this actor). TR3 says both give the same misalignment.
"""
import numpy as np
from scipy.optimize import minimize_scalar

FINE = 2 ** 16                                                   # quadrature points per unit, for the closed forms


def kl_cells(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    m = a > 0
    if np.any(b[m] <= 0):
        return np.inf
    return float(np.sum(a[m] * np.log(a[m] / b[m])))


def circle():
    x = (np.arange(FINE * 8) + 0.5) * 2 * np.pi / (FINE * 8)
    phat = 1 + 0.4 * np.sin(x) + 0.1 * np.cos(x)
    ks = np.arange(1, 400)
    def kl_dens(f, g):                                            # densities to u, averaged over the circle
        return float(np.mean(f * np.log(f / g)))
    closure = min(min(kl_dens(phat, 1 + 0.5 * np.sin(k * x)) for k in ks[:50]), kl_dens(phat, np.ones_like(x)))
    print(f"circle: least divergence over the closure = {closure:.6f}")
    for N in (2, 4, 16, 64, 256, 1024, 4096):
        edges = np.linspace(0, 2 * np.pi, N + 1)
        def cells(dens):                                          # exact arc probabilities by the antiderivative
            return np.diff(dens(edges)) / (2 * np.pi)
        a = cells(lambda e: e - 0.4 * np.cos(e) + 0.1 * np.sin(e))
        best = kl_cells(a, np.full(N, 1 / N))                     # the limit u is in the closure
        for k in ks:
            b = cells(lambda e: e - 0.5 * np.cos(k * e) / k)
            best = min(best, kl_cells(a, b))
        print(f"  N = {N:5d}: M_P = {best:.6f}")


def ray():
    w_atom, w_cont = 0.95, 0.05
    def ray_cells(t, edges, atom_alone):
        z = 0.5 * np.exp(t) + 0.5 * (np.expm1(t) / t if t > 0 else 1.0)
        cont = 0.5 * (np.diff(np.exp(t * edges)) / t if t > 0 else np.diff(edges)) / z
        atom = 0.5 * np.exp(t) / z
        if atom_alone:
            return np.append(cont, atom)
        cont[-1] += atom
        return cont
    def kl_full(t):                                               # KL(p̂‖p_t), atom plus continuous part
        z = 0.5 * np.exp(t) + 0.5 * (np.expm1(t) / t if t > 0 else 1.0)
        atom = w_atom * np.log(w_atom / (0.5 * np.exp(t) / z))
        xs = (np.arange(FINE) + 0.5) / FINE
        cont = np.mean(w_cont * np.log(w_cont / (0.5 * np.exp(t * xs) / z)))
        return atom + cont
    r = minimize_scalar(kl_full, bounds=(0, 60), method="bounded", options={"xatol": 1e-10})
    print(f"ray: least divergence over the closure = {r.fun:.6f} at t = {r.x:.4f} (the limit at t = ∞ is at +∞)")
    for atom_alone in (True, False):
        label = "{1} its own cell (no nearness)" if atom_alone else "1 in the last bin (usual nearness)"
        print(f"  {label}")
        for N in (1, 2, 4, 16, 64, 256, 1024):
            edges = np.linspace(0, 1, N + 1)
            a = w_cont * np.diff(edges)
            a = np.append(a, w_atom) if atom_alone else np.concatenate([a[:-1], [a[-1] + w_atom]])
            f = lambda t: kl_cells(a, ray_cells(t, edges, atom_alone))
            res = minimize_scalar(f, bounds=(0, 60), method="bounded", options={"xatol": 1e-10})
            limit = kl_cells(a, np.append(np.zeros(N), 1.0) if atom_alone else np.append(np.zeros(N - 1), 1.0))
            print(f"    N = {N:5d}: M_P = {max(0.0, min(res.fun, limit)):.6f}")


if __name__ == "__main__":
    circle()
    ray()
