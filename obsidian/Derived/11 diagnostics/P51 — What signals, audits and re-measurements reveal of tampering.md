---
kind: proposition
id: P51
aliases: ["P51"]
source: "derived/diagnostics.md"
---
# P51 — What signals, audits and re-measurements reveal of tampering
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p51--what-signals-audits-and-re-measurements-reveal-of-tampering). Edit the source, not this note.

## Statement
In the setting of [[P50 — Tampering: a change of the measurement, not of the world|P50]], let `p ∈ Δ`, with distribution of signals `p_S`. For a channel `C` from `W` to a
finite set `Z`, whose distributions `C(·|w)` need not have full support, and a distribution `μ` on `Z`, let
`L_C(μ) = min_{r_W} KL(μ‖C^⊤r_W)` over the distributions `r_W` on `W`, where `(C^⊤r_W)(z) = Σ_w r_W(w)·C(z|w)` is what
the world `r_W` produces through `C`; write `L = L_K`.
(i) **The least tampering the signals show.** The minimum is attained, and `T(p) ≥ L(p_S)`. If `r*_W` attains `L(p_S)`,
the behaviour `p*(w, s) = r*_W(w)·K(s|w)·p_S(s)/(K^⊤r*_W)(s)` has signals `p_S` and tampering `L(p_S)`, so no smaller
tampering is consistent with the signals; and `L(p_S) = 0` exactly when some distribution of worlds produces `p_S`
through `K`. For every `r_W` with `KL(μ‖C^⊤r_W)` finite, with `c(w) = Σ_{z : μ(z) > 0} C(z|w)·μ(z)/(C^⊤r_W)(z)`,
`KL(μ‖C^⊤r_W) − log max_w c(w) ≤ L_C(μ) ≤ KL(μ‖C^⊤r_W)`: a certificate for any computed `r_W`.
(ii) **The most.** The values of `T` over the behaviours with signals `p_S` form the interval `[L(p_S), Ū(p_S)]`, where
`Ū(p_S)` is the largest tampering among the behaviours in which every signal comes from a single world:
`p_a(w, s) = p_S(s)` if `w = a(s)` and `0` otherwise, for a map `a` from `S` to `W`. `Ū(p_S) ≥ max_w KL(p_S‖K(·|w))`,
and if `W` and `S` each have at least two elements, `Ū(p_S) > 0` for every `p_S`: no distribution of signals, not even
the default's, rules tampering out.
(iii) **An audit.** Let each world be measured a second time through a channel `K'` from `W` to a finite set `S'` that
the actor cannot influence, so that the actor's behaviour on `(w, s, s')` is `p(w, s)·K'(s'|w)`, and let `p_{SS'}` be
its distribution of the two signals. With `(K⊗K')(s, s'|w) = K(s|w)·K'(s'|w)`, `L(p_S) ≤ L_{K⊗K'}(p_{SS'}) ≤ T(p)`. If
the audit is exact, `S' = W` and `K'(·|w)` the point mass at `w`, then `L_{K⊗K'}(p_{SS'}) = T(p)`, and tampering is
identified ([[D9 — Observation and identification|D9]]).
(iv) **A re-measurement.** If `K' = K`, a second honest measurement through the same channel, the evaluator's gain over
the default splits exactly into an **honest gain** and a **channel gain**:
`E_p[F̂] − E_q[F̂] = (E_{p_W}[m] − E_{q_W}[m]) + (E[F̂(s)] − E[F̂(s')])`, where both averages of the second term are
under the actor's behaviour on `(w, s, s')`, and `E[F̂(s')] = E_{p_W}[m]`. The channel gain, the fall of the average
score from the first measurement to the second, satisfies `|E[F̂(s)] − E[F̂(s')]| ≤ (max F̂ − min F̂)·(T(p)/2)^{1/2}`,
and `KL(p_S‖p_{S'}) ≤ T(p)`.

## In plain terms
From the signals alone a principal sees only part of the tampering: the least that any actor would
need to produce signals like these, which is positive when the scores come out in a way no honest measurement of any
world produces. Some actor tampers exactly that much, so the signals cannot show more; and they cannot rule tampering
out, because every distribution of signals, even the default's, could come from an actor that tampers. An audit through
a measurement the actor cannot touch raises the lower end, up to the whole tampering when the audit sees the world
exactly. Measuring the same worlds again through the honest channel separates what the actor gained by changing the
world from what it gained through the measurement: the second shows as the fall of the score on re-measurement, and it
bounds the tampering from below.

## Proof
(i) `r_W ↦ KL(μ‖C^⊤r_W)` is lower semicontinuous on the compact set of distributions on `W`, so the minimum
is attained; for `C = K` it is finite, as `K` has full support. By [[P50 — Tampering: a change of the measurement, not of the world|P50]](i), `T(p) = KL(p‖p_W ⊗ K)`, and merging the
pairs into their signals never increases KL ([[P4 — What KL measures|P4]](iv), whose proof needs only that the second behaviour be positive
wherever the first is), so `T(p) ≥ KL(p_S‖K^⊤p_W) ≥ L(p_S)`. The signals of `p*` are
`p_S(s)·(K^⊤r*_W)(s)/(K^⊤r*_W)(s) = p_S(s)`, and its worlds are `r*_W(w)·c*(w)`, with `c*` the `c` of the certificate at
`r*_W`, for `C = K` and `μ = p_S`. The function `r_W ↦ −Σ_s p_S(s)·log (K^⊤r_W)(s)` is convex, with partial derivatives
`−c(w)`, so at its minimum `c*(w) ≤ λ` for every `w`, with equality where `r*_W(w) > 0`; as
`Σ_w r*_W(w)·c*(w) = Σ_s p_S(s) = 1`, `λ = 1`. So the worlds of `p*` are `r*_W`, its signals given `w` are `K(·|w)·ρ`
with `ρ = p_S/(K^⊤r*_W)`, and `T(p*) = Σ_w r*_W(w)·Σ_s K(s|w)·ρ(s)·log ρ(s) = Σ_s p_S(s)·log ρ(s) = L(p_S)`.
`L(p_S) = 0` exactly when `p_S = K^⊤r_W` for some `r_W`, by Gibbs' inequality. For the certificate, let `r*_W` attain
`L_C(μ)`; by Jensen's inequality,
`KL(μ‖C^⊤r_W) − L_C(μ) = Σ_{z : μ(z) > 0} μ(z)·log((C^⊤r*_W)(z)/(C^⊤r_W)(z)) ≤ log Σ_w r*_W(w)·c(w) ≤ log max_w c(w)`.
(ii) The behaviours with signals `p_S` form a polytope: for each `s`, `p(·, s)` is `p_S(s)` times a distribution on `W`,
so the vertices are the `p_a`. `T(p) = KL(p‖p_W ⊗ K)` is convex in `p`, because KL is jointly convex and `p ↦ p_W ⊗ K`
is linear, and it is continuous, because `K` has full support. A convex function on a polytope attains its maximum at a
vertex, and a continuous function maps the connected polytope onto an interval, which contains `L(p_S)` by (i). The
constant map at `w` gives the behaviour with the single world `w` and signals `p_S`, whose tampering is
`KL(p_S‖K(·|w))`. That is positive unless `K(·|w) = p_S`. If every `K(·|w)` equals `p_S`, then `p_S` has full support on
`S`, which has two elements, so some signal `s₁` has `0 < p_S(s₁) < 1`; mapping `s₁` to one world and every other signal
to another gives tampering at least `p_S(s₁)·KL(δ_{s₁}‖p_S) = −p_S(s₁)·log p_S(s₁) > 0`, where `δ_{s₁}` is the point
mass at `s₁`.
(iii) Where `p(w, s)·K'(s'|w) > 0`, the ratio of the actor's behaviour on `(w, s, s')` to `p_W(w)·K(s|w)·K'(s'|w)` is
`p(s|w)/K(s|w)`, so the divergence between them is `T(p)`. Merging into `(s, s')`, as in (i), gives
`T(p) ≥ KL(p_{SS'}‖(K⊗K')^⊤p_W) ≥ L_{K⊗K'}(p_{SS'})`, and merging away `s'` gives
`KL(p_{SS'}‖(K⊗K')^⊤r_W) ≥ KL(p_S‖K^⊤r_W)` for every `r_W`, so `L_{K⊗K'}(p_{SS'}) ≥ L(p_S)`. For an exact audit,
`(K⊗K')^⊤r_W(s, w) = r_W(w)·K(s|w)` and `p_{SS'}(s, w) = p(w, s)`, so the divergence is
`KL(p‖r_W ⊗ K) = KL(p_W‖r_W) + T(p)` by [[P50 — Tampering: a change of the measurement, not of the world|P50]](i), least at `r_W = p_W`.
(iv) `E[F̂(s')] = Σ_{w,s,s'} p(w, s)·K(s'|w)·F̂(s') = E_{p_W}[m]`, and `E_q[F̂] = E_{q_W}[m]`, so the split is an
identity. `E_{p_W}[m]` is also the average of `F̂` under `p_W ⊗ K`, from which `p` departs by `T(p)` ([[P50 — Tampering: a change of the measurement, not of the world|P50]](i)); the
difference of two averages of `F̂` is at most `max F̂ − min F̂` times the total variation distance, which Pinsker's
inequality bounds by `(KL/2)^{1/2}` ([[References|@polyanskiy2025]], Theorem 7.10, read in its open draft). Finally
`p_{S'} = K^⊤p_W`, so `KL(p_S‖p_{S'}) ≤ T(p)` by (i).

## Notes
(ii) is the identified set ([[D9 — Observation and identification|D9]]) of tampering for a principal who sees signals only, and (iii) is the audit
as a designed observation that narrows it, as an intervention does for the pass-through ([[D6 — Intervention and pass-through|D6]]). `L(p_S)` is a problem of
maximum likelihood: the least divergence of the signals from the mixtures of the honest channel's distributions, as in
estimating the weights of a mixture. The check computes it by the fixed point `r_W ← r_W·c`, the EM iteration for those
weights, polished by a constrained solver; the certificate of (i) makes any computed `r_W` a bracket, whatever the
solver. In `probes/diagnostics/probe_grounding.py`, an actor that leaves the world at the default and measures each
world `n` times, keeping the signal the evaluator scores highest, has no honest gain, and all its gain is channel gain.
The signals alone reveal a median of about half its tampering (`49%`, `52%` and `46%` for `n` = 2, 4 and 16, from `0%`
to `98%` across instances), the fall on re-measurement through (iv)'s bound a median `30%` for `n = 4`, and an exact
audit all of it. (iv) needs the second measurement to be honest. If the actor's influence persists, as with a sensor
replaced, the second measurement goes through the actor's channel, and the fall can be `0` while `T > 0`: a
re-measurement through the same instrument exposes selection on the noise of measurement, not every tampering. Only a
channel the actor cannot influence, as in (iii), bounds both kinds from below.

## Lineage
New, from the grounding brainstorm (`NOTES.md`, Q32). The optimality conditions in the proof of (i) are
those of a log-optimal portfolio [[References|@cover2006]], with the honest channel's distributions in the place of the assets; the
certificate follows from Jensen's inequality.

## Checks
- [`checks/test_diagnostics.py::test_signals_and_audits_bound_tampering`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P4 — What KL measures|P4]] — What KL measures
- [[P50 — Tampering: a change of the measurement, not of the world|P50]] — Tampering: a change of the measurement, not of the world

## Used by
- no later item
