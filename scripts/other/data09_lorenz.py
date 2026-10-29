"""DATA-09: Lorenz curve of faculty production (US-trained faculty), academia-wide, from Larremore lab edge lists."""
import csv, collections, sys
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-09"
E = f"{D}/data/us-faculty-hiring-networks-v2026.08/data/edge-lists.csv"
prod, employers = collections.Counter(), set()
for r in csv.DictReader(open(E)):
    if r["TaxonomyLevel"] != "Academia": continue
    employers.add(r["InstitutionId"]); prod[r["DegreeInstitutionId"]] += int(r["Total"])
# US PhD-granting institutions = employing institutions in the sample (non-US degree institutions only appear as degree sources)
us = {k: prod.get(k, 0) for k in employers}
vals = sorted(us.values(), reverse=True); tot = sum(vals); n = len(vals)
rows, cum = [], 0
for i, v in enumerate(vals, 1):
    cum += v; rows.append((i / n, cum / tot))
with open(f"{D}/data/DATA-09_lorenz_academia.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["share_of_institutions_top_first", "share_of_US_trained_faculty"]); w.writerows([(round(a, 5), round(b, 5)) for a, b in rows])
x80 = next(a for a, b in rows if b >= 0.8)
print("institutions", n, "faculty", tot, "share of institutions producing 80%:", round(x80, 4))
fig, ax = plt.subplots(figsize=(6.2, 5))
ax.plot([0] + [a for a, _ in rows], [0] + [b for _, b in rows], color="black", lw=2, label="Observed")
ax.plot([0, 1], [0, 1], color="grey", ls="--", lw=1, label="Equal production")
ax.axvline(x80, color="grey", lw=0.8); ax.axhline(0.8, color="grey", lw=0.8)
ax.annotate(f"{x80*100:.0f}% of universities\ntrained 80% of faculty", (x80, 0.8), xytext=(x80 + 0.1, 0.55),
            arrowprops=dict(arrowstyle="->", color="black"), fontsize=11)
ax.set_xlabel("Share of US PhD-granting universities (most productive first)", fontsize=11)
ax.set_ylabel("Cumulative share of US-trained faculty", fontsize=11)
ax.set_xlim(0, 1); ax.set_ylim(0, 1.01); ax.legend(frameon=False, loc="lower right")
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, "Source: Wapman et al. 2022 data, Zenodo 10.5281/zenodo.6941650 (v2026.08), edge-lists.csv, Academia level; our computation",
         fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f"{D}/figures/DATA-09_redraw.png", dpi=200)
