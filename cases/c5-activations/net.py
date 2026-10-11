"""C5's system, shared by rehearse.py and run.py: a small network whose internals are known, its exact distributions in
two conditions, the probes on its activations, and the bound of [P17](ii).

Inputs are 6 bits: x_0 is the cue of evaluation, x_1 .. x_5 are task bits. The view is the last hidden layer, 8 binary
units; the output, one of good, bad and other, depends on the input only through it. Two structures:
- "linear": h_1 = x_0 copies the cue, h_2 = x_1;
- "xor":    h_1 = x_0 XOR x_1 and h_2 = x_1, so the cue is h_1 XOR h_2 and neither unit alone carries it (P(x_1) = 1/2);
in both, h_3 .. h_8 are threshold units on x_2 .. x_5 with random weights. The output's logits are B·h + c, with B zero
on h_1 and h_2, plus GAP on "good" when the cue is detected (h_1 in the linear structure, h_1 XOR h_2 in the xor one): the actor behaves better when
it reads the cue. Every distribution is exact, over the 64 inputs.
"""
import sys
from itertools import combinations, product
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, minimize
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from casekit import log_mean_exp                                                    # noqa: E402

INPUTS = np.array(list(product([0, 1], repeat=6)), dtype=int)                     # 64 × 6
F = np.array([1.0, -1.0, 0.0])                                                     # good, bad, other
GAP = 2.0
UNITS = 8


def kl(p, r):
    """KL(p‖r) in nats; +inf when p puts mass where r has none."""
    p, r = np.asarray(p, float), np.asarray(r, float)
    m = p > 0
    if np.any(r[m] <= 0):
        return float("inf")
    return float(np.sum(p[m] * np.log(p[m] / r[m])))


class Instance:
    """One network, with the input laws of the two conditions, eval (observed) and use (not observed)."""

    def __init__(self, seed, structure, p_cue_eval, p_cue_use):
        rng = np.random.default_rng(seed)
        self.rng = rng
        pis = rng.uniform(0.3, 0.7, 5)
        if structure == "xor":
            pis[0] = 0.5                                                           # x_1 balanced: h_1 alone is blind
        self.structure = structure
        Wt = rng.normal(0, 1, (UNITS - 2, 4)); bt = rng.normal(0, 0.5, UNITS - 2)
        self.B = rng.normal(0, 0.7, (3, UNITS)); self.c = rng.normal(0, 0.5, 3)
        self.B[:, :2] = 0                                                          # the cue acts only through GAP
        x = INPUTS
        h1 = x[:, 0] if structure == "linear" else x[:, 0] ^ x[:, 1]
        rest = (x[:, 2:] @ Wt.T + bt > 0).astype(int)
        self.H = np.column_stack([h1, x[:, 1], rest])                              # 64 × 8, the view of each input
        cue = self.H[:, 0] if structure == "linear" else self.H[:, 0] ^ self.H[:, 1]
        z = self.H @ self.B.T + self.c + GAP * np.outer(cue, [1, 0, 0])
        z -= z.max(axis=1, keepdims=True)
        self.out = np.exp(z) / np.exp(z).sum(axis=1, keepdims=True)                 # 64 × 3: outputs given the view
        task = np.prod(np.where(x[:, 1:] == 1, pis, 1 - pis), axis=1)
        self.W = {c: np.where(x[:, 0] == 1, pc, 1 - pc) * task
                  for c, pc in (("eval", p_cue_eval), ("use", p_cue_use))}
        keys, self.cell = np.unique(self.H, axis=0, return_inverse=True)           # the distinct views
        self.cell = self.cell.ravel(); self.views = keys
        self.V = {c: np.bincount(self.cell, weights=w, minlength=len(keys)) for c, w in self.W.items()}
        self.p = {c: w @ self.out for c, w in self.W.items()}                     # the behaviour in each condition

    def exact(self):
        """The truths: KL(p_use‖p_eval) ≤ KL(V_use‖V_eval) ≤ KL(W_use‖W_eval), and the averages of F."""
        return {"kl_behaviour": kl(self.p["use"], self.p["eval"]), "kl_view": kl(self.V["use"], self.V["eval"]),
                "kl_input": kl(self.W["use"], self.W["eval"]), "F_eval": float(self.p["eval"] @ F),
                "F_use": float(self.p["use"] @ F)}

    def activations(self, n):
        """n views drawn independently in each condition, from the instance's own generator."""
        return {c: self.H[self.rng.choice(len(INPUTS), size=n, p=w / w.sum())] for c, w in self.W.items()}


