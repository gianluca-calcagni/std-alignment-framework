---
id: "T7 summary"
type: "report"
updated: "2026-09-27"
---
# T7 — summary: the framework against real cases (closed by the PI after case 2d)

T7 asked whether the framework, run on real data, gives a diagnosis, a checkable prediction and the imported theorems:
more than a relabelling (ROADMAP §4b, item 3). It is closed by the PI's decision: **"a negative is still a result."**
Every case was pre-registered before any value was read, and each amendment was registered before any affected
prediction was computed.

## The cases

| Case | Substrate | Data | Designs | Outcome |
|---|---|---|---|---|
| 1 | AI: evaluator length bias | AlpacaEval 2 (216 models), Chatbot Arena Elo (37), LLMBar (65 evaluator configurations) | 3 ([[T7 case 1 index]]) | verification always held; the style term **predicted out of sample** with independent labels (ρ 0.52) but **never beat the raw feature** it isolates |
| 2 | Humans: retirement-enrolment defaults | Choi et al. 2004 (Companies A, B, C), Madrian & Shea 2001, Beshears et al. w12009 | 3 ([[T7-2 results]], [[T7-2b results]], [[T7-2d results]]) | B12's structure **held roughly against opt-in** (3 of 4 companies), **failed the clean two-default test**; both post-hoc patterns failed once registered |
| 3 | Institutions: public goods | — | — | **skipped**: no complete public dataset reachable (CRAN, Dataverse, OSF, openICPSR blocked) |
| 4 | Biology | — | — | not attempted (the stop rule: one case, then decide) |

> [!warning] Read with [[R8 foundations review]]. **B1:** case 2 tested B12's actor model (explanation layer); it
> computed no misalignment measure, so §4b item 3 is *untested*, not failed, for humans. **B2:** case 1's targets were
> binary, so it exercised mainly the chain rule. **B3:** across T7, 5 of 15 empirical predictions held, and case 1's one
> success came after two failed designs.

## What T7 showed about the framework

1. **The mathematics holds on real data.** Every verification prediction held, in every design: the exact splits, the
   sign of the budget misattribution `Θ`, and the three-term decomposition.
2. **The measurement layer's diagnosis is a reading, not a new predictor.** In the AI case it isolated the right term
   (length inside quality cells) and that term predicted evaluator failure out of sample. The raw feature did as well.
   Its value there is the structure: named terms, the lever for each, and `Θ`.
3. **The explanation layer made a sharp, falsifiable claim, and the clean test rejected it.** B12's human actor — a
   logit with a default-dependent reference and a fixed evaluator — predicts one common ratio across non-default
   options. It holds roughly when one regime is opt-in and fails when two participation defaults are compared: a
   higher default pushed some people *down*. The default enters the evaluator, which B12 names as its bias; here the
   bias is large.
4. **The registration discipline earned its cost.** Two post-hoc patterns I read off small tables (the floor, the local
   pull) both failed when registered. Six stop-rule firings and amendments caught data-reading errors before any
   prediction was computed.

## Against the finish line (ROADMAP §4b)

- **Item 3 (one real diagnostic per substrate):** **not met.** AI: a prediction that held, but a relabelling. Humans: a
  real diagnostic, and it came out negative. Institutions and biology: no case.
- **Item 4 (an outside reader):** not started. It needs the PI.
- **The core is not final by its own definition.** It is a checked calculus whose measurement layer reads real data
  correctly, and whose one tested explanation-layer model (B12) needs revision.

## The toy-example debt (ROADMAP §4c)

- **R7-10 row:** retired as far as real data allow. The misattribution exists on real models; the style term predicts
  but ties the raw feature.
- **R7-7 row:** untouched. A best-of-n pipeline with its reward model was not available.
- **R7-6a and R7-6b rows:** untouched.

## What T7 leaves for the PI

- **Revise B12:** a default that enters the evaluator, or deviation costs that depend on direction. Test it on fresh
  two-default data.
- **An outside reader (§4b item 4):** now possible. The vault has real cases to run.
- **Data the environment cannot reach:** a public-goods replication file (case 3); a best-of-n reward-model dataset
  (§4c R7-7).
