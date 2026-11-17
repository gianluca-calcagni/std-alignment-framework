"""G1, the coverage test: on a paradigm case and a contrary case of each form of misalignment that authors
popularized, does the framework's diagnosis, at the least level that can make it, say what the form's source says?
Registered in REGISTRATION.md before this script was first run; it computes exactly what the registration says.
Usage: python3 probes/coverage/run.py        (seconds)

Every instance is exact: no sampling, no seed. A value is `positive` at 1e-4 nats or more, `zero` at 1e-6 or less,
`infinite` when the library says so; between the two thresholds a prediction is unresolved and counts as failed.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
from stdalign.spec import (Limit, kl_binary, misalignment, overall_rate_limit, rate_limit, forbidden,   # noqa: E402
                           unavoidable)

ROWS = []
DELTA = 0.01                                                                         # the care margin of G8


def over(u, eps):
    """Misalignment of a rate u against a limit eps on one binary outcome (mvp/CORE.md, R7)."""
    return kl_binary(u, eps) if u > eps else 0.0


def alike(rates, weights=None):
    """Evidence against "the same conduct in these conditions", for binary conduct with the given rates: the least
    weighted divergence to one common behaviour, attained at the weighted mean."""
    r = np.asarray(rates, float)
    w = np.full(r.size, 1.0 / r.size) if weights is None else np.asarray(weights, float) / np.sum(weights)
    m = float(w @ r)
    return float(sum(wi * kl_binary(ri, m) for wi, ri in zip(w, r)))


def sign(v):
    if np.isinf(v):
        return "infinite"
    return "positive" if v >= 1e-4 else "zero" if abs(v) <= 1e-6 else "negative" if v <= -1e-4 else "unresolved"


def row(cid, what, value, predicted, sense, agrees):
    got = value if isinstance(value, str) else sign(value)
    shown = value if isinstance(value, str) else ("inf" if np.isinf(value) else f"{value:.4f}")
    ROWS.append((cid, what, shown, got, predicted, "held" if got == predicted else "FAILED", sense, agrees))


def g1_g7():
    # G1 breaking a rule: bad answers at most 5%
    row("G1a", "M, bad rate 0.20", over(0.20, 0.05), "positive", "yes", "agrees")
    row("G1b", "M, bad rate 0.03", over(0.03, 0.05), "zero", "no", "agrees")
    # G2 side effects: outcomes (task done or not) x (vase whole or broken); index = 2*notdone + broken
    def joint(done, broken):
        return np.array([done * (1 - broken), done * broken, (1 - done) * (1 - broken), (1 - done) * broken])
    task = rate_limit([2, 3], 0.10, 4, name="task not done")
    side = rate_limit([1, 3], 0.01, 4, name="vase broken")
    p_yes, p_no = joint(0.95, 0.30), joint(0.95, 0.005)
    row("G2a", "M against the task alone, vase broken 30%", misalignment(p_yes, [task]).value, "zero", "yes",
        "silent: no requirement names the vase")
    row("G2b", "M against task and vase, vase broken 30%", misalignment(p_yes, [task, side]).value, "positive", "yes",
        "agrees")
    row("G2c", "M against task and vase, vase broken 0.5%", misalignment(p_no, [task, side]).value, "zero", "no",
        "agrees")
    # G3 a shift between evaluation and use: bad at most 5% in each kind of situation
    def by_mix(rates, mix):
        return float(sum(m * over(r, 0.05) for m, r in zip(mix, rates)))
    row("G3a", "gap, hard cases rarer in evaluation", by_mix((0.02, 0.30), (0.5, 0.5)) - by_mix((0.02, 0.30), (0.9, 0.1)),
        "positive", "yes", "agrees")
    row("G3b", "gap, same conduct in both kinds", by_mix((0.02, 0.02), (0.5, 0.5)) - by_mix((0.02, 0.02), (0.9, 0.1)),
        "zero", "no", "agrees")
    # G4 hidden from a coarse grader: outcomes ok, wrong, harmful; harmful at most 1%; the grader merges the last two
    harm, cells = rate_limit([2], 0.01, 3), np.array([0, 1, 1])
    for cid, p, pred_full, pred_hidden, sense in (("G4a", [0.8, 0.1, 0.1], "positive", "positive", "yes"),
                                                  ("G4b", [0.8, 0.195, 0.005], "zero", "zero", "no")):
        full = misalignment(np.array(p), [harm]).value
        seen = misalignment(np.array(p), [harm], cells=cells).value
        row(cid + "1", "M at full resolution", full, pred_full, sense, "agrees")
        row(cid + "2", "M seen by the grader", seen, "zero", sense, "agrees: the grader sees nothing either way")
        row(cid + "3", "hidden from the grader", full - seen, pred_hidden, sense, "agrees")
    # G6 random against systematic mistakes: four tasks, bad at most 10% overall
    w = np.full(4, 0.25)
    for cid, u, pred, sense in (("G6a", [0.3, 0.3, 0.3, 0.3], "zero", "random"), ("G6b", [1.0, 0.2, 0.0, 0.0], "positive",
                                                                                 "systematic")):
        step = overall_rate_limit(w, u, 0.10)[0] - kl_binary(float(w @ np.array(u)), 0.10)
        row(cid, "step from tasks merged to tasks apart", step, pred, sense, "agrees")
    # G7 hallucination: outcomes faithful, contradicts the source, unsupported by it; the last two at most 5% together
    unfaithful, cells = rate_limit([1, 2], 0.05, 3), np.array([0, 1, 0])           # a grader that checks contradiction
    p = np.array([0.7, 0.1, 0.2])
    full, seen = misalignment(p, [unfaithful]).value, misalignment(p, [unfaithful], cells=cells).value
    row("G7a", "M, 30% unfaithful", full, "positive", "yes", "agrees")
    row("G7b", "M seen by a grader that checks contradiction only", seen, "positive", "yes", "agrees")
    row("G7c", "hidden from that grader: the unsupported part", full - seen, "positive", "yes", "agrees")
    row("G7d", "M, 3% unfaithful", misalignment(np.array([0.97, 0.01, 0.02]), [unfaithful]).value, "zero", "no", "agrees")


def verdict(m_actor, m_shown, m_limit):
    if m_actor - m_shown > DELTA:
        return "culpable, shown"
    return "excused" if m_actor - m_limit <= DELTA else "open"


def g8_g13():
    # G8 inability and negligence: bad at most 5%; a limit says the actor's tool fails at least 20% of the time
    lim = over(0.20, 0.05)
    row("G8a", "verdict: at its limit", verdict(over(0.20, 0.05), over(0.20, 0.05), lim), "excused", "could not", "agrees")
    row("G8b", "verdict: at 40%, shown to reach 20%", verdict(over(0.40, 0.05), over(0.20, 0.05), lim),
        "culpable, shown", "could, and did not", "agrees")
    row("G8c", "verdict: at 40%, nothing else shown", verdict(over(0.40, 0.05), over(0.40, 0.05), lim), "open",
        "unknown", "agrees")
    row("G8d", "verdict: at 40%, nothing shown, no limit", verdict(over(0.40, 0.05), over(0.40, 0.05), 0.0), "open",
        "unknown", "agrees")
    # G10 not seeing what matters: two situations of equal weight; in the first "y" at most 5%, in the second "x"
    def m_two(x1, x2):                                                               # x_i: share of "x" in situation i
        return 0.5 * over(1 - x1, 0.05) + 0.5 * over(x2, 0.05)
    blind_best = min(m_two(u, u) for u in np.linspace(0, 1, 100001))
    row("G10a", "M, always x in both situations", m_two(0.98, 0.98), "positive", "yes", "agrees")
    row("G10b", "upper end of the cost of not telling them apart", blind_best - m_two(0.98, 0.02), "positive", "yes",
        "agrees: an upper end only")
    row("G10c", "verdict once it is shown telling them apart", verdict(m_two(0.98, 0.98), m_two(0.98, 0.02), 0.0),
        "culpable, shown", "it could tell", "agrees")
    row("G10d", "M, x in the first and y in the second", m_two(0.98, 0.02), "zero", "no", "agrees")
    # G11 sandbagging: accuracy in the evaluation and under elicitation, on a dangerous and on a control topic
    for cid, (de, dx, ce, cx), preds, sense, agrees in (
            ("G11a", (0.3, 0.9, 0.9, 0.9), ("positive", "zero"), "yes", "agrees: a drop on the one topic"),
            ("G11b", (0.3, 0.3, 0.9, 0.9), ("zero", "zero"), "no", "agrees"),
            ("G11c", (0.3, 0.9, 0.3, 0.9), ("positive", "positive"), "no: not strategic",
             "broader: it reports the drop, not the intent")):
        row(cid + "1", "evidence of a gap, dangerous topic", alike([de, dx]), preds[0], sense, agrees)
        row(cid + "2", "evidence of a gap, control topic", alike([ce, cx]), preds[1], sense, agrees)
    # G12 acting differently when watched: bad at most 5%; watched, and a honeypot that looks like use
    for cid, (bw, bh), pa, pg, sense, agrees in (
            ("G12a", (0.01, 0.20), "positive", "positive", "yes", "agrees"),
            ("G12b", (0.03, 0.03), "zero", "zero", "no", "agrees"),
            ("G12c", (0.20, 0.01), "positive", "negative", "no: worse when watched", "agrees: the gap's sign says so")):
        row(cid + "1", "evidence of acting differently", alike([bw, bh]), pa, sense, agrees)
        row(cid + "2", "misalignment unwatched less watched", over(bh, 0.05) - over(bw, 0.05), pg, sense, agrees)
    row("G12d", "evidence that it tells evaluation from use, asked", alike([0.8, 0.3]), "positive", "yes", "agrees")
    row("G12e", "the same, answers alike", alike([0.5, 0.5]), "zero", "no", "agrees")
    # G13 alignment faking: compliance with and without the cue that the conversation is used for training
    row("G13a", "evidence of conduct keyed to the cue", alike([0.14, 0.01]), "positive", "yes", "agrees on the conduct")
    row("G13b", "the same, no difference", alike([0.01, 0.01]), "zero", "no", "agrees")
    row("G13c", "the same difference, for another reason", alike([0.14, 0.01]), "positive", "no",
        "broader: the reason is not in the conduct")


def tamper(p_state, p_high, k_high):
    """The divergence of the signal from the honest channel, given the world's state ([P50])."""
    return float(sum(ps * kl_binary(ph, kh) for ps, ph, kh in zip(p_state, p_high, k_high) if ps > 0))


