---
id: "R7-6 go-no-go"
type: "report"
updated: "2026-09-26"
---
# R7-6 — go/no-go: is there a real case that needs a non-linear target?

**Decision (proposed, for the PI): a narrow GO.** One real case gives a verdict that is wrong by common sense and
that no other step repairs: **distributional targets**. Its minimal repair is not the general machinery R7-6
planned (a target `U` on `Δ(X)`), but a **declared intensity cap** on the existing intent ray. General non-linear
targets stay untriggered until a case needs more than that.

## The PI's test

As for R7-5 ([[R7-5 go-no-go]]): proceed only if a real principal gets a verdict that is wrong by common sense,
and no other step (R7-7 target sets, R7-8 declared resolution) repairs it.

## The real case: the principal wants a distribution

The principal's intent is a *distribution* `p_T` over behaviours, not a direction to push in:
- **distributional pluralism** — a model's answers should reflect the spread of views in a population (Sorensen
  et al., *A Roadmap to Pluralistic Alignment*, ICML 2024);
- **diversity loss under RLHF** — fine-tuned models produce less varied outputs than their base models (Kirk et
  al., ICLR 2024);
- **coverage** — R7-5's case 4, mode dropping in generative modelling;
- **calibration** — frequencies of stated outcomes should match the world's.

*Bibliographic details not checked (no network access in this session); source notes follow if R7-6a starts.*

## What the current measures say

`p_T` is itself on an intent ray: it is the tilt of `q` by `F = log(p_T/q)` at `t = 1`. So the linear target that
best expresses the intent is `F`, and the half-ray `{p_{F,t} : t ≥ 0}` runs from `q` through `p_T` and on towards
the modes of `p_T/q`. **Every point beyond `p_T` is "the target, pursued harder"**, and the contract's M5 exempts it.

Probe (`70 Project/R7/r76_probe.py`, output `r76_probe_output.txt`; 300 random instances, exploratory, not
pre-registered, not a `verify.py` block):

| Behaviour | linear free measure | free measure on the path to `p_T` | `KL(p̂‖p_T)` |
|---|---|---|---|
| exactly `p_T` | 0 (all) | 0 (all) | 0 |
| **collapsed**, `p_{F,3}` | **0 (all)** | 0.673 median, `> 10⁻⁶` in all | 0.673 |
| **collapsed**, `p_{F,10}` | **0 (all)** | 1.210 median, `> 10⁻⁶` in all | 1.210 |
| over-diffuse, `p_{F,0.5}` | 0 (all) | 0 (all) | 0.178 |
| random | 0.445 median | 0.451 median | 0.759 |

**The collapsed agent — the RLHF diversity failure — scores as perfectly aligned.** That is wrong by common sense:
the principal asked for a spread, and got its modes. Neither R7-7 nor R7-8 repairs it: a target set is closed under
positive scaling (Def. 17), so it contains the whole ray; and nothing here is about resolution.

## The minimal repair, and why it is not general R7-6

The non-linear target `U(p) = −KL(p‖p_T)` gives the right verdicts. Its intent path — the regularized optima
`argmax_p [U(p) − KL(p‖q)/t]`, `t ≥ 0`, the construction Prop. 15 already uses — is, by stationarity,

```
p_t ∝ q^{1/(1+t)} · p_T^{t/(1+t)} = q · e^{(t/(1+t))·F},     F = log(p_T/q).
```

The probe confirms this against a generic optimizer to `1.1·10⁻⁵`. **This is the old ray, reparametrized by
`s = t/(1+t) ∈ [0, 1)`: the ray cut off at `p_T`.** So the defect needs one declaration, not a new kind of target:

> **Declared intensity cap.** A target may declare a maximum intensity `s_max`. The intended set is the capped
> ray `{p_{F,s} : 0 ≤ s ≤ s_max}`. A distributional target is the cap `s_max = 1` on `F = log(p_T/q)`.

- Under-pursuit (`s < s_max`) stays exempt, as M5 says: weakness, not misdirection.
- Over-pursuit (beyond the cap) is charged: the free measure becomes `KL(p̂‖p_{F,s*})` with `s*` capped, which is
  `KL(p̂‖p_T)` for the collapsed agents above.
- M5 needs restating as "pursues the target at an intensity up to the declared cap". With no cap it reads as now.

**Elegance is a warning** (anti-drift rule 5), so the falsifier comes first. The coincidence holds because both
`U` and the regularizer are KL: it will not survive a principal whose distributional target is scored by another
divergence. If a real case needs, say, total variation to `p_T`, the cap is not enough and general R7-6 is
triggered.

## Other candidates, not examined here

- **Risk-sensitive targets**, `U = E_p F − κ·Var_p F` (Prop. 15's example), and CVaR.
- **Group fairness**, `U = min_g E_p[F | g]`.

Each may give a wrong verdict under the linear measures; neither was probed. They are the revival trigger for
general R7-6.

## Proposal

- **R7-6a — intensity caps and distributional targets.** Pre-register, then define the cap against the contract
  (M5 restated; reduction to the uncapped ray when `s_max = ∞`, so M7 is exact); decide the budget convention past
  the cap; restate the free and budget measures; one `verify.py` block.
- **R7-6 proper** (a general `U` on `Δ(X)`): **not pursued** until a risk-sensitive, fairness or non-KL
  distributional case gives a wrong verdict that the cap cannot repair.
