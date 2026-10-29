"""Transcribe RERS 2025 fiche 7.16 (L'origine sociale des étudiants français) tables 1-3 from the PDF text to CSV; redraw table 3 + table 1."""
import re, csv, pymupdf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-03'
lines = [l.replace('\xa0', ' ').strip() for l in pymupdf.open(f'{D}/source_rers2025_fiche7-16.pdf')[1].get_text().split('\n')]
lines = [l for l in lines if l]
isnum = lambda s: re.fullmatch(r'[\d ]+(,\d+)?', s) is not None
num = lambda s: float(s.replace(' ', '').replace(',', '.'))
def grab(start_label, end_label, ncols):
    i = lines.index(start_label); j = next(n for n in range(i, len(lines)) if lines[n].startswith(end_label[:20]) or end_label[:20] in lines[n])
    rows, k = [], i
    while k < j:
        lab = lines[k]; vals = lines[k + 1:k + 1 + ncols]
        if all(isnum(v) for v in vals) and not isnum(lab):
            rows.append([lab] + [num(v) for v in vals]); k += ncols + 1
        else: k += 1
    return rows
C1 = ['agriculteurs_artisans_commercants_chefs_entreprise', 'cadres_prof_intellectuelles_sup', 'professions_intermediaires',
      'employes', 'ouvriers', 'retraites_inactifs', 'ensemble', 'pct_valeurs_manquantes']
t1 = grab('Universités', 'Champ : France', 8)
t2 = grab('Disciplines générales', 'Champ : France', 9)
i3 = lines.index('Agriculteurs')
t3 = grab('Agriculteurs', 'Effectifs', 12) if False else None
# table 3: rows of 12 values after label
t3 = []; k = i3
while lines[k] != 'Proportion de valeurs manquantes':
    t3.append([lines[k]] + [num(v) for v in lines[k + 1:k + 13]]); k += 13
for name, rows, cols in (('SOC-03_table1_filieres', t1, ['filiere'] + C1),
                         ('SOC-03_table2_disciplines', t2, ['discipline'] + C1 + ['effectifs']),
                         ('SOC-03', t3, ['origine_sociale'] + [f'{c}_{s}' for c in ('licence', 'master', 'doctorat', 'ensemble') for s in ('femmes', 'hommes', 'total')])):
    with open(f'{D}/data/{name}.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(cols); w.writerows(rows)
    print(name, len(rows)); [print('  ', r) for r in rows[:30]]
# redraw: share of cadres vs ouvriers children by LMD level (table 3, totals)
get = {r[0]: r for r in t3}
lv = ['Licence', 'Master', 'Doctorat']
cad = [get['Cadres et professions intellectuelles supérieures'][i] for i in (3, 6, 9)]
ouv = [get['Ouvriers'][i] for i in (3, 6, 9)]
emp = [get['Employés'][i] for i in (3, 6, 9)]
fig, ax = plt.subplots(figsize=(7.5, 4.8)); x = range(3); wd = 0.26
for off, vals, col, lab in ((-wd, cad, '0.15', 'Senior managers & professionals (cadres)'), (0, emp, '0.55', 'Clerical/service workers (employés)'), (wd, ouv, '0.85', 'Manual workers (ouvriers)')):
    b = ax.bar([i + off for i in x], vals, wd, color=col, edgecolor='black', label=lab)
    for i, v in zip(x, vals): ax.text(i + off, v + 0.8, f'{v:.1f}', ha='center', fontsize=9)
ax.set_xticks(list(x)); ax.set_xticklabels(lv); ax.set_ylabel('% of French students (known origin)')
ax.set_title('Parents\' occupation of French university students by level, 2024-25', fontsize=11)
ax.legend(frameon=False, fontsize=8.5, loc='upper center', ncol=2); ax.set_ylim(0, 58)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: MENESR DEPP-SIES, RERS 2025, fiche 7.16 table 3 (SISE)', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-03_redraw.png', dpi=200)
