---
id: "Prop 23"
type: "proposition"
title: "argmax selectors on a common candidate set — tier 2′, v6.4"
section: "Core 04 Capacity"
order: 24
layer: "explanation"
tier: ["2′"]
assumes: []
status: "proved"
depends_on: ["Def 13"]
mentions: ["Thm 5"]
checks: ["V28"]
sources: []
aliases: ["Proposition 23", "Prop. 23"]
updated: "2026-09-26"
---
# Prop 23 — argmax selectors on a common candidate set — tier 2′, v6.4
<!-- gen:header -->
> [!abstract] Proposition · tier 2′ · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Proposition 23 (argmax selectors on a common candidate set — tier 2′, v6.4).** Let a random candidate set
`S ⊆ X` be drawn by any mechanism — for instance `n` i.i.d. draws from `q`. Let the intended actor pick
`x* ∈ argmax_{S} F`, and the actual actor pick `x̂ ∈ argmax_{S} F̂`, **from the same `S`** and with a common
tie-breaking rule. With `p*`, `p̂` their laws and `R = E_{p*}F − E_{p̂}F`:

```
0 ≤ R ≤ E_{p̂}E − E_{p*}E.
```

## Proof

*Proof.* Pathwise, `x̂ ∈ S` gives `F(x*) ≥ F(x̂)`, and `x* ∈ S` gives `F̂(x̂) ≥ F̂(x*)`. Hence
`0 ≤ F(x*) − F(x̂) ≤ F(x*) − F(x̂) + F̂(x̂) − F̂(x*) = E(x̂) − E(x*)`. Take expectations. ∎

## Notes and checks

*Check.* [[V28]]: best-of-`k` at equal `k`, 20,000 instances (30 % with ties), 0 violations of either inequality.
R6 found 0 of 1,150 at equal `n`.

*Reading.* Tier 2 (Thm [[Thm 5|5]](i)) needs an exact maximizer over a *set* containing the intended actor. Prop. 23
needs only that both actors maximize over the *same random* set. That is the coupling that makes best-of-n
safe to compare **at equal `n`**, and **not at matched KL**, where R6 found 4.3 % violations. The same
coupling covers any search that shares its candidate pool — for example reranking a common sample. Unlike
Thm [[Thm 5|5]], Prop. 23 gives no width: the right-hand side still depends on the actor's selection.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution

## Mentions
- [[Thm 5]] — the width is the exact worst case

## Mentioned in
- [[Def 13]] — actor models; R7-1

## Checks
- [[V28]]

## Sources
- none

## Retractions touching this note
- [[R067]]
<!-- /gen:links -->
