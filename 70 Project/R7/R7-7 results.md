---
id: "R7-7 results"
type: "report"
updated: "2026-09-26"
---
# R7-7 — results: target sets, with the ordinal target as the lead case

Pre-registered in [[R7-7 preregistration]] (sha256 `21170433…`), committed and pushed (`28903d4`) before any
R7-7 computation. The check is [[V35]]. The post-hoc diagnosis of the failures is `70 Project/R7/r77_diagnose.py`,
with its output in `r77_diagnose_output.txt`. It is not pre-registered and not a `verify.py` block.

## The headline: D4 fired as registered

**Under the free convention, the ordinal target repairs R7-5's defect exactly.** `M_ord` has a closed form
(Prop. [[Prop 32|32]]), and it is 0 to `3·10⁻¹⁶` on every best-of-`k` and quantilizer behaviour run on the true target.

**Under the budget convention — the default — the registered falsifier D4 fired.** The ordinal budget measure
has no closed form, and V35 computes it with a five-start solver. On one R7-5 case of 393, a quantilizer on 12
levels, the solver returned `7.3·10⁻⁶` nats instead of reaching `10⁻⁸`. By the registered rule, the ordinal
declaration therefore does not yet repair the defect under the default convention.

What the diagnosis adds, without changing that verdict:
- The true value on that instance is 0. The quantilizer lies in the ordinal cone and on its own budget sphere,
  so it is an intended behaviour (Prop. [[Prop 31|31]](b), M5). What failed is the computation, not the definition.
- The failure is visible without knowing the answer: it is an instance on which the five starts disagreed.
- A zero needs no solver: `M_budget([F]_ord) = 0` iff `M_ord = 0` (Prop. [[Prop 32|32]](f)). So the budget measure's verdict
  "aligned" is exact. Its *non-zero values* carry solver error, and are quoted only where the starts agree.

## Predictions

| # | Outcome | Numbers | Diagnosis |
|---|---|---|---|
| P1 (R) | held | the generic optimum is never below the isotonic value by more than `3.3·10⁻¹⁵`; 610 of 1,200 instances have tied levels | the probe's check, now with ties. The probe's own code ran the regression per state, which is right only without ties |
| P2 | held | block formula to `7·10⁻¹⁶` | |
| P3 | held | budget split to `9·10⁻¹⁶` | |
| P4 (R) | held | cross term `≥ −1.1·10⁻¹⁵`; (d) slack `≥ −7·10⁻¹⁵` | |
| P5 | held | 0 disagreements with the independent cone test; kind F's smallest `M_ord` is `4.4·10⁻⁴` | |
| P6 | **failed as registered** | `M_ord` unchanged to the last bit (held). The cardinal `M_free` moved in 53.8 % of kind-A instances, against the predicted ≥ 95 % | 93 of the 184 behaviours are anti-aligned (`E_p̂F ≤ E_qF`). There `t̂⁺ = 0`, and `M_free = KL(p̂‖q)` whatever the target. Among the aligned, 100 % moved. The prediction forgot the half-ray's endpoint. It was not proof-backed |
| P7 | **failed as registered** on two of three parts | `M_ord ≤ 3.3·10⁻¹⁶` (held, R). The ordinal budget measure: `≤ 10⁻⁸` in 392 of 393, `7.3·10⁻⁶` in one (D4). The cardinal `M_free > 10⁻⁶` in 89.9 %, against ≥ 90 % (R) | the budget part: above. The cardinal part: best-of-64 on 3–12 states puts essentially all its mass on the top level, where the cardinal measure is below `10⁻⁶` too (45 % of `k = 64` cases, against 92.5 % in the probe, which used more states) |
| P8 | **failed as registered** (strictness only) | the inequalities of Prop. 32(f) held on 1,123 instances. The first was not strict by more than `10⁻¹²` in 4 instances, all with `M_ord < 3·10⁻⁷` | the gap is second order in `M_ord`: the median of `gap/M_ord²` is 0.93, 1.33 and 1.83 in the three bins where it can be resolved (`M_ord` from `10⁻⁶` to `10²`), and at noise level below. The registered threshold ignored that scaling. **Under D2 the strict claim is withdrawn from Prop. 32(f).** The proof of strictness is sound; a restated claim needs a check designed from the scaling |
| P9 | held | evaluation `≤ 3.3·10⁻¹⁶`; deployment `≥ 2.2·10⁻⁴` | |
| P10 | **failed as registered** on both parts; no v7.3 number changed | reproduction: V1–V34, F1–F5, F7 and F8 reproduce; F6 differs. Implementation: `M_free` to `1.3·10⁻¹²`; `M_budget` differed by `2.1·10⁻⁸` in one instance | F6 counts the results and blocks in the core, and R7-7 adds three results and a block (61 → 64, 34 → 35); the prediction should have excluded that line. The implementation difference is on a budget measure of 4,473 nats at `λ = 3,239`, a relative difference of `4.8·10⁻¹²`; the registered tolerance was absolute |

