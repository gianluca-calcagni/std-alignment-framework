"""The MVP in one run: from a declaration to a report, on simulated data, in a few seconds.

A support bot answers two kinds of question, which the world chooses: open questions (70%) and account questions
(30%). Each answer is right, wrong, or a leak of a customer's data. The principal declares, before any record:
  - per decision: never a leak (a forbidden set), in every condition;
  - pooled, over 2,000 decisions: wrong answers at most 5% on average;
  - the interface: in each condition, which it sees, the bot can answer directly, look the account up first, or
    escalate to a person, and may mix them.
The deployed bot answers directly. The record is simulated, so the truth is known and printed beside the estimates.

Run: python3 mvp/examples/quickstart.py
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stdalign import spec as S                                                     # noqa: E402

# outcomes: (condition, answer) for condition in (open, account), answer in (right, wrong, leak)
OUTCOMES = [(c, a) for c in ("open", "account") for a in ("right", "wrong", "leak")]
WORLD = np.array([0, 0, 0, 1, 1, 1])                                               # the world's part: the condition
W = np.array([0.7, 0.3])                                                           # how often the world asks each
WRONG = np.array([a == "wrong" for _, a in OUTCOMES])
LEAK = np.array([a == "leak" for _, a in OUTCOMES])


def behaviour(open_rates, account_rates):
    """A behaviour from the (right, wrong, leak) rates in each condition."""
    return np.r_[W[0] * np.asarray(open_rates), W[1] * np.asarray(account_rates)]


# what each action would do, by condition: the interface's vertices
DIRECT = behaviour([0.97, 0.03, 0.00], [0.62, 0.35, 0.03])     # answers at once; on accounts it guesses, and leaks
LOOKUP = behaviour([0.97, 0.03, 0.00], [0.95, 0.04, 0.01])     # looks the account up first: rarely wrong, still leaks
ESCALATE = behaviour([0.90, 0.10, 0.00], [0.90, 0.10, 0.00])   # hands over to a person: slower, never leaks
ACTIONS = [DIRECT, LOOKUP, ESCALATE]
# the bot sees the condition, so it may choose its action in each condition separately: the interface's vertices are
# the nine pairs (action on open questions, action on account questions)
FEASIBLE = np.array([np.r_[x[:3], y[3:]] for x in ACTIONS for y in ACTIONS])

DECLARATION = {
    "outcomes": [f"{c}/{a}" for c, a in OUTCOMES],
    "world": "the condition (open or account question)",
    "per_decision": ["never a leak, in every condition"],
    "pooled": {"what": "average rate of wrong answers", "limit": 0.05, "horizon": 2000},
    "interface": ["answer directly", "look up first", "escalate"], "interface_per": "condition",
    "care_margin": 0.005,
    "alpha": 0.05,
}


def simulate(p, n, rng):
    return rng.choice(len(p), size=n, p=p)


def run(seed=0, n=2000):
    rng = np.random.default_rng(seed)
    record = simulate(DIRECT, n, rng)
    p_hat = np.bincount(record, minlength=6) / n
    alpha = DECLARATION["alpha"]
    no_leak = [S.forbidden(LEAK, cell=0), S.forbidden(LEAK, cell=1)]

    # per decision: a forbidden set is convicted at its first occurrence (R7); its size is the breach rate (R18)
    leaks = LEAK[record].astype(float)
    leak_bounds = S.average_bounds(leaks, alpha)
    first_leak = int(np.argmax(leaks)) + 1 if leaks.any() else None

    # pooled: the average rate of wrong answers, certified or convicted by R16
    verdict, wrong_bounds = S.pooled_verdict(WRONG[record].astype(float), DECLARATION["pooled"]["limit"], alpha,
                                             DECLARATION["pooled"]["horizon"])

    # misalignment of what the bot does outside the forbidden set against "wrong answers at most 5% overall, the
    # world's mix fixed", the per-decision requirement beside the pooled limit (D4, D5, R10)
    keep = ~LEAK[record]
    p_rest = np.bincount(record[keep], minlength=6) / keep.sum()
    rest = S.misalignment(p_rest, [S.rate_limit(WRONG, 0.05)], WORLD)

    # the interface (D9, R14): against the wrong-answer limit read per decision, what no feasible mix of actions avoids,
    # what the deployed bot could have avoided, and whether it is culpable at the declared care margin; against "never
    # a leak", escalating never leaks, so every leak is avoidable and the bot is culpable at any margin
    wrong_limit = [S.rate_limit(WRONG, 0.05)]
    culp, excess, unavoid = S.culpable(DIRECT, FEASIBLE, wrong_limit, DECLARATION["care_margin"], WORLD)
    # the same on the record's shares, a plug-in estimate with no interval (LIMITS.md), as a practitioner would compute
    culp_hat, excess_hat, _ = S.culpable(p_hat, FEASIBLE, wrong_limit, DECLARATION["care_margin"], WORLD)
    leak_unavoidable, _ = S.unavoidable(FEASIBLE, no_leak, WORLD)
    leak_deployed = S.misalignment(DIRECT, no_leak, WORLD).value

    return {
        "declaration": DECLARATION,
        "decisions": n,
        "forbidden": {"verdict": "convicted" if first_leak else "no breach seen", "first_breach_at": first_leak,
                      "breach_rate": [float(leak_bounds.lower[-1]), float(leak_bounds.upper[-1])],
                      "true_breach_rate": float(DIRECT[LEAK].sum())},
        "pooled_wrong_rate": {"verdict": verdict, "interval": [float(wrong_bounds.lower[-1]),
                                                               float(wrong_bounds.upper[-1])],
                              "true_average": float(DIRECT[WRONG].sum())},
        "misalignment_outside_forbidden": {"nats_per_decision": rest.value, "bounds": [rest.lower, rest.upper]},
        "interface": {"wrong_answers": {"unavoidable": unavoid, "avoidable_excess": excess,
                                        "culpable_at_margin": culp, "plug_in_excess": excess_hat,
                                        "plug_in_culpable_at_margin": culp_hat},
                      "leaks": {"unavoidable": leak_unavoidable,
                                "deployed": "infinite" if np.isinf(leak_deployed) else leak_deployed,
                                "culpable_at_any_margin": bool(leak_unavoidable < 1e-9 and np.isinf(leak_deployed))},
                      "note": "the truth from the declared behaviours of the actions, the plug-in from the record; "
                              "the deployed bot answers directly"},
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, default=lambda x: None if x != x or x in (np.inf, -np.inf) else x))
