---
kind: corollary
id: C10
aliases: ["C10"]
source: "derived/forbids.md"
---
# C10 — An actor cannot behave more differently than it can tell conditions apart
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c10--an-actor-cannot-behave-more-differently-than-it-can-tell-conditions-apart). Edit the source, not this note.

## Statement
If the actor's response depends on the condition only through its view ([[D8 — Conditions, responses and views|D8]]), then
`KL(p_c‖p_{c'}) ≤ KL(V_c‖V_{c'})` for any two conditions, and conditions it cannot tell apart get the same behaviour
([[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]]). In particular, it does not behave differently when observed and when not unless its view tells the two apart.

## In plain terms
Behaving well only when watched requires being able to tell when one is watched.

## Proof
[[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](i) and (ii).

## Lineage
v9: [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]]. New as a forbidden statement.

## Checks
- [`checks/test_identifiability.py::test_identical_views_give_identical_behaviour`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)
- [`checks/test_identifiability.py::test_behaviour_differs_no_more_than_views`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] — An actor cannot behave more differently than it can tell conditions apart

## Used by
- no later item
