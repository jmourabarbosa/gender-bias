"""Write data/<ID>.csv and figures/<ID>_redraw.png (black/white/grey) for sources whose
numbers are reported in text/tables but lack a usable figure. Run: python3 -I redraw.py"""
import csv, os, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/user/gender-bias/gender-bias-data"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
K, G1, G2 = "#000000", "#7f7f7f", "#c8c8c8"

def save(sec, id_, header, rows, fig, source):
    d = f"{ROOT}/{sec}/{id_}"
    os.makedirs(f"{d}/data", exist_ok=True); os.makedirs(f"{d}/figures", exist_ok=True)
    with open(f"{d}/data/{id_}.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(header + ["source"]); [w.writerow(list(r) + [source]) for r in rows]
    txt = textwrap.fill("Source: " + source, 110)
    fig.text(0.01, 0.01, txt, fontsize=6.5, color="#555555", va="bottom")
    fig.tight_layout(rect=(0, 0.04 * (txt.count("\n") + 1), 1, 1)); fig.savefig(f"{d}/figures/{id_}_redraw.png", dpi=300); plt.close(fig)

def bars(ax, labels, vals, colors, fmt="{:.0f}", errs=None):
    b = ax.bar(labels, vals, color=colors, edgecolor=K, yerr=errs, capsize=4 if errs else 0)
    for r, v in zip(b, vals):
        ax.text(r.get_x() + r.get_width() / 2, v, fmt.format(v), ha="center",
                va="bottom" if v >= 0 else "top", fontsize=10)
    return b

# PAY-02 UCEA
fig, ax = plt.subplots(figsize=(5, 4))
bars(ax, ["UK higher education\n(UCEA, 107 HEIs)", "UK whole economy\n(2024)"], [11.5, 13.1], [G1, G2], "{:.1f}%")
ax.set_ylabel("Median gender pay gap (%)"); ax.set_title("Median gender pay gap, 2023-24")
save("06-pay", "PAY-02", ["group", "median_gender_pay_gap_pct"], [["UK HE (UCEA members)", 11.5], ["UK whole economy 2024", 13.1]],
     fig, "UCEA, Intersectional Pay Gaps in HE 2023-24, key findings on report landing page")

# PAY-07 Sege et al.
fig, ax = plt.subplots(figsize=(5, 4))
bars(ax, ["Men (n=127)", "Women (n=92)"], [889, 350], [G1, G2], "${:.0f}k")
ax.set_ylabel("Median start-up support ($ thousands)"); ax.set_title("Institutional start-up support, junior\nbiomedical researchers, New England 2012-14")
save("06-pay", "PAY-07", ["group", "median_startup_usd_thousands", "share_over_1M_pct"], [["men", 889, 40], ["women", 350, 12]],
     fig, "Sege, Nykiel-Bub & Selk 2015 JAMA 314(11):1175 as reported in JAMA Network press release (EurekAlert 676536)")

# TEACH-01 MacNell
fig, ax = plt.subplots(figsize=(5, 4))
bars(ax, ["Perceived male", "Perceived female"], [4.35, 3.55], [G1, G2], "{:.2f}")
ax.set_ylim(0, 5); ax.set_ylabel("Mean 'promptness' rating (1-5)"); ax.set_title("Same grading turnaround, different rating")
save("07-teaching", "TEACH-01", ["perceived_instructor_gender", "promptness_mean"], [["male", 4.35], ["female", 3.55]],
     fig, "MacNell et al. 2015 via NC State press release 2014-12; full 2x2 (perceived x actual) cell means need the paywalled paper")

# TEACH-04 Guarino & Borden, Table 6 (FSSE 2014)
fig, ax = plt.subplots(figsize=(5.5, 4))
lab = ["Female\n(vs male)", "Associate\n(vs assistant)", "Full\n(vs assistant)"]
v = [0.6, 3.84, 2.45]; se = [0.22, 0.26, 0.19]
bars(ax, lab, v, [K, G1, G2], "+{:.2f} h", [1.96 * s for s in se])
ax.set_ylabel("Extra service hours per week"); ax.set_title("Service hours/week: regression coefficients\n(FSSE 2014, N=6,727, institution FE)")
save("07-teaching", "TEACH-04", ["variable", "coef_hours_per_week", "se"], list(zip(["female", "associate", "full"], v, se)),
     fig, "Guarino & Borden, IZA DP 10010 (2016) Table 6, p.16; error bars 95% CI")

# TEACH-05 Babcock et al. Experiment 3
fig, ax = plt.subplots(figsize=(5.5, 4))
x = [0, 1, 3, 4]
ax.bar(x, [14, 14, 51, 76], color=[G1, G2, G1, G2], edgecolor=K)
for xi, vi in zip(x, [14, 14, 51, 76]): ax.text(xi, vi, f"{vi}%", ha="center", va="bottom")
ax.set_xticks([0.5, 3.5]); ax.set_xticklabels(["Not asked", "Asked to volunteer"])
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, fc=G1, ec=K), plt.Rectangle((0, 0), 1, 1, fc=G2, ec=K)], labels=["Men", "Women"], frameon=False)
ax.set_ylabel("Investment (volunteering) rate, %"); ax.set_title("Accepting a request to do a\nlow-promotability task (Experiment 3)")
save("07-teaching", "TEACH-05", ["condition", "gender", "invest_rate_pct"], [["not asked", "men", 14], ["not asked", "women", 14], ["asked", "men", 51], ["asked", "women", 76]],
     fig, "Babcock, Recalde, Vesterlund & Weingart 2017 AER 107(3) p.733 (text, Experiment 3)")

