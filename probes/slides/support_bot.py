"""The worked example of slides/framework.md: a frozen support bot, judged against its previous version.
Every number the slides quote is printed here. Probed, not tested: the results used are proved in v14/.
Run from the repository's root: python3 probes/slides/support_bot.py   (about a minute)

Conditions c: an open question (answerable from the documentation, 70%) or an account question (needs account access
the bot lacks, 30%). Outcomes x: L leaks another customer's data, W a wrong answer, R escalates to a human, A a correct
answer. Actions u: answer from the documentation, look up the account, escalate. The environment: answering an open
question is right with probability 0.97; answering an account question from the documentation is always wrong; looking
up an account is wrong, and leaks with probability 0.004; escalating gives R. The view: the bot sees an open question
as open. The previous version saw every account question as one (a full view); the new version was deployed without
that signal, and sees an account question as one with probability 0.8, and as open with probability 0.2.
The request, declared before: R1 never leak; R2 at most 5% wrong answers overall; R3 no shortfall beyond 0.02 against
the previous version at the standards "escalated or correct" and "correct".
"""
import numpy as np
from scipy.optimize import minimize

C, X = ["open", "account"], ["L", "W", "R", "A"]
w = np.array([0.7, 0.3])
ENV = {("open", "answer"): [0, .03, 0, .97], ("account", "answer"): [0, 1, 0, 0],
       ("open", "lookup"): [0, 1, 0, 0], ("account", "lookup"): [.004, .996, 0, 0],
       ("open", "escalate"): [0, 0, 1, 0], ("account", "escalate"): [0, 0, 1, 0]}
U = ["answer", "lookup", "escalate"]
VIEW_COARSE = {"open": {"open": 1.0}, "account": {"account": 0.8, "open": 0.2}}
VIEW_FULL = {"open": {"open": 1.0}, "account": {"account": 1.0}}
M_MARGIN, W_LIMIT = 0.02, 0.05


def behaviour(policy, view):
    """Joint behaviour on (condition, outcome), as an array of shape (2, 4), from a policy on signals."""
    out = np.zeros((2, 4))
    for i, c in enumerate(C):
        for z, pz in view[c].items():
            for u in U:
                out[i] += w[i] * pz * policy[z][u] * np.array(ENV[(c, u)])
    return out


def kl(p, a):
    p, a = p.ravel(), a.ravel(); m = p > 0
    return np.inf if np.any(a[m] <= 0) else float(np.sum(p[m] * np.log(p[m] / a[m])))


previous = behaviour({"open": {"answer": .9, "lookup": 0, "escalate": .1},
                      "account": {"answer": 0, "lookup": 0, "escalate": 1}}, VIEW_FULL)
actual = behaviour({"open": {"answer": .97, "lookup": 0, "escalate": .03},
                    "account": {"answer": 0, "lookup": .2, "escalate": .8}}, VIEW_COARSE)
pool = lambda b: b.sum(0)
rAR, rA = pool(previous)[2] + pool(previous)[3], pool(previous)[3]


def constraints(forbid):
    cons = [{"type": "eq", "fun": lambda a, i=i: a.reshape(2, 4)[i].sum() - w[i]} for i in range(2)]
    cons.append({"type": "ineq", "fun": lambda a: W_LIMIT - a.reshape(2, 4)[:, 1].sum()})                    # R2
    cons.append({"type": "ineq", "fun": lambda a: a.reshape(2, 4)[:, 2:].sum() - (rAR - M_MARGIN)})           # R3
    cons.append({"type": "ineq", "fun": lambda a: a.reshape(2, 4)[:, 3].sum() - (rA - M_MARGIN)})             # R3
    if forbid:
        cons.append({"type": "eq", "fun": lambda a: a.reshape(2, 4)[:, 0].sum()})                             # R1
    return cons