def features(H, kind):
    """The probe's features: an intercept and the units ("linear"), and their pairwise products ("quadratic")."""
    cols = [np.ones(len(H)), *H.T.astype(float)]
    if kind == "quadratic":
        cols += [H[:, i] * H[:, j] for i, j in combinations(range(H.shape[1]), 2)]
    return np.column_stack(cols)


def fit_probe(X, y, l2=1e-3):
    """Logistic regression of y (1 = use) on X, L2-penalized except the intercept; returns the coefficients."""
    def loss(w):
        f = X @ w
        lse = np.logaddexp(0, f)
        reg = 0.5 * l2 * np.sum(w[1:] ** 2)
        return float(np.mean(lse - y * f) + reg), X.T @ (1 / (1 + np.exp(-f)) - y) / len(y) + l2 * np.r_[0, w[1:]]
    w = minimize(loss, np.zeros(X.shape[1]), jac=True, method="L-BFGS-B", options={"maxiter": 2000, "gtol": 1e-10}).x
    return w


def probe_divergence(acts, kind, n_train):
    """ε̂: the Donsker–Varadhan bound E_use[f] − log E_eval[e^f] on held-out views, f the probe's log-odds of use."""
    tr = {c: a[:n_train] for c, a in acts.items()}; te = {c: a[n_train:] for c, a in acts.items()}
    X = np.vstack([features(tr["use"], kind), features(tr["eval"], kind)])
    y = np.r_[np.ones(len(tr["use"])), np.zeros(len(tr["eval"]))]
    w = fit_probe(X, y)
    f_use, f_eval = features(te["use"], kind) @ w, features(te["eval"], kind) @ w
    return float(f_use.mean() - log_mean_exp(f_eval))


def lower_bound(p_a, eps):
    """[P17](ii): the least average of F in a condition whose behaviour departs from p_a by at most eps."""
    if not eps > 0:
        return float(p_a @ F)
    low = F == F.min()
    if eps >= -np.log(p_a[low].sum()):
        return float(F.min())
    tilt = lambda lam: (p_a * np.exp(-lam * F)) / (p_a * np.exp(-lam * F)).sum()
    hi = 1.0
    while kl(tilt(hi), p_a) < eps:
        hi *= 2
    lam = brentq(lambda lam: kl(tilt(lam), p_a) - eps, 0.0, hi)
    return float(tilt(lam) @ F)


def measure(seed, structure, n=1000, p_cue=(0.7, 0.3)):
    """Every quantity of one instance: the truths, the two probes' ε̂, and the bound of [P17](ii) with each."""
    inst = Instance(seed, structure, *p_cue)
    row = {"seed": seed, "structure": structure, **inst.exact(), "p_eval": inst.p["eval"].tolist(),
           "p_use": inst.p["use"].tolist()}
    acts = inst.activations(n)
    for kind in ("linear", "quadratic"):
        row[f"eps_{kind}"] = probe_divergence(acts, kind, n // 2)
    row["bound_true"] = lower_bound(inst.p["eval"], row["kl_view"])
    for kind in ("linear", "quadratic"):
        row[f"bound_{kind}"] = lower_bound(inst.p["eval"], row[f"eps_{kind}"])
    return row
