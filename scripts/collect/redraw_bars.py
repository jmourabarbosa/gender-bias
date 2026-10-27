"""Simple grey bar redraw: python3 -I redraw_bars.py <csv> <labelcol> <valcol> <ylabel> <title> <out.png>"""
import sys, csv
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
src, lc, vc, yl, title, out = sys.argv[1:7]
rows = list(csv.DictReader(open(src, encoding="utf-8-sig")))
fig, ax = plt.subplots(figsize=(6, 4), dpi=200)
cols = ["black", "grey", "lightgrey", "dimgrey"]
v = [float(r[vc]) for r in rows]
b = ax.bar(range(len(rows)), v, color=[cols[i % 4] for i in range(len(rows))], edgecolor="black")
ax.bar_label(b, fmt="%g")
ax.set_xticks(range(len(rows)), [r[lc] for r in rows], fontsize=8)
ax.set_ylabel(yl); ax.set_title(title, fontsize=10)
fig.tight_layout(); fig.savefig(out); print("saved", out)
