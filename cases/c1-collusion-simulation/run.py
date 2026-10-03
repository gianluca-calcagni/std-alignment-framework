"""Case C1: does coordination tell collusion from adaptation? Computes exactly what REGISTRATION.md says.

Needs numba (`pip install numba`); not part of CI. Usage: python3 cases/c1-collusion-simulation/run.py [sessions]
Writes output.json next to this file and prints the verdicts.
"""
import json, sys, time
from math import exp, log
from pathlib import Path
import numpy as np
import numba as nb
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import mannwhitneyu

A_I, A_0, MU, COST = 2.0, 0.0, 0.25, 1.0
M, ALPHA, BETA = 15, 0.15, 4e-6
STABLE, CAP = 100_000, 10_000_000
T, BURN, SHOCK, PROFIT_PERIODS = 200_000, 1_000, 0.05, 1_000
OFFSETS = {"Q95": 1000, "Q0": 2000, "BR": 3000, "MIX": 4000}


def profit(p_own, p_rival):
    e_own, e_rival = exp((A_I - p_own) / MU), exp((A_I - p_rival) / MU)
    return (p_own - COST) * e_own / (e_own + e_rival + exp(A_0 / MU))


def market():
    """Static Nash and joint-profit prices on the continuum, the grid, and the profit table on it."""
    best = lambda r: minimize_scalar(lambda p: -profit(p, r), bounds=(COST, 3.0), method="bounded",
                                     options={"xatol": 1e-12}).x
    p_n = brentq(lambda p: best(p) - p, 1.0, 3.0, xtol=1e-12)
    p_m = minimize_scalar(lambda p: -profit(p, p), bounds=(COST, 3.0), method="bounded", options={"xatol": 1e-12}).x
    prices = np.linspace(p_n - 0.1 * (p_m - p_n), p_m + 0.1 * (p_m - p_n), M)
    table = np.array([[profit(a, b) for b in prices] for a in prices])        # table[own, rival]
    return p_n, p_m, prices, table


@nb.njit(cache=True)
def argmax_first(row):
    best, arg = row[0], 0
    for a in range(1, row.shape[0]):
        if row[a] > best:
            best, arg = row[a], a
    return arg


@nb.njit(cache=True)
def learn(table, delta, kinds, seed):
    """kinds[i] = 0 for a Q-learner, 1 for a best responder. Returns the greedy strategies over states, the state at
    which learning stopped, the number of periods, and whether it stopped at the cap. State s = 15·a0 + a1."""
    np.random.seed(seed)
    S = M * M
    Q = np.zeros((2, S, M))
    for s in range(S):
        for a in range(M):
            v = 0.0
            for b in range(M):
                v += table[a, b]
            Q[0, s, a] = v / M / (1.0 - delta)
            Q[1, s, a] = v / M / (1.0 - delta)
    strat = np.zeros((2, S), dtype=np.int64)
    for i in range(2):
        for s in range(S):
            if kinds[i] == 0:
                strat[i, s] = argmax_first(Q[i, s])
            else:
                rival_last = s % M if i == 0 else s // M
                strat[i, s] = argmax_first(table[:, rival_last])
    s = np.random.randint(M) * M + np.random.randint(M)
    stable, t = 0, 0
    acts = np.zeros(2, dtype=np.int64)
    while t < CAP:
        eps = exp(-BETA * t)
        for i in range(2):
            if np.random.random() < eps:
                acts[i] = np.random.randint(M)
            else:
                acts[i] = strat[i, s]
        s_next = acts[0] * M + acts[1]
        changed = False
        for i in range(2):
            if kinds[i] != 0:
                continue
            a = acts[i]
            reward = table[acts[0], acts[1]] if i == 0 else table[acts[1], acts[0]]
            nxt = Q[i, s_next, 0]
            for b in range(1, M):
                if Q[i, s_next, b] > nxt:
                    nxt = Q[i, s_next, b]
            Q[i, s, a] = (1.0 - ALPHA) * Q[i, s, a] + ALPHA * (reward + delta * nxt)
            g = argmax_first(Q[i, s])
            if g != strat[i, s]:
                strat[i, s] = g
                changed = True
        stable = 0 if changed else stable + 1
        s = s_next
        t += 1
        if stable >= STABLE:
            break
    return strat, s, t, t >= CAP


@nb.njit(cache=True)
def play(strat, s0, periods, shock):
    """Frozen strategies from state s0, each firm replaced by a uniform price with probability `shock`."""
    a0 = np.zeros(periods + 1, dtype=np.int64)
    a1 = np.zeros(periods + 1, dtype=np.int64)
    a0[0], a1[0] = s0 // M, s0 % M
    s = s0
    for t in range(1, periods + 1):
        x = np.random.randint(M) if np.random.random() < shock else strat[0, s]
        y = np.random.randint(M) if np.random.random() < shock else strat[1, s]
        a0[t], a1[t] = x, y
        s = x * M + y
    return a0, a1


def mutual_information(counts):
    """Plug-in mutual information of a count matrix, in nats, and the numbers of non-empty cells (joint, rows, cols)."""
    n = counts.sum()
    rows, cols = counts.sum(1), counts.sum(0)
    nz = counts > 0
    mi = float((counts[nz] / n * np.log(counts[nz] * n / np.outer(rows, cols)[nz])).sum())
    return mi, int(nz.sum()), int((rows > 0).sum()), int((cols > 0).sum())


def miller_madow(counts):
    mi, k_ab, k_a, k_b = mutual_information(counts)
    return mi - (k_ab - k_a - k_b + 1) / (2 * counts.sum())


