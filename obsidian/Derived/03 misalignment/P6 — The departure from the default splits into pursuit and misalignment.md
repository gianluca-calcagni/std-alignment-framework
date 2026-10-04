---
kind: proposition
id: P6
aliases: ["P6"]
source: "derived/misalignment.md"
---
# P6 — The departure from the default splits into pursuit and misalignment
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p6--the-departure-from-the-default-splits-into-pursuit-and-misalignment). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ` and let `p°` be as in [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv). The
**departure** of `p̂` from the default is `KL(p̂‖q)`, and
`KL(p̂‖q) = KL(p°‖q) + M(p̂)`.
So `0 ≤ M(p̂) ≤ KL(p̂‖q)`, and `M(p̂) = KL(p̂‖q)` when `E_{p̂}[F] ≤ E_q[F]`.

## In plain terms
How far the actor moved away from the default splits exactly into two parts: the movement explained
by pursuing the objective, and the misalignment. An actor that does no better than the default has all of its movement
counted as misalignment.

## Proof
In the first case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv), `p° = q` and `KL(q‖q) = 0`. In the second,
`log(p°/q) = t*·F − log E_q[e^{t*F}]`,
so `KL(p̂‖q) − KL(p̂‖p°) = E_{p̂}[log(p°/q)] = t*·E_{p̂}[F] − log E_q[e^{t*F}]`. Since `E_{p̂}[F] = E_{p°}[F]`, this
equals
`t*·E_{p°}[F] − log E_q[e^{t*F}] = E_{p°}[log(p°/q)] = KL(p°‖q)`. In the third, `p̂` and `q(·|A)` put all their mass on
`A`, so `KL(p̂‖q) − KL(p̂‖q(·|A)) = −log q(A) = KL(q(·|A)‖q)`. The bounds follow because KL is non-negative, and the
last
claim is the first case.

## Notes
The identity is a Pythagorean relation for KL along the pursuit ray. In RL fine-tuning the departure is the
KL from the reference policy, often treated as a budget; the identity splits that budget into the part spent on the
objective and the misaligned part. Whenever the actor departs from the default, `M(p̂)/KL(p̂‖q)` is the misaligned share
of its departure, between 0 and 1.

## Lineage
v7.10: Thm 13 (the intent-ray decomposition) and NOTES §2.5 (the intent ray). New: the third case, and the
reading as a split of the departure.

## Checks
- [`checks/test_misalignment.py::test_departure_splits_into_pursuit_and_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P47 — The cost of reweighting|P47]] — The cost of reweighting
- [[P48 — Misalignment when the target is uncertain|P48]] — Misalignment when the target is uncertain
