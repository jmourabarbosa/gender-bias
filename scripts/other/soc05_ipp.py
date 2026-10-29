"""Transcribe IPP report n°30 (Bonneau, Charousset, Grenet, Thebault 2021): Figure 4.1 (p.93) and Figure 7.17 (p.215) labels -> CSV; B/W redraws."""
import re, csv, pymupdf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-05'
doc = pymupdf.open(f'{D}/source.pdf')
CL = ['pcs_defavorisees', 'pcs_moyennes', 'pcs_favorisees', 'pcs_tres_favorisees']
def pcts(lines): return [int(l[:-1]) for l in lines if re.fullmatch(r'\d+%', l)]
# Fig 4.1
L = [l.strip() for l in doc[92].get_text().split('\n')]
i = next(k for k, l in enumerate(L) if l.startswith('FIGURE 4.1'))
v = pcts(L[i:i + 60])[:32]
groups = ['Cohorte (population 20-24)', 'Étudiants bac+3 à bac+5', 'Étudiants grandes écoles', 'Ingénieur', 'Commerce', 'ENS', 'IEP', 'Autre']
with open(f'{D}/data/SOC-05.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['groupe'] + CL + ['source'])
    for g, k in zip(groups, range(0, 32, 4)): w.writerow([g] + v[k:k + 4] + ['IPP rapport 30, figure 4.1 p.93 (2016-2017)'])
fig41 = {g: v[k:k + 4] for g, k in zip(groups, range(0, 32, 4))}
print(fig41)
# Fig 7.17
L = [l.strip() for l in doc[214].get_text().split('\n')]
rows = []
for k, l in enumerate(L):
    m = re.match(r'\(([a-z])\) (.+)', l)
    if m:
        vals = pcts(L[k + 1:k + 60])[:44]
        for y, j in zip(range(2006, 2017), range(0, 44, 4)): rows.append([m.group(2), y] + vals[j:j + 4])
with open(f'{D}/data/SOC-05_fig7-17_trend.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['panel', 'year'] + CL); w.writerows(rows)
for r in rows: print(r)
# redraw 1: students vs age group
fig, ax = plt.subplots(figsize=(8, 4.6))
keys = ['Cohorte (population 20-24)', 'Étudiants bac+3 à bac+5', 'Étudiants grandes écoles', 'ENS']
labs = ['Age group\n(20-24)', 'All students\nbac+3 to bac+5', 'Grandes\nécoles', 'ENS']
cols = ['0.9', '0.65', '0.4', '0.1']; names = ['Disadvantaged', 'Middle', 'Advantaged', 'Very advantaged']
left = [0] * 4
for c in range(4):
    vals = [fig41[k][c] for k in keys]
    ax.barh(range(4), vals, left=left, color=cols[c], edgecolor='black', label=names[c])
    for i, (lft, v) in enumerate(zip(left, vals)):
        if v >= 7: ax.text(lft + v / 2, i, f'{v}%', ha='center', va='center', fontsize=9, color='white' if c == 3 else 'black')
    left = [a + b for a, b in zip(left, vals)]
ax.set_yticks(range(4)); ax.set_yticklabels(labs); ax.invert_yaxis(); ax.set_xlim(0, 101); ax.set_xlabel('% (parental socio-occupational group)')
ax.legend(frameon=False, ncol=4, fontsize=8.5, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax.set_title('Social origin: grandes écoles vs their age group, France 2016-17', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Bonneau, Charousset, Grenet & Thebault (2021), IPP report 30, fig. 4.1 p. 93', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-05_redraw.png', dpi=200); plt.close(fig)
# redraw 2: trend very advantaged share
fig, ax = plt.subplots(figsize=(7.5, 4.4))
for panel, st, lab in ((rows[0][0], '-o', 'Grandes écoles (2006 scope)'), (rows[11][0], '--s', 'University (bac+3)')):
    ys = [r for r in rows if r[0] == panel]
    ax.plot([r[1] for r in ys], [r[5] for r in ys], st, color='black', label=lab)
    ax.annotate(f'{ys[0][5]}%', (2006, ys[0][5]), textcoords='offset points', xytext=(-4, 8), fontsize=9)
    ax.annotate(f'{ys[-1][5]}%', (2016, ys[-1][5]), textcoords='offset points', xytext=(-4, 8), fontsize=9)
ax.axhline(23, color='0.5', ls=':'); ax.text(2006, 24, 'share in the 20-24 age group (2016-17): 23%', fontsize=8, color='0.3')
ax.set_ylim(0, 80); ax.set_ylabel('% of students from very advantaged backgrounds'); ax.legend(frameon=False, fontsize=9, loc='center', bbox_to_anchor=(0.5, 0.66))
ax.set_title('No democratisation of grandes écoles, 2006-2016', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: IPP report 30 (2021), fig. 7.17 p. 215 and fig. 4.1 p. 93', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-05_redraw_trend.png', dpi=200)
