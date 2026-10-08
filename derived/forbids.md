# Derived — what the core forbids

Each item states something the core rules out, as a corollary of earlier results, with the checks that would fail if it
happened. A framework that forbids nothing says nothing; this file collects, in one place, what data could contradict.

The archive's chapter "what the core forbids" (v7.10, §11) had nine statements. Eight are kept here, re-derived from the
core: C1–C8. The ninth said that the price and the budget conventions rank errors differently; it is about the price
convention, which the core does not use (`IMPORT.md`). C9–C12 are statements the core adds.

## Kept from the archive

### C1 — No ranking of errors holds at every budget
**Statement.** Let `E₁` and `E₂` be the errors of two evaluators known in the objective's units ([P29]), with
`Var_q(E₁) > Var_q(E₂)` and `max E₁ − min E₁ < max E₂ − min E₂`. Then `w_δ(E₁) > w_δ(E₂)` for every small enough budget
`δ`, and `w_δ(E₁) < w_δ(E₂)` for every `δ` at least as large as each `−log q(argmax E_i)` and `−log q(argmin E_i)`. So
the worst case of the objective lost ([P29](ii)) ranks the two errors one way at small budgets and the other way at
large ones.

**In plain terms.** An error that is spread out and an error that is rare but large cannot be ranked once and for all.
Under a small budget of departure the spread-out error does more damage; under a large one, the rare large error does.

**Proof.** By [P28](ii), `w_δ(E) = 2·(2δ·Var_q(E))^{1/2} + O(δ^{3/2})`, so the larger variance gives the larger width
for small `δ`. By [P28](iii), once `δ` reaches both ends of `E`, `w_δ(E)` is the range of `E`, so the larger range gives
the larger width. By [P29](ii), the width is the worst case of the objective lost.

**Checks.** checks/test_forbids.py::test_no_ranking_of_errors_holds_at_every_budget

**Notes.** The archive also measured the crossing for actual optimizers, not only for the worst case: for the pursuit
of the evaluator, best-of-`n` and policy gradient, at different departures for each (v7.10: R5, R6). Those are its
measurements; the core proves the crossing for the worst case only, and a worked case could test the rest.

**Lineage.** v7.10: §11.1, Thm 9 and the boundary claim C8 (crossing curves). The core's form uses [P28] and [P29].

### C2 — A KL budget does not contain a rare, large error
**Statement.** For every budget `δ > 0` and every number `B`, there are a default and an error `E` with `Var_q(E) = 1`
whose largest rise over the departure budget `δ` ([P27]) exceeds `B`, while its largest rise over the `χ²` budget `δ` is
at most `δ^{1/2}`.

**In plain terms.** Limiting how far an actor departs in KL does not limit the damage of an error that is rare but
large, however small the error's variance; limiting it in `χ²` does.

**Proof.** [P31](vi) with the variance held at `1`: the KL rise is at least `min(1, δ/log(1/r))·M·(1 − r)` with
`M = (r·(1 − r))^{−1/2}`, which grows without bound as `r → 0`, and the `χ²` rise is at most `(δ·1)^{1/2}`.

**Checks.** checks/test_feasibility.py::test_feasible_sets_of_other_shapes

**Lineage.** v7.10: §11.2 and Prop 11, in the form on finite outcomes of [P31](vi).

### C3 — An error confined to one region costs bounded nats
**Statement.** Let `A` be a set of outcomes, `t > 0`, `F̂ = F + M·1_A` an evaluator whose error is confined to `A`,
`p̂ = p_{F̂,t}`, and `a = p_{F,t}(A)`. For every `M`,
`M(p̂) ≤ KL(p̂‖p_{F,t}) = kl(p̂(A)‖a) ≤ max(log(1/a), log(1/(1 − a)))`, where `kl(x‖y)` is the divergence between coins
with biases `x` and `y`. The bound is approached as `M → ∞` or `M → −∞`.

**In plain terms.** An error confined to one region can be as large as one likes; the misalignment it causes in an
actor that pursues it is capped by how much of the pursuit's mass the region already had. A bound in nats is not a
bound in value: the stakes can still be large.

