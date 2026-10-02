---
kind: corollary
id: C3
aliases: ["C3"]
source: "derived/forbids.md"
---
# C3 — An error confined to one region costs bounded nats
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c3--an-error-confined-to-one-region-costs-bounded-nats). Edit the source, not this note.

## Statement
Let `A` be a set of outcomes, `t > 0`, `F̂ = F + M·1_A` an evaluator whose error is confined to `A`,
`p̂ = p_{F̂,t}`, and `a = p_{F,t}(A)`. For every `M`,
`M(p̂) ≤ KL(p̂‖p_{F,t}) = kl(p̂(A)‖a) ≤ max(log(1/a), log(1/(1 − a)))`, where `kl(x‖y)` is the divergence between coins
with biases `x` and `y`. The bound is approached as `M → ∞` or `M → −∞`.

## In plain terms
An error confined to one region can be as large as one likes; the misalignment it causes in an
actor that pursues it is capped by how much of the pursuit's mass the region already had. A bound in nats is not a
bound in value: the stakes can still be large.

## Proof
By [[P1 — Every behaviour is a tilt of any other|P1]](iii), `p̂ = tilt(p_{F,t}, t·M·1_A)`, a reweighting by a function constant on `A` and on its
complement, so `p̂` splits each of the two as `p_{F,t}` does. By the chain rule [[P4 — What KL measures|P4]](iii), `KL(p̂‖p_{F,t})` is then
the divergence between the masses of `A`, `kl(p̂(A)‖a)`. As a function of `p̂(A)`, `kl(·‖a)` is convex, so it is at
most its larger value at the ends: `kl(1‖a) = log(1/a)` and `kl(0‖a) = log(1/(1 − a))`. As `M → ∞`, `p̂(A) → 1`, and
as `M → −∞`, `p̂(A) → 0`. Finally, `p_{F,t}` is on the pursuit ray, so `M(p̂) ≤ KL(p̂‖p_{F,t})` ([[D3 — Specification, declaration and misalignment|D3]]).

## Lineage
v7.10: §11.3 and Prop 4 (an error confined to one region saturates), imported here.

## Checks
- [`checks/test_forbids.py::test_an_error_confined_to_one_region_costs_bounded_nats`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_forbids.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item
