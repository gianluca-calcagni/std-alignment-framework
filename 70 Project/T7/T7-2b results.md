---
id: "T7-2b results"
type: "report"
updated: "2026-09-27"
---
# T7 case 2b/2c — results: is the default a floor? Replication on two further companies

Pre-registered in [[T7-2b preregistration]] (sha256 `7301d4f9…`, `a52845a`). D2 fired on extraction (legend swatches
counted as bars), and [[T7-2c amendment]] (`620879e0…`, `df7deb0`) fixed it before any prediction was computed; that
amendment discloses that Figure 3C's bar heights were seen during the diagnosis. Script `t72b_run.py`; output
`t72b_output.txt`; extracted values `t72b_figures.csv`.

**Data.** Madrian & Shea (2001) Figure 4C: the WINDOW and NEW cohorts, including non-participation. Choi et al. (2004)
Figure 3C: Company C, participants. Both plans default to 3%. Integrity: series sums 1.003, 0.991, 1.007 and 1.007;
tick-fit `R²` 0.99998 and 1.00000.

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| P1 | empirical, replication | the default acts as a floor in both companies: `δ` = −0.271 (Madrian & Shea), **+0.876** (Company C) | **fails** |
| P2 | empirical | `δ < −log 1.25` in at least one: Madrian & Shea −0.271 | holds |
| P3 | empirical | untestable: 2 below-default bins in total (fewer than 3). Disclosed in T7-2c before any prediction was computed | not evaluated |

**Reported.** T7-2's exclusion statistic `|δ|` against `log 1.5` (0.405): Madrian & Shea 0.271 (within), Company C
0.876 (outside). The default pull `π_D`: +3.13 and +1.43.

Per-bin log-ratios `ℓ(x) = log(p_AE/p_noAE)`:

| Bin | 1–2% | 4–5% | 6% | 7–9/10% | 10% | 11–14/15% | 15% |
|---|---|---|---|---|---|---|---|
| Madrian & Shea | −0.72 | **−0.83** | −0.52 | −0.34 | −0.14 | −0.43 | −0.20 |
| Company C | +0.36 | **−0.81** | −0.45 | −0.49 | — | −0.48 | — |

## What it shows

- **T7-2's post-hoc "floor" pattern does not replicate.** It holds in Madrian & Shea's company and reverses in Company
  C, where the below-default cell is 1–2 percentage points, so the reversal rests on very few employees. On this
  evidence the Company B pattern in [[T7-2 results]] is not a general property of defaults.
- **B12's exclusion test passes in one further company and fails in the other.** Company C fails at the registered
  tolerance, again on the tiny below-default cell. Across three companies (A, B, and Madrian & Shea's) the constant-ratio
  structure holds loosely; Company C is the exception, and it rests on one small cell.

## A different pattern, in both new companies (post hoc; labelled; not tested)

The suppression of non-default rates under automatic enrollment is **strongest just above the default** (4–5%: −0.83
and −0.81), and weaker further away. In both companies it is the most negative ratio.
- **Why it matters.** B12's reference family `q_d = (1−α)u + α·1_d` puts the default's pull on the default alone. A pull
  that reaches the neighbouring rates says the family is too narrow: the reference shift is **local**, a kernel around
  the default rather than a point mass. People who would have chosen 4–5% stay at 3%; people who would have chosen 10%
  mostly do not.
- **What would test it:** a registered prediction that `ℓ(x)` rises with the distance above the default, on a fresh
  company. It would also refine B12. With a kernel family, the constant-ratio prediction applies only to rates outside
  the kernel's reach.

## Verdict for T7 case 2 (with 2b)

The framework's human actor survives its structural test loosely: 3 of 4 companies at the registered tolerance, and the
exception rests on one tiny cell. The one post-hoc pattern registered for replication failed. The data point to a
better reference family (a local pull around the default), which is a concrete correction to B12, not a vindication
of it.
