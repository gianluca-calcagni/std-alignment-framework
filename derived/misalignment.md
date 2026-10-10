# Derived — misalignment

When misalignment ([D3]) is attained and when it is zero, its closed forms for "pursue `F`" ([P5]), and the split of the
departure from the default into pursuit and misalignment ([P6]). Then two other ways of declaring the intended
behaviours: a floor or a cap on the intensity of pursuit ([P35]), and an objective known only by the order of its values
([P36]).

### P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits
**Statement.** Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ`.
(i) If `p̂ ∈ Δ°`, the infimum in `M(p̂)` is attained: some `p ∈ 𝓘` has `KL(p̂‖p) = M(p̂)`.
(ii) `M(p̂) = 0` if and only if `p̂` is in the closure of `𝓘` in `Δ`. For `p̂ ∈ Δ°`, this means `p̂ ∈ 𝓘`.
(iii) If `q ∈ 𝓘`, then `M(p̂) ≤ KL(p̂‖q)`.
(iv) Let `F` be non-constant, and `A` the set of outcomes where `F` is largest. The pursuit ray `R_F` is closed in `Δ°`,
so `(q, R_F)` is a specification. Under it, with `p°` the **nearest intended behaviour** (or its limit), and `t*` the
intensity of `p°`, the **revealed intensity**:
- if `E_{p̂}[F] ≤ E_q[F]`, then `t* = 0`, `p° = q` and `M(p̂) = KL(p̂‖q)`;
- if `E_q[F] < E_{p̂}[F] < max F`, then `t* > 0` is the unique intensity with `E_{p_{F,t*}}[F] = E_{p̂}[F]`,
  `p° = p_{F,t*}` and `M(p̂) = KL(p̂‖p°)`;
- if `E_{p̂}[F] = max F`, that is, `p̂` puts all its mass on `A`, then `t* = ∞`, `p° = q(·|A)` and
  `M(p̂) = KL(p̂‖q(·|A))`, approached as `t → ∞` and not attained. It is `0` exactly when `p̂ = q(·|A)`.

**In plain terms.** For a full-support behaviour there is always a nearest acceptable behaviour. Misalignment is zero
only for acceptable behaviours and their limits. When the default is acceptable, misalignment is never more than the
actual behaviour's departure from the default. For "pursue `F`": a behaviour that does no better than the default is
charged its whole departure from it; one that does better is compared with the pursuit that reaches the same average of
`F`, whose intensity is the one the behaviour reveals; and one that only ever picks the best outcomes is aligned exactly
when it splits its choices among tied best outcomes as the default would. In particular, a maximizer with a single best
outcome is aligned.

**Proof.** (i) Pick `p₀ ∈ 𝓘` and let `c = KL(p̂‖p₀)` and `H(p̂) = −Σ_x p̂(x)·log p̂(x)`. For any `p ∈ Δ°`,
`KL(p̂‖p) = −H(p̂) − Σ_y p̂(y)·log p(y)`, and every term `−p̂(y)·log p(y)` is non-negative. So `KL(p̂‖p) ≤ c` implies
`p(x) ≥ exp(−(c + H(p̂))/p̂(x)) > 0` for every `x`, since `p̂(x) > 0`. The set `K = {p ∈ Δ : KL(p̂‖p) ≤ c}` is closed in
`Δ`, because `KL(p̂‖·)` is lower semicontinuous on `Δ` (with value `+∞` where some `p(x) = 0`). So `K` is compact, and
by the bound it lies in `Δ°`. Since `𝓘` is closed in `Δ°`, the set `𝓘 ∩ K` is closed in `K`, hence compact, and it
contains `p₀`. The continuous function `KL(p̂‖·)` attains its minimum on `𝓘 ∩ K`, and that minimum is `M(p̂)`, because
every point of `𝓘` outside `K` has `KL(p̂‖p) > c`.
(ii) If `M(p̂) = 0`, there are `p_k ∈ 𝓘` with `KL(p̂‖p_k) → 0`, and by Pinsker's inequality
`Σ_x |p̂(x) − p_k(x)| ≤ (2·KL(p̂‖p_k))^{1/2} → 0`, so `p̂` is in the closure of `𝓘`. Conversely, if `p_k ∈ 𝓘` and
`p_k → p̂`, then `KL(p̂‖p_k) = Σ_{p̂(x) > 0} p̂(x)·log(p̂(x)/p_k(x)) → 0`, because `p_k(x) → p̂(x) > 0` on every term.
For `p̂ ∈ Δ°`, the closure of `𝓘` in `Δ` meets `Δ°` exactly in `𝓘`, because `𝓘` is closed in `Δ°`.
(iii) `q` is one of the candidates in the infimum.
(iv) *Closed.* Let `x₋` and `x₊` be outcomes where `F` is smallest and largest, and `osc F = F(x₊) − F(x₋) > 0`. Then
`p_{F,t}(x₋) = q(x₋)·e^{t·F(x₋)} / E_q[e^{tF}] ≤ (q(x₋)/q(x₊))·e^{−t·osc F}`. If `p_{F,t_k} → p ∈ Δ°`, then
`p(x₋) > 0`, so the `t_k` are bounded. A subsequence converges to some `t ≥ 0`, and by continuity `p = p_{F,t} ∈ R_F`.
*Minimum.* Let `g(t) = KL(p̂‖p_{F,t}) = KL(p̂‖q) − t·E_{p̂}[F] + log E_q[e^{tF}]`, finite for every `t ≥ 0`. Then
`g'(t) = E_{p_{F,t}}[F] − E_{p̂}[F]` and `g''(t) = Var_{p_{F,t}}(F) > 0`, because `F` is non-constant and `p_{F,t}` has
full support; so `g` is strictly convex. As `t → ∞`, `E_{p_{F,t}}[F]` increases continuously toward `max F`. If
`E_{p̂}[F] ≤ E_q[F]`, then `g'(0) ≥ 0`, and the minimum over `t ≥ 0` is at `0`. If `E_q[F] < E_{p̂}[F] < max F`, then
`g'` has a unique root `t* > 0`, where `g` is minimal. If `E_{p̂}[F] = max F`, then `g' < 0` everywhere, so `g`
decreases toward its limit, which is not attained: with `m = max F`,
`g(t) = KL(p̂‖q) − t·m + log E_q[e^{tF}] = KL(p̂‖q) + log E_q[e^{t(F − m)}] → KL(p̂‖q) + log q(A) = KL(p̂‖q(·|A))`,
using that `p̂` puts all its mass on `A`. That limit is `0` exactly when `p̂ = q(·|A)`.

