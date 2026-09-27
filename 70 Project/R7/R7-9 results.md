---
id: "R7-9 results"
type: "report"
updated: "2026-09-27"
---
# R7-9 — results: stopped by the registered rule D2

Pre-registered in [[R7-9 preregistration]] (sha256 `90ab57a9…`), pushed before any computation. The check is [[V37]].
Runs under rule 13's structural exception (the PI, after v7.5).

## Headline

**D2 fired as registered, and R7-9 is stopped.** P3 — the registered test of the reduction (a) — failed on one
instance of 300: a generic optimizer, from three starts, missed the ordinal measure by `1.4·10⁻³`. D2 said: "if the
reduction (a) fails for any existing measure, R7-9 stops and Def. 11 stays as it is." So Def. 11 is unchanged, and the
proposed Def. 19 and Prop. 34 are **not** in the core; their text is below. **Resuming is the PI's decision**, with a
check corrected as the diagnosis suggests, pre-registered again.

**What the diagnosis says** (post hoc, `70 Project/R7/r79_diagnose.py`, output `r79_diagnose_output.txt`): the reduction
did not fail. Over the 300 instances the generic value is never below the closed form, and it is above it only on
that one instance — 8 states, 8 levels — where 40 starts reach the closed form to `2·10⁻¹⁶`. A generic value above
an infimum is the optimizer not converging; only a value below would contradict the closed form. The registered
test could not tell the two apart.

## Predictions (all verification, rule 11)

| # | Outcome | Numbers | Diagnosis |
|---|---|---|---|
| P1 | held | minimizers from 5 starts agree to `1.5·10⁻⁸` on 400 generic log-convex hulls | |
| P2 | **failed as registered** | the smallest Pythagorean slack is `−1.1·10⁻⁸`, against `−10⁻⁸` | the generic minimizer is itself accurate only to about `10⁻⁸` (P1), so a slack of that size is solver noise. The registered threshold ignored the solver's accuracy — the NOTES failure mode "registering a threshold without deriving its scale", once more. On exact projections of log-convex sets the inequality is already checked to machine precision: the ordinal cone (V35, P4: `≥ −1.1·10⁻¹⁵`), the capped segment (V36, P2), the ray (V7, V14) |
| P3 | **failed as registered** — D2 | the capped measure reproduced to `9·10⁻¹⁶`; the ordinal measure missed by `1.4·10⁻³` on 1 of 300 | non-convergence, above (never below) the closed form |
| P4 | exploratory | the budget sphere intersected with a log-convex cone: 5 starts end more than `10⁻⁶` apart in 58 of 184 instances | consistent with the structural claim: sets that are not log-convex lose uniqueness. **Deviation:** the registered two-point hull meets the sphere in a single point, which cannot show non-uniqueness; V37 used the two-dimensional cone `{p ∝ q e^(aF + bG) : a, b ≥ 0}` instead |

V37's recorded output:

```
[V37] R7-9: the core as a declared intended set; log-convex sets (Def. 19, Prop. 34), against the pre-registration (P1-P4)
  P1 uniqueness on 400 generic log-convex hulls (K = 2, 3, 5): the minimizers from 5 starts agree to 1.5e-08 -> holds
  P2 Pythagorean inequality KL(p_hat||p) - M - KL(p°||p), 20 members per hull: min -1.1e-08 -> FAILS
  P3 generic code reproduces the capped free measure (two-point hull {q, p_(F,s)}): 8.9e-16; the ordinal measure (conic hull of level steps): 1.4e-03 -> FAILS
  P4 (exploratory) budget sphere intersected with a log-convex cone: 5 starts end more than 1e-6 apart in 58 of 184 instances with >= 2 feasible end points
```

**Second SIMD path.** V37 was rerun with AVX-512 disabled before its reference output was recorded: every verdict is
the same; P2's slack (`−1.5·10⁻⁸`) and P4's count (56) move, and V37's solver-bound numbers have declared tolerances in
`tools/reproduce_tolerances.json`.

## To resume (for the PI)

A corrected check, pre-registered: test the reduction on the *side* the claim makes (a generic value must never be
below the closed form), with enough starts to show convergence; and test Prop. 34(c)'s inequality only on
projections that are exact, or with a tolerance derived from the solver's accuracy. The proposed items follow,
unchanged.

## Proposed, not adopted: Def. 19

# Def 19 — declared intended set; R7-9

## Statement

**Definition 19 (declared intended set; R7-9).** Let `Δ°` be the set of full-support distributions on `X`.
- A **declaration** fixes a set `𝓘 ⊆ Δ°` of **intended behaviours**, closed in `Δ°`.
- The **misalignment** of a full-support `p̂` under `𝓘` is `M_𝓘(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`, undefined when `𝓘` is empty.
- `𝓘` is **log-convex** if, for all `p₀, p₁ ∈ 𝓘` and `λ ∈ [0, 1]`, the **geometric mixture**
  `p_λ = p₀^{1−λ}·p₁^{λ} / Σ_x p₀^{1−λ}·p₁^{λ}` is in `𝓘`.

## Notes and checks

*Note (what this definition does).* It states the measurement layer in one line: **misalignment is the KL projection
of the actual behaviour onto what the principal declared as intended.** Everything else the measurement layer
contains is a way to *generate* `𝓘` from declarations — the reference `q`, a target set (Def. Def 17|17), a convention
(Def. Def 8|8), a cap (Def. Def 18|18) — and Prop. Prop 34|34(a) shows each existing measure is a case. A new notion enters as a
new generator of `𝓘`, not as a new axiom. KL is fixed by detection (Prop. Prop 18|18), not by this definition.

