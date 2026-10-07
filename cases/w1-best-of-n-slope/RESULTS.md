# W1 — The best-of-`n` slope on unseen answers. Results

**Registered in commit:** `f7a2665`, pushed before any computation on the test data.
**Registration SHA-256:** `6ea9e57cc285ccb3e19bd51c52da1f226dcc39812345053cdf6409dd0c9afea2`
**Computed by:** `run.py` in this folder, run once in full after the registration, by the executor (a Claude model);
12.6 million answers scored in 568 seconds. Its output is `output.json`. The proxy's hash was checked before scoring.
**Departures from the registration:** none. Prompts are numbered in the order `split_1`, …, `split_10` (stated in
`run.py`).

**Licences.** The answers and gold scores are released without a declared licence, on AlpacaFarm prompts under CC BY-NC
4.0, and the proxy's training pairs likewise. Since this repository is under the AGPL, it keeps none of them, nor
anything trained or computed answer by answer from them: the proxy's weights (`proxy.npz`) and the per-prompt statistics
were removed after the run. `train_proxy.py` rebuilds the proxy exactly (the same SHA-256 on two runs), and `run.py`
checks the hash before scoring; `output.json` keeps only aggregates.

## Verdict

| Quantity | Value | 95% interval (2,000 resamples of prompts) |
|---|---|---|
| `a_pred = √2·Cov_q(G, F)/σ_q(G)`, the framework's initial slope | `0.278` | `0.263` to `0.294` |
| `a_fit`, the literature's form fitted over `n = 1, …, 12,500` | `0.338` | `0.311` to `0.366` |
| `b_fit` | `0.035` | |
| `D = a_fit − a_pred` | `+0.060` | `+0.040` to `+0.081` |

The interval of `D` excludes 0: **the prediction is refuted.** The literature's fitted coefficient overstates the
initial slope by about 22%.

Reported without a prediction: over `n ≤ 16`, the fitted `a` is `0.290`; the averaged gold curve rises to `n = 11,369`,
gaining `0.676`, and is flat after it (`0.675` at `n = 12,500`), so this proxy barely overoptimizes; the proxy's
correlation with the gold, within prompts, averages `0.42`; 786 prompts have tied proxy scores, and 3.2 million of the
12.6 million answers share their score with another, most likely because the policy repeats answers.

## Reading, as registered

The literature's fitted coefficient is not the initial slope for this proxy and gold: the best-of-`n` curve does not
keep the literature's form from `d = 0`. The ontology's statement that the best-of-`n` form carries the core's slope is
revised (`ontologies/machine-learning/`, section 3), and `RECORD.md` records the prediction as refuted.

## Exploratory, after the verdict

These analyses were made after the verdict, on the same data; they are not tests.

**Where the form fails.** The averaged gold curve, read in segments of `d`:

| `n` | `d` | slope of the gold in `d` |
|---|---|---|
| 1 to 2 | 0 to 0.44 | `0.284` |
| 2 to 4 | 0.44 to 0.80 | `0.291` |
| 4 to 16 | 0.80 to 1.35 | `0.281` |
| 16 to 64 | 1.35 to 1.77 | `0.257` |
| 64 to 256 | 1.79 to 2.13 | `0.206` |
| 256 to 1,024 | 2.13 to 2.43 | `0.164` |
| 1,024 to 4,096 | 2.44 to 2.70 | `0.143` |
| 4,096 to 12,500 | 2.71 to 2.90 | `0.096` |

The curve is straight, with the slope the framework computes from the initial policy, up to `d ≈ 1.35` (`n = 16`), and
then saturates. A form `d·(a − b·d)` cannot be straight and then bend, and the registered grid, spread evenly in
`log n`, puts most of its points at large `d`, so the fit raises `a` to follow the bend. The slope at `n = 1` to `2`
agrees with `a_pred` by construction, nearly: it is the same covariance read off the same samples ([P13](ii)). That it
stays at `0.28` to `0.29` up to `n = 16` is not by construction; it is a property of these answers.

**A hypothesis that failed.** The executor first suspected the ties: with repeated answers, best-of-`n`'s KL is below
the formula `log n − (n − 1)/n`, so the axis is stretched. Computing each prompt's exact KL from its tied blocks
(`explore.py`) moves `D` from `+0.060` to `+0.062`: the axis is not the cause. By the share of tied answers, `D` is
`+0.138` on the 214 prompts with no ties, `+0.106` on the 350 with fewer than 10% tied, and `−0.016` on the 436 with 10%
or more. The misfit lives where the proxy separates every answer and the gains are largest.

**What this case says.** The framework's initial slope agrees with the curve near its start, as it must, and the curve
keeps that slope up to `n = 16`, which the framework did not predict. The literature's two-parameter form, which the
ontology had vouched for, does not describe the curve beyond that. The ontology predicted that the two agree; they do
not, so the prediction is refuted, as registered. The finding concerns one proxy, a linear model of the answer's words:
a learned neural proxy might give a curve of another shape, and only a new registration could say.