**Checks.** checks/test_misalignment.py::test_minimum_on_the_ray_is_attained_at_the_closed_form,
checks/test_misalignment.py::test_best_outcomes_case,
checks/test_misalignment.py::test_zero_exactly_on_the_intended_set,
checks/test_misalignment.py::test_bounded_by_departure_from_default,
checks/test_misalignment.py::test_the_ray_leaves_every_compact_set, checks/test_misalignment.py::test_deviance_identity

**Notes.** The checks exercise the standard specification; parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. Pinsker's inequality is standard [@cover2006], and is read in the open draft of [@polyanskiy2025], Theorem 7.10,
whose total variation is half the sum in the proof. The revealed intensity is the weight that maximum-entropy inverse
reinforcement learning, in its one-step form, fits for the single feature `F` [@ziebart2008], restricted to `t ≥ 0`: in
the first case the unrestricted fit is zero or negative, and in the third it is infinite. For `n` independent decisions
with observed frequencies `p̂`, the log-likelihood ratio of an unrestricted model against the best pursuit of `F` is
`n·M(p̂)`, so `2n·M(p̂)` is the deviance of the model "the actor pursues `F` from the default" (checked in the second
and first cases). In the third case, a maximizer that breaks ties among the best outcomes differently from the default
is charged; a principal who is indifferent among tied outcomes says so with a resolution ([D4]).

