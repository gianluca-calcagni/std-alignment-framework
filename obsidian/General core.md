# The general core

> **Status: draft 3.** Frozen by Q26, and unfrozen by Q33 for outcomes that are not finite and for estimation, which
> draft 4 takes up (`ROADMAP.md`, step 3); `general/dictionary.md` maps each object from the finite core to this file.
> This file extends the core (`CORE.md`, v11) from finitely many outcomes to the outcome spaces met in practice: counts,
> waiting times, scores, texts, trait values. It holds premises and definitions only, as `CORE.md` does for finite
> outcomes. Its results, expected, probed or tested, are in `general/`, as the finite core's are in `derived/`, and
> nothing there is claimed until it is proved and checked. Items are numbered GA (premises) and GD (definitions), and
> GD3 extends [[D3 — Specification, declaration and misalignment|D3]]. Every number the draft cites is reproduced by a script in `probes/general/`. Lint checks that every
> item this file and `general/` name exists (R12); it does not yet check their structure.

## 0. What this file is

The finite core is enough in practice: every record counts finitely many cells, minutes on a clock or digits of a score.
But a framework whose verdicts depended on how finely outcomes are described, or on what they are called, would be about
descriptions, not about alignment. This file asks what the core's definitions must become when outcomes are not finite,
and reads the answer for what alignment depends on.

**Three tests.** In the finite core, each choice had its own canonicity argument: Čencov's theorem for pursuit, [[P14 — The cost of departing from the default is forced|P14]]
for the cost. Here every definition must also pass three tests.
1. **Reduction.** On a finite outcome space it is the core's definition.
2. **Invariance.** It uses only the events, the sets of outcomes that have a probability. Relabelling the outcomes by a
   one-to-one map that carries events to events, both ways, changes nothing. So no distance, no topology and no
   reference measure, such as length or volume, appears in the framework.
3. **Finite determination** (GA6). Its value is the limit of its values on finite descriptions, groupings of the
   outcomes into finitely many cells, as the descriptions are refined.

The first and third tests together leave no freedom for any quantity the framework assigns to behaviours: on finite
descriptions its values are the core's, by reduction, and in general they are the limit of those, by finite
determination. A freedom remains only in a structure, such as which limits of intended behaviours are intended too; each
item's "Why" names it, and hands it to a declaration by the principal or a fact about the actor. The finite core met all
three tests without stating them. On a finite set every topology that separates points is the discrete one, so the core
never had to say which outcomes are near which. On a continuum many topologies have the same events [[References|@kechris1995]], so
the framework cannot choose one: where a topology matters, the principal or the actor supplies it, as each supplies a
resolution.

**What the tests show about alignment.**
- *Three kinds of outcome space, not more.* Any two uncountable standard Borel spaces are the same up to relabelling
  [[References|@kechris1995]]. By invariance, the framework tells apart only finite, countable and continuous outcome spaces. Whether
  the outcomes are waiting times, trait values or responses, alignment depends on them only through which events can be
  told apart (resolutions), which events are possible at all (the default), and what the parties declare.
- *Geometry belongs to the parties.* Which outcomes are near which enters through the principal's objective, and through
  declarations of nearness, never through the framework.
- *Two phenomena that finite outcomes hide.* (a) An actor can do what the default never does: pin one exact value, which
  the default produces with probability zero. Its misalignment is then infinite unless a declaration forgives it (GD3).
  (b) The tail of an objective can stop pursuit at a finite intensity; past it, more departure buys more of the
  objective only by betting on ever rarer extremes (GD2, GD5). Both say that the default decides more than it seemed to:
  which outcomes are possible, and how far pursuit can go.
- *Strategic scenarios become standard ones on derived spaces.* Several actors, actors that respond to the measurement,
  several principals and dependent samples each become a scenario with one principal and one actor, on a space of joint
  actions, rules, principals or trajectories, most of them continua even when the outcomes are finite. What stays
  strategic is measured as a divergence from a structure: independence, attention, reversibility, regularity
  (`general/derived-spaces.md`; on finite derived spaces, these are results of the finite core, `derived/structure.md`).

**Scope.** As in `CORE.md` §0, with outcomes and conditions in standard Borel spaces in place of finite sets. The finite
core takes groups of actors, several principals with declared weights, measurement rules as conditions and episodes of
dependent decisions into scope on finite outcomes; `general/derived-spaces.md` proposes the same on spaces that are not
finite: long records, large populations, continuous rules, models.

**How to read.** Six premises, GA1–GA6, and eleven definitions, GD1–GD11. Each "Why this choice" starts with the three
tests, then gives what is specific to outcomes that are not finite. The results are in `general/`, whose README gives
their reading order and the status of each. A bracketed name, such as [[D3 — Specification, declaration and misalignment|D3]] or [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]], is an item of `CORE.md` or a result
in `derived/`; GD3, without brackets, is an item of this file.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `(X, 𝔅)` | the outcomes and their events | GA1 |
| `Δ` | the behaviours: probability measures on the events | GD1 |
| `dp/dr` | the ratio of `p` to `r`, which exists when `p` never does what `r` never does | GD1 |
| `Δ_q` | the behaviours equivalent to the default | GD2 |
| `T_F`, `t_max` | the intensities at which pursuit of `F` exists; their upper end | GD2 |
| `𝒩`, `𝓘_0`, `𝓘` | a declared nearness; the declared intended behaviours; with their limits | GD3 |
| `σ(g)` | the resolution of a statistic `g`: the events it settles | GD4 |
| `Φ_F(B)` | the frontier: the most of `F` that a departure `B` can buy | GD5 |
| `k` | a noise kernel: the actor's precision | GD7 |
| `𝒫`, `N_𝒫` | a record's resolution; the record, its counts per cell | GD11 |

