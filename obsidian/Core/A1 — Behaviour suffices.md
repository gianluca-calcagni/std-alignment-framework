---
kind: premise
id: A1
aliases: ["A1"]
source: "CORE.md"
---
# A1 — Behaviour suffices
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#a1--behaviour-suffices). Edit the source, not this note.

## Statement
What an actor does is described by how often each of finitely many outcomes occurs, in each condition it
may face. Alignment is judged from that description alone, never from how the behaviour is produced.

## In plain terms
We judge what the actor does, in every situation it may meet, and not what goes on inside it.

## Why this choice
- *It can be observed.* Behaviour can be counted. Internal goals and mechanisms differ across AI systems, people,
  institutions and organisms, and are often out of reach. A premise about behaviour applies to all four.
- *In every condition, not in one.* Judging a single behaviour would miss an actor that behaves well when it is
  observed and badly otherwise. Requiring behaviour in every condition keeps such deceptive alignment inside the
  framework, as misalignment in conditions that are not observed (section 8).
- *Finitely many outcomes.* Every statement can then be proved with finite sums and checked exactly on random
  instances. General outcome spaces are out of scope for now.
- *What it costs.* Two actors that behave alike in every condition are the same actor for the core, whatever their
  internal goals. That is deliberate: a difference that shows in no condition has no consequence a principal could
  suffer.

## Lineage
v7.10: R7-1 (the actual behaviour is any distribution, Def 13). v8: [[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s "why", where this was an
argument. New: behaviour in every condition, so that deceptive alignment is in scope.

## Depends on
- nothing

## Used by
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[D11 — Sample and evidence|D11]] — Sample and evidence
