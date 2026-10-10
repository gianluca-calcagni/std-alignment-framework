---
kind: definition
id: D11
aliases: ["D11"]
source: "CORE.md"
---
# D11 — Sample and evidence
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d11--sample-and-evidence). Edit the source, not this note.

## Statement
A **sample** of size `n` from a behaviour `p` is a sequence `x_1, …, x_n` of outcomes drawn independently
from `p`. Its **empirical behaviour** `p̂_n` gives each outcome its frequency in the sample. For full-support behaviours
`r` and `r'`, the **evidence** that the sample gives for `r` against `r'` is `Σ_{i=1}^n log(r(x_i)/r'(x_i))`, in nats.

## In plain terms
A sample is a record of what the actor did on separate occasions, each drawn from its behaviour
independently of the others. Counting gives the empirical behaviour. The evidence for one behaviour against another is
how much more likely the record is under the first than under the second, on a logarithmic scale.

## Why this choice
- *Behaviours are never observed; samples are.* This is the act of measurement that [[A1 — Behaviour suffices|A1]] presumes when it says that
  behaviour can be counted, and that [[D9 — Observation and identification|D9]]'s observed conditions stand for.
- *It is universal.* Counted choices, sampled genotypes, sampled responses, case records and logged units of work are
  all samples.
- *Evidence is the canonical statistic.* Between two behaviours, the most powerful test thresholds the likelihood ratio
  (the Neyman–Pearson lemma [[References|@cover2006]], read in the open draft of [[References|@polyanskiy2025]], Theorem 14.11).
- *It gives misalignment a second meaning.* The expected evidence per decision, under the actual behaviour, for it
  against the nearest intended behaviour is the misalignment (`derived/estimation.md`). Value lost ([[A4 — Misalignment is value lost|A4]]) and evidence
  gained agree, in the same direction of KL, as the steepest climb ([[A2 — Pursuit is the steepest climb|A2]]) and the best trade-off ([[A3 — Pursuit is the best trade-off|A3]]) agree on the
  cost.
- *It compares explanations in the same unit.* Two evaluators proposed for one actor are compared by the evidence a
  sample gives for one pursuit against the other, in nats, the unit of misalignment and of value.
- *Independence is the default model.* Successive decisions of one actor can depend on each other; dependent samples
  are out of scope until an item needs them.

## Notes
The evidence is the log-likelihood ratio; I. J. Good called it the weight of evidence. In statistics a sample
from a finite set is multinomial, and the empirical behaviour is the type of the sequence [[References|@cover2006]].

## Lineage
v7.10: Prop 18 (detection) and the deviance of v8's [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] Notes, which used samples without defining them.
New: the definition, and evidence as the second meaning of misalignment.

## Depends on
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[A2 — Pursuit is the steepest climb|A2]] — Pursuit is the steepest climb
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[A4 — Misalignment is value lost|A4]] — Misalignment is value lost
- [[D9 — Observation and identification|D9]] — Observation and identification

## Used by
- [[P21 — The expected evidence is misalignment|P21]] — The expected evidence is misalignment
