---
id: "T7-2 results"
type: "report"
updated: "2026-09-27"
---
# T7 case 2 — results: retirement-enrolment defaults

Pre-registered in [[T7-2 preregistration]] (sha256 `8e774bf8…`, commit `0c1569a`) before any value was read. Data:
Choi, Laibson, Madrian & Metrick (2004), NBER w8651, Table 2, copied from the PDF text layer into `t72_table2.csv`.
Script `t72_run.py`; output `t72_output.txt`. The PDF (sha256 `9b152cf0…`) was supplied by the PI and is not committed.

**Data.** 9 comparable rows (Company A: 4 tenure bands; Company B: 5), all passing the sum check. The table reports
one decimal place, not whole numbers as the pre-registration assumed, so rounding noise is smaller than the tolerance
allowed for. The tolerance stays as registered.

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| P1 | empirical, key | the two non-default categories share one ratio: median `\|δ\|` = 0.265 against `log 1.5` = 0.405 | **holds** |
| P2 | empirical | the constant-ratio model beats "active choices unchanged": median error 0.132 against 0.293 | **holds** (weak by construction) |
| P3 | empirical | each default pulls toward itself: `π_D > 0` and `π_N > 0` in 9 of 9 rows | **holds** |

| Row | `Δ_<` | `Δ_>` | `δ` | `π_D` | `π_N` |
|---|---|---|---|---|---|
| A 24–29 | +0.000 | −0.086 | +0.086 | +1.50 | +1.56 |
| A 30–35 | +0.100 | −0.165 | +0.265 | +1.53 | +1.50 |
| A 36–41 | −0.201 | −0.047 | −0.154 | +1.44 | +1.60 |
| A 42–47 | +0.405 | −0.181 | +0.587 | +1.31 | +1.52 |
| B 3–5 | −0.722 | −0.573 | −0.149 | +3.52 | +0.95 |
| B 6–11 | −0.665 | −0.405 | −0.260 | +3.15 | +0.98 |
| B 12–17 | −0.421 | +0.032 | −0.454 | +2.85 | +1.40 |
| B 18–23 | −0.668 | +0.005 | −0.673 | +2.59 | +1.13 |
| B 24–26 | −0.840 | +0.031 | −0.871 | +2.38 | +0.93 |

## What it shows

- **The framework's human actor passes its structural test on the canonical default data.** Under (E_A) and exclusion,
  the two categories that are the default in neither regime must move by one common factor; at the registered
  tolerance, they do. The default effect then reads as a **reference shift**: large pulls toward each regime's default
  (`π_D` 1.3–3.5 nats), with the rest of the distribution rescaled.
- **This is the first T7 result where the framework's structure is the test, and it passed.** In case 1 the framework
  could at best tie a raw feature. Here the claim is structural, and no raw feature makes it.

## A pattern the median hides (post hoc, labelled; not tested)

- **Company B shows a systematic drift.** `δ` grows from −0.15 to −0.87 with tenure. The "above default" share
  converges between the regimes (`Δ_>` → 0), while "below default" stays suppressed under automatic enrollment
  (`Δ_<` ≈ −0.4 to −0.8).
- **Reading:** employees who leave the default rarely go *below* it. The default acts as a recommended minimum, which
  changes what people value — an endorsement or anchoring effect (McKenzie et al. 2006). That is exactly the failure of
  exclusion that B12 names as its bias. The framework does more than pass here: **its test locates where exclusion
  fails** (below the default, in Company B, growing with tenure).
- **Company A** shows no such trend. Its largest `δ` (+0.59 at 42–47 months) sits on a cell of 0.9 %.
- **Caveats:** the "below default" cells are 1–4 %, so their ratios are noisy; no standard errors are published; and
  hired-before and hired-after employees are observed at different dates.
- **Tested since, and not replicated** ([[T7-2b results]]): the pattern held in Madrian & Shea's company and reversed in Company C.
- **A follow-up test could check the Company B pattern:** register "`Δ_<` stays below `Δ_>`, with a gap that widens
  with tenure", and run it on Madrian & Shea's company or on Choi et al.'s Company C, if their distributions can be
  obtained as numbers.

## Verdict for T7 case 2

For §4b item 3, the human substrate has **a real diagnostic with a prediction its literature can check, and it held.**
It is also more than a relabelling: the framework separates a reference shift from a change in values, and on this
data it points to where the second begins. The imported theorem is B12 (the logit with a default-dependent reference;
McFadden 1974, and Matějka & McKay 2015 for its rational-inattention form).
