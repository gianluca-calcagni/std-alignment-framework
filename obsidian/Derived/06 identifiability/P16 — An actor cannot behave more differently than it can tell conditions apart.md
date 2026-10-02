---
kind: proposition
id: P16
aliases: ["P16"]
source: "derived/identifiability.md"
---
# P16 — An actor cannot behave more differently than it can tell conditions apart
> [!info] Generated from [derived/identifiability.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/identifiability.md#p16--an-actor-cannot-behave-more-differently-than-it-can-tell-conditions-apart). Edit the source, not this note.

## Statement
Let the actor's response depend on the condition only through a view `(Z, V)` ([[D8 — Conditions, responses and views|D8]]), and let `c` and
`c'` be conditions.
(i) If `V_c = V_{c'}`, then `p_c = p_{c'}`.
(ii) `KL(p_c‖p_{c'}) ≤ KL(V_c‖V_{c'})`.
(iii) If the view depends on the condition only through an input, that is, there are finitely many inputs `w`, with
distribution `W_c` in condition `c`, and distributions `K_w` on `Z` with `V_c = Σ_w W_c(w)·K_w`, then
`KL(V_c‖V_{c'}) ≤ KL(W_c‖W_{c'})`.

## In plain terms
An actor that perceives two situations alike acts alike in them. More generally, how differently it
can act in two situations is bounded by how well it can tell them apart, and it cannot tell them apart better than
what it receives in them differs.

## Proof
(i) `p_c = Σ_z V_c(z)·π_z` depends on `c` only through `V_c`. (ii) If some `z` has `V_c(z) > 0 = V_{c'}(z)`,
the right side is infinite. Otherwise, for each outcome `x`, the log-sum inequality applied to the numbers
`V_c(z)·π_z(x)` and `V_{c'}(z)·π_z(x)` gives `p_c(x)·log(p_c(x)/p_{c'}(x)) ≤ Σ_z V_c(z)·π_z(x)·log(V_c(z)/V_{c'}(z))`,
with the terms where `V_c(z)·π_z(x) = 0` left out. Summing over `x`, and using `Σ_x π_z(x) = 1`, gives (ii). (iii) is
(ii) with the inputs in the place of the signals and the distributions `K_w` in the place of the behaviours `π_z`.

## Notes
(ii) and (iii) are the data-processing inequality [[References|@cover2006]]. (iii) matters in practice: the principal can
bound how well the actor tells two conditions apart from what the actor receives in them, without knowing anything
about the actor. The bound holds only for a view that includes everything the actor uses. Memory across episodes,
timestamps and side channels are inputs too, and an input left out of `W` can make the bound false.

## Lineage
New. v7.10: ROADMAP §6 I1 (identification through interventions).

## Checks
- [`checks/test_identifiability.py::test_identical_views_give_identical_behaviour`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)
- [`checks/test_identifiability.py::test_behaviour_differs_no_more_than_views`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views

## Used by
- [[P17 — What an unobserved condition can hide|P17]] — What an unobserved condition can hide
- [[C10 — An actor cannot behave more differently than it can tell conditions apart|C10]] — An actor cannot behave more differently than it can tell conditions apart
