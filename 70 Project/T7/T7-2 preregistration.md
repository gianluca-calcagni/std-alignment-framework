---
id: "T7-2 preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 2 — pre-registration: retirement-enrolment defaults (before any value is read)

**The claim under test (B12, Prop. B12).** Suppose the chooser is a logit with a default-dependent reference, (E_A),
`p_d ∝ q_d·e^{βF̂}`, with `q_d = (1−α)u + α·1_d`, and suppose the default does not change what the chooser values
(**exclusion**). Then, for every option that is the default in neither regime, `log(p_{d₀}(x)/p_{d₁}(x))` is **the same
constant**. The same holds for any union of such options. This is a structural prediction of the framework's human
actor. If it fails, (E_A) or exclusion fails for these data. If it holds, the reference is identified, and a departure
caused by the default can be told apart from one caused by the evaluator. By Prop. 26(b), a single environment cannot
do that.

**Rule 13.** It changes a verdict: whether the default effect is a reference shift (the framework's reading, with
attribution possible) or a change in what people value (endorsement; B12's identification biased). **Rule 11:**
labels below.

**Seen before.** Both PDFs' table and figure titles, with digits masked, and the row and column labels of Choi et al.
Table 2 (p. 32), with digits masked. No value. The PDFs were supplied by the PI:
- Madrian & Shea 2001, NBER w7682: sha256 `5d8da983…`;
- Choi, Laibson, Madrian & Metrick 2004, NBER w8651: sha256 `9b152cf0…`.

Neither PDF is committed (third-party copyright). Only the numbers extracted into a table are committed.

## Data

**Choi et al. (2004), Table 2 (p. 32):** "The Distribution of 401(k) Contribution Rates by Tenure for Employees Hired
Before and After Automatic Enrollment".
- **Rows:** Company A and Company B, by tenure band.
- **Columns:** four categories — non-participant, `< default`, `default`, `> default` — for employees hired before
  automatic enrollment (default: non-participation) and after it (default: the default rate).
- **Comparable rows:** those with values in both regimes. The labels suggest about 4 for Company A and 5 for Company B;
  the exact count is reported.

Madrian & Shea report their contribution-rate distributions only in figures. They are context, not data, here.

**Extraction rule.** Values are copied exactly from the PDF text layer into `t72_table2.csv`. The extraction is checked
by recomputing that each regime's four percentages sum to 100 within rounding (±2). A row that fails the check is
excluded and counted. **D2:** if more than a third of comparable rows fail, the extraction is wrong: stop and
re-register.

## Quantities

- Every percentage gets `+0.5` percentage points before any logarithm (zero cells).
- For each comparable row, with *after* meaning hired after automatic enrollment:
  - `Δ_< = log(p_after(<D)/p_before(<D))` and `Δ_> = log(p_after(>D)/p_before(>D))`;
  - `δ = Δ_< − Δ_>` — **the framework predicts δ = 0**;
  - `c = (Δ_< + Δ_>)/2`, the common ratio;
  - the **default pull** `π_D = log(p_after(D)/p_before(D)) − c` and the **non-participation pull**
    `π_N = log(p_before(N)/p_after(N)) + c`.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | **empirical, the key test** | the two non-default categories share one ratio: median `\|δ\|` over comparable rows `≤ log 1.5` | median `\|δ\| > log 1.5` |
| P2 | empirical | the constant-ratio model fits better than "active choices are unchanged" (`Δ_< = Δ_> = 0`): median `\|δ\|/2 <` median `(\|Δ_<\| + \|Δ_>\|)/2` | `≥` |
| P3 | empirical | the defaults pull toward themselves: `π_D > 0` and `π_N > 0` in every comparable row | any exception |

**Tolerance, derived before registering** (NOTES §1). The percentages are rounded to whole numbers, and the tenure
cohorts have a few hundred employees each, so a cell near 5 % carries sampling noise of roughly ±30 % in ratio. So
`log 1.5` is a loose test: it can catch a gross failure, not a subtle one. Degenerate case: if a non-default cell is
near 0 in both regimes, `δ` is dominated by the pseudo-count. Such rows are reported, not excluded.

**P2 is weak by construction:** the constant-ratio model has one free parameter per row, and the null has none.

**Reported, not predicted.** Every row's `Δ_<`, `Δ_>`, `δ`, `π_D` and `π_N`; `π_D`'s trend with tenure (the default's
pull should decay as people move).

**Decision rules.** D1: a failed prediction is recorded; corrected analyses are new and labelled post hoc. D2 as above.
**Falsifier of the purpose:** P1 fails. Then the framework's human actor does not fit this canonical default case, and
B12's identification cannot be used on it.

**Not shown, and why.**
- Hired-before and hired-after employees at the same tenure are observed at different calendar dates, so cohort
  differences can break exclusion without any endorsement effect.
- The categories `< default` and `> default` pool many rates. Pooling preserves the prediction under (E_A), but it
  weakens the test.
- No standard errors are published for the table.
