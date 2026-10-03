# Results, as run on 2026-10-03

The output of every probe, verbatim, on one machine. A probe prints diagnostics, not verdicts; the verdicts are in
`README.md`, against the predictions in `PREDICTIONS.md`.

## t1_dimension.py

```
(a) pile 10%:        slope 0.0998   predicted 0.10
(b) rounding to 0.1: slope 1.0000   predicted 1.00  (KL at w=0.01: 2.3026 = ln 10 = 2.3026)
(c) a line in 2-D:   slope 0.9997   predicted 1.00
(d) Cantor, triadic: slope 0.3691   predicted 0.3691
    Cantor, decimal: slope 0.3723   predicted 0.3691 ± 0.03
```

## t2_no_piles.py

```
T2: max |log ratio| controlled vs endpoint tilt = 3.33e-16  (predicted < 1e-12)
    density ratio to the default, below and above the threshold: [0.16843102 1.24454627]
```

## t3_coordination_in_time.py

```
T3: stationary law [0.25 0.25 0.25 0.25]; same-round mutual information -8.33e-17  (predicted < 1e-12)
    entropy rates: each player 0.3140, the pair 0.3970; mutual information rate 0.2309 nats/round  (predicted > 0.1)
    lagged mutual information, a1 now vs a2 next round: 0.4946
```

## t4_irreversibility.py

```
T4 (i): largest entropy production over 120 potential-game cases 9.47e-25  (predicted < 1e-12)
T4 (ii): EP/(t·C)^2 over 50 random 2x2 games: mean 0.015624, CV 5.42e-05  (predicted CV < 1%)
T4 (iii): matching pennies, t=0.01: EP 9.9997e-05, misalignment against reversible chains 2.4999e-05, ratio 0.2500  (predicted <= 0.5; about 0.25 at t = 0.01)
T4 (iii): matching pennies, t=0.1: EP 9.9668e-03, misalignment against reversible chains 2.4876e-03, ratio 0.2496  (predicted <= 0.5; about 0.25 at t = 0.01)
T4 (iii): matching pennies, t=2.0: EP 1.9281e+00, misalignment against reversible chains 3.0153e-01, ratio 0.1564  (predicted <= 0.5; about 0.25 at t = 0.01)
```

## t5_principals.py

```
T5 floors (0.0, 0.0, 0.0): weighted misalignment -3.977e-16; KL(p*||q) -1.220e-16; relative residual 4.02e-01
T5 floors (0.5, 1.0, 1.5): weighted misalignment 8.901e-02; KL(p*||q) 6.030e-02; relative residual 1.02e-08
    coefficients [0.1  0.5  0.45] against w·t [0.1  0.5  0.45] (nearest intensities [0.5 1.  1.5])
```

## t5b_floors.py

```
T5b independent objectives: all principals exactly at their floors in 11 of 20 instances
T5b nearly identical objectives: all principals exactly at their floors in 0 of 20 instances
```

## t6_lockin.py

```
T6: largest |rate - KL(share||1/2)| 3.49e-04 (predicted < 1e-3); rates mean 0.1992 (predicted 0.1931 ± 0.02), sd 0.1851 (predicted > 0.05)
```

## draft1_examples.py

```
1. I-projection [0.2903 0.3194 0.3903], KL(p*||p0) = 0.1231
   n=50: rate 0.175; law of one draw given the event [0.2701 0.3202 0.4097]
   n=200: rate 0.139; law of one draw given the event [0.2849 0.3196 0.3955]
   n=800: rate 0.128; law of one draw given the event [0.2889 0.3194 0.3917]
2. x0=0: w=0.01: centred 0.00, edge 0.69; w=0.0001: centred 0.00, edge 0.69; w=1e-06: centred 0.00, edge 0.69
2. x0=0.001: w=0.01: centred 0.00, edge 0.69; w=0.0001: centred 3.72, edge 3.77; w=1e-06: centred 8.33, edge 8.33
3. n=2: 0.193147 (formula 0.193147); five tied levels 0.180139
3. n=4: 0.636294 (formula 0.636294); five tied levels 0.606690
3. n=16: 1.835089 (formula 1.835089); five tied levels 1.479613
4. average of the ray: t=0: 0.354, t=0.5: 0.474, t=0.9: 0.736, t=0.99: 0.937, t=0.999: 0.989, t=1.0: 1.000
   divergence of an exponential behaviour of mean 2 to the ray, up to a constant: t=0.5: -2.0069, t=0.9: -2.5764, t=0.99: -2.6828, t=1.0: -2.6931
5. D_max = 0.483; half a nat more buys L=10: 0.390, L=100: 0.468, L=1000: 0.494, L=10000: 0.499 (bound 0.5)
6. KL(u||p_k) = 0.069 for every k; at 100 cells: k=7: 6.8e-02, k=77: 4.7e-03, k=7777: 4.6e-07
7. limit 4.082; κ²·KL: κ=10: 3.041, κ=30: 3.601, κ=100: 3.915, κ=300: 4.023, κ=1000: 4.064
```

## vocabulary_examples.py

```
1. pass rate 0.840 -> 0.929; minutes moved per patient: honest tilt 15.6, fudging 2.3
   landing in the last 5 min: w=20: 0.107, w=10: 0.141, w=5: 0.184, w=1: 0.184, w=0.1: 0.184, w=0.01: 0.184
   landing in the last 1 min: w=20: 0.107, w=10: 0.141, w=5: 0.184, w=1: 0.304, w=0.1: 0.304, w=0.01: 0.304
   landing in the last 0.01 min: w=20: 0.107, w=10: 0.141, w=5: 0.184, w=1: 0.304, w=0.1: 0.501, w=0.01: 0.704
2. New Zealand, manual: 32.8% zeros -> 0.045 nats per reading, about 22 readings per nat
2. England, IHD patients (baseline assumed 20%): 64.0% zeros -> 0.457 nats per reading, about 2 readings per nat
3. h=1, d=1: found at intensity 6.9; the 10%-90% switch takes 4.39 (63.6% of it)
3. h=1, d=10: found at intensity 69.1; the 10%-90% switch takes 4.39 (6.4% of it)
3. h=3, d=10: found at intensity 23.0; the 10%-90% switch takes 1.46 (6.4% of it)
4. sigma=0.05: deployment vs test at most 1.0000; deployment vs halfway at most 1.0000
4. sigma=0.1: deployment vs test at most 1.0000; deployment vs halfway at most 0.9876
4. sigma=0.3: deployment vs test at most 0.9044; deployment vs halfway at most 0.5953
4. sigma=0.5: deployment vs test at most 0.6827; deployment vs halfway at most 0.3829
```

