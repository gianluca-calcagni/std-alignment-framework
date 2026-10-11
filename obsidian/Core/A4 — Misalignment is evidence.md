---
kind: premise
id: A4
aliases: ["A4"]
source: "CORE.md"
---
# A4 — Misalignment is evidence
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#a4--misalignment-is-evidence). Edit the source, not this note.

## Statement
The misalignment of the shares that a record of decisions shows, against the behaviours a principal
accepts, is the rate per decision at which, as records with those shares grow, the highest probability that accepted
behaviours give them, a supremum, falls, each accepted behaviour deciding independently. The misalignment of a behaviour
is that of the shares that approach it.

## In plain terms
Watch the actor decide, and count what it does. Misalignment is how fast those counts become
improbable for every acceptable way of acting, judged by the acceptable way that makes them most probable. It needs no
model of how the actor decides.

## Status
A principle, conceptual: it says what a record of counts shows against acceptance, which is all that [[A1 — Behaviour suffices|A1]]
lets a judgement rest on, and it assumes nothing about how the actor decides: independently, alike over time, or
neither. Three conventions give it its form, each justified in the table of conventions above: probability counted on a
logarithmic scale, per decision; the accepted behaviour most favourable to the record; and accepted behaviours that
decide independently, unless the principal declares episodes ([[B2 — Episodes and conditions as outcomes|B2]]).

## Why this choice
- *It needs nothing about the actor.* The probabilities are computed under the accepted behaviours, which the principal
  declares, so the measure applies to any actor, any record and any declared set, with no model of how the actor
  decides and no price of departing from the default.
- *Improbability under acceptance is evidence against it.* Counts that are improbable under every accepted behaviour
  are evidence that the actor acts in no accepted way. Judging a set of hypotheses by its member most favourable to the
  data is the generalized likelihood ratio test ([[References|@polyanskiy2025]], §16.4), which gives the actor the benefit of the
  doubt and charges it only for what no accepted behaviour explains.
- *The measure follows.* The highest probability that accepted behaviours give the shares `s` falls at the rate
  `inf_{p∈𝓘} KL(s‖p)` (Notes): that is the measure, its form and the order of its arguments.
- *For an actor that decides independently, it is the rate of likelihood-ratio evidence.* Each independent decision
  drawn from `p̂` adds on average `KL(p̂‖p)` nats to the evidence for `p̂` against `p` (the Neyman–Pearson lemma makes
  that evidence canonical, [[References|@polyanskiy2025]], Theorem 14.11), so misalignment is also the least expected evidence per
  decision. For an actor whose decisions depend on each other, or drift, that evidence is larger, by exactly two terms
  that are reported beside it (Notes).
- *Value lost, as a reading.* Every full-support behaviour is the best trade-off for its own objective at a KL price
  ([[P4 — What KL measures|P4]](ii)), so the same number is the least net value lost against an accepted behaviour, judged by that behaviour's
  own objective. Until v12 that reading was the premise, and it needed two premises on pursuit to make the price KL
  ([[P14 — The cost of departing from the default is forced|P14]]); here it is a consequence, and the measure rests on evidence alone.

## Notes
The rate is the method of types, [[P55 — What a record of counts certifies, at every size|P55]](i); the test it gives, exact at every size of record, is [[P55 — What a record of counts certifies, at every size|P55]](ii);
what dependence and drift add to the likelihood-ratio evidence is [[P54 — Dependence and drift only add evidence|P54]]. That "misaligned" is verifiable in chance, and
"exactly aligned" only refutable, is [[P55 — What a record of counts certifies, at every size|P55]], Notes, after Genin and Kelly [[References|@genin2017]].

## Lineage
v7.10: Thm 1 (regret is a divergence) and Prop 18 (detection). v8: [[D3 — Specification, declaration and misalignment|D3]]'s "what the number means". v12:
"misalignment is value lost", which this premise replaces, its reading kept as a consequence (`NOTES.md` §16, §17). The
idea is the hunch H4 of `NOTES.md` §5.4. v13, at the PI's question whether independence could be dropped (Q53): the
rate at which the record's shares become improbable under acceptance, which needs no independence of the actor, in
place of the rate of likelihood-ratio evidence of an actor that decides independently, now a reading ([[P54 — Dependence and drift only add evidence|P54]]).

## Depends on
- [[B2 — Episodes and conditions as outcomes|B2]] — Episodes and conditions as outcomes
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[P4 — What KL measures|P4]] — What KL measures
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced

## Used by
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D11 — Record, sample and evidence|D11]] — Record, sample and evidence
