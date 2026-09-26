---
id: "Prop 31"
type: "proposition"
title: "target sets against the contract; R7-7"
section: "Core 09 Observation what an overseer can detect"
order: 51.5
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 17", "Def 10", "Def 11", "Lemma 5.1", "Def 9"]
mentions: ["Prop 32", "R7-7 preregistration", "R7-7 results"]
checks: ["V35"]
sources: []
aliases: ["Proposition 31", "Prop. 31"]
updated: "2026-09-26"
---
# Prop 31 — target sets against the contract; R7-7
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Proposition 31 (target sets against the contract; R7-7; tier 1).** Let `𝒯` be a target set (Def. [[Def 17|17]]) and
`p̂` a full-support actual behaviour.

(a) For `𝒯 = [F]₊`: `I_free(𝒯) = 𝓡⁺_F`, and `M_free(𝒯)` and `M_budget(𝒯)` are the measures `M_free` and `M_budget` of
Def. [[Def 10|10]], defined in the same cases.

(b) `M_free(𝒯)` satisfies M1–M6 and M8 of Def. [[Def 11|11]], with intended set `I_free(𝒯)`. `M_budget(𝒯)` satisfies them
wherever it is defined, with intended set `I_budget(𝒯)`. Both infima are attained.

(c) If `𝒯 ⊆ 𝒯′`, then `M_κ(𝒯′) ≤ M_κ(𝒯)` wherever both are defined, and `M_free(𝒯) ≤ M_budget(𝒯)`. In particular
`M_κ([F]_ord) ≤ M_κ([F]₊)`.

## Proof

*Proof.* (a) The half-ray of `aF + c` is `{p_{F,at} : t ≥ 0} = 𝓡⁺_F`, so the union over `[F]₊` is `𝓡⁺_F`. It is closed
in `Δ°`: its limit points as `t → ∞` are supported on `argmax F`, a proper subset of `X`. By Lemma [[Lemma 5.1|5.1]], `𝓡⁺_F`
meets `{p : KL(p‖q) = k}` in the single point `p_{F,λ}` when `k < log 1/q(argmax F)`, and nowhere otherwise. These
are the measures of Def. [[Def 10|10]] and its saturation rule.

(b) For every `x`, `KL(p̂‖p) ≥ p̂(x)·log(1/p(x)) − log |X|`, so `KL(p̂‖p) → ∞` as `p` approaches the boundary of
the simplex. Each sublevel set `{p ∈ I : KL(p̂‖p) ≤ c}` of a set `I` closed in `Δ°` is therefore compact, and the
infimum over `I` is attained. Hence `M = 0` iff `p̂ ∈ I` (M1), and `M ≥ 0` (M2).
- M3: the measure is defined from `𝒯` as a set, and neither convention carries a unit.
- M4 and M6: the measure is a function of `(q, 𝒯, p̂)`, and `M_budget(𝒯)` is undefined only by the explicit rule.
- M5: if `p̂ = p_{G,t}` with `G ∈ 𝒯` and `t ≥ 0`, then `p̂ ∈ I_free(𝒯)`; and since `KL(p̂‖q) = k`, also `p̂ ∈ I_budget(𝒯)`.
- M8: apply the measure per context (Def. [[Def 9|9]]).

(c) A larger target set has a larger intended set under either convention, and `I_budget(𝒯) ⊆ I_free(𝒯)`. An
infimum over a larger set is smaller. `[F]₊ ⊆ [F]_ord`, since `v ↦ av + c` is strictly increasing for `a > 0`. ∎

## Notes and checks

*Check.* [[V35]] (pre-registered, [[R7-7 preregistration]]):
- (a): the target-set code for `[F]₊` returns Def. [[Def 10|10]]'s reference code's `M_free` to `1.3·10⁻¹²`, and `M_budget`
  to relative `4.8·10⁻¹²`. *As registered* the tolerance was an absolute `10⁻¹⁰`, and one instance failed it: a
  budget measure of 4,473 nats, at `λ = 3,239`, differs by `2.1·10⁻⁸` (P10; [[R7-7 results]]).
- (b), for `[F]_ord`: `M_ord = 0` agrees with an independent membership test for `C_F` in all 1,200 instances.
  M5 holds for monotone, best-of-`k` and quantilizer behaviours, and a sign-flipped behaviour always scores
  positive (smallest `4.4·10⁻⁴`). A two-context agent scores 0 in evaluation and positive in deployment (M8).
- (b), for `M_budget([F]_ord)`: its value comes from a non-convex solver. On the 393 best-of-`k` and quantilizer
  cases where it is defined, the solver reached `≤ 10⁻⁸` in 392, and `7.3·10⁻⁶` in one, a 12-level quantilizer on
  which its five starts disagreed. The true value there is 0 by M5. That one case fired the registered
  falsifier D4 ([[R7-7 results]]). Membership in `I_budget` needs no solver: see Prop. [[Prop 32|32]](f).

*Reading.* **The contract survives the move from one target to a set of targets unchanged in form.** M1, M3 and M5
now refer to the declared set, and for `[F]₊` they are word for word what they were. A set of targets can only
lower the measures: declaring less about the intent can only excuse more behaviour.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 17]] — target sets; R7-7
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- none

## Mentions
- [[Prop 32]] — the ordinal measure; R7-7
- [[R7-7 preregistration]]
- [[R7-7 results]]

## Mentioned in
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 17]] — target sets; R7-7
- [[Prop 24]] — the v6.4 measures against the contract; tier 1

## Checks
- [[V35]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