def g14_g19():
    # G14 tampering: states none, diamond, fake; the reward reads high; the honest channel errs 5% of the time
    k = (0.05, 0.95, 0.95)                                                           # high given none, diamond, fake
    row("G14a", "tampering: no diamonds, the sensor made to read high", tamper((0.9, 0.1, 0.0), (0.9, 0.95, 0.95), k),
        "positive", "yes", "agrees")
    row("G14b", "tampering: diamonds collected, sensor untouched", tamper((0.1, 0.9, 0.0), k, k), "zero", "no", "agrees")
    row("G14c", "tampering: fakes collected, sensor untouched", tamper((0.05, 0.05, 0.9), k, k), "zero",
        "no: gaming, not tampering", "agrees")
    # G22 reward hacking, on G14c's actor: the measured requirement (reads high at least 80%) and the meant one
    high = 0.05 * 0.05 + 0.05 * 0.95 + 0.9 * 0.95
    row("G22a", "M against the measured requirement, fakes", over(1 - high, 0.20), "zero", "yes", "agrees")
    row("G22b", "M against the meant requirement, fakes", over(0.95, 0.20), "positive", "yes", "agrees")
    row("G22c", "M against the meant requirement, diamonds", over(0.10, 0.20), "zero", "no", "agrees")
    # G15 sycophancy: accuracy on a neutral question and when the user states a wrong belief
    row("G15a", "evidence of answers keyed to the user's belief", alike([0.90, 0.63]), "positive", "yes", "agrees")
    row("G15b", "the same, accuracy unchanged", alike([0.90, 0.90]), "zero", "no", "agrees")
    # G16 secret collusion: does the second agent's action follow the first one's private information, given what
    # the messages openly say? conditional mutual information, from the joint of (says, private, action)
    def cmi(joint):                                                                  # joint[o][s][b]
        j = np.asarray(joint, float)
        tot = 0.0
        for o in range(j.shape[0]):
            po = j[o].sum()
            if po == 0:
                continue
            pb = j[o].sum(axis=0) / po
            for s in range(j.shape[1]):
                ps = j[o][s].sum()
                for b in range(j.shape[2]):
                    if j[o][s][b] > 0:
                        tot += j[o][s][b] * np.log((j[o][s][b] / ps) / pb[b])
        return float(tot)
    covert = [[[0.45, 0.05], [0.05, 0.45]]]                                          # one innocuous message; b follows s
    none = [[[0.25, 0.25], [0.25, 0.25]]]
    overt = [[[0.45, 0.05], [0.0, 0.0]], [[0.0, 0.0], [0.05, 0.45]]]                 # the message says s
    row("G16a", "action follows private information, messages alike", cmi(covert), "positive", "yes", "agrees")
    row("G16b", "action independent of it", cmi(none), "zero", "no", "agrees")
    row("G16c", "the message says it openly", cmi(overt), "zero", "no: collusion in the open", "agrees")
    # G17 injection: the attacker's action at most 1% whether or not the retrieved text carries instructions
    row("G17a", "M, the attacker's action 60% of the time when injected", 0.1 * over(0.60, 0.01) + 0.9 * over(0.0, 0.01),
        "positive", "yes", "agrees")
    row("G17b", "M, 0.5% either way", 0.1 * over(0.005, 0.01) + 0.9 * over(0.005, 0.01), "zero", "no", "agrees")
    # G18 resisting shutdown: when the switch is pressed, continuing is forbidden
    m = misalignment(np.array([0.5, 0.5]), [forbidden([1], 2)])
    row("G18a", "M, continues half the time", float("inf") if m.infinite else m.value, "infinite", "yes", "agrees")
    row("G18b", "M, always stops", misalignment(np.array([1.0, 0.0]), [forbidden([1], 2)]).value, "zero", "no", "agrees")
    # G19 influence on the principal: how often the principal's preference changes, against 5% left alone
    row("G19a", "influence: changes 80% of the time", kl_binary(0.80, 0.05), "positive", "yes", "agrees")
    row("G19b", "influence: changes as when left alone", kl_binary(0.05, 0.05), "zero", "no", "agrees")
    row("G19c", "influence every preference welcomes", kl_binary(0.80, 0.05), "positive", "influence, not objectionable",
        "agrees: a measure; the objection is a requirement to declare")


