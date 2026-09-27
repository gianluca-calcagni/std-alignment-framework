---
id: "R8 foundations review"
type: "report"
updated: "2026-09-27"
---
# R8 — foundations review: hidden assumptions, simplifications, coherence (after T7)

Asked for by the PI after T7: re-read the core, the diagnostics and the predictions; find hidden assumptions and
simplifications that should have been avoided; check that the reasoning is coherent and sound. Read for this review:
Defs 1, 2, 8–11, 13, 17, 19, 21; Thms 1, 13; Lemma 5.1; Props 18, 26, 34, 36; B12; R7-5; R7-9's registry; every T7
note. **No proof read was found wrong.** Prop. 36(c)'s key step (`λ_𝒢 ≥ t̂`, by the maximum-entropy property of the
tilt) was re-derived and holds. The problems are in what the mathematics is taken to mean, and in how T7 used it.

Severity: **high** means it changes a headline claim; **medium** means it changes how a result must be read; **low**
is wording.

## A. The core

**A1 (high) — "misalignment" measures distinguishability, not harm.**
- M3 makes every measure invariant to `F ↦ aF + c`. The number, in nats, says how far behaviour is from intended
  behaviour in information, not how bad the gap is. Scaling the stakes by 1000 leaves `M` unchanged.
- Only the price measure carries value units, `R_J = KL/β`, and only at a declared price.
- The word "misalignment", and phrases like "ε-aligned", invite a harm reading that the definitions do not support. A
  rare catastrophic outcome and a rare harmless one, with the same probabilities, score the same.
- **Fix:** say this in Def. 8 and in the Status abstract. Report `R_J` in value units whenever a price is declared. A
  principal who cares about stakes needs a value-weighted measure, which the core does not offer.

**A2 (high) — every measure is relative to an entropic principal.**
- The default intended behaviours are Gibbs tilts of `q`. KL is *the* measure only because the principal's value is
  taken to be `E_p F − KL(p‖q)/β` (Thm 1). R7-5 states this correctly: "no [choice], once the intent is entropic".
- R7-9's registry shortened it to "forced by detection", which is wrong. Detection gives Chernoff and Stein exponents
  (Prop. 18), which bound `KL(p̂‖p*)` but do not select that divergence or its direction. **Corrected in R7-9 results**
  with this review.
- Real principals rarely state an entropic intent. R7-7, R7-6, R7-9 and R7-10 widen the intended *set*, but its
  default, and the reason the divergence is KL, remain the entropic principal.

**A3 (high) — the framework has population quantities and no estimation layer.**
- Every measure is a functional of true distributions. Real use plugs in empirical frequencies. Plug-in KL is biased
  upward (about `(k−1)/2n` nats for `k` cells), dominated by small cells, and sensitive to pseudo-counts: T7 used 0.5,
  0.005 and 0.5 percentage points without justification.
- The "statistical layer" sits under ROADMAP's "Later". It is a prerequisite for any diagnostic.
- **Fix:** before any further empirical step, adopt a minimal estimation protocol: bootstrap intervals, a bias
  correction, and a pseudo-count sensitivity check.

**A4 (medium–high) — the outcome space `X` and the reference `q` are modelling choices that dominate the numbers.**
- By data processing, a measure on a coarsening of `X` is a lower bound on the measure on `X` (Prop. 36(d)). Real
  computations are on coarse bins, so they are lower bounds, and results on different `X` are not comparable.
- T7 shows the size of the effect. Changing length from a binary relation to quartiles moved one correlation from
  0.276 to 0.083. Changing `q` changes every number.
- "Substrate-free" is true of the mathematics, not of the numbers. Every reported value should name its `X` and its `q`.

**A5 (medium) — the default convention is the one with the known defects.**
- Def. 8 names the budget measure "misalignment (the default)". Since then:
  - it misreads style as pursuit (`Θ`, Prop. 36(c));
  - it is undefined at saturation;
  - its ordinal version is not log-convex and needs a solver (R7-7).
