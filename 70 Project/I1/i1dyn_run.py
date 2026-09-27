"""I1-dyn (fixed after the first run: bootstrap samples exactly at Hardy-Weinberg have an undefined angle; they are excluded and counted): dynamic rank on Dobzhansky 1947, Tables 3-4 (I1-dyn preregistration + amendment)."""
import numpy as np, warnings
warnings.filterwarnings('ignore')
# counts as resolved under the amendment (ambiguous cells: I6->16, I3->13, IS->15; S=8 only in printed decimals)
data = {"ST/CH (cage 22)": {"young F": [31, 83, 16], "old M": [26, 86, 13]},
        "AR/CH (cage 23)": {"young F": [24, 63, 13], "old M": [22, 63, 15], "young M": [34, 70, 30]}}
printed = {("ST/CH (cage 22)", "young F"): [40.4, 64.1, 25.4], ("ST/CH (cage 22)", "old M"): [38.1, 61.6, 25.1],
           ("AR/CH (cage 23)", "young F"): [30.8, 49.4, 19.8], ("AR/CH (cage 23)", "old M"): [28.6, 49.8, 21.6],
           ("AR/CH (cage 23)", "young M"): [35.5, 66.9, 31.5]}
def hw(c):
    c = np.asarray(c, float); n = c.sum(); p = (2*c[0] + c[1])/(2*n)
    return n*np.array([p*p, 2*p*(1-p), (1-p)**2])
def cent(v, w): return v - w@v
def angle(a, b, e):
    w = e/e.sum(); a, b = cent(a, w), cent(b, w)
    return np.degrees(np.arccos(np.clip((w@(a*b))/np.sqrt((w@(a*a))*(w@(b*b))), -1, 1)))
rng = np.random.default_rng(1947); level = 1 - 0.05/4; ok_all = True; lines = []
for sysname, groups in data.items():
    for g, c in groups.items():
        e = hw(c); assert np.all(np.abs(e - printed[(sysname, g)]) <= 0.6), (sysname, g, e)
        assert min(c) > 0 and sum(c) >= 30
    tot = np.sum([np.asarray(c, float) for c in groups.values()], axis=0); etot = hw(tot)
    lpool = np.log(tot/etot); names = ["hom1", "het", "hom2"]
    top = names[int(np.argmax(cent(lpool, etot/etot.sum())))]
    lines.append(f"{sysname}: pooled centered increment {np.round(cent(lpool, etot/etot.sum()), 3)}; first = {top} -> P2 {'holds' if top == 'het' else 'FAILS'}")
    for g, c in groups.items():
        c = np.asarray(c, float); n = int(c.sum()); e = hw(c); th = angle(np.log(c/e), lpool, e)
        pr = e*np.exp(lpool); pr /= pr.sum(); sims = []
        for _ in range(10000):
            s = rng.multinomial(n, pr).astype(float)
            if s.min() == 0: s += 0.5
            es = hw(s); sims.append(angle(np.log(s/es), lpool, es))
        sims = np.array(sims); und = int(np.isnan(sims).sum()); q = np.nanquantile(sims, level); ok = th <= q; ok_all &= ok
        lines.append(f"   {g}: n {n}, theta {th:.1f} deg, bootstrap {100*level:.2f}th pct {q:.1f} deg -> {'within' if ok else 'EXCEEDS'} (undefined bootstrap angles excluded: {und})")
lines.append(f"P1 one evaluator across sex and age (within sampling): {'holds' if ok_all else 'FAILS'}")
print("\n".join(lines))
