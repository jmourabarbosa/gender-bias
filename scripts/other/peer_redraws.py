"""Black/white/grey redraws for 09-peer sources from their data/<ID>.csv files."""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = "/home/user/gender-bias/other-biases-data/09-peer"


def finish(fig, ax, src, out):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.text(0.01, 0.008, src, fontsize=7, color="dimgrey")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(out, dpi=200)
    plt.close(fig)


# PEER-01: 2x2 decision table as a heat-table
rows = list(csv.reader(open(f"{R}/PEER-01/data/PEER-01.csv")))
m = [[int(rows[1][1]), int(rows[1][2])], [int(rows[2][1]), int(rows[2][2])]]
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.imshow([[1, 0], [0, 1]], cmap="Greys", vmin=-1.5, vmax=2.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, f"{m[i][j]}", ha="center", va="center", fontsize=22, color="white" if i == j else "black", weight="bold")
ax.set_xticks([0, 1], ["Accepted", "Rejected / withdrawn"], fontsize=11)
ax.set_yticks([0, 1], ["Accepted", "Rejected /\nwithdrawn"], fontsize=11)
ax.set_xlabel("Committee B (copy)", fontsize=11)
ax.set_ylabel("Committee A (original)", fontsize=11)
ax.xaxis.set_label_position("top"); ax.xaxis.tick_top()
ax.set_title("NeurIPS 2021: 882 papers reviewed twice\n203 (23%) inconsistent decisions\n107/206 and 96/195 accepted papers rejected by the other committee (50.6% on average)",
             fontsize=8.5, y=-0.28)
for s in ax.spines.values():
    s.set_visible(False)
fig.text(0.01, 0.008, "Source: Beygelzimer et al. 2023, arXiv:2306.03262, Table 1 (aggregated: oral+spotlight+poster = accepted)", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{R}/PEER-01/figures/PEER-01_redraw.png", dpi=200); plt.close(fig)

# PEER-07: Mahoney summary recommendation by condition
rows = list(csv.DictReader(open(f"{R}/PEER-07/data/PEER-07.csv")))
r = next(x for x in rows if x["rating"] == "Summary recommendation")
labels = ["Positive\nresults", "Negative\nresults", "No results", "Mixed,\npositive disc.", "Mixed,\nnegative disc."]
vals = [float(r[k]) for k in list(r)[1:]]
fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.bar(labels, vals, color=["black", "grey", "lightgrey", "grey", "grey"], edgecolor="black")
for i, v in enumerate(vals):
    ax.text(i, v + 0.08, f"{v:.1f}", ha="center", fontsize=11)
ax.set_ylim(0, 6); ax.set_ylabel("Mean summary recommendation\n(0 = reject … 6 = accept)", fontsize=10)
ax.set_title("Identical manuscript, only the results changed (n = 67 reviewers)", fontsize=10)
finish(fig, ax, "Source: Mahoney 1977, Cognitive Therapy and Research 1(2):161-175, Table I", f"{R}/PEER-07/figures/PEER-07_redraw.png")

# PEER-10: SNSF junior fellowships, decision groups by panel
rows = list(csv.DictReader(open(f"{R}/PEER-10/data/PEER-10.csv")))
fig, ax = plt.subplots(figsize=(7, 3.8))
y = range(len(rows))
a = [int(x["funded_outright"]) for x in rows]; b = [int(x["random_selection_group"]) for x in rows]; c = [int(x["rejected"]) for x in rows]
ax.barh(y, a, color="black", label="Funded (above the line)")
ax.barh(y, b, left=a, color="white", edgecolor="black", hatch="///", label="Draw zone (lottery)")
ax.barh(y, c, left=[i + j for i, j in zip(a, b)], color="lightgrey", edgecolor="black", label="Rejected")
ax.set_yticks(list(y), [x["panel"] for x in rows]); ax.invert_yaxis()
ax.set_xlabel("Proposals discussed by the panel", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="lower right")
ax.set_title("SNSF junior fellowships, Feb. 2020 call\n8 of 79 discussed proposals (181 submitted) went to the lottery", fontsize=9)
finish(fig, ax, "Source: Heyard, Ott, Salanti & Egger 2022, arXiv:2102.09958, Table 1 and Figure 2", f"{R}/PEER-10/figures/PEER-10_redraw.png")

# PEER-13: CNU qualification rate by discipline group (MCF)
rows = [x for x in csv.DictReader(open(f"{R}/PEER-13/data/PEER-13.csv")) if x["groupe"] != "Théologie"]
rows.sort(key=lambda x: float(x["mcf_taux_pct"]))
fig, ax = plt.subplots(figsize=(7.5, 5.6))
lab = [x["groupe"].replace("Groupe ", "G").replace(", génies mécanique et informatique", ", génies") for x in rows]
v = [float(x["mcf_taux_pct"]) for x in rows]
ax.barh(lab, v, color=["black" if x["groupe"] == "Ensemble" else "grey" for x in rows])
for i, t in enumerate(v):
    ax.text(t + 0.8, i, f"{t:.1f}%".replace(".", ","), va="center", fontsize=9)
ax.set_xlim(0, 100); ax.set_xlabel("Qualifications délivrées / dossiers examinés, MCF (%)", fontsize=10)
ax.set_title("Qualification CNU 2024 (provisoire) : taux par groupe disciplinaire", fontsize=10.5)
finish(fig, ax, "Source: MESR-DGRH A1-1, Bilan provisoire de la campagne de qualification 2024 (juillet 2024), figure 3, p. 3", f"{R}/PEER-13/figures/PEER-13_redraw.png")
print("done")