- The free measure has none of these defects, and caps and floors now declare intensity explicitly (R7-6a, R7-6b).
- **Proposal for the PI:** make `free` the default, and keep `budget` as a declared option.

**A6 (medium) — the budget "intended set" is not a declaration.**
- Def. 19 says a declaration fixes `𝓘`. Under the budget convention, `𝓘` is the ray point at `p̂`'s own KL level, so it
  depends on the behaviour being judged.
- Prop. 34 still holds, since `M_𝓘` is evaluated with that set. But "misalignment is the projection onto what the
  principal declared" is true only of the free-type measures. Under the budget convention the declaration is a
  *family* indexed by the agent's spending. State this.

**A7 (medium) — exact maximizers and deterministic intents are degenerate.**
- At `β = ∞`, `p* = q(·|argmax F)` lacks full support, so `KL(p̂‖p*) = ∞` for any `p̂` off `argmax F`. The same
  saturation hits continuous `X` (R7-5, case 5).
- These cases (exact optimization, deterministic control) are among the most important for alignment. The core covers
  them only by declaring them undefined or by coarsening.

**A8 (medium, known) — contexts are exogenous and averaged linearly.**
- An agent that chooses its contexts falls outside Def. 9.
- A rare catastrophic context is averaged away under `Σ ρ(c)·M_c`.
- Both are recorded (A8 frame exogeneity; the M8 candidate). They remain real limits.

## B. How T7 used the framework

**B1 (high) — case 2 never measured misalignment.**
- Case 2 tested B12's identification of the chooser's reference: (E_A) and exclusion, which belong to the explanation
  layer.
- No target `F` was declared, no measure was computed, and no diagnosis table was produced.
- So "the human case failed its clean test" is a result about an actor model, not about the framework's diagnostics.
  §4b item 3 remains untested, not failed, for humans. **Corrected in T7 summary** with this review.

**B2 (high) — case 1's targets were binary, which barely exercises the core.**
- With a two-level target (win/lose, gold/not gold), the intent half-ray contains every behaviour that beats `q` on
  the target. For any such behaviour the free measure is exactly the within-cell term. T7-1's P5 degeneracy was one
  instance of this.
- So case 1 tested the chain rule of KL on 2×2 tables: correct, but thin. The cardinal structure (exchange rates,
  intensity, the ray) was never engaged by real data.

**B3 (high) — forking paths across designs.** Each registration was honest. Taken together:

| Case | Empirical predictions held |
|---|---|
| Case 1 (T7-1, 1b, 1d) | 1 of 7 (plus 1 that could not fail) |
| Case 2 (T7-2, 2b, 2d) | 4 of 8 (1 more untestable) |
| **Total** | **5 of 15** |

- Case 1's one success came after two failed designs and a search for a better dataset.
- Two amendments followed partial exposure: T7-1c (coverage counts seen) and T7-2c (bar heights seen).
- Read the single held prediction (LLMBar, ρ 0.52) with this in mind.

**B4 (medium) — the thresholds had no sampling model.**
- Spearman > 0.3 and `|δ| ≤ log 1.5` were chosen without power calculations or standard errors.
- Several verdicts sit on the thresholds (0.276, 0.285, 0.265). Those are coin-flips, not findings.
- Same fix as A3.

**B5 (low–medium) — case 2d's explanation is one of several.**
- "The default enters the evaluator" competes with other explanations: the 6% match kink, the difference in cohort
  timing, and affordability.
- The data reject B12's point-mass family. They do not identify why.

## What holds up

- The mathematics: every verification prediction held on real data, and no proof read was wrong.
- The discipline: pre-registration caught two post-hoc patterns, and the stop rules caught data-reading errors.
- The structure: decompositions with named terms and levers. It is a correct and useful vocabulary, not yet a validated
  instrument.

## Recommended order (budget-aware)

1. **Wording, cheap:** A1 (stakes) in Def. 8 and the abstract; A6 in Def. 19's notes. Done now, in project notes only:
   the R7-9 registry row (A2) and T7 summary (B1, B3).
2. **One PI decision:** the default convention (A5).
3. **Before any more empirical work:** the estimation protocol (A3, B4).
