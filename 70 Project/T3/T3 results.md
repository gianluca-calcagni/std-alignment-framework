---
id: "T3 results"
type: "report"
updated: "2026-09-26"
---
# T3 — results: C9 is not testable from published data

Pre-registered in [[T3 preregistration]] (commit `37be3d8`), before any number was retrieved. The environment could
not reach the paper ([[T3 status]]); the PI then supplied both versions as PDFs (PMLR, ICML 2023; arXiv v1). Neither
is added to the repository.

## What source S1 reports (Gao, Schulman & Hilton 2023)

| Quantity | Reported? | Where |
|---|---|---|
| `α_bon`, gold, per proxy size | **only in a figure** | Fig. 3a (PMLR p. 4): from about 0.51 at 3M to about 0.65 at 3B parameters, read with the registered ±10 % uncertainty; policy 1.2B, 90,000 comparisons |
| `sd` of gold under the initial policy | **fixed by normalization** | §2.2: each RM is recentred so the initial policy's mean is 0, and "we also unit normalize the variance of the gold RM scores". Hence `sd = 1`. Flag: the text does not say under which distribution the variance is taken; the initial policy is the natural reading of the same paragraph |
| `ρ`, proxy–gold correlation under the initial policy | **not reported** | the paper gives held-out validation cross-entropy losses (Fig. 6, Fig. 11; e.g. 0.686 for its weakest runs, against ln 2 = 0.693 at chance). Data rule 2 admits a correlation or a pairwise agreement rate, not a loss |
| `α_RL` | stated constant across RM sizes, value not reported numerically | §3.2 |

**S2.** No other source could be read: every publisher and preprint host is blocked in this environment (web
search returns snippets only). None was searched in full.

## The passages and readings used

Quoted from the PMLR version:
- §1: "We find empirically that for best-of-n (BoN) sampling, `R_bon(d) = d(α_bon − β_bon·d)`"; "Here, `R(0) := 0` by
  convention because the reward is translation invariant."
- §2: "The KL divergences for BoN are computed analytically: `KL_bon = log n − (n−1)/n`."
- §2.1: "The 6B reward model from Ouyang et al. (2022) is used as the gold RM, and our proxy RMs vary from 3M to 3B
  parameters"; the synthetic comparisons are labelled by "always marking the trajectory with the higher gold RM
  score as preferred"; 100,000 comparisons, 10 % held out "for computing the validation loss of RMs".
- §2.2: "we recenter each RM such that the average reward of the initial policy is 0. We also unit normalize the
  variance of the gold RM scores." Footnote 5: "We later decided this was unnecessary but decided not to change it."
  And: "All renormalization and recalibration is applied after the experiments; this does not affect BoN at all."
- §3.2: "We hold policy size (1.2B) and data size (90,000) constant … for the gold RM scores, `α_bon` and `β_bon`
  change smoothly with RM size (Figures 3a and 3b). For RL, we find that we can hold `α_RL` constant across all RM
  sizes."

**Figure 3a, gold `α_bon`, read point by point** (PMLR p. 4; rendered at 220 dpi). Nine points, left to right on a
logarithmic RM-size axis; the sizes are read positions, not the paper's labels. Reading uncertainty ±10 % (data
rule 1).

| Point | RM size (read) | `α_bon` (read) | `ρ` needed for P1 exactly (`α/√2`) |
|---|---|---|---|
| 1 | ≈ 3·10⁶ | 0.51 | 0.36 |
| 2 | ≈ 1.2·10⁷ | 0.52 | 0.36 |
| 3 | ≈ 2.5·10⁷ | 0.55 | 0.39 |
| 4 | ≈ 4·10⁷ | 0.57 | 0.40 |
| 5 | ≈ 8·10⁷ | 0.58 | 0.41 |
| 6 | ≈ 3·10⁸ | 0.62 | 0.44 |
| 7 | ≈ 7·10⁸ | 0.65 | 0.46 |
| 8 | ≈ 1.2·10⁹ | 0.63 | 0.45 |
| 9 | ≈ 3·10⁹ | 0.64 | 0.45 |

## Verdict under the registered rules

**Data rule 5 applies: C9 is not testable from published data.** P1 and P2 are not evaluated. This is a clean
negative about the cheapest route, not about C9.

## Post hoc, not registered

- **A bound that cannot fail here.** Because `ρ ≤ 1` and `sd = 1`, P1 would fail for any `ρ` if `α_bon > 1.5·√2 ≈ 2.12`.
  The read values (0.51–0.65) are far below it, so the bound says nothing.
- **What C9 would need.** For P1 to hold exactly, `ρ = α_bon/√2`: about **0.36 at 3M to 0.46 at 3B**; with the
  Gaussian best-of-n constant 1.30 of P2, about 0.39 to 0.50. Within the factor-1.5 band, `ρ` from about 0.24 to 0.69.
  These are the correlations a replication must measure; they are not evidence.
- **One qualitative match, not a test.** C9 predicts that `α_bon` rises with the proxy's correlation to the gold
  model. `α_bon` rises smoothly with proxy size (Fig. 3a), and larger proxies have lower validation loss. That is
  the predicted direction, but so would almost any account predict it.

## Next

**T3b — replication with small open models** (registered route, data rule 5): measure `ρ` and `sd` under the initial
policy, run best-of-n, fit `α_bon`. It needs compute and access to model hosts, neither available in this
environment. It is recorded, not started.
