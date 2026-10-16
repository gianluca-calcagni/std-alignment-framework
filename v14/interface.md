# The interface: what the actor sees and can do

> **Status: draft of v14 (Q61–Q64); the definitions are proposals, the results proved here, not yet checked in CI.**
> This file gathers what `NOTES.md` §25 and §26 found, so that the INTERFACE layer has one place before it is written in
> `CORE.md`'s format.

CORE judges what an actor did. INTERFACE adds what it could have done and what it could tell, with no model of
optimization: a frozen model has an interface, and nothing in it optimizes. Notation as in `evidence.md` and
`factorization.md`.

## Definitions

**Interface.** For finitely many conditions `c ∈ 𝒞` and outcomes `X`, an interface `ℐ = (U, Z, V, E)` declares a set `U`
of **actions**, a set `Z` of **signals** with, for each condition, a **view** `V(·|c)`, a distribution on `Z`, and an
**environment** `E(·|c, u)`, a distribution on `X` for each condition and action. A **policy** is a choice of
distribution `π(·|z)` on `U` for each signal, with finite support when `U` is infinite. The **feasible behaviours** are
those the policies produce: `𝓕(ℐ) = {(p_c)_c : p_c(x) = Σ_z V(z|c)·Σ_u π(u|z)·E(x|c, u), π a policy}`.

**Culpability and the avoidable excess.** For a request whose acceptable set is `A` and an actor whose actual behaviour
`p̂` lies in `𝓕 = 𝓕(ℐ)`: the **unavoidable misalignment** `M_A(𝓕) = inf_{f∈𝓕} M_A(f)`; the **best feasible behaviours**
`𝓕* = {f ∈ 𝓕 : M_A(f) = M_A(𝓕)}`; the **avoidable excess** `E(p̂) = M_A(p̂) − M_A(𝓕)`; and the
**culpability** `K(p̂) = inf_{f∈𝓕*} KL(p̂‖f)`, the evidence that the actor does not do the best it could. Both are `0`
exactly when `p̂ ∈ 𝓕*`; `K = E + R ≥ E` for linear interfaces (`factorization.md`, FA2), and they are not ordered
otherwise. The executor recommends `K` as culpability, as evidence ([A4]), and `E` as the share of misalignment that was
avoidable; L2 is to test both names.

**Elicitation.** A condition `c'` is an **elicitation** of a condition `c` when the declaration links the actor's
feasible behaviours there, such as one set of policies faced with another prompt or incentive. Only through such links
can an excuse about capability be refuted beyond what the actor actually did (`factorization.md`, VF3).

### IN1 — The interface loses no generality for convex feasible sets
**Statement.** (i) `𝓕(ℐ)` is convex for every interface. (ii) For every closed convex set `𝓕` of behaviours there is an
interface `ℐ` with `𝓕(ℐ) = 𝓕`: the actions are the behaviours of `𝓕` themselves, the view is one signal that tells the
conditions nothing, and the environment returns the chosen behaviour in each condition.

**In plain terms.** Whatever an actor can do, if mixing two things it can do is something it can do, there is an
interface that says exactly that, and no other. The interface adds structure where the declaration has it, what the
actor sees and how the world responds, and loses nothing where it does not.

**Proof.** (i) The map from policies to behaviours is affine in `π`, and the policies form a convex set (each `π(·|z)`
ranges over the distributions on `U`), so its image is convex. (ii) Let `U = 𝓕`, `Z` a single signal `z₀` with
`V(z₀|c) = 1` for every `c`, and `E(·|c, f) = f_c`. A policy is then one finitely supported distribution `π` on `𝓕`, the
same in every condition, and it produces `(Σ_f π(f)·f_c)_c`, the mixture of its actions, which is in `𝓕` by convexity;
so `𝓕(ℐ) ⊆ 𝓕`. The policy that chooses `f` with probability one produces `f`, so `𝓕 ⊆ 𝓕(ℐ)`. A view that told the
conditions apart would let a policy mix differently in each, and leave a set that ties the conditions together. ∎

**Notes.** The qualifier: a feasible set that is not convex, such as a parametric class of policies that cannot
randomize, is not the feasible set of any interface whose policies may randomize; it is a capacity limit, declared as a
set, and FA1 factors it, while FA2's Pythagorean form does not apply. With finitely many actions, (ii) covers polytopes.

## Every form of misalignment, by the layer that can define it

Each form is sorted by the least the framework needs to define it. Three questions mark the layers: what happened
(CORE), whether the actor could have done otherwise or known (INTERFACE), and why (OPTIMIZERS).

| Form | Layer | The least it needs |
|---|---|---|
| breach of a requirement | CORE | the requirement |
| misalignment by condition, and a shift of the conditions' weights between test and use | CORE | conditions |
| hidden misalignment, in conditions no record covers | CORE to define; INTERFACE to bound | views or feasible sets that tie them to recorded ones ([D9], [P17]) |
| drift and dependence over time | CORE | repeated records or declared episodes ([P54]) |
| the evaluation gap: a measured requirement met while the true one is breached | CORE | outcomes that hold both the measure and the truth |
| a shortfall below a declared floor | CORE | the floor, a requirement |
| side effects | CORE | requirements on the other coordinates of the outcome |
| unavoidable against avoidable, culpability | INTERFACE | the feasible behaviours |
| coarse perception, including not knowing what is asked | INTERFACE | views |
| execution noise | INTERFACE | the environment kernel |
| tampering against honest selection | INTERFACE | which variables the actions reach, and what is seen before acting |
| ignoring the situation against the environment's doing | INTERFACE | the split of actions from outcomes |
| collusion between actors | INTERFACE | each actor's views and private randomness; under v14's mixture principle, independence is no requirement a record enforces (`LIMITS.md`) |
| gaming or reward hacking as a motive | OPTIMIZERS | the actor's objective, an evaluator |
| overoptimization | OPTIMIZERS | an intensity of optimization |
| outer misalignment | OPTIMIZERS | the trainer's objective |
| inner misalignment | OPTIMIZERS | the learned objective against the trainer's |
| strategic deception, alignment faking | INTERFACE and OPTIMIZERS | views to tell when it is observed, and an objective over its own future |
| the shadow price of a constraint | OPTIMIZERS | a model of the actor optimizing under it (VK5) |
| misspecification | none: not the actor's | a second standard, another principal or a later judgement |
| severity | the principal's side | a declared value scale (`NOTES.md` §24) |

**The grades of fault** follow the layers: a breach (CORE); negligence, culpability above `0` (INTERFACE); intent, the
breach serving the actor's objective (OPTIMIZERS). Their verification status differs: a breach is verifiable,
culpability verifiable with the interface taken as known, intent a refutable hypothesis (`factorization.md`, VF2).
