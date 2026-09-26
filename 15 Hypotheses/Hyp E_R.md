---
id: "Hyp E_R"
type: "hypothesis"
title: "the reward-coupled entropic agent"
defined_in: ["Def 16"]
assumed_by: ["Prop 27", "Prop 28", "Prop 29", "Prop 30"]
aliases: ["(E_R)", "Hypothesis (E_R)"]
updated: "2026-09-26"
---
# Hyp E_R — the reward-coupled entropic agent
<!-- gen:header -->
> [!important] Hypothesis about the actual actor · assumed by 4 results
<!-- /gen:header -->

## Statement

The agent maximizes its own entropic utility plus its continuation value, which depends on the external
reward it earns: `p̂_c = argmax_p [E_pG − KL(p‖q_A)/β + W_c(E_pR)]`. Under the persistence coupling, it
maximizes its discounted value.

## Where it is defined

[[Def 16]] (R7-4). This note is an index. The authoritative statement is in [[Def 16]].

## What it adds

By [[Prop 27]], (E_R) reduces to (E_A) context by context, with effective evaluator `G + κ_c R`. So every
(E_A) and (E) result applies per context. What it adds is the **derivation** of the weight `κ_c` — a
shadow price — and with it the dependence of behaviour on the contingency `m_c`.

<!-- gen:links -->
## Assumed by
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4
- [[Prop 28]] — incentive masking; R7-4
- [[Prop 29]] — the outer process sees only rewarded behaviour; R7-4
- [[Prop 30]] — the fake-alignment gap; R7-4
<!-- /gen:links -->