**Proof.** By [P1](iii), `p̂ = tilt(p_{F,t}, t·M·1_A)`, a reweighting by a function constant on `A` and on its
complement, so `p̂` splits each of the two as `p_{F,t}` does. By the chain rule [P4](iii), `KL(p̂‖p_{F,t})` is then the
divergence between the masses of `A`, `kl(p̂(A)‖a)`. As a function of `p̂(A)`, `kl(·‖a)` is convex, so it is at most its
larger value at the ends: `kl(1‖a) = log(1/a)` and `kl(0‖a) = log(1/(1 − a))`. As `M → ∞`, `p̂(A) → 1`, and as `M → −∞`,
`p̂(A) → 0`. Finally, `p_{F,t}` is on the pursuit ray, so `M(p̂) ≤ KL(p̂‖p_{F,t})` ([D3]).

**Checks.** checks/test_forbids.py::test_an_error_confined_to_one_region_costs_bounded_nats

**Lineage.** v7.10: §11.3 and Prop 4 (an error confined to one region saturates), imported here.

### C4 — Rescaling the objective is not misalignment
**Statement.** An actor that pursues `s·F` from `q`, for any `s > 0` and any intensity, has misalignment `0` and stakes
`0` under the standard specification of `F`.

**In plain terms.** Pursuing the objective harder or more gently than someone else would is not pursuing the wrong
thing.

**Proof.** `tilt(q, t·s·F) = p_{F, t·s}` is on the pursuit ray ([D2]), so its misalignment is `0` ([P5](ii)) and its
stakes are `0` ([P9](iv)).

**Checks.** checks/test_misalignment.py::test_zero_exactly_on_the_intended_set, checks/test_stakes.py::test_zero_stakes

**Notes.** The archive found that rescaling costs something only when the intended behaviour is required to keep the
actor's price of departing, the price convention the core does not use.

**Lineage.** v7.10: §11.4, Cor 13.3 and Remark 13.5.

### C5 — The first effect of optimization depends on the optimizer; its end, on the evaluator's top
**Statement.** Let `F̂` be an evaluator and `F` the objective.
(i) Along any path of behaviours from `q`, the objective's average starts to move at the rate `Cov_q(F_0, F)`, where
`F_0` is the path's first revealed objective; along the pursuit of `F̂`, at the rate `Cov_q(F̂, F)`.
(ii) One step of softmax policy gradient on `E_p[F̂]`, from the logits `log q`, is the tilt of `q` by `η·g` with
`g = q·(F̂ − E_q[F̂])`: it first pursues the evaluator weighted by the default. Its rate is
`η·Σ_x q(x)²·(F̂(x) − E_q[F̂])·(F(x) − E_q[F])`, which can have the opposite sign to `Cov_q(F̂, F)`.
(iii) Along the pursuit of `F̂`, the objective's average tends to its average under `q` over the outcomes where `F̂` is
largest, which is `max F` exactly when `F` is largest at all of them.

**In plain terms.** Whether pushing on an evaluator helps at first depends on how one pushes: the plain pursuit of the
evaluator and a gradient step can start in opposite directions. Where pushing hard ends depends only on the outcomes
the evaluator scores highest.

**Proof.** (i) is [P13](i), with [P20](i) for the pursuit. (ii) The derivative of `E_{softmax(θ)}[F̂]` in the logit
`θ(x)` is `p(x)·(F̂(x) − E_p[F̂])`; at `θ = log q` it is `g`, and the logits `log q + η·g` give `tilt(q, η·g)` ([D1]).
The revealed objective of `η ↦ tilt(q, η·g)` at `η = 0` is `g − E_q[g]`, so by (i) the rate is
`η·Cov_q(g, F) = η·Σ_x q(x)²·(F̂(x) − E_q[F̂])·(F(x) − E_q[F])`. The check exhibits instances where it and
`Cov_q(F̂, F)` have opposite signs. (iii) is [P20](ii): the limit is the regression at the largest value of `F̂`, which
is `max F` exactly when `F = max F` on that level set, since `q` gives each outcome positive mass.

**Checks.** checks/test_forbids.py::test_the_first_effect_depends_on_the_optimizer

**Lineage.** v7.10: §11.5, Prop 14 (initial and terminal effects) and Prop 22 (the first-order effect of any smooth
optimizer). New: the gradient step as the pursuit of `q·(F̂ − E_q[F̂])`.

### C6 — A monotone regression forbids overoptimization
**Statement.** If the regression of the objective on an evaluator is non-decreasing in it ([D10]), no path from `q`
whose revealed objectives are non-decreasing in the evaluator lowers the objective's average. In particular, none does
when the regression is affine with a non-negative slope.

**In plain terms.** If, under the default, outcomes the evaluator scores higher are never worse on average for the
principal, following the evaluator harder never hurts the principal on average.

**Proof.** [P19]; an affine function with a non-negative slope is non-decreasing.

