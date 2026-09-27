---
id: "00 Home"
type: "home"
index_of: "home"
updated: "2026-09-26"
---
# Alignment as the tilt of an error by a bounded actor — vault v7.8

**What this is.** A formal framework for alignment: it measures how far behaviour departs from the behaviour
intended for a target, from behaviour alone, and explains the departure by actor models. As of v7.0 it is an
Obsidian vault. Every definition, result, check, source and retraction is a typed note, and dependencies are
derived from the text and verified by a linter.

## Two layers

- **Measurement** — what misalignment *is*. It needs only the declared reference, the target, a convention
  and the actual behaviour.
- **Explanation** — *why* behaviour departs from the intended one: an evaluator and its error, the actor's
  own reference, and actor models.

The [[Core index]] lists items by layer. The linter keeps the measurement layer free of explanation
vocabulary and dependencies, and requires a check for every measurement-layer result.

## Where to start
- [[Core index]] — the core, section by section; start with [[Core A1 Abstract, in plain terms]].
- [[Dictionary index]] — outside results derived or related inside the core.
- [[Boundary index]] — the attack surface, and what is outside.
- [[Status index]] — the claim ledger, retractions, open questions, honest position.
- [[Checks index]] — the numerical checks and their recorded outputs.
- [[Sources index]] — the bibliography, one note per source.
- [[ROADMAP]] · [[Method]] · [[Census]] · [[T1_RULES_FROZEN]] (the frozen generality result).

## Note types

Every note has a `type` in its frontmatter. Each type has a template in `_templates/`.

| Type | Folder | Holds |
|---|---|---|
| `definition`, `theorem`, `proposition`, `corollary`, `lemma`, `remark`, `overview` | `10 Core/items` | Statement, Proof, Notes and checks, then generated links |
| `hypothesis` | `15 Hypotheses` | named assumptions about the actual actor ((E), (E_A), (E_R), (C)); results carry an `[Assumes …]` tag |
| `section` | every part | narrative text; embeds its items with `![[…]]`, so a section reads linearly in Obsidian |
| `dictionary-entry` | `20 Dictionary` | one entry per section of the dictionary |
| `attack-surface` | `30 Boundary` | C01–C15 |
| `check` | `40 Checks` | the script and block, the recorded output, what it verifies |
| `source` | `50 Sources` | the reference, where it is used, bibliographic status, external links, citing notes |
| `retraction` | `60 Status/retractions` | what was retracted, its replacement, who found it, the notes it affects |
| `index`, `home` | — | generated navigation |
| `project`, `working-notes`, `method`, `census`, `report`, `log` | `70 Project`, `80 Logs` | whole documents |

## Rules — how the vault stays sound

1. **Derived fields are never edited by hand.** These are `depends_on`, `mentions`, `checks`, `sources`,
   `assumes`, `tier`, `status`, `verifies`, `cited_by` and `affects`, plus everything between
   `<!-- gen:… -->` markers. Run `python3 tools/vault.py sync` after any edit.
2. **Logical dependencies are the references in a note's Statement and Proof, plus the symbols they use.**
   References elsewhere are `mentions`. Dependencies are parsed from the text — including ranges like
   "Props 18–19" — and from a symbol table: a statement using `R^C` depends on the note that defines `R^C`,
   whether or not it cites it. So they cannot drift from what the proof says.
3. **`python3 tools/vault.py lint` must report 0 errors before a turn ends.** It checks:
   - the schema for every type;
   - that every link resolves;
   - no dependency cycles;
   - definitions citing only earlier items;
   - `[Assumes …]` tags;
   - the two layers: no explanation vocabulary or dependency in the measurement layer, and a check for every
     measurement-layer result;
   - that checks and sources exist;
   - that generated sections are up to date;
   - that the current version is stated consistently, and that no part's status banner is older than the
     newest version its own text refers to (v7.3.3).
4. **Linear views** for reviewers are compiled into `build/` by `python3 tools/vault.py compile`.
5. **Queries:**
   - `python3 tools/vault.py deps "Thm 13"` gives dependencies and dependents;
   - `python3 tools/vault.py scan A3` gives the dependency scan for a refactor step.
6. **The migration from v6.6 is proved lossless** by `python3 tools/vault.py migration-check`. A fresh build from
   the frozen flat files in `archive/v6.6_flat/` reproduces every file's token stream, after file-name
   citations become links. Edits made since are listed in [[Status 05 Hygiene log]].

## Counts
<!-- gen:index -->
| Type | Notes |
|---|---|
| attack-surface | 15 |
| census | 1 |
| check | 53 |
| corollary | 11 |
| definition | 20 |
| dictionary-entry | 13 |
| home | 1 |
| hypothesis | 4 |
| index | 6 |
| lemma | 2 |
| log | 7 |
| method | 1 |
| overview | 1 |
| project | 1 |
| proposition | 30 |
| remark | 3 |
| report | 35 |
| retraction | 78 |
| section | 39 |
| source | 101 |
| theorem | 5 |
| working-notes | 1 |
<!-- /gen:index -->
