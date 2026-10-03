"""T3. Two tit-for-tat players with errors: no coordination in any single round, a lot over time."""
import numpy as np
from itertools import product
from math import log
eps = 0.05
S = list(product((0, 1), (0, 1)))                     # (a1, a2); 0 = cooperate, 1 = defect
P = np.zeros((4, 4))
for i, (a1, a2) in enumerate(S):
    for j, (b1, b2) in enumerate(S):                   # next a1 copies a2, next a2 copies a1, each with error eps
        P[i, j] = (1 - eps if b1 == a2 else eps) * (1 - eps if b2 == a1 else eps)
ev, V = np.linalg.eig(P.T); pi = np.real(V[:, np.argmin(abs(ev - 1))]); pi /= pi.sum()
joint = pi.reshape(2, 2); m1, m2 = joint.sum(1), joint.sum(0)
mi_round = float(np.sum(joint * np.log(joint / np.outer(m1, m2))))
H = lambda r: -float(np.sum(r[r > 0] * np.log(r[r > 0])))
h_joint = float(sum(pi[i] * H(P[i]) for i in range(4)))
def block_entropy(n, who):
    """Exact entropy of one player's first n actions, by the forward algorithm over all 2^n sequences."""
    probs = []
    for seq in product((0, 1), repeat=n):
        alpha = np.array([pi[i] if S[i][who] == seq[0] else 0.0 for i in range(4)])
        for x in seq[1:]:
            alpha = (alpha @ P) * np.array([1.0 if S[j][who] == x else 0.0 for j in range(4)])
        probs.append(alpha.sum())
    return H(np.array(probs))
hb = [block_entropy(n, 0) for n in (13, 14)]
h1 = hb[1] - hb[0]                                     # conditional entropy of the next action: the entropy rate
print(f"T3: stationary law {pi.round(4)}; same-round mutual information {mi_round:.2e}  (predicted < 1e-12)")
print(f"    entropy rates: each player {h1:.4f}, the pair {h_joint:.4f}; mutual information rate {2 * h1 - h_joint:.4f} nats/round  (predicted > 0.1)")
lag = (pi[:, None] * P).reshape(2, 2, 2, 2).sum(axis=(1, 2))  # a1 at t against a2 at t+1
print(f"    lagged mutual information, a1 now vs a2 next round: {float(np.sum(lag * np.log(lag / np.outer(lag.sum(1), lag.sum(0))))):.4f}")
