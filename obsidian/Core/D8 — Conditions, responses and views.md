---
kind: definition
id: D8
aliases: ["D8"]
source: "CORE.md"
---
# D8 — Conditions, responses and views
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d8--conditions-responses-and-views). Edit the source, not this note.

## Statement
A **condition** is a situation in which the actor may act; `𝒞` is a finite set of conditions. The
actor's **response** is the family `(p_c)_{c ∈ 𝒞}` of its behaviours, one in each condition. A **view** is a finite set
`Z` of signals and, for each condition `c`, a distribution `V_c` on `Z`: what the actor perceives in condition `c`. The
response **depends on the condition only through the view** if there are behaviours `π_z`, for `z ∈ Z`, with
`p_c = Σ_z V_c(z)·π_z` for every condition `c`. When nothing is known about the actor's perception, the view is exact:
`Z = 𝒞`, and each condition is perceived as itself.

## In plain terms
Conditions are the situations the actor may face: a prompt, a client, a test, or real use. The
response collects what the actor does in each. The view describes what the actor can perceive of its situation. An actor
whose response depends only on its view must act alike in situations it perceives alike, and can act differently only
where it perceives a difference.

## Why this choice
- *[[A1 — Behaviour suffices|A1]] judges behaviour in every condition.* A single behaviour is the case of one condition. Situations whose
  frequencies the actor does not choose, such as prompts or arriving patients, are conditions: a response weighted by
  those frequencies is a behaviour on condition–outcome pairs with fixed condition masses, a linear feasible set
  ([[D7 — Feasibility|D7]]).
- *The view makes "cannot tell apart" a quantity.* [[D4 — Resolution|D4]]'s actor resolution limits what the actor can do with outcomes;
  a view limits what it can perceive of conditions. A view that gives each condition a single signal is a partition of
  the conditions; a random view says by how much two conditions can be told apart.
- *Deceptive alignment needs a view.* An actor that behaves well when it is observed and badly otherwise must perceive
  whether it is observed. A derived result bounds what it can hide by how well its view separates the two
  (`derived/identifiability.md`).
- *The exact view, when nothing is known,* assumes nothing about the actor's perception, and excuses nothing.

## Notes
In control theory the response is an input–output map and the view is the actor's observation of its input;
here observability runs from the condition to the actor. In reinforcement learning the conditions are states or prompts
and the response is the policy. In statistics, a response that depends on the condition only through a view is a
Markov kernel composed with a channel.

## Lineage
New. v7.10: ROADMAP §6 I1 (identification through interventions) and the brainstorm's point on
identifiability dynamics. The ontologies' "contexts" (v8, `NOTES.md`) are conditions with fixed frequencies.

## Depends on
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[D4 — Resolution|D4]] — Resolution
- [[D7 — Feasibility|D7]] — Feasibility

## Used by
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] — An actor cannot behave more differently than it can tell conditions apart
- [[P17 — What an unobserved condition can hide|P17]] — What an unobserved condition can hide
- [[P32 — Regulation costs departure|P32]] — Regulation costs departure
- [[P24 — The evaluation gap|P24]] — The evaluation gap
- [[C10 — An actor cannot behave more differently than it can tell conditions apart|C10]] — An actor cannot behave more differently than it can tell conditions apart
