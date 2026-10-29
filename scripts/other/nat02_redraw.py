"""Line redraw for NAT-02 foreign share of recruits (black/grey)."""
import csv, sys
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
src, out = sys.argv[1:3]
rows = list(csv.DictReader(open(src)))
yrs = [int(r['year']) for r in rows]
fig, ax = plt.subplots(figsize=(8, 5))
for col, st, c in [('MCF', '-', '#222222'), ('PR', '-', '#888888'), ('PR not previously MCF', '--', '#555555')]:
    v = [float(r[col]) for r in rows]
    ax.plot(yrs, v, st, color=c, lw=2.2, marker='o', label=col)
    for x, y in [(yrs[0], v[0]), (yrs[-1], v[-1])]:
        ax.annotate(f'{y:.1f}%', (x, y), textcoords='offset points', xytext=(0, 7), ha='center', fontsize=9)
ax.set_ylim(0, 50); ax.set_xticks(yrs); ax.set_ylabel('% foreign nationals among recruits')
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=9, loc='upper right')
fig.suptitle('Foreign nationals among university faculty recruited, France 2020-2024', fontsize=12, x=0.01, ha='left')
fig.text(0.01, 0.01, 'Source: MESR-DGRH Note n°2-2026, graph 6 p.4 (2021-2023 digitised from the vector chart, +-0.2 pt). Excl. transfers.', fontsize=8, color='#444444')
fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(out, dpi=200); print(out)
