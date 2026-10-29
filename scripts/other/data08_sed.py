"""DATA-08: NCSES SED 2022 figure 14 (parental education by race) -> CSV + B/W redraw."""
import csv, openpyxl
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-08"
ws = openpyxl.load_workbook(f"{D}/data/nsf24300-fig014.xlsx", read_only=True).worksheets[0]
rows = [r for r in ws.iter_rows(values_only=True) if isinstance(r[1], (int, float))]
with open(f"{D}/data/DATA-08.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["race_ethnicity", "pct_parent_bachelor_or_higher_2002", "pct_parent_bachelor_or_higher_2022"]); w.writerows(rows)
fig, ax = plt.subplots(figsize=(7, 4))
y = range(len(rows))
ax.barh([i + 0.2 for i in y], [r[1] for r in rows], 0.4, color="lightgrey", edgecolor="black", label="2002")
ax.barh([i - 0.2 for i in y], [r[2] for r in rows], 0.4, color="black", label="2022")
for i, r in enumerate(rows): ax.text(r[2] + 1, i - 0.2, f"{r[2]:.0f}%", va="center", fontsize=9)
ax.set_yticks(list(y), [r[0] for r in rows]); ax.invert_yaxis(); ax.set_xlim(0, 100)
ax.set_xlabel("% of US PhD recipients with a parent holding a bachelor's degree or higher", fontsize=8.5)
ax.legend(frameon=False, fontsize=9, loc="lower right"); [ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.008, "Source: NCSES, Doctorate Recipients from U.S. Universities: 2022 (NSF 24-300), figure 14 data (US citizens & permanent residents)", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{D}/figures/DATA-08_redraw.png", dpi=200)
