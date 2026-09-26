---
id: "R7-5 go-no-go"
type: "report"
updated: "2026-09-26"
---
# R7-5 — go/no-go: is there a real case where KL is the wrong tool?

**Decision: R7-5 is not pursued (v7.3.1).** No real case was found in which the measurement layer needs a
divergence other than KL and no other refactor step repairs it. The one real defect found is repaired by
target sets, which is R7-7, and it keeps KL.

## The question and the decision rule

The PI, after v7.3: proceed with R7-5 only if there is a real case where KL divergence is the wrong tool.
Otherwise it adds complexity for no practical reason.

## Where KL enters, and which of its roles are forced

| Role | Where | A choice? |
|---|---|---|
| detectability | Chernoff exponent `≤ min KL ≤ β·R_J` ([[Prop 18]]) | no. Error exponents of tests are KL/Chernoff by theorem (Stein, Chernoff) |
| the measure | `β·R_J = KL(p̂‖p*)` ([[Thm 1]]) | no, once the intent is entropic. For another convex regularizer `Ψ` the identity becomes the Bregman divergence `B_Ψ` ([[Prop 15]]) |
| the intended regularizer | the entropic intent, `p* ∝ q·e^{βF}` | **yes**. This is the only real choice |

So "replace KL by a general divergence" reduces to "allow intents that are not entropic". A real case must
show a measurement verdict that is wrong by common sense, and that no other step repairs: target sets
(R7-7), non-linear targets (R7-6), or measurable spaces with a declared resolution (R7-8).

## Candidates examined