## 1. Premises

### GA1 — Behaviour suffices
**Statement.** The outcomes form a **standard Borel space** `(X, 𝔅)`: a set `X` with the **events** `𝔅` generated by the
open sets of some complete separable metric on `X`. What an actor does is described by the probability of every event,
in each condition it may face: a probability measure on `𝔅`. Alignment is judged from that description alone, never from
how the behaviour is produced.

**In plain terms.** We judge what the actor does, in every situation it may meet, and not what goes on inside it. What
it does is how probable each kind of outcome is, such as "the wait was between two and three hours": a single outcome,
such as a wait of exactly 2.5 hours, may have probability zero.

**Why this choice.**
- *Reduction.* On a finite set every set of outcomes is an event, and a probability on events is a probability on
  outcomes: this is [[A1 — Behaviour suffices|A1]].
- *Invariance.* Many metrics give the same events, and the premise names none: only the events are part of the
  description.
- *Finite determination.* Probabilities add over countably many disjoint events. That is what lets every event be
  approximated, to any accuracy in probability, by finitely many cells of a fixed sequence of finer and finer
  descriptions, so that counts in cells can determine a behaviour (GA6).
- *Why standard Borel spaces.* Every outcome space in the ontologies is one: counts, real numbers, vectors, finite
  sequences of tokens, curves. On them, conditioning on a statistic is well defined even when each of its values has
  probability zero (GD4); on more general measurable spaces it can fail. Requiring a topology instead would fail
  invariance.
- *What it costs.* "How often each outcome occurs" is no longer available: on a continuum, single outcomes carry no
  probability, and everything is said about events.

**Lineage.** [[A1 — Behaviour suffices|A1]]. v7.10: R7-8 (measurable spaces with a declared resolution, proposed and never done) and R7-5, case 5
(deterministic behaviour on a continuous `X`).

### GA2 — Pursuit is the steepest climb
**Statement.** As [[A2 — Pursuit is the steepest climb|A2]]: to pursue an objective is to raise its average as steeply as possible, with steepness measured
in a geometry on behaviours that does not change when outcomes are split into finer outcomes in fixed proportions.

**In plain terms.** As in the core: wanting more of something means moving toward it by the most direct route, and what
counts as most direct must not depend on how finely we describe what happens.

**Why this choice.**
- *Reduction.* The Statement is [[A2 — Pursuit is the steepest climb|A2]]'s.
- *Invariance.* Splitting outcomes in fixed proportions needs no distance: it is a kernel from coarse outcomes to fine
  ones.
