---
id: "Thm 9"
type: "theorem"
title: "the worst-case regret is not separable"
section: "Core 05 Non-separability"
order: 26
layer: "explanation"
tier: ["2"]
assumes: []
status: "proved"
depends_on: ["Thm 5", "Lemma 8", "Prop 6", "Def 6"]
mentions: ["B03"]
checks: ["V05"]
sources: []
aliases: ["Theorem 9", "Thm. 9"]
updated: "2026-09-26"
---
# Thm 9 — the worst-case regret is not separable
<!-- gen:header -->
> [!abstract] Theorem · tier 2 · proved · in [[Core 05 Non-separability]]
<!-- /gen:header -->

## Statement

**Theorem 9 (the worst-case regret is not separable).** Let `E₁` be non-constant, `A ⊂ X` with `q(A) = r ∈ (0,1)`.
Then

```
lim_{δ→0} w_δ(E₁)/w_δ(1_A) = √( Var_q(E₁) / (r(1−r)) ),   and   w_δ(E₁)/w_δ(1_A) = osc(E₁) for all δ ≥ δ̄,
```

with `δ̄ = max{log 1/q(argmax E₁), log 1/q(argmin E₁), log 1/r, log 1/(1−r)}`. Hence, for the pair
`{E₁, M·1_A}` (any `M > 0`; `w_δ` is positively homogeneous),
`K ≥ √(Var_q E₁)/(osc(E₁)·√(r(1−r)))`. `K` is unbounded over any family of instances in which `q(A) → 0`
while `Var_q(E₁)/osc(E₁)²` stays bounded away from 0. By Theorem [[Thm 5|5]](ii) and Lemma [[Lemma 8|8]], **no bound on the
worst-case regret of the pure capacity maximizer (`β = ∞`) of the form `a(E)·b(δ)` has bounded looseness.**

## Proof

*Proof.* Prop. [[Prop 6|6]](ii) on both errors, using `Var_q(1_A) = r(1−r)`; Prop. [[Prop 6|6]](iii) on both, using `osc(1_A) = 1`. ∎

## Notes and checks

*Check.* [[V05|V5]] (`n = 200`, `r = min q`): ratio 62.80 at `δ = 10⁻⁶` vs predicted 62.7957; 5.3013 at large `δ` vs
`osc(E₁) = 5.3013`; `K ≥ 11.8`, so any separable bound is ≥ 3.4× loose on this pair.

**Fixed intent (measured, not proved).** For a single fixed `F` (`n = 2000`, uniform `q`, `β = 30`), a dense
error (`sd_q = 0.61`) and a one-state spike (`sd_q = 0.13`) give `R^C(E₁)/R^C(E₂)` from 13.45 at
`δ = 0.002` to 0.13 at `δ = 7`, a ×103 span. Any separable bound is therefore ≥ 10× loose somewhere on this
pair. [[V05|V5]].

> **"Which of two errors is worse" has no capacity-free answer.** At small capacity errors are ranked by
> their variance under the reference; at large capacity, by their extremes. This is the regressional /
> extremal Goodhart distinction, derived here as the two asymptotes of one support function
> ([[B03|B §3]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 6]] — width
- [[Lemma 8]] — separable bounds are loose when rankings move
- [[Prop 6]] — the width, computed
- [[Thm 5]] — the width is the exact worst case

## Used by
- [[B03]] — Goodhart variants — Manheim & Garrabrant (2018)
- [[C03]] — Non-separability (Lemma 8, Thm 9)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C08]] — Crossing curves *(tested in R5 on best-of-n and vanilla policy gradient: holds)*

## Mentions
- [[B03]] — Goodhart variants — Manheim & Garrabrant (2018)

## Mentioned in
- none

## Checks
- [[V05]]

## Sources
- none

## Retractions touching this note
- [[R033]]
- [[R051]]
<!-- /gen:links -->
