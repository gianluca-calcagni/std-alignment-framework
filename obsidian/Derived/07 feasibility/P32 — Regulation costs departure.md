---
kind: proposition
id: P32
aliases: ["P32"]
source: "derived/feasibility.md"
---
# P32 — Regulation costs departure
> [!info] Generated from [derived/feasibility.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/feasibility.md#p32--regulation-costs-departure). Edit the source, not this note.

## Statement
Let the conditions `c` ([[D8 — Conditions, responses and views|D8]]) have frequencies `ρ(c) > 0` that the actor does not choose. Let the actor's
response in condition `c` be a behaviour `p_c` on finitely many actions, all with one default `q`, and let the result of
action `x` in condition `c` be `φ(c, x)`, with `φ(·, x)` injective for every action `x`: no action gives two conditions
the same result. Under `ρ` and the response, write `C`, `X`, `Z` for the condition, the action and the result, `H` for
entropy in nats, `p̄ = Σ_c ρ(c)·p_c` for the average action, and `I(C; X) = Σ_c ρ(c)·KL(p_c‖p̄)` for the information the
actions carry about the conditions.
(i) `Σ_c ρ(c)·KL(p_c‖q) = I(C; X) + KL(p̄‖q)`.
(ii) `H(Z) ≥ H(C) − I(C; X)`.
(iii) So a response whose average departure `Σ_c ρ(c)·KL(p_c‖q)` is at most `δ` leaves `H(Z) ≥ H(C) − δ`. For the
objective of hitting a result `z₀`, the miss rate `g = P(Z ≠ z₀)` satisfies `h(g) + g·log(m − 1) ≥ H(C) − δ`, with `h`
the entropy of a coin with bias `g` and `m` the number of results: a floor on the misses that falls as the budget grows.

## In plain terms
An actor that must counter situations it does not choose, to keep the result steady, has to act
differently in different situations, and acting differently costs departure from its one default. So the variety of the
situations, less the departure spent, is a floor on the variety of the result. With a small budget, an actor cannot hit
a target reliably when the situations vary much.

## Proof
(i) `Σ_c ρ(c)·Σ_x p_c(x)·log(p_c(x)/q(x))` splits as `Σ_c ρ(c)·Σ_x p_c(x)·log(p_c(x)/p̄(x))` plus
`Σ_x p̄(x)·log(p̄(x)/q(x))`. (ii) `H(Z) ≥ H(Z|X)`, since conditioning does not increase entropy. Given the action, the
result determines the condition, by injectivity, and the condition determines the result, so `H(Z|X) = H(C|X)`, which
is `H(C) − I(C; X)`. (iii) By (i), `I(C; X)` is at most the average departure. A distribution on `m` results with mass
`1 − g` on `z₀` has entropy at most `h(g) + g·log(m − 1)`, the entropy when the rest is spread evenly [[References|@cover2006]].

## Notes
(ii) is Ashby's law of requisite variety [[References|@ashby1956]] in Conant's information form [[References|@conant1969]]; (i) prices
it in the core's unit, the departure from the default. The set of responses with average departure at most `δ` is the
departure budget of [[P27 — The best use of a departure budget|P27]] on condition–action pairs, with the frequencies of the conditions fixed: a convex feasible
set ([[D7 — Feasibility|D7]]). The check confirms that the floor can fail when an action gives two conditions the same result. In each
condition, [[P4 — What KL measures|P4]] applies as stated; v7.10's closed-loop lift also re-derived it there. When the default is itself chosen
to minimize the average departure, it is the average action `p̄`, and the departure is the information `I(C; X)`:
rational inattention (`RELATED.md`, bounded rationality), which is not imported yet.

## Lineage
v7.10: the dictionary's entry B7, parts (a)–(d) (the closed-loop lift), and its check V9. Part (e),
rational inattention, is not imported (`IMPORT.md`).

## Checks
- [`checks/test_feasibility.py::test_regulation_costs_departure`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views

## Used by
- no later item
