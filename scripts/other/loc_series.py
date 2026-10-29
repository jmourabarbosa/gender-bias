"""Build LOC-01/02/03 CSVs (DGRH 'Trajectoire professionnelle' notes, recruits 2018-2024) and B/W redraws.
Values transcribed from the PDF text (pages noted) and from the labelled bar charts (figure 3/4 of each note)."""
import csv, os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
L = '/home/user/gender-bias/other-biases-data/01-localism'
NOTE = {2018: ('DGRH note n°8, juillet 2019', 'LOC-03/series/dgrh_trajectoire_recrutes_2018.pdf'),
        2019: ('DGRH note n°7, septembre 2020', 'LOC-03/series/dgrh_trajectoire_recrutes_2019.pdf'),
        2020: ('DGRH note n°8, septembre 2021', 'LOC-03/series/dgrh_trajectoire_recrutes_2020.pdf'),
        2021: ('DGRH note n°8, septembre 2022', 'LOC-03/source.pdf'),
        2022: ('DGRH note n°7, septembre 2023', 'LOC-03/series/dgrh_trajectoire_recrutes_2022.pdf'),
        2023: ('DGRH note n°3, 2025', 'LOC-02/source.pdf'),
        2024: ('DGRH note n°2, 2026', 'LOC-01/source.pdf')}
# year: n_recruited, mcf_endo, pr_endo, pr_endo_scope, mcf_foreign, pr_foreign, pages
TOT = {2018: (1433, 18, 45, 'incl. agrégés du supérieur', 14, 12, 'endo p1+p2+fig3 p3; foreign p1+p4'),
       2019: (1367, 17, 41, 'incl. agrégés du supérieur', 16, 11, 'endo p1+fig3 p3 (body text p2 says 18% MCF); foreign p1+p4'),
       2020: (1444, 20, 47, 'excl. agrégés du supérieur', 18, 12, 'endo p1+p2+fig4 p3; foreign p1+p4 (PR excl. agrégés)'),
       2021: (1449, 18, 46, 'excl. agrégés du supérieur', 20, 11, 'endo p1+p2+fig4 p3; foreign p1+p4 (PR excl. agrégés)'),
       2022: (1730, 19, 57, 'incl. agrégés and art. 46-3', 23, 10, 'endo p1+p2+fig4 p3; foreign p1+p4'),
       2023: (1836, 19, 54, 'incl. agrégés and art. 46-3', 18.5, 11, 'endo p1+p2+fig4 p3; foreign p1+p4'),
       2024: (2015, 23, 54, 'incl. agrégés and art. 46-3', 23.5, 7.9, 'endo p1+p2+fig4 p3; foreign p1+p3+fig6 p4')}
# by discipline: (neo, endo, mutation) for DEG, LSH, ST, All ; MCF then PR
DISC = ['Droit-Économie-Gestion', 'Lettres-Sciences humaines', 'Sciences-Techniques', 'Toutes disciplines']
FIG = {2018: ('fig3 p3', [60,73,73,70],[21,16,18,18],[19,11,8,12],[41,37,36,38],[26,46,55,45],[33,16,9,17]),
       2019: ('fig3 p3', [64,71,77,71],[18,19,14,17],[17,10,9,11],[50,42,39,42],[18,41,53,41],[33,17,8,17]),
       2020: ('fig4 p3', [65,70,70,69],[20,20,19,20],[15,10,11,12],[41,42,33,35],[26,45,58,47],[33,13,9,18]),
       2021: ('fig4 p3', [66,69,77,71],[19,20,15,18],[15,10,9,11],[41,47,36,38],[26,40,60,46],[33,12,4,16]),
       2022: ('fig4 p3', [62,71,71,68],[15,17,20,19],[22,13,9,13],[41,34,26,31],[26,54,70,57],[33,12,5,12]),
       2023: ('fig4 p3', [62,71,75,70],[21,17,17,19],[17,12,8,11],[41,42,28,33],[26,45,67,54],[33,12,5,13]),
       2024: ('fig4 p3', [68,66,69,66],[17,24,23,23],[15,11,9,10],[41,43,25,35],[26,46,68,54],[33,10,7,11])}
os.makedirs(f'{L}/LOC-03/data', exist_ok=True)
with open(f'{L}/LOC-03/data/local_hiring_series.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['year', 'n_recruited_concours', 'mcf_endo_pct', 'pr_endo_pct', 'pr_endo_scope', 'mcf_foreign_pct', 'pr_foreign_pct',
                'source_note', 'source_file', 'pages', 'loc_id'])
    for y, (n, me, pe, sc, mf, pf, pg) in TOT.items():
        lid = {2023: 'LOC-02', 2024: 'LOC-01'}.get(y, 'LOC-03')
        w.writerow([y, n, me, pe, sc, mf, pf, NOTE[y][0], 'other-biases-data/01-localism/' + NOTE[y][1], pg, lid])
