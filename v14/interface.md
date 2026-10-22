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
distribution `π(·|z)` on `U` for each signal, with finite support when `U` is infinite. The **feasible behaviours**
`𝓕(ℐ)` are the closure of those the policies produce,
`{(p_c)_c : p_c(x) = Σ_z V(z|c)·Σ_u π(u|z)·E(x|c, u), π a policy}`, so that best behaviours exist. A tuple `(p_c)_c` is
read, as in [B2], as one behaviour on pairs of a condition and an outcome, with the conditions' frequencies `w_c` fixed
by the declaration, and divergences between tuples are taken on those pairs: v14's one space, the conditions being the
cells of the declared exogenous σ-algebra `ℰ` (`README.md`, one distribution).

**Culpability and the avoidable excess.** For a specification whose acceptable set is `A` and an actor whose actual
behaviour `p̂` lies in `𝓕 = 𝓕(ℐ)`: the **unavoidable misalignment** `M_A(𝓕) = inf_{f∈𝓕} M_A(f)`; the **best feasible
behaviours** `𝓕* = {f ∈ 𝓕 : M_A(f) = M_A(𝓕)}`; the **avoidable excess** `E(p̂) = M_A(p̂) − M_A(𝓕)`; and the
**culpability** `K(p̂) = inf_{f∈𝓕*} KL(p̂‖f)`, the evidence that the actor does not do the best it could. When `M_A(𝓕)`
is finite, both are `0` exactly when `p̂ ∈ 𝓕*`; `K = E + R ≥ E` for linear interfaces whose best behaviours have nearest
acceptable behaviours of full support (`factorization.md`, FA2), and they are not ordered otherwise. When `M_A(𝓕) = ∞`,
as for a forbidden outcome no feasible behaviour avoids, `E` is not defined and `K` is `0` for every feasible behaviour;
culpability must then be read on the breach rate, the least rate a feasible behaviour reaches, not yet written.
Culpability is only as good as the declared interface: one that overstates the actor's capability charges it for what no
record of it can show it could not do, so an interface should declare capabilities demonstrated in elicitation, which
are verifiable, rather than assumed. The executor recommended `K` as culpability, as evidence ([A4]), and `E` as the
share of misalignment that was avoidable; L2 is to test both names. The example of `slides/mathematicians.md` showed
that `K` is infinite exactly when the actor produces an outcome no best feasible behaviour produces (`𝓕*` is convex, so
the union of its members' supports is one member's support), which is the common case, the best behaviours of a convex
program over a polytope sitting on its boundary, often with a deterministic policy: so `K` is `0` or `∞` for most
actors. And when `M_A(𝓕)` is finite, `K > 0`, `E > 0` and `p̂ ∉ 𝓕*` say the same thing, so `K` adds no verdict, only a
growth-rate reading where it is finite. The recommendation became `E` for the size, and the verdict "culpable" read as
`p̂ ∉ 𝓕*`, verifiable with the interface taken as known (VF2) (`NOTES.md` §32, H52). Decided in its shape (Q74,
`NOTES.md` §33.17): the verdict is "culpable at a care margin `δ`", `p̂ ∉ 𝓕*_δ = {f ∈ 𝓕 : M_A(f) ≤ M_A(𝓕) + δ}`, with
`δ`, a standard of care, declared by the principal, and `δ = 0` the strict reading above; its evidence rate is
`K_δ = M_{𝓕*_δ}(p̂)`, finite in the usual case for `δ > 0`; its size is `E`; and where severity and the costs of the
alternatives are declared, a negligence size in the principal's units is reported beside `E`, never summed with it.
Whether "culpable" is the right word is left to L2. Culpability needs no new measure: `K(p̂) = M_{𝓕*}(p̂)`, the
misalignment against the **derived requirement** `𝓕*`, which is convex and closed when `A` and `𝓕` are, being the set
where a convex lower semicontinuous function on `𝓕` takes its least value; so VE1's bets, VE3's test and VF1's status
apply to it unchanged. The same holds for "the interface fits", the requirement `𝓕`, and for "perceives no more than its
view" (`resolution.md`, RS5): INTERFACE adds requirements derived from the declarations, not measures (`NOTES.md` §32,
item 7); so is `𝓕*_δ`, a sublevel set of a convex lower semicontinuous function. Two refinements came from the
literature (`v14/related.md`, entries 18 and 24): blame mitigated by the cost of the better alternative, which `K`
ignores, now the negligence size where costs are declared, its formula still to be written; and the worst-case breach
rate over `𝓕`, which a deployment protocol guarantees whatever the actor does, still open.

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
so `𝓕(ℐ) ⊆ 𝓕`. The policy that chooses `f` with probability one produces `f`, so `𝓕 ⊆ 𝓕(ℐ)`. Closedness is not used. A
view that told the conditions apart would let a policy mix differently in each condition, producing every combination of
per-condition mixtures, a larger set than `𝓕` when `𝓕` ties the conditions together. ∎

