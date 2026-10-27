"""redraw_bars.py OUT.png JSONSPEC  -- grouped bar chart in black/white/grey.
spec: {"categories":[...], "series":{"name":[values...]}, "ylabel":"...", "ylim":[0,100], "ref":50}"""
import sys, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np
out, spec = sys.argv[1], json.loads(sys.argv[2])
cats, series = spec['categories'], spec['series']
greys = ['#222222', '#888888', '#cccccc', '#555555', '#aaaaaa']
x = np.arange(len(cats)); w = 0.8 / len(series)
fig, ax = plt.subplots(figsize=spec.get('size', (6, 4)), dpi=200)
for k, (name, vals) in enumerate(series.items()):
    b = ax.bar(x + (k - (len(series) - 1) / 2) * w, vals, w, label=name, color=greys[k % 5], edgecolor='black', linewidth=0.6)
    ax.bar_label(b, fmt=spec.get('fmt', '%.1f'), fontsize=8, padding=2)
if 'ref' in spec: ax.axhline(spec['ref'], color='black', lw=0.8, ls='--')
ax.set_xticks(x, cats); ax.set_ylabel(spec.get('ylabel', '')); ax.set_ylim(*spec.get('ylim', (0, 100)))
for s in ('top', 'right'): ax.spines[s].set_visible(False)
if len(series) > 1: ax.legend(frameon=False, fontsize=9)
fig.tight_layout(); fig.savefig(out)
