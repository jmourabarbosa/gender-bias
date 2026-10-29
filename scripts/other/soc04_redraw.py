import csv
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-04'
rows = list(csv.DictReader(open(f'{D}/data/SOC-04.csv')))
lab = ['Two\nmanagers', 'Other\nmanager', 'Inter-\nmediate', 'Clerical', 'Self-\nemployed', 'Manual\nworker', 'Single earner\nclerical/manual', 'Inactive', 'All']
fig, ax = plt.subplots(figsize=(9, 4.6)); wd = 0.27
for off, k, col, nm in ((-wd, 'non_diplomes_pct', 'white', 'No diploma'), (0, 'diplomes_superieur_court_pct', '0.65', 'Short higher ed (up to bac+4)'), (wd, 'diplomes_superieur_long_pct', '0.15', 'Long higher ed (bac+5 and above)')):
    v = [float(r[k]) for r in rows]
    ax.bar([i + off for i in range(len(rows))], v, wd, color=col, edgecolor='black', label=nm)
    for i, x in enumerate(v): ax.text(i + off, x + 0.8, f'{x:.0f}', ha='center', fontsize=7.5)
ax.set_xticks(range(len(rows))); ax.set_xticklabels(lab, fontsize=8.5); ax.set_ylim(0, 62)
ax.set_ylabel('% of school leavers (2017 cohort)'); ax.legend(frameon=False, fontsize=8.5)
ax.set_title("Highest qualification by parents' occupation, French school leavers of 2017", fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Céreq Bref n°452 (2024), figure 2 p. 2, enquête Génération 2017 (2020 survey)', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-04_redraw.png', dpi=200)