- *Finite determination.* A behaviour whose ratio to another is constant on the cells of a finite description is a
  behaviour on those cells, split inside each in fixed proportions. Among such behaviours [[A2 — Pursuit is the steepest climb|A2]] gives the Fisher metric
  (Čencov's theorem [[References|@cencov1982]]). Since they approximate every behaviour, the geometry is the Fisher metric
  `⟨h, k⟩_p = E_p[h·k]` on directions `h` with `E_p[h] = 0` and `E_p[h²] < ∞`; the steepest climb of `E_p[F]` is the
  direction `F − E_p[F]`, and its flow from `q` is `tilt(q, s·F)` for as long as that tilt exists (GD2). To be proved
  (`general/transfer.md`).

**Lineage.** [[A2 — Pursuit is the steepest climb|A2]]. Ay, Jost, Lê and Schwachhöfer extend Čencov's theorem to general spaces directly, by invariance under
sufficient statistics [[References|@ay2015]]; GA6 gives a route that reuses the finite theorem instead.

### GA3 — Pursuit is the best trade-off
**Statement.** As [[A3 — Pursuit is the best trade-off|A3]], with the cost differentiable along segments: to pursue an objective at an intensity is to choose
the behaviour with the largest average of the objective minus a cost of departing from the default, priced at the
reciprocal of the intensity. With the default fixed, the cost depends only on the behaviour, and is differentiable along
every segment between two behaviours equivalent to the default.

**In plain terms.** As in the core: pursuing harder means accepting more cost of change for more of what is pursued, and
the cost depends only on how the behaviour changes.

**Why this choice.**
- *Reduction.* [[A3 — Pursuit is the best trade-off|A3]], with differentiability stated along segments.
- *Invariance.* ✓: the cost is a function of behaviours.
- *Finite determination.* On each finite description, [[P14 — The cost of departing from the default is forced|P14]] forces the cost to be the KL divergence from the default, up
  to a constant. The limit over finer descriptions is the supremum of those divergences, which is the divergence of GD1
  (the Gelfand–Yaglom–Perez theorem [[References|@pinsker1964]]). So the cost is forced on every outcome space. To be proved
  (`general/transfer.md`).
- *When no trade-off exists.* By the Donsker–Varadhan formula, the best net value at intensity `t` is
  `(1/t)·log E_q[e^{t·F}]`. When that is infinite, every behaviour is beaten by one that moves a little more probability
  into the objective's upper tail, and no behaviour is the best trade-off: the objective cannot be pursued at that
  intensity (GD2). For a reward model whose error has a heavy upper tail, this is the catastrophic Goodhart of Kwa,
  Thomas and Garriga-Alonso [[References|@kwa2024]].

**Lineage.** [[A3 — Pursuit is the best trade-off|A3]]; [[P14 — The cost of departing from the default is forced|P14]]. v7.10: Prop 11 (a KL limit cannot contain heavy-tailed errors), which becomes importable.

### GA4 — Misalignment is value lost
**Statement.** As [[A4 — Misalignment is value lost|A4]]: the misalignment of a behaviour is the least value it loses against a behaviour the principal
accepts, each accepted behaviour judged by its own objective at its own intensity, with value counted in nats.

**In plain terms.** As in the core: misalignment is how much worse the actor did than the closest acceptable way of
acting, judged by the standard of that acceptable way.

**Why this choice.**
- *Reduction; invariance.* The Statement is [[A4 — Misalignment is value lost|A4]]'s, and names no structure on the outcomes.
- *Finite determination.* Each accepted behaviour `p` equivalent to the default is the best trade-off for its own
  objective, `log(dp/dq)` at intensity `1`, as on finite outcomes ([[P4 — What KL measures|P4]](ii)); the value lost against it is a divergence,
  which finite descriptions determine (GD1).

**Lineage.** [[A4 — Misalignment is value lost|A4]].

### GA5 — Declared before
**Statement.** The default, the intended behaviours, and every nearness and resolution that enters a judgement,
including the resolution at which a record is kept, are fixed before, and without using, the behaviour they will judge.

**In plain terms.** Decide what counts as acceptable, which outcomes count as near, and how finely the record will be
kept, before looking at what the actor did.

**Why this choice.**
- *Reduction.* [[A5 — Declared before|A5]] names the default and the acceptable behaviours. On finite outcomes the core records every outcome,
  and needs no nearness; the one requirement added there is that a coarser record, such as the three time intervals of
  the medical-sciences ontology, is declared before the data too.
- *Why the record's resolution.* Misalignment at a resolution can only grow as its cells are refined ([[P4 — What KL measures|P4]](iv)), so
  cells chosen after seeing the data can be chosen to raise it or to lower it. Two grids of the same width give a
  controller that always hits its target exactly the misalignment `0` or `log 2` (`general/transfer.md`).
- *Why the nearness.* It decides which limits of intended behaviours are intended (GD3), and so whether an actor is
  aligned.

**Lineage.** [[A5 — Declared before|A5]]; README, rule of evidence (d).

### GA6 — Finite descriptions decide
**Statement.** A **finite description** of the outcomes is a partition of `X` into finitely many events, its **cells**;
one finite description **refines** another if each of its cells lies inside a cell of the other. Every quantity the
framework assigns to behaviours is the limit of the values it takes on the cell probabilities of finite descriptions, as
the descriptions are refined.

**In plain terms.** Anything the framework says about an actor can be checked, to any accuracy, by asking finitely many
yes-or-no questions about its outcomes.

**Why this choice.**
- *It is what GA1 presumes.* Behaviour is observed by counting, and a count is always of finitely many cells: a clock
  that reads minutes, a score kept to two digits. A quantity that finite descriptions do not determine could not be
  estimated from any record, however long.
- *Reduction.* On a finite space the finest description is finite and is the limit: the premise adds nothing to the
  core.
- *Invariance.* Partitions into events need no distance.
- *No grid is chosen.* The limit runs over all finite partitions into events, ordered by refinement; a quantity that can
  only grow under refinement has the supremum as its limit. A grid of equal intervals is one particular family of
  descriptions, and it can decide a verdict: two grids of the same width give a controller that always hits its target
  exactly the misalignment `0` or `log 2` (`general/transfer.md`). A grid is therefore a declaration, of the principal's
  nearness (GD3) or of a record's resolution (GD11), never part of the framework.
- *What it forces*, each to be proved (`general/transfer.md`):
  - the KL divergence as the cost on every outcome space (GA3);
  - the framework's only nearness between behaviours: two behaviours are near when every finite description finds their
    cell probabilities near, which needs no topology on the outcomes;
  - misalignment's meaning as a rate of evidence: Sanov's theorem on general spaces is the limit of its finite form over
    finite descriptions (the Dawson–Gärtner theorem [[References|@dembo1998]]);
  - intended sets closed under the limits that finite descriptions cannot tell apart (GD3);
  - the exclusion of quantities with no finite limit. The entropy of finer and finer descriptions of a continuous
    behaviour grows without bound, so differential entropy, which also changes with the units of measurement, is not a
    quantity of the framework; neither is a default that is not a probability (GD2).

**Lineage.** New. v7.10: R7-10, part (e), where continuous `X` was "covered by finite refinement only".

## 2. Behaviour and pursuit

### GD1 — Behaviours, ratios, divergence and tilt
**Statement.** `X` is a standard Borel space with events `𝔅` and at least two outcomes. A **behaviour** is a probability
measure `p` on `𝔅`, and `Δ` is the set of behaviours. For an event `C` with `p(C) > 0`, `p(·|C)` is `p` conditioned on
`C`. For a measurable `F : X → ℝ`, `E_p[F] = ∫ F dp` when the integral exists, and `Var_p` and `Cov_p` are as in [[D1 — Outcomes, behaviours, divergence and tilt|D1]]. A
behaviour `p` is **absolutely continuous** with respect to `r` if every event of probability zero under `r` has
probability zero under `p`; the **ratio** `dp/dr` is then the Radon–Nikodym derivative, fixed up to an event of
probability zero under `r`. Two behaviours are **equivalent** if each is absolutely continuous with respect to the
other. The **Kullback–Leibler divergence** is `KL(p‖r) = E_p[log(dp/dr)]` if `p` is absolutely continuous with respect
to `r`, and `+∞` otherwise. For a measurable `F` with `E_r[e^F] < ∞`, the **tilt** `tilt(r, F)` is the behaviour whose
ratio to `r` is `e^F/E_r[e^F]`.

**In plain terms.** A behaviour says how probable each kind of outcome is. The ratio of two behaviours says, outcome by
outcome, how much more often one produces it than the other; it exists when the first never does what the second never
does. Divergence and tilt are the core's, written with ratios in place of the probabilities of single outcomes.

**Why this choice.**
- *Reduction.* On a finite set the ratio is `p(x)/r(x)` where `r(x) > 0`; divergence and tilt are [[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s.
- *Invariance.* A ratio is defined from the two behaviours alone, with no reference measure.
- *Finite determination.* The divergence is the supremum, over finite descriptions, of the core's divergence between the
  cell probabilities [[References|@pinsker1964]]. A tilt by a function constant on the cells of a finite description is the core's
  tilt on those cells, with the proportions inside each cell kept, and every tilt is a limit of such tilts.
- *Equivalence replaces full support.* "Full support", positive probability on every open set, needs a topology and
  changes with it. On a finite set, full support is equivalence to any behaviour with full support; equivalence needs no
  topology, and GD2 uses it with the default.
- *Ratios to another behaviour, not densities.* Densities with respect to length or volume depend on units and
  coordinates, which fails invariance. They appear only inside checks, to compute.

**Lineage.** [[D1 — Outcomes, behaviours, divergence and tilt|D1]].

### GD2 — Pursuit of an objective
**Statement.** The **default** `q` is a behaviour, and `Δ_q` is the set of behaviours equivalent to it. An **objective**
is a measurable `F : X → ℝ`. The intensities at which its pursuit exists form the interval
`T_F = {t ≥ 0 : E_q[e^{t·F}] < ∞}`, from `0` to an upper end `t_max(F) ≤ ∞`, which it may or may not contain. The
**pursuit** of `F` at intensity `t ∈ T_F` is `p_{F,t} = tilt(q, t·F)`, and the **pursuit ray** is
`R_F = {p_{F,t} : t ∈ T_F}`. `F` is **pursuable** if `T_F` contains some `t > 0`. A path `s ↦ p_s` in `Δ_q` **pursues**
`F` if `p_s = tilt(p_0, τ(s)·F)` for a differentiable, non-decreasing `τ` with `τ(0) = 0`.

**In plain terms.** As in the core: pursuing an objective reweights the default toward the outcomes the objective scores
higher, and the intensity says how strongly. New: when the default reaches very high values of the objective often
enough, a heavy upper tail, pursuit exists only up to some intensity, or not at all. And the default must be a
behaviour: the actor's own way of acting when it pursues nothing.

**Why this choice.**
- *Reduction.* On a finite set, with a default of full support as [[D2 — Pursuit of an objective|D2]] requires, every objective is bounded,
  `T_F = [0, ∞)`, and `Δ_q = Δ°`: this is [[D2 — Pursuit of an objective|D2]].
- *Invariance; finite determination.* For an objective constant on the cells of a finite description, the pursuit is the
  core's, on the cells; every pursuit is a limit of these.
- *Canonical, given GA2 and GA3,* as in [[D2 — Pursuit of an objective|D2]]: the flow of the steepest climb and the best trade-off are this tilt, for
  as long as it exists.
- *Where it stops is forced, not chosen.* Past `t_max`, the best net value of GA3 is infinite and no behaviour attains
  it, so no pursuit exists there. A ray can stop with its averages still finite: `general/transfer.md` gives a default
  under which the pursuit of `F(x) = x` stops at intensity `1`, with the average of `F` stuck at `1`.
- *The default must be a probability.* The cost of departure, `KL(p‖q)`, is non-negative and zero only at `q` when `q`
  is a behaviour. Maximum-entropy reinforcement learning on unbounded continuous actions rewards entropy measured
  against length or volume, which is not a behaviour: "doing nothing" then does not exist, and the "cost" can be
  negative. Such a method fits the framework only with a proper default, such as a uniform default on a bounded set of
  actions, or a prior policy. This is the core's failure mode "a familiar formula that hides a typing error" (`NOTES.md`
  §1).
- *Behaviours equivalent to the default* rule out exactly what the default rules out. Every pursuit is one; a behaviour
  that is not makes a departure that no pursuit makes (GD3).

**Lineage.** [[D2 — Pursuit of an objective|D2]]. v7.10: Prop 11.

## 3. The specification and misalignment

### GD3 — Specification, nearness and misalignment
**Statement.** A **nearness** `𝒩` is either none or a topology on `X` that some complete separable metric generates and
whose open sets generate `𝔅`. A behaviour `p` is **indistinguishable** from a set `S` of behaviours if, for every finite
description and every `ε > 0`, some `p' ∈ S` gives each of its cells a probability within `ε` of the probability `p`
gives it; under a nearness, if instead, for every finitely many bounded functions continuous in `𝒩` and every `ε > 0`,
some `p' ∈ S` gives each of them an average within `ε` of `p`'s. A **specification** is a triple `(q, 𝓘_0, 𝒩)`: a
default `q`, a non-empty set `𝓘_0 ⊆ Δ_q` of declared intended behaviours, and a nearness. Its **intended behaviours**
`𝓘` are the behaviours indistinguishable from `𝓘_0`. The **misalignment** of `p̂ ∈ Δ` is `M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`.
The **standard specification** of an objective `F` under `𝒩` is `(q, R_F, 𝒩)`. A specification is **declared** when it
is fixed as GA5 requires. When no nearness is declared, there is none.

**In plain terms.** As in the core, the principal states a default and the behaviours it accepts, and misalignment is
the divergence to the nearest one. New: the principal may also say which outcomes count as near one another, such as
waiting times a second apart. That decides which limits of acceptable behaviours are acceptable too: for instance,
whether an actor that always hits the exact target, the limit of ever more precise pursuit, is acceptable. When the
principal says nothing, a limit counts only if every finite description agrees.

**Why this choice.**
- *Reduction.* On a finite set the only nearness is the discrete one, and both kinds of indistinguishability are
  convergence in `Δ`. Adding the limits does not change the infimum there, since `KL(p̂‖·)` is continuous at every limit
  where it is finite, so the misalignment is [[D3 — Specification, declaration and misalignment|D3]]'s; the limits are those that [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](ii) and the third case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)
  already count as intended.
- *Invariance: the framework fixes no nearness.* The events do not determine a topology: any event can be made both open
  and closed by refining a topology without changing the events [[References|@kechris1995]]. Which outcomes are near is part of what
  the principal means, like its resolution: waiting times a second apart are near for a four-hour target, and not for a
  sprint. So a nearness is declared, or there is none.
- *Finite determination forces the limits in.* Leaving out a behaviour that no finite description can tell apart from
  the intended ones would make misalignment depend on what no record can see. With densities proportional to
  `1 + ½·sin(k·x)` on a circle, the uniform behaviour's divergence from each of them is `0.069`, for every `k`, yet
  every finite description finds them converging to it (`general/transfer.md`). With those densities declared and the
  limit left out, the uniform behaviour would be misaligned by `0.069` while every record says `0`. Whether adding the
  limits is enough for misalignment to be the limit of its values on finite descriptions, in every case, is the first
  result to prove (`general/transfer.md`).
- *What a nearness decides: the on-target controller.* With a standard normal default on the real line and `F(x) = −x²`,
  pursuit narrows toward `0`. An actor that always outputs exactly `0` is, under the usual nearness of the line, the
  limit of pursuit, so its misalignment is `0`, as in the third case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv). With no nearness, the finite
  description whose cells are `{0}` and the rest tells it apart from every pursuit, each of which gives `{0}`
  probability zero: its misalignment is `+∞`.
- *What the usual nearness does not forgive: near misses.* An actor that always outputs exactly `0.001` is infinitely
  misaligned under the usual nearness too: no intended behaviour can produce exact repeats of one point that the default
  never produces. In plain terms, to pin a real number is to decide every one of its digits, and each digit decided
  beyond what the objective asks is a choice the principal did not ask for. At a resolution of width `w` the count is
  finite, and it grows at a precise rate: like `(D − d)·log(1/w)`, where `D` is the number of real coordinates of an
  outcome and `d` the information dimension of the actor's behaviour [[References|@renyi1959]], `D` for a behaviour spread like the
  default and `0` for one pinned to points. So each decimal digit of the record adds `2.3·(D − d)` nats: `2.3` for an
  actor pinned to points on a line, a tenth of that for one that piles a tenth of its behaviour on one value, and again
  `2.3` for one that pins one of two attributes and spreads the other (`general/transfer.md`). A principal who wants
  near misses graded declares a resolution (GD4), or judges outcomes that include noise the actor does not control
  (GD7). A distance that grades them directly cannot be the measure: GA3 and GA4 force the divergence.
- *The rest is [[D3 — Specification, declaration and misalignment|D3]]'s.* The formula is forced by GA3 and GA4, the direction charges the unintended, and the infimum
  gives the benefit of the doubt.

**Notes.** Under a nearness, indistinguishability is the closure for weak convergence; with none, for setwise
convergence, the topology in which large deviations of empirical behaviours are stated on general spaces [[References|@dembo1998]].

**Lineage.** [[D3 — Specification, declaration and misalignment|D3]]. v7.10: R7-5, case 5: "A controller 1 mm off target scores ∞, the same as one 50 m off — and so does
one exactly on target", with "measure outcomes (with environment noise), or declare a resolution" as the remedy, and a
distance rejected as a new primitive. Here the on-target case is settled by a declared nearness, and the other two by
those remedies.

## 4. Resolution: what each side distinguishes

### GD4 — Resolution
**Statement.** A **statistic** is a measurable map `g` from `X` to a standard Borel space. The **resolution** it
generates, `σ(g)`, is the set of events `{x : g(x) ∈ B}`, for the events `B` of the space of its values; its cells are
the sets on which `g` is constant. For a behaviour `q` and an `F` with `E_q[|F|] < ∞`, the **cell average**
`E_q[F|σ(g)]` is the conditional expectation: a function of `g`, fixed up to an event of probability zero under `q`.
Resolutions are used in two positions, and in a third in GD11.
- A specification is **stated at resolution** `σ(g)` if `𝓘_0` holds exactly the behaviours in `Δ_q` under which `g` has
  a distribution in a declared set.
- A behaviour `p`, absolutely continuous with respect to `q`, is **limited to** `σ(g)` if its ratio `dp/dq` is a
  function of `g`. An actor **has resolution** `σ(g)` if every behaviour it can produce is limited to it.

When nothing is declared or known, the statistic is the identity, in both positions: the finest resolution.

**In plain terms.** A resolution is what a report records about an outcome: a measurement, a score, a list of yes-or-no
answers, possibly endless, like the digits of a number. Its cells are the outcomes the report cannot tell apart. As in
the core, a principal may be indifferent inside cells, and an actor may be unable to tell their outcomes apart; then,
inside each cell, the default decides.

**Why this choice.**
- *Reduction.* On a finite set the cells of a statistic form a partition, every partition is the cells of a statistic,
  and "the ratio to the default is a function of `g`" is [[D4 — Resolution|D4]]'s `p(·|A) = q(·|A)` on the cells with `p(A) > 0`.
- *Why σ-algebras.* On a continuum, cells usually have probability zero: the patients with a risk score of exactly
  `0.31`. Conditioning on a cell of probability zero means something only relative to the whole statistic: the same set
  can be a cell of two statistics and get two different conditional behaviours (the Borel–Kolmogorov paradox). So a
  resolution is the whole family of events that a statistic settles, a σ-algebra, never a list of cells; and "inside a
  cell, the default decides" becomes "the ratio to the default is a function of the statistic".
- *Why generated by a statistic.* These σ-algebras are exactly those generated by countably many events: what someone
  could record by answering countably many yes-or-no questions. Others mislead. The events that are countable, or whose
  complement is, form a σ-algebra whose cells are single outcomes; yet under a default that gives every single outcome
  probability zero it settles nothing, and every cell average over it is the overall average.
- *Measurability is all or nothing.* A one-to-one statistic on a standard Borel space generates every event (the
  Lusin–Souslin theorem [[References|@kechris1995]]), so a resolution is coarser than the finest only if its statistic merges
  outcomes: a pass-or-fail target, a risk model that reads a few variables, a reward that scores two responses alike.
  And a statistic that does merge outcomes makes almost no function a function of it. v7.10 withdrew a condition stated
  as non-measurability because it held generically (v7.10: row 4, "vacuous — generically satisfied"). The framework uses
  graded quantities instead, such as what an actor loses by pursuing a cell average ([[P8 — An actor that cannot tell outcomes apart|P8]]).
- *Invariance; finite determination.* Events only; a cell average is the limit of the core's cell averages over finer
  descriptions of the values of `g`.
- *Noisy perception is not a resolution.* An actor that perceives outcomes through noise is described by a kernel, as
  views are (GD8); a resolution is the case without noise.

**Notes.** Every function that is a function of `g` in the sense of measurability is `h∘g` for a measurable `h` (the
Doob–Dynkin lemma).

**Lineage.** [[D4 — Resolution|D4]]. On finite outcomes a partition sufficed; σ-algebras are needed exactly when cells have probability
zero, and only for statistics that merge outcomes.

## 5. Stakes

### GD5 — Stakes
**Statement.** Under the standard specification of an objective `F`, let `p̂ ∈ Δ` with `E_{p̂}[|F|] < ∞`. The
**frontier** of `F` is `Φ_F(B) = sup{E_p[F] : p ∈ Δ, KL(p‖q) ≤ B}` for `B ≥ 0`, over the behaviours whose average of `F`
exists, and may be `+∞`. The **shortfall** of `p̂` is `S(p̂) = Φ_F(KL(p̂‖q)) − E_{p̂}[F]`, in the units of `F`. The
matched intensity and the matched pursuit are [[D5 — Stakes|D5]]'s, when a pursuit of departure `KL(p̂‖q)` exists.

**In plain terms.** As in the core: how much more of the objective the same departure from the default could have
bought. New: past the end of pursuit, more departure still buys more of the objective, but only by betting more on ever
rarer extremes, and no behaviour buys the most.

**Why this choice.**
- *Reduction.* On a finite set the matched pursuit has the largest average of `F` at its departure ([[P9 — What is at stake|P9]](i)), and beyond
  the departure of `q(·|A)` the frontier is `max F`: the shortfall is [[D5 — Stakes|D5]]'s.
- *Invariance; finite determination.* The frontier is a supremum of averages under a bound on a divergence, both of
  which finite descriptions approximate.
- *The frontier, not the matched pursuit.* [[D5 — Stakes|D5]] compares the actor with the pursuit of equal departure, which exists on
  finite outcomes. With a tail, the ray can stop at a finite departure. In `general/transfer.md`'s example the ray stops
  at intensity `1`, with departure `0.483` and average `1`; half a nat more departure buys `0.39`, `0.47`, `0.494` and
  `0.499` of `F` as the extra probability is placed near `10`, `100`, `1000` and `10000`, approaching `0.5`, the extra
  departure divided by the last intensity, without reaching it. The frontier always exists; the matched pursuit may not.
- *An actor that left the default entirely,* with infinite departure, is compared with the best that any departure can
  buy.

**Lineage.** [[D5 — Stakes|D5]]; [[P9 — What is at stake|P9]]; [[P27 — The best use of a departure budget|P27]] (the best use of a departure budget).

## 6. Interventions

### GD6 — Intervention and pass-through
**Statement.** An **intervention** is a known measurable `u : X → ℝ`. With `p` the actor's behaviour before it and `p'`
after, the actor passes it through, with **pass-through** `φ`, if `E_p[e^{φ·u}] < ∞` and `p' = tilt(p, φ·u)`. The
intervention is non-constant: no event of probability one under `p` makes it constant.

**In plain terms.** As in the core: a known nudge, followed by a reweighting. New: a reweighting never makes possible
what was impossible, or impossible what was possible. So a nudge that is passed through cannot create a pile of choices
at an exact value that nobody chose before.

**Why this choice.**
- *Reduction; invariance; finite determination.* As [[D6 — Intervention and pass-through|D6]], with the condition under which the tilt exists.
- *A tilt keeps the events of probability zero.* `tilt(p, φ·u)` is equivalent to `p`. So a change that creates an atom,
  an exact value now chosen with positive probability where before it had probability zero, is not the pass-through of
  any intervention, whatever `u`: the divergence between before and after is infinite. Economists measure such atoms as
  bunching [[References|@kleven2016]]; `general/disciplines.md` reads the behavioural-economics ontology with them.

**Lineage.** [[D6 — Intervention and pass-through|D6]].

## 7. Feasibility

### GD7 — Feasibility and precision
**Statement.** The actor's **feasible set** `𝓕 ⊆ Δ` is non-empty and contains every behaviour indistinguishable from it,
as in GD3, under no nearness or under one known of the actor. It is **linear** if
`𝓕 = {p ∈ Δ : E_p[f] = a_f for every f ∈ 𝓛}` for a family `𝓛` of bounded measurable functions and numbers `a_f`. The
actor has **precision** `k` if its outcome is its choice blurred by noise it does not control: `k` is a kernel from a
standard Borel space of choices to `X`, and every feasible behaviour is `∫ k(a, ·) π(da)` for a behaviour `π` on
choices. When nothing is known, `𝓕 = Δ`.

**In plain terms.** As in the core: the feasible set is what the actor can do, and it is linear when the actor's limits
say "these averages cannot change". New: limited precision is a limit too. What the actor produces is its choice blurred
by noise it does not control, so it can never pin an exact value that the default never produces.

**Why this choice.**
- *Reduction.* On a finite set: closure in `Δ`, finitely many functions, and precision adds nothing that a feasible set
  cannot already say: [[D7 — Feasibility|D7]].
- *Invariance; finite determination.* Averages of bounded functions, and limits that finite descriptions see.
- *Linear limits on general spaces.* Csiszár's Pythagorean theorem for linear sets was proved on general spaces
  [[References|@csiszar1975]], so the exact split of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] is expected to carry. On a continuum, an actor's resolution (GD4) is a
  linear limit given by infinitely many functions: the ratio to the default must be a function of the statistic.
