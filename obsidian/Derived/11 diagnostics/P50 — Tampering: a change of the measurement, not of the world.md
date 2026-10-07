---
kind: proposition
id: P50
aliases: ["P50"]
source: "derived/diagnostics.md"
---
# P50 — Tampering: a change of the measurement, not of the world
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p50--tampering-a-change-of-the-measurement-not-of-the-world). Edit the source, not this note.

## Statement
Let the outcomes be pairs, `X = W × S`: a state `w` of the world, and a signal `s`, the measurement from
which an evaluator is computed. Let the default be `q(w, s) = q_W(w)·K(s|w)`, with `q_W` a full-support distribution on
`W` and `K` a **channel**: for each `w`, a full-support distribution `K(·|w)` on `S`, the honest measurement of `w`. For
`p ∈ Δ`, let `p_W` be its distribution of worlds and, where `p_W(w) > 0`, `p(·|w)` its distribution of signals given
`w`; for a distribution `r_W` on `W`, let `r_W ⊗ K` be the behaviour `r_W(w)·K(s|w)`. The **tampering** of `p` is
`T(p) = Σ_{w : p_W(w) > 0} p_W(w)·KL(p(·|w)‖K(·|w))`, and `p` is **grounded** if `T(p) = 0`, that is, if `p = p_W ⊗ K`.
A function on `W` or on `S` is read as a function on `X`.
(i) **The split.** For every `p ∈ Δ` and every distribution `r_W` on `W`, `KL(p‖r_W ⊗ K) = KL(p_W‖r_W) + T(p)`. In
particular `KL(p‖q) = KL(p_W‖q_W) + T(p)`: the departure is the change of the world plus the tampering.
(ii) **A target on the world charges all tampering.** Let `F` be a non-constant function on `W`. The intended behaviours
of the standard specification of `F` are `p_{F,t} = tilt(q_W, t·F) ⊗ K`, all grounded, and for every `p̂ ∈ Δ`,
`M_F(p̂) = M^W_F(p̂_W) + T(p̂)`, where `M^W_F` is misalignment under the standard specification of `F` on `W`, from
`q_W`.
(iii) **The trainer's optimum tampers.** Let the evaluator `F̂` be a non-constant function on `S`, and let
`m(w) = E_{K(·|w)}[F̂]` be the expected score of the world `w`. For `t > 0`, `p_{F̂,t}` has worlds `tilt(q_W, Λ_t)`,
with `Λ_t(w) = log E_{K(·|w)}[e^{t·F̂}]`, and signals `tilt(K(·|w), t·F̂)` given `w`, so `T(p_{F̂,t}) > 0`. As `t → 0`,
`T(p_{F̂,t})/KL(p_{F̂,t}‖q) → 1 − R²`, where `R² = Var_{q_W}(m)/Var_q(F̂)` is the share of the evaluator's variance
under the default that the world explains. For a target `F` on `W`, let `θ` be the angle of [[P11 — The misaligned share at the start of a change|P11]] between `F̂` and `F`,
and `θ_W` the angle between `m` and `F` under `q_W` (with `R²·sin²θ_W` read as `0` when `m` is constant). Then
`sin²θ = (1 − R²) + R²·sin²θ_W`; the outer misalignment of [[P49 — Outer and inner misalignment|P49]] splits as `O(t) = M^W_F((p_{F̂,t})_W) + T(p_{F̂,t})`;
and as `t → 0` the world's part, divided by `KL(p_{F̂,t}‖q)`, tends to `R²·sin²θ_W` if `cos θ ≥ 0` and to `R²`
otherwise, so that outer misalignment's share at the start, `sin²θ` or `1`, is the tampering share `1 − R²` plus the
world's.
(iv) **The best grounded behaviour.** The grounded behaviours form a linear feasible set ([[D7 — Feasibility|D7]]) that contains `q`. Among
them, the unique maximizer of the net value `J_t` of `F̂` ([[P4 — What KL measures|P4]]) is `p^g_t = tilt(q_W, t·m) ⊗ K`: the world pursues the
expected score at the same intensity, and the measurement is left alone. It is the best feasible behaviour for
`r = p_{F̂,t}` ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]), and what tampering adds to the net value is
`t·(J_t(p_{F̂,t}) − J_t(p^g_t)) = KL(p^g_t‖p_{F̂,t}) = log E_q[e^{t·F̂}] − log E_{q_W}[e^{t·m}]`.

