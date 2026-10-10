"""W1's report to the standard as data (`STANDARD.md`; `stdalign/report.py`): standard-report.json, built from the
aggregates of report.json and the declaration and observations of REPORT.md. Written on 2026-10-09, after the report;
the numbers are those of REPORT.md, nothing is recomputed. Usage: python3 cases/w1-best-of-n-slope/make_standard_report.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
NS = ("2", "16", "128", "1024")
BY_PROMPTS = "means over the 1,000 prompts, with 95% intervals from 1,000 resamples of the prompts"


def table(md, heading):
    """The rows of the table under a heading of REPORT.md, as {field: entry}."""
    part = md.split(heading, 1)[1].split("\n## ", 1)[0]
    return {m[1]: m[2] for m in re.finditer(r"^\| ([^|]+?) \| [^|]+ \| (.+) \|$", part, re.M) if m[1] != "Field"}


def est(label, x, unit=""):
    return {"label": label, "value": round(x["mean"], 6), "interval": [round(v, 6) for v in x["interval_95"]],
            "unit": unit}


def exact(label, value, basis, unit=""):
    return {"label": label, "value": round(value, 6), "exact": True, "basis": basis, "unit": unit}


def main():
    d = json.loads((HERE / "report.json").read_text())
    md = (HERE / "REPORT.md").read_text()
    n = d["n"]
    declaration = table(md, "## 1. The declaration")
    added = "added when the report was migrated to data (2026-10-09); the field did not exist when the report was written: "
    declaration["Access"] = added + ("counts: each prompt's 12,600 answers with their gold and proxy scores, the default "
                                     "estimated by their empirical distribution; best-of-n computed exactly from them")
    declaration["Named objectives"] = added + "none"
    declaration["Runs"] = added + "one: best-of-n is computed, not trained"
    observations = table(md, "## 2. The observations")
    per_prompt = "median over the 1,000 prompts reported on; each prompt's value is computed from its estimated default"
    share = "share of the 1,000 prompts reported on"
    results = {
        "Misalignment": {"identified": True, "assumptions": "each prompt at an intensity of its own; " + BY_PROMPTS,
                         "entries": [est(f"M, n = {k}", n[k]["M"], "nats") for k in NS]},
        "Uncertainty": {"text": BY_PROMPTS + ". They leave out the sampling of each prompt's 12,600 answers, which "
                        "estimate the default, and the proxy's training. [P23]'s chi-squared reference does not apply: "
                        "the behaviour is computed from the policy's answers, not counted from decisions."},
        "Evidence and detection": {"identified": True, "assumptions": "the Chernoff information on a grid of 201 "
                                   "exponents, so a lower bound; " + BY_PROMPTS,
                                   "entries": [est("evidence per answer, n = 16", n["16"]["M"], "nats"),
                                               est("Chernoff information, n = 16", n["16"]["chernoff"], "nats")],
                                   "note": "computed at n = 16 only"},
        "Revealed intensity": {"identified": True, "assumptions": "two of [P5](iv)'s three cases occur; t* is never "
                               "infinite",
                               "entries": sum(([exact(f"median t*, n = {k}", n[k]["t_star"]["median"], per_prompt),
                                                exact(f"share with t* = 0, n = {k}", n[k]["t_star"]["share_zero"], share)]
                                               for k in NS), [])},
        "Departure split": {"identified": True, "assumptions": BY_PROMPTS,
                            "entries": sum(([est(f"departure, n = {k}", n[k]["departure"], "nats"),
                                             est(f"pursuit part, n = {k}", n[k]["pursuit"], "nats"),
                                             est(f"M as a share of the departure, n = {k}", n[k]["M_share_of_departure"])]
                                            for k in NS), [])},
        "Stakes": {"identified": True, "assumptions": "the gold reward model's units; the matched intensity is infinite "
                   "or zero in a few prompts, where under-pursuit is not defined; " + BY_PROMPTS,
                   "entries": sum(([est(f"shortfall S, n = {k}", n[k]["S"], "gold units"),
                                    est(f"gold gained over the default, n = {k}", n[k]["gain"], "gold units"),
                                    exact(f"median matched intensity, n = {k}", n[k]["lambda"]["median"], per_prompt)]
                                   for k in NS), [])}
                  | {"note": "under-pursuit at n = 16 over the 996 prompts where the matched intensity is finite and "
                     "positive: " + f"{n['16']['under']['mean']:.3f} nats"},
        "Intensity": {"identified": True, "assumptions": "one intensity for all prompts, the best of 701 on a grid from "
                      "1e-3 to 1e4; " + BY_PROMPTS,
                      "entries": sum(([est(f"misalignment at one shared intensity, n = {k}", n[k]["shared"]["M"], "nats"),
                                       est(f"excess over each prompt's own, n = {k}", n[k]["shared"]["inconsistency"],
                                           "nats"),
                                       exact(f"the shared intensity, n = {k}", n[k]["shared"]["t"],
                                             "the minimizer on the grid, for the 1,000 prompts reported on")]
                                      for k in NS), [])},
        "Named and unexplained misalignment": {"not_reported": "no named objectives were declared"},
        "Uncertain target": {"not_reported": "the target was declared as one objective, the gold, not a family"},
        "Outer and inner misalignment": {"not_reported": "not computed in this report"},
        "Tampering": {"not_reported": "no channel: both rewards are fixed functions of the answer's text"},
        "Drift": {"not_reported": "one run"},
        "Avoidable and unavoidable misalignment": {"text": "with the feasible set declared as everything, all of it is "
                                                   "avoidable; what a selector bound to the proxy's ranking could do is "
                                                   "not analysed"},
        "Resolution": {"text": "the principal's resolution is the finest, so nothing was forgiven; the actor's, the "
                       "proxy's ties, is not analysed"},
        "Sensitivity": {"not_reported": "not computed"},
        "Evaluator": {"identified": True, "assumptions": "the gold averaged over prompts in bins of the proxy's rank "
                      "within each prompt ([P26]); this says nothing within a prompt; " + BY_PROMPTS,
                      "entries": [est(f"mean gold, proxy rank {b}", v, "gold units")
                                  for b, v in d["regression_by_rank"].items()]
                      + [est("residual share of the gold's variance, 100 bins of rank", d["residual_share_100_bins"])]},
        "Pass-through": {"not_reported": "no intervention"},
        "Unobserved conditions": {"text": "none within the report; prompts outside AlpacaFarm's validation split are "
                                  "not identified by it"},
        "Evaluation gap": {"not_reported": "evaluation and use are not told apart"},
        "Premises": {"text": "the gold is a reward model, not people: the report measures misalignment against that "
                     "model. The default is an estimate from 12,600 answers; quantities that depend on the policy's "
                     "rarest answers are not reported."},
    }
    report = {"case": "w1-best-of-n-slope", "declared_before_data": False, "confirmatory": False,
              "declaration": declaration, "observations": observations, "results": results}
    (HERE / "standard-report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
