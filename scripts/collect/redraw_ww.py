"""Model-based redraw of Wenneras & Wold 1997 Fig.1 from Table 1 regression parameters (NOT the raw data points).
usage: python3 -I redraw_ww.py <params.csv> <out.png>"""
import sys, csv
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
p = {r["parameter"]: float(r["value"]) for r in csv.DictReader(open(sys.argv[1]))}
x = list(range(0, 151, 5))
f = [p["intercept_female"] + p["competence_per_impact_point"] * v for v in x]
m = [p["intercept_female"] + p["male_bonus_points"] + p["competence_per_impact_point"] * v for v in x]
fig, ax = plt.subplots(figsize=(6, 4), dpi=200)
ax.plot(x, m, "-", color="black", label="Men (model)")
ax.plot(x, f, "--", color="grey", label="Women (model)")
ax.annotate("", xy=(104, m[8]), xytext=(40, m[8]), arrowprops=dict(arrowstyle="<->", color="black"))
ax.text(72, m[8] + 0.015, "+64 impact points", ha="center", fontsize=8)
ax.set_xlabel("Total impact points"); ax.set_ylabel("Mean competence score (model)")
ax.set_title("Swedish MRC 1995: competence vs productivity\n(redrawn from Table 1 regression, Wennerås & Wold 1997)", fontsize=9)
ax.legend(frameon=False); fig.tight_layout(); fig.savefig(sys.argv[2]); print("saved", sys.argv[2])
