"""Write notes.md and _status/<ID>.json for NEURO-01..16. Run from repo root."""
import json, os, glob
S = 'gender-bias-data/08-neuroscience/'
E = {}
def add(i, title, citation, url, status, headline, check, notes, extra=''):
    E[i] = dict(title=title, citation=citation, url=url, status=status, headline=headline, check=check, notes=notes, extra=extra)

add('NEURO-01', 'Widening the scope of diversity (editorial)',
    'Nature Neuroscience editorial (2020). Nat Neurosci 23:903. DOI 10.1038/s41593-020-0670-2',
    'https://www.nature.com/articles/s41593-020-0670-2.pdf (PDF); landing page https://www.nature.com/articles/s41593-020-0670-2',
    'downloaded',
    'p.903: "Dworkin and colleagues show that the gender ratio in authorship has not changed considerably in our pages across a 20-year span." Quote for slide: "Aspire for an equal gender ratio in your citations."',
    'OK', 'Extract item is a quote; no figure in the editorial.')
add('NEURO-02', 'Women are systematically under-cited in neuroscience. New tools can change that.',
    'Churchland A, Davatolhagh F (22 July 2024). The Transmitter (Perspectives). DOI 10.53053/FWWC7810',
    'https://www.thetransmitter.org/publishing/women-are-systematically-under-cited-in-neuroscience-new-tools-can-change-that/',
    'downloaded',
    'Body text: women first/last authors "increased from 36 percent in 1995 to 50 percent in 2018" (five broad-scope journals); citation gap "widening at a rate of 0.41 percentage points per year" (citing Dworkin et al. 2020).',
    'OK', 'Page has no data figure (header photo only); numbers are second-hand from Dworkin et al. 2020 (CIT-01) - use CIT-01 figures for the plot.')
add('NEURO-03', 'Gender (im)balance in citation practices in cognitive neuroscience',
    'Fulvio JM, Akinnola I, Postle BR (2021). J Cogn Neurosci 33(1):3-7. DOI 10.1162/jocn_a_01643. Preprint bioRxiv 10.1101/2020.08.19.257402v1 (CC-BY-ND 4.0)',
    'https://www.biorxiv.org/content/biorxiv/early/2020/08/20/2020.08.19.257402.full.pdf (bioRxiv v1, via api.biorxiv.org / Unpaywall); published-version author manuscript text: PMC9811856 (article.xml, PMC text-mining bucket)',
    'downloaded',
    'Fig. 2 (preprint p.9): Gender Citation Balance Index MM approx. +0.42 (over-cited), WM approx. -0.25, MW approx. -0.04, WW approx. -0.44 (values read from the bar chart). Fig. 1: MM 43%->44%, WW 14%->20% of JoCN papers 2009->2020.',
    'OK', 'Extract "GCBI by category over years": the paper has GCBI by cited category (Fig 2) and by citing category (Fig 3) pooled over 2009-2020, no GCBI time series; only authorship shares are shown over years (Fig 1). PMC PDF/figures behind reCAPTCHA; Europe PMC render 403.')
add('NEURO-04', 'Racial and ethnic imbalance in neuroscience reference lists and intersections with gender',
    'Bertolero MA, Dworkin JD, David SU, Lloreda CL, Srivastava P, Stiso J, Zhou D, Dzirasa K, Fair DA, Kaczkurkin AN, Marlin BJ, Shohamy D, Uddin LQ, Zurn P, Bassett DS (2020). bioRxiv 10.1101/2020.10.12.336230 (v1, 12 Oct 2020; licence: all rights reserved, no reuse)',
    'https://biorxiv.org/content/10.1101/2020.10.12.336230v1 (abstract page); PDF https://www.biorxiv.org/content/biorxiv/early/2020/10/12/2020.10.12.336230.full.pdf',
    'abstract_only',
    'Abstract: "reference lists tend to include more papers with a White person as first and last author than would be expected"; imbalance "driven largely by the citation practices of White authors, and is increasing over time".',
    'OK', 'bioRxiv PDF returned HTTP 429 (Cloudflare rate limit 1015) on every attempt; not peer-reviewed/published elsewhere; no other OA host found (Unpaywall: not OA; Europe PMC PPR224995 links only to bioRxiv). Retry the PDF from a normal browser. bioRxiv licence forbids reuse of figures without permission.')
