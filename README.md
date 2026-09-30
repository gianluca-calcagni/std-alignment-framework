# std-alignment-framework — the slim core (v8, in progress)

[![checks](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml/badge.svg)](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml)

A standard formal framework for alignment problems in general, not only in machine learning: AI systems, humans,
institutions and organisms. The aim is a framework that is solid enough to build on, substrate-independent, easy to
import existing theorems into, and able to make testable predictions, support diagnostics, and show its own limits.

This branch rebuilds the core from scratch: slim, justified, and in plain terms first.

## Where things are

| | |
|---|---|
| `CORE.md` | the core: one document, read top to bottom |
| `REFERENCES.md` | the sources the core cites |
| `checks/` | one pytest check, at least, for every result in the core |
| `tools/lint.py` | the rules below, as code; `tools/test_lint.py` tests them |
| `NOTES.md` | the executor's working notes: hunches not yet in the core, and open issues. Not part of the core |
| `main` branch | **the archive** (v7.10, commit `9459c14`): everything proved, tested, retracted and logged before this restart. Nothing there changes. A file comes over only when an item needs it (`git checkout main -- <path>`), and the item's lineage says so |

## Rules

**Enforced by lint** (`python3 tools/lint.py`; a property of the core is claimed only if lint checks it):
- **R1–R2.** Every `###` heading in `CORE.md` is an item: `### D1 — title`. The kinds are D (definition), P (proposition),
  T (theorem), L (lemma), C (corollary) and R (remark). Numbers increase within each kind.
- **R3–R4.** Every item has a **Statement**, an **In plain terms** twin and a **Lineage**. A definition also has a
  **Why this choice**; a result (P, T, L, C) has a **Proof** and **Checks**. Fields come in a fixed order, with no field
  empty.
- **R5.** References are written `[D1]`, `[P3]`. A statement, justification or proof may use only items that come
  earlier, so the dependencies follow the reading order and cannot form a cycle.
- **R6–R7.** Every check a result cites exists in `checks/`, and every check there is cited by some item.
- **R8.** Every citation `[@key]` is listed in `REFERENCES.md`, and every listed source is cited.

**Enforced by CI** (`.github/workflows/checks.yml`, on every push and pull request): lint, and every check on two
SIMD paths. A check asserts its claim with a tolerance derived from the scale of the quantity. It must hold on both
paths, rather than reproduce printed digits.

**Working agreements** (no tool checks these, so they are commitments, not claimed properties):
- **Reliability over elegance.** A result enters with a proof and a check that could fail: random instances, the
  degenerate and sign cases, and tolerances derived from the quantity's scale.
- **Every choice is justified.** "Why this choice" argues it, by generality (for example: every full-support
  distribution is an exponential tilt of the default), by canonicity, or by a named case where the alternative gives
  a wrong verdict.
- **Plain terms keep the qualifiers** of the formal statement.
- **Slim.** About a dozen items. An item that does not earn its place goes to an appendix, or stays on `main`.
- **Lineage** names the items on `main` that an item replaces and the retraction rows that touch them
  (`main: 60 Status/retractions/`), or says "New".
- **Empirical tests** are pre-registered and pushed before any computation, as on `main`.
- **One step, one branch, one pull request** into the branch that holds the new core, merged with a merge commit.

## The format of an item

```markdown
### D1 — Outcomes and default
**Statement.** A finite set `X` of outcomes, and a full-support distribution `q` on `X`, the default.
**In plain terms.** The things that can happen, and how often each happens by default.
**Why this choice.** …
**Lineage.** main: Def 1 (in part).

### P1 — Every behaviour is a tilt of the default
**Statement.** For every full-support `p` on `X` there is `F` with `p ∝ q·e^F`; `F` is unique up to a constant.
**In plain terms.** Any way of behaving can be written as the default reweighted by some objective.
**Proof.** …
**Checks.** checks/test_tilt.py::test_every_distribution_is_a_tilt
**Lineage.** New.
```

Optional fields, in order: **Example** (after Proof) and **Notes** (after Checks; attribution goes here, because a
citation in a proof is a dependency claim).

## Commands

```bash
pip install -r requirements.txt       # Python 3.11
python3 tools/lint.py                 # 0 errors required
python3 -m pytest                     # checks and linter tests
NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell python3 -m pytest   # the second SIMD path
```

## Starting a session

Read this file, `CORE.md` and `NOTES.md`. Then, on `main`, read `70 Project/NOTES_claude.md` §1: the failure modes of
past sessions, each with its evidence.

## License

GNU Affero General Public License v3.0 — see `LICENSE`.
