"""I1-dyn2: is the egg-to-young-adult increment of the two sexes rank 1? Dobzhansky (1947), cage 23 (AR/CH).
Pre-registered in 'I1-dyn2 preregistration.md'. Usage: python3 i1dyn2_run.py gate | test"""
import sys, numpy as np
from scipy.optimize import minimize
from scipy.special import xlogy, logsumexp

MIS = 1 / 64  # a heterozygous adult is read as each homozygote with probability 1/64 (six larvae all alike: 1/32)
MOBS = np.array([[1, MIS, 0], [0, 1 - 2 * MIS, 0], [0, MIS, 1]])  # observed class <- true genotype (columns)
E1, E2 = np.array([1., 0, -1]), np.array([-1., 2, -1])  # additive and dominance directions, centered log space
ADULTS = {"young F": [24, 63, 13], "young M": [34, 70, 30]}  # Table 4, cage 23: AR/AR, AR/CH, CH/CH
# Table 2, cage 23, filled in after the gate passed. OCR '8I' -> 81 (amendment rule); both rows match the printed
# Expected row to 0.07 and total 150
EGGS = {"November 1945": [29, 81, 40], "December 1945": [48, 74, 28]}


def norm(lv): return np.exp(lv - logsumexp(lv))
def direction(phi): return np.cos(phi) * E1 + np.sin(phi) * E2
def slog(c): c = np.asarray(c, float) + 0.5; return np.log(c / c.sum())
def coords(v): return np.linalg.lstsq(np.stack([E1, E2], 1), v - v.mean(), rcond=None)[0]


def ll_h0(t, eggs, cf, cm, delta):
    lq = np.array([0., t[0], t[1]]); d = direction(t[2]); base = lq + delta * E1
    return (xlogy(eggs, norm(lq)).sum() + xlogy(cf, MOBS @ norm(base + t[3] * d)).sum()
            + xlogy(cm, MOBS @ norm(base + t[4] * d)).sum())


def grad_h0(t, eggs, cf, cm, delta):
    lq = np.array([0., t[0], t[1]]); q = norm(lq); d = direction(t[2]); dd = -np.sin(t[2]) * E1 + np.cos(t[2]) * E2
    g = np.zeros(5); g[:2] = (eggs - np.sum(eggs) * q)[1:]
    for k, c in ((3, cf), (4, cm)):
        p = norm(lq + delta * E1 + t[k] * d); h = MOBS.T @ (c / (MOBS @ p)); gz = p * h - p * (p @ h)
        g[:2] += gz[1:]; g[2] += t[k] * (dd @ gz); g[k] = d @ gz
    return g


def fit_h0(eggs, cf, cm, delta=0.0, nstart=3):
    le = slog(eggs); uf, um = coords(slog(cf) - le), coords(slog(cm) - le)
    v = np.linalg.svd(np.stack([uf, um], 1))[0][:, 0]; phi0 = np.arctan2(v[1], v[0])
    best, lls = None, []
    for k in range(nstart):
        phi = phi0 + k * np.pi / nstart; w = np.array([np.cos(phi), np.sin(phi)])
        t0 = np.array([le[1] - le[0], le[2] - le[0], phi, uf @ w, um @ w])
        r = minimize(lambda t: -ll_h0(t, eggs, cf, cm, delta), t0, jac=lambda t: -grad_h0(t, eggs, cf, cm, delta), method="BFGS")
        lls.append(-r.fun)
        if best is None or -r.fun > -best.fun: best = r
    return -best.fun, best.x, np.array(lls)


def ll_h1_group(c):
    c = np.asarray(c, float); pt = np.linalg.solve(MOBS, c / c.sum())
    if pt.min() >= 0: return xlogy(c, c / c.sum()).sum()
    r = minimize(lambda t: -xlogy(c, MOBS @ norm(np.array([0., *t]))).sum(), slog(c)[1:] - slog(c)[0], method="BFGS")
    return -r.fun


def lam(eggs, cf, cm, delta=0.0, nstart=3):
    ll1 = xlogy(eggs, np.asarray(eggs, float) / np.sum(eggs)).sum() + ll_h1_group(cf) + ll_h1_group(cm)
    ll0, t, lls = fit_h0(eggs, cf, cm, delta, nstart)
    return 2 * (ll1 - ll0), t, lls


def h0_probs(t, delta=0.0):
    lq = np.array([0., t[0], t[1]]); d = direction(t[2])
    return norm(lq), norm(lq + delta * E1 + t[3] * d), norm(lq + delta * E1 + t[4] * d)


def draw(rng, q, pf, pm, n):
    return rng.multinomial(n[0], q), rng.multinomial(n[1], MOBS @ pf), rng.multinomial(n[2], MOBS @ pm)


def gate():
    rng = np.random.default_rng(1945); n = (150, 100, 134); x0 = 249 / 468
    q = np.array([x0 * x0, 2 * x0 * (1 - x0), (1 - x0) ** 2]); F = np.log([0.7, 1.0, 0.3])
    a = (np.log(0.7) - np.log(0.3)) / 2; lq = np.log(q)
    configs = {"H0a (one evaluator, equal intensity)": (F, F), "H0b (one evaluator, male intensity 0.3)": (F, 0.3 * F),
               "H1 (gate: females F, males additive part only)": (F, a * E1),
               "H1-half (information: males half the additive part)": (F, a / 2 * E1)}
    out, lines = {}, [f"x0 {x0:.4f}; q {np.round(q, 4)}; F = log(0.7, 1, 0.3); additive part a = {a:.4f}"]
    for name, (lf, lm) in configs.items():
        pf, pm = norm(lq + lf), norm(lq + lm); L, neg = [], 0
        for _ in range(2000):
            v, _, _ = lam(*draw(rng, q, pf, pm, n)); neg += v < -1e-6; L.append(max(v, 0.0))
        out[name] = np.array(L)
        lines.append(f"{name}: chi2(1) rejection share {np.mean(out[name] > 3.841):.3f}; 95th pct {np.quantile(out[name], 0.95):.3f}; negative Lambda {neg}")
    k = list(out); c = max(np.quantile(out[k[0]], 0.95), np.quantile(out[k[1]], 0.95))
    power, half = np.mean(out[k[2]] > c), np.mean(out[k[3]] > c)
    lines.append(f"critical value c (max of the two H0 95th percentiles) {c:.3f}")
    lines.append(f"power against H1 {power:.3f}; against H1-half (information) {half:.3f}")
    lines.append(f"GATE (power >= 0.50): {'passes' if power >= 0.5 else 'FIRES: P1 is not computed and the egg rows are not read'}")
    print("\n".join(lines))