add('NEURO-05', 'Gender bias in academia: A lifetime problem that needs solutions',
    'Llorens A, Tzovara A, Bellier L, et al. (2021). Neuron 109(13) (Perspective, 7 July 2021). DOI 10.1016/j.neuron.2021.06.002; PMC8553227',
    'https://www.cns.nyu.edu/wanglab/publications/pdf/llorens.neuron2021.pdf (author-lab PDF); full text XML from PMC8553227',
    'downloaded',
    'p.2048: SfN - women applicants to PhD programs rose "from 38% in 2000-2001 to 57% in 2016-2017"; "women represented only 30% of all faculty for PhD programs".',
    'OK', 'Fig. 1 (p.2049) and Table 2 (6 rotated pages, saved as table2_part1-6) cropped at 300 dpi.')
add('NEURO-06', 'Gender bias in (neuro)science: facts, consequences and solutions',
    'Schrouff J, Frau-Pascual A, Pischedda D, Genon S, Fryns G, Pinho AL, Vassena E, Liuzzi AG, Ferreira FS (2019). Eur J Neurosci 50(7):3094-3100. DOI 10.1111/ejn.14397',
    'https://iris.unitn.it/retrieve/e3835195-58e6-72ef-e053-3705fe0ad821/Schrouff%26al_2019_Pre-rev_version.pdf (pre-review author version, Univ. Trento repository)',
    'downloaded',
    'Fig. 1 / Methods: women under-represented as conference speakers across n=295 events 2015-2018 (BiasWatchNeuro data; p=5.7e-80); also prizes (n=23 awards), first/last authors (n=1760 journal-years), seminar series (n=38).',
    'OK', 'Pre-review version: numbers/figures may differ slightly from the EJN version of record. Fig 2 caption is on p.7, image on p.6.')
add('NEURO-07', 'Executive Summary of Report of Neuroscience Departments & Programs Survey, Academic Year 2016-2017',
    'Society for Neuroscience (2017/2018). SfN NDP Survey executive summary.',
    'https://www.sfn.org/-/media/SfN/Documents/Survey-Reports/Final-SfN_2016-NDP-Survey-Executive-Summary.pdf',
    'downloaded',
    'p.1: "Women represented 30% of tenure-stream faculty in doctoral graduate programs, a number that has changed little during the past decade." p.2: 57% of applicants, 58% admitted, 53% began training.',
    'OK', 'Text-only summary (no charts); pipeline bars redrawn from stated numbers (data/neuro07_sfn2016_pipeline.csv).')
add('NEURO-08', 'Supporting Female Neuroscientists in Their Careers',
    'Society for Neuroscience (spring 2018). Neuroscience Quarterly.',
    'https://sfn.org/publications/neuroscience-quarterly/spring-2018/women-in-neuroscience',
    'downloaded',
    'Women were 51% of US PhD program applicants in 2010-11, "57 percent of applicants and 58 percent of enrollees in 2016-17"; women 30% of faculty in US PhD programs, 32% master\'s, 44% undergraduate programs.',
    'OK', 'Web article, no figure; 2010 vs 2016 pipeline redrawn (data/neuro08_sfn2018_pipeline.csv).')
add('NEURO-09', 'Women in neuroscience: Where are we in 2019?',
    'Machlovi S, Pero A, Ng S, Zhong M, Cai D (2021). J Neurosci Res 99(1):9-12. DOI 10.1002/jnr.24570; PMC7754118',
    'https://rcastoragev2.blob.core.windows.net/904567a72136304394b5d2782423da04/PMC7754118.pdf ; full-text XML PMC7754118',
    'downloaded',
    'p.9: in 2017-18 women were 53% of PhD matriculates, 30.8% of tenure-track faculty "but only 13.8% of tenured full professors"; neuroscience journals 2005-2017: 29.8% of authors, 33.1% of first authors, 18.1% of last authors (citing Bendels et al. 2018; Shen et al. 2018).',
    'OK', 'Commentary has no figures; first vs last author shares redrawn (data/neuro09_machlovi2021_authorship.csv). Numbers are second-hand.')
