---
kind: proposition
id: P35
aliases: ["P35"]
source: "derived/misalignment.md"
---
# P35 — Floors and caps
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p35--floors-and-caps). Edit the source, not this note.

## Statement
Let `F` be non-constant and `0 ≤ r ≤ s ≤ ∞`. The **intended segment** between a **floor** `r` and a
**cap** `s` is `𝓘_{r,s} = {p_{F,t} : r ≤ t ≤ s, t < ∞}`. It is closed in `Δ°`, so `(q, 𝓘_{r,s})` is a specification
([[D3 — Specification, declaration and misalignment|D3]]); `r = 0` and `s = ∞` give the standard specification. For `p̂ ∈ Δ°`, let `t̂ ∈ ℝ` be the intensity with
`E_{p_{F,t̂}}[F] = E_{p̂}[F]`, and `t° = min(max(t̂, r), s)`.
(i) The misalignment under the segment is `KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t°})`: the departure from the whole line of
pursuit, plus an undershoot when `t̂ < r` and an overshoot when `t̂ > s`.
(ii) **A floor is a minimum standard.** For `t ≥ 0`, `t ≥ r` exactly when `E_{p_{F,t}}[F] ≥ E_{p_{F,r}}[F]`: a floor
declares a minimum average of `F`, in its units, and a cap a maximum.
(iii) For `F = −1_H` and `0 < ε < q(H)`, the floor at which `p_{F,r}(H) = ε` is
`r = log(q(H)·(1 − ε)/(ε·(1 − q(H)))) > 0`, and under it the default itself is misaligned, by `KL(q‖p_{F,r}) > 0`;
under the standard specification its misalignment is `0`.
(iv) For `p_T ∈ Δ°` and `F = log(p_T/q)`, the behaviour with the largest `−KL(p‖p_T) − KL(p‖q)/t` is `p_{F, t/(1+t)}`:
as `t` grows from `0` to `∞`, imitating `p_T` with a KL penalty runs along the segment `𝓘_{0,1}`, from `q` toward
`p_T`.

## In plain terms
A principal can declare a minimum and a maximum strength of pursuit: "at least this much of the
objective, but no more than that". Misalignment is then the distance from the whole line of pursuit, plus how far the
actor falls short of the minimum or overshoots the maximum along it. A minimum strength is the same as a minimum
average of the objective. Under a minimum, doing nothing can be a failure: a principal who wants a fine to cut lateness
to a given rate charges an actor that keeps the default. Imitating a target behaviour with a penalty for departing
moves along such a segment, with the target as its end.

## Proof
With `Λ(t) = log E_q[e^{t·F}]`, `E_{p_{F,t}}[F] = Λ'(t)` and its derivative is `Var_{p_{F,t}}(F) > 0`, so
the average of `F` increases strictly along the line of pursuit, and `t̂` exists because `min F < E_{p̂}[F] < max F`.
For `s < ∞` the segment is the image of `[r, s]` under a continuous map, hence compact; for `s = ∞` it is the part of
the pursuit ray where the average of `F` is at least `Λ'(r)`, a closed part of a set closed in `Δ°` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)).
(i) For every `t ∈ ℝ`, `KL(p̂‖p_{F,t}) − KL(p̂‖p_{F,t̂}) = E_{p̂}[log(p_{F,t̂}/p_{F,t})] = (t̂ − t)·E_{p̂}[F] − Λ(t̂) + Λ(t)`,
and the same expression with `p_{F,t̂}` in place of `p̂` is `KL(p_{F,t̂}‖p_{F,t})`, since the two have the same average
of `F`. So `KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t})`. The second term is convex in `t`, as `Λ` is, and
zero at `t̂`, so over `[r, s]` it is smallest at the point nearest `t̂`, which is `t°`. (ii) follows from the strict
increase of the average. (iii) `p_{F,t}(H) = q(H)·e^{−t}/(q(H)·e^{−t} + 1 − q(H))` decreases continuously from `q(H)`
toward `0`; solving for `ε` gives `r`. The default `q = p_{F,0}` has `t̂ = 0 < r`, so by (i) its misalignment is
`KL(q‖p_{F,r}) > 0`; under the standard specification `q` is intended. (iv) The objective is strictly concave, and its
stationarity condition, `−log(p/p_T) − log(p/q)/t = constant`, gives `log p = log q + (t/(1 + t))·F + constant`.

## Notes
(iii) answers the principal for whom doing nothing is a failure ([[D3 — Specification, declaration and misalignment|D3]], Why). The archive also defined
budget versions of these measures; in the core, the comparison at the same departure is the stakes of [[D5 — Stakes|D5]].

## Lineage
v7.10: Defs 18 and 20 (caps; floors and the intended segment), Props 33 (a), (b), (d) and 35 (a), (c), and
Prop 37 (d) (a floor is a minimum standard); R7-6a and R7-6b. Their parts about the contract are dropped
(`IMPORT.md`).

## Checks
- [`checks/test_misalignment.py::test_floors_and_caps`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- no later item