**Notes.** The qualifier: a feasible set that is not convex, such as a parametric class of policies that cannot
randomize, is not the feasible set of any interface whose policies may randomize; it is a capacity limit, declared as a
set, and FA1 factors it, while FA2's Pythagorean form does not apply. With finitely many actions, (ii) covers polytopes.

## Every form of misalignment, by the layer that can define it

Each form is sorted by the least the framework needs to define it. Three questions mark the layers: what happened
(CORE), whether the actor could have done otherwise or known (INTERFACE), and why (PURPOSE).

| Form | Layer | The least it needs |
|---|---|---|
| breach of a requirement | CORE | the requirement |
| misalignment by condition, and a shift of the conditions' weights between test and use | CORE | conditions |
| hidden misalignment, in conditions no record covers | CORE to define; INTERFACE to bound | views or feasible sets that tie them to recorded ones ([D9], [P17]) |
| drift across runs or episodes | CORE | runs or episodes declared as conditions, judged by condition; dependence between acceptable decisions is no misalignment under the mixture principle (VE2, VE3), so [P54]'s drift and dependence terms are evidence against v13's independence, not parts of v14's number |
| the evaluation gap: a measured requirement met while the true one is breached | CORE | outcomes that hold both the measure and the truth |
| a shortfall below a declared floor | CORE | the floor, a requirement |
| side effects | CORE | requirements on the other coordinates of the outcome |
| unavoidable against avoidable, culpability | INTERFACE | the feasible behaviours |
| coarse perception, including not knowing what is asked | INTERFACE | views |
| execution noise | INTERFACE | the environment kernel |
| tampering against honest selection | INTERFACE, extended | the outcome split into the world and its measurement, with a declared honest channel the actions cannot reach ([P50]), and what is seen before acting |
| ignoring the situation against the environment's doing | INTERFACE | the split of actions from outcomes |
| collusion between actors | INTERFACE, for several actors (not yet defined here) | each actor's views and actions; with shared randomness allowed, the joint behaviours reachable with no communication beyond the views are mixtures of local strategies, a convex set, so communication is testable by bets; independence of private randomness is not convex, and no requirement a record enforces under the mixture principle (`v14/README.md`, the conventions; `LIMITS.md`) |
| gaming or reward hacking as a motive | PURPOSE | the actor's objective, an evaluator |
| overoptimization | PURPOSE | an intensity of optimization |
| outer misalignment | PURPOSE | the trainer's objective |
| inner misalignment | PURPOSE | the learned objective against the trainer's |
| strategic deception, alignment faking | INTERFACE and PURPOSE | views to tell when it is observed, and an objective over its own future |
| the shadow price of a constraint | PURPOSE | a model of the actor optimizing under it (VK5) |
| misspecification | none: not the actor's | a second standard, another principal or a later judgement |
| severity | the principal's side | a declared value scale (`NOTES.md` §24) |

**Three questions, not a ladder.** A breach (CORE), culpability above `0` (INTERFACE) and intent, the breach serving the
actor's objective (PURPOSE), are separate verdicts: intent is possible with culpability `0`, when the best the actor
could do serves its objective too. Their verification status differs: a breach is verifiable, culpability verifiable
with the interface taken as known, intent a refutable hypothesis (`factorization.md`, VF2). Culpability above `0`
charges any departure from the best feasible behaviour; reading it as negligence needs a tolerance, a margin the
principal declares.
