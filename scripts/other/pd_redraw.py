"""Black/grey redraws for 07-precarity and 08-disability. usage: python3 -I pd_redraw.py [ID ...]
Reads other-biases-data/<section>/<ID>/data/*.csv, writes figures/<ID>_redraw.png."""
import sys, csv, glob, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = '/home/user/gender-bias/other-biases-data'
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': 'black', 'axes.grid': True, 'grid.color': '#dddddd', 'grid.linewidth': 0.6})
plt.rcParams['axes.grid.axis'] = 'y'
GREYS = ['black', '#777777', '#bbbbbb']


def folder(i):
    return glob.glob(f'{ROOT}/*/{i}')[0]


def rows(i, name=None):
    f = f'{folder(i)}/data/{name or i + ".csv"}'
    return [r for r in csv.DictReader(open(f, encoding='utf-8'))]


def finish(fig, ax, i, title, source):
    fig.suptitle(title, fontsize=11, x=0.01, ha='left')
    from matplotlib.ticker import MaxNLocator
    if ax.get_xlabel() in ('Year', 'Campaign year', 'Fiscal year') or ax.lines and isinstance(ax.lines[0].get_xdata()[0], (int, np.integer)):
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.text(0.01, 0.01, 'Source: ' + source, fontsize=7.5, color='#444444', ha='left', va='bottom', wrap=True)
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    out = f'{folder(i)}/figures/{i}_redraw.png'
    fig.savefig(out, dpi=200); plt.close(fig); print('saved', out)


def hbars(i, labels, values, title, source, xlabel, fmt='{:.0f}%', vline=None, vlabel=None, colors=None):
    fig, ax = plt.subplots(figsize=(7.5, 0.45 * len(labels) + 1.6))
    y = np.arange(len(labels))[::-1]
    ax.barh(y, values, color=colors or 'grey', height=0.6)
    for yy, v in zip(y, values):
        ax.text(v, yy, ' ' + fmt.format(v), va='center', fontsize=9)
    import textwrap; ax.set_yticks(y, [textwrap.fill(l, 42) for l in labels]); ax.set_xlabel(xlabel); ax.grid(axis='x'); ax.grid(axis='y', visible=False)
    ax.set_xlim(min(0, min(values) * 1.3), max(max(values) * 1.18, (vline or 0) * 1.1))
    if vline is not None:
        ax.axvline(vline, color='black', ls='--', lw=1.2); ax.text(vline, y.max() + 0.45, vlabel, ha='center', va='bottom', fontsize=8.5)
    finish(fig, ax, i, title, source)


def grouped(i, cats, series, title, source, ylabel, fmt='{:.0f}', ylim=None, rot=0):
    fig, ax = plt.subplots(figsize=(7.5, 4.3))
    x = np.arange(len(cats)); n = len(series); w = 0.8 / n
    for k, (name, vals) in enumerate(series):
        b = ax.bar(x + (k - (n - 1) / 2) * w, vals, w * 0.95, color=GREYS[k % 3], edgecolor='black', lw=0.6, label=name)
        for xx, v in zip(x + (k - (n - 1) / 2) * w, vals):
            if v is not None and not np.isnan(v): ax.text(xx, v, fmt.format(v), ha='center', va='bottom', fontsize=8)
    ax.set_xticks(x, cats, rotation=rot, ha='right' if rot else 'center'); ax.set_ylabel(ylabel)
    if ylim: ax.set_ylim(*ylim)
    ax.legend(frameon=False, fontsize=9)
    finish(fig, ax, i, title, source)


def f(v):
    try: return float(v)
    except (TypeError, ValueError): return np.nan