# TEACH-06 Misra et al. associate professors
fig, ax = plt.subplots(figsize=(5, 4.5))
cats = ["Men", "Women"]; res = [37, 25]; srv = [20, 27]; oth = [100 - a - b for a, b in zip(res, srv)]
ax.bar(cats, res, color=K, edgecolor=K, label="Research")
ax.bar(cats, srv, bottom=res, color=G1, edgecolor=K, label="Service")
ax.bar(cats, oth, bottom=[a + b for a, b in zip(res, srv)], color="white", edgecolor=K, label="Teaching + mentoring (remainder)")
for i in range(2):
    ax.text(i, res[i] / 2, f"{res[i]}%", ha="center", va="center", color="white")
    ax.text(i, res[i] + srv[i] / 2, f"{srv[i]}%", ha="center", va="center")
ax.set_ylabel("Share of work time (%)"); ax.set_title("Associate professors' time use, UMass Amherst")
ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=3)
save("07-teaching", "TEACH-06", ["gender", "research_pct", "service_pct", "teaching_mentoring_remainder_pct"], list(zip(cats, res, srv, oth)),
     fig, "Misra et al. 2011, Academe 97(1) p.2 of AAUP web version; remainder computed, not reported")

# INT-04 Tomkins et al. odds multipliers (forest plot)
names = ["Top company", "Famous author", "Top university", "Woman author", "Same country", "Academic", "USA"]
coef = [0.74, 0.49, 0.46, -0.25, 0.14, 0.06, 0.01]
lo = [0.27, 0.05, 0.09, -0.60, -0.34, -0.38, -0.42]; hi = [1.21, 0.93, 0.83, 0.10, 0.62, 0.51, 0.44]
import math
fig, ax = plt.subplots(figsize=(6, 4))
for i, (n, c, l, h) in enumerate(zip(names, coef, lo, hi)):
    y = len(names) - i
    ax.plot([math.exp(l), math.exp(h)], [y, y], color=K); ax.plot(math.exp(c), y, "s", color=K if l > 0 or h < 0 else G1)
    ax.text(math.exp(hi[0]) * 1.12, y, f"{math.exp(c):.2f}", va="center", fontsize=9)
ax.axvline(1, color=G1, ls="--"); ax.set_xscale("log"); ax.set_yticks(range(len(names), 0, -1)); ax.set_yticklabels(names)
ax.set_xlabel("Odds multiplier, single- vs double-blind reviewers (95% CI)"); ax.set_title("WSDM 2017: who benefits when reviewers see authors")
save("09-interventions", "INT-04", ["feature", "coef", "ci_low", "ci_high", "odds_multiplier"],
     [[n, c, l, h, round(math.exp(c), 2)] for n, c, l, h in zip(names, coef, lo, hi)],
     fig, "Tomkins, Zhang & Heavlin 2017, arXiv:1702.00502v6 Table 5 (review score model)")

