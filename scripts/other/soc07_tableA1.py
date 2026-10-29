"""Schultz & Stansbury 2022 (PIIE WP 22-4), Table A1 p.65: transcribe to CSV; B/W redraw of share with a parent holding a graduate degree."""
import re, csv, pymupdf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-07'
d = pymupdf.open(f'{D}/source.pdf')
L = [l.strip() for l in (d[64].get_text() + '\n' + d[65].get_text()).split('\n') if l.strip()]
start = L.index('Agriculture')
isval = lambda s: re.fullmatch(r'[\d,.]+%?', s) is not None
rows, lab, k = [], [], start
while k < len(L) and len(rows) < 16:
    if isval(L[k]):
        vals = []
        while k < len(L) and isval(L[k]) and len(vals) < 11: vals.append(L[k]); k += 1
        rows.append([' '.join(lab)] + vals); lab = []
    else:
        lab.append(L[k]); k += 1
cols = ['phd_field', 'n_phd_recipients', 'n_institutions', 'hhi_institutions', 'median_age_phd', 'median_years_ba_to_phd',
        'median_years_grad_entry_to_phd', 'female_share', 'share_no_parent_ba', 'share_parent_graduate_degree', 'share_parent_phd', 'share_missing_parental_ed']
with open(f'{D}/data/SOC-07.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(cols + ['source']); [w.writerow(r + [''] * (12 - len(r)) + ['PIIE WP 22-4 Table A1 p.65, all PhD recipients 2010-18']) for r in rows]
for r in rows: print(r)
rr = [r for r in rows if len(r) >= 10 and r[0] not in ('Other or unknown',)]
rr.sort(key=lambda r: float(r[9].strip('%')))
fig, ax = plt.subplots(figsize=(7.5, 5.5))
y = range(len(rr)); v = [float(r[9].strip('%')) for r in rr]
ax.barh(list(y), v, color=['black' if r[0] == 'Economics' else ('0.35' if r[0] == 'All' else '0.7') for r in rr])
ax.set_yticks(list(y)); ax.set_yticklabels([r[0].replace('Biological/ biomedical sciences', 'Biological/biomedical sci.') for r in rr], fontsize=9)
for i, x in enumerate(v): ax.text(x + 0.5, i, f'{x:.0f}%', va='center', fontsize=8.5)
ax.set_xlabel('% of PhD recipients with at least one parent holding a graduate degree'); ax.set_xlim(0, 60)
ax.set_title('US PhD recipients 2010-18: parent with a graduate degree, by field', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Schultz & Stansbury (2022), PIIE WP 22-4, Table A1 p. 65 (NSF Survey of Earned Doctorates)', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-07_redraw.png', dpi=200)