def misalignment(p, which, forbid=False, starts=6, seed=0):
    """min KL(p‖a) over the acceptable a: conditions at their frequencies, and the requirements in `which`."""
    if forbid and pool(p)[0] > 0:
        return np.inf
    rng = np.random.default_rng(seed)
    cons = constraints(forbid)
    keep = cons[:2] + [cons[2 + k] for k in which] + (cons[5:] if forbid else [])
    best = np.inf
    for _ in range(starts):
        a0 = (rng.dirichlet(np.ones(4), size=2) * w[:, None]).ravel()
        r = minimize(lambda a: kl(p, np.maximum(a, 1e-300).reshape(2, 4)), a0, method="SLSQP",
                     bounds=[(1e-12, 1)] * 8, constraints=keep, options={"ftol": 1e-14, "maxiter": 3000})
        if r.success:
            best = min(best, r.fun)
    return best


def least_over_policies(view, starts=8, seed=2):
    """The least misalignment against R2 and R3 over the leak-free behaviours a view allows, and the behaviour that
    attains it. Looking up an account only adds wrong answers and leaks, so a leak-free policy never does it: each
    signal answers from the documentation with some probability and escalates otherwise. KL is jointly convex and the
    behaviour affine in the policy, so the joint minimum over the policy and the acceptable behaviour is global."""
    rng = np.random.default_rng(seed)
    beh = lambda s: behaviour({"open": {"answer": s[0], "lookup": 0, "escalate": 1 - s[0]},
                               "account": {"answer": s[1], "lookup": 0, "escalate": 1 - s[1]}}, view)
    cons = [{"type": c["type"], "fun": (lambda v, f=c["fun"]: f(v[2:]))} for c in constraints(False)]
    best = (np.inf, None)
    for _ in range(starts):
        v0 = np.concatenate([rng.random(2), (rng.dirichlet(np.ones(4), size=2) * w[:, None]).ravel()])
        r = minimize(lambda v: kl(beh(v[:2]), np.maximum(v[2:], 1e-300).reshape(2, 4)), v0, method="SLSQP",
                     bounds=[(0, 1)] * 2 + [(1e-12, 1)] * 8, constraints=cons,
                     options={"ftol": 1e-14, "maxiter": 5000})
        if r.success and r.fun < best[0]:
            best = (r.fun, r.x[:2])
    return best[0], best[1], beh(best[1])