# INT-02 Pallesen: p-values
fig, ax = plt.subplots(figsize=(5, 4))
bars(ax, ["Reported\n(nominal)", "Bonferroni-\ncorrected (8 tests)"], [0.042, 0.33], [G1, G2], "p = {:.3f}")
ax.axhline(0.05, color=K, ls="--"); ax.text(1.45, 0.055, "0.05", fontsize=9)
ax.set_ylabel("p-value"); ax.set_title("Goldin & Rouse Table 5: the one\n'significant' blind-audition result")
save("09-interventions", "INT-02", ["p_value_type", "p_value"], [["nominal", 0.042], ["bonferroni_8_tests", 0.33]],
     fig, "Pallesen 2019, 'Orchestrating false beliefs about gender discrimination' (Medium, gwern.net mirror)")

# INT-07 Antecol et al. (IZA DP 9904 Table 3)
fig, ax = plt.subplots(figsize=(5, 4))
bars(ax, ["Men", "Women"], [19.4, -22.4], [G1, G2], "{:+.1f} pp", [1.96 * 8.6, 1.96 * 10.3])
ax.axhline(0, color=K, lw=0.8); ax.set_ylabel("Change in P(tenure at first job), pp")
ax.set_title("Gender-neutral tenure clock stopping\n(top-50 US economics departments)")
save("09-interventions", "INT-07", ["group", "effect_pp", "se_pp"], [["men", 19.4, 8.6], ["women", -22.4, 10.3]],
     fig, "Antecol, Bedard & Stearns, IZA DP 9904 (2016) Table 3 col.1; AER 2018 published values differ (+17/-19 pp)")

# INT-08 Carnes et al. Table 3
outs = ["Personal bias awareness", "Internal motivation", "External motivation", "GE self-efficacy", "Positive outcome exp.", "Action"]
d3 = [0.36, 0.29, 0.08, 0.17, 0.17, -0.06]; m3 = [0.48, 0.27, 0.49, 0.20, 0.10, 0.13]
fig, ax = plt.subplots(figsize=(7, 4))
xs = range(len(outs))
ax.bar([x - 0.2 for x in xs], d3, 0.4, color=G2, edgecolor=K, label="3 days")
ax.bar([x + 0.2 for x in xs], m3, 0.4, color=G1, edgecolor=K, label="3 months")
ax.axhline(0, color=K, lw=0.8); ax.set_xticks(list(xs)); ax.set_xticklabels(outs, rotation=25, ha="right", fontsize=9)
ax.set_ylabel("Experimental - control change\nvs baseline (scale units)"); ax.legend(frameon=False)
ax.set_title("Gender-bias habit-breaking workshop (cluster RCT, 92 depts)")
save("09-interventions", "INT-08", ["outcome", "diff_3day", "diff_3month"], list(zip(outs, d3, m3)),
     fig, "Carnes et al. 2015 Acad Med 90(2) Table 3 (adjusted for gender and rank)")

# INT-09 Devine et al.
fig, ax = plt.subplots(figsize=(5.5, 4))
x = [0, 1, 3, 4]; v = [33, 32, 32, 47]
ax.bar(x, v, color=[G2, G1, G2, G1], edgecolor=K)
for xi, vi in zip(x, v): ax.text(xi, vi, f"{vi}%", ha="center", va="bottom")
ax.set_xticks([0.5, 3.5]); ax.set_xticklabels(["Before intervention", "After intervention"])
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, fc=G2, ec=K), plt.Rectangle((0, 0), 1, 1, fc=G1, ec=K)], labels=["Control depts", "Intervention depts"], frameon=False)
ax.set_ylabel("Women among new faculty hires (%)"); ax.set_title("Hiring after habit-breaking workshop")
save("09-interventions", "INT-09", ["period", "arm", "pct_women_hires", "n_hires"],
     [["pre", "control", 33, 109], ["pre", "intervention", 32, 85], ["post", "control", 32, 113], ["post", "intervention", 47, 101]],
     fig, "Devine et al. 2017 JESP 73:211, OSF preprint p.6 (descriptive hiring rates)")
print("done")
