"""T7 case 2d, per T7-2d preregistration (P1-P3): Beshears, Choi, Laibson & Madrian (NBER w12009) Figure 3, Company A,
new hires under a 3% and a 6% automatic-enrollment default. Bars extracted from the PDF's vector geometry by the T7-2c
rule (filled rectangles of a legend colour sitting on the zero line; heights calibrated on the y-axis tick labels).
Usage: t72d_run.py DIR  (DIR holds the PI-supplied PDF, sha256 9b46de36...)."""
import sys, re, numpy as np, pymupdf
from scipy.stats import spearmanr
p = pymupdf.open(sys.argv[1].rstrip('/') + '/30f16858-w12009.pdf')[36]
L = []
for b in p.get_text('dict')['blocks']:
    for l in b.get('lines', []):
        t = ' '.join(s['text'] for s in l['spans']).strip()
        if t: L.append((t, pymupdf.Rect(l['bbox'])))
cap = [r for t, r in L if t == 'Contribution Rate'][0]
xlab = [(t, (r.x0 + r.x1)/2) for t, r in L if re.fullmatch(r'\d+(-\d+)?%', t) and cap.y0 - 20 < r.y0 < cap.y0]
left = min(x for _, x in xlab)
ticks = [(float(t.rstrip('%')), (r.y0 + r.y1)/2) for t, r in L if re.fullmatch(r'\d+(\.\d+)?%?', t) and r.x1 < left - 10 and r.y1 < cap.y0 - 5]
vals, ys = np.array([v for v, _ in ticks]), np.array([y for _, y in ticks]); A = np.polyfit(ys, vals, 1)
r2 = 1 - np.sum((np.polyval(A, ys) - vals)**2)/np.sum((vals - vals.mean())**2); scale = 100.0 if vals.max() > 1 else 1.0
zero = np.roots([A[0], A[1]])[0]
rects = [d for d in p.get_drawings() if d.get('fill') is not None]
series = {"3%": "Hired under automatic enrollment (3% default)", "6%": "Hired under automatic enrollment (6% default)"}
P = {}; ok = r2 > 0.999
for k, s in series.items():
    lab = [r for t, r in L if t == s][0]
    sw = [d for d in rects if abs((d['rect'].y0 + d['rect'].y1)/2 - (lab.y0 + lab.y1)/2) < 6 and lab.x0 - 40 < d['rect'].x1 <= lab.x0 + 1 and d['rect'].width < 30]
    col = tuple(round(x, 3) for x in sw[0]['fill'])
    bars = [d['rect'] for d in rects if tuple(round(x, 3) for x in d['fill']) == col and d['rect'].height > 0.2 and d['rect'].width < 40 and abs(d['rect'].y1 - zero) <= 3]
    v = {b: 0.0 for b, _ in xlab}
    for r in bars: v[min(xlab, key=lambda t: abs(t[1] - (r.x0 + r.x1)/2))[0]] += (np.polyval(A, r.y0) - np.polyval(A, r.y1))/scale
    P[k] = v; tot = sum(v.values()); good = abs(tot - 1) <= 0.03; ok &= good
    print(f"series {k} default: sum={tot:.4f} tick-fit R2={r2:.6f} -> {'ok' if good else 'FAILS integrity'}")
if not ok: print("D2: integrity check fails -> stop and re-register"); sys.exit()
with open("70 Project/T7/t72d_figure3.csv", "w") as fh:
    fh.write("bin,default_3pct,default_6pct\n"); [fh.write(f"{b},{P['3%'][b]:.5f},{P['6%'][b]:.5f}\n") for b, _ in xlab]
mid = {"0%": 0, "1-2%": 1.5, "4-5%": 4.5, "7-10%": 8.5, "11-15%": 13}
bins = [b for b in mid if b in P["3%"] and (P["3%"][b] >= 0.01 or P["6%"][b] >= 0.01)]
l = {b: np.log((P["6%"][b] + .005)/(P["3%"][b] + .005)) for b in bins}; r = {b: abs(mid[b] - 3) - abs(mid[b] - 6) for b in bins}
okf = lambda x: "holds" if x else "FAILS"
rho = spearmanr([l[b] for b in bins], [r[b] for b in bins]).correlation
print(f"test bins: {bins}")
print(f"P1 Spearman(l(x), r(x)) = {rho:.3f} over {len(bins)} bins -> {okf(rho > 0.5)}")
if "4-5%" in l and "1-2%" in l: print(f"P2 l(4-5%) = {l['4-5%']:+.3f} > l(1-2%) = {l['1-2%']:+.3f} -> {okf(l['4-5%'] > l['1-2%'])}")
dev = max(abs(v - np.mean(list(l.values()))) for v in l.values())
print(f"P3 max |l(x) - mean| = {dev:.3f} vs log 1.5 = {np.log(1.5):.3f} -> {okf(dev <= np.log(1.5))}")
print("reported: per-bin l(x) (r): " + ", ".join(f"{b} {l[b]:+.2f} ({r[b]:+.0f})" for b in bins))
print("reported: fractions 3% / 6% default: " + ", ".join(f"{b} {P['3%'][b]:.3f}/{P['6%'][b]:.3f}" for b, _ in xlab))
print(f"reported: without the 0% bin, Spearman = {spearmanr([l[b] for b in bins if b != '0%'], [r[b] for b in bins if b != '0%']).correlation:.3f}")
