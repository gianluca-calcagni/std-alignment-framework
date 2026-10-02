---
kind: definition
id: D6
aliases: ["D6"]
source: "CORE.md"
---
# D6 — Intervention and pass-through
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d6--intervention-and-pass-through). Edit the source, not this note.

## Statement
An **intervention** changes what the actor faces by a known non-constant function `u : X → ℝ`: an
incentive, a fine, or a known shift of the actor's own default. With `p ∈ Δ°` the actor's behaviour before it and
`p' ∈ Δ°` after,
the actor passes the intervention through, with **pass-through** `φ ∈ ℝ`, if `p' = tilt(p, φ·u)`.

## In plain terms
An intervention is a known nudge added to the situation: a bonus for some outcomes, a fine for
others, or a shift in what the actor would do by default. The actor passes it through when its behaviour changes exactly
by reweighting
with that nudge. The pass-through says how strongly it responds: zero ignores the nudge, a positive value follows it,
and
a negative value means the nudge backfires.

## Why this choice
- *The simplest response that can fail.* Any change of behaviour is a reweighting by some function ([[P1 — Every behaviour is a tilt of any other|P1]](i)). The claim
  that this function is a multiple of the intervention is testable, and a derived result tests it
  (`derived/identifiability.md`). When it fails, more
  happened between the two behaviours than adding `u`: the intervention also changed what the actor pursues or where
  it starts from, or something else changed at the same time.
- *It needs no model of the actor.* The pass-through is defined from behaviour before and after; the actor's objective,
  default and intensity never appear. An actor that pursues `F̂` at intensity `t` from its own default (every behaviour
  can be written so, by [[P1 — Every behaviour is a tilt of any other|P1]]), and adds `w·u` to `F̂`, has pass-through `φ = t·w` by [[P1 — Every behaviour is a tilt of any other|P1]](iii); only that product is
  identified.
- *A change of default is an intervention too.* If the actor's own default is shifted by a known tilt `h` and its
  objective is unchanged, its behaviour moves to `tilt(p, h)` by [[P1 — Every behaviour is a tilt of any other|P1]](iii): pass-through `1` for `u = h`.

## Lineage
v7.10: ROADMAP §6 I1 (instrument pass-through: regress the increments on the fine), Def 23's instruments
slot,
made measurable, and T7-2d (a change of default that moved the evaluator).

## Depends on
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other

## Used by
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P37 — A strong incentive masks the actor, and can fake alignment|P37]] — A strong incentive masks the actor, and can fake alignment
