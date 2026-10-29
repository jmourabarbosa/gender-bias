import csv
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
L = '/home/user/gender-bias/other-biases-data/01-localism'
def style(ax):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
# LOC-04: how posts were filled, 2024
rows = {r['corps_article']: r for r in csv.DictReader(open(f'{L}/LOC-04/data/LOC-04.csv'))}
fig, ax = plt.subplots(figsize=(7.5, 3.8))
for i, (k, lab) in enumerate((('Maîtres de conférences (total)', 'MCF'), ('Professeurs des universités (total)', 'PR'), ('Total général', 'All'))):
    r = rows[k]; c, m, d = (float(r[x] or 0) for x in ('pourvus_concours', 'pourvus_mutation', 'pourvus_detachement')); t = float(r['total_pourvus'])
    left = 0
    for v, col, nm in ((c, '0.3', 'Competitive exam (concours)'), (m, '0.8', 'Transfer (mutation)'), (d, 'white', 'Secondment (détachement)')):
        ax.barh(i, v / t * 100, left=left, color=col, edgecolor='black', label=nm if i == 0 else None)
        if v / t > 0.05: ax.text(left + v / t * 50, i, f'{v / t * 100:.0f}% ({int(v)})', ha='center', va='center', color='white' if col == '0.3' else 'black', fontsize=9)
        left += v / t * 100
ax.set_yticks(range(3)); ax.set_yticklabels(['MCF', 'PR', 'All']); ax.invert_yaxis(); ax.set_xlim(0, 100)
ax.set_xlabel('% of posts filled in 2024'); ax.legend(frameon=False, fontsize=8, ncol=3, loc='upper center', bbox_to_anchor=(0.5, -0.25))
ax.set_title('How French university posts were filled, 2024 campaign', fontsize=11); style(ax)
fig.text(0.01, 0.01, 'Source: MESR-DGRH Note n°1-2026 (campagne 2024), figure 6 p. 3', fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{L}/LOC-04/figures/LOC-04_redraw.png', dpi=200); plt.close(fig)
# LOC-08: inbred effect relative to mean
rows = list(csv.DictReader(open(f'{L}/LOC-08/data/LOC-08.csv')))
fig, ax = plt.subplots(figsize=(7.5, 3.8))
lab = ['Peer-reviewed articles', 'Consulting contracts', 'Prototypes & patents', 'Undergrad theses supervised', "Master's theses supervised", 'PhD theses supervised']
v = [float(r['inbred_marginal_effect']) / float(r['sample_mean']) * 100 for r in rows]
sig = [r['significance'] != 'n.s.' for r in rows]
ax.barh(range(6), v, color=['black' if s else '0.8' for s in sig], edgecolor='black')
for i, (x, s) in enumerate(zip(v, sig)): ax.text(x + (2 if x >= 0 else -2), i, f'{x:+.0f}%' + ('' if s else ' (n.s.)'), va='center', ha='left' if x >= 0 else 'right', fontsize=9)
ax.axvline(0, color='black', lw=0.8); ax.set_yticks(range(6)); ax.set_yticklabels(lab, fontsize=9); ax.invert_yaxis(); ax.set_xlim(-30, 60)
ax.set_xlabel('Effect of being inbred, % of sample mean'); ax.set_title('Inbred faculty publish less (Mexico, 1999-2002)', fontsize=11); style(ax)
fig.text(0.01, 0.01, 'Source: Horta, Veloso & Grediaga (2010), Management Science; Table 3 p. 17 of the CMU KiltHub (figshare) preprint', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{L}/LOC-08/figures/LOC-08_redraw.png', dpi=200); plt.close(fig)
# LOC-13 + LOC-11 + France comparison (stock indicators)
fig, ax = plt.subplots(figsize=(7.5, 3.6))
items = [('Spain, public universities 2024-25\n(teaching staff, PhD from same university)', 72.8), ('Portugal, public universities 2021-22\n(career PhD faculty, PhD from same institution)', 68)]
ax.barh(range(2), [b for _, b in items], color=['0.3', '0.6'], edgecolor='black')
for i, (_, b) in enumerate(items): ax.text(b + 1, i, f'{b:.0f}%', va='center', fontsize=10)
ax.set_yticks(range(2)); ax.set_yticklabels([a for a, _ in items], fontsize=8.5); ax.invert_yaxis(); ax.set_xlim(0, 100)
ax.set_xlabel('% of academic staff'); ax.set_title('Academic inbreeding (stock of staff), Spain and Portugal', fontsize=11); style(ax)
fig.text(0.01, 0.01, 'Sources: MICIU SIIU-EPU (PDITESIS); SEDES Policy Paper 5/2024 citing DGEEC. Not comparable with French flow rates (LOC-01..03).', fontsize=7)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f'{L}/LOC-13/figures/LOC-13_redraw.png', dpi=200); plt.close(fig)
