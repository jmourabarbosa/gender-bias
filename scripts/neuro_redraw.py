"""Simple black/white/grey redraws for NEURO sources from data/*.csv. Run from repo root."""
import csv, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False,
                     'font.family': 'DejaVu Sans'})
B = 'gender-bias-data/08-neuroscience/'
def rows(f): return list(csv.DictReader(open('data/' + f)))
def out(fig, idd):
    fig.tight_layout(); fig.savefig(f'{B}{idd}/figures/{idd}_redraw.png', dpi=300); plt.close(fig)

def hbars(idd, labels, vals, title, src, ref=None):
    fig, ax = plt.subplots(figsize=(7, 0.55 * len(labels) + 1.6))
    y = range(len(labels))[::-1]
    ax.barh(list(y), vals, color='0.55', edgecolor='black', height=0.6)
    for yy, v in zip(y, vals): ax.text(v + 1, yy, f'{v:g}%', va='center')
    ax.set_yticks(list(y)); ax.set_yticklabels(labels); ax.set_xlim(0, 100)
    ax.axvline(50, color='black', lw=0.8, ls=':')
    ax.set_xlabel('% women'); ax.set_title(title, loc='left', fontsize=12)
    fig.text(0.01, 0.005, src, fontsize=7, color='0.3')
    out(fig, idd)

r = rows('neuro07_sfn2016_pipeline.csv')
hbars('NEURO-07', [x['stage'] for x in r], [float(x['pct_women']) for x in r],
      'US neuroscience PhD programs, 2016-17', 'Source: SfN 2016-17 Neuroscience Departments & Programs Survey, executive summary')
r = rows('neuro08_sfn2018_pipeline.csv')
hbars('NEURO-08', [f"{x['group']} ({x['academic_year']})" for x in r], [float(x['pct_women']) for x in r],
      'Women in US neuroscience programs', 'Source: SfN, "Supporting Female Neuroscientists in Their Careers" (Neuroscience Quarterly, spring 2018)')
r = rows('neuro09_machlovi2021_authorship.csv')
hbars('NEURO-09', [x['measure'] for x in r], [float(x['pct_women']) for x in r],
      'Women: authorship and faculty', 'Source: Machlovi et al. 2021, J Neurosci Res 99:9-12 (numbers cited from Bendels 2018, Shen 2018, SfN)')

# NEURO-10 slope chart
r = [x for x in rows('neuro10_else2019_speaker_share.csv') if x['pct_women_speakers_end']]
fig, ax = plt.subplots(figsize=(6, 5))
for x in r:
    a, b = float(x['pct_women_speakers_start']), float(x['pct_women_speakers_end'])
    neuro = x['discipline'] == 'Neuroscience'
    ax.plot([2011, 2019], [a, b], '-o', color='black' if neuro else '0.65', lw=2.5 if neuro else 1.5)
    dy = {'Geology': 1.6, 'Artificial intelligence': -1.6}.get(x['discipline'], 0)
    ax.text(2019.2, b + dy, f"{x['discipline']} {b:g}%", va='center', fontweight='bold' if neuro else 'normal')
    ax.text(2010.8, a, f'{a:g}%', va='center', ha='right')
ax.set_xlim(2009.5, 2022.5); ax.set_ylim(0, 50); ax.set_xticks([2011, 2019])
ax.set_ylabel('% women among invited speakers'); ax.set_title('Invited speakers at major conferences', loc='left')
fig.text(0.01, 0.005, 'Source: Else 2019, Nature 573:184-186 (Nature analysis). Chemistry stayed <24% (no endpoints given).', fontsize=7, color='0.3')
out(fig, 'NEURO-10')

# NEURO-11 counts
r = rows('neuro11_hoy2021_brainstim_speakers.csv')
fig, ax = plt.subplots(figsize=(6, 3.5))
lab = [f"{x['year']}\n{x['conference'].split('(')[1].rstrip(')')}" for x in r]
w = [int(x['n_women']) for x in r]; m = [int(x['n_invited_speakers']) - int(x['n_women']) for x in r]
ax.barh(lab, m, color='0.75', edgecolor='black', label='men')
ax.barh(lab, w, left=m, color='black', label='women')
for i, (ww, mm) in enumerate(zip(w, m)): ax.text(ww + mm + 0.5, i, f'{ww} women / {ww + mm}', va='center')
ax.invert_yaxis(); ax.set_xlim(0, 50); ax.set_xlabel('invited speakers'); ax.legend(frameon=False, loc='lower right')
ax.set_title('International Brain Stimulation Conference', loc='left')
fig.text(0.01, 0.005, 'Source: Hoy, Fitzgibbon & Brem 2021, eLife 10:e75818', fontsize=7, color='0.3')
out(fig, 'NEURO-11')

# NEURO-12 two bars
r = rows('neuro12_cosyne2019_acceptance.csv')
fig, ax = plt.subplots(figsize=(4.5, 4.5))
ax.bar([x['first_author_gender'] for x in r], [float(x['acceptance_pct']) for x in r], color=['0.3', '0.75'], edgecolor='black', width=0.6)
for i, x in enumerate(r): ax.text(i, float(x['acceptance_pct']) + 1, f"{x['acceptance_pct']}%\n({x['accepted']}/{x['submitted']})", ha='center')
ax.set_ylim(0, 50); ax.set_ylabel('abstract acceptance rate (%)'); ax.set_xlabel('first author')
ax.set_title('Cosyne 2019', loc='left')
fig.text(0.01, 0.005, 'Source: C. Frye blog (6 Mar 2019), data via M. Carey', fontsize=7, color='0.3')
out(fig, 'NEURO-12')

# NEURO-15 BiasWatchNeuro: pooled share by post year + median base rate
r = rows('biaswatchneuro.csv')
by = collections.defaultdict(lambda: [0, 0, []])
for x in r:
    y = int(x['post_date'][:4]); by[y][0] += int(x['n_women']); by[y][1] += int(x['n_speakers'])
    if x['base_rate_pct']: by[y][2].append(float(x['base_rate_pct']))
yrs = [y for y in sorted(by) if by[y][1] >= 50]
import statistics as st
share = [100 * by[y][0] / by[y][1] for y in yrs]; base = [st.median(by[y][2]) for y in yrs]
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(yrs, share, '-o', color='black', label='women among listed speakers (pooled)')
ax.plot(yrs, base, '--s', color='0.55', label='median estimated base rate of women in field')
for y, s in zip(yrs, share): ax.text(y, s + 1.5, f'{s:.0f}%', ha='center', fontsize=9)
ax.set_ylim(0, 50); ax.set_ylabel('%'); ax.set_xticks(yrs)
ax.legend(frameon=False, loc='lower right', fontsize=9)
ax.set_title(f'Neuroscience meetings tracked by BiasWatchNeuro (n={len(r)} conference posts)', loc='left', fontsize=11)
fig.text(0.01, 0.005, 'Source: biaswatchneuro.com posts via WordPress API; year = post date; ratio line parsed per post (see data/biaswatchneuro.csv)', fontsize=7, color='0.3')
out(fig, 'NEURO-15')
for y, s, b in zip(yrs, share, base): print(y, by[y][1], round(s, 1), b)
