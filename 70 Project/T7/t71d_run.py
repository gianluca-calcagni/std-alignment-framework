"""T7 case 1d, with the T7-1e amendment (winner names the original output in both orders): evaluator length bias on LLMBar, per T7-1d preregistration (P1-P4).
Usage: t71d_run.py REPO  (a clone of github.com/princeton-nlp/LLMBar at commit 900616bff90b6c6c8e1681f7d079250637c55992)."""
import json, subprocess, sys, numpy as np
from scipy.stats import spearmanr
sys.path.insert(0, '.')
from verify import KL, KLl, lgibbs, _mfree_mm, _mbud_card
REPO = sys.argv[1]; COMMIT = "900616bff90b6c6c8e1681f7d079250637c55992"
show = lambda p: json.loads(subprocess.run(["git", "-C", REPO, "show", f"{COMMIT}:{p}"], capture_output=True, text=True, check=True).stdout)
tree = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", COMMIT], capture_output=True, text=True).stdout.split()
SUBS = ["Natural", "Adversarial/Neighbor", "Adversarial/GPTInst", "Adversarial/GPTOut", "Adversarial/Manual"]
cfgs = sorted({p.split("/evaluators/")[1].rsplit("/", 1)[0] for p in tree if p.startswith("Dataset/LLMBar/Natural/evaluators/") and p.endswith("result.json")})
def picks(sub, cfg):
    """per pair: (weight on gold, weight on the longer output), both orders, and the per-order accuracies"""
    out, acc = [], {False: [], True: []}
    for r in show(f"Dataset/LLMBar/{sub}/evaluators/{cfg}/result.json"):
        g = r["label"]; longer = 1 if len(r["output_1"]) > len(r["output_2"]) else 2
        w = {1: 0.0, 2: 0.0}
        cand = [x for x in r["results"] if isinstance(x, dict) and ("swap = False" in x or "swap = True" in x)]
        if not cand: raise subprocess.CalledProcessError(1, "no judgment")   # incomplete configuration
        res = cand[-1]   # Metrics strategies store the generated rubric first
        for sw in (False, True):
            k = f"swap = {sw}"
            if k not in res: continue
            win = str(res[k]["winner"]).strip()
            sel = {"1": 1, "2": 2}.get(win)
            if sel is None: w[1] += 0.25; w[2] += 0.25; acc[sw].append(0.0)   # T7-1e: ties count as not correct in the check
            else: w[sel] += 0.5; acc[sw].append(float(sel == g))
        tot = w[1] + w[2]; out.append((w[g]/tot, w[longer]/tot, g == longer))
    return out, acc
def integrity(sub, cfg, acc):
    st = show(f"Dataset/LLMBar/{sub}/evaluators/{cfg}/statistics.json"); ok = True
    for sw in (False, True):
        if not acc[sw]: continue
        v = st.get(f"correct_{sw}")
        if v is not None:   # stored as "81 / 100 = 81.0"
            a_, b_ = str(v).split("=")[0].split("/"); v = float(a_)/float(b_)
        ok &= v is not None and round(sum(acc[sw])) == round(v*len(acc[sw]))   # T7-1e: exact count
    return ok
data, failed = {}, 0
for cfg in cfgs:
    d = {}; good = True
    for sub in SUBS:
        try: pk, acc = picks(sub, cfg)
        except subprocess.CalledProcessError: good = False; break
        good &= integrity(sub, cfg, acc); d[sub] = pk
    if good: data[cfg] = d
    else: failed += 1
print(f"configurations: {len(cfgs)}; failing the integrity check or incomplete: {failed}; used: {len(data)}")
if failed > 0.1*len(cfgs): print("D2: more than 10 % fail -> stop and re-register"); sys.exit()
adv = [show(f"Dataset/LLMBar/{s}/dataset.json") for s in SUBS[1:]]
dsgn = np.sign(np.mean([len(r[f"output_{3 - r['label']}"]) - len(r[f"output_{r['label']}"]) for a in adv for r in a]))
print(f"trap direction d = {dsgn:+.0f} (adversarial distractors are {'longer' if dsgn > 0 else 'shorter'} on average)")
# cells: (not gold, not longer), (not gold, longer), (gold, not longer), (gold, longer)
def cells(pk):
    c = np.full(4, 0.5); qc = np.zeros(4)
    for wg, wl, gl in pk:   # gl: gold is the longer output
        c[2 + int(gl)] += wg; c[int(not gl)] += 1 - wg
        qc[2 + int(gl)] += 0.5; qc[int(not gl)] += 0.5
    return c/c.sum(), (qc + 0.5)/(qc + 0.5).sum()