**Lineage.** v7.10: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for the first two cases of (iv) (the transverse
error `D_⊥`, attained at `t̂⁺`). New: behaviours that rule outcomes out, including the deterministic maximizer (the
third case), and the name "revealed intensity".

### P6 — The departure from the default splits into pursuit and misalignment
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ` and let `p°` be as in [P5](iv). The
**departure** of `p̂` from the default is `KL(p̂‖q)`, and `KL(p̂‖q) = KL(p°‖q) + M(p̂)`. So `0 ≤ M(p̂) ≤ KL(p̂‖q)`, and
`M(p̂) = KL(p̂‖q)` when `E_{p̂}[F] ≤ E_q[F]`.

**In plain terms.** How far the actor moved away from the default splits exactly into two parts: the movement explained
by pursuing the objective, and the misalignment. An actor that does no better than the default has all of its movement
counted as misalignment.

**Proof.** In the first case of [P5](iv), `p° = q` and `KL(q‖q) = 0`. In the second,
`log(p°/q) = t*·F − log E_q[e^{t*F}]`, so `KL(p̂‖q) − KL(p̂‖p°) = E_{p̂}[log(p°/q)] = t*·E_{p̂}[F] − log E_q[e^{t*F}]`.
Since `E_{p̂}[F] = E_{p°}[F]`, this equals `t*·E_{p°}[F] − log E_q[e^{t*F}] = E_{p°}[log(p°/q)] = KL(p°‖q)`. In the
third, `p̂` and `q(·|A)` put all their mass on `A`, so `KL(p̂‖q) − KL(p̂‖q(·|A)) = −log q(A) = KL(q(·|A)‖q)`. The bounds
follow because KL is non-negative, and the last claim is the first case.

**Checks.** checks/test_misalignment.py::test_departure_splits_into_pursuit_and_misalignment

**Notes.** The identity is a Pythagorean relation for KL along the pursuit ray. In RL fine-tuning the departure is the
KL from the reference policy, often treated as a budget; the identity splits that budget into the part spent on the
objective and the misaligned part. Whenever the actor departs from the default, `M(p̂)/KL(p̂‖q)` is the misaligned share
of its departure, between 0 and 1.

**Lineage.** v7.10: Thm 13 (the intent-ray decomposition) and NOTES §2.5 (the intent ray). New: the third case, and the
reading as a split of the departure.

### P35 — Floors and caps
**Statement.** Let `F` be non-constant and `0 ≤ r ≤ s ≤ ∞`. The **intended segment** between a **floor** `r` and a
**cap** `s` is `𝓘_{r,s} = {p_{F,t} : r ≤ t ≤ s, t < ∞}`. It is closed in `Δ°`, so `(q, 𝓘_{r,s})` is a specification
([D3]); `r = 0` and `s = ∞` give the standard specification. For `p̂ ∈ Δ°`, let `t̂ ∈ ℝ` be the intensity with
`E_{p_{F,t̂}}[F] = E_{p̂}[F]`, and `t° = min(max(t̂, r), s)`.
(i) The misalignment under the segment is `KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t°})`: the departure from the whole line
of pursuit, plus an undershoot when `t̂ < r` and an overshoot when `t̂ > s`.
(ii) **A floor is a minimum standard.** For `t ≥ 0`, `t ≥ r` exactly when `E_{p_{F,t}}[F] ≥ E_{p_{F,r}}[F]`: a floor
declares a minimum average of `F`, in its units, and a cap a maximum.
(iii) For `F = −1_H` and `0 < ε < q(H)`, the floor at which `p_{F,r}(H) = ε` is
`r = log(q(H)·(1 − ε)/(ε·(1 − q(H)))) > 0`, and under it the default itself is misaligned, by `KL(q‖p_{F,r}) > 0`;
under the standard specification its misalignment is `0`.
(iv) For `p_T ∈ Δ°` and `F = log(p_T/q)`, the behaviour with the largest `−KL(p‖p_T) − KL(p‖q)/t` is `p_{F, t/(1+t)}`:
as `t` grows from `0` to `∞`, imitating `p_T` with a KL penalty runs along the segment `𝓘_{0,1}`, from `q` toward
`p_T`.

**In plain terms.** A principal can declare a minimum and a maximum strength of pursuit: "at least this much of the
objective, but no more than that". Misalignment is then the distance from the whole line of pursuit, plus how far the
actor falls short of the minimum or overshoots the maximum along it. A minimum strength is the same as a minimum
average of the objective. Under a minimum, doing nothing can be a failure: a principal who wants a fine to cut lateness
to a given rate charges an actor that keeps the default. Imitating a target behaviour with a penalty for departing
moves along such a segment, with the target as its end.

**Proof.** With `Λ(t) = log E_q[e^{t·F}]`, `E_{p_{F,t}}[F] = Λ'(t)` and its derivative is `Var_{p_{F,t}}(F) > 0`, so
the average of `F` increases strictly along the line of pursuit, and `t̂` exists because `min F < E_{p̂}[F] < max F`.
For `s < ∞` the segment is the image of `[r, s]` under a continuous map, hence compact; for `s = ∞` it is the part of
the pursuit ray where the average of `F` is at least `Λ'(r)`, a closed part of a set closed in `Δ°` ([P5](iv)).
(i) For every `t ∈ ℝ`,
`KL(p̂‖p_{F,t}) − KL(p̂‖p_{F,t̂}) = E_{p̂}[log(p_{F,t̂}/p_{F,t})] = (t̂ − t)·E_{p̂}[F] − Λ(t̂) + Λ(t)`, and the same
expression with `p_{F,t̂}` in place of `p̂` is `KL(p_{F,t̂}‖p_{F,t})`, since the two have the same average of `F`. So
`KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t})`. The second term is convex in `t`, as `Λ` is, and zero at
`t̂`, so over `[r, s]` it is smallest at the point nearest `t̂`, which is `t°`. (ii) follows from the strict increase of
the average. (iii) `p_{F,t}(H) = q(H)·e^{−t}/(q(H)·e^{−t} + 1 − q(H))` decreases continuously from `q(H)` toward `0`;
solving for `ε` gives `r`. The default `q = p_{F,0}` has `t̂ = 0 < r`, so by (i) its misalignment is
`KL(q‖p_{F,r}) > 0`; under the standard specification `q` is intended. (iv) The objective is strictly concave, and its
stationarity condition, `−log(p/p_T) − log(p/q)/t = constant`, gives `log p = log q + (t/(1 + t))·F + constant`.

