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


# Second batch, as run on 2026-10-03

Pasted from the runs of this session; `b3_diagnose.py` is shown after its fix.

## b1_b2_reversibility.py

```
B1: misalignment against reversible chains, optimized, against the Jensen-Shannon divergence of the fluxes
    matching pennies t=0.01: optimum 2.4998750056e-05, JS 2.4998750056e-05, EP 9.9997e-05
    matching pennies t=0.1: optimum 2.4875553204e-03, JS 2.4875553204e-03, EP 9.9668e-03
    matching pennies t=2.0: optimum 3.0152620640e-01, JS 3.0152620640e-01, EP 1.9281e+00
    largest relative gap over the 13 cases: 2.2e-12  (predicted < 1e-6)
B2: EP = cycle flux x cycle affinity; low-intensity constant from the edge fluxes
    t=0.5: EP 6.1945971492e-03, J·t·C 6.1945971492e-03, ratio 1.000000000000  (predicted 1)
    t=2.0: EP 6.3266409094e-02, J·t·C 6.3266409094e-02, ratio 1.000000000000  (predicted 1)
    revision probabilities 0.7 and 0.3: EP/(t·C)^2 = 0.013125 ± 5.2e-09, predicted 0.013125
```

## b3_inattention.py

```
beta=   3.0: atoms  1 at [0.5]; spread of the default 0.0041; max |behaviour - tilt of default| 2.4e-06; predicted atoms ~ 0.7
beta=   5.5: atoms  1 at [0.5]; spread of the default 0.0074; max |behaviour - tilt of default| 1.3e-06; predicted atoms ~ 1.0
beta=   6.5: atoms  2 at [0.397 0.603]; spread of the default 0.1024; max |behaviour - tilt of default| 9.1e-07; predicted atoms ~ 1.0
beta=   8.0: atoms  2 at [0.327 0.673]; spread of the default 0.1730; max |behaviour - tilt of default| 2.0e-06; predicted atoms ~ 1.2
beta=  30.0: atoms  3 at [0.19 0.5  0.81]; spread of the default 0.2613; max |behaviour - tilt of default| 3.6e-06; predicted atoms ~ 2.2
beta= 100.0: atoms  6 at [0.105 0.275 0.423 0.577 0.725 0.895]; spread of the default 0.2806; max |behaviour - tilt of default| 6.0e-06; predicted atoms ~ 4.1
beta= 300.0: atoms 11 at [0.06  0.158 0.241 0.319 0.401 0.5   0.599 0.681 0.759 0.842 0.94 ]; spread of the default 0.2861; max |behaviour - tilt of default| 1.0e-05; predicted atoms ~ 7.1
dimension slope of the optimized default at beta=30, w 0.1 -> 0.01: 0.751  (predicted > 0.9)
```

## b3_diagnose.py

```
iterations    2000: atom widths [0.0086, 0.0181, 0.0086], slope w 0.1->0.01 0.535, mass of grid points above 1e-3: 149
iterations   20000: atom widths [0.0027, 0.0059, 0.0027], slope w 0.1->0.01 0.751, mass of grid points above 1e-3: 59
iterations  100000: atom widths [0.0012, 0.0027, 0.0012], slope w 0.1->0.01 0.806, mass of grid points above 1e-3: 29
iterations  300000: atom widths [0.0007, 0.0015, 0.0007], slope w 0.1->0.01 0.843, mass of grid points above 1e-3: 19
```

## b3b_followup.py

```
beta=50.0: 4 atoms, predicted between 2.9 and 5.8
beta=200.0: 10 atoms, predicted between 5.8 and 11.5
beta=5.85: spread of the default 0.0060
beta=6.15: spread of the default 0.0601
```

## b4_b5_b6.py

```
B4a: L=   1e+01: gain in F    0.240
B4a: L=   1e+02: gain in F    0.854
B4a: L=   1e+03: gain in F    4.939
B4a: L=   1e+04: gain in F   34.394
B4a: L=   1e+06: gain in F 2127.136
B4b: chi-squared budget used 0.100000; gain 0.273861; sqrt(0.1·Var) = 0.273861; positive everywhere: True
B4c: B=0.1: chi-squared gain 0.223606798 vs sqrt(B)·rho·sd = 0.223606798; KL pursuit gain 0.3504 vs sqrt(2B)·rho·sd = 0.3162 (ratio 1.1081)
B4c: B=0.3: chi-squared gain 0.387298335 vs sqrt(B)·rho·sd = 0.387298335; KL pursuit gain 0.6520 vs sqrt(2B)·rho·sd = 0.5477 (ratio 1.1903)
B4c: B=0.5: chi-squared gain 0.500000000 vs sqrt(B)·rho·sd = 0.500000000; KL pursuit gain 0.8827 vs sqrt(2B)·rho·sd = 0.7071 (ratio 1.2483)
B4c: B=1 (chi-squared infeasible beyond B = 0.5): KL pursuit gain 1.3577 vs 1.0000
B5 Gaussian: largest relative error over 150 cases 3.6e-15  (predicted < 1e-9)
B5 exponential product, t=0.1: M/departure 0.500000, sin^2 = 0.5   (registered: departs by >1% at t = 2; t_max = 1)
B5 exponential product, t=0.5: M/departure 0.500000, sin^2 = 0.5   (registered: departs by >1% at t = 2; t_max = 1)
B5 exponential product, t=0.9: M/departure 0.500000, sin^2 = 0.5   (registered: departs by >1% at t = 2; t_max = 1)
B5 exploratory, Exp x Normal, t=0.05: M/departure 0.4829, sin^2 = 0.5
B5 exploratory, Exp x Normal, t=0.2: M/departure 0.4268, sin^2 = 0.5
B5 exploratory, Exp x Normal, t=0.5: M/departure 0.2895, sin^2 = 0.5
B6: depends on r/sigma only (max gap 0.0e+00); non-increasing in r: True; zero from r = sigma·Phi^-1(1-alpha): True
```

## b7_attention.py

```
B7: largest gap between the misalignment against 'ignoring the situation' and the mutual information: 3.1e-16
```
