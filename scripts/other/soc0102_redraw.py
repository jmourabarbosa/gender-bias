import csv
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
R = '/home/user/gender-bias/other-biases-data/02-social'
def style(ax):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
# SOC-01
rows = {r['origine_sociale']: r for r in csv.DictReader(open(f'{R}/SOC-01/data/SOC-01.csv'))}
lv = ['Licence', 'Master', 'Doctorat']
fig, ax = plt.subplots(figsize=(7.5, 4.6)); wd = 0.36
for off, key, col, lab in ((-wd / 2, 'Cadres supérieurs', '0.2', 'Senior managers & professionals'), (wd / 2, 'Ouvriers', '0.8', 'Manual workers')):
    vals = [float(rows[key][l]) for l in lv]
    ax.bar([i + off for i in range(3)], vals, wd, color=col, edgecolor='black', label=lab)
    for i, v in enumerate(vals): ax.text(i + off, v + 0.8, f'{v:.1f}', ha='center', fontsize=9)
ax.set_xticks(range(3)); ax.set_xticklabels(lv); ax.set_ylim(0, 50); ax.set_ylabel('% of university students')
ax.legend(frameon=False, loc='upper left', fontsize=9); style(ax)
ax.set_title("Parents' occupation of French university students by level, 2019-20", fontsize=11)
fig.text(0.01, 0.01, 'Source: Observatoire des inégalités, from MESRI data 2019-2020 (inegalites.fr)', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{R}/SOC-01/figures/SOC-01_redraw.png', dpi=200); plt.close(fig)
# SOC-02
rows = list(csv.DictReader(open(f'{R}/SOC-02/data/SOC-02.csv')))
fil = ['Université', 'BTS', 'Classes préparatoires aux grandes écoles', 'Écoles normales supérieures']
lab = ['University', 'BTS', 'CPGE', 'ENS']
fig, axs = plt.subplots(1, 2, figsize=(9, 4.4), sharey=False)
for ax, key, title in ((axs[0], 'Cadres', 'Children of senior managers & professionals'), (axs[1], 'Ouvriers', 'Children of manual workers')):
    for off, yr, col in ((-0.2, '2009', '0.75'), (0.2, '2024', '0.2')):
        vals = [float(next(r for r in rows if r['filiere'] == f and r['origine_sociale'].startswith(key))[yr]) for f in fil]
        ax.bar([i + off for i in range(4)], vals, 0.4, color=col, edgecolor='black', label=yr)
        for i, v in enumerate(vals): ax.text(i + off, v + 0.6, f'{v:.0f}', ha='center', fontsize=8.5)
    ax.set_xticks(range(4)); ax.set_xticklabels(lab); ax.set_title(title, fontsize=10); style(ax)
axs[0].set_ylabel('% of students in the track'); axs[0].set_ylim(0, 72); axs[1].set_ylim(0, 26); axs[0].legend(frameon=False, fontsize=9)
fig.suptitle('Social composition of French higher-education tracks, 2009 vs 2024', fontsize=11)
fig.text(0.01, 0.01, 'Source: Martin-Kleinbauer & Maurin (2025), Observatoire des inégalités, from MESR data', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{R}/SOC-02/figures/SOC-02_redraw.png', dpi=200); plt.close(fig)
