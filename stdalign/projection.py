"""The behaviour nearest to a given one among those with given averages: the I-projection onto a linear set ([P15](i)).

[P44], [P48] and [P49] are built on it, and so is the split of misalignment into its avoidable and unavoidable parts
for linear limits ([P15]).
"""
import numpy as np
from scipy.optimize import minimize
from .core import tilt, log_normalizer


def project_linear(r, A, b):
    """argmin over {p ∈ Δ : A·p = b} of KL(p‖r), for `r` of full support and a feasible set with a point of full
    support. By [P15](iii) it is tilt(r, Aᵀθ), with θ minimizing the convex dual log E_r[exp(Aᵀθ)] − θ·b; solved by
    BFGS, then polished by damped Newton steps."""
    r, A, b = np.asarray(r, dtype=float), np.atleast_2d(np.asarray(A, dtype=float)), np.atleast_1d(np.asarray(b, float))
    if A.shape != (b.size, r.size):
        raise ValueError(f"A must have one row per average and one column per outcome: shape ({b.size}, {r.size})")
    dual = lambda th: log_normalizer(r, A.T @ th) - th @ b
    grad = lambda th: A @ tilt(r, A.T @ th) - b
    th = minimize(dual, np.zeros(A.shape[0]), jac=grad, method="BFGS", options={"gtol": 1e-13, "maxiter": 10000}).x
    for _ in range(30):
        p = tilt(r, A.T @ th)
        H = (A * p) @ A.T - np.outer(A @ p, A @ p)
        step = np.linalg.lstsq(H, grad(th), rcond=None)[0]
        lam = 1.0
        while dual(th - lam * step) > dual(th) + 1e-15 and lam > 1e-8:
            lam /= 2
        th = th - lam * step
    return tilt(r, A.T @ th)
