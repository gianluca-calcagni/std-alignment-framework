"""Q77 brainstorm: a declared contamination tolerance removes infinite misalignment.

A_eta = {(1 - eta) a + eta q : a in A, q any behaviour}. For a rate limit A = {a : a(C) <= eps},
A_eta is the rate limit at eps' = (1 - eta) eps + eta (checked here by sampling), so misalignment has a closed form.
Claims: (i) M_{A_eta}(p) <= log(1/eta); (ii) M_{A_eta}(p) increases to M_A(p) as eta -> 0;
(iii) a forbidden outcome (eps = 0) gives M_A infinite and M_{A_eta} finite.
"""
import numpy as np

def m_rate_limit(u, eps):
    """Misalignment of a behaviour putting mass u on C against a(C) <= eps (binary reduction, exact)."""
    if u <= eps:
        return 0.0
    if eps == 0:
        return np.inf
    return u * np.log(u / eps) + (1 - u) * np.log((1 - u) / (1 - eps))

def check_characterization(eps, eta, rng, n=200000):
    """Sample a with a(C) <= eps and q free; the largest mass on C of (1-eta) a + eta q is eps'."""
    aC = rng.uniform(0, eps, n) if eps > 0 else np.zeros(n)
    qC = rng.uniform(0, 1, n)
    bC = (1 - eta) * aC + eta * qC
    return bC.max(), (1 - eta) * eps + eta

rng = np.random.default_rng(1)
for eps in (0.01, 0.0):
    for eta in (0.1, 0.001):
        got, want = check_characterization(eps, eta, rng)
        print(f"eps={eps} eta={eta}: sampled max b(C) = {got:.6f}, eps' = {want:.6f}, never above: {got <= want + 1e-12}")

u = 0.02
for eps in (0.01, 0.0):
    print(f"u={u}, eps={eps}: M_A = {m_rate_limit(u, eps):.6f}")
    for eta in (0.1, 0.01, 0.001, 0.0001, 1e-6, 1e-9):
        m = m_rate_limit(u, (1 - eta) * eps + eta)
        print(f"  eta={eta:<7g} M_A_eta = {m:.6f}  log(1/eta) = {np.log(1/eta):.3f}  below bound: {m <= np.log(1/eta)}")