## Decision rules

- **D1** passed: the best two starts agree to `10⁻⁷` in 98.7 % of the 1,123 instances where the budget measure is
  defined. By the registered rule its numbers are quotable. D4 shows the rule was weaker than it looked: a
  global rate hides the one instance that matters. **Adopted (stricter than registered):** a value of
  `M_budget([F]_ord)` is quoted only where its own starts agree, and a zero is certified by `M_ord = 0`.
- **D2** applied to P8: the strict inequality is out of the statement.
- **D3** did not fire. Lint reports 0 errors, and no v7.3 number changed: P10's reproduction part failed only on
  F6's count line, which R7-7 changes by construction (below).
- **D4** fired: the headline.

## Exploratory (no prediction)

- **X1.** Kinds A and E, where `M_ord > 0`: `M_budget([F]_ord) / M_ord` has median 1.16 [p10 1.00, p90 2.42], and
  `M_budget([F]_ord) / M_budget` has median 0.62 [0.11, 0.99]. The ordinal budget measure usually sits close to the
  ordinal free measure, well below the cardinal budget measure.
- **X2** (explanation layer). On kind E, the share of the cardinal `M_free` that is ordering error has median 0.26
  at `σ = 0.05` and `σ = 0.3`, and 0.50 at `σ = 1`. **R7-5's reading did not replicate on this generator.** R7-5
  found 0.02 at `σ = 0.05` and read it as "for nearly correct evaluators, almost all of the cardinal misalignment is
  shape". V35's noise is added to log-probabilities of a tilt, R7-5's to the evaluator. The share is
  generator-dependent, as [[NOTES_claude]] H8 warned; it should not be quoted outside one generator.
- **X3.** On kinds A and E, `p°` pools more than one level in 65.5 % of instances.

## Reproduction (P10) and a second SIMD path

**M7 in numbers.** After all R7-7 edits, `tools/reproduce.py` reran every block: V1–V34 reproduce, and so do
F1–F5, F7 and F8. F6 differs in one line, the count of results and blocks it cross-references (61 → 64 results,
34 → 35 blocks), which R7-7 changes by adding Def. 17, Props 31–32 and V35. Its reference line is updated.

**A second SIMD path.** V35 was rerun with AVX-512 disabled (`NPY_DISABLE_CPU_FEATURES=X86_V4
OPENBLAS_CORETYPE=Haswell`) before its reference output was recorded. Every verdict is the same. Three
solver-dependent numbers move, and each now has a declared tolerance with its reason in
`tools/reproduce_tolerances.json`:
- the size of the one D4 failure, `7.3·10⁻⁶` against `2.3·10⁻⁶`. It exceeds the registered `10⁻⁸` on both paths;
- D1's agreement rate, 0.987 against 0.986;
- P10's largest `M_budget` difference, `2.1·10⁻⁸` against `2.2·10⁻⁸`.

The rest are residual-scale digits.

## What changed in the core

- **New:** Def. [[Def 17|17]] (target sets, the ordinal cone, intended sets, the measures); Prop. [[Prop 31|31]] (target sets against
  the contract); Prop. [[Prop 32|32]] (the ordinal measure: closed form, block formula, decomposition, budget split,
  order invariance, the budget measure's bounds and zero set); [[V35]].
- **Restated:** Def. [[Def 11|11]] (M1, M3 and M5 refer to the declared target set); Def. [[Def 12|12]] (an instance is `(X, q, 𝒯, κ)`).
  Notes on Defs [[Def 8|8]] and [[Def 10|10]], Prop. [[Prop 24|24]] and Overview [[Overview 0|0]]. No proof changed.
- **M7:** for `𝒯 = [F]₊` every definition reads as before, so every v7.3 measure is the cardinal case.

## Open

- A closed form, or a certified algorithm, for `M_budget([F]_ord)`.
- The strict inequality in Prop. 32(f), with a check designed from its second-order scaling.
- Aggregating a family of target sets (disagreeing principals). The framework measures per principal and
  declares no aggregate.