rows = []
for y, (fg, mn, me, mm, pn, pe, pm) in FIG.items():
    for corps, (n_, e_, m_) in (('MCF', (mn, me, mm)), ('PR', (pn, pe, pm))):
        for i, d in enumerate(DISC):
            rows.append([y, corps, d, n_[i], e_[i], m_[i], NOTE[y][0], fg])
hdr = ['year', 'corps', 'discipline', 'neo_recrutement_pct', 'endo_recrutement_pct', 'mutation_detachement_pct', 'source_note', 'figure_page']
with open(f'{L}/LOC-03/data/local_hiring_by_discipline.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(hdr); w.writerows(rows)
for y, lid in ((2024, 'LOC-01'), (2023, 'LOC-02')):
    os.makedirs(f'{L}/{lid}/data', exist_ok=True)
    with open(f'{L}/{lid}/data/{lid}.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(hdr); w.writerows([r for r in rows if r[0] == y])
# age at hiring and foreign share (LOC-01 fig5, fig6)
with open(f'{L}/LOC-01/data/LOC-01_age_foreign.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['indicator', 'corps', 'discipline_or_year', 'value', 'page'])
    for c, vals in (('MCF', [35, 37, 33, 35]), ('PR', [42, 50, 46, 47])):
        for d, v in zip(DISC, vals): w.writerow(['mean_age_at_hiring', c, d, v, 'fig5 p3'])
    for c, a, b in (('MCF', 17.5, 23.5), ('PR', 10.0, 7.9), ('PR not previously MCF', 39.6, 30.9)):
        w.writerow(['foreign_pct', c, 2020, a, 'fig6 p4']); w.writerow(['foreign_pct', c, 2024, b, 'fig6 p4'])

plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
# series redraw
yrs = list(TOT)
fig, ax = plt.subplots(figsize=(8, 5))
mcf = [TOT[y][1] for y in yrs]; pr = [TOT[y][2] for y in yrs]; fo = [TOT[y][4] for y in yrs]
ax.plot(yrs, mcf, '-o', color='black', label='New MCF hired where they did their PhD')
ax.plot(yrs, pr, '--s', color='black', label='New PR hired where they were already MCF')
for y, a, b in zip(yrs, mcf, pr):
    ax.annotate(f'{a}%', (y, a), textcoords='offset points', xytext=(0, -16), ha='center', fontsize=9)
    ax.annotate(f'{b}%', (y, b), textcoords='offset points', xytext=(0, 8), ha='center', fontsize=9)
ax.axvspan(2019.5, 2021.5, color='0.92', zorder=0)
ax.text(2020.5, 3, 'PR rate excludes\nagrégés (2020-21)', ha='center', fontsize=8, color='0.3')
ax.set_ylim(0, 65); ax.set_ylabel('% of recruits'); ax.set_xticks(yrs)
ax.set_title('Local hiring in French universities, recruits 2018-2024')
ax.legend(frameon=False, loc='upper right', bbox_to_anchor=(1, 0.62), fontsize=9)
fig.text(0.01, 0.01, 'Source: MESR-DGRH notes "Trajectoire professionnelle des enseignants-chercheurs recrutés en <année>" (2019-2026 editions)', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{L}/LOC-03/figures/LOC-03_redraw.png', dpi=200); plt.close(fig)

# per-year discipline redraw (LOC-01, LOC-02)
SHORT = ['Law-Econ-Mgmt', 'Humanities-Soc.Sci.', 'Science-Tech', 'All']
for y, lid, src in ((2024, 'LOC-01', 'MESR-DGRH Note n°2-2026, fig. 4 p. 3'), (2023, 'LOC-02', 'MESR-DGRH Note n°3-2025, fig. 4 p. 3')):
    _, mn, me, mm, pn, pe, pm = FIG[y]
    fig, axs = plt.subplots(1, 2, figsize=(9, 4.2), sharey=True)
    for ax, corps, (n_, e_, m_) in zip(axs, ('MCF (local = PhD institution)', 'PR (local = already MCF there)'), ((mn, me, mm), (pn, pe, pm))):
        x = range(4)
        ax.bar(x, e_, color='0.25', label='Local (endo-recrutement)')
        ax.bar(x, n_, bottom=e_, color='0.8', label='External new hire')
        ax.bar(x, m_, bottom=[a + b for a, b in zip(e_, n_)], color='white', edgecolor='black', label='Transfer / secondment')
        for i, v in enumerate(e_):
            ax.text(i, v / 2, f'{v}%', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
        ax.set_xticks(list(x)); ax.set_xticklabels(SHORT, rotation=20, ha='right', fontsize=9); ax.set_title(corps, fontsize=10)
    axs[0].set_ylabel('% of posts filled'); axs[0].set_ylim(0, 100)
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, frameon=False, fontsize=8, loc='lower center', bbox_to_anchor=(0.5, 0.04), ncol=3)
    fig.suptitle(f'Local hiring by discipline group, French recruits {y}')
    fig.text(0.01, 0.01, f'Source: {src}', fontsize=8)
    fig.tight_layout(rect=(0, 0.1, 1, 1)); fig.savefig(f'{L}/{lid}/figures/{lid}_redraw.png', dpi=200); plt.close(fig)
print('ok')