**Checks.** checks/test_misalignment.py::test_floors_and_caps

**Notes.** (iii) answers the principal for whom doing nothing is a failure ([D3], Why). The archive also defined budget
versions of these measures; in the core, the comparison at the same departure is the stakes of [D5].

**Lineage.** v7.10: Defs 18 and 20 (caps; floors and the intended segment), Props 33 (a), (b), (d) and 35 (a), (c), and
Prop 37 (d) (a floor is a minimum standard); R7-6a and R7-6b. Their parts about the contract are dropped (`IMPORT.md`).

### P36 — Ordinal objectives
**Statement.** Let `F` be non-constant, with values `v_1 < … < v_m` on the level sets `L_1, …, L_m`. The **ordinal
specification** of `F` is `(q, C_F)`, with `C_F = {p ∈ Δ° : p/q is a non-decreasing function of F}`. For `p̂ ∈ Δ°`, let
`r°` be the isotonic regression of the level ratios `p̂(L_j)/q(L_j)` with weights `q(L_j)`: the non-decreasing sequence
nearest to them in weighted least squares [@robertson1988], read as a function of `F` on `X`. Its pooled blocks
`B_1, …, B_k` are the unions of consecutive level sets on which it is constant. Let `p° = q·r°`.
(i) `C_F` is the closure in `Δ°` of the union of the pursuit rays of `φ∘F` over the increasing functions `φ`, and it
contains best-of-`n` by `F` for every `n ≥ 1`; it is closed in `Δ°`, so `(q, C_F)` is a specification ([D3]).
(ii) `p°` is the nearest intended behaviour, and the ordinal misalignment is
`M_ord(p̂) = KL(p̂‖p°) = Σ_i p̂(B_i)·KL(p̂(·|B_i)‖q(·|B_i))`.
(iii) For every `p ∈ C_F`, `KL(p̂‖p) ≥ KL(p̂‖p°) + KL(p°‖p)`, with equality at `p = q`:
`KL(p̂‖q) = M_ord(p̂) + KL(p°‖q)`.
(iv) Under the standard specification of `F`, `M(p̂) ≥ M_ord(p̂) + M(p°)`.
(v) `C_F`, `p°` and `M_ord` are unchanged when `F` is replaced by `φ∘F`, for every strictly increasing `φ`.