| Case | Source | What goes wrong with KL | Where it belongs | Verdict |
|---|---|---|---|---|
| 1. Heavy-tailed evaluator error | [[src Kwa 2024]]; [[src Huang 2025]] | KL is too weak as the **trained actor's** regularizer: bounded KL, unbounded proxy gain | explanation layer; already [[Prop 10]]–[[Prop 11]] | the measurement is not fooled. It scores behaviour against `F`, not `F̂` |
| 2. Semantic blindness; mode collapse | [[src Na 2026]]; [[src Wang 2024]] | as a **regularizer**, KL ignores token geometry ("cat" vs "kitten" vs "table") and trades diversity for alignment | explanation layer (the actor's regularizer) | not a measurement case. In the measure, `F` carries the semantics. A swap between outcomes of equal `F` registers only through the declared `q`, and declaring `X` at the level of meanings removes it |
| 3. Best-of-n and quantilizers **run on the true target** | [[src Beirami 2024]]; [[src Taylor 2016]]; [[src Verdun 2025]] | the current measures score them as misaligned | target sets, ordinal target (R7-7) | **a real defect, and not a defect of KL** — below |
| 4. Mode dropping when the target is a distribution | generative modelling | `KL(p̂‖p*)` charges dropping modes only logarithmically: keeping 1 % of `p*`'s mass costs `log 100 ≈ 4.6` nats | under an entropic intent this is the exact utility loss ([[Thm 1]]). A principal who values coverage more has a target non-linear in `p` (R7-6) | not R7-5 |
| 5. Deterministic behaviour on a continuous `X` | continuous control | every f-divergence saturates. A controller 1 mm off target scores `∞`, the same as one 50 m off — and so does one exactly on target | measurable spaces (R7-8); a graded measure needs a metric on `X`, a new primitive, and loses [[Thm 1]] | **the only case where KL is genuinely wrong — and so is every f-divergence**. The cheap remedy keeps KL: measure outcomes (with environment noise), or declare a resolution |

## Case 3 in detail (exploratory probe, not pre-registered)

**Why the current measures call them misaligned.** Best-of-n on the true target has
`dp/dq = (Q(F)^n − Q(F⁻)^n)/q(level of F)`, an increasing function of `F`. So it is the tilt of an increasing
transform, `p_{φ∘F, 1}`. The measures of [[Def 10]] compare it with tilts of `F` itself, and `F` enters them
**cardinally**: [[Def 11]] M3 allows only positive affine maps. The same holds for quantilizers (a step
function of `F`) and for an evaluator that is any increasing transform of `F`.

**Numbers** (`r75_probe.py`, 400 random instances per case):

| Actor on the true target | `M_free` median [p5, p95] | `M_free / KL(p̂‖q)` median | `M_free > 10⁻⁶` in | max `M_ord` |
|---|---|---|---|---|
| best-of-4 | 0.079 [0.017, 0.197] | 0.13 | 100 % | `1.2·10⁻¹⁶` |
| best-of-16 | 0.107 [0.004, 0.459] | 0.06 | 99.5 % | `1.2·10⁻¹⁶` |
| best-of-64 | 0.035 [0.000, 0.572] | 0.01 | 92.5 % | `1.4·10⁻¹⁶` |
| quantilizer, top 10 % | 0.330 [0.006, 0.863] | 0.16 | 100 % | `2.1·10⁻¹⁶` |
| quantilizer, top 30 % | 0.392 [0.060, 0.639] | 0.35 | 100 % | `2.6·10⁻¹⁶` |

**The repair keeps KL.** Declare the target **ordinal**: the target set `{φ∘F : φ strictly increasing}`.
Its aligned set is the cone `C_F = {p : dp/dq is a non-decreasing function of F}`, which contains the ray.
The measure is

```
M_ord(p̂) = inf_{p ∈ C_F} KL(p̂‖p) = inf_{φ increasing, t ≥ 0} KL(p̂‖p_{φ∘F, t}),
```

and it has a closed form: `p° = q·r°`, with `r°` the `q`-weighted isotonic regression of `y = p̂/q` over the
levels of `F` (pool-adjacent-violators). A generic constrained optimizer agrees to `5·10⁻¹⁵` on 60 instances.
`M_ord` is 0 to `3·10⁻¹⁶` on every instance above and on every evaluator that is an increasing transform of
`F`. It is positive for 98.3 % of noisy evaluators `F + σ·noise` (`σ` between 0.1 and 1); the rest are noise draws that do not reorder anything that matters.

**A decomposition (proved here; checked on 1000 instances).** For every `p ∈ C_F`,

```
KL(p̂‖p) = KL(p̂‖p°) + KL(p°‖p) + ⟨r° − y, log(p/q)⟩_q,   the last term ≥ 0.
```

*Proof.* `C_F` corresponds to the convex cone `K` of non-decreasing functions of `F`, which contains the
constants of both signs. `r°` is the `L²(q)` projection of `y` onto `K`. So `⟨y − r°, g⟩_q ≤ 0` for every
`g ∈ K`, and `⟨y − r°, h(r°)⟩_q = 0` for every function `h`, because `r°` is constant on each pooled block
and equals the `q`-mean of `y` there. With `p = q·r`,
`KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p) = Σ q (y − r°) log(r°/r) = −⟨y − r°, log r⟩_q ≥ 0`, because `log r ∈ K`.
The same line with `p` feasible shows that `p°` is the minimizer. `⟨y − r°, 1⟩_q = 0` gives `Σ p° = 1`. ∎
This is order-restricted inference ([[src Barlow 1972]], [[src Robertson 1988]]) applied to the measure.

*Corollary.* Take `p = p_{F,t}` and minimize over `t`: `M_free(p̂) ≥ M_ord(p̂) + M_free(p°)`. The off-ray part
of the free measure splits into an **ordering error**, a **shape** term (how far the ordinal projection is
from the ray), and a non-negative cross term. Checked: the inequality holds in 1000 of 1000 instances (min
slack `−4·10⁻¹⁶`), with equality in 9.5 %.

**What the cardinal/ordinal declaration changes** (`r75_c5.py`; evaluators `F̂ = F + σ·noise`, 400 instances
per row):

| `σ` | share of `M_free` that is ordering error, median [p10, p90] |
|---|---|
| 0.05 | 0.02 [0.00, 0.18] |
| 0.2 | 0.14 [0.00, 0.46] |
| 0.5 | 0.34 [0.04, 0.64] |
| 1.0 | 0.53 [0.15, 0.77] |
| 3.0 | 0.71 [0.23, 0.93] |

For nearly correct evaluators — the regime of practical interest — **almost all of the misalignment the
cardinal measures report is shape, not order.** Whether shape counts as misalignment is the principal's
declaration: it counts under a cardinal target (the principal's exchange rates between outcomes are
distorted) and not under an ordinal one. This is a declared-convention question of the same kind as
budget/free/price, and the framework currently makes it silently, for the cardinal side.

**Against the contract** (a sketch, for R7-7 to prove). Under an ordinal declaration, `M_ord` satisfies M1
(0 exactly on `C_F`), M2, M3 strengthened to every increasing map, M4, M5 (the ray lies in `C_F`), M6 and
M8. M7 does not apply: this is a new declared convention, not a refactor of `M_free`.

## Verdict and trigger

- **R7-5 is not pursued.** Roles 1 and 2 of KL are forced. Role 3 is already generalized by [[Prop 15]]
  where it matters, the identity. Every candidate belongs to another layer or another step. This is a clean
  negative.
- **What survives.** [[Prop 15]] stays as the hook. The decoupling of harm and detectability outside KL is a
  corollary of [[Prop 15]] and [[Prop 18]]. It will be stated when an intent with `Ψ ≠ KL` is actually
  needed.
- **Revival trigger.** A real principal whose intended regularizer is not KL, whose verdict under the KL
  measures is wrong by common sense, and whose case is not repaired by a target set, a non-linear target or
  a declared resolution.

## Consequences for the roadmap

- **R7-7 next.** Lead case: the ordinal target, with `M_ord`, the decomposition and a pre-registration.
- **R7-6** passes the PI's test at first sight (coverage and diversity targets, case 4). Apply the test
  properly before starting it.
- **R7-8** has a real trigger, case 5, but only for continuous `X` with singular behaviour. It stays
  optional.

## Probe output

Scripts: `70 Project/R7/r75_probe.py`, `70 Project/R7/r75_c5.py` (seeded). Output:
`70 Project/R7/r75_probe_output.txt`. Exploratory: not pre-registered, and not a `verify.py` block. R7-7
will turn the claims above into core items with a check.

```
C2 PAVA vs generic optimizer, 60 instances: min(generic - PAVA) = -8.9e-16 (negative would refute), max = 4.6e-15
C1 bon4     : M_free median 0.079 [p5 0.017, p95 0.197]; M_free/KL(p||q) median 0.13; M_free>1e-6 in 1.000; max M_ord 1.2e-16
C1 bon16    : M_free median 0.107 [p5 0.004, p95 0.459]; M_free/KL(p||q) median 0.06; M_free>1e-6 in 0.995; max M_ord 1.2e-16
C1 bon64    : M_free median 0.035 [p5 0.000, p95 0.572]; M_free/KL(p||q) median 0.01; M_free>1e-6 in 0.925; max M_ord 1.4e-16
C1 quant0.1 : M_free median 0.330 [p5 0.006, p95 0.863]; M_free/KL(p||q) median 0.16; M_free>1e-6 in 1.000; max M_ord 2.1e-16
C1 quant0.3 : M_free median 0.392 [p5 0.060, p95 0.639]; M_free/KL(p||q) median 0.35; M_free>1e-6 in 1.000; max M_ord 2.6e-16
C3 monotone-transform evaluator: max M_ord 1.2e-16; M_free median 0.000 (>1e-6 in 0.66)
C3 reordering evaluator: M_ord > 1e-9 in 0.983; median M_ord/M_free 0.30
C4 M_free - (M_ord + M_free(p0)) over 1000 instances: min -4.44e-16, max 8.36e-01, |.|<1e-10 in 0.095
C5 share of the free measure that is ordering error, M_ord/M_free, for evaluators F_hat = F + sigma*noise (400 instances each)
  sigma=0.05: median 0.02  [p10 0.00, p90 0.18]
  sigma= 0.2: median 0.14  [p10 0.00, p90 0.46]
  sigma= 0.5: median 0.34  [p10 0.04, p90 0.64]
  sigma= 1.0: median 0.53  [p10 0.15, p90 0.77]
  sigma= 3.0: median 0.71  [p10 0.23, p90 0.93]
```
