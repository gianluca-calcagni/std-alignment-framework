---
kind: definition
id: D2
aliases: ["D2"]
source: "CORE.md"
---
# D2 — Pursuit of an objective
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d2--pursuit-of-an-objective). Edit the source, not this note.

## Statement
Let `q ∈ Δ°`, the **default**, and let `F : X → ℝ` be a function, an **objective**. The **pursuit** of
`F` from `q` at **intensity** `t ≥ 0` is `p_{F,t} = tilt(q, t·F)`. The **pursuit ray** of `F` from `q` is
`R_F = {p_{F,t} : t ≥ 0}`; for a constant `F` it is the single point `q`. A continuously differentiable path `s ↦ p_s`
in `Δ°`, over an interval containing `0`, **pursues** `F` if `p_s = tilt(p_0, τ(s)·F)` for a differentiable,
non-decreasing `τ` with `τ(0) = 0`.

## In plain terms
Pursuing an objective means reweighting the default behaviour toward the outcomes that the objective
scores higher, and the intensity says how strongly. Intensity zero is the default itself, and the pursuit ray collects
every intensity. A path of behaviours pursues an objective when it keeps reweighting toward that same objective, never
away from it, from wherever it starts.

## Why this choice
- *It loses no generality.* Every full-support behaviour `p` lies on the pursuit ray of some objective, from any
  default: `p = p_{F,1}` with `F = log(p/q)` ([[P1 — Every behaviour is a tilt of any other|P1]](i)). Every path of behaviours follows the replicator equation of an
  objective that may move over time ([[P2 — Every change of behaviour follows a replicator equation|P2]](i)). What the definition adds is a claim that can fail: that the objective
  stays fixed, which a derived result makes testable (`derived/tilts-and-paths.md`). Mixing a behaviour with another,
  for example, generally gives a path whose objective turns, as that result's check shows; cut-offs that exclude
  outcomes leave `Δ°` altogether.
- *It is canonical, given [[A2 — Pursuit is the steepest climb|A2]].* Pursuing `F` means climbing `E_p[F]` as steeply as possible, in a Riemannian geometry
  on behaviours that is unchanged when outcomes are split into sub-outcomes in fixed proportions. Up to a constant
  factor, the Fisher metric is the only such geometry, across outcome spaces of every size (Čencov's theorem
  [[References|@cencov1982]]; [[References|@campbell1986]]). In the Fisher metric the steepest climb is the replicator field ([[P2 — Every change of behaviour follows a replicator equation|P2]](ii)), and its
  flow from `q` is `tilt(q, s·F)` ([[P2 — Every change of behaviour follows a replicator equation|P2]](iii)). A constant factor in the metric only rescales time, so the ray is the
  same. A notion of pursuit that must not depend on how finely outcomes are described is therefore led to this ray.
- *The ray needs a default; the path does not.* The same objective pursued from two defaults gives two different rays,
  so the specification of section 3 fixes the default. Whether a path pursues `F` needs no default at all, which is why
  derived results can read pursuit from changes of behaviour without declaring one.

## Notes
Names in other fields. The default is the reference policy of RL fine-tuning, the prior of KL control, the
base measure of an exponential family, the status quo of behavioural economics, and the population before selection in
biology. The objective is a reward, a utility, or a log-fitness. The pursuit `p_{F,t}` is the optimum of KL-regularized
reward maximization with coefficient `1/t` in RL fine-tuning, for one prompt (across prompts, which the policy does not
choose, the optimum reweights each prompt's responses separately, which is not a pursuit on prompt–response pairs); with
a uniform default it is the logit choice rule, or quantal response, with rationality `t` [[References|@mckelvey1995]]; and it is the
result of `t` generations of constant selection with fitness `e^F`, for types that are passed on intact, as in clonal
reproduction. The intensity is an inverse temperature in physics, and "optimization pressure" in AI safety.

## Lineage
v7.10: Def 1 (the Gibbs tilt `p_{G,t}`, with `q` there called the reference), Def 2 (the bounded actor,
whose optimum is the tilt: here a property, [[P4 — What KL measures|P4]](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray
defines intended pursuit; it is not a model of the actor. v7.10's rows 67–68 and 76–78 filed results by the intended
actor's model instead of by what their proofs need, and the core keeps the two apart by construction.

## Depends on
- [[A2 — Pursuit is the steepest climb|A2]] — Pursuit is the steepest climb
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P2 — Every change of behaviour follows a replicator equation|P2]] — Every change of behaviour follows a replicator equation

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D4 — Resolution|D4]] — Resolution
- [[P3 — A fixed objective is visible in the changes of behaviour|P3]] — A fixed objective is visible in the changes of behaviour
- [[C4 — Rescaling the objective is not misalignment|C4]] — Rescaling the objective is not misalignment
