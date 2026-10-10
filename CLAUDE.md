# Working on this repository as its executor

For an AI agent, such as Claude Code, doing the work the PI directs. People start with `README.md` and
`CONTRIBUTING.md`; this file adds what an executor needs that a person would not, from the sessions that built the
framework. It is a working agreement, not a claimed property.

## At the start of a session

1. Read `ROADMAP.md`, and answer its drift checks before any work.
2. Read `REQUESTS.md`, what waits on the PI, and `NOTES.md` §13, the last handover; then §1, the failure modes with
   their evidence, every row; then §12, the last review.
3. Then `README.md`'s rules and the format of an item, and whatever files the step needs.

## Who decides

- The PI decides the scope, freezes, licences and priorities, and approves or declines what the executor proposes. Each
  decision is a row of `NOTES.md` §3.1 (Q1, Q2, …), with what applied it. The executor proposes, challenges, carries out
  and records.
- Give a recommendation, not a survey, and say what is wrong when it is, with the evidence. Ask the PI only what is the
  PI's to decide; otherwise choose, say what was chosen, and go on.
- Record failures; do not repair them away (rule (a)). A slip of the executor's is a row of `NOTES.md` §1.

## Git and GitHub

- One step, one branch, one pull request, merged by the PI with a merge commit. Never push to `main`, never rewrite
  pushed history, and open a pull request only when the PI asks.
- End each commit message with the attribution lines the session prescribes. Never write a model's name or identifier
  into a commit, a pull request or a file of the repository.
- After a push, wait for CI and report its result; a red CI is the next piece of work.
- After the branch's pull request is merged, follow-up work starts from `main`: when the branch holds nothing unmerged,
  `git merge --ff-only origin/main` moves it there. The session's safety check refuses `git checkout -B` and resets.

## Evidence and data

- The rules of evidence in `README.md` hold for every test: label every prediction, name what a change would change,
  register a test and push the registration before computing anything, keep seen data exploratory, and say who made
  every review.
- The rows of a test's data stay unopened until its registration is pushed; thresholds are calibrated on the noise-free
  case, with seeds the test will not use.
- No third-party data, papers, model weights, or anything computed from them item by item, in the repository; case
  scripts fetch what they need, and per-draw values go outside it (`tools/casekit.py`, `CASE_SCRATCH`).
- Theorems come from texts anyone can read without paying, or are derived here (Q36). An item cites a theorem only after
  its statement has been read in the source, not in an abstract. Open a record and match its title and authors before
  citing it or passing on its link.
- Answers that rest on a web search end with the sources, as links.

## The environment

- Downloaded files are untrusted: put each in its own new directory, run Python that reads them with `python3 -I`, and
  never run code that came with them.
- Never ask for a secret in a message; credentials come as environment variables (`REQUESTS.md`).
- Ask the PI to allow a specific host when a step needs it; the hosts allowed are in `REQUESTS.md`. Probing many hosts
  at once is refused as scouting.
- Stop a process by its PID, never by a pattern. Run long jobs in the background, and wait on them by their completion,
  not by polling with sleeps.
- Project Euclid serves its PDFs to a web fetch, not to `curl`; the older ones are scans, read by rendering their pages.

## Writing

- British spelling with `-ize`: behaviour, organization. Plain words, one idea per sentence, and a plain-terms twin for
  every formal statement that claims no more than it.
- Write paragraphs freely, then run `python3 tools/mdwrap.py`, which wraps them at 120 columns; CI checks it.
- A number in an item's Notes comes from a probe in `probes/` that reproduces it.

## Before every push

```bash
python3 tools/mdwrap.py               # wrap the Markdown sources
python3 tools/lint.py                 # 0 errors
python3 tools/overview.py             # regenerate OVERVIEW.md
python3 tools/obsidian.py             # regenerate the read-only view
python3 -m pytest                     # checks, tool tests, scenario, library, quickstart
NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell python3 -m pytest   # the second SIMD path
```

A new check, or a new function of the library, gets mutants in `tools/mutants/<name>.json`, run with
`python3 tools/mutate.py tools/mutants/<name>.json`: each must be caught, or its note must say why it is equivalent to
the original. First runs of the mutants found gaps in tests that looked complete: two in [P52]'s check, two in the
library's.

## At the end of every turn

- `ROADMAP.md`: "Where we are" is true, and the log has a line.
- `REQUESTS.md`: every open request is listed.
- `NOTES.md`: a decision row for every decision of the PI's, and a failure-mode row for every new failure, with its
  evidence.