**Checks.** checks/test_evaluator.py::test_a_monotone_regression_rules_out_overoptimization

**Notes.** The archive's form was a target and an evaluator jointly Gaussian under the default, which have an affine
regression; on finitely many outcomes, the affine case is what remains of it.

**Lineage.** v7.10: §11.6, Prop 21 and the dictionary's B §4.

### C7 — No test detects misalignment faster than misalignment
**Statement.** From independent samples, no test separates the actor's behaviour from its nearest intended behaviour
with an error exponent above its misalignment `M(p̂)` ([P22]).

**In plain terms.** A small misalignment is, necessarily, slow to detect, even for an observer who knows both
behaviours exactly.

**Proof.** [P22](i) and (iii).

**Checks.** checks/test_estimation.py::test_detection_is_capped_by_misalignment

**Lineage.** v7.10: §11.7 and Prop 18.

### C8 — An evaluation weighted unlike use misses the evaluation gap
**Statement.** When each condition is judged on its own terms, the misalignment in use exceeds the misalignment in an
evaluation that meets the conditions in other proportions by exactly `Γ = Σ_c (ρ_dep(c) − ρ_ev(c))·M_c` ([P24]). An
evaluation that over-samples the conditions where the actor is closest to its specification understates the
misalignment in use.

**In plain terms.** An evaluation that meets easy situations more often than real use does reports less misalignment
than real use has, by a computable amount.

**Proof.** [P24](ii); over-sampling the conditions with the smaller `M_c` makes `Γ` positive.

**Checks.** checks/test_estimation.py::test_the_evaluation_gap

**Lineage.** v7.10: §11.8 and Prop 19.

## Added by the core

### C9 — Grouping outcomes never shows more misalignment
**Statement.** For any specification `(q, 𝓘)`, resolution `ℬ` and `p̂ ∈ Δ`, `inf_{p∈𝓘} KL(p̂_ℬ‖p_ℬ) ≤ M(p̂)`, where
`p_ℬ` gives each cell of `ℬ` its mass under `p`.

**In plain terms.** A principal who sees only coarse records never sees more misalignment than there is.

**Proof.** By [P4](iv), `KL(p̂_ℬ‖p_ℬ) ≤ KL(p̂‖p)` for every intended `p`; take the infimum over `𝓘`.

**Checks.** checks/test_forbids.py::test_grouping_never_shows_more_misalignment,
checks/test_value.py::test_merging_never_increases

**Lineage.** v8: [D3]'s "grouping only hides". New as a forbidden statement.

### C10 — An actor cannot behave more differently than it can tell conditions apart
**Statement.** If the actor's response depends on the condition only through its view ([D8]), then
`KL(p_c‖p_{c'}) ≤ KL(V_c‖V_{c'})` for any two conditions, and conditions it cannot tell apart get the same behaviour
([P16]). In particular, it does not behave differently when observed and when not unless its view tells the two apart.

**In plain terms.** Behaving well only when watched requires being able to tell when one is watched.

**Proof.** [P16](i) and (ii).

**Checks.** checks/test_identifiability.py::test_identical_views_give_identical_behaviour,
checks/test_identifiability.py::test_behaviour_differs_no_more_than_views

**Lineage.** v9: [P16]. New as a forbidden statement.

### C11 — No recovery after the fall
**Statement.** If the regression of the objective on an evaluator is single-peaked, then along the pursuit of the
evaluator, and along best-of-`n`, the objective's average never falls and then rises again ([P25](iii) and its Notes).

**In plain terms.** When the evaluator's scores are worth more to the principal up to a point and less beyond it,
pushing harder on the evaluator can help and then hurt, but it never helps again after it has started to hurt.

**Proof.** [P25](iii), and its Notes for best-of-`n`.

**Checks.** checks/test_evaluator.py::test_the_target_curve_turns_no_more_often_than_the_regression

**Lineage.** v10: [P25]. New as a forbidden statement.

### C12 — No misalignment, no stakes
**Statement.** Under the standard specification of a non-constant `F`, `M(p̂) = 0` implies `S(p̂) = 0`; and the stakes
are `0` with a positive misalignment only when the actor puts all its mass on the outcomes where `F` is largest, split
otherwise than the default splits them ([P9](iv)).

**In plain terms.** An actor that does what was intended loses nothing of the objective. The only way to lose nothing
while being misaligned is to choose only best outcomes, in proportions of one's own.

**Proof.** [P9](iv).

**Checks.** checks/test_stakes.py::test_zero_stakes

**Lineage.** v8: [P9](iv). New as a forbidden statement.
