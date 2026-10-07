---
kind: proposition
id: P4
aliases: ["P4"]
source: "derived/value.md"
---
# P4 — What KL measures
> [!info] Generated from [derived/value.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/value.md#p4--what-kl-measures). Edit the source, not this note.

## Statement
Let `q ∈ Δ°`, `F : X → ℝ` and `t > 0`. The **net value** of `p ∈ Δ` is `J_t(p) = E_p[F] − KL(p‖q)/t`:
the average of the objective, minus the cost of departing from the default, priced at `1/t`.
(i) **Value.** For every `p ∈ Δ`, `J_t(p_{F,t}) − J_t(p) = KL(p‖p_{F,t})/t`. So `p_{F,t}` is the unique maximizer of
`J_t`.
(ii) **Every behaviour is an optimum.** For every `r ∈ Δ°`, `r = p_{G,1}` with `G = log(r/q)`. So `r` is the unique
maximizer of `J_1` for the objective `G`, and for every `p ∈ Δ` the net value `p` loses against `r` in that objective is
exactly `KL(p‖r)`.
(iii) **Chain rule.** For every partition `𝒢` of `X` into non-empty cells, every `p ∈ Δ` and every `r ∈ Δ°`,
`KL(p‖r) = KL(p_𝒢‖r_𝒢) + Σ_{C ∈ 𝒢, p(C) > 0} p(C)·KL(p(·|C)‖r(·|C))`, where `p_𝒢` is the distribution of the cell
masses `p(C)`.
(iv) **Merging never increases it.** `KL(p_𝒢‖r_𝒢) ≤ KL(p‖r)`, with equality if and only if `p/r` is constant on every
cell `C` with `p(C) > 0`.

## In plain terms
Count the net value of a behaviour as the average of an objective minus the cost of moving away from
the default. Then the best behaviour is the pursuit of the objective, at the intensity set by the price of moving away,
and the KL from any behaviour to it is exactly the net value given up. Every full-support behaviour is the best one for
some objective, so this reading always applies. KL also splits into a part between groups and a part within groups when
outcomes are grouped, and grouping outcomes can only hide differences, never create them.

## Proof
(i) With `Z = E_q[e^{tF}]`, `log p_{F,t} = log q + t·F − log Z`, so for every `p ∈ Δ`,
`KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + log Z = log Z − t·J_t(p)`. Hence `J_t(p) = (log Z − KL(p‖p_{F,t}))/t`. Taking the
difference at `p_{F,t}`, where the KL is `0`, and at `p` gives the identity. KL is non-negative, and zero only between
equal behaviours (Gibbs' inequality), so the maximizer is unique.
(ii) `p_{G,1} = tilt(q, log(r/q)) = r` by [[P1 — Every behaviour is a tilt of any other|P1]](i). Then apply (i) with `t = 1`.
(iii) For `x ∈ C` with `p(x) > 0`, `log(p(x)/r(x)) = log(p(C)/r(C)) + log(p(x|C)/r(x|C))`. Averaging over `p` gives the
identity.
(iv) By (iii), the difference is `Σ_C p(C)·KL(p(·|C)‖r(·|C)) ≥ 0`. It is zero if and only if `p(·|C) = r(·|C)` on every
cell with `p(C) > 0`, that is, if and only if `p/r` is constant there.

## Notes
(i) is the Gibbs variational principle. The net value is the objective of KL-regularized RL fine-tuning, and
a
free energy in the literature on bounded rationality [[References|@ortega2013]]. The same ray therefore arises twice: as the steepest
climb of [[D2 — Pursuit of an objective|D2]] and as the set of best behaviours at every price in (i). The chain rule and Gibbs' inequality are standard
[[References|@cover2006]]. Hobson characterized KL, up to a positive factor, by a small set of conditions that includes the chain
rule
(iii) [[References|@hobson1969]]. The last check confirms that three common alternatives (χ², squared Hellinger, total variation)
break it.

## Lineage
v7.10: Thm 1 (regret is a divergence) for (i); Def 21 (the within-cell divergence) for (iii) and (iv). New:
(ii), which follows from [[P1 — Every behaviour is a tilt of any other|P1]] and removes the need to assume that intended behaviour is "Gibbs", since every
full-support behaviour is. v7.10's Prop 15 (other regularizers) is not carried: the score is KL.

## Checks
- [`checks/test_value.py::test_value_identity`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)
- [`checks/test_value.py::test_every_behaviour_is_an_optimum`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)
- [`checks/test_value.py::test_chain_rule`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)
- [`checks/test_value.py::test_merging_never_increases`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)
- [`checks/test_value.py::test_other_divergences_break_the_chain_rule`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)

## Depends on
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D4 — Resolution|D4]] — Resolution
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced
- [[P38 — Any convex cost|P38]] — Any convex cost
- [[P36 — Ordinal objectives|P36]] — Ordinal objectives
- [[P7 — Indifference forgives exactly what happens inside cells|P7]] — Indifference forgives exactly what happens inside cells
- [[P8 — An actor that cannot tell outcomes apart|P8]] — An actor that cannot tell outcomes apart
- [[P9 — What is at stake|P9]] — What is at stake
- [[P17 — What an unobserved condition can hide|P17]] — What an unobserved condition can hide
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget
- [[P37 — A strong incentive masks the actor, and can fake alignment|P37]] — A strong incentive masks the actor, and can fake alignment
- [[P42 — Several principals: gridlock, and the pooled pursuit|P42]] — Several principals: gridlock, and the pooled pursuit
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
- [[P50 — Tampering: a change of the measurement, not of the world|P50]] — Tampering: a change of the measurement, not of the world
- [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] — What signals, audits and re-measurements reveal of tampering
- [[C3 — An error confined to one region costs bounded nats|C3]] — An error confined to one region costs bounded nats
- [[C9 — Grouping outcomes never shows more misalignment|C9]] — Grouping outcomes never shows more misalignment
