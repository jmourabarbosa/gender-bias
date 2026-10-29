"""redraw.py CSV OUT.png TITLE YLABEL SOURCE [--cols c1,c2] [--cat col] [--filter col=val] [--horizontal] [--fmt {:.1f}]
Grouped bar chart, black/white/grey only. CSV: one category column + numeric series columns."""
import sys, csv, argparse
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
ap = argparse.ArgumentParser()
ap.add_argument('csv'); ap.add_argument('out'); ap.add_argument('title'); ap.add_argument('ylabel'); ap.add_argument('source')
ap.add_argument('--cols'); ap.add_argument('--cat'); ap.add_argument('--filter', action='append', default=[])
ap.add_argument('--horizontal', action='store_true'); ap.add_argument('--fmt', default='{:.1f}')
ap.add_argument('--labels', help='display names for series, comma-separated'); ap.add_argument('--ymax', type=float)
a = ap.parse_args()
rows = list(csv.DictReader(open(a.csv, encoding='utf-8')))
for f in a.filter:
    k, v = f.split('='); rows = [r for r in rows if r[k] == v]
cat = a.cat or list(rows[0].keys())[0]
cols = a.cols.split(',') if a.cols else [c for c in rows[0] if c != cat]
labels = a.labels.split(',') if a.labels else cols
cats = [r[cat] for r in rows]
greys = ['#222222', '#888888', '#cccccc', '#555555', '#aaaaaa', '#eeeeee']
hatches = ['', '', '', '//', '\\\\', '..']
n = len(cols); w = 0.8 / n
fig, ax = plt.subplots(figsize=(max(7, 1.1 * len(cats) * max(1, n / 2) + 2), 5) if not a.horizontal else (9, max(4, 0.5 * len(cats) * n + 1.5)))
for i, c in enumerate(cols):
    vals = [float(r[c]) if r[c] not in ('', 'NA') else 0 for r in rows]
    pos = [j + (i - (n - 1) / 2) * w for j in range(len(cats))]
    kw = dict(color=greys[i % 6], edgecolor='black', hatch=hatches[i % 6], label=labels[i])
    bars = ax.barh(pos, vals, height=w, **kw) if a.horizontal else ax.bar(pos, vals, width=w, **kw)
    for b, v in zip(bars, vals):
        if a.horizontal: ax.text(b.get_width(), b.get_y() + b.get_height() / 2, ' ' + a.fmt.format(v), va='center', fontsize=9)
        else: ax.text(b.get_x() + b.get_width() / 2, b.get_height(), a.fmt.format(v), ha='center', va='bottom', fontsize=9)
if a.horizontal:
    ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats, fontsize=10); ax.invert_yaxis(); ax.set_xlabel(a.ylabel)
    if a.ymax: ax.set_xlim(0, a.ymax)
else:
    ml = max(len(l) for c in cats for l in c.split('\n')); short = ml < 14 or any('\n' in c for c in cats)
    ax.set_xticks(range(len(cats))); ax.set_xticklabels(cats, fontsize=10 if ml < 24 else 9, rotation=0 if short else 20, ha='center' if short else 'right')
    ax.set_ylabel(a.ylabel)
    if a.ymax: ax.set_ylim(0, a.ymax)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.suptitle(a.title, fontsize=12, x=0.01, ha='left')
if n > 1: ax.legend(frameon=False, fontsize=9)
fig.text(0.01, 0.01, a.source, fontsize=8, color='#444444', ha='left', va='bottom')
fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(a.out, dpi=200); print(a.out)
