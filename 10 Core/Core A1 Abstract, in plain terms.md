---
id: "Core A1 Abstract, in plain terms"
type: "section"
part: "core"
order: 1
updated: "2026-09-26"
---
## Abstract, in plain terms

Someone — or something, like natural selection — has a goal: the **target**. An agent works toward a slightly
different goal: the **evaluator**, meaning whatever it is actually rewarded for. The agent is limited: moving
away from its default habits costs it something. This file does two things. It **measures** how far the
agent's actual behaviour departs from the behaviour intended for the target — from behaviour alone, whatever
the agent is, against a default that whoever states the target also declares. And it **explains** the departure by what the agent optimizes and how.

The main findings, in words:

- **The loss equals how far the agent's actual behaviour is from the behaviour it would show if it
  pursued the target.** It is not a bound; it is an equality, and it holds for any agent (Theorem [[Thm 1|1]]).
  **Misalignment** is the part of that departure that pursuing the target harder or more softly cannot
  explain (Def. [[Def 8|8]], Prop. [[Prop 24|24]]).
- **Which mistakes matter depends on how hard the agent optimizes.** A lightly optimizing agent is hurt by
  errors that are spread out; a strongly optimizing agent is hurt by rare, extreme errors. So no ranking of
  errors holds at every level of optimization (Theorem [[Thm 9|9]]).
- **How you limit the agent decides what you must know about the evaluator's errors.** The most common
  limit (KL) cannot contain errors with heavy tails, whatever the budget; a different limit (χ²) can
  (Prop. [[Prop 11|11]]).
- **Several results hold for any optimizer at all** — not only the idealized one used elsewhere. The
  simplest: the target gains exactly what the evaluator gains, minus how much the optimizer's choices
  correlate with the evaluator's error (Prop. [[Prop 20|20]]).
- **For any agent, a departure that costs little — counting both lost value and the information spent,
  and measured against an idealized intended agent — is hard to detect from behaviour** (Prop. [[Prop 18|18]]). The converse fails: a misalignment
  that loses no value at all can still be easy to detect. An agent that behaves differently when it is
  tested than when it is deployed is captured by a single number, the evaluation gap (Prop. [[Prop 19|19]]).

