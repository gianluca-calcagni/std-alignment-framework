---
id: "Def 21"
type: "definition"
title: "declared resolution; R7-10"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.81
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 17"]
mentions: ["Prop 36", "R7-10 results", "R7-5 go-no-go"]
checks: []
sources: []
aliases: ["Definition 21", "Def. 21"]
updated: "2026-09-27"
---
# Def 21 — declared resolution; R7-10

## Statement

**Definition 21 (declared resolution; R7-10).** A **resolution** is a partition `𝒢 = {C_1, …, C_m}` of `X` into
non-empty cells, such that every member of the declared target set `𝒯` is constant on each cell. Write `p_𝒢` for the
cell masses of `p`, and the **coarse instance** for the instance on `𝒢` with reference `q_𝒢`, target set `𝒯` read on
cells, and the same convention, floor and cap.
- The **measure at resolution `𝒢`** is `M^𝒢(p̂) = M(p̂_𝒢)`, the declared measure of the coarse instance. Under the budget
  convention its budget is `k_𝒢 = KL(p̂_𝒢‖q_𝒢)`.
- Its **intended set** is the preimage of the coarse instance's intended set: `{p ∈ Δ° : p_𝒢 is intended on 𝒢}`.
  Inside a cell, every split is intended.
- The **within-cell divergence** of `p̂` is `W = Σ_C p̂(C)·KL(p̂(·|C)‖q(·|C)) = KL(p̂‖q) − KL(p̂_𝒢‖q_𝒢)`.
- The **default** resolution is the finest partition, `{{x} : x ∈ X}`, under which `M^𝒢 = M`.

## Notes and checks

*Note (what it declares).* Which differences between behaviours matter to the principal at all. Elicitation: "Which
differences between behaviours matter to you?" A principal who asks only for correct answers, style free, declares
the partition into correct and incorrect answers.

*Note (why the default is the finest partition).* Drift inside cells the target does not distinguish — verbosity,
sycophancy, style — is where reward hacking often lives. The default charges it (Prop. [[Prop 36|36]](b)); a principal
who declares indifference gives up seeing it (Prop. [[Prop 36|36]](d)). This replaces a choice the core made silently until
v7.7: inside such cells, the intended split followed `q` ([[R7-10 results]]).

*Note (the admissibility condition).* A resolution coarser than the target would declare indifference to
distinctions the target makes. That is incoherent, so it is excluded, not repaired.

*Note (R7-8).* A declared resolution is the cheap remedy for deterministic behaviour on a continuous `X`, which
saturates every divergence ([[R7-5 go-no-go]], case 5). The finite core covers it by refinement only (Prop. [[Prop 36|36]](e));
measurable spaces remain R7-8.
