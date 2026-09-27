"""Usage: t71b_run.py CACHE [COLUMN] — T7-1b used the April column (D2 fired); T7-1c amendment uses "Arena Elo [Feb".
T7 case 1b: AlpacaEval 2 length bias against Chatbot Arena Elo, per T7-1b preregistration (P1-P5).
Data: tatsu-lab/alpaca_eval @cd543a1 (cached in CACHE by t71_run.py). Prints results."""
import csv, json, os, re, sys, subprocess, numpy as np
from scipy.stats import spearmanr, rankdata
sys.path.insert(0, '.')
from verify import KL, KLl, lgibbs, _mfree_mm, _mbud_card, _that_full
B = "https://raw.githubusercontent.com/tatsu-lab/alpaca_eval/cd543a149df89434d8a54582c0151c0b945c3d20"
CACHE = sys.argv[1]; COL = sys.argv[2] if len(sys.argv) > 2 else "Arena Elo [April"; bp = os.path.join(CACHE, "bench.csv")
if not os.path.exists(bp): subprocess.run(["curl", "-sf", "-o", bp, B + "/notebooks/benchmarks.csv"], check=True)
lb = {r[""]: r for r in csv.DictReader(open(os.path.join(CACHE, "lb.csv")))}
used = {}
for m in lb:
    p = os.path.join(CACHE, m.replace("/", "_") + ".json")
    if not os.path.exists(p): continue
    a = [r for r in json.load(open(p)) if r.get("preference") is not None]
    if abs(np.mean([min(max(r["preference"] - 1, 0), 1) for r in a]) - float(lb[m]["win_rate"])/100) > 0.005: continue
    used[m] = [(min(max(r["preference"] - 1, 0), 1), len(r["output_2"] or "")) for r in a]
cuts = np.quantile([L for v in used.values() for _, L in v], [0.25, 0.5, 0.75])
def counts(recs):
    c = np.full(12, 0.5)
    for v, L in recs: c[(0 if v < 1/3 else 2 if v > 2/3 else 1)*4 + int(np.searchsorted(cuts, L, side='right'))] += 1
    return c
P = {m: (lambda c: c/c.sum())(counts(r)) for m, r in used.items()}
q = np.mean(list(P.values()), axis=0); q /= q.sum(); lq = np.log(q)
lab = np.repeat(np.arange(3), 4); F = np.array([0, .5, 1])[lab]; FG = np.array([0, .5, 1]); qG = np.bincount(lab, q, 3); lqG = np.log(qG)
lbin = np.tile(np.arange(4), 3); mq = q@lbin
res = {}; p1 = 0.0; p2_bad = 0; offpos = 0
for m, ph in P.items():
    pG = np.bincount(lab, ph, 3); W = KL(ph, q) - KL(pG, qG); th = _that_full(pG, lqG, FG)
    off = KLl(np.log(pG), lgibbs(lqG, FG, th)); inten = KLl(lgibbs(lqG, FG, th), lqG) if th < 0 else 0.0
    p1 = max(p1, abs(_mfree_mm(ph, lq, F) - W - off - inten)); offpos += off > 1e-6
    fb, cb = _mbud_card(ph, lq, F), _mbud_card(pG, lqG, FG); Th = np.nan
    if fb[0] is not None and cb[0] is not None:
        Th = KLl(np.log(pG), lgibbs(lqG, FG, fb[1])) - KLl(np.log(pG), lgibbs(lqG, FG, cb[1]))
        if W > 1e-9 and not Th > 0: p2_bad += 1
    res[m] = dict(W=W, sW=W*np.sign(ph@lbin - mq), off=off, inten=inten, Th=Th,
                  D=abs(float(lb[m]["win_rate"]) - float(lb[m]["length_controlled_winrate"])),
                  wr=float(lb[m]["win_rate"]), lc=float(lb[m]["length_controlled_winrate"]), L=float(lb[m]["avg_length"]))
ok = lambda b: "holds" if b else "FAILS"
print(f"models used: {len(res)}; design check: off-ray > 1e-6 for {offpos/len(res):.0%} (needs >= 25%) -> {'passes' if offpos >= 0.25*len(res) else 'FAILS: three-term reading uninformative'}")
print(f"P1 M_free = W + off + intensity: max error {p1:.1e} -> {ok(p1 <= 1e-12)}")
print(f"P2 Theta > 0 where W > 1e-9: exceptions {p2_bad} -> {ok(p2_bad == 0)}")
r3 = spearmanr([r['W'] for r in res.values()], [r['D'] for r in res.values()]).correlation
print(f"P3 Spearman(W, D) = {r3:.3f} over {len(res)} -> {ok(r3 > 0.3)}")
n = lambda s: re.sub(r'[^a-z0-9]', '', s.lower()); elo = {}
for r in csv.DictReader(open(bp)):
    k = [x for x in r if " ".join(x.split()).startswith(COL)][0]
    try: elo[n(r["Model"] or "")] = float((r[k] or "").strip())
    except ValueError: pass
M = [m for m in res if n(m) in elo]
print(f"matched set: {len(M)} models")
if len(M) < 25: print("D2: fewer than 25 matched -> P4, P5 not evaluated"); sys.exit()
E = np.array([elo[n(m)] for m in M]); WR = np.array([res[m]['wr'] for m in M]); J = rankdata(WR) - rankdata(E)
sW = np.array([res[m]['sW'] for m in M]); L = np.array([res[m]['L'] for m in M]); D = np.array([res[m]['D'] for m in M])
with open("70 Project/T7/t71c_table.csv", "w") as f:
    f.write("model,arena_elo,win_rate,lc_win_rate,avg_length,J,sW,W,off_ray,intensity,Theta\n")
    for i, m in enumerate(M):
        r = res[m]; f.write(f"{m},{E[i]},{r['wr']},{r['lc']},{r['L']},{J[i]},{r['sW']:.6f},{r['W']:.6f},{r['off']:.6f},{r['inten']:.6f},{r['Th']:.6f}\n")
r4 = spearmanr(sW, J).correlation; rL = spearmanr(L, J).correlation
print(f"P4 Spearman(sW, J) = {r4:.3f} -> {ok(r4 > 0.3)}")
print(f"P5 Spearman(sW, J) = {r4:.3f} vs Spearman(avg_length, J) = {rL:.3f} -> {ok(r4 > rL)}")
print(f"reported: Spearman(D, J) = {spearmanr(D, J).correlation:.3f}; Spearman(win_rate, Elo) = {spearmanr(WR, E).correlation:.3f}; Spearman(LC, Elo) = {spearmanr([res[m]['lc'] for m in M], E).correlation:.3f}")
print("reported: diagnosis table, largest and smallest J:")
for i in list(np.argsort(-J)[:5]) + list(np.argsort(J)[:5]):
    r = res[M[i]]; print(f"  {M[i][:34]:34s} J={J[i]:+5.1f}  sW={r['sW']:+.4f}  off={r['off']:.4f}  int={r['inten']:.4f}  Theta={r['Th']:.4f}  len={r['L']:.0f}")