**In plain terms.** A principal who cares only about the order of outcomes accepts every behaviour that favours better
outcomes at least as much as worse ones, relative to the default. Its misalignment pools the outcomes whose order the
actor's behaviour contradicts, and charges only the actor's departure from the default inside those pools. Misalignment
against the objective's values is the ordinal misalignment plus a term for the shape. Best-of-`n` on the objective
itself is aligned with its order, though not with its values.

**Proof.** (i) For an increasing `φ`, `p_{φ∘F,t}/q = e^{t·φ(F)}/Z` is a non-decreasing function of `F`, so every such
ray lies in `C_F`, which is closed in `Δ°`, being defined by non-strict inequalities. Conversely, if `p ∈ C_F` has level
ratios increasing strictly, then `p = p_{φ∘F,1}` for an increasing `φ` with `φ(v_j)` the log of the `j`-th ratio;
otherwise `p` is a limit of such behaviours. Best-of-`n` by `F` has the level ratio `(A_j^n − A_{j−1}^n)/q(L_j)`, with
`A_j` the default's mass of `F ≤ v_j`, which is `n` times the average of `u^{n−1}` over `[A_{j−1}, A_j]`, non-decreasing
in `j`. (iii) Let `y = p̂/q`, a function on `X`, and `K` the convex cone of non-decreasing functions of `F`. `r°` is the
projection of `y` onto `K` in `L²(q)` [@robertson1988]; hence `E_q[(y − r°)·g] ≤ 0` for every `g ∈ K`, and
`E_q[(y − r°)·h] = 0` for every `h` constant on each pooled block, since `r°` is the `q`-average of `y` there. With
`h = 1`, `p°` sums to one, and `r° > 0`, so `p° ∈ C_F`. For `p = q·ρ ∈ C_F`,
`KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p) = E_q[(y − r°)·log(r°/ρ)]`; the part with `log r°` is `0`, since `log r°` is constant
on blocks, and the part with `−log ρ` is at least `0`, since `log ρ ∈ K`. At `p = q`, `log ρ = 0`. (ii) By (iii),
`KL(p̂‖p) > KL(p̂‖p°)` for every `p ≠ p°` in `C_F`. On a block `B`, `p°(B) = p̂(B)` and `p°(·|B) = q(·|B)`, so the chain
rule [P4](iii) gives the sum. (iv) Every point of the pursuit ray of `F` is in `C_F`; apply (iii) to each and take the
infimum. (v) `C_F` and the regression depend on `F` only through the ordered level sets.

**Checks.** checks/test_misalignment.py::test_ordinal_objectives

**Notes.** This is `NOTES.md` proposal E3. A coarse actor's best effort ([P8](ii)) and best-of-`n` are ordinally
aligned whenever their reweighting rises with `F`. The archive's check found, against its pre-registration, that the
gap between the ordinal and the budget measure is of second order in `M_ord`; the core does not use the budget measure.

**Lineage.** v7.10: Def 17 (target sets, the ordinal part) and Prop 32 (the ordinal measure), with Prop 31 (c); R7-7.