def run(i):
    if i == 'PREC-01':
        r = rows(i); yrs = [int(x['year']) for x in r]
        fig, ax = plt.subplots(figsize=(7.5, 4.2))
        ax.plot(yrs, [f(x['contract_share_pct']) for x in r], '-o', color='black', ms=4)
        for x in r:
            if x['year'] in ('2000', '2005', '2015', '2024'): ax.annotate(f"{float(x['contract_share_pct']):.1f}%", (int(x['year']), f(x['contract_share_pct'])), textcoords='offset points', xytext=(0, 7), ha='center', fontsize=8.5)
        ax.set_ylim(15, 30); ax.set_ylabel('Contract teachers, % of all teachers'); ax.set_xlabel('Year')
        finish(fig, ax, i, 'Contract teachers (excl. hourly vacataires) as a share of all higher-ed teachers',
               'MESR-DGRH notes on contract teachers (n°4-2017, n°5-2022, n°4-2023, n°6-2025); headcounts, excl. hospital staff')
    elif i == 'PREC-02':
        hbars(i, ['MCF', 'PU (professors)', 'All EC', 'Secondary-school teachers (E2D)'], [-6.5, 6.8, -1.8, -1.5],
              'Change in tenured staff, 2010 to 2023, by body', 'SNESUP Le Snesup n°734 (2025) p11; union compilation of MESR data',
              'Change (%)', fmt='{:+.1f}%')
    elif i in ('PREC-03', 'PREC-04'):
        r = rows('PREC-03', 'posts_candidates_series.csv'); yrs = [int(x['year']) for x in r]
        fig, ax = plt.subplots(figsize=(7.5, 4.3))
        if i == 'PREC-03':
            ax.plot(yrs, [f(x['mcf_posts']) for x in r], '-o', color='black', ms=4, label='MCF posts published')
            ax.plot(yrs, [f(x['pr_posts']) for x in r], '--s', color='grey', ms=4, label='PR posts published')
            ax.plot(yrs, [f(x['posts_authorised']) for x in r], ':', color='black', lw=1.2, label='Posts authorised (MCF+PR ceiling)')
            ax.set_ylabel('Posts'); ax.set_ylim(0, 4000); ax.legend(frameon=False, fontsize=9)
            title = 'Lecturer (MCF) and professor (PR) posts per recruitment campaign, 2008-2025'
            note = 'MESR-DGRH campaign reports and notes 2011-2026 (data/posts_candidates_series.csv); 2025 provisional (July)'
        else:
            st = [x['ratio_status'] for x in r]; v = [f(x['candidates_per_mcf_post']) for x in r]
            ax.plot(yrs, v, '-', color='black')
            for s, mk, fc, lab in [('official', 'o', 'black', 'stated by DGRH'), ('derived', 'o', 'white', 'computed from DGRH counts'), ('provisional', 's', 'grey', 'provisional (July)')]:
                ax.plot([y for y, ss in zip(yrs, st) if ss == s], [vv for vv, ss in zip(v, st) if ss == s], mk, mfc=fc, mec='black', ms=6, ls='none', label=lab)
            ax.set_ylim(0, 9); ax.set_ylabel('Candidates per MCF post'); ax.legend(frameon=False, fontsize=9, loc='lower right')
            title = 'Candidates per lecturer (MCF) post, 2008-2025 (2019 missing)'
            note = 'MESR-DGRH campaign reports; definitions of the post base vary slightly (see notes.md)'
        ax.set_xlabel('Campaign year'); finish(fig, ax, i, title, note)
    elif i == 'PREC-05':
        r = [x for x in rows(i) if x['table'] == 'prev_activity_2023' and x['category'] == 'Post-doctorant']
        hbars(i, [x['group'] for x in r], [f(x['value']) for x in r], 'New lecturers (MCF) 2023 who were postdocs just before hiring',
              'MESR-DGRH Note n°3-2025 (= LOC-02), fig. 3 p2; mean age at hiring: MCF 35, PR 47', '% of recruits (excl. "other activity")')
    elif i == 'PREC-07':
        r = rows(i, 'PREC-07_selection_rate.csv'); yrs = [int(x['year']) for x in r]
        fig, ax = plt.subplots(figsize=(7.5, 4.2))
        ax.plot(yrs, [f(x['selection_rate_researchers_pct']) for x in r], '-o', color='black', ms=4, label='Researcher competitions (CR/DR)')
        ax.plot(yrs, [f(x['selection_rate_IT_pct']) for x in r], '--s', color='grey', ms=4, label='Engineer/technician competitions')
        ax.set_ylim(0, 12); ax.set_ylabel('Selection rate (% of applicants hired)'); ax.legend(frameon=False)
        finish(fig, ax, i, 'CNRS competitions: share of applicants selected, 2013-2022',
               'Cour des comptes, CNRS 2013-2023 report, Graphique 11 p49 (values read from the vector chart)')
    elif i == 'PREC-08':
        r = rows(i); cats = ['Sciences exactes et applications', 'Sciences du vivant', 'Sciences humaines et sociales', 'Ensemble']
        lab = ['Exact sciences', 'Life sciences', 'Humanities & social sci.', 'All']
        g = lambda yr: [f(next(x['funded_pct'] for x in r if x['field'] == c and x['year'] == yr)) for c in cats]
        grouped(i, lab, [('2023-24', g('2023-2024')), ('2024-25', g('2024-2025'))], 'First-year doctoral students with dedicated funding',
                'MESR-SIES Note Flash n°14 (June 2025) p2', '% funded', ylim=(0, 110))
    elif i == 'PREC-09':
        hbars(i, ['Rate per hour taught (TD)', 'SMIC (gross hourly minimum wage)', 'Effective rate incl. 4.2 h prep per hour'],
              [43.50, 11.88, 8.37], 'Hourly pay of a university vacataire', "AN written question n°1155 (2025), deputy's worked example; SMIC added by collector",
              'Euros per hour', fmt='{:.2f} €', colors=['grey', '#bbbbbb', 'black'])
    elif i == 'PREC-10':
        hbars(i, ['Junior chairs (CPJ) 2021-22', 'Professors (PU) recruited 2022'], [25, 42], 'Women among recruits',
              'SNESUP Le Snesup n°728 (Nov 2024) p19', '% women', vline=50, vlabel='parity')
    elif i == 'PREC-11':
        hbars(i, ['Cohorts of the 1960s', 'Cohorts of the 2010s'], [35, 5], 'Years until half of an entering cohort of scientists has left',
              'Milojević, Radicchi & Walsh 2018, PNAS 115:12616, abstract & Fig. 4D (astronomy, ecology, robotics)', 'Half-life (years)', fmt='{:.0f} y')
    elif i == 'PREC-12':
        r = rows(i)
        hbars(i, [x['field'] for x in r], [100 * f(x['p_tenure_track']) for x in r], 'US postdocs who eventually land a tenure-track job',
              'Andalib, Ghaffarzadegan & Larson 2018, Syst Res Behav Sci 35:675, Table 1 (1 - P{reneging})', '% of postdocs')
    elif i == 'PREC-13':
        r = [x for x in rows(i) if x['median_age_first_R01']]
        fig, ax = plt.subplots(figsize=(7.5, 4.2))
        ax.plot([int(x['fiscal_year']) for x in r], [f(x['median_age_first_R01']) for x in r], '-o', color='black', ms=4)
        ax.set_ylim(30, 46); ax.set_ylabel('Median age at first R01 (years)'); ax.set_xlabel('Fiscal year')
        ax.annotate('mean 36.2 (1990)', (1990, 36), xytext=(1991, 33), fontsize=8.5); ax.annotate('mean 44.9 (2016)', (2016, 43), xytext=(2009, 44.8), fontsize=8.5)
        finish(fig, ax, i, 'Age of NCI-funded PhD investigators at their first R01 grant',
               'Antman et al. 2021, JCI 131:e146925, Suppl. Fig. 3 (medians read from bars) and Results text (means)')
    elif i == 'PREC-14':
        r = rows(i)
        hbars(i, [x['item'] for x in r], [f(x['pct']) for x in r],
              'Nature postdoc survey 2020 (n > 7,600)', 'Nature editorial 2020, doi:10.1038/d41586-020-02541-9', '% of respondents')
    elif i == 'PREC-15':
        r = rows(i)
        grouped(i, [x['field'] for x in r], [('Before 1905', [f(x['mean_age_early_period_pre1905']) for x in r]),
                                              ('After 1985', [f(x['mean_age_late_period_post1985']) for x in r])],
                'Mean age at Nobel-winning work', 'Jones & Weinberg 2011 PNAS 108:18910 (Fig. 1); means as summarised by Lindau 2016',
                'Age (years)', fmt='{:.1f}', ylim=(0, 60))
    elif i == 'DIS-01':
        r = [x for x in rows(i) if not x['entity'].startswith('Legal')]
        hbars(i, [f"{x['entity']} ({x['year']})" for x in r], [f(x['boe_employment_rate_pct']) for x in r],
              'Employment rate of staff with recognised disability vs 6% legal quota',
              'SNESUP Métier n°743 (2026) p18 [union]; Univ. Lorraine 2023 report; AN answer 13-52233; Inserm', '% of staff', fmt='{:.2f}%',
              vline=6, vlabel='6% quota', colors=['black' if 'official' in x['source_type'] else 'grey' for x in r])
    elif i == 'DIS-04':
        r = rows(i)
        hbars(i, [f"{x['group']} - {x['motive']}" for x in r], [f(x['pct_reporting_unequal_treatment']) for x in r],
              'Staff reporting unequal treatment (one university, ACADISCRI)', 'Cognet, Hajjat, Hamel et al. 2022, ACADISCRI first results pp.9-11 (= ETH-04)', '% of staff', fmt='{:.1f}%')
    elif i == 'DIS-05':
        r = rows(i)
        grouped(i, [x['motive'] for x in r], [('Students', [f(x['students_reporting_pct']) for x in r]), ('Staff', [f(x['staff_reporting_pct']) for x in r])],
                'Victims who reported the discrimination, by motive', 'Défenseur des droits 2024, Graphiques 1, 5, 6 (= ETH-05)', '% who reported', fmt='{:.1f}', ylim=(0, 60))
    elif i == 'DIS-07':
        r = rows(i)
        grouped(i, [x['violence_type'] for x in r], [('Men', [f(x['men_pct']) for x in r]), ('Women', [f(x['women_pct']) for x in r]),
                                                    ('Trans / queer / non-binary', [f(x['trans_queer_nonbinary_pct']) for x in r])],
                'Students experiencing sexual violence since entering higher education', 'MILDECA-UGA 2024 report Fig. 3 p13; MESR LGBTI guide 2026 p11',
                '% of students', fmt='{:.1f}', ylim=(0, 40), rot=15)
    elif i == 'DIS-08':
        r = rows(i)
        grouped(i, [x['outcome'][:45] for x in r], [('LGBTQ', [f(x['LGBTQ_pct']) for x in r]), ('Non-LGBTQ', [f(x['non_LGBTQ_pct']) for x in r])],
                'US STEM professionals: intentions to leave', 'Cech & Waidzunas 2021, Science Advances 7:eabe0933, p4', '% of respondents', ylim=(0, 30))
    elif i == 'DIS-09':
        r = [x for x in rows(i) if x['table'] == 'exclusionary_behaviour_last_12m' and x['group'] != 'All respondents']
        hbars(i, [x['group'] for x in r], [f(x['pct']) for x in r], 'UK physical scientists: exclusionary behaviour in last 12 months',
              'IOP/RAS/RSC 2019, Exploring the workplace for LGBT+ physical scientists, Fig. 5 p14', '% experiencing')
    elif i == 'DIS-10':
        r = rows(i); yrs = [int(x['fiscal_year']) for x in r]
        fig, ax = plt.subplots(figsize=(7.5, 4.2))
        ax.plot(yrs, [f(x['pct_applicants_disability']) for x in r], '-o', color='black', ms=4, label='Applicants reporting a disability')
        ax.plot(yrs, [f(x['pct_awardees_disability']) for x in r], '--s', color='grey', ms=4, label='Awardees reporting a disability')
        ax.set_ylim(0, 2.5); ax.set_ylabel('% of NIH applicants / awardees'); ax.legend(frameon=False)
        finish(fig, ax, i, 'NIH grant applicants and awardees reporting a disability, 2008-2018',
               'Swenor, Munoz & Meeks 2020, PLOS ONE 15:e0228686, Table 1')
    elif i == 'DIS-11':
        r = rows(i); keep = ['US population 18-74', 'In the STEM workforce', 'All doctorate recipients', 'S&E doctorate recipients', 'College-educated workers in S&E occupations']
        r = [x for x in r if x['group'] in keep]
        hbars(i, [f"{x['group']} ({x['survey']})" for x in r], [f(x['pct_with_disability']) for x in r], 'US: share with at least one disability, 2021',
              'NCSES 2023, Diversity and STEM (NSF 23-315), Fig. 1-1 p6, Fig. 7-10 p56, p37', '%', fmt='{:.1f}%')
    else:
        print('no redraw for', i)


for i in sys.argv[1:]:
    run(i)
