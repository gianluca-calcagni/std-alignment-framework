---
kind: proposition
id: P39
aliases: ["P39"]
source: "derived/structure.md"
---
# P39 — Several actors: coordination plus individual misalignment
> [!info] Generated from [derived/structure.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/structure.md#p39--several-actors-coordination-plus-individual-misalignment). Edit the source, not this note.

## Statement
Let actors `i = 1, …, k`, with `k ≥ 2`, have finite outcome sets `X_i`, and take as outcomes the joint
outcomes `X = X_1 × … × X_k`. For `p ∈ Δ(X)` let `p_i` be its marginal on `X_i`, and write `⊗_i r_i` for the product of
behaviours `r_i` on the `X_i`. The **coordination** of `p` is `K(p) = KL(p‖⊗_i p_i)`. Let `(q_i, 𝓘_i)` be
specifications for the actors one by one, with misalignments `M_i`, and take on `X` the **independent pursuit**
specification: the default `⊗_i q_i`, and as intended behaviours the products `⊗_i r_i` with `r_i ∈ 𝓘_i`.
(i) For every `p ∈ Δ(X)` and all `r_i ∈ Δ°(X_i)`, `KL(p‖⊗_i r_i) = K(p) + Σ_i KL(p_i‖r_i)`.
(ii) Independent pursuit is a specification ([[D3 — Specification, declaration and misalignment|D3]]), and under it `M(p) = K(p) + Σ_i M_i(p_i)`. `K(p) ≥ 0`, with
equality exactly when `p` is the product of its marginals.
(iii) Coordination depends on what counts as one outcome: there is a behaviour of two actors over two rounds whose
coordination is `0` in each round and `2·log 2` on the two rounds taken together.

## In plain terms
When the principal wants several actors each to pursue its own objective on its own, their joint
misalignment is the sum of their own misalignments plus one more term that no single actor's record shows: how much
their outcomes go together, their coordination. Coordination can hide in time. Two actors can look independent in
every round and still be tightly coordinated across rounds.

## Proof
(i) Where `p(x) > 0`, every `p_i(x_i) > 0`, and
`log(p(x)/Π_i r_i(x_i)) = log(p(x)/Π_i p_i(x_i)) + Σ_i log(p_i(x_i)/r_i(x_i))`. Averaging under `p`, each last term
gives `KL(p_i‖r_i)`, since `x_i` has the distribution `p_i` under `p`.
(ii) The default and every `⊗_i r_i` with `r_i ∈ Δ°(X_i)` have full support. The intended set is closed in `Δ°(X)`: if
`⊗_i r_i^{(n)} → s ∈ Δ°(X)`, the marginals converge, `r_i^{(n)} → s_i`, with `s_i ∈ 𝓘_i` because each `𝓘_i` is closed
in `Δ°(X_i)`, and `s = ⊗_i s_i` by continuity. So [[D3 — Specification, declaration and misalignment|D3]] holds. By (i), the infimum over products splits into one
infimum per actor, which is `M_i(p_i)`. `K(p)` is a divergence, zero exactly when `p = ⊗_i p_i`.
(iii) Draw two fair coins `z_1` and `z_2` independently; actor 1 plays `z_1` then `z_2`, and actor 2 plays `z_2` then
`z_1`. In each round the two plays are independent fair coins, so the coordination is `0`. On the two rounds each actor's
outcome is uniform on four values, and so is the joint outcome, so `K = log 4 + log 4 − log 4 = 2·log 2`.

## Notes
Coordination is the total correlation of the actors' outcomes, the mutual information when there are two.
With finitely many joint outcomes, several actors are one actor on joint outcomes (`CORE.md` §0); coordination is what
that reading adds to the actors' own misalignments. Pricing algorithms that learn to sustain high prices across rounds
[[References|@calvano2020]] are the case of (iii): a regulator reading one round's table sees independent firms. Two tit-for-tat
players with 5% errors show `0` in every round and `0.231` nats per round over long records (`probes/general/`, T3).

## Lineage
New. `CORE-GENERAL.md`, draft 2, independence as a structural specification; `NOTES.md` §5.4, H11.

## Checks
- [`checks/test_structure.py::test_coordination_splits_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)
- [`checks/test_structure.py::test_coordination_can_hide_in_time`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment

## Used by
- no later item