- *Precision is the actor's own nearness.* Which limits the actor can reach is a fact about the actor, not a choice of
  the framework, so it enters as the actor's feasible set. Noise is the remedy v7.10 named for deterministic control
  ("measure outcomes, with environment noise"); here it is a property of the actor, stated once. If every `k(a, ·)` is
  absolutely continuous with respect to the default, so is every feasible behaviour, and the actor is never infinitely
  misaligned merely for pinning values.

**Lineage.** [[D7 — Feasibility|D7]]. v7.10: R7-5, case 5 (the remedy by noise).

## 8. Conditions, views and identification

### GD8 — Conditions, responses and views
**Statement.** The **conditions** form a standard Borel space `𝒞`. The actor's **response** is a kernel `c ↦ p_c`: a
behaviour in each condition, measurable in `c`. A **view** is a standard Borel space `Z` of signals with a kernel
`c ↦ V_c` of behaviours on `Z`. The response **depends on the condition only through the view** if there is a kernel
`z ↦ π_z` from `Z` to `X` with `p_c = ∫ π_z V_c(dz)` for every condition `c`. When nothing is known about the actor's
perception, the view is exact: `Z = 𝒞`, and `V_c` puts all its probability on `c`.

**In plain terms.** As in the core. New: situations may form a continuum, such as a patient's age or the estimated
difficulty of a prompt.

