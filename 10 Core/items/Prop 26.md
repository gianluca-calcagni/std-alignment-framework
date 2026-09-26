---
id: "Prop 26"
type: "proposition"
title: "reference misspecification is measured misalignment; R7-2"
section: "Core 07 Identification, gauge, and the intent ray"
order: 40.5
layer: "explanation"
tier: ["4 (E_A)"]
assumes: ["Hyp E_A"]
status: "proved"
depends_on: ["Def 13", "Def 10", "Prop 12", "Lemma 5.1", "Cor 13.4"]
mentions: ["B12", "Def 8"]
checks: ["V32"]
sources: []
aliases: ["Proposition 26", "Prop. 26"]
updated: "2026-09-26"
---
# Prop 26 — reference misspecification is measured misalignment; R7-2
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E_A) · assumes [[Hyp E_A]] · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Proposition 26 (reference misspecification is measured misalignment; R7-2).** *[Assumes (E_A).]* Let
`p̂ = p^{q_A}_{F̂,β}` with `β ∈ (0, ∞)` (hypothesis (E_A), Def. 13), and let `h = log(q_A/q)`, defined up to an
additive constant. The measures `M_free`, `M_budget` are those of Def. 10, relative to the declared `q`.

(a) **(Absorption.)** `p̂ = p_{F̂ + h/β, β}`. So `p̂` satisfies (E) from the declared reference with the effective
error `E_A = E + h/β`, and every result stated under (E) holds under (E_A) with `E` replaced by `E_A`.

(b) **(No behavioural test separates the two loci.)** For every `q_A` there is an evaluator — `F̂ + h/β` — with
which an actor from the declared reference produces the same behaviour. Conversely, for every evaluator error
`E'` there is a reference — `q_A ∝ q·e^{βE'}` — with which an actor pursuing `F̂ − E'` produces the same
behaviour.

(c) **(Right target, own default.)** Let `F̂ = F`, with `F` non-constant. Then `M_free = 0` iff `h = aF + c` on `X`
for constants `a`, `c` with `β + a ≥ 0`. In that case `M_budget = 0` as well. Otherwise `M_free > 0` and,
where defined, `M_budget > 0`.

(d) **(Second order.)** Let `F̂ = F` and `h = εh₀`. As `ε → 0`,
`M_free = (ε²/2)·Var_{p*}(h₀⊥) + O(ε³)`, where `h₀⊥ = h₀ − a₀F` and `a₀ = Cov_{p*}(h₀, F)/Var_{p*}(F)`.

(e) **(Limits in the optimization strength.)** Let `F̂ = F`.
- If `argmax F` is a single behaviour, then `M_free → 0` as `β → ∞`.
- As `β → 0`, `M_free → inf_{t≥0} KL(q_A ‖ p_{F,t})`.

## Proof

*Proof.*
(a) `p^{q_A}_{F̂,β} ∝ q_A·e^{βF̂} ∝ q·e^{h + βF̂} = q·e^{β(F̂ + h/β)}`. A result under (E) is a statement about
`p_{F + E, β}`; apply it with `E_A` in place of `E`.

(b) Part (a) read in both directions, with `h = βE'`. This is Prop. 12(ii) seen from the declared reference.

(c) With `F̂ = F`, `p̂ ∝ q·e^{βF + h}`. The curve `t ↦ KL(p̂‖p_{F,t})` is continuous and convex, and tends to `+∞` as
`t → ∞`: `p̂` has full support, and `p_{F,t}` loses mass on every behaviour outside `argmax F`, which is a proper
subset because `F` is non-constant. So its infimum over `t ≥ 0` is attained. Hence `M_free = 0` iff
`p̂ = p_{F,s}` for some `s ≥ 0`. Both have full support, so this holds iff `βF + h = sF + c`, i.e. `h = aF + c`
with `a = s − β ≥ −β`. If `p̂ = p_{F,s}`, then `KL(p̂‖q) = KL(p_{F,s}‖q)`, so the budget point is `λ = s`
(Lemma 5.1) and `M_budget = 0`. If `p̂` is off the half-ray, `M_budget = KL(p̂‖p_{F,λ}) > 0`.

