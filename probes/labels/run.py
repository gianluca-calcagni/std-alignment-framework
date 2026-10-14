"""L1: the framework's labels against what their words mean, on the paradigm cases of REGISTRATION.md (pushed before
this script was first run). Computes each case's quantity with the library `stdalign`, checks the registered
prediction, and compares the framework's verdict with the sense's. Exact: no sampling, no seed. Run from the
repository's root: python3 probes/labels/run.py   (a second)
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import stdalign as sa                                                                    # noqa: E402
from stdalign.diagnostics import outer_misalignment, tampering, pairs, drift            # noqa: E402

POS, ZERO = 1e-6, 1e-9
q = np.full(4, 0.25)
F = np.array([0.0, 1.0, 2.0, 3.0])
G = np.array([1.0, -1.0, -1.0, 1.0])
b4 = np.array([((x + 1) ** 4 - x ** 4) / 4 ** 4 for x in range(4)])


def isotonic(y, w):
    """Weighted least-squares non-decreasing fit (pool adjacent violators), as in checks/test_misalignment.py."""
    out = []
    for s, ww in zip(y * w, w):
        out.append([s, ww, 1])
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            s2, w2, k2 = out.pop(); out[-1][0] += s2; out[-1][1] += w2; out[-1][2] += k2
    return np.concatenate([[s / ww] * k for s, ww, k in out])


def M(p):
    return sa.misalignment(p, q, F)


def M_ord(p):
    """[P36](ii): the divergence to the q-weighted isotonic fit of the ratio, on the levels of F (distinct here)."""
    return sa.kl(p, q * isotonic(p / q, q))


def sign(v):
    return "positive" if v > POS else "zero" if abs(v) < ZERO else "unresolved"


rows = []


def case(cid, value, predicted, sense, framework_says, quantity):
    """`framework_says` maps the computed sign to the framework's yes/no for the label; `sense` is the registered one."""
    got = sign(value)
    held = (predicted is None) or (got == predicted)
    verdict = framework_says(got)
    rows.append((cid, quantity, value, predicted or "not predicted", held, sense, verdict,
                 "agree" if verdict == sense else "DISAGREE"))


def pg(steps=20, eta=0.5):
    theta = np.zeros(4)
    for _ in range(steps):
        p = np.exp(theta - theta.max()); p /= p.sum()
        theta = theta + eta * p * (F - p @ F)
    p = np.exp(theta - theta.max())
    return p / p.sum()


yes_if_pos = lambda s: "yes" if s == "positive" else "no"
yes_if_zero = lambda s: "yes" if s == "zero" else "no"

# L1 pursuit: on the ray iff the distance to the ray, M, is zero
case("L1a", M(sa.pursuit(q, F, 1)), "zero", "yes", yes_if_zero, "distance to R_F")
case("L1b", M(b4), "positive", "yes", yes_if_zero, "distance to R_F")
case("L1c", M(q), "zero", "no", yes_if_zero, "distance to R_F")
case("L1d", M(sa.pursuit(q, F ** 2, 1)), "positive", "yes", yes_if_zero, "distance to R_F")

# L2 misalignment (M and M_ord), and "aligned" for M = 0
for cid, p, sense, pm, po in [("L2a", sa.pursuit(q, -F, 1), "yes", "positive", "positive"),
                              ("L2b", sa.pursuit(q, G, 1), "yes", "positive", "positive"),
                              ("L2c", b4, "no", "positive", "zero"),
                              ("L2d", sa.pursuit(q, F, 5), "no", "zero", "zero"),
                              ("L2e", pg(), "no", "positive", None)]:
    case(cid, M(p), pm, sense, yes_if_pos, "M")
    case(cid + "-ord", M_ord(p), po, sense, yes_if_pos, "M_ord")
case("L2f", M(q), "zero", "no", yes_if_zero, "M (is it 'exactly aligned'?)")
case("L2f-ord", M_ord(q), "zero", "no", yes_if_zero, "M_ord (is it 'exactly aligned'?)")

# L3 outer misalignment at intensity 1, and its ordinal version
for cid, Fh, sense, po, pord in [("L3a", F, "no", "zero", "zero"), ("L3b", 2 * F + 3, "no", "zero", "zero"),
                                  ("L3c", np.exp(F), "no", "positive", "zero"), ("L3d", G, "yes", "positive", "positive")]:
    case(cid, outer_misalignment(q, F, Fh, 1.0), po, sense, yes_if_pos, "O(1)")
    case(cid + "-ord", M_ord(sa.pursuit(q, Fh, 1)), pord, sense, yes_if_pos, "M_ord of the trainer's optimum")

# L4 inner misalignment, with the evaluator F
case("L4a", M(sa.pursuit(q, G, 1)), "positive", "yes", yes_if_pos, "M_T")
case("L4b", M(b4), "positive", "no", yes_if_pos, "M_T")
case("L4c", M(sa.pursuit(q, F, 0.1)), "zero", "no", yes_if_pos, "M_T")

# L5 tampering: worlds as rows, signals as columns; K(s|w)
K = np.array([[0.8, 0.2], [0.2, 0.8]])
qWS = pairs([0.5, 0.5], K)
q_w_given_s = qWS / qWS.sum(0)                                   # columns: q(w | s)
p_sel1 = 1 - qWS.sum(0)[0] ** 4                                  # best-of-4 picks a signal 1 unless all four read 0
best4 = np.column_stack([(1 - p_sel1) * q_w_given_s[:, 0], p_sel1 * q_w_given_s[:, 1]])
case("L5a", tampering(np.array([[0.0, 0.5], [0.0, 0.5]]), K), "positive", "yes", yes_if_pos, "T")
case("L5b", tampering(pairs([0.1, 0.9], K), K), "zero", "no", yes_if_pos, "T")
case("L5c", tampering(best4, K), "positive", "no", yes_if_pos, "T")