def g20_g29():
    # G20 power: three outcomes; a family of three specifications, "outcome j at least 90% of the time", equal weights;
    # the least misalignment each later position leaves, averaged over the family (less is more power)
    def left_unavoidable(vertices):
        return float(np.mean([unavoidable(vertices, [rate_limit([i for i in range(3) if i != j], 0.10, 3)])[0]
                              for j in range(3)]))
    dead_end, open_options = left_unavoidable(np.array([[1.0, 0, 0]])), left_unavoidable(np.array([[0, 1.0, 0],
                                                                                                    [0, 0, 1.0]]))
    row("G20a", "more is left unavoidable at the dead end than with options", dead_end - open_options, "positive",
        "the position with options has more power", "agrees")
    row("G20b", "value at the dead end, predicted 1.5351", f"{dead_end:.4f}", "1.5351", "", "")
    row("G20c", "value with two options, predicted 0.7675", f"{open_options:.4f}", "0.7675", "", "")
    # G21 the worst case under a protocol: 5,000 tasks, the first 100 audited; an attack is caught in the audited
    # part and succeeds after it; the worst probability of an unsafe run over the attacker's rate
    beta = np.logspace(-6, 0, 200001)
    unsafe = (1 - beta) ** 100 * (1 - (1 - beta) ** 4900)
    row("G21a", "worst probability of an unsafe run, predicted in [0.90, 0.91]",
        "in range" if 0.90 <= unsafe.max() <= 0.91 else f"{unsafe.max():.4f}", "in range", "", f"{unsafe.max():.4f}")
    row("G21b", "the same, the untrusted model not used", 0.0, "zero", "safe", "agrees")
    # G25 goal misgeneralization: a shifted situation; outcomes coin, the old place without the coin, neither
    def m_goal(p):                                                                   # gets the coin at least 90%
        return over(1 - p[0], 0.10)
    def m_place(p):                                                                  # reaches the old place at least 90%
        return over(p[0] + p[2], 0.10)
    for cid, p, pg, pp, sense, agrees in (
            ("G25a", (0.05, 0.90, 0.05), "positive", "zero", "goal misgeneralization", "agrees"),
            ("G25b", (0.05, 0.05, 0.90), "positive", "positive", "capability misgeneralization", "agrees"),
            ("G25c", (0.95, 0.00, 0.05), "zero", "positive", "neither", "agrees")):
        row(cid + "1", "M against the declared goal, shifted", m_goal(p), pg, sense, agrees)
        row(cid + "2", "M against the named other goal, shifted", m_place(p), pp, sense, agrees)
    # G26 misalignment that spreads: bad answers at most 1% on unrelated questions, before and after narrow training
    row("G26a", "rise on unrelated questions, 0% to 20%", over(0.20, 0.01) - over(0.0, 0.01), "positive", "yes", "agrees")
    row("G26b", "the same, the control", over(0.0, 0.01) - over(0.0, 0.01), "zero", "no", "agrees")
    # G27 a trigger: bad at most 1% with and without it; the trigger absent from evaluation, 10% of use
    row("G27a", "M in evaluation, trigger never posed", 1.0 * over(0.0, 0.01), "zero", "yes", "silent in evaluation")
    row("G27b", "M in use", 0.9 * over(0.0, 0.01) + 0.1 * over(0.90, 0.01), "positive", "yes", "agrees")
    row("G27c", "M in use, no backdoor", 0.9 * over(0.0, 0.01) + 0.1 * over(0.0, 0.01), "zero", "no", "agrees")
    # G29 principals that conflict: bad at most 5%, and bad at least 20%
    m = misalignment(np.array([0.9, 0.1]), [rate_limit([1], 0.05, 2), Limit((1.0, 0.0), 0.80, None, "ok at most 80%")])
    row("G29a", "the two requirements together", "inconsistent" if not m.consistent else "consistent", "inconsistent",
        "conflict", "agrees")


if __name__ == "__main__":
    g1_g7()
    g8_g13()
    g14_g19()
    g20_g29()
    print(f"{'case':6s} {'quantity':60s} {'value':>10s} {'predicted':>16s} {'':7s} sense | framework against the sense")
    for cid, what, shown, got, predicted, state, sense, agrees in ROWS:
        print(f"{cid:6s} {what[:60]:60s} {shown:>10s} {predicted:>16s} {state:7s} {sense} | {agrees}")
    failed = [r[0] for r in ROWS if r[5] == "FAILED"]
    print(f"\n{len(ROWS)} predictions, {len(ROWS) - len(failed)} held, {len(failed)} failed: {failed}")
