---
id: "Def 22"
type: "definition"
title: "value shortfall at equal effort; R8-1"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.83
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 10"]
mentions: ["Cor 17.1", "Def 11", "Def 20", "Def 9", "Prop 12", "Prop 37", "R8 foundations review", "T7-2d results", "Thm 17"]
checks: []
sources: []
aliases: ["Definition 22", "Def. 22"]
updated: "2026-09-27"
---
# Def 22 — value shortfall at equal effort; R8-1

## Statement

**Definition 22 (value shortfall at equal effort; R8-1).** Let `F` be a cardinal target, `p̂` full-support, and `λ` the
budget-matched intensity of Def. [[Def 10|10]], `KL(p_{F,λ}‖q) = KL(p̂‖q)`. The **value shortfall** of `p̂` is

```
ΔV = E_{p_{F,λ}}F − E_{p̂}F           below saturation,
ΔV = max F − E_{p̂}F                  at saturation (KL(p̂‖q) ≥ log 1/q(argmax F)).
```

It is the value, in `F`'s own units, that `p̂` forgoes against the behaviour that pursues `F` purely with the same
effort, effort being information spent away from `q`. It is a **report**, not a measure: it changes with the units of
`F`, by design, so it does not satisfy M3 of the contract.

## Notes and checks

*Note (why it exists).* Misalignment is in nats and unit-free (M3), so it cannot say how much is at stake. Below
saturation, `ΔV = M_budget/λ` (Thm [[Thm 17|17]](iii); Prop. [[Prop 37|37]](a)): the nats are the value shortfall priced at the
intended exchange rate. At low intensity a large shortfall costs few nats, and near saturation a small one costs
many. Reporting `ΔV` next to `M` shows both ([[R8 foundations review]], A1). It fails M3 of Def. [[Def 11|11]] on purpose: units are what it adds.

*Note (why at equal effort).* Against the free intended point the shortfall is zero whenever `t̂ ≥ 0`
(Prop. [[Prop 37|37]](c)): the free projection keeps value and removes only the off-ray divergence. A value gap needs a
counterfactual that holds something fixed. Equal information spent is the one the core already has (Cor. [[Cor 17.1|17.1]]:
the capacity actor's regret).

*Note (reading across substrates).* `F` is the principal's declared target, not a quantity the substrate supplies,
and `q` is the declared reference. Both are modelling choices, and `ΔV` inherits them.

| Substrate | `q` | `F` | effort `KL(p̂‖q)` | `ΔV` | floor (Def. [[Def 20\|20]]) as a standard |
|---|---|---|---|---|---|
| ML | the reference policy (e.g. SFT) | the principal's target (gold reward, not the proxy) | the KL spent from the reference, which RLHF budgets | gold reward forgone against the best policy with the same KL | a minimum expected gold score; with `F = −1{harmful}`, a maximum harm rate |
| Humans | behaviour under the status quo or default | a declared welfare criterion, with its declarer named (the person or a planner) | how far choices move from the default | welfare forgone against the choices that move as far and pursue the criterion only | an adequacy standard (e.g. a minimum saving rate) |
| Institutions | the pre-reform or baseline distribution of decisions | the mandate a principal (legislature, board) declares | how far the institution departs from the baseline | mandate value forgone at equal departure: movement spent in other directions | a statutory minimum service level |
| Biology | the population's distribution without selection (neutral or ancestral) | log fitness (Malthusian), declared by the modeller | the information change the population undergoes | mean log fitness forgone against pure selection with the same change | a viability threshold (mean Malthusian fitness `≥ 0`) |

- *Biology is the exact case, and the principal is a metaphor.* With constant fitness, the replicator dynamics give
  `p_t ∝ q·e^{tF}`: the intent ray is the selection trajectory, and `dE_{p_t}F/dt = Var_{p_t}F` is Fisher's
  fundamental theorem. `ΔV` is then the log-fitness lost to forces other than selection (drift, mutation, migration,
  constraint) at equal divergence; at saturation it is `max F − E_{p̂}F`, a log-fitness form of genetic load. No one
  intends anything; "misalignment" means departure from pure selection. Frequency-dependent fitness breaks the fixed
  `F`.
- *Humans:* the welfare criterion is declared, not inferred from choices (Prop. [[Prop 12|12]]). T7 found the default can move
  the evaluator itself ([[T7-2d results]]), so `q` must be the declared reference, not a fitted one.
- *Institutions and ML:* the principal and the agent are distinct and `F` is the principal's. Contexts are exogenous
  (Def. [[Def 9|9]]); an agent that chooses its contexts is outside this reading.

*Note (what it does not fix).* Risk attitude over outcomes (a CVaR, "no catastrophe above 1%") is non-linear in `p`
and not representable. `ΔV` is an expectation. All quantities are population quantities; estimation is not yet
specified ([[R8 foundations review]], A3).
