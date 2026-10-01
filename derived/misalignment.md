# Derived — misalignment

When misalignment ([D3]) is attained and when it is zero, its closed forms for "pursue `F`" ([P5]), and the split of
the departure from the default into pursuit and misalignment ([P6]).

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
charged its whole departure from it; one that does better is compared with the pursuit that reaches the same average
of `F`, whose intensity is the one the behaviour reveals; and one that only ever picks the best outcomes is aligned
exactly when it splits its choices among tied best outcomes as the default would. In particular, a maximizer with a
single best outcome is aligned.

**Proof.** (i) Pick `p₀ ∈ 𝓘` and let `c = KL(p̂‖p₀)` and `H(p̂) = −Σ_x p̂(x)·log p̂(x)`. For any `p ∈ Δ°`,
`KL(p̂‖p) = −H(p̂) − Σ_y p̂(y)·log p(y)`, and every term `−p̂(y)·log p(y)` is non-negative. So `KL(p̂‖p) ≤ c` implies
`p(x) ≥ exp(−(c + H(p̂))/p̂(x)) > 0` for every `x`, since `p̂(x) > 0`. The set `K = {p ∈ Δ : KL(p̂‖p) ≤ c}` is closed in
`Δ`, because `KL(p̂‖·)` is lower semicontinuous on `Δ` (with value `+∞` where some `p(x) = 0`). So `K` is compact, and
by
the bound it lies in `Δ°`. Since `𝓘` is closed in `Δ°`, the set `𝓘 ∩ K` is closed in `K`, hence compact, and it contains
`p₀`. The continuous function `KL(p̂‖·)` attains its minimum on `𝓘 ∩ K`, and that minimum is `M(p̂)`, because every
point of `𝓘` outside `K` has `KL(p̂‖p) > c`.
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
using
that `p̂` puts all its mass on `A`. That limit is `0` exactly when `p̂ = q(·|A)`.

**Checks.** checks/test_misalignment.py::test_minimum_on_the_ray_is_attained_at_the_closed_form,
checks/test_misalignment.py::test_best_outcomes_case,
checks/test_misalignment.py::test_zero_exactly_on_the_intended_set,
checks/test_misalignment.py::test_bounded_by_departure_from_default,
checks/test_misalignment.py::test_the_ray_leaves_every_compact_set, checks/test_misalignment.py::test_deviance_identity

**Notes.** The checks exercise the standard specification; parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. Pinsker's inequality is standard [@cover2006]. The revealed intensity is the weight that maximum-entropy inverse
reinforcement learning, in its one-step form, fits for the single feature `F` [@ziebart2008], restricted to `t ≥ 0`:
in the first case the unrestricted fit is zero or negative, and in the third it is infinite. For `n` independent
decisions with observed frequencies `p̂`, the log-likelihood ratio of an unrestricted
model against the best pursuit of `F` is `n·M(p̂)`, so `2n·M(p̂)` is the deviance of the model "the actor pursues `F`
from the default" (checked in the second and first cases). In the third case, a maximizer that breaks ties among the
best outcomes differently from the default is charged; a principal who is indifferent among tied outcomes says so with
a resolution ([D4]).

**Lineage.** main: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for the first two cases of (iv) (the transverse
error
`D_⊥`, attained at `t̂⁺`). New: behaviours that rule outcomes out, including the deterministic maximizer (the third
case),
and the name "revealed intensity".

### P6 — The departure from the default splits into pursuit and misalignment
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ` and let `p°` be as in [P5](iv). The
**departure** of `p̂` from the default is `KL(p̂‖q)`, and
`KL(p̂‖q) = KL(p°‖q) + M(p̂)`.
So `0 ≤ M(p̂) ≤ KL(p̂‖q)`, and `M(p̂) = KL(p̂‖q)` when `E_{p̂}[F] ≤ E_q[F]`.

**In plain terms.** How far the actor moved away from the default splits exactly into two parts: the movement explained
by pursuing the objective, and the misalignment. An actor that does no better than the default has all of its movement
counted as misalignment.

**Proof.** In the first case of [P5](iv), `p° = q` and `KL(q‖q) = 0`. In the second,
`log(p°/q) = t*·F − log E_q[e^{t*F}]`,
so `KL(p̂‖q) − KL(p̂‖p°) = E_{p̂}[log(p°/q)] = t*·E_{p̂}[F] − log E_q[e^{t*F}]`. Since `E_{p̂}[F] = E_{p°}[F]`, this
equals
`t*·E_{p°}[F] − log E_q[e^{t*F}] = E_{p°}[log(p°/q)] = KL(p°‖q)`. In the third, `p̂` and `q(·|A)` put all their mass on
`A`, so `KL(p̂‖q) − KL(p̂‖q(·|A)) = −log q(A) = KL(q(·|A)‖q)`. The bounds follow because KL is non-negative, and the
last
claim is the first case.

**Checks.** checks/test_misalignment.py::test_departure_splits_into_pursuit_and_misalignment

**Notes.** The identity is a Pythagorean relation for KL along the pursuit ray. In RL fine-tuning the departure is the
KL from the reference policy, often treated as a budget; the identity splits that budget into the part spent on the
objective and the misaligned part. Whenever the actor departs from the default, `M(p̂)/KL(p̂‖q)` is the misaligned share
of its departure, between 0 and 1.

**Lineage.** main: Thm 13 (the intent-ray decomposition) and NOTES §2.5 (the intent ray). New: the third case, and the
reading as a split of the departure.
