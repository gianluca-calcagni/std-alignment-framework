---
kind: definition
id: D9
aliases: ["D9"]
source: "CORE.md"
---
# D9 — Observation and identification
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d9--observation-and-identification). Edit the source, not this note.

## Statement
The principal observes the response in a set `O ⊆ 𝒞` of **observed conditions**. Let `𝓡` be the set of
responses that satisfy stated assumptions, such as a feasible set in each condition ([[D7 — Feasibility|D7]]) or a view ([[D8 — Conditions, responses and views|D8]]). A quantity
defined from the response is **identified** if every response in `𝓡` that agrees with the observed behaviours `p_c`,
for `c ∈ O`, gives it the same value. Otherwise the set of values that those responses give is its **identified set**.

## In plain terms
The principal watches the actor only in some situations. A quantity is identified when everything
that fits what was watched, and what is assumed, gives it one value. Otherwise the honest report is the range of values
it could take.

## Why this choice
- *It reports what the evidence and the assumptions determine, and no more.* This is partial identification
  [[References|@manski2003]]. A report that gives one number for a quantity that is not identified hides an assumption.
- *It makes deceptive alignment measurable.* Misalignment in a condition that is not observed has an identified set.
  With no assumption it can be anything; a view narrows it, and an exact view of indistinguishable conditions makes it
  identified (`derived/identifiability.md`).
- *It is why interventions belong to the core.* An intervention ([[D6 — Intervention and pass-through|D6]]) is a designed change of condition. It adds
  observed conditions, chosen so that what the principal needs, such as the pass-through, is identified.
- *Every report states it.* The reporting standard (`STANDARD.md`) asks, for each reported quantity, whether it is
  identified, and under which assumptions.

## Notes
In econometrics this is identification, and partial identification when only a set is determined; in control
theory, identifiability of a system from input–output data, which needs inputs varied enough (persistent excitation).

## Lineage
New. v7.10: ROADMAP §6 I1 (the ladder: declare, measure, identify through interventions).

## Depends on
- [[D6 — Intervention and pass-through|D6]] — Intervention and pass-through
- [[D7 — Feasibility|D7]] — Feasibility
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views

## Used by
- [[D11 — Sample and evidence|D11]] — Sample and evidence
- [[P17 — What an unobserved condition can hide|P17]] — What an unobserved condition can hide
- [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] — What signals, audits and re-measurements reveal of tampering