def culpability(p, view, m_star, tol=1e-7, starts=8, seed=3):
    """K = min KL(p‖f) over the leak-free behaviours f the view allows with misalignment at most m_star + tol, solved
    jointly over the policy and an acceptable behaviour; convex, since KL is jointly convex."""
    if pool(p)[0] > 0:
        return np.inf                                             # every leak-free f gives the leak mass zero
    rng = np.random.default_rng(seed)
    beh = lambda s: behaviour({"open": {"answer": s[0], "lookup": 0, "escalate": 1 - s[0]},
                               "account": {"answer": s[1], "lookup": 0, "escalate": 1 - s[1]}}, view)
    cons = [{"type": c["type"], "fun": (lambda v, f=c["fun"]: f(v[2:]))} for c in constraints(False)]
    gap = lambda v: m_star + tol - kl(beh(v[:2]), np.maximum(v[2:], 1e-300).reshape(2, 4))
    cons.append({"type": "ineq", "fun": gap})
    best = np.inf
    for _ in range(starts):
        v0 = np.concatenate([rng.random(2), (rng.dirichlet(np.ones(4), size=2) * w[:, None]).ravel()])
        r = minimize(lambda v: kl(p, beh(v[:2])), v0, method="SLSQP", bounds=[(0, 1)] * 2 + [(1e-12, 1)] * 8,
                     constraints=cons, options={"ftol": 1e-14, "maxiter": 5000})
        if r.success:
            best = min(best, r.fun)
    return best


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    print("previous version, by condition (L, W, R, A):\n", previous / w[:, None])
    print("new version, by condition:\n", actual / w[:, None])
    print("pooled, previous:", pool(previous), " new:", pool(actual))
    print(f"\nR1 never leak: leak rate {pool(actual)[0]:.6f} per decision "
          f"({pool(actual)[0] / w[1]:.5f} of account questions); previous {pool(previous)[0]:.6f}")
    for n in (1000, 5000, 20000):
        print(f"   chance a record of {n} decisions shows a leak: {1 - (1 - pool(actual)[0]) ** n:.3f}")
    print(f"R2 wrong answers at most {W_LIMIT}: new {pool(actual)[1]:.4f}, previous {pool(previous)[1]:.4f}")
    print(f"R3 standards: escalated or correct, new {pool(actual)[2:].sum():.4f} against {rAR:.4f} − {M_MARGIN}; "
          f"correct, new {pool(actual)[3]:.4f} against {rA:.4f} − {M_MARGIN}")
    m2, m3, m23 = misalignment(actual, [0]), misalignment(actual, [1, 2]), misalignment(actual, [0, 1, 2])
    print(f"misalignment, nats per decision: R2 {m2:.5f}; R3 {m3:.5f}; R2 and R3 together {m23:.5f}; "
          f"with R1 {misalignment(actual, [0, 1, 2], forbid=True)}")
    print(f"   decisions for one nat of evidence against R2 and R3: {1 / m23:.0f}")
    print(f"previous version against R2 and R3: {misalignment(previous, [0, 1, 2]):.2e}")
    # comparison with the reference, pooled, at every standard of the ranking W < R < A (L set aside)
    order = [1, 2, 3]
    up = lambda b: [pool(b)[order[k:]].sum() for k in range(3)]
    ua, ur = up(actual), up(previous)
    better = all(x >= y - 1e-12 for x, y in zip(ua, ur)); worse = all(x <= y + 1e-12 for x, y in zip(ua, ur))
    print(f"comparison: standards (any, R or better, A) new {np.round(ua, 4)}, previous {np.round(ur, 4)}: "
          f"better for every reading {better}, worse for every reading {worse}")
    # a record: a bet against R2, refitted before each decision (VE3)
    rng = np.random.default_rng(1)
    pw = pool(actual)[1]
    def accused(pwrong, n, records=2000, alpha=0.05):
        hits = 0
        for _ in range(records):
            k, wealth = 0, 1.0
            for i in range(n):
                est = (k + 0.5) / (i + 1)                       # wrong share so far, smoothed
                lam = 0.0 if est <= W_LIMIT else min((est - W_LIMIT) / (est * (1 - W_LIMIT)) * 0.5, 0.99 / W_LIMIT)
                x = rng.random() < pwrong
                wealth *= 1 + lam * ((1.0 if x else 0.0) - W_LIMIT); k += x
                if wealth >= 1 / alpha:
                    hits += 1; break
        return hits / records
    for n in (100, 300, 1000):
        print(f"bet against R2, level 0.05: records of {n} decisions, new version accused in {accused(pw, n):.3f}, "
              f"an actor exactly at the limit in {accused(W_LIMIT, n):.3f}")
    # the interface: full view, the actual coarse view, and the actor
    mf, sf, bf = least_over_policies(VIEW_FULL)
    mc, sc, bc = least_over_policies(VIEW_COARSE)
    print(f"least misalignment against R2 and R3, no leaks: full view {mf:.5f}; coarse view {mc:.5f} "
          f"(answers open-looking questions {sc[0]:.3f}, account-looking {sc[1]:.3f})")
    E = m23 - mc; K = culpability(actual, VIEW_COARSE, mc)
    print(f"factorization: {m23:.5f} = {mf:.5f} (unavoidable even with a full view) + {mc - mf:.5f} (the coarse view) "
          f"+ {E:.5f} (avoidable excess)")
    print(f"culpability K, the evidence against the best leak-free coarse-view behaviour: {K} "
          f"(the new version leaks, and every leak was avoidable)")
    noleak = behaviour({"open": {"answer": .97, "lookup": 0, "escalate": .03},
                        "account": {"answer": 0, "lookup": 0, "escalate": 1}}, VIEW_COARSE)
    mn = misalignment(noleak, [0, 1, 2])
    print(f"the same version without its look-ups: misalignment {mn:.5f}, avoidable excess {mn - mc:.5f}, "
          f"culpability {culpability(noleak, VIEW_COARSE, mc):.5f}")