F = np.array([0, 0, 1, 1.]); lab = np.array([0, 0, 1, 1]); FG = np.array([0, 1.]); ln = np.array([0, 1, 0, 1])
rows = []; p1 = 0.0; p2_bad = 0
for cfg, d in data.items():
    ph, q = cells(d["Natural"]); lq = np.log(q); pG, qG = np.bincount(lab, ph, 2), np.bincount(lab, q, 2)
    W = KL(ph, q) - KL(pG, qG); p1 = max(p1, abs(_mfree_mm(ph, lq, F) - _mfree_mm(pG, np.log(qG), FG) - W))
    fb, cb = _mbud_card(ph, lq, F), _mbud_card(pG, np.log(qG), FG); Th = np.nan
    if fb[0] is not None and cb[0] is not None:
        Th = KLl(np.log(pG), lgibbs(np.log(qG), FG, fb[1])) - KLl(np.log(pG), lgibbs(np.log(qG), FG, cb[1]))
        if W > 1e-9 and not Th > 0: p2_bad += 1
    R = ph@ln - q@ln; sW = W*np.sign(R)
    A = 1 - np.mean([wg for s in SUBS[1:] for wg, _, _ in d[s]]); nat = np.mean([wg for wg, _, _ in d["Natural"]])
    rows.append((cfg, dsgn*sW, dsgn*R, A, nat, W, Th, _mfree_mm(ph, lq, F)))
with open("70 Project/T7/t71d_table.csv", "w") as f:
    f.write("config,adversarial_error,natural_accuracy,d_sW,d_R,W,Theta,M_free\n")
    for r in rows: f.write(f"{r[0]},{r[3]:.6f},{r[4]:.6f},{r[1]:.6f},{r[2]:.6f},{r[5]:.6f},{r[6]:.6f},{r[7]:.6f}\n")
x = np.array([r[1] for r in rows]); rr = np.array([r[2] for r in rows]); A = np.array([r[3] for r in rows]); nat = np.array([r[4] for r in rows])
ok = lambda b: "holds" if b else "FAILS"
r3 = spearmanr(x, A).correlation; rR = spearmanr(rr, A).correlation
print(f"P1 M_free = M_free^G + W: max error {p1:.1e} -> {ok(p1 <= 1e-12)}")
print(f"P2 Theta > 0 where W > 1e-9: exceptions {p2_bad} -> {ok(p2_bad == 0)}")
print(f"P3 Spearman(d*sW_Natural, adversarial error) = {r3:.3f} over {len(rows)} -> {ok(r3 > 0.3)}")
print(f"P4 {r3:.3f} vs raw Spearman(d*R_Natural, adversarial error) = {rR:.3f} -> {ok(r3 > rR)}")
from scipy.stats import rankdata
def partial(a, b, c):
    a, b, c = rankdata(a), rankdata(b), rankdata(c); res = lambda y: y - np.polyval(np.polyfit(c, y, 1), c)
    return np.corrcoef(res(a), res(b))[0, 1]
print(f"reported: Spearman(Natural accuracy, adversarial error) = {spearmanr(nat, A).correlation:.3f}; partial Spearman(d*sW, A | Natural accuracy) = {partial(x, A, nat):.3f}; same for raw R: {partial(rr, A, nat):.3f}")
print("reported: diagnosis table (Natural), best and worst adversarial error:")
for r in sorted(rows, key=lambda r: r[3])[:5] + sorted(rows, key=lambda r: -r[3])[:5]:
    print(f"  {r[0]:32s} A={r[3]:.3f}  nat_acc={r[4]:.3f}  d*sW={r[1]:+.4f}  d*R={r[2]:+.3f}  W={r[5]:.4f}  Theta={r[6]:.4f}  M_free={r[7]:.4f}")