*Note (the declaration registry).* Every declaration needs an elicitation story — how a real principal states it
— and a justified default. The registry, and the audit of choices still made silently, are in R7-9 results.

*Note (why log-convexity).* Prop. Prop 34|34(c): on a log-convex set the projection is unique and satisfies a
Pythagorean inequality. That is where every decomposition of the core comes from, and why the ordinal budget
measure, whose set is not log-convex, needed a solver.

## Proposed, not adopted: Prop. 34

# Prop 34 — the core as a declared intended set; R7-9

## Statement

**Proposition 34 (the core as a declared intended set; R7-9; tier 1).** Let `𝓘` be a declared intended set and `p̂` a
full-support behaviour (Def. Def 19|19).

(a) **Reduction.** The free and budget measures of Def. Def 10|10, of Def. Def 17|17 and of Def. Def 18|18 are `M_𝓘` for the
intended sets those definitions give: the half-ray `𝓡⁺_F`, the budget point, `I_free(𝒯)`, `I_budget(𝒯)`, the capped
segment, and the capped budget reference.

(b) **The contract as conditions on `𝓘`.** For every `𝓘` closed in `Δ°`, `M_𝓘` attains its infimum and satisfies M1
(with `𝓘` as the intended behaviours), M2, M4 and M6 of Def. Def 11|11. It satisfies M5 iff `𝓘` contains the declared
pursuit family, and M3 iff `𝓘` depends on the target only through the declared target set. M8 holds per context.

(c) **Log-convex sets.** If `𝓘` is log-convex and closed in `Δ°`, the minimizer `p°` is unique, and for every `p ∈ 𝓘`

```
KL(p̂‖p) ≥ M_𝓘(p̂) + KL(p°‖p),
```

with equality when the geometric line through `p` and `p°` continues in `𝓘` beyond `p°`.

(d) **Instances.** The half-ray, the capped segment and the ordinal cone `C_F` are log-convex. Thm Thm 13|13(a) is the
equality case of (c) on the full ray; the cross-term inequality of Prop. Prop 32|32(c) and the overshoot split of
Prop. Prop 33|33(b) are cases of (c).

## Proof

*Proof.* (a) By inspection of each definition: each measure is an infimum of `KL(p̂‖·)` over the set named.

(b) `KL(p̂‖p) ≥ p̂(x)·log(1/p(x)) − log |X|` for every `x`, so the sublevel sets of `KL(p̂‖·)` in a set closed in `Δ°`
are compact, and the infimum is attained. Hence `M_𝓘 = 0` iff `p̂ ∈ 𝓘` (M1), and `M_𝓘 ≥ 0` (M2). M4 and M6: `M_𝓘` is a
function of `(𝓘, p̂)`, undefined only by the explicit rule. M5: if `𝓘` contains the pursuit family, a pursuing `p̂`
lies in `𝓘` and scores 0; if it does not, a member outside `𝓘` scores positive by M1. M3: `M_𝓘` depends on the target
only through `𝓘`. M8: apply per context (Def. Def 9|9).

(c) Let `p₀, p₁ ∈ 𝓘` and `Z_λ = Σ_x p₀^{1−λ} p₁^{λ}`. Then
`f(λ) := KL(p̂‖p_λ) = (1−λ)·KL(p̂‖p₀) + λ·KL(p̂‖p₁) + log Z_λ`. `log Z_λ` is convex in `λ` (a log-sum-exp of affine functions),
and strictly so unless `p₀ = p₁`; so `f` is strictly convex along every geometric line in `𝓘`. Two distinct minimizers
would give a smaller value between them; so `p°` is unique. For `p ∈ 𝓘`, take `p₀ = p°`, `p₁ = p`: `f(λ) ≥ f(0)` on
`[0, 1]`, so `f'(0⁺) ≥ 0`, and `f'(0) = KL(p̂‖p) − KL(p̂‖p°) + d/dλ log Z_λ |₀ = KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p)`. If the
line continues in `𝓘` for `λ < 0`, then `f'(0) = 0` by minimality on both sides.

(d) Half-ray and capped segment: `p_{F,t}^{1−λ}·p_{F,t′}^{λ} ∝ p_{F,(1−λ)t+λt′}`, so a geometric mixture of two ray points is
the ray point at the convex combination of the intensities. Ordinal cone: `log(p/q)` is a non-decreasing function of
`F` for each member, and convex combinations of non-decreasing functions are non-decreasing. On the full ray every
point has the line continuing on both sides, which gives Thm 13(a)'s equality. ∎

## Notes and checks


*Reading.* **Every decomposition in the measurement layer is one inequality.** The Pythagorean splits, the
ordinal/shape split and the overshoot term all come from convexity of the divergence along geometric lines. What a
declaration must preserve for the measure to behave well is log-convexity. The budget sets (spheres of fixed
divergence from `q`) are not log-convex, and that is where the core needed a non-convex solver (R7-7, D4).

*Prior art.* Information projections and their Pythagorean identities: Csiszár (1975); for the reverse projection,
minimizing over the second argument, and log-convex sets, Csiszár & Matúš (2003). Bibliographic details not checked
(no network access in this session).
