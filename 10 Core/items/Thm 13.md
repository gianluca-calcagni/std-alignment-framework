---
id: "Thm 13"
type: "theorem"
title: "intent-ray decomposition"
section: "Core 07 Identification, gauge, and the intent ray"
order: 31
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Thm 1", "Def 10", "Def 3"]
mentions: ["R050"]
checks: ["V07", "V14"]
sources: ["src Amari 2000", "src Bregman 1967", "src Csiszár 1975", "src Skalse 2024"]
aliases: ["Theorem 13", "Thm. 13"]
updated: "2026-09-26"
---
# Thm 13 — intent-ray decomposition
<!-- gen:header -->
> [!abstract] Theorem · tier 1 · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Theorem 13 (intent-ray decomposition).** Let `F` be non-constant, and let `A(t) = log E_q e^{tF}`. There
is a unique `t̂ ∈ ℝ` with `E_{p_{F,t̂}}F = E_{p̂}F`; `t̂ < 0` iff `E_{p̂}F < E_qF`.

(a) *(Full ray.)* For every `t ∈ ℝ`: `KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t})`.

(b) *(Half-ray; canonical from v6.1.)* Let `t̂⁺ = max(t̂, 0)`. For every `t ≥ 0`:

```
KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂⁺}) + KL(p_{F,t̂⁺}‖p_{F,t}) + t·[E_qF − E_{p̂}F]⁺.
```

With `t = β` and Theorem [[Thm 1|1]]:

```
β·R_J = D_⊥ + D_∥ + X_anti,
  D_⊥    = KL(p̂‖p_{F,t̂⁺}) = min_{t≥0} KL(p̂‖p_{F,t})        (transverse error)
  D_∥    = KL(p_{F,t̂⁺}‖p*) = A(β) − A(t̂⁺) − (β − t̂⁺)A'(t̂⁺)  (axial error: right objective, wrong intensity)
  X_anti = β·[E_qF − E_{p̂}F]⁺                             (anti-alignment excess; nonzero iff t̂ < 0)
```

## Proof

*Proof.* `t ↦ E_{p_{F,t}}F` is continuous and strictly increasing (derivative `Var > 0`), with limits
`min F`, `max F`, and `p_{F,0} = q`. `E_{p̂}F` lies strictly between the limits because `p̂` has full support;
this gives existence, uniqueness, and the sign statement.

(a) `log(p_{F,t̂}/p_{F,t}) = (t̂ − t)F − A(t̂) + A(t)` is affine in `F`, so its expectation under `p̂` equals its
expectation under `p_{F,t̂}` (Csiszár's Pythagorean identity).

(b) If `t̂ ≥ 0`, this is (a). If `t̂ < 0`, then `t̂⁺ = 0` and
`KL(p̂‖p_{F,t}) − KL(p̂‖q) − KL(q‖p_{F,t}) = E_{p̂}[−tF + A(t)] − E_q[−tF + A(t)] = t(E_qF − E_{p̂}F)`.

Finally, by (a), `KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + [A(t) − A(t̂) − (t − t̂)A'(t̂)]`: a constant plus a convex
function of `t` with unconstrained minimizer `t̂`. So its minimum over `t ≥ 0` is at `t̂⁺`, which identifies
`D_⊥` (Def. [[Def 10|10]]) with `KL(p̂‖p_{F,t̂⁺})`. ∎

## Notes and checks

*Check.* [[V07|V7]] checks (a), to `5.5·10⁻¹²` over 5,000 instances. [[V14]] checks (b), to `3.0·10⁻¹³` over 3,000
instances, 1,052 of them anti-aligned (`t̂ < 0`).

**Reading.**
- `D_⊥` is what no positive rescaling of the target can produce.
- `D_∥` is the cost of pursuing the target itself at the wrong intensity.
- `X_anti` is the extra cost of net movement *against* the target.

With the half-ray, `F̂ = −F` has `D_⊥ = KL(p̂‖q) > 0`, so anti-alignment is no longer invisible to the
transverse part (the v6 full-ray definition gave `D_⊥ = 0`; [[R050|row 50]], 54). The half-ray
matches the quotient by **positive** rescalings used by STARC (Skalse et al., ICLR 2024), which compares
reward functions rather than behaviours. The decomposition still says *where* the regret lies; `β·R_J`
says how large it is.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Thm 1]] — regret is a divergence

## Used by
- [[B01]] — Anchor
- [[B13]] — Potential games — collective behaviour is a tilt (Blume 1993) *(new in v6.2)*
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Cor 13.2]] — convention-freedom
- [[Cor 13.3]] — rescaling is purely axial
- [[Cor 13.4]] — second order
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Prop 35]] — the intended segment against the contract; R7-6b
- [[Prop 36]] — declared resolution against the core; R7-10
- [[Prop 37]] — the value shortfall; R8-1
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentions
- [[R050]]

## Mentioned in
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V07]]
- [[V14]]

## Sources
- [[src Amari 2000]]
- [[src Bregman 1967]]
- [[src Csiszár 1975]]
- [[src Skalse 2024]]

## Retractions touching this note
- [[R054]]
- [[R068]]
<!-- /gen:links -->
