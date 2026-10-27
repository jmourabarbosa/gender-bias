"""Black/grey redraws for funding series. usage: python3 -I redraw.py <which> <in.csv> <out.png>"""
import sys, csv
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
which, src, out = sys.argv[1:4]
rows = list(csv.DictReader(open(src, encoding="utf-8-sig")))
fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
for s in ax.spines.values(): s.set_color("black")
if which == "erc":
    for sch, st, mk in [("StG", "-", "o"), ("AdG", "--", "s")]:
        r = [x for x in rows if x["scheme"] == sch]
        ax.plot([int(x["call_year"]) for x in r], [float(x["women_share_of_grantees_pct"]) for x in r],
                st, marker=mk, color="black" if sch == "StG" else "grey", label=f"{sch} (women % of grantees)")
    ax.set_ylabel("Women among grantees (%)"); ax.set_xlabel("Call year"); ax.set_ylim(0, 50)
    ax.set_title("ERC: women's share of Starting vs Advanced Grant grantees")
elif which == "nih":
    for ds, st, c in [("Female Applicants", "-", "black"), ("Male Applicants", "--", "grey")]:
        r = [x for x in rows if x["dataset"] == ds]
        ax.plot([int(x["Year"]) for x in r], [float(x["Success Rate"]) for x in r], st, color=c, label=ds.replace(" Applicants", ""))
    ax.set_ylabel("Success rate (%)"); ax.set_xlabel("Fiscal year"); ax.set_ylim(0, 40)
    ax.set_title("NIH research project grants: success rate by sex")
elif which == "wellcome":
    lab = [x["period"] for x in rows]; import numpy as np; i = np.arange(len(rows))
    ax.bar(i - 0.2, [float(x["men_pct"]) for x in rows], 0.4, color="grey", label="Men")
    ax.bar(i + 0.2, [float(x["women_pct"]) for x in rows], 0.4, color="black", label="Women")
    ax.set_xticks(i, lab); ax.set_ylabel("Success rate (%)"); ax.set_title("Wellcome: applicant success rate by gender")
from matplotlib.ticker import MaxNLocator
if which != "wellcome": ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.legend(frameon=False); fig.tight_layout(); fig.savefig(out); print("saved", out)