## In plain terms
Make the measurement part of what happens: each outcome records what the world became and what the
evaluator was shown. The default measures each world honestly, through a declared channel. Tampering is how far the
actor's measurements depart from the honest channel, given the world it produced; an actor that leaves the measurement
alone is grounded. The departure from the default is exactly the change of the world plus the tampering, and a principal
whose goal is stated on the world charges every nat of tampering as misalignment. The optimum of training on the
measured signal tampers at every intensity, because reweighting the signals of a world raises the score as surely as
changing the world does; at the start, the share of its change that is tampering is the share of the evaluator's
variance that is noise of the measurement. An actor that cannot tamper does best by pursuing each world's expected
score, at the same intensity, and the difference in net value is what tampering is worth.

## Proof
(i) Where `p(w, s) > 0`, `log(p(w, s)/(r_W(w)·K(s|w))) = log(p_W(w)/r_W(w)) + log(p(s|w)/K(s|w))`; averaging
under `p` gives the identity, with both sides infinite when `r_W` misses a world that `p` produces. With `r_W = q_W` it
is the departure.
(ii) `tilt(q, t·F)(w, s) = q_W(w)·e^{t·F(w)}·K(s|w)/E_{q_W}[e^{t·F}] = tilt(q_W, t·F)(w)·K(s|w)`. By (i),
`KL(p̂‖p_{F,t}) = KL(p̂_W‖tilt(q_W, t·F)) + T(p̂)` for every `t ≥ 0`; the second term does not depend on `t`, so the
infimum over `t` ([[D3 — Specification, declaration and misalignment|D3]]) gives the identity.
(iii) With `Z = E_{q_W}[e^{Λ_t}]`, `q_W(w)·K(s|w)·e^{t·F̂(s)}/Z = [q_W(w)·e^{Λ_t(w)}/Z]·[K(s|w)·e^{t·F̂(s)−Λ_t(w)}]`,
which gives the worlds and the signals. Each `tilt(K(·|w), t·F̂)` differs from `K(·|w)` when `t > 0`, by [[P1 — Every behaviour is a tilt of any other|P1]](ii),
because `F̂` is not constant on `S`, the support of `K(·|w)`; and every world has positive mass, so `T > 0`. The
expansion in the proof of [[P11 — The misaligned share at the start of a change|P11]] gives `KL(tilt(K(·|w), t·F̂)‖K(·|w)) = ½·t²·Var_{K(·|w)}(F̂) + O(t³)` and
`KL(p_{F̂,t}‖q) = ½·t²·Var_q(F̂) + O(t³)`; as the worlds tend to `q_W`, the ratio tends to
`E_{q_W}[Var_{K(·|w)}(F̂)]/Var_q(F̂)`, which is `1 − R²` by the law of total variance,
`Var_q(F̂) = Var_{q_W}(m) + E_{q_W}[Var_{K(·|w)}(F̂)]`. Since `F` depends on `w` only, `Cov_q(F̂, F) = Cov_{q_W}(m, F)`
and `Var_q(F) = Var_{q_W}(F)`, so `cos θ = R·cos θ_W`, with `R = (R²)^{1/2}`, and
`sin²θ = 1 − R²·cos²θ_W = (1 − R²) + R²·sin²θ_W`; when `m` is constant, `cos θ = 0` and `R = 0`. The split of `O(t)` is
(ii) at `p̂ = p_{F̂,t}`. Its share at the start is `sin²θ` if `cos θ ≥ 0` and `1` otherwise ([[P49 — Outer and inner misalignment|P49]](i)); subtracting the
tampering share `1 − R²` leaves the world's.
(iv) The grounded set is cut out by the equations `p(w, s)·K(s'|w) = p(w, s')·K(s|w)`, for all `w`, `s`, `s'`, each of
the form `E_p[f] = 0`; they say that `p(·|w)` is `K(·|w)` wherever `p_W(w) > 0`. For grounded `p = p_W ⊗ K`, (i) gives
`KL(p‖q) = KL(p_W‖q_W)`, and `E_p[F̂] = E_{p_W}[m]`, so `J_t(p) = E_{p_W}[m] − KL(p_W‖q_W)/t`, the net value of `m` on
`W`, whose unique maximizer is `tilt(q_W, t·m)` by [[P4 — What KL measures|P4]](i). By [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iv) the maximizer over the feasible set is the best
feasible behaviour for `r = p_{F̂,t}`, and `t·(J_t(p_{F̂,t}) − J_t(p^g_t)) = KL(p^g_t‖p_{F̂,t})`. By the proof of
[[P4 — What KL measures|P4]](i), `t·J_t(p_{F̂,t}) = log E_q[e^{t·F̂}]` and, on `W`, `t·J_t(p^g_t) = log E_{q_W}[e^{t·m}]`.

