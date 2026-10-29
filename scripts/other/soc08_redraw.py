import csv
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-08'
rows = [r for r in csv.DictReader(open(f'{D}/data/SOC-08.csv')) if r['year']]
rows.sort(key=lambda r: float(r['pct_independent']))
fig, ax = plt.subplots(figsize=(7.5, 4.5))
v = [float(r['pct_independent']) for r in rows]
ax.barh(range(len(rows)), v, color=['black' if r['group'].startswith('Scientists') else '0.65' for r in rows])
ax.set_yticks(range(len(rows))); ax.set_yticklabels([f"{r['group']} ({r['year']})" for r in rows], fontsize=9)
for i, x in enumerate(v): ax.text(x + 1, i, f'{x:.0f}%', va='center', fontsize=9)
ax.axvline(7, color='0.3', ls='--', lw=1); ax.set_ylim(-0.6, len(rows) + 0.2); ax.text(7.8, len(rows) - 0.45, '7% of pupils attend independent schools', fontsize=8, color='0.3')
ax.set_xlim(0, 80); ax.set_xlabel('% privately (independently) educated')
ax.set_title('UK elites educated at independent schools', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Sutton Trust (2009), The Educational Backgrounds of Leading Scientists and Scholars, Table 3 p. 8', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-08_redraw.png', dpi=200)
