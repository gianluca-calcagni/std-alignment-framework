---
kind: definition
id: D11
aliases: ["D11"]
source: "CORE.md"
---
# D11 — Record, sample and evidence
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d11--record-sample-and-evidence). Edit the source, not this note.

## Statement
A **record** of size `n` is the sequence `x_1, …, x_n` of the outcomes of `n` decisions, and its
**empirical behaviour** `p̂_n` gives each outcome its share in the record. A record is a **sample** from a behaviour
`p` when its outcomes are drawn independently from `p`. For full-support behaviours `r` and `r'`, the **evidence** that
a record gives for `r` against `r'` is `Σ_{i=1}^n log(r(x_i)/r'(x_i))`, in nats.

## In plain terms
A record is what the actor did on successive occasions, in order. Counting gives the empirical
behaviour. A sample is a record whose occasions are independent draws from one behaviour: a model of the actor, which a
case can test. The evidence for one behaviour against another is how much more likely the record is under the first
than under the second, on a logarithmic scale.

## Interpretation
*Declared.* A record is the log of the actor's decisions; its empirical behaviour is the shares in
it; a sample is a record whose decisions are independent draws from one behaviour; the evidence for one behaviour
against another is how much more likely the record is under the first, in nats. *Verified.* The record is what is
verified, decision by decision; every claim about behaviour reaches the world through it. That a record is a sample is
a claim about the actor, which the order of the record can refute (Notes). *Justified.* Shares are what [[A1 — Behaviour suffices|A1]] judges and
[[A4 — Misalignment is evidence|A4]] measures, whatever the actor; independence is what makes them approach one behaviour ([[M2 — Independent repetition|M2]]) and the evidence add
up decision by decision, and decisions that depend on each other within an episode are one outcome ([[B2 — Episodes and conditions as outcomes|B2]]).

## Why this choice
- *Behaviours are never observed; records are.* This is the act of measurement that [[A1 — Behaviour suffices|A1]] presumes when it says that
  behaviour can be counted, and that [[D9 — Observation and identification|D9]]'s observed conditions stand for.
- *It is universal.* Counted choices, sampled genotypes, sampled responses, case records and logged units of work are
  all samples.
- *Evidence is the canonical statistic.* Between two behaviours, the most powerful test thresholds the likelihood ratio
  (the Neyman–Pearson lemma [[References|@cover2006]], read in the open draft of [[References|@polyanskiy2025]], Theorem 14.11).
- *It makes [[A4 — Misalignment is evidence|A4]] exact.* For a sample, the expected evidence per decision, under the actual behaviour, for it against
  the nearest intended behaviour is the misalignment (`derived/estimation.md`). Evidence gained ([[A4 — Misalignment is evidence|A4]]) and value lost
  ([[P4 — What KL measures|P4]](ii)) agree, in the same direction of KL, as the steepest climb and the best trade-off, the reasons of [[D2 — Pursuit of an objective|D2]],
  agree on the cost.
- *It compares explanations in the same unit.* Two evaluators proposed for one actor are compared by the evidence a
  sample gives for one pursuit against the other, in nats, the unit of misalignment and of value.
- *Records first, samples as a model.* What a record shows against acceptance needs no model of the actor ([[A4 — Misalignment is evidence|A4]]); a
  sample is the model under which shares estimate one behaviour, with an interval. An actor whose decisions depend on
  each other, or drift, is judged by its average behaviour, and what dependence and drift add is measured beside it
  (Notes).

## Notes
The evidence is the log-likelihood ratio; I. J. Good called it the weight of evidence. In statistics a sample
from a finite set is multinomial, and the empirical behaviour is the type of the sequence [[References|@cover2006]]. For a record
that is not a sample, [[P54 — Dependence and drift only add evidence|P54]] gives what dependence and drift add to the evidence; [[P55 — What a record of counts certifies, at every size|P55]] gives the test of acceptance from
counts, exact at every size, and the interval for a sample. Independence between episodes can be tested from the order
of a record, for instance by comparing the shares of pairs of successive episodes with the products of their shares.

## Lineage
v7.10: Prop 18 (detection) and the deviance of v8's [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] Notes, which used samples without defining them.
New: the definition, and evidence as the second meaning of misalignment. v13: the record, of which the sample is the
case of independent decisions (Q53).

## Depends on
- [[M2 — Independent repetition|M2]] — Independent repetition
- [[B2 — Episodes and conditions as outcomes|B2]] — Episodes and conditions as outcomes
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[A4 — Misalignment is evidence|A4]] — Misalignment is evidence
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- [[P21 — The expected evidence is misalignment|P21]] — The expected evidence is misalignment
- [[P54 — Dependence and drift only add evidence|P54]] — Dependence and drift only add evidence
- [[P55 — What a record of counts certifies, at every size|P55]] — What a record of counts certifies, at every size
