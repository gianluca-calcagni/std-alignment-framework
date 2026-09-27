---
id: "HANDOVER"
type: "report"
updated: "2026-09-27"
---
# Handover — start here in a fresh session

This note points to other notes rather than repeating them. If it disagrees with [[ROADMAP]] §0 or
[[NOTES_claude]] §0, those two notes are right and this one is stale: fix it.

## Opening prompt (paste into a new session)

```
You are continuing work on std-alignment-framework (an Obsidian vault in a git repo).
Read, in order, before doing anything:
  1. "70 Project/HANDOVER.md"  (this note: rules and tooling)
  2. README.md
  3. "70 Project/ROADMAP.md"  §0, §1, §4, §4b, §6
  4. "70 Project/NOTES_claude.md"  §0, §1, §5, §6
  5. "60 Status/Status 00b Abstract, in plain terms.md"
Then tell me, in a few lines, the current version, what is next, and which item you
would start with. Before you start it, apply rule 13: name an example where it changes
a verdict. Do not compute anything before its pre-registration is committed and pushed.
Preference: no sycophancy, only intellectual honesty and constructive challenges.
```

## State at handover (v7.8)

- **The core:** misalignment is the KL projection onto a declared intended set (Def. 19, Prop. 34). The
  declarations are the target set (Def. 17), the cap (Def. 18), the floor (Def. 20) and the resolution (Def. 21); the
  contract is Def. 11. §4b is confirmed: the core steps are closed, and next is T7.
- **Next:** a PI decision; T7 is closed ([[T7 summary]]): the AI case was a relabelling with one out-of-sample prediction, the human case failed its clean test, and case 3 was skipped (no public data); case 1 is indexed in [[T7 case 1 index]]. B1 ([[B1 brainstorm]], [[NOTES_claude]] §8) shaped its protocol.
- **Open for the PI:** identifiability ([[ROADMAP]] §6 I1),
  the lead brainstorming theme; rater disclosure
  ([[ROADMAP]] §5, item 3). Deferred by the PI: T3b. T6 is deferred: do not build toward it.
- **The honest gap:** §4b item 3 is not met ([[T7 summary]]). Real data confirmed the mathematics every time, but the
  diagnosis never beat a raw feature, and B12's human actor failed its clean test. T3 was a clean negative ([[T3 results]]). The refactor steps were justified by toy examples, by
  the PI's choice; the debt, and the real case that retires each row, is [[ROADMAP]] §4c.

## Working rules (the ones a fresh instance breaks first)

- **Pre-register, then compute.** Commit and push the pre-registration first; it is hash-frozen in
  `tools/frozen.json`. A failed registered prediction is recorded, never repaired in place ([[ROADMAP]] §4, and
  rules 11–13 there).
- **Rule 13:** an item runs only with a named example where it changes a verdict, or, if the PI approves it, a
  structural claim that could fail.
- **One roadmap step is one branch and one pull request.** Merge with a merge commit, not squash or rebase, so
  the pre-registration commits keep their timestamps.
- **The tools are slow.** Locally, rerun only the blocks a change touches, in the background:
  `python3 tools/reproduce.py verify V39`. CI (`.github/workflows/checks.yml`) reruns everything on each push.
- **Second SIMD path** for every new block before recording its output:
  `NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell python3 verify.py Vn`. Optimizer-bound lines get an
  entry in `tools/reproduce_tolerances.json`, with its reason.
- **Vault cycle:** edit notes, then `python3 tools/vault.py sync`, then `lint` (0 errors required; the warnings
  are known), then `compile`. Never hand-edit `depends_on` or text between `gen` markers. A citation in a proof
  is a dependency claim; attribution goes in Notes.
- **New core item:** add its symbols to `SYMBOLS` in `tools/vault.py`; if it names a test case such as
  `p̂ = p_{F,t}`, add it to `NOT_E`. Version bumps must agree across the Home title, README title, ROADMAP §0 and
  the newest hygiene-log row, and each part's banner must be as recent as its text: lint checks both.
- **Environment:** only package registries are reachable (arxiv, PMLR and Hugging Face return 403). Read PDFs
  with `pymupdf`. Kill processes by PID; `pkill -f` can match its own shell. Quote Markdown heredocs (`<< 'EOF'`).