(d) By (a), `p̂ = p_{F + εh₀/β, β}`, an error `εE₀` with `E₀ = h₀/β`. Cor. 13.4 gives
`D_⊥ = (β²ε²/2)·Var_{p*}(E₀⊥) + O(ε³) = (ε²/2)·Var_{p*}(h₀⊥) + O(ε³)`, and `M_free = D_⊥`.

(e) `M_free ≤ M(β) = KL(p̂‖p*)`. By (a), `p̂ ∝ p*·e^{h}`, so `KL(p̂‖p*) = E_{p̂}h − log E_{p*}e^{h}`. As `β → ∞`,
both `p̂` and `p*` converge to the point mass at `argmax F`, and both terms converge to `h(argmax F)`. As
`β → 0`, `p̂ → q_A` uniformly on the finite `X`. The curves `t ↦ KL(p̂‖p_{F,t})` converge uniformly on compact
sets. Their minimizers over `t ≥ 0` stay in a bounded interval: near `q_A`, `p̂(x)` is bounded below
uniformly, and `−log p_{F,t}(x)` grows linearly in `t` for every `x` outside `argmax F`. So the infima
converge. ∎

## Notes and checks

*Check.* [[V32]]:
- (a) to `7·10⁻¹⁵` in log-probability over 2,000 instances.
- (c) over 600 instances:
  - `M_free` and `M_budget` are both below `2·10⁻¹⁵` when `h = aF + c` with `a > −β`;
  - both are positive when `a < −β`: `M_free ≥ 9·10⁻⁵`;
  - both are positive for random `h`.
- (d) the ratio is 0.873, 0.951, 0.984 and 0.995 at `ε = 0.3, 0.1, 0.03, 0.01`.
- (e) on one instance, `M_free` is 0.545 nats at `β = 0.25` (the `β → 0` limit is 0.535), peaks at 0.756 at
  `β = 4`, and falls to 0.002 at `β = 16`.
- (e) over 200 random instances with `β ∈ [0.25, 64]`:
  - `M_free` falls below 1 % of its maximum by `β = 64` in 195 of 200;
  - it peaks at an intermediate `β` in only 67 of 200, and is otherwise largest at the weakest optimization.

*Reading.* **A wrong default counts as misalignment unless it leans along the target.** This is the
consequence of measuring against a *declared* reference, the choice made in R7-2 (Def. [[Def 8|8]]). The
alternative — measuring against the actor's own reference — fails the contract's M4. The same behaviour,
attributed to two (reference, evaluator) pairs, would receive measures differing by a median of 0.22 nats and
up to 10.6 ([[V32]]).

**A wrong default stops mattering as optimization strengthens.** Its cost vanishes as the agent concentrates
on a unique optimum, because the default no longer shapes the choice. At weak optimization it tends to the
distance of the actor's default from the intent ray. In between it can rise before it falls — it did in a
third of the random instances — so "a stronger optimizer has a less misaligned default" is not a safe
monotone claim. *(An earlier draft of this note, written from a single instance, said the cost was largest
at intermediate strength. The random sample does not support that as a general statement.)* The
explanation layer can attribute a departure to the reference rather than the evaluator only with an
independent measurement of `q_A` — for humans, default experiments under exclusion ([[B12]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 13.4]] — second order
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 13]] — actor models; R7-1
- [[Lemma 5.1]] — form of the capacity actor
- [[Prop 12]] — what behaviour identifies

## Used by
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[B13]] — Potential games — collective behaviour is a tilt (Blume 1993) *(new in v6.2)*
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0

## Mentioned in
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 13]] — actor models; R7-1
- [[Rem 16.1]] — reference misspecification

## Checks
- [[V32]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
