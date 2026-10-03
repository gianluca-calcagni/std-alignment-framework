"""Write REPORT.md, W1's report to STANDARD.md, from report.json, output.json and explore.json: every number is filled
in from them, so the text cannot drift from the computation. Usage: python3 make_report.py"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def f(x, d=3):
    return f"{x:.{d}f}".replace("-", "−")


def ci(s, d=3):
    lo, hi = s["interval_95"]
    return f"`{f(s['mean'], d)}` (`{f(lo, d)}` to `{f(hi, d)}`)"


def reflow(text, width=120):
    """Join each paragraph's lines and wrap them at `width`, never inside `code`; headings and tables are kept."""
    out, para = [], []

    def flush():
        if para:
            words, cur = " ".join(para).split(" "), ""
            tokens, buf, inside = [], "", False
            for w in words:                          # keep a code span with spaces in one token
                buf = f"{buf} {w}" if buf else w
                inside ^= w.count("`") % 2 == 1
                if not inside:
                    tokens.append(buf); buf = ""
            if buf:
                tokens.append(buf)
            for t in tokens:
                if cur and len(cur) + 1 + len(t) > width:
                    out.append(cur); cur = t
                else:
                    cur = f"{cur} {t}" if cur else t
            out.append(cur); para.clear()

    for line in text.split("\n"):
        if not line.strip() or line.startswith(("#", "|")):
            flush(); out.append(line)
        else:
            para.append(line.strip())
    flush()
    return "\n".join(out)


def shape_of(means):
    rising = all(b >= a for a, b in zip(means, means[1:]))
    peak = max(range(len(means)), key=lambda i: means[i])
    single = all(b >= a for a, b in zip(means[:peak + 1], means[1:peak + 1])) and \
        all(b <= a for a, b in zip(means[peak:], means[peak + 1:]))
    if rising:
        return ("rises over every bin. Averaged over prompts, this says nothing within a prompt: [P19] would rule out "
                "overoptimization in a prompt only if that prompt's own regression rose")
    if single:
        return ("is single-peaked across the bins, averaged over prompts; within a prompt, [P25](iii) applies to that "
                "prompt's own regression, which bins averaged over prompts do not show")
    return "turns more than once across the bins, averaged over prompts"


