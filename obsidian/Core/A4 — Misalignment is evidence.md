---
kind: premise
id: A4
aliases: ["A4"]
source: "CORE.md"
---
# A4 — Misalignment is evidence
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#a4--misalignment-is-evidence). Edit the source, not this note.

## Statement
The misalignment of a behaviour, against the behaviours a principal accepts, is the least rate, per
independent decision drawn from it, at which a record of the behaviour gathers evidence against an accepted behaviour,
with evidence counted as the logarithm of the ratio of the record's likelihoods.

## In plain terms
Watch the actor decide, one occasion after another. Misalignment is how fast the record builds a
case that the actor is not acting in any acceptable way, against the acceptable way it resembles most.

## Why this choice
- *It needs nothing about the actor.* Evidence is defined by the record and the two behaviours compared, so the measure
  applies to any actor and any declared set of acceptable behaviours, with no model of how the actor chooses, and no
  price of departing from the default.
- *The likelihood ratio is the canonical evidence.* Between two behaviours, the most powerful test thresholds it (the
  Neyman–Pearson lemma, read in the open draft of [[References|@polyanskiy2025]], Theorem 14.11), and a sequential test that stops
  when it crosses a threshold needs, on average, about the threshold divided by the rate.
- *Under the actual behaviour, against the nearest.* The record comes from the actor, so the rate is the average under
  its behaviour; the least over the accepted behaviours gives the actor the benefit of the doubt, and charges it only
  for what no accepted behaviour explains. Each independent decision adds on average `KL(p̂‖p)` nats to the evidence for
  `p̂` against `p`, so the measure is `inf_{p∈𝓘} KL(p̂‖p)`, its form and the order of its arguments; section 10 makes
  the record exact.
- *Value lost, as a reading.* Every full-support behaviour is the best trade-off for its own objective at a KL price
  ([[P4 — What KL measures|P4]](ii)), so the same number is the least net value lost against an accepted behaviour, judged by that behaviour's
  own objective. Until v12 that reading was the premise, and it needed [[A2 — Pursuit is the steepest climb|A2]] and [[A3 — Pursuit is the best trade-off|A3]] to make the price KL ([[P14 — The cost of departing from the default is forced|P14]]); here
  it is a consequence, and the measure rests on evidence alone.

## Lineage
v7.10: Thm 1 (regret is a divergence) and Prop 18 (detection). v8: [[D3 — Specification, declaration and misalignment|D3]]'s "what the number means". v12:
"misalignment is value lost", which this premise replaces, its reading kept as a consequence (`NOTES.md` §16). The idea
is the hunch H4 of `NOTES.md` §5.4.

## Depends on
- [[A2 — Pursuit is the steepest climb|A2]] — Pursuit is the steepest climb
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[P4 — What KL measures|P4]] — What KL measures
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D11 — Sample and evidence|D11]] — Sample and evidence