add('NEURO-10', 'Making meetings more equal (How to banish manels and manferences from scientific meetings)',
    'Else H (2019). Nature 573:184-186 (News Feature, 12 Sep 2019). DOI 10.1038/d41586-019-02658-6',
    'https://media.nature.com/original/magazine-assets/d41586-019-02658-6/d41586-019-02658-6.pdf ; landing page https://www.nature.com/articles/d41586-019-02658-6',
    'downloaded',
    'p.185: "In neuroscience, the proportion of female speakers almost doubled, rising from 24% in 2011 to 42% in 2019" (9 conferences); graphic "A changing balance" p.185.',
    'OK', 'Graphic cropped (fig1); start/end shares for 4 disciplines saved to data/neuro10_else2019_speaker_share.csv. "Full data" shortlink go.nature.com/2jumtdx redirects to the article (no separate dataset reachable).')
add('NEURO-11', 'Lessons from an initiative to address gender bias',
    'Hoy KE, Fitzgibbon BM, Brem A-K (2021). eLife 10:e75818 (Point of View). DOI 10.7554/eLife.75818; PMC8673833',
    'https://pmc-oa-opendata.s3.amazonaws.com/PMC8673833 (PMC OA bucket: PDF + figure JPGs)',
    'downloaded',
    'p.1: 1st Int. Brain Stimulation Conference (Singapore 2015) "just two of the 39 invited speakers were female"; Barcelona 2017 "all 10 invited speakers were male" (BiasWatchNeuro base rate 34%).',
    'OK', 'Figs are a protest-poster photo (fig1) and a map of the Women in BrainStim database (fig2); before/after counts redrawn (data/neuro11_hoy2021_brainstim_speakers.csv).')
add('NEURO-12', 'Tails You Win, One Tail You Lose (Cosyne 2019 gender bias analysis)',
    'Frye C (6 Mar 2019). Blog post, charlesfrye.github.io.',
    'https://charlesfrye.github.io/stats/2019/03/06/cosyne19-gender-bias.html',
    'downloaded',
    'Quoted tweet (M. Carey, 2 Mar 2019): first authors with known gender - Female 83/264 accepted = 31.4%; Male 255/677 = 37.7%; one-tailed vs two-tailed test p approx. 0.03 vs 0.07.',
    'OK', 'No raw data file linked; counts saved to data/neuro12_cosyne2019_acceptance.csv; embedded welcome-talk slide saved as fig1; linked post neuroecology "#Cosyne19, by the numbers" saved.')
add('NEURO-13', 'Addressing Gender and Institutional Bias at Cosyne',
    'Simons Foundation / Simons Collaboration on the Global Brain (28 Aug 2020). Interview with A.-M. Oswald and S. Ostojic.',
    'https://www.simonsfoundation.org/2020/08/28/addressing-gender-and-institutional-bias-at-cosyne/',
    'downloaded',
    'Each Cosyne 2020 abstract got 2 single-blind + 2 double-blind reviews; under single blind, female first and last authors scored significantly lower; double-blind improved female first-author scores but not significantly and had no effect for female last authors. Reviewer pool and program committee raised to 30% women; ~17% of submissions from women.',
    'OK', 'No linked report or numeric score gaps on the page (results said to be published later); no figure to extract.')
add('NEURO-14', 'Developing Knowledge that Improves Lives for All (Bias in neuroscience)',
    'Wachspress E (16 Oct 2020). UChicago Neuroscience Institute news/blog.',
    'https://neuroscience.uchicago.edu/biasinneuroscience',
    'downloaded',
    'Cosyne 2020 chairs Oswald & Ostojic "made sure 50% of podium talks were by women, an ongoing initiative for Cosyne"; women on program committee/referees raised "to a third or more", vs approx. 20% women in the field.',
    'OK', 'Narrative page, no figure or outcome numbers beyond the policy.')
