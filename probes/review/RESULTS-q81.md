# Outputs of the probes of Q81 (`NOTES.md` §39)

Run on 2026-11-10 and 2026-11-11, with the pins of `requirements.txt` (NumPy 2.4.4, SciPy 1.17.1), on the default
floating-point path. Exploratory: simulated data only, no registered prediction, and no result rests on them.

## `python3 probes/review/q81_plugin_bias.py`

```text
== bias ==
conditions merged      kl(ubar‖eps)       = 0.1903
conditions deterministic ubar·log(ubar/eps) = 0.3852

truth                                true M      K=1      K=4     K=16     K=64    K=256
the same rate in every condition     0.1903   0.3853   0.2202   0.1970   0.1919   0.1905
rates Beta(1, 2.07)                  0.2193   0.3885   0.2522   0.2266   0.2206   0.2193
rates Beta(0.3, 0.62)                0.2642   0.3791   0.2980   0.2718   0.2660   0.2646
rate 0 or 1 in each condition        0.3940   0.3940   0.3940   0.3940   0.3940   0.3940

== edge ==
rates (0.5, 0.5, 0, 0.9), eps = 0.1:  M = 0.5418316169065958
rates (0.5, 0.5, 1e-300, 0.9), eps = 0.1:  M = inf
rates (0.5, 0.5, 1e-17, 0.9), eps = 0.1:  M = inf
rates (0.5, 0.5, 1e-12, 0.9), eps = 0.1:  M = 0.5418316169070179
rates (0.5, 0.5, 1e-09, 0.9), eps = 0.1:  M = 0.5418316173285679

```

## `python3 probes/review/q81_universal_bet.py`

```text
vertices of A: [[1.0, 0.0, 0.0], [0.9, 0.0, 0.1], [0.5, 0.5, 0.0], [0.7, 0.2, 0.1]]
grid points inside B: 5299144

record                           n  n·M(s_n)   log W_n     gap   d·log(n+1)+1
independent, outside A          30     5.264    -0.371   5.634         11.302
independent, a vertex of A      30     0.000    -5.302   5.302         11.302
a sticky Markov chain           30     1.332    -3.515   4.847         11.302
fixed blocks 0…0 1…1 2…2        30     6.940     1.361   5.579         11.302
every breach at the end         30     2.243    -2.569   4.812         11.302
independent, outside A         100    14.214     6.165   8.048         14.845
independent, a vertex of A     100     0.000    -7.256   7.256         14.845
a sticky Markov chain          100     3.661    -4.338   7.999         14.845
fixed blocks 0…0 1…1 2…2       100    30.308    22.336   7.971         14.845
every breach at the end        100     9.233     2.611   6.622         14.845
independent, outside A         300    46.878    36.574  10.303         18.121
independent, a vertex of A     300     0.000    -9.980   9.980         18.121
a sticky Markov chain          300    71.661    60.401  11.260         18.121
fixed blocks 0…0 1…1 2…2       300    93.737    83.348  10.389         18.121
every breach at the end        300    27.699    19.419   8.280         18.121
independent, outside A        1000   135.262   122.203  13.059         21.726
independent, a vertex of A    1000     0.000   -13.180  13.180         21.726
a sticky Markov chain         1000   557.300   545.788  11.512         21.726
fixed blocks 0…0 1…1 2…2      1000   320.024   307.018  13.006         21.726
every breach at the end       1000    92.332    82.278  10.053         21.726
independent, outside A        3000   402.238   386.641  15.597         25.020
independent, a vertex of A    3000     0.017   -19.009  19.025         25.020
a sticky Markov chain         3000   961.338   947.057  14.281         25.020
fixed blocks 0…0 1…1 2…2      3000   962.922   947.647  15.275         25.020
every breach at the end       3000   276.995   265.694  11.300         25.020

least gap 4.812 (the claim asks ≥ 0); largest gap as a share of the bound 0.760 (asks ≤ 1)
```
