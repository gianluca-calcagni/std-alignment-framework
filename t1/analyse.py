import sys, collections, random
sys.path.insert(0, '.')
from routing_data import R, HARD
N = len(R)
sec = lambda i: i[0]
SECNAME = {'A':'AI — specification','B':'AI — inner alignment','C':'AI — generalization','D':'AI — strategic','E':'AI — training pipelines',
           'F':'AI — oversight','G':'AI — multi-agent/systemic','H':'humans — individual','I':'humans — institutional','J':'biology — organism',
           'K':'biology — within-genome','L':'formal results','M':'empirical regularities'}
LAYERS = ['static','statistical','dynamic','strategic','outside-E','outside-X','category','undetermined']
def pct(x): return f"{100*x/N:.1f} %"
out = []
ex = collections.Counter(r[2] for r in R); ly = collections.Counter(r[3] for r in R); lo = collections.Counter(r[1] for r in R)
out.append(("expressibility", {k: ex[k] for k in 'FPN'}))
out.append(("layer", {k: ly[k] for k in LAYERS}))
out.append(("locus", dict(sorted(lo.items()))))
print("N =", N)
for name, d in out: print(name, {k: f"{v} ({pct(v)})" for k, v in d.items()})
print("F+P =", ex['F'] + ex['P'], pct(ex['F'] + ex['P']))
# by section
print("\nby section: F / P / N ; static / statistical / dynamic / strategic / outside-E / outside-X / category")
for s in 'ABCDEFGHIJKLM':
    rs = [r for r in R if sec(r[0]) == s]; e = collections.Counter(r[2] for r in rs); l = collections.Counter(r[3] for r in rs)
    print(f"  {s} {SECNAME[s]:28s} n={len(rs):2d}  F {e['F']:2d} P {e['P']:2d} N {e['N']:2d} | " + " ".join(f"{l[k]:2d}" for k in LAYERS[:-1]))
# N items: justified?
print("\nN items by layer:", collections.Counter(r[3] for r in R if r[2] == 'N'))
# hard cases
print("\nhard cases (a group 'fires' if any item needs a layer other than static or is outside):")
fired = 0
for name, ids in HARD:
    rs = [r for r in R if r[0] in ids]; needs = [r for r in rs if r[3] != 'static']
    f = len(needs) > 0; fired += f
    print(f"  {name:14s} {'FIRES' if f else 'handled'}  ({len(needs)}/{len(rs)} items need a layer or are outside)")
print(f"  fired: {fired} of {len(HARD)} (prediction: >= 8)")
# sensitivity: pessimistic reclassification of generous projections
generous = [r for r in R if r[2] == 'P' and (r[3] in ('outside-X','outside-E') or r[0][0] in 'JK' or r[0] in
            ('B3','B4','D6','F1','F8','F10','F12','H25','I19','I20','I21','I29','D16','M15','D17','M13','M16'))]
pess = ex['F'] + ex['P'] - len(generous)
print(f"\nsensitivity: {len(generous)} projections judged generous; pessimistic F+P = {pess} ({pct(pess)})")
# which layers the non-static items need, as a build-order signal
need = collections.Counter(r[3] for r in R if r[3] != 'static')
print("non-static items by layer (build-order signal):", dict(need.most_common()))
