---
kind: premise
id: A6
aliases: ["A6"]
source: "CORE.md"
---
# A6 — Declared no finer than identified
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#a6--declared-no-finer-than-identified). Edit the source, not this note.

## Statement
A specification of an objective distinguishes no more than the actor's way of acting can carry: its
values, up to a positive factor and a constant, for an actor that pursues as [[A2 — Pursuit is the steepest climb|A2]] and [[A3 — Pursuit is the best trade-off|A3]] say; only its order for an
actor that ranks outcomes, or whose way of acting is not known; unless the declaration says why a finer one applies.

## In plain terms
Judge an actor only on what its way of acting can express. An actor that weighs outcomes by how
much better they are is judged on the objective's values; one that only picks the better of what it sees, or whose
method is unknown, is judged on their order.

## Why this choice
- *A finer declaration charges what no behaviour of that kind could show.* An actor that keeps the best of `n` draws by
  `F` compares draws only by their order under `F`, so it behaves alike for every increasing transformation of `F`, and
  nothing in its behaviour depends on the values of `F` beyond their order. Judged by those values, it is charged for
  its method rather than for its goal (Notes).
- *A pursuer's class.* A pursuit reveals its objective up to a positive factor and a constant ([[P1 — Every behaviour is a tilt of any other|P1]](ii)), and the
  pursuit ray, which accepts every intensity, declares exactly that.
- *Other channels.* A learner of preferences compared within one context identifies the objective only up to a constant
  in each context: a specification across contexts that charges those constants is finer than the channel, while one
  stated condition by condition is not.
- *Coarser is allowed; finer needs a reason.* A principal may declare less than the actor's way of acting carries, and
  lose sensitivity. Declaring more is a claim about the actor, which the declaration states and a case can test.

## Notes
The ordinal specification of [[D3 — Specification, declaration and misalignment|D3]] contains every best-of-`n` by `F` and is unchanged under increasing
transformations of `F` ([[P36 — Ordinal objectives|P36]](i) and (v)). In random instances, best-of-4 on the principal's own objective is charged a
median `0.13` of its departure under the standard specification, and is exactly aligned under the ordinal one; with a
proxy that correlates about `0.96` with the objective, the standard specification ranks the exact pursuit of the proxy
as less misaligned than best-of-4 on the objective in 65% of pairs (`probes/review/known_groups.py`, `NOTES.md` §15).
Whether the actor pursues, as declared, can itself be tested ([[P3 — A fixed objective is visible in the changes of behaviour|P3]], [[P12 — What interventions reveal|P12]]).

## Lineage
v7.10: the brainstorm B1 (identification classes, and the rule "no target set finer than the channel
identifies, or say why", which its protocol adopted), its notes' H8 and H10(a), and item 2 of its review of v7.3.3; the
restart did not carry them over (`NOTES.md` §1). New in the core.

## Depends on
- [[A2 — Pursuit is the steepest climb|A2]] — Pursuit is the steepest climb
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