add('NEURO-15', 'BiasWatchNeuro', 'BiasWatchNeuro (2015-2023). Blog tracking speaker gender ratios at neuroscience meetings.',
    'https://biaswatchneuro.com ; posts via WordPress.com public REST API https://public-api.wordpress.com/wp/v2/sites/biaswatchneuro.com/posts?per_page=100&page=1..8 (site-local /wp-json returns 404)',
    'downloaded',
    '740 posts (Aug 2015 - Sep 2023); 676 parsed into data/biaswatchneuro.csv; pooled share of women among listed speakers 3859/11720 = 32.9%; 274 of 657 events with a base rate were below their estimated base rate.',
    'n.a.', 'Key number is descriptive; per-post ratio line chosen by label priority (overall/invited speakers over keynote-only); 6 rows flagged where the site\'s own % disagrees with its counts (e.g. AI & Brain Science 2020 lists 19 W : 7 M (27%) - probably swapped). 64 posts had no ratio line (essays, screenshot-only).',
    extra='Parser: scripts/biaswatchneuro_scrape.py; raw API dump api/posts_all.json; redraw by post year in figures/NEURO-15_redraw.png (year = post date, not meeting date).')
add('NEURO-16', 'anneslist - Highlighting female systems neuroscientists', 'anneslist (A. Churchland et al.), web directory.',
    'https://anneslist.net', 'downloaded', 'Directory front page; no statistics.', 'n.a.',
    'Front page HTML saved (no screenshot tool used).')

def rel(p): return os.path.relpath(p, '.')
for i, e in E.items():
    d = S + i
    files = sorted(f for f in glob.glob(d + '/**/*', recursive=True) if os.path.isfile(f) and '/figures/' not in f and not f.endswith('notes.md'))
    figs = sorted(f for f in glob.glob(d + '/figures/*') if os.path.basename(f).startswith(i))
    allfig = sorted(glob.glob(d + '/figures/*'))
    data = {'NEURO-07': ['data/neuro07_sfn2016_pipeline.csv'], 'NEURO-08': ['data/neuro08_sfn2018_pipeline.csv'],
            'NEURO-09': ['data/neuro09_machlovi2021_authorship.csv'], 'NEURO-10': ['data/neuro10_else2019_speaker_share.csv'],
            'NEURO-11': ['data/neuro11_hoy2021_brainstim_speakers.csv'], 'NEURO-12': ['data/neuro12_cosyne2019_acceptance.csv'],
            'NEURO-15': ['data/biaswatchneuro.csv']}.get(i, [])
    md = [f'# {i}: {e["title"]}', '', f'- **Citation:** {e["citation"]}', f'- **url_used:** {e["url"]}',
          f'- **Access status:** {e["status"]}', '- **Files:** ' + (', '.join(os.path.relpath(f, d) for f in files) or 'none'),
          '- **Figures:** ' + (', '.join(os.path.relpath(f, d) for f in allfig) or 'none'),
          '- **Data:** ' + (', '.join('../../../' + x for x in data) or 'none'), '',
          f'**Headline number (from source):** {e["headline"]}', '',
          f'**Key number in SOURCES.md check:** {e["check"]}', '', f'**Notes:** {e["notes"]}']
    if e['extra']: md += ['', e['extra']]
    open(d + '/notes.md', 'w').write('\n'.join(md) + '\n')
    st = dict(id=i, title=e['title'], url_used=e['url'], file_paths=[rel(f) for f in files + [d + '/notes.md']] + data,
              access_status=e['status'], figures_extracted=[rel(f) for f in figs],
              notes=(f'Key number check: {e["check"]}. ' + e['notes']).replace('\n', ' '))
    json.dump(st, open(f'gender-bias-data/_status/{i}.json', 'w'), indent=1, ensure_ascii=False)
print('ok', len(E))
