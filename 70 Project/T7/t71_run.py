"""T7 case 1 (structural): AlpacaEval 2 length bias, against T7-1 preregistration (P1-P5). Data: tatsu-lab/alpaca_eval
@cd543a1, downloaded to CACHE (not committed). Writes t71_counts.csv (derived per-model soft counts) and prints results."""
import csv, json, os, sys, subprocess, numpy as np
from concurrent.futures import ThreadPoolExecutor
from scipy.stats import spearmanr
sys.path.insert(0, '.')
from verify import KL, KLl, lgibbs, _mfree_mm, _mbud_card, _that_full
B = "https://raw.githubusercontent.com/tatsu-lab/alpaca_eval/cd543a149df89434d8a54582c0151c0b945c3d20"
CACHE = sys.argv[1] if len(sys.argv) > 1 else "/tmp/t71"; os.makedirs(CACHE, exist_ok=True)
lbp = os.path.join(CACHE, "lb.csv")
if not os.path.exists(lbp):
    subprocess.run(["curl", "-sf", "-o", lbp, B + "/src/alpaca_eval/leaderboards/data_AlpacaEval_2/weighted_alpaca_eval_gpt4_turbo_leaderboard.csv"], check=True)
lb = {r[""]: r for r in csv.DictReader(open(lbp))}
def fetch(m):
    p = os.path.join(CACHE, m.replace("/", "_") + ".json")
    if not os.path.exists(p):
        subprocess.run(["curl", "-sf", "-o", p, f"{B}/results/{m}/weighted_alpaca_eval_gpt4_turbo/annotations.json"])
    return m, p if os.path.exists(p) else None
with ThreadPoolExecutor(16) as ex: files = dict(ex.map(fetch, lb))
rows, bad, missing = [], [], 0
for m, p in files.items():
    if p is None: missing += 1; continue
    a = json.load(open(p)); c = np.full(4, 0.5)          # cells: (lose,notlonger),(lose,longer),(win,notlonger),(win,longer)
    for r in a:
        if r.get("preference") is None: continue
        w = min(max(r["preference"] - 1, 0), 1); L = int(len(r["output_2"] or "") > len(r["output_1"] or ""))
        c[L] += 1 - w; c[2 + L] += w
    wr = np.mean([min(max(r["preference"] - 1, 0), 1) for r in a if r.get("preference") is not None])
    if abs(wr - float(lb[m]["win_rate"])/100) > 0.005: bad.append(m); continue
    rows.append((m, c, abs(float(lb[m]["win_rate"]) - float(lb[m]["length_controlled_winrate"]))))
print(f"models: {len(lb)} on the leaderboard, {missing} without annotations, {len(bad)} failing the integrity check, {len(rows)} used")
if len(bad) > 0.1*(len(lb) - missing): print("D2: integrity check fails for more than 10 % -> stop"); sys.exit()
with open("70 Project/T7/t71_counts.csv", "w") as f:
    f.write("model,lose_notlonger,lose_longer,win_notlonger,win_longer,D\n")
    for m, c, D in sorted(rows): f.write(f"{m}," + ",".join(f"{x:.4f}" for x in c) + f",{D:.4f}\n")
q = sum(c/c.sum() for _, c, _ in rows); q /= q.sum(); lq = np.log(q); F = np.array([0, 0, 1, 1.])
lab = np.array([0, 0, 1, 1]); qG = np.bincount(lab, q, 2); lqG = np.log(qG); FG = np.array([0, 1.])
res = []; p1 = 0.0; p2_bad = 0; undef = 0
for m, c, D in rows:
    ph = c/c.sum(); pG = np.bincount(lab, ph, 2); W = KL(ph, q) - KL(pG, qG)
    Mf, MfG = _mfree_mm(ph, lq, F), _mfree_mm(pG, lqG, FG); p1 = max(p1, abs(Mf - MfG - W))
    th = _that_full(pG, lqG, FG); off = KLl(np.log(pG), lgibbs(lqG, FG, th)); inten = KLl(lgibbs(lqG, FG, th), lgibbs(lqG, FG, max(th, 0))) if th < 0 else 0.0
    fb, cb = _mbud_card(ph, lq, F), _mbud_card(pG, lqG, FG); Th = np.nan
    if fb[0] is None or cb[0] is None: undef += 1
    else:
        Th = KLl(np.log(pG), lgibbs(lqG, FG, fb[1])) - KLl(np.log(pG), lgibbs(lqG, FG, cb[1]))
        if W > 1e-9 and not Th > 0: p2_bad += 1
    res.append((m, D, W, Mf, off, inten, Th))
D = np.array([r[1] for r in res]); W = np.array([r[2] for r in res]); Mf = np.array([r[3] for r in res]); Th = np.array([r[6] for r in res])
ok = lambda b: "holds" if b else "FAILS"
r3 = spearmanr(W, D).correlation; fin = np.isfinite(Th); r4 = spearmanr(Th[fin], D[fin]).correlation
top = D >= np.quantile(D, 0.9); sh = np.median(W[top]/Mf[top])
print(f"P1 M_free = M_free^G + W: max error {p1:.1e} -> {ok(p1 <= 1e-12)}")
print(f"P2 Theta > 0 where W > 1e-9 ({fin.sum()} models with both budget measures): exceptions {p2_bad} -> {ok(p2_bad == 0)}")
print(f"P3 Spearman(W, D) = {r3:.3f} over {len(res)} models -> {ok(r3 > 0.3)}")
print(f"P4 Spearman(Theta, D) = {r4:.3f} over {fin.sum()} models -> {ok(r4 > 0.3)}")
print(f"P5 median W/M_free over the top decile of D ({top.sum()} models) = {sh:.3f} -> {ok(sh > 0.5)}")
print(f"reported: finest budget measure undefined for {undef} models; q (pooled) = {np.round(q, 4).tolist()}")
print("reported: diagnosis table (W, off-ray, intensity, Theta, M_free), largest and smallest D:")
for r in sorted(res, key=lambda r: -r[1])[:5] + sorted(res, key=lambda r: r[1])[:5]:
    print(f"  {r[0][:38]:38s} D={r[1]:5.2f}  W={r[2]:.4f}  off={r[4]:.4f}  int={r[5]:.4f}  Theta={r[6]:.4f}  M_free={r[3]:.4f}")
