"""Stacked 100% bars (greyscale). usage: python3 -I redraw_stacked.py <csv> <labelcol> <col1,col2,..> <names> <title> <out>"""
import sys, csv
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
src, lc, cols, names, title, out = sys.argv[1:7]
cols = cols.split(","); names = names.split(",")
rows = list(csv.DictReader(open(src, encoding="utf-8-sig")))
fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
shades = ["black", "grey", "lightgrey", "white"]
left = [0.0] * len(rows)
for c, n, s in zip(cols, names, shades):
    v = [float(r[c]) for r in rows]
    b = ax.barh([r[lc] for r in rows], v, left=left, color=s, edgecolor="black", label=n)
    for i, (l, x) in enumerate(zip(left, v)):
        if x >= 5: ax.text(l + x / 2, i, f"{x:g}%", ha="center", va="center", color="white" if s in ("black", "grey") else "black", fontsize=8)
    left = [l + x for l, x in zip(left, v)]
ax.set_xlim(0, 100); ax.set_xlabel("% of letters"); ax.set_title(title, fontsize=10)
ax.legend(frameon=False, ncol=len(cols), loc="upper center", bbox_to_anchor=(0.5, -0.25))
fig.tight_layout(); fig.savefig(out); print("saved", out)
