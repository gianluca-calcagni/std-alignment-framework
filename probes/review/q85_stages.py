"""Can each term of the factorization be computed on its own? (NOTES.md §43, H86–H88, Q85). Exploratory, not a check;
an invented instance, in the shape of the slides' support bot.
Usage: python3 probes/review/q85_stages.py        (a few seconds)

part A  A pooled limit as a family of limits per condition. Conditions open (0.7) and account (0.3); wrong answers in
        2.9% and 35.3% of them; the limit is 5% overall (the slides' numbers). For an allocation (ε_open, ε_account)
        with 0.7·ε_open + 0.3·ε_account = 0.05, the misalignment against the two limits is a sum of two terms, each
        computed from its own condition. Its least value over the allocations is compared with the misalignment
        against the overall limit (mvp/CORE.md, R10).
part B  A specification written stage by stage. An outcome is (condition c, the actor's reading z of it, action u).
        The contracts: the reading is wrong in at most 2% of each kind of question; when the reading is "open", the
        actor does anything but answer at most 5% of the time; when it is "account", it answers from the
        documentation at most 1% of the time and escalates at most 30%. Three perceptions (exact; 20% of account
        questions read as open; blind, everything read as open) and three ways of deciding (with the look-up; without
        it, escalating; sloppy), nine actors. For each: the perception term, from the perception alone; the decision
        term, from the decisions alone, weighted by how often each reading occurs; their sum; the misalignment the
        library computes on the twelve joint outcomes against all the contracts at once; and the decision term when
        each reading is weighted as an exact perception would give it ("in isolation").
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
from stdalign.spec import Limit, kl_binary, misalignment, overall_rate_limit, rate_limit    # noqa: E402

W_C = np.array([0.7, 0.3])                                                           # open, account


def over(u, eps):
    return kl_binary(u, eps) if u > eps else 0.0


def part_a():
    u, eps = np.array([0.029, 0.353]), 0.05
    pooled, _, v = overall_rate_limit(W_C, u, eps)
    print(f"against the overall limit: {pooled:.4f}; its nearest rates per condition: {v[0]:.4f}, {v[1]:.4f}")
    print(f"{'allocation (open, account)':30s} {'open':>8s} {'account':>8s} {'sum':>8s}")
    for name, e in (("equal", (0.05, 0.05)), ("looser on account", (0.03, 0.29 / 3)), ("the nearest rates", tuple(v))):
        t = [W_C[c] * over(u[c], e[c]) for c in range(2)]
        print(f"{name + f' ({e[0]:.4f}, {e[1]:.4f})':30s} {t[0]:8.4f} {t[1]:8.4f} {sum(t):8.4f}")
    grid = np.linspace(0.0, 0.05 / 0.7, 20001)
    sums = [W_C[0] * over(u[0], a) + W_C[1] * over(u[1], (0.05 - 0.7 * a) / 0.3) for a in grid]
    print(f"least sum over 20,001 allocations: {min(sums):.4f}")


# ---- part B: outcomes indexed (c, z, u), c and z in {open, account}, u in {answer, escalate, look-up}
def idx(c, z, u):
    return (c * 2 + z) * 3 + u


def contracts():
    lims = []
    for c in range(2):                                                               # perception, per condition
        g = np.zeros(12)
        for u in range(3):
            g[idx(c, 1 - c, u)] = 1.0
        lims.append(Limit(tuple(g), 0.02, c, f"reading wrong in condition {c}"))
    for c in range(2):                                                               # decision, per history (c, z)
        for z, rules in ((0, [((1, 2), 0.05)]), (1, [((0,), 0.01), ((1,), 0.30)])):
            for acts, b in rules:
                g = np.zeros(12)
                for u in range(3):
                    g[idx(c, z, u)] = (1.0 if u in acts else 0.0) - b              # a(acts | c, z) ≤ b, homogeneous
                lims.append(Limit(tuple(g), 0.0, None, f"decision at ({c}, {z})"))
    return lims


def joint(V, pi):
    p = np.zeros(12)
    for c in range(2):
        for z in range(2):
            for u in range(3):
                p[idx(c, z, u)] = W_C[c] * V[c][z] * pi[z][u]
    return p


def perception_term(V):
    return sum(W_C[c] * over(V[c][1 - c], 0.02) for c in range(2))


def decision_local(pi):
    """The misalignment of the decisions at each reading, against that reading's contract: from pi alone."""
    at_open = over(pi[0][1] + pi[0][2], 0.05)
    lims = [rate_limit([0], 0.01, n=3), rate_limit([1], 0.30, n=3)]
    at_account = misalignment(np.asarray(pi[1], float), lims).value
    return np.array([at_open, at_account])


def part_b():
    perceptions = {"exact": [[1, 0], [0, 1]], "20% of account read open": [[1, 0], [0.2, 0.8]],
                   "blind": [[1, 0], [1, 0]]}
    decisions = {"with the look-up": [[1, 0, 0], [0, 0, 1]], "no look-up, escalates": [[1, 0, 0], [0, 1, 0]],
                 "sloppy": [[0.9, 0.1, 0], [0.2, 0.6, 0.2]]}
    world = np.repeat([0, 1], 6)
    lims = contracts()
    print(f"{'perception':26s} {'decisions':22s} {'percep.':>8s} {'decis.':>8s} {'sum':>8s} {'joint':>8s} {'isolated':>9s}")
    worst = 0.0
    for pn, V in perceptions.items():
        V = np.asarray(V, float)
        for dn, pi in decisions.items():
            pi = np.asarray(pi, float)
            local = decision_local(pi)
            reading = W_C @ V                                                        # how often each reading occurs
            tp, td, iso = perception_term(V), float(reading @ local), float(W_C @ local)
            jm = misalignment(joint(V, pi), lims, world).value
            worst = max(worst, abs(jm - tp - td))
            print(f"{pn:26s} {dn:22s} {tp:8.4f} {td:8.4f} {tp + td:8.4f} {jm:8.4f} {iso:9.4f}")
    print(f"largest gap between the sum of the two terms and the joint misalignment: {worst:.1e}")


if __name__ == "__main__":
    print("== part A ==")
    part_a()
    print("\n== part B ==")
    part_b()