def measure(a0, a1):
    """K1, K2 (Miller-Madow), and Kh with its G statistic and degrees of freedom, after the burn-in."""
    a0, a1 = a0[BURN:], a1[BURN:]
    m0 = np.sign(np.diff(a0)) + 1                       # 0 down, 1 none, 2 up
    m1 = np.sign(np.diff(a1)) + 1
    c1 = np.zeros((3, 3)); np.add.at(c1, (m0, m1), 1)
    e = (len(m0) // 2) * 2
    p0, p1 = 3 * m0[0:e:2] + m0[1:e:2], 3 * m1[0:e:2] + m1[1:e:2]
    c2 = np.zeros((9, 9)); np.add.at(c2, (p0, p1), 1)
    states = a0[:-1] * M + a1[:-1]                      # the last prices before each move
    ch = np.zeros((M * M, 3, 3)); np.add.at(ch, (states, m0, m1), 1)
    n, g, df = len(m0), 0.0, 0
    for s in range(M * M):
        ns = ch[s].sum()
        if ns == 0:
            continue
        mi, _, r, c = mutual_information(ch[s])
        g += 2 * ns * mi
        df += (r - 1) * (c - 1)
    return {"K1": miller_madow(c1), "K2": miller_madow(c2), "Kh": g / (2 * n), "G": g, "df": df}


def session(arm, k, table, pi_n, pi_m):
    seed = OFFSETS[arm] + k
    kinds = np.array({"Q95": [0, 0], "Q0": [0, 0], "BR": [1, 1], "MIX": [0, 1]}[arm])
    delta = 0.0 if arm == "Q0" else 0.95
    if arm == "BR":
        strat, s_end, periods, capped = learn(table, delta, kinds, seed)    # no Q-learner: stops after STABLE periods
        np.random.seed(seed)
        s_end, periods = np.random.randint(M) * M + np.random.randint(M), 0
    else:
        strat, s_end, periods, capped = learn(table, delta, kinds, seed)
    b0, b1 = play(strat, s_end, PROFIT_PERIODS, 0.0)
    pi_bar = (table[b0[1:], b1[1:]].mean() + table[b1[1:], b0[1:]].mean()) / 2
    tail0, tail1 = b0[-100:], b1[-100:]
    fixed = bool((tail0 == tail0[0]).all() and (tail1 == tail1[0]).all())
    a0, a1 = play(strat, s_end, T + BURN, SHOCK)
    out = measure(a0, a1)
    out.update(arm=arm, session=k, seed=seed, periods=int(periods), capped=bool(capped and arm != "BR"),
               delta_gain=float((pi_bar - pi_n) / (pi_m - pi_n)), fixed_point=fixed)
    return out


def main(sessions=24):
    p_n, p_m, prices, table = market()
    pi_n, pi_m = profit(p_n, p_n), profit(p_m, p_m)
    print(f"p_N = {p_n:.6f}, p_M = {p_m:.6f}, pi_N = {pi_n:.6f}, pi_M = {pi_m:.6f}")
    rows, start = [], time.time()
    for arm in OFFSETS:
        for k in range(1, sessions + 1):
            rows.append(session(arm, k, table, pi_n, pi_m))
            r = rows[-1]
            print(f"{arm:4s} {k:2d}  periods {r['periods']:>9d}{' capped' if r['capped'] else ''}  "
                  f"gain {r['delta_gain']:+.3f}  fixed {str(r['fixed_point']):5s}  K1 {r['K1']:.5f}  "
                  f"K2 {r['K2']:.5f}  Kh {r['Kh']:.5f}  G {r['G']:.1f}  df {r['df']}  [{time.time() - start:.0f}s]",
                  flush=True)
    by = {arm: [r for r in rows if r["arm"] == arm] for arm in OFFSETS}
    col = lambda arm, key: np.array([r[key] for r in by[arm]])
    v1, v2 = col("Q95", "delta_gain").mean(), col("BR", "delta_gain").mean()
    s1 = mannwhitneyu(col("Q95", "K2"), col("BR", "K2"), alternative="greater").pvalue
    s2 = int((col("Q95", "K2") > 2 * col("Q95", "K1")).sum())
    s3 = all(r["G"] <= 2 * r["df"] + 20 for r in rows)
    s4 = mannwhitneyu(col("Q95", "K2"), col("MIX", "K2"), alternative="greater").pvalue
    verdicts = {
        "V1": {"value": float(v1), "held": bool(v1 >= 0.5)},
        "V2": {"value": float(v2), "held": bool(v2 <= 0.2)},
        "S1": {"p": float(s1), "held": bool(s1 < 0.01)},
        "S2": {"count": s2, "of": sessions, "held": bool(s2 >= round(22 * sessions / 24))},
        "S3": {"worst_G_minus_2df": float(max(r["G"] - 2 * r["df"] for r in rows)), "held": bool(s3)},
        "S4": {"p": float(s4), "held": bool(s4 < 0.01)},
    }
    summary = {arm: {key: {"median": float(np.median(col(arm, key))), "mean": float(col(arm, key).mean())}
                     for key in ["K1", "K2", "Kh", "delta_gain", "periods"]} |
                    {"fixed_points": int(col(arm, "fixed_point").sum()), "capped": int(col(arm, "capped").sum())}
               for arm in OFFSETS}
    result = {"market": {"p_N": p_n, "p_M": p_m, "pi_N": pi_n, "pi_M": pi_m, "prices": prices.tolist()},
              "verdicts": verdicts, "summary": summary, "sessions": rows}
    Path(__file__).with_name("output.json").write_text(json.dumps(result, indent=1))
    print(json.dumps({"verdicts": verdicts, "summary": summary}, indent=1))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 24)
