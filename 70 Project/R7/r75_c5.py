import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r75_probe.py')).read().split('# ---- C2')[0])
rng = np.random.default_rng(7506)
print("C5 share of the free measure that is ordering error, M_ord/M_free, for evaluators F_hat = F + sigma*noise (400 instances each)")
for sig in (0.05, 0.2, 0.5, 1.0, 3.0):
    r = []
    for _ in range(400):
        n = rng.integers(5, 40); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); b = rng.uniform(0.5, 5)
        ph = tilt(q, F + sig * rng.normal(size=n), b); mo = m_ord(ph, q, F)[0]; mf = m_free(ph, q, F)[0]
        if mf > 1e-9: r.append(mo / mf)
    r = np.array(r); print(f"  sigma={sig:4}: median {np.median(r):.2f}  [p10 {np.percentile(r,10):.2f}, p90 {np.percentile(r,90):.2f}]")