**Why this choice.**
- *Reduction.* On finite sets, kernels are tables of behaviours, and the integral is [[D8 — Conditions, responses and views|D8]]'s sum.
- *Invariance; finite determination.* Kernels are defined from events.
- *Regularity across situations comes from the view.* By data processing, `KL(p_c‖p_c') ≤ KL(V_c‖V_c')` when the
  response depends on the condition only through the view ([[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], expected to carry). So the response can change across
  a continuum of situations no faster than the view does. Generalizing from observed situations to nearby unobserved
  ones needs some such regularity; here it follows from the view, and is not assumed of the response.

**Lineage.** [[D8 — Conditions, responses and views|D8]]; `NOTES.md` §3.3, E5 and E7.

### GD9 — Observation and identification
**Statement.** The principal observes the response on an event `O ⊆ 𝒞` of **observed conditions**, which occur with a
declared frequency `ρ`, a behaviour on `𝒞` with `ρ(O) > 0`. What is observed is the behaviour `ρ(dc)·p_c(dx)` on
condition–outcome pairs with `c ∈ O`. Identification and identified sets are [[D9 — Observation and identification|D9]]'s, with "agrees with the observed
behaviours" read on those pairs.

**In plain terms.** As in the core. New: when situations form a continuum, each one occurs at most once: no patient
arrives twice. What is observed is how outcomes go with situations across many of them; the behaviour in one particular
situation is never observed, and is known only through assumptions, such as a view.

**Why this choice.**
- *Reduction.* With finitely many conditions, each of positive frequency, the behaviour on pairs fixes every observed
  `p_c`: this is [[D9 — Observation and identification|D9]].
- *Invariance; finite determination.* Pairs are outcomes of a standard Borel space.
- *When every condition has frequency zero, a single condition is never observed.* The behaviour on pairs fixes `p_c`
  only for `ρ`-almost every `c`: changing the response on a set of conditions of frequency zero changes nothing
  observed. A report about one condition is therefore always an identified set, narrowed only by assumptions; the view
  (GD8) is the assumption the framework already has.

**Lineage.** [[D9 — Observation and identification|D9]].

## 9. The evaluator

### GD10 — Evaluator, regression and residual
**Statement.** Let `F` be the target, with `E_q[|F|] < ∞`. An **evaluator** is a measurable `F̂ : X → ℝ`: known, or
revealed from an actual behaviour `p̂ ∈ Δ_q` as `F̂ = log(dp̂/dq)`, which fixes it up to a positive factor, an added
constant, and an event of probability zero. The **regression** of the target on the evaluator is `m = E_q[F|σ(F̂)]`, a
function of `F̂` (GD4), and the **residual** is `R = F − m`.

**In plain terms.** As in the core. On a continuum the regression is a curve: the average of the principal's objective
at each value of the evaluator, under the default.

**Why this choice.**
- *Reduction.* The cell average over the level sets of `F̂` is [[D10 — Evaluator, regression and residual|D10]]'s regression.
- *Invariance; finite determination.* As in GD4.
- *A continuum does not make the regression informative; merging does.* As in the core, an evaluator that gives distinct
  outcomes distinct values has `m = F` and `R = 0`, on any outcome space (GD4). It is informative when it reads less
  than the outcome holds: a reward model scoring a long response, a risk model reading a few recorded variables, a test
  passed or failed.
- *One-dimensional by construction.* The regression is a function on the real line, whatever the outcomes are. So the
  evaluator's scores, one number per outcome, are its natural record, and their empirical distribution function (GD11)
  carries best-of-`n`, the ordinal specification and their error bands (`general/transfer.md`).

**Lineage.** [[D10 — Evaluator, regression and residual|D10]]. Corrects `NOTES.md` §3.3, E8, which expected continuous outcomes to make the regression informative
without bins.

## 10. Samples and evidence

### GD11 — Sample, record and evidence
**Statement.** A **sample** of size `n` from `p` is a sequence `x_1, …, x_n` of outcomes drawn independently from `p`;
its **empirical behaviour** `p̂_n` gives probability `1/n` to each draw. A **record** of the sample at a **resolution**
`𝒫`, a partition of `X` into finitely or countably many events declared as GA5 requires, gives the count `N_𝒫(C)` of
draws in each cell `C`. For a real statistic `g`, the sample's **empirical distribution function** is
`y ↦ #{i : g(x_i) ≤ y}/n`. For equivalent behaviours `r` and `r'`, the **evidence** that the sample gives for `r`
against `r'` is `Σ_i log((dr/dr')(x_i))`, in nats.

**In plain terms.** As in the core. New: on a continuum no two decisions give exactly the same outcome, so a record
counts cells: minutes on a clock, bins of a score. How finely the record is kept is declared before looking, because the
misalignment a record shows can only grow as its cells are refined.

**Why this choice.**
- *Reduction.* The core records each outcome: the record at the finest resolution, which is finite there.
- *Invariance.* Cells are events. The evidence does not depend on which version of the ratio is used, except on an event
  of probability zero.
- *Finite determination.* A record is a finite description of the sample.
- *When the default gives every single outcome probability zero, the empirical behaviour is singular.* It puts all its
  probability on finitely many outcomes, each of probability zero under every behaviour equivalent to the default, so
  its divergence from every intended behaviour is infinite. Misalignment is never estimated by plugging it in, as [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]
  does on finite outcomes. It is estimated at a record's resolution, where [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] applies to the cells, and the value is
  a lower bound ([[P4 — What KL measures|P4]](iv)) that rises toward the misalignment as the record is refined (GA6).
- *A record shows "at least", not "at most"* (expected, `general/transfer.md`). When the default gives every single
  outcome probability zero, for every `n`, some behaviour within total variation `1/(100·n)` of an intended one, so that
  no test on `n` decisions tells them apart with a difference in rejection probability above `0.01`, has a misalignment
  as large as one likes: move a little probability to where the objective is low and the default rarely goes. So a
  report that misalignment is small rests on a declared resolution, or on a model of the behaviour, never on samples
  alone. What records can show without a model is the rate: the misalignment of finer and finer records grows like
  `(D − d)·log(1/w)` (GD3), so its slope against the logarithm of the resolution estimates the dimension deficit
  `D − d`, within the resolutions that the sample size supports: on a line, the share of the behaviour piled on single
  values, when the rest is spread.
- *Evidence, and Sanov.* The expected evidence per decision is the divergence, as [[P21 — The expected evidence is misalignment|P21]] states. Misalignment has a
  further meaning: the probability that the most favourable intended behaviour produces a record that looks like the
  actual behaviour falls like `e^{−n·M(p̂)}`. On finite outcomes this is the method of types; on a continuum, Sanov's
  theorem, which GA6 makes the limit of the finite one [[References|@dembo1998]]. Two directions must not be confused: the
  probability that a misaligned actor's record looks intended falls at the rate `inf_{p ∈ 𝓘} KL(p‖p̂)`, not at `M(p̂)`.
- *Distribution functions are exact for one number per outcome.* For a one-dimensional statistic, such as an evaluator's
  score or a waiting time, the empirical distribution function is within `√(log(2/α)/(2n))` of the true one everywhere,
  with probability at least `1 − α`, at every `n` and for every behaviour (the Dvoretzky–Kiefer–Wolfowitz inequality,
  with Massart's constant [[References|@massart1990]]). This is where distribution functions, rather than counts in cells, are the
  right record.

**Lineage.** [[D11 — Sample and evidence|D11]]; [[P21 — The expected evidence is misalignment|P21]]–[[P23 — The estimated misalignment of an actor that pursues the objective|P23]].

## 11. What the framework fixes, and what the parties declare

| Object | Fixed by the framework | Declared or known |
|---|---|---|
| the events | the outcome space's (GA1) | — |
| divergence, tilt, cell averages, the Fisher geometry | forced by the three tests | — |
| how behaviours approach one another | through finite descriptions only (GA6) | — |
| the default | — | by the principal: a behaviour (GD2) |
| which outcomes are near | — | by the principal, for its intended behaviours (GD3); of the actor, for what it can produce (GD7); none when nothing is said |
| resolutions | — | by the principal (indifference); of the actor (its limits); by whoever keeps a record (GD4, GD11); the finest when nothing is said |
| bins and grids | — | a record's resolution or a nearness, before the data (GA5) |

## 12. Open decisions

1. GA6 as a sixth premise. It is the one premise this file adds; everything else extends the core's.
2. No nearness when nothing is declared, so that nothing is forgiven that a finite description could see, as the finest
   resolution is the core's default in [[D4 — Resolution|D4]]. The alternative, the usual topology of each outcome space, would put a
   choice in the framework that the events do not make.
3. Names and versions. This file is draft 3, with items GA and GD; `CORE.md` (v11) is unchanged by it. The general
   results stay in `general/` until they are proved and checked; then they become items of a derived folder of their
   own, as the finite results are in `derived/`.
4. Two additions to the finite core, where checks are exact: the Sanov reading of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] and of misalignment, with the
   direction trap of GD11; and a record's resolution as a field of `STANDARD.md`.
5. Whether `general/disciplines.md` moves into the ontologies, which needs lint R10 to allow a section for outcomes that
   are not finite.
6. Whether the derived spaces of `general/derived-spaces.md` become definitions of this file: a derived space, with its
   default and its specification.
7. Whether `probes/` stays a folder of exploratory scripts, and whether CI should at least run them.
