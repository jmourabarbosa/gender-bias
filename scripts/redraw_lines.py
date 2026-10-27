"""redraw_lines.py OUT.png JSONSPEC -- line chart, black/grey. spec: {"x":[...], "series":{"name":[...]}, "ylabel":..., "ylim":[..], "ref":50, "labels":true}"""
import sys, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
out, spec = sys.argv[1], json.loads(sys.argv[2])
styles = [dict(color='black', ls='-', marker='o'), dict(color='#777777', ls='--', marker='s'), dict(color='#aaaaaa', ls='-.', marker='^'), dict(color='#444444', ls=':', marker='D')]
fig, ax = plt.subplots(figsize=spec.get('size', (6, 4)), dpi=200)
for k, (name, ys) in enumerate(spec['series'].items()):
    xs = spec['xs'][name] if 'xs' in spec else spec['x']
    pts = [(a, b) for a, b in zip(xs, ys) if b is not None]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], label=name, lw=1.6, ms=4, **styles[k % 4])
    if spec.get('labels'):
        for a, b in pts: ax.annotate(f'{b:g}', (a, b), textcoords='offset points', xytext=(0, 6), ha='center', fontsize=7)
if 'ref' in spec: ax.axhline(spec['ref'], color='black', lw=0.7, ls='--')
ax.set_ylabel(spec.get('ylabel', '')); ax.set_xlabel(spec.get('xlabel', '')); ax.set_ylim(*spec.get('ylim', (0, 100)))
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=8, loc=spec.get('legend_loc', 'best'))
fig.tight_layout(); fig.savefig(out)