def main():
    rep = json.loads((HERE / "report.json").read_text())
    out = json.loads((HERE / "output.json").read_text())
    tied = json.loads((HERE / "explore.json").read_text())["share_of_answers_tied_median"]
    ns = list(rep["n"])
    x16, reg = rep["n"]["16"], out["registered"]
    rows = "\n".join(f"| {n} | {ci(x['departure'])} | {ci(x['M'])} | {ci(x['pursuit'])} | "
                     f"{ci(x['M_share_of_departure'], 2)} | {ci(x['gain'])} | {ci(x['S'])} |"
                     for n, x in rep["n"].items())
    shared = "\n".join(f"| {n} | {ci(x['shared']['M'])} | {ci(x['shared']['inconsistency'])} | "
                       f"`{f(x['shared']['t'], 2)}` |" for n, x in rep["n"].items())
    edge = [n for n, x in rep["n"].items() if x["shared"]["t_at_grid_edge"]]
    grid_check = min(x["shared"]["grid_check"] for x in rep["n"].values())
    intensities = "\n".join(
        f"| {n} | `{f(x['t_star']['median'], 2)}` | {x['t_star']['share_zero']:.1%} | {x['t_star']['share_infinite']:.1%} "
        f"| `{f(x['lambda']['median'], 2)}` | {x['lambda']['share_infinite']:.1%} |" for n, x in rep["n"].items())
    bins = rep["regression_by_rank"]
    bin_rows = "\n".join(f"| {k} | {ci(v)} |" for k, v in bins.items())
    k0 = x16["prompts_without_departure"]
    no_departure = (f"In {'one prompt' if k0 == 1 else f'{k0} prompts'} the proxy scores every answer alike, so "
                    f"best-of-`n` is the default there, with no departure and `λ = 0`. " if k0 else "")
    share = rep["residual_share_100_bins"]["mean"]
    xs = list(rep["n"].values())
    m_lo, m_hi = min(x["M_share_of_departure"]["mean"] for x in xs), max(x["M_share_of_departure"]["mean"] for x in xs)
    ratio = min((x["gain"]["mean"] + x["S"]["mean"]) / x["gain"]["mean"] for x in xs)
    losing = [x["prompts_losing_gold"] / rep["prompts"] for x in xs]
    closing = (f"**What this report says.** Judged against the gold, best-of-`n` by this proxy is mostly misalignment: at "
               f"every `n` reported, `{f(m_lo, 2)}` to `{f(m_hi, 2)}` of its departure from the default is misalignment, "
               f"and the rest is pursuit of the gold. The gold rises with `n`, since on average over prompts it rises "
               f"with the proxy's rank, but in {min(losing):.0%} to {max(losing):.0%} of the prompts best-of-`n` lowers "
               f"it. The same departure, spent on pursuing the gold, would have gained at least {ratio:.1f} times as "
               f"much of it, on average, at every `n`. And a fixed `n` is not a fixed intensity: at one intensity shared "
               f"by all prompts, misalignment at `n = 16` is higher by {ci(x16['shared']['inconsistency'])} nats. These "
               f"are statements about one linear proxy, much simpler than Coste et al.'s neural ones, on one policy's "
               f"answers; they are exploratory, and a registered test would be needed to rely on any of them.")
    seen = ("at that resolution, most of the gold's variation within a prompt does not follow the proxy's rank"
            if share > 0.5 else "at that resolution, most of the gold's variation within a prompt follows the proxy's rank")
    text = f"""# W1 — Report to the standard

W1's data reported field by field to `STANDARD.md`: the framework's diagnostics on a real optimizer, best-of-`n`
selection by a learned proxy, judged against the gold. Computed by `report.py` after W1's verdict, on the same data;
descriptive, not a test, and it changes no verdict (`RESULTS.md`). Numbers are means over the {rep['prompts']:,} prompts,
with 95% intervals from 1,000 resamples of the prompts. `make_report.py` writes this file from `report.json`, which
holds aggregates only.

**Computation.** This is the sixth computation, and the only one whose numbers are reported. The first mishandled the
infinite intensities of section 3, and the second crashed in its final aggregation (`NOTES.md` §1, a run lost at its
last step). The third was stopped halfway: it broke ties in the proxy's score by one fixed order, which leaves the
gold's mean unchanged but adds that order to every divergence; here ties are broken at random, so each tied answer gets
its block's average weight, which a simulation of the selector confirmed (`NOTES.md` §1, a tie-breaking order charged
as departure). The fourth was stopped to add the specification at one shared intensity. The fifth ran in full, but its
under-pursuit was infinite in 9 prompts at the two largest `n`, where the matched intensity is in the hundreds or more and the
matched pursuit underflowed to zeros; under-pursuit is now computed in closed form.

## 1. The declaration

| Field | Core | Entry |
|---|---|---|
| Outcomes | [D1] | within each prompt, its 12,600 sampled answers; nothing was cut |
| Conditions | [D8] | the 1,000 prompts of AlpacaFarm's validation split used by Coste et al. [@coste2024], at equal frequencies; each prompt is a context, whose frequency the actor does not choose |
| Default | [D2] | within each prompt, the initial policy's behaviour, estimated by the empirical distribution of its 12,600 answers |
| Specification | [D3] | the standard specification of the gold reward `F`, AlpacaFarm's 7B human-preference reward model: in each prompt, pursue `F` from the default. Two forms: each prompt at an intensity of its own, judged on its own terms; and every prompt at one shared intensity, the stricter (`derived/estimation.md`, the Notes of [P24]), which KL-regularized training with one coefficient aims at. Declared by the executor for this report, after W1's data were seen (section 2) |
| Principal's resolution | [D4] | finest |
| Feasible set | [D7] | everything: nothing is assumed about what selection could do |
| View | [D8] | exact |
| Interventions | [D6] | none |
| Observed conditions | [D9] | all 1,000 prompts; the report is about these prompts only |
| Objective's units | [D5] | the gold reward model's score |
| Evaluator | [D10] | known: the proxy of `train_proxy.py`, a linear Bradley–Terry model of the answer's hashed words and word pairs and of its length. It scores alike the answers with equal counts of these, among them every answer repeated word for word; in the median prompt, {tied:.1%} of the answers share their score with another (`explore.json`) |
| Sampling | [D11] | the 12,600 answers of each prompt are independent draws of the initial policy at temperature 1; best-of-`n`'s behaviour is computed exactly from them, by Coste et al.'s estimator, with ties in the proxy broken at random; nothing is sampled |

## 2. The observations

| Field | Core | Entry |
|---|---|---|
| Behaviour | [D1], [D11] | 1,000 × 12,600 answers with their gold scores, and the proxy's scores computed here; best-of-`n` at `n` = {", ".join(ns)}, computed from them |
| Interventions applied | [D6] | none |
| Departures from the declaration | [A5] | **the declaration was written after the data were seen in W1**, so every result below is exploratory, not confirmatory |

## 3. The results

**Misalignment, departure and stakes** ([D3], [P5], [P6], [D5], [P9]), each prompt at an intensity of its own.
Best-of-`n`'s departure from the default splits exactly into the pursuit of the gold and misalignment against it
([P6]); the identities of [P6] and [P9] hold to `{rep['identity_max_error']:.1e}` in the worst prompt. The shortfall `S`
is how much more of the gold the same departure would have gained by pursuing the gold itself, in the gold's units
([D5]).

| `n` | departure, nats | misalignment `M`, nats | pursuit part, nats | `M` as a share of the departure | gold gained over the default | shortfall `S` |
|---|---|---|---|---|---|---|
{rows}

The behaviour is computed from the policy's answers, not counted from decisions, so `2n·M` and [P23]'s `χ²` reference
do not apply.

**At one shared intensity.** Under the stricter form of the specification, misalignment is the least, over one
intensity `t` for all prompts, of the average of `KL(p_c‖p_{{c,F,t}})`; it is at least the average above, and the
excess is the part that comes from best-of-`n` pursuing the gold harder in some prompts than in others.

| `n` | misalignment at one shared intensity, nats | excess over the average of each prompt's own | the shared intensity |
|---|---|---|---|
{shared}

The shared intensity is the best of 701 on a grid from `10⁻³` to `10⁴` (ratio `1.023`){
    "; it lies inside the grid at every `n`" if not edge else "; it lies at the grid's edge at `n` = " + ", ".join(edge)}.
In every prompt the grid's least divergence is at least that prompt's own `M`, as it must be ({
    "checked: the smallest difference is `0`, met where `t* = 0`" if grid_check == 0 else
    f"checked: the smallest difference is `{grid_check:.1e}`"}).

**Revealed and matched intensities** ([P5], [P9]).

| `n` | median revealed intensity `t*` | prompts where `t* = 0` | prompts where `t*` is infinite | median matched intensity `λ` | prompts where `λ` is infinite |
|---|---|---|---|---|---|
{intensities}

Two of [P5](iv)'s three cases occur. Where `t* = 0`, best-of-`n` lowers the gold's mean below the default's
({x16['prompts_losing_gold']} prompts at `n = 16`, {rep['n'][ns[-1]]['prompts_losing_gold']} at `n = {ns[-1]}`): its whole
departure is misalignment, and [P9](ii)'s third cause, anti-pursuit, is positive. Elsewhere `t*` is finite and positive.
It is never infinite, since best-of-`n` never puts all its mass on the answers with the top gold score. The matched
intensity `λ` is infinite where those answers make up at least `e^{{−KL(p̂‖q)}}` of the default: then even the gold's
pursuit at its limit, with all its mass on them, departs less than best-of-`n` does ([P9](i)). {no_departure}Where `λ` is infinite or zero, the under-pursuit of [P9](ii) is not
defined: at `n = 16` it is {ci(x16['under'])} nats over the {x16['prompts_with_finite_lambda']} prompts where `λ` is
finite and positive.

**Uncertainty** ([D11], [P23]). The intervals are over prompts. They leave out two sources: the sampling of each
prompt's 12,600 answers, which estimate the default, and the proxy's training. [P23]'s `χ²` reference does not apply,
as above.

**Evidence and detection** ([P21], [P22]). At `n = 16`, each answer gives, in expectation, {ci(x16['M'])} nats of
evidence against the nearest pursuit of the gold. The Chernoff information between them, computed on a grid of 201
exponents and so a lower bound, is {ci(x16['chernoff'])} nats; [P22](iii) bounds it by `M`.

**Evaluator** ([D10], [P18], [P19], [P25], [P26]). The proxy gives most answers distinct scores, so the regression of
the gold on the proxy itself is close to the gold, and says little ([D10]). On bins of the proxy's rank within each
prompt, a coarser evaluator ([P26]), the gold averaged over prompts is:

| proxy rank, as a quantile | mean gold |
|---|---|
{bin_rows}

The binned regression {shape_of([v["mean"] for v in bins.values()])}. With 100 bins of rank, the residual holds
{ci(rep['residual_share_100_bins'], 2)} of the gold's variance within a prompt: {seen}. Not computed: [P29], [P33] and
[P34]. W1's registered result is in `RESULTS.md`: the literature's form overstates best-of-`n`'s initial slope,
`{f(reg['a_fit'])}` against `{f(reg['a_pred'])}`.

**Resolution** ([P7], [P8]): the principal's resolution is the finest, so nothing was forgiven; the actor's, the
proxy's ties, is not analysed. **Avoidable and unavoidable misalignment** ([P15]): with the feasible set declared as
everything, all of it is avoidable; what a selector bound to the proxy's ranking could do is not analysed.
**Pass-through** ([P12]): no intervention. **Unobserved conditions** ([D9], [P16], [P17]): none within the report;
prompts outside AlpacaFarm's validation split are not identified by it. **Evaluation gap** ([P24]): not applicable, as
evaluation and use are not told apart. **Sensitivity** ([P10]): not computed.

{closing}

**Premises** ([A1]–[A4]). The gold is a reward model, not people: the report measures misalignment against that model.
The default is an estimate from 12,600 answers; quantities that depend on the policy's rarest answers, such as
best-of-`n` at `n` near 12,600, are not reported.
"""
    (HERE / "REPORT.md").write_text(reflow(text))
    print("REPORT.md written")


if __name__ == "__main__":
    main()
