import csv
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/01-localism/LOC-06'
rows = list(csv.DictReader(open(f'{D}/data/LOC-06.csv')))
rows.sort(key=lambda r: float(r['mh_odds_ratio_digitized']))
fig, ax = plt.subplots(figsize=(7.5, 10))
for i, r in enumerate(rows):
    o, lo, hi = (float(r[k]) for k in ('mh_odds_ratio_digitized', 'ci_low_digitized', 'ci_high_digitized'))
    ax.plot([lo, hi], [i, i], color='0.6', lw=1.2)
    ax.plot(o, i, 'o', color='black', ms=4)
ax.set_xscale('log'); ax.set_xticks([0.5, 1, 2, 5, 10, 20, 50]); ax.set_xticklabels(['0.5', '1', '2', '5', '10', '20', '50'])
ax.axvline(1, color='0.4', ls=':', lw=1); ax.axvline(9.5, color='black', ls='--', lw=1)
ax.text(9.7, len(rows) - 0.3, 'all sections: 9.5', fontsize=8)
ax.text(1.05, -1.2, 'no preference', fontsize=8, color='0.3')
ax.set_yticks(range(len(rows))); ax.set_yticklabels([f"{r['cnu_section']}. {r['section_label']}" for r in rows], fontsize=7.5)
ax.set_ylim(-2, len(rows))
ax.set_xlabel('Odds that a local candidate is hired vs an external one\n(Mantel-Haenszel odds ratio, 95% CI, log scale)')
ax.set_title('Local preference in MCF hiring by CNU section, France 2017-2024', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.005, 'Source: Godechot, Issiakou, Renisio & Rougier (2025), La Vie des idées, fig. 1 p. 15 (values read from the vector figure)', fontsize=7)
fig.tight_layout(rect=(0, 0.015, 1, 1)); fig.savefig(f'{D}/figures/LOC-06_redraw.png', dpi=200)
