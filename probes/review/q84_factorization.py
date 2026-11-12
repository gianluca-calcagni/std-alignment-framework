"""Is "the cost of each limitation" one number, and can the avoidable excess be split as the unavoidable part is?
(NOTES.md §42, H83–H85, Q84). Exploratory, not a check; an invented instance, in the shape of the slides' support bot.
Usage: python3 probes/review/q84_factorization.py        (about a minute)

The instance. Conditions: open questions (0.7) and account questions (0.3), the world's part. Outcomes in each: W
wrong, R escalated, A correct. Actions: answer from the documentation, escalate, look the account up. Environment:
open, answer → A 0.97, W 0.03; open, look-up → A 0.5, W 0.5; account, answer → W; account, look-up → A 0.9, W 0.1;
escalate → R. Requirements: wrong answers at most 5% overall, escalations at most 10% overall, the world's mix fixed.

Two capabilities: the VIEW (telling open from account) and the TOOL (the look-up). m(S) is the least misalignment of
any policy with the capabilities in S (mvp/CORE.md, D9), found by minimizing the library's misalignment over
policies, a convex problem, from several starts.

part 1  The cost of each capability by the order in which they are removed (R14's chain), and their Shapley shares.
part 2  The actor has both capabilities; on account questions it answers 20%, escalates 60%, looks up 20%. Its
        avoidable excess, split along features of what it did: F1, "answers account questions from the documentation
        at least 20% of the time"; F2, "looks up at most 20% of the time". c(F) is the least misalignment of any
        feasible policy with the features F, less m(both): what the features alone entail. The rest is unexplained.
"""
import itertools
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
from stdalign.spec import misalignment, rate_limit                                   # noqa: E402

W_C = np.array([0.7, 0.3])                                                           # open, account
ENV = np.array([[[0.03, 0.0, 0.97], [0.0, 1.0, 0.0], [0.5, 0.0, 0.5]],               # open: answer, escalate, look-up
                [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.1, 0.0, 0.9]]])                # account; columns W, R, A
WORLD = np.array([0, 0, 0, 1, 1, 1])
LIMITS = [rate_limit([0, 3], 0.05, n=6, name="wrong"), rate_limit([1, 4], 0.10, n=6, name="escalated")]


def behaviour(pi):
    pi = np.asarray(pi, float).reshape(2, 3)
    return np.concatenate([W_C[c] * (pi[c] @ ENV[c]) for c in range(2)])


def M(pi):
    return misalignment(behaviour(pi), LIMITS, WORLD).value


def least(view=True, tool=True, features=()):
    """The least misalignment over policies with the given capabilities and features (linear in the policy). The
    policy is written in the fewest free numbers, so that no constraint repeats another: one distribution over the
    actions the actor has, per condition it can tell apart."""
    k = 3 if tool else 2                                                             # actions it has
    blocks = 2 if view else 1                                                        # conditions it can tell apart

    def full(x):
        rows = np.zeros((2, 3))
        for c in range(2):
            rows[c, :k] = x[(c if view else 0) * k:(c if view else 0) * k + k]
        return rows.ravel()

    cons = [{"type": "eq", "fun": (lambda x, j=j: x[j * k:(j + 1) * k].sum() - 1)} for j in range(blocks)]
    if "F1" in features:
        cons.append({"type": "ineq", "fun": lambda x: full(x)[3] - 0.2})             # answers account questions ≥ 20%
    if "F2" in features:
        cons.append({"type": "ineq", "fun": lambda x: 0.2 - full(x)[5]})             # looks up ≤ 20%
    rng = np.random.default_rng(3)
    best = np.inf
    for x0 in [np.full(blocks * k, 1 / k)] + [rng.dirichlet(np.ones(k), blocks).ravel() for _ in range(8)]:
        r = minimize(lambda x: M(full(x)), x0, method="SLSQP", bounds=[(0, 1)] * (blocks * k), constraints=cons,
                     options={"ftol": 1e-12})
        x = np.clip(r.x, 0, 1)
        ok = all(abs(c["fun"](x)) < 1e-6 if c["type"] == "eq" else c["fun"](x) > -1e-6 for c in cons)
        if ok and np.isfinite(r.fun) and r.fun < best:
            best = float(r.fun)
    return max(best, 0.0)


def shapley(players, v):
    out = {}
    for i in players:
        rest = [j for j in players if j != i]
        tot = 0.0
        for order in itertools.permutations(players):
            before = frozenset(order[:order.index(i)])
            tot += v[before | {i}] - v[before]
        out[i] = tot / len(list(itertools.permutations(players)))
        del rest
    return out


if __name__ == "__main__":
    # part 1: a capability REMOVED is a limitation; v(S) = least misalignment with the limitations in S
    m = {(v, t): least(view=v, tool=t) for v in (True, False) for t in (True, False)}
    print("part 1: least misalignment by capabilities (nats per decision)")
    for (v, t), val in m.items():
        print(f"  view {'yes' if v else 'no ':3s} tool {'yes' if t else 'no ':3s}  {val:.4f}")
    v1 = {frozenset(): m[True, True], frozenset({"view"}): m[False, True], frozenset({"tool"}): m[True, False],
          frozenset({"view", "tool"}): m[False, False]}
    print("  the cost of losing the VIEW: removed first", f"{v1[frozenset({'view'})] - v1[frozenset()]:.4f};",
          "removed after the tool", f"{v1[frozenset({'view', 'tool'})] - v1[frozenset({'tool'})]:.4f}")
    print("  the cost of losing the TOOL: removed first", f"{v1[frozenset({'tool'})] - v1[frozenset()]:.4f};",
          "removed after the view", f"{v1[frozenset({'view', 'tool'})] - v1[frozenset({'view'})]:.4f}")
    sh = shapley(["view", "tool"], v1)
    print("  Shapley shares:", {k: round(x, 4) for k, x in sh.items()}, "sum", f"{sum(sh.values()):.4f}",
          "= m(neither) − m(both)", f"{v1[frozenset({'view', 'tool'})] - v1[frozenset()]:.4f}")

    # part 2: the avoidable excess along features of what the actor did
    actor = [1, 0, 0, 0.2, 0.6, 0.2]
    total, base = M(actor), m[True, True]
    v2 = {frozenset(): base, frozenset({"F1"}): least(features=("F1",)), frozenset({"F2"}): least(features=("F2",)),
          frozenset({"F1", "F2"}): least(features=("F1", "F2"))}
    print("\npart 2: the actor's misalignment", f"{total:.4f}", "unavoidable", f"{base:.4f}", "avoidable excess",
          f"{total - base:.4f}")
    print("  entailed by F1 alone", f"{v2[frozenset({'F1'})] - base:.4f};", "by F2 alone",
          f"{v2[frozenset({'F2'})] - base:.4f};", "by both", f"{v2[frozenset({'F1', 'F2'})] - base:.4f}")
    sh2 = shapley(["F1", "F2"], v2)
    print("  Shapley shares:", {k: round(x, 4) for k, x in sh2.items()})
    print("  unexplained by the two features", f"{total - v2[frozenset({'F1', 'F2'})]:.4f}")
    print("  check: unavoidable + shares + unexplained =",
          f"{base + sum(sh2.values()) + total - v2[frozenset({'F1', 'F2'})]:.4f}")