## Notes
Tampering counts every influence of the actor on the measurement, given the world: a reward rewritten, a
sensor covered or replaced, a rater persuaded, or a measurement repeated until it comes out well. [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] says what
signals, audits and re-measurements reveal of it, and separates the last kind from the others. What is world and what is
signal is declared, as the principal and the target are ([[P48 — Misalignment when the target is uncertain|P48]]), and the declaration decides what counts as tampering: a
text that persuades a rater is world if the world is the text, and a channel if the world is the facts the text reports
and the signal is the rater's verdict. The channel is declared with the default, before the behaviour is seen ([[D3 — Specification, declaration and misalignment|D3]]); a
channel known only to lie in a family would give an interval, as a target does in [[P48 — Misalignment when the target is uncertain|P48]], not stated here. An evaluator
that is a fixed function of the outcome, as the reward models of cases W1 to W4 were of the text, is the case where
every `K(·|w)` is a point mass: the default then lacks full support and the statement does not apply, and nothing could
be tampered without leaving the default's support. There every gap between evaluator and target is in the world, and is
outer misalignment ([[P49 — Outer and inner misalignment|P49]]), not tampering. The share `1 − R²` holds at the start only: in
`probes/diagnostics/probe_grounding.py`, with 4 worlds and 5 signals, the trainer's optimum at intensity 2 tampers by a
median `0.47` nats, and its tampering share differs from `1 − R²` by `−0.51` to `+0.21`. Two things stay outside: an
actor that changes what the principal wants, because the target is fixed by the declaration; and a change of the
evaluator's function `F̂`, unless the evaluator's output is taken as the signal, when changing it is tampering with the
channel.

## Lineage
v7.10 archive, gap 3 (grounding: wireheading and reward tampering), which `IMPORT.md` §8 mapped as "partly;
needs": a tampered measurement there was only an outcome that the evaluator scores high and the target low. New: the
measurement as part of the outcome, tampering as a divergence from a declared channel, and its split from the change of
the world, from the PI's question in `NOTES.md` (Q32). The causal analyses of reward tampering [[References|@everitt2021]] and the
corrupted reward channel [[References|@everitt2017]] are the nearest work (`RELATED.md`).

## Checks
- [`checks/test_diagnostics.py::test_tampering_splits_the_departure`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D7 — Feasibility|D7]] — Feasibility
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P4 — What KL measures|P4]] — What KL measures
- [[P11 — The misaligned share at the start of a change|P11]] — The misaligned share at the start of a change
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment

## Used by
- [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] — What signals, audits and re-measurements reveal of tampering