# L6 fake alignment: the label applies by [P37](ii)'s hypotheses; the ratio is what it predicts
own = sa.pursuit(q, G, 1); evaluated = sa.tilt(own, 10 * F)
ratio = M(evaluated) / M(own)
case("L6a", 0.01 - ratio, "positive", "no", lambda s: "yes" if s == "positive" else "no",
     "0.01 − M(evaluation)/M(use)")

# L7 coordination K(p) = KL(p ‖ p_1 ⊗ p_2)
def coordination(J):
    J = np.asarray(J, dtype=float)
    return sa.kl(J.ravel(), np.outer(J.sum(1), J.sum(0)).ravel())
case("L7a", coordination([[0.5, 0], [0, 0.5]]), "positive", "yes", yes_if_pos, "K")
case("L7b", coordination([[0.25, 0.25], [0.25, 0.25]]), "zero", "no", yes_if_pos, "K")
case("L7c", coordination([[0.7, 0], [0, 0.3]]), "positive", "no", yes_if_pos, "K")
case("L7d", max(coordination([[0, 0], [0, 1.0]]), coordination([[1.0, 0], [0, 0]])), "zero", "no", yes_if_pos,
     "K in each condition (the larger)")

# L8 drift within a record, δ = (1/n)·Σ_i KL(p_i ‖ p̄)
pA, pB = np.array([0.7, 0.3]), np.array([0.3, 0.7])
case("L8a", drift([(1 - i / 3) * pA + (i / 3) * pB for i in range(4)], np.full(4, 0.25))[0], "positive", "yes", yes_if_pos, "δ")
case("L8b", drift([pA, pB, pA, pB], np.full(4, 0.25))[0], "positive", "no", yes_if_pos, "δ")
case("L8c", drift([pA, pA, pA, pA], np.full(4, 0.25))[0], "zero", "no", yes_if_pos, "δ")

# L9 attention: Σ_c ρ(c)·KL(p_c ‖ p̄), ρ = (½, ½)
att = lambda a, b: drift([np.array(a), np.array(b)], np.full(2, 0.5))[0]
flip_B = np.array([0.95 * 0.2 + 0.05 * 0.8, 0.95 * 0.8 + 0.05 * 0.2])
case("L9a", att([0.9, 0.1], [0.1, 0.9]), "positive", "yes", yes_if_pos, "attention")
case("L9b", att([0.9, 0.1], [0.9, 0.1]), "zero", "no", yes_if_pos, "attention")
case("L9c", att([0.95, 0.05], flip_B), "positive", "no", yes_if_pos, "attention")

# L10 shortfall S = E_{p_{F,λ}}[F] − E_p̂[F], λ the matched intensity ([D5])
def shortfall(p):
    d = sa.kl(p, q)
    if d >= sa.kl(sa.best_outcomes(q, F), q):
        return float(F.max() - p @ F)
    lo, hi = 0.0, 1.0
    while sa.kl(sa.pursuit(q, F, hi), q) < d:
        hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sa.kl(sa.pursuit(q, F, mid), q) < d else (lo, mid)
    return float(sa.pursuit(q, F, hi) @ F - p @ F)
case("L10a", shortfall(sa.pursuit(q, G, 1)), "positive", "yes", yes_if_pos, "S")
case("L10b", shortfall(sa.pursuit(q, F, 1)), "zero", "no", yes_if_pos, "S")
case("L10c", shortfall(q), "zero", "yes", yes_if_pos, "S")

# L11 masking
p1, p2 = sa.pursuit(q, G, 1), sa.pursuit(q, F, 1)
mask = sa.kl(sa.tilt(p1, 10 * F), sa.tilt(p2, 10 * F)) / sa.kl(p1, p2)
case("L11a", 0.01 - mask, "positive", "yes", yes_if_pos, "0.01 − KL after / KL before")

# L12 overoptimization along the pursuit of F̂ = F
ts = np.linspace(0, 20, 2001)
def falls_after_rising(target):
    v = np.array([sa.pursuit(q, F, t) @ target for t in ts])
    run_max = np.maximum.accumulate(v)
    return float(np.max(run_max - v)) if v[1] > v[0] else 0.0
case("L12a", falls_after_rising(np.array([0.0, 1.0, 3.0, 1.0])), "positive", "yes", yes_if_pos, "largest fall")
case("L12b", falls_after_rising(F), "zero", "no", yes_if_pos, "largest fall")

if __name__ == "__main__":
    print(f"{'case':10s} {'quantity':38s} {'value':>12s} {'predicted':>13s} {'held':>5s} {'sense':>5s} "
          f"{'framework':>9s}  label")
    for cid, qty, val, pred, held, sense, verdict, agree in rows:
        print(f"{cid:10s} {qty:38s} {val:12.6g} {pred:>13s} {str(held):>5s} {sense:>5s} {verdict:>9s}  {agree}")
    print(f"\npredictions held: {sum(r[4] for r in rows)} of {len(rows)}; label disagreements: "
          f"{sum(r[7] == 'DISAGREE' for r in rows)}")
