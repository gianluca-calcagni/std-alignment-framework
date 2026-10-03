# W1 — The best-of-`n` slope on unseen answers. Registration

**Kind:** world: the machine-learning ontology's prediction from [[P13 — What the start of a change gains|P13]], with its row in `RECORD.md`; it counts toward
the finish line and the base rate (`cases/README.md`). **Who:** registered by the executor, a Claude model, under the
PI's instruction to test as the executor sees fit (`NOTES.md` §3.1, Q26); no one else has read it before it was pushed
(`NOTES.md` §5.4, H29). Nothing below has been computed on the test data before this file was pushed.

## The prediction

From the ontology (`ontologies/machine-learning/`, section 3): for best-of-`n`, the coefficient `a` of the literature's
form for the gold score, `gold(d) − gold(0) = d·(a − b·d)` with `d = √KL` and `KL = log n − (n − 1)/n`, is
`a = √2·Cov_q(G, F)/σ_q(G)`, where `F` is the gold, `G` is `log Q(r̂)` centred within each prompt, and `Q` is the
distribution function of the proxy `r̂` under the initial policy `q`. Both sides come from samples of the initial policy
scored by the gold and the proxy, with no optimization. *Refuted if* the fitted `a` differs from this value by more than
its sampling error.

## What has been seen

- **The test data**: `huggingface.co/datasets/tlc4418/gold_labelled_gens` [[References|@coste2024]], downloaded on 2026-10-03: ten
  JSON files, 3.3 GB. Seen: the file list and sizes, the card's two sentences, and the structure of the records (100 per
  file; each has `instruction`, `input`, `answers`, a list of 12,600 strings, and `gold_scores`, a list of 12,600
  numbers). No answer and no score has been read.
- **The paper**, read in full. Its figures show best-of-`n` gold curves on these answers for its own proxies, which are
  not the proxy here; the curves are seen in summary, so this test concerns a proxy whose curve nobody has seen.
- **The proxy's training data**: the four files of the `train` folder of
  `tlc4418/1.4b-policy_preference_data_gold_labelled`, 49,383 pairs of answers from the same policy with the gold's
  preference. Its `validation` folder, which may share prompts with the test data, was not downloaded.

## The proxy, frozen before registration

`proxy.npz` in this folder, SHA-256 `a58685aed890c8e9d677cee13ea200271fb810488824fc6f3d9be9d0fc0310ea`, made by
`train_proxy.py`: a Bradley–Terry model, linear in hashed features of the answer's text alone (unigram and bigram
counts, as `log(1 + count)`, and `log(1 + words)`), trained on 44,415 of the pairs and right on 67.1% of the 4,968 held
out, inside the 60 to 75% the paper reports for its own proxies. A learned reward model, small enough to score all 12.6
million answers on this machine's processors.

## The procedure

`run.py` in this folder, written after this registration, does exactly the following.
1. For each of the 1,000 prompts, score its `N = 12,600` answers with the proxy, and sort them by score, ascending, with
   ties broken by a uniformly random permutation drawn with seed `20261003 + k` for the prompt numbered `k` in file
   order. `F_(i)` is the gold score of the `i`-th answer in that order.
2. **The predicted slope.** `G_i = log((i − ½)/N)`, centred, and `σ(G)` its standard deviation over `i = 1, …, N`. For
   each prompt, `c_k = (1/N)·Σ_i G_i·(F_(i) − mean F)/σ(G)`, and `a_pred = √2·mean_k c_k`.
3. **The best-of-`n` curve**, by the unbiased estimator of Coste et al. (their eq. 8):
   `g_k(n) = Σ_{i=n}^{N} C(i−1, n−1)/C(N, n)·F_(i)`, on the grid of the integers `round(10^{j·log10(12500)/199})`,
   `j = 0, …, 199`, without repeats (1 to 12,500, the paper's `n_max`), and `g(n) = mean_k g_k(n)`.
4. **The fitted slope.** `a_fit` and `b_fit` by least squares of `g(n) − g(1)` on `d(n)` and `−d(n)²`, without
   intercept, over the grid points with `n ≥ 2`, each with equal weight.
5. **The sampling error.** 2,000 resamples of the 1,000 prompts with replacement (seed `20261003`), each recomputing
   `a_pred` and `a_fit` from the resampled prompts' `c_k` and `g_k`; the 95% interval of `D = a_fit − a_pred` is between
   their 2.5th and 97.5th percentiles.

**Held** if that interval contains 0; **refuted** otherwise.

## Calibration, before registration, on synthetic prompts only

The procedure was run on synthetic prompts, with Gaussian proxy and gold scores, and seeds the test does not use
(`calibration/`). Without noise, the fitted `a` is 0.993 of the initial slope over the registered grid. With 1,000 noisy
prompts, it held in 6 of 6 runs, at correlations 0.2 and 0.4, with intervals about ±0.02 wide. It held with heavy-tailed
noise, and was refuted, with `D` about `+0.65`, in a world where the gold falls at the top ranks of the proxy. So the
prediction holds when the best-of-`n` curve keeps the literature's form over the whole range, and fails when the curve
rises and then falls sharply, the overoptimization the paper reports for single proxies.

## Readings, fixed now

- **Held**: on answers no one had scored with this proxy, the literature's fitted coefficient is the initial slope that
  the framework computes from the initial policy alone, before any optimization. The ontology's prediction from [[P13 — What the start of a change gains|P13]]
  holds for this proxy and gold.
- **Refuted**: the literature's fitted coefficient is not the initial slope for this pair: the curve does not keep the
  literature's form from `d = 0`, and the ontology's statement that the best-of-`n` form carries the core's slope is
  revised. Recorded in `RECORD.md` as refuted.

Reported without a prediction: `a_pred`, `a_fit`, `b_fit` and `D`, with their intervals; the fit over `n ≤ 16`; where
the averaged gold curve peaks and whether it falls by `n = 12,500`; the correlation of proxy and gold under the initial
policy, averaged over prompts; and the number of ties.
