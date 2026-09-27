"""T7 case 2b (with the T7-2c amendment: bars sit on the zero line), per T7-2b preregistration (P1-P3): Madrian & Shea (2001) Figure 4C and Choi et al. (2004) Figure 3C,
extracted from the PDFs' vector geometry (bars = filled rectangles; heights calibrated on the y-axis tick labels).
Usage: t72b_run.py DIR  (DIR holds the PI-supplied PDFs: sha256 5d8da983..., 9b152cf0...)."""
import sys, re, csv, numpy as np, pymupdf
from scipy.stats import spearmanr
U = sys.argv[1].rstrip('/') + '/'
FIGS = {  # name: (file, page, y-range of the plot, series labels in legend order, default bin, other-regime default bin)
    "MS_4C": ("00e9c7c7-w7682.pdf", 63, (540, 700), ["WINDOW", "NEW"], "3%", "0%"),
    "CC_3C": ("eebcc573-w8651.pdf", 43, (130, 345), ["Hired before AE", "Hired after AE"], "3%", None)}
def lines(p, y0, y1):
    out = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ' '.join(s['text'] for s in l['spans']).strip()
            if t and y0 <= l['bbox'][1] <= y1: out.append((t, pymupdf.Rect(l['bbox'])))
    return out
rows = []; ok_all = True
for name, (f, pg, (y0, y1), series, dflt, other) in FIGS.items():
    p = pymupdf.open(U + f)[pg - 1]; L = lines(p, y0, y1)
    ticks = [(float(t.rstrip('%')), (r.y0 + r.y1)/2) for t, r in L if re.fullmatch(r'\d+%?', t) and r.x1 < 125]
    xlab = [(t, (r.x0 + r.x1)/2) for t, r in L if re.fullmatch(r'\d+(-\d+)?%', t) and r.y0 > max(y for _, y in ticks)]
    vals, ys = np.array([v for v, _ in ticks]), np.array([y for _, y in ticks]); A = np.polyfit(ys, vals, 1)
    r2 = 1 - np.sum((np.polyval(A, ys) - vals)**2)/np.sum((vals - vals.mean())**2)
    scale = 100.0 if max(vals) > 1 else 1.0
    rects = [d for d in p.get_drawings() if d.get('fill') is not None and y0 <= d['rect'].y0 <= y1]
    colour = {}
    for s in series:   # legend swatch: the filled rectangle just left of the label, on the same line
        lab = [r for t, r in L if t.startswith(s)][0]
        sw = [d for d in rects if abs((d['rect'].y0 + d['rect'].y1)/2 - (lab.y0 + lab.y1)/2) < 6 and lab.x0 - 40 < d['rect'].x1 <= lab.x0 + 1 and d['rect'].width < 30]
        colour[s] = tuple(round(x, 3) for x in sw[0]['fill'])
    for s in series:
        zero = np.roots([A[0], A[1]])[0]   # T7-2c: the y where the calibrated axis reads 0; a bar sits on it
        bars = [d['rect'] for d in rects if tuple(round(x, 3) for x in d['fill']) == colour[s] and d['rect'].height > 0.2 and d['rect'].width < 40
                and abs(d['rect'].y1 - zero) <= 3]
        v = {}
        for r in bars:
            xc = (r.x0 + r.x1)/2; b = min(xlab, key=lambda t: abs(t[1] - xc))[0]
            v[b] = v.get(b, 0) + (np.polyval(A, r.y0) - np.polyval(A, r.y1))/scale
        for b, _ in xlab: rows.append((name, s, b, v.get(b, 0.0)))
        tot = sum(v.values()); good = abs(tot - 1) <= 0.03 and r2 > 0.999; ok_all &= good
        print(f"{name} {s:16s} sum={tot:.4f} tick-fit R2={r2:.6f} -> {'ok' if good else 'FAILS integrity'}")
if not ok_all: print("D2: integrity check fails -> stop and re-register"); sys.exit()
with open("70 Project/T7/t72b_figures.csv", "w") as fh:
    fh.write("figure,series,bin,fraction\n"); [fh.write(f"{a},{b},{c},{d:.5f}\n") for a, b, c, d in rows]
order = lambda b: 0 if b == "0%" else float(re.match(r'\d+', b).group())
res = {}; below_pts = []
for name, (f, pg, yr, series, dflt, other) in FIGS.items():
    no, ae = series
    P = {s: {b: v for n, ss, b, v in rows if n == name and ss == s} for s in series}
    bins = [b for b in P[no] if b not in (dflt, other) and (P[no][b] >= 0.01 or P[ae][b] >= 0.01)]
    lo = [b for b in bins if order(b) < order(dflt)]; hi = [b for b in bins if order(b) > order(dflt)]
    l = {b: np.log((P[ae][b] + .005)/(P[no][b] + .005)) for b in bins}
    dl = np.log((sum(P[ae][b] for b in lo) + .005)/(sum(P[no][b] for b in lo) + .005))
    dg = np.log((sum(P[ae][b] for b in hi) + .005)/(sum(P[no][b] for b in hi) + .005))
    piD = np.log((P[ae][dflt] + .005)/(P[no][dflt] + .005)) - (dl + dg)/2
    res[name] = (dl, dg, dl - dg, piD, l, lo, hi)
    below_pts += [(l[b], order(dflt) - order(b)) for b in lo]
okf = lambda x: "holds" if x else "FAILS"
d = {k: v[2] for k, v in res.items()}
print(f"P1 delta < 0 in both: {', '.join(f'{k} {v:+.3f}' for k, v in d.items())} -> {okf(all(v < 0 for v in d.values()))}")
print(f"P2 delta < -log 1.25 = {-np.log(1.25):.3f} in at least one -> {okf(any(v < -np.log(1.25) for v in d.values()))}")
if len(below_pts) < 3: print(f"P3 untestable: {len(below_pts)} below-default bins in total (fewer than 3), as registered")
else:
    r = spearmanr([a for a, _ in below_pts], [b for _, b in below_pts]).correlation; print(f"P3 Spearman = {r:.3f} -> {okf(r < 0)}")
for k, (dl, dg, dd, piD, l, lo, hi) in res.items():
    print(f"reported {k}: Delta_< {dl:+.3f} (bins {lo}), Delta_> {dg:+.3f} (bins {hi}), |delta| {abs(dd):.3f} vs log 1.5 {np.log(1.5):.3f}, pi_D {piD:+.3f}")
    print("   per-bin log-ratio: " + ", ".join(f"{b} {v:+.2f}" for b, v in sorted(l.items(), key=lambda t: order(t[0]))))
