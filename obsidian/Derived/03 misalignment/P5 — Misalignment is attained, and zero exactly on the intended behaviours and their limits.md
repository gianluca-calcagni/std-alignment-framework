---
kind: proposition
id: P5
aliases: ["P5"]
source: "derived/misalignment.md"
---
# P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p5--misalignment-is-attained-and-zero-exactly-on-the-intended-behaviours-and-their-limits). Edit the source, not this note.

## Statement
Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ`.
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

## In plain terms
For a full-support behaviour there is always a nearest acceptable behaviour. Misalignment is zero
only for acceptable behaviours and their limits. When the default is acceptable, misalignment is never more than the
actual behaviour's departure from the default. For "pursue `F`": a behaviour that does no better than the default is
charged its whole departure from it; one that does better is compared with the pursuit that reaches the same average of
`F`, whose intensity is the one the behaviour reveals; and one that only ever picks the best outcomes is aligned exactly
when it splits its choices among tied best outcomes as the default would. In particular, a maximizer with a single best
outcome is aligned.

## Proof
(i) Pick `p₀ ∈ 𝓘` and let `c = KL(p̂‖p₀)` and `H(p̂) = −Σ_x p̂(x)·log p̂(x)`. For any `p ∈ Δ°`,
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

## Notes
The checks exercise the standard specification; parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. Pinsker's inequality is standard [[References|@cover2006]]. The revealed intensity is the weight that maximum-entropy inverse
reinforcement learning, in its one-step form, fits for the single feature `F` [[References|@ziebart2008]], restricted to `t ≥ 0`: in
the first case the unrestricted fit is zero or negative, and in the third it is infinite. For `n` independent decisions
with observed frequencies `p̂`, the log-likelihood ratio of an unrestricted model against the best pursuit of `F` is
`n·M(p̂)`, so `2n·M(p̂)` is the deviance of the model "the actor pursues `F` from the default" (checked in the second
and first cases). In the third case, a maximizer that breaks ties among the best outcomes differently from the default
is charged; a principal who is indifferent among tied outcomes says so with a resolution ([[D4 — Resolution|D4]]).

## Lineage
v7.10: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for the first two cases of (iv) (the transverse
error `D_⊥`, attained at `t̂⁺`). New: behaviours that rule outcomes out, including the deterministic maximizer (the
third case), and the name "revealed intensity".

## Checks
- [`checks/test_misalignment.py::test_minimum_on_the_ray_is_attained_at_the_closed_form`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_misalignment.py::test_best_outcomes_case`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_misalignment.py::test_zero_exactly_on_the_intended_set`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_misalignment.py::test_bounded_by_departure_from_default`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_misalignment.py::test_the_ray_leaves_every_compact_set`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_misalignment.py::test_deviance_identity`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- nothing

## Used by
- [[D5 — Stakes|D5]] — Stakes
- [[P6 — The departure from the default splits into pursuit and misalignment|P6]] — The departure from the default splits into pursuit and misalignment
- [[P35 — Floors and caps|P35]] — Floors and caps
- [[P8 — An actor that cannot tell outcomes apart|P8]] — An actor that cannot tell outcomes apart
- [[P9 — What is at stake|P9]] — What is at stake
- [[P11 — The misaligned share at the start of a change|P11]] — The misaligned share at the start of a change
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not
- [[P21 — The expected evidence is misalignment|P21]] — The expected evidence is misalignment
- [[P22 — No test detects misalignment faster than misalignment|P22]] — No test detects misalignment faster than misalignment
- [[P52 — What a sample certifies about misalignment, by access|P52]] — What a sample certifies about misalignment, by access
- [[P43 — Misalignment at any intensity|P43]] — Misalignment at any intensity
- [[P44 — What named objectives explain|P44]] — What named objectives explain
- [[P48 — Misalignment when the target is uncertain|P48]] — Misalignment when the target is uncertain
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
- [[C4 — Rescaling the objective is not misalignment|C4]] — Rescaling the objective is not misalignment
