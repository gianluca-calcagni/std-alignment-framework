---
kind: proposition
id: P37
aliases: ["P37"]
source: "derived/estimation.md"
---
# P37 — A strong incentive masks the actor, and can fake alignment
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p37--a-strong-incentive-masks-the-actor-and-can-fake-alignment). Edit the source, not this note.

## Statement
Let `u` be an intervention ([[D6 — Intervention and pass-through|D6]]) with a unique outcome `x_u` of largest value, `d(x) = u(x_u) − u(x)`,
and `γ = min_{x≠x_u} d(x) > 0`. An actor whose behaviour is `p` passes it through with pass-through `φ` when its
behaviour becomes `p^φ = tilt(p, φ·u)`.
(i) **Masking.** For two actors with behaviours `p_1, p_2 ∈ Δ°`, let `a_i(x) = p_i(x)/p_i(x_u)` and
`c(x) = a_1(x)·log(a_1(x)/a_2(x)) − a_1(x) + a_2(x) ≥ 0`. As `φ → ∞`,
`KL(p_1^φ‖p_2^φ) = Σ_{x≠x_u} c(x)·e^{−φ·d(x)} + O(e^{−2φγ})`. So the divergence vanishes like `e^{−φγ}`, and the
Chernoff information between the two actors, the best error exponent of any test between them, at least as fast
([[P22 — No test detects misalignment faster than misalignment|P22]](ii)); and `(1/φ)·log KL(p_1^φ‖p_2^φ) → −γ` when `c > 0` at some outcome with `d = γ`.
(ii) **Fake alignment.** In a condition where `u` and the objective `F` have the same unique best outcome, the
misalignment of `p^φ` under the standard specification of `F` tends to `0` as `φ → ∞`. So if an actor faces `u` only in
the conditions where it is evaluated, judged as in [[P24 — The evaluation gap|P24]], its misalignment in evaluation can be made as small as one
likes by a strong enough incentive, while in the conditions of use, where it faces no incentive, its misalignment is
that of its own behaviour, and the evaluation gap tends to the whole misalignment in use.
(iii) **Reward hacking shows.** In a condition where the unique best outcome `x_u` of `u` is not among the best
outcomes of `F`, the misalignment of `p^φ` tends to `−log sup_{t≥0} p_{F,t}(x_u) > 0`.

## In plain terms
A strong enough incentive makes every actor behave almost alike: two actors with different aims
become indistinguishable by any test, exponentially fast as the incentive grows. Where the incentive points at what the
principal wants, every actor looks aligned under evaluation, whatever it does where it is not evaluated: alignment can
be faked by incentives at evaluation time alone. Where the incentive points elsewhere, the misalignment it causes shows,
and stays.

## Proof
(i) For `x ≠ x_u`, `p_i^φ(x) = a_i(x)·e^{−φ·d(x)}/(1 + S_i)` and `p_i^φ(x_u) = 1/(1 + S_i)`, with
`S_i = Σ_{y≠x_u} a_i(y)·e^{−φ·d(y)} = O(e^{−φγ})`. Write `KL(p_1^φ‖p_2^φ)` as the sum over `x` of
`p_1^φ·log(p_1^φ/p_2^φ) − p_1^φ + p_2^φ`, the added terms summing to zero. For `x ≠ x_u` the term is
`e^{−φ·d(x)}·(c(x) + O(S_1 + S_2))`, and at `x_u` it is of order `(S_1 − S_2)²`. Since
`Σ_{x≠x_u} e^{−φ·d(x)} = O(e^{−φγ})`, the corrections are `O(e^{−2φγ})`. By [[P22 — No test detects misalignment faster than misalignment|P22]](ii) the Chernoff information is at
most the divergence. (ii) Let `x*` be the shared best outcome. For every `t ≥ 0`, `M(p^φ) ≤ KL(p^φ‖p_{F,t})`, and
`KL(p^φ‖p_{F,t}) ≤ −log p_{F,t}(x*) + Σ_{x≠x*} p^φ(x)·(log(1/q(x)) + t·(max F − min F))`, using `log p^φ ≤ 0` and
`p_{F,t}(x) ≥ q(x)·e^{−t·(max F − min F)}`. With `t = φ^{1/2}`, the first term tends to `0`, since `x*` is the unique
best outcome of `F`, and the sum tends to `0`, since `p^φ(x) = O(e^{−φγ})` for `x ≠ x*`. In the conditions without the
incentive the behaviour, and so its misalignment, does not depend on `φ`; [[P24 — The evaluation gap|P24]] gives the gap. (iii) `p^φ` tends to the
point mass at `x_u`. For each `t`, `KL(p^φ‖p_{F,t}) → −log p_{F,t}(x_u)`, which bounds the limit superior of the
misalignment by `inf_t (−log p_{F,t}(x_u))`. Conversely, grouping into `{x_u}` and its complement ([[P4 — What KL measures|P4]](iv)) gives
`KL(p^φ‖p_{F,t}) ≥ −p^φ(x_u)·log p_{F,t}(x_u) − h(p^φ(x_u))`, with `h` the entropy of a coin, which gives the matching
lower bound as `p^φ(x_u) → 1`. The limit is positive: `p_{F,t}(x_u) < 1` for every `t` and tends to `0` as `t → ∞`,
since `x_u` is not a best outcome of `F`, so its supremum is below `1`.

## Notes
The archive derived these for an agent that values reward through a continuation value (its hypothesis
`E_R`); here the incentive enters only through the observed pass-through of [[D6 — Intervention and pass-through|D6]], so no model of the agent's stake in
the reward is needed. [[P17 — What an unobserved condition can hide|P17]] bounds the other route to the same gap: a behaviour that differs in conditions the actor can
tell apart. Evaluations with strong incentives that point where the principal's objective does are therefore weak
evidence of alignment in use; an incentive that points elsewhere makes misalignment show instead ((iii)).

## Lineage
v7.10: Prop 28 (incentive masking) and Prop 30 (the fake-alignment gap), without the reward coupling of
Def 16. New: the leading form in (i) as a statement, and the derivation from pass-through alone.

## Checks
- [`checks/test_estimation.py::test_a_strong_incentive_masks_the_actor_and_can_fake_alignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[D6 — Intervention and pass-through|D6]] — Intervention and pass-through
- [[P4 — What KL measures|P4]] — What KL measures
- [[P22 — No test detects misalignment faster than misalignment|P22]] — No test detects misalignment faster than misalignment
- [[P24 — The evaluation gap|P24]] — The evaluation gap

## Used by
- no later item
