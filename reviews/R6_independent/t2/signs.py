import pickle
from t2_r6 import *
# ---- P5: BoN-2 identity on the V25 generator
e5 = 0; P7 = []; P8 = []
for q, F, Fh in v25_instances():
    o = np.argsort(Fh, kind='stable'); Gam = np.empty_like(q); Gam[o] = np.cumsum(q[o])
    eff = bon(q, Fh, 2)@F - q@F; e5 = max(e5, abs(eff - cov(q, 2*Gam - q, F)))
    c = cov(q, Fh, F); P7.append((np.sign(eff) != np.sign(c), eff, c))
    # P8: NPG initial effect by central finite difference of one NPG step of size +-h (explicit Fisher solve)
    h = 1e-5; pp = npg_path(q, Fh, eta=h, steps=1)[-1]; pm = npg_path(q, Fh, eta=-h, steps=1)[-1]
    d_npg = (pp@F - pm@F)/(2*h); P8.append(abs(d_npg - c)/max(abs(c), 1e-12))
fl = [x[0] for x in P7]
print(f'[P5] max |E_BoN2 F - E_q F - Cov_q(2Gamma - q, F)| over 2000 V25 instances = {e5:.1e}')
print(f'[P7] BoN-2 initial effect vs sign of Cov_q(Fh,F): opposite signs in {sum(fl)}/{len(fl)} = {100*np.mean(fl):.2f} %')
mag = sorted([(abs(x[2]), x[1], x[2]) for x in P7 if x[0]])[-3:]
print('     largest |Cov_q| among the disagreements (Cov_q, BoN-2 effect):', [(round(c, 4), round(e, 4)) for _, e, c in mag])
print(f'[P8] NPG initial effect vs Cov_q(Fh,F): max relative error = {max(P8):.1e}; median {np.median(P8):.1e}')
# ---- P6: constructed instance, Cov_q(Fh,F) > 0 but BoN-2 effect < 0
n = 101; q = np.ones(n)/n; z = np.linspace(-1, 1, n-1)
Fh = np.r_[z, 1000.0]; F = np.r_[-3*z, 2.0]          # bulk: ranks anti-aligned with F; one outlier aligned in value
print(f'[P6] constructed: Cov_q(Fh,F) = {cov(q, Fh, F):+.3f};  Gibbs initial slope = Cov_q = same sign;  '
      f'BoN-2 effect E_BoN2 F - E_q F = {bon(q, Fh, 2)@F - q@F:+.4f};  BoN-8: {bon(q, Fh, 8)@F - q@F:+.4f};  '
      f'BoN-1000: {bon(q, Fh, 1000)@F - q@F:+.4f}')
# ---- P10: KL-PG initial sign on the R5 T-B instance
qb, Fb, Fhb = tb_instance(); b = 30.0
lq = np.log(qb); p = qb.copy()
g_kl = p*((Fhb - p@Fhb) - ((np.log(p) - lq) - p@(np.log(p) - lq))/b)
g_v = p*(Fhb - p@Fhb)
v_kl = qb*(g_kl - qb@g_kl)                              # dp/dt = p * (theta_dot - E_p theta_dot)
print(f'[P10] T-B: Cov_q(Fh,F) = {cov(qb, Fhb, Fb):+.3f};  q^2-weighted = {np.sum(qb**2*(Fb-qb@Fb)*(Fhb-qb@Fhb)):+.3e};  '
      f'KL-PG initial d/dt E_pF = {v_kl@Fb:+.3e};  max|grad_KLPG - grad_VPG| at q = {np.abs(g_kl-g_v).max():.1e}')
ts, P = flow_path(qb, Fhb, beta=b, T=50, npts=50)
print(f'      KL-PG flow gain E_pF - E_qF at t = {ts[5]:.3g}, {ts[20]:.3g}, {ts[-1]:.3g}: '
      + ', '.join(f'{P[i]@Fb - qb@Fb:+.3e}' for i in (5, 20, -1)))
# ---- P11: Thm 1 along the (T = 1e8) KL-PG paths on the V5 pair, target F, p* = p_{F,beta}
q, F, E1, E2 = v5_pair(); ps = tilt(q, F, b); Jf = lambda p: p@F - KL(p, q)/b
paths = pickle.load(open('paths_KLPG.pkl', 'rb')); e11 = 0; cnt = 0
for k in ('E1', 'E2', 'F'):
    for pt in paths[k]:
        e11 = max(e11, abs((Jf(ps) - Jf(pt)) - KL(pt, ps)/b)); cnt += 1
print(f'[P11] Thm 1 along {cnt} non-Gibbs KL-PG iterates: max |J_F(p*) - J_F(p_t) - KL(p_t||p*)/beta| = {e11:.1e}')
