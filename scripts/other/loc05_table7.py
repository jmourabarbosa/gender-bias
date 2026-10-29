"""Transcribe Godechot & Louvet 2008 Tableau 7 (PDF p.15) and Tableau 5 key rows (p.12) to CSV; B/W redraw of odds ratios."""
import sys, csv, pymupdf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/01-localism/LOC-05'
NAMES = ['Philosophie', 'Ethnologie ; Sciences des religions', 'Littérature', 'Sociologie', 'Art et archéologie ; Cinéma ; Théâtre ; Musicologie',
         'Linguistique', 'Études langues et civilisations', 'Histoire', "Sciences de l'éducation", 'Psychologie', 'Biologie', 'Physique',
         'Mathématiques', 'Ensemble', 'Terre, Océan, Géologie', 'Géographie', 'Gestion', 'Sciences médicales', 'Science politique',
         'Informatique', 'Droit', 'Économie', 'Chimie', "Sciences de l'ingénieur"]
def num(s, dec):
    s = s.replace('\n', '').replace('%', '').replace(',', '')
    return float(s) / 10 ** dec if (',' in s or dec) else float(s)
rows = pymupdf.open(f'{D}/source.pdf')[14].find_tables().tables[0].extract()[1:]
out = []
for name, r in zip(NAMES, rows):
    dec_att = 1 if ',' in r[2] else 0
    out.append([name, int(r[1]), num(r[2], dec_att), int(r[3]), int(r[4]), int(r[5]), num(r[6], 2), num(r[7], 2)])
with open(f'{D}/data/LOC-05.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['discipline', 'recrutes_locaux', 'recrutes_locaux_attendus', 'candidatures_locales', 'recrutes_exterieurs',
                'candidatures_exterieures', 'part_locaux_parmi_recrutes_pct', 'mantel_haenszel_odds_ratio'])
    w.writerows(out)
with open(f'{D}/data/LOC-05_table5_summary.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows([['indicator', 'value', 'page'],
                 ['success_rate_local_applications_pct', 6.30, 12], ['success_rate_external_applications_pct', 0.24, 12],
                 ['mantel_haenszel_odds_ratio', 18.02, 12], ['crude_odds_ratio_text', 27, 12],
                 ['share_locals_among_recruits_pct', 55, 12], ['share_locals_expected_under_independence_pct', 8, 12],
                 ['local_applications', 72257, 12], ['external_applications', 1546186, 12],
                 ['local_recruits', 4549, 12], ['external_recruits', 3780, 12]])
for r in out: print(r)
# redraw
out.sort(key=lambda r: r[-1])
fig, ax = plt.subplots(figsize=(7.5, 8))
y = range(len(out))
ax.barh(y, [r[-1] for r in out], color=['black' if r[0] == 'Ensemble' else '0.6' for r in out])
ax.set_yticks(list(y)); ax.set_yticklabels([('All disciplines' if r[0] == 'Ensemble' else r[0]) for r in out], fontsize=8.5)
for i, r in enumerate(out): ax.text(r[-1] + 0.5, i, f'{r[-1]:.1f}', va='center', fontsize=8)
ax.set_xlabel('Mantel-Haenszel odds ratio: local vs external applicant hired')
ax.set_title('Local candidates\' odds of being hired, by discipline\n(French PhDs defended 1972-1996)', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Godechot & Louvet (2008), La Vie des idées, Tableau 7 p. 15 (DOCTHESE data)', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/LOC-05_redraw.png', dpi=200)
