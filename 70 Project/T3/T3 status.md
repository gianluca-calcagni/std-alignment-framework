---
id: "T3 status"
type: "report"
updated: "2026-09-26"
---
# T3 — status: blocked on network access (after v7.4)

The pre-registration ([[T3 preregistration]], commit `37be3d8`) was pushed before any retrieval. Then every
route to source S1 (Gao, Schulman & Hilton 2023) was refused by the environment's egress policy: `arxiv.org`,
`proceedings.mlr.press` and `ar5iv.labs.arxiv.org`, from the shell and from the web-fetch tool. `semanticscholar.org`,
`openreview.net` and `huggingface.co` are refused too; only package registries are reachable.

A web search returned only snippets. One says that the paper *shows* the values of `α_bon`, `β_bon` and `β_RL` as
they scale with parameter count, which suggests a figure rather than a table; under data rule 1 a figure is
usable only with a stated reading uncertainty. Snippets are not a source, and nothing was filled from them or
from memory (data rule 6).

**No prediction has been evaluated.** To resume: allow `arxiv.org` (or `proceedings.mlr.press`) in the
environment's network settings and rerun the retrieval against the frozen pre-registration.