def test():
    eggs = np.array(EGGS["November 1945"], float); dec = np.array(EGGS["December 1945"], float)
    cf, cm = (np.array(ADULTS[g], float) for g in ("young F", "young M")); n = (int(eggs.sum()), int(cf.sum()), int(cm.sum()))
    L0, t, lls = lam(eggs, cf, cm); Lg, tg, llg = lam(eggs, cf, cm, nstart=24)
    flag = abs(llg.max() - lls.max()) > 1e-6
    if flag: L0, t = Lg, tg
    lines = [f"eggs (cage 23, November 1945) {eggs.astype(int).tolist()}, n {n[0]}; young F {cf.astype(int).tolist()}; young M {cm.astype(int).tolist()}",
             f"D4: 3-start log-liks {np.round(lls, 6).tolist()}; 24-start best {llg.max():.6f} -> {'FLAG: grid best used' if flag else 'agree'}"]

    def pboot(delta, B, seed, L):
        rng = np.random.default_rng(seed); q, pf, pm = h0_probs(t_d[delta], delta); s = 0; neg = 0
        for _ in range(B):
            v, _, _ = lam(*draw(rng, q, pf, pm, n), delta=delta); neg += v < -1e-6; s += max(v, 0.0) >= L
        return (s + 1) / (B + 1), neg
    t_d = {0.0: t}
    p0, neg0 = pboot(0.0, 10000, 1946, L0)
    from scipy.stats import chi2
    lines.append(f"Lambda {L0:.4f}; chi2(1) p {chi2.sf(L0, 1):.4f}; parametric bootstrap p {p0:.4f} (10,000, seed 1946; negative Lambda {neg0})")
    verdict0 = p0 >= 0.05
    lines.append(f"P1 rank 1 (one evaluator for both sexes, against the November eggs): {'holds' if verdict0 else 'FAILS'}")
    xa = lambda c: (2 * c[0] + c[1]) / (2 * c.sum()); lg = lambda x: np.log(x / (1 - x))
    dmax = abs(lg(xa(dec)) - lg(xa(eggs))) / 4.35
    lines.append(f"S: AR frequency November {xa(eggs):.4f}, December {xa(dec):.4f}; delta_max (one week) {dmax:.4f}")
    same = True
    for sgn, seed in ((+1, 1947), (-1, 1948)):
        d = sgn * dmax; Ld, td, _ = lam(eggs, cf, cm, delta=d, nstart=24); t_d[d] = td
        pd, negd = pboot(d, 2000, seed, Ld); same &= (pd >= 0.05) == verdict0
        lines.append(f"   delta {d:+.4f}: Lambda {Ld:.4f}; bootstrap p {pd:.4f} (2,000, seed {seed}; negative Lambda {negd})")
    lines.append(f"S: verdict {'robust' if same else 'SENSITIVE'} to the cohort assumption")
    q, pf, pm = h0_probs(t)
    lf, lm = np.log(cf / cf.sum()) - np.log(eggs / eggs.sum()), np.log(cm / cm.sum()) - np.log(eggs / eggs.sum())
    w = eggs / eggs.sum(); cen = lambda v: v - w @ v
    cos = (w @ (cen(lf) * cen(lm))) / np.sqrt((w @ cen(lf) ** 2) * (w @ cen(lm) ** 2))
    lines.append(f"Descriptive, not registered: H0 fit eta_F {t[3]:.3f}, eta_M {t[4]:.3f}; raw increments (E1, E2 coordinates) "
                 f"F {np.round(coords(lf), 3).tolist()}, M {np.round(coords(lm), 3).tolist()}; angle between them (Fisher metric at eggs) {np.degrees(np.arccos(np.clip(cos, -1, 1))):.1f} deg")
    print("\n".join(lines))


def describe():
    """Added after the test, not registered: the raw increments beside Wright and Dobzhansky's evaluator, same basis."""
    eggs = np.array(EGGS["November 1945"], float); le = np.log(eggs / eggs.sum()); wd = coords(np.log([0.7, 1.0, 0.3]))
    lines = [f"(additive, dominance) coordinates in the (E1, E2) basis; Wright-Dobzhansky log(0.7, 1, 0.3): {np.round(wd, 3).tolist()}"]
    for g, c in ADULTS.items():
        c = np.array(c, float); u = coords(np.log(c / c.sum()) - le)
        lines.append(f"   {g}: increment {np.round(u, 3).tolist()}; additive part / W-D additive part {u[0] / wd[0]:.2f}; "
                     f"AR frequency {(2 * c[0] + c[1]) / (2 * c.sum()):.4f} (eggs {(2 * eggs[0] + eggs[1]) / (2 * eggs.sum()):.4f})")
    print("\n".join(lines))


if __name__ == "__main__":
    {"gate": gate, "test": test, "describe": describe}[sys.argv[1]]()
