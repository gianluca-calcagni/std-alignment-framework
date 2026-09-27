"""T7 case 2: retirement-enrolment defaults, per T7-2 preregistration (P1-P3). Data: Choi, Laibson, Madrian & Metrick
(2004), NBER w8651, Table 2 (p. 32), copied from the PDF text layer into t72_table2.csv (PDF sha256 9b152cf0...)."""
import csv, numpy as np
rows = list(csv.DictReader(open("70 Project/T7/t72_table2.csv")))
ks = ["N", "lt", "D", "gt"]; comp, bad = [], 0
for r in rows:
    if not r["before_N"] or not r["after_N"]: continue
    b = np.array([float(r["before_" + k]) for k in ks]); a = np.array([float(r["after_" + k]) for k in ks])
    if abs(b.sum() - 100) > 2 or abs(a.sum() - 100) > 2: bad += 1; continue
    comp.append((r["company"] + " " + r["tenure"], b + 0.5, a + 0.5))
print(f"comparable rows: {len(comp)}; failing the sum check: {bad}")
res = []
for name, b, a in comp:
    dl, dg = np.log(a[1]/b[1]), np.log(a[3]/b[3]); c = (dl + dg)/2
    res.append((name, dl, dg, dl - dg, np.log(a[2]/b[2]) - c, np.log(b[0]/a[0]) + c))
d = np.array([abs(r[3]) for r in res]); null = np.array([(abs(r[1]) + abs(r[2]))/2 for r in res])
ok = lambda x: "holds" if x else "FAILS"
print(f"P1 median |delta| = {np.median(d):.3f} vs log 1.5 = {np.log(1.5):.3f} -> {ok(np.median(d) <= np.log(1.5))}")
print(f"P2 median |delta|/2 = {np.median(d/2):.3f} vs 'active choices unchanged' {np.median(null):.3f} -> {ok(np.median(d/2) < np.median(null))}")
print(f"P3 default pull > 0 and non-participation pull > 0 in every row: {sum(r[4] > 0 and r[5] > 0 for r in res)}/{len(res)} -> {ok(all(r[4] > 0 and r[5] > 0 for r in res))}")
print("reported: per row (Delta_<, Delta_>, delta, pi_D, pi_N):")
for r in res: print(f"  {r[0]:10s} {r[1]:+.3f} {r[2]:+.3f}  delta={r[3]:+.3f}  pi_D={r[4]:+.3f}  pi_N={r[5]:+.3f}")
