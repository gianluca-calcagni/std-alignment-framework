---
kind: proposition
id: P42
aliases: ["P42"]
source: "derived/structure.md"
---
# P42 — Several principals: gridlock, and the pooled pursuit
> [!info] Generated from [derived/structure.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/structure.md#p42--several-principals-gridlock-and-the-pooled-pursuit). Edit the source, not this note.

## Statement
Let principals `k = 1, …, K` declare standard specifications of objectives `F_k` from one default `q`,
with misalignments `M_k`, and let weights `w_k > 0` with `Σ_k w_k = 1` be declared. The **weighted misalignment** of
`p ∈ Δ` is `Σ_k w_k·M_k(p)`.
(i) **Gridlock.** `M_k(q) = 0` for every `k`, so `q` minimizes the weighted misalignment, and every minimizer has
`M_k = 0` for every `k`.
(ii) **Pooling.** If each principal declares one intensity `t_k ≥ 0`, so that its only intended behaviour is
`p_k = p_{F_k,t_k}`, then for every `p ∈ Δ`,
`Σ_k w_k·KL(p‖p_k) = KL(p‖p_{G,1}) + Σ_k w_k·log E_q[e^{t_k·F_k}] − log E_q[e^G]`, with `G = Σ_k w_k·t_k·F_k`. So the
pursuit of `G` at intensity `1` is the unique minimizer.

## In plain terms
When several principals each ask for a pursuit of their own objective from one default, doing
nothing satisfies all of them: the default is never misaligned under a standard specification, so gridlock is always a
best compromise. When each names the strength it wants, the compromise that disappoints them least on weighted average
is a single pursuit, of their objectives added up, each scaled by its strength and its weight. Who counts how much
remains a declaration, not a result.

## Proof
(i) `q = p_{F_k,0}` lies on every pursuit ray, so `M_k(q) = 0` for each `k`; a weighted sum of non-negative
terms with positive weights is `0` exactly when each term is.
(ii) `log p_k = log q + t_k·F_k − log E_q[e^{t_k F_k}]`, so
`Σ_k w_k·KL(p‖p_k) = KL(p‖q) − E_p[G] + Σ_k w_k·log E_q[e^{t_k F_k}]`. By [[P4 — What KL measures|P4]](i) at intensity `1` with the objective
`G`, `KL(p‖q) − E_p[G] = KL(p‖p_{G,1}) − log E_q[e^G]`, since the net value of `p_{G,1}` is `log E_q[e^G]`.

## Notes
(ii) is logarithmic pooling: the compromise multiplies the intended behaviours, each raised to its weight.
With floors ([[P35 — Floors and caps|P35]]) in place of fixed intensities, a probe found the compromise to be a pursuit of `Σ_k w_k·t_k·F_k`,
with `t_k` the intensity of its nearest intended behaviour for principal `k` (T5), often at the floors but not always
(T5b, a failed prediction); this is not claimed. Choosing the weights, by aggregating preferences, is outside the core.

## Lineage
New. `NOTES.md` §5.4, H13; probes T5 and T5b.

## Checks
- [`checks/test_structure.py::test_gridlock`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)
- [`checks/test_structure.py::test_pooling_with_declared_intensities`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)

## Depends on
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item
