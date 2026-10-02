---
kind: definition
id: D4
aliases: ["D4"]
source: "CORE.md"
---
# D4 — Resolution
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d4--resolution). Edit the source, not this note.

## Statement
A **resolution** is a partition `𝒢` of `X` into non-empty **cells**. A function is constant on cells if
it
takes one value on each cell. For `p ∈ Δ`, `p_𝒢` is the distribution of the cell masses `p(C)`. For `q ∈ Δ°` and
`F : X → ℝ`, the **cell average** `E_q[F|𝒢]` is the function equal, on each cell `C`, to `E_{q(·|C)}[F]`. Resolutions
are used in two positions.
- A specification `(q, 𝓘)` is **stated at resolution** `ℬ` if `𝓘 = {p ∈ Δ° : p_ℬ ∈ 𝓘_ℬ}` for a non-empty set `𝓘_ℬ`
  of full-support distributions on the cells, closed in the set of all full-support distributions on the cells. The
  principal is then **indifferent** inside the cells of `ℬ`. For an objective `F` constant on the cells of `ℬ`,
  the **standard specification at resolution** `ℬ` takes
  `𝓘_ℬ` to be the pursuit ray of `F`, read on the cells, from `q_ℬ`.
- A behaviour `p` is **limited to** a resolution `𝒜` if it splits every cell as the default does: `p(·|A) = q(·|A)` for
  every cell `A` of `𝒜` with `p(A) > 0`. An actor **has resolution** `𝒜` if every behaviour it can produce is limited
  to `𝒜`.

When nothing is declared or known, the resolution is the finest one, with one outcome per cell, in both positions.

## In plain terms
A resolution groups outcomes into cells that are treated as one. A principal who states its
specification on cells declares that it does not care how outcomes inside a cell are split, only how often each cell
occurs. An actor with a resolution cannot tell the outcomes inside a cell apart: it can change how often each cell
occurs, but inside a cell the outcomes keep the proportions they have by default.

## Why this choice
- *One object, two positions.* The same kind of object describes what the principal cares to distinguish and what the
  actor can distinguish. Gaps between the two cover two familiar failures: a principal who cares about distinctions the
  actor cannot see (v7.10's transmission gap, G2), and an actor that acts on distinctions the principal never mentioned
  (underdetermination, G1).
- *Partitions are the general case here.* On a finite set, a σ-algebra is the same thing as a partition into cells.
- *Inside an actor's cells, the default decides.* An actor that cannot tell two outcomes apart cannot change how often
  one occurs relative to the other, so that ratio stays where it is without the actor's choice: at the default ([[D2 — Pursuit of an objective|D2]]).
  This needs no object beyond the specification.
- *The finest resolution unless declared.* A principal who declares a coarse resolution cannot see what happens inside
  its cells; in v7.10, a style exploit lived almost entirely inside cells in toy tests (B1). So indifference has to be
  declared, never assumed. An actor's resolution, in contrast, is a fact about the actor, to be identified from its
  behaviour rather than declared.
- *Not the meet.* The finest partition coarser than both resolutions (their meet) holds the events both sides can
  describe, which are common knowledge in Aumann's sense [[References|@aumann1976]]. Misalignment computed there is a lower bound
  both
  can verify ([[P4 — What KL measures|P4]](iv)), but it is blind to every gap between the two resolutions, so it is not the score.

## Notes
The actor's position is a case of feasibility: the behaviours limited to `𝒜` form a linear feasible set
([[D7 — Feasibility|D7]]). In reinforcement learning, an actor's resolution is a state abstraction, and outcomes it cannot tell apart
are aliased. A principal's resolution is a coarse-graining of the outcomes.

## Lineage
v7.10: Def 21 (the declared resolution: the principal's position), B1 and NOTES H14 (one object in several
positions; retention), and ROADMAP §6 G1, G2 and G4. New: the actor's position as a definition, with the default
deciding
inside cells.

## Depends on
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- [[D7 — Feasibility|D7]] — Feasibility
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P18 — Through the evaluator, only the regression counts|P18]] — Through the evaluator, only the regression counts
