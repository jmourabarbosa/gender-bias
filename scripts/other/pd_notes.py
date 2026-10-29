"""Write notes.md and _status/<ID>.json for PREC-01..15 and DIS-01..12. usage: python3 -I pd_notes.py"""
import json, glob, os
ROOT = '/home/user/gender-bias'
D = f'{ROOT}/other-biases-data'
S = 'source.pdf'

M = {}
def add(i, **k): M[i] = k

add('PREC-01', title='Les enseignants contractuels affectés dans l\'enseignement supérieur - Année 2024 (Note de la DGRH n°6-2025)',
    cite='MESR-DGRH (A.-S. Beaurenaut), Note de la DGRH - Enseignement supérieur n°6-2025, published Jan 2026.',
    url='https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-01/note-dgrh-n-6---2025---enseignants-contractuels-ann-e-2024-pdf-39144.pdf',
    access='downloaded', key='21,080 contract vs 61,879 tenured',
    found='2024: 21,080 contract teachers (text p1; table fig.2 p2 gives 21,084) vs 61,879 tenured; 25% of teachers (25.4% in table). Excludes 164,500 vacataires (p5).',
    match='MATCH', figs={'PREC-01_redraw.png': 'data/PREC-01.csv (fig.2 table p2 of this note + 3 earlier editions)'},
    extra='Series: earlier editions downloaded to series/ (Note DGRH n°4-2017 "enseignants non permanents 2015-2016", n°5-2022 (2020-2021), n°4-2023 (2022), n°3-2024 (2023)). data/PREC-01.csv merges contract vs tenured headcounts for 2000, 2005, 2010, 2012-2024 (2011 not in any edition retrieved). The 2016 value is the first year that includes L954-3 contract staff (break in series). Figure 1 (p1) is a chart of contract headcount since 2008; the fig.2 table on p2 holds the numbers, so no crop was made beyond the redraw.')
add('PREC-02', title='Dossier "Les effectifs d\'enseignant-es titulaires en baisse depuis 2010" / "Des choix budgétaires qui structurent l\'emploi", Le Snesup n°734',
    cite='SNESUP-FSU (R. Grüber; P. Aubry), Le Snesup n°734, June-Aug 2025, pp.10-15.',
    url='https://www.snesup.fr/sites/default/files/2025-06/dossier-mensuel-snesup734.pdf', access='downloaded',
    key='EC posts 3,613 (2011) -> 2,378 (2023)',
    found='"le nombre d\'ouvertures d\'emplois d\'EC autorisées est passé de 3 613 (campagne 2011) à 2 378 (campagne 2023), soit une baisse de plus de 34 %" (printed p11 = PDF p3). Teachers per 100 students 5.6 -> 4.4 (2008-09 to 2022-23, PDF p7).',
    match='MATCH. Cross-check against official DGRH notes: 3,613 = posts AUTHORISED in 2010 and 2011 (DGRH bilan 2011 p6, bilan 2013 p10) and 2,378 = posts authorised in 2023 (Note DGRH n°2-2025 p1). The union figures are correct but are authorised ceilings; posts actually PUBLISHED were 2,792 (2011) and 2,280 (2023), a 18% fall (see PREC-03/data/posts_candidates_series.csv).',
    figs={'PREC-02_fig1.png': 'PDF p7 (printed p15): staff-student ratio and budget per student 2008-09 to 2023-24',
          'PREC-02_fig2.png': 'PDF p3 (printed p11): table, change in headcount by body 2010-2023',
          'PREC-02_fig3.png': 'PDF p2 (printed p10): map of EC/E2D headcount change by académie',
          'PREC-02_redraw.png': 'data/PREC-02.csv (p11 table)'},
    extra='The infographic on p7 is a dual-axis chart in the original (left: euros, right: teachers per 100 students); the redraw only shows the table of changes by body to avoid a dual axis.')
add('PREC-03', title='La campagne de recrutement et d\'affectation des MCF et des PR - Session 2023 (Note de la DGRH n°2-2025) + all campaign reports back to 2008',
    cite='MESR-DGRH (M. Le Gendre), Note de la DGRH n°2-2025, Oct 2025; series of DGRH campaign reports 2006-2026 (series/).',
    url='https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-10/note-dgrh-n-2---2025---campagne-2023-pdf-38079.pdf', access='downloaded',
    key='1,567 MCF posts, 8,110 candidates',
    found='2023: 1,567 MCF posts published, 49,141 applications by 8,110 candidates, 5.2 candidates per post (p2 and fig.2 table p2); 2,280 posts published, 2,378 authorised (p1).',
    match='MATCH',
    figs={'PREC-03_fig1.png': 'PDF p1: fig.1 posts authorised/published/filled 2014-2023',
          'PREC-03_fig2.png': 'PDF p2: fig.2 table posts, applications, candidates by discipline 2023',
          'PREC-03_redraw.png': 'data/posts_candidates_series.csv'},
    extra='SERIES (data/posts_candidates_series.csv; year, MCF posts, PR posts, total published, authorised, MCF candidates, candidates per MCF post, status, basis, source+page). Files in series/: campaign reports 2011 (bilan, 103 p), 2013 (bilrec13, 98 p; holds 2004-2013 posts chart p10 and candidate changes 2007-2013 p12), 2014 (bilan), 2015 (Note n°5-2016), 2016 (Note n°6-2017), 2017 (Note n°6-2018), 2018 (Note n°7-2019), 2020 (Note n°7-2021, copy hosted by Université de Lorraine), 2024 (Note n°1-2026), provisional bilans 2022/2024/2025, plus 2006/2007 bilans and the 2008 candidate study. 2021 = PREC-04, 2023 = this source. trajectoire*.pdf are the companion "trajectoire professionnelle" notes (2015, 2019), downloaded by mistake but kept (previous status of recruits, useful for PREC-05).\n'
          'Gaps and caveats: (1) no separate campaign PDFs found for 2008, 2009, 2010, 2012 (their posts come from the 2013 report chart labels, their candidate counts are back-computed from the year-on-year changes printed in the 2011/2013 reports; the back-computed 2010-2012 ratios reproduce the official 5.08/5.52/5.53, which validates the method); (2) 2019 and 2022 final campaign notes (Notes d\'information DGRH 20-06 and 23-06) are listed on the ministry site but the site\'s HTML pages are behind a Cloudflare block for this client and no PDF URL could be found, so 2019 has no candidate figure and 2022 uses the provisional July bilan (6.1); 2019/2022 posts and 2014/2022 authorised posts were read from the vector lines of fig.1 of the 2023 note (script scripts/other/prec03_fig1_vector.py; it reproduces the stated values for 2015, 2016, 2019, 2022 exactly); (3) the post base of the official ratio changes: 2014-2015 use synchronised-session posts only (on all published posts the ratio would be 6.4 and 6.9), 2018 excludes art. 29 posts.')
add('PREC-04', title='La campagne de recrutement et d\'affectation des MCF et des PR - Session 2021 (Note de la DGRH n°7, Sept 2022)',
    cite='MESR-DGRH, Note de la DGRH - Enseignement supérieur n°7, September 2022.',
    url='https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2023-01/note-dgrh-n-7-septembre-2022---campagne-2021-26095.pdf', access='downloaded',
    key='7.7 candidates per MCF post',
    found='"Pour les 1 106 postes de MCF publiés, 45 762 candidatures recevables ont été déposées par 8 504 candidats, soit 41,4 candidatures et 7,7 candidats par poste" (PDF p2; same in fig.2 table p2).',
    match='MATCH', figs={'PREC-04_fig1.png': 'PDF p2: fig.2 table by discipline 2021 (LSH 10.4 candidates per MCF post)',
                         'PREC-04_redraw.png': 'candidates per MCF post 2008-2025 from PREC-03/data/posts_candidates_series.csv'},
    extra='The candidates-per-post series for all years lives in ../PREC-03/data/posts_candidates_series.csv (see PREC-03 notes for definitions and gaps). Peak 7.7-7.8 in 2015 and 2021; falls to ~5 in 2023-2024 as posts rose.')
add('PREC-05', title='Trajectoire professionnelle des enseignants-chercheurs recrutés en 2023 (Note de la DGRH n°3-2025) (= LOC-02)',
    cite='MESR-DGRH, Note de la DGRH n°3-2025 (same document as LOC-02).', url='see other-biases-data/01-localism/LOC-02/source.pdf',
    access='downloaded', key='New MCF age 35; 42% from postdoc',
    found='MCF recruited at 35 on average (PR 47), up from 33 a decade earlier (LOC-02 PDF p1-2, fig.5 p3); 42% of 2023 MCF recruits were postdocs (p1, fig.3 p2); ATER non-civil-servants 13% in 2023 vs 37% in 2005 (p1).',
    match='MATCH', figs={'PREC-05_fig1.png': 'LOC-02 PDF p2: fig.2 (previous activity of MCF recruits 2003-2023) and fig.3 (2023 by discipline)',
                         'PREC-05_fig2.png': 'LOC-02 PDF p3: fig.5 mean age at hiring by discipline, MCF and PR, 2023',
                         'PREC-05_redraw.png': 'data/PREC-05.csv (postdoc share by discipline)'},
    extra='No file duplicated: the PDF stays in ../../01-localism/LOC-02/source.pdf; crops were made from it. The 2005 postdoc share (~24%) is read off the fig.2 curve and is approximate; the ATER 37% (2005) is stated in the text.')
add('PREC-06', title='Confronté à un "mur du vieillissement", le CNRS doit revoir sa politique d\'attractivité (Acteurs Publics)',
    cite='M. Malaterre, Acteurs Publics, 9 April 2025 (on the Cour des comptes report on the CNRS 2013-2023).',
    url='https://acteurspublics.fr/articles/confronte-a-un-mur-du-vieillissement-le-cnrs-doit-revoir-sa-politique-dattractivite-pour-assurer-la-perennite-de-ses-activites/',
    access='downloaded', key='CR recruitment age 34.4 (2020)',
    found='"Un âge moyen qui est passé de 30 ans à près de 34 ans en 2013, puis à 34,4 ans en 2020" (page.html). Primary source PREC-07 p44: 30 (2006), 33.9 (2013), 34.4 since 2020.',
    match='MATCH (confirmed in the primary Cour des comptes report, PREC-07 PDF p44)', figs={},
    extra='Secondary press article; page saved by the first pass (real article, not a challenge page; the article may be partly behind a subscription wall but the quoted passage is present). Use PREC-07 for figures/data (PREC-07/data/PREC-07_staff_age.csv).')
add('PREC-07', title='Le Centre national de la recherche scientifique (CNRS), exercices 2013-2023 - rapport d\'observations définitives',
    cite='Cour des comptes, 2025 (copy hosted by Campus Matin).', url='https://campusmatin.com/file/a706bd62d95ab4dcc9c1a4df08973ee9/rapport-cour-comptes-exercices-2013-2023-cnrs.pdf',
    access='downloaded', key='Contract staff 23% -> 29%',
    found='"la part des contractuels financés sur ressources propres augmente peu à peu (29 % des effectifs en 2023 contre 23 % en 2013)" (PDF p7). Annex table 2 (p114): contract staff 9,445 ETPT (27.8%) in 2013 -> 11,034 (32.2%) in 2023. CR recruitment age 30 (2006) -> 33.9 (2013) -> 34.4 (2020) (p44).',
    match='MATCH (note: 23%->29% is the share funded on own resources; all contract staff are 27.8%->32.2% of ETPT)',
    figs={'PREC-07_fig1.png': 'PDF p49: Graphique 11, selection rate of CNRS competitions 2013-2022',
          'PREC-07_fig2.png': 'PDF p114: annex Tableau 2, staff in ETPT 2013/2022/2023 by status',
          'PREC-07_redraw.png': 'data/PREC-07_selection_rate.csv'},
    extra='The age-at-recruitment "series" exists only as three numbers in the text (p44); they are in data/PREC-07_staff_age.csv. "Applications vs posts" is given as selection rates (Graphique 11), read from the vector chart by scripts/other/prec07_fig11_vector.py (+-0.05 pt). The ccomptes.fr copy was not fetched (the Campus Matin copy is the full report, 131 pages).')
add('PREC-08', title='Les docteurs diplômés en 2024 / doctorants 2024-2025 (Note Flash SIES n°14, juin 2025)',
    cite='MESR-SIES (A. Le Chanu), Note Flash n°14, June 2025.', url='https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-06/nf-2025-14-37279.pdf',
    access='downloaded', key='81% funded; 53% in humanities',
    found='81% of first-year doctoral students funded in 2024-25; 98% exact sciences, 86% life sciences, 53% humanities & social sciences (PDF p2 text and table).',
    match='MATCH', figs={'PREC-08_fig1.png': 'PDF p2: table, funded share by field 2023-24 and 2024-25 (source is a low-resolution embedded image, cropped at 400 dpi)',
                         'PREC-08_redraw.png': 'data/PREC-08.csv'}, extra='')
add('PREC-09', title='Question écrite n°1155 (17e législature), Vacataires de l\'enseignement supérieur, with ministry answer',
    cite='Assemblée nationale, question by Mme Sylvie Ferrer; answer JO 8 April 2025 p2486.', url='https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1155.pdf',
    access='downloaded', key='€8.37/h effective',
    found='"il gagne 43,50 euros/heure face étudiants ... sa rémunération est donc de 8,37 euros/heure, un taux nettement inférieur au SMIC horaire" (PDF p1, question text).',
    match='MATCH, but note: 8.37 is the deputy\'s worked example (43.50 / (1 + 4.2 h prep)), not an official statistic; the ministry answer (p1-2) does not confirm it (it says 150,000+ vacataires, only 10% earn > EUR 4,000 gross/yr).',
    figs={'PREC-09_redraw.png': 'data/PREC-09.csv'}, extra='SMIC 11.88 EUR gross/h (from 1 Nov 2024) added by the collector as a reference line; it is not in the source.')
add('PREC-10', title='Les chaires de professeur junior : premier bilan (Le Snesup n°728, p19)',
    cite='SNESUP-FSU secteur Situation des personnels, Le Snesup n°728, Nov 2024, p19.', url='https://www.snesup.fr/sites/default/files/2024-11/cpjpremierbilan_p19ndeg728.pdf',
    access='downloaded', key='25% women in junior chairs',
    found='"les femmes ne représentent que 25 % des CPJ recrutées en 2021-2022, très loin des 42 % de femmes parmi les PU recrutés lors de la campagne d\'emploi 2022" (PDF p1).',
    match='MATCH. Cross-check: the DGRH 2021 campaign note (PREC-04 p2) gives 42% women among PR recruited in 2021, consistent with the 42% PU benchmark.',
    figs={'PREC-10_fig1.png': 'PDF p1: infographic, CPJ 2021-22 opened/filled and PU 2022 published/filled by discipline', 'PREC-10_redraw.png': 'data/PREC-10.csv'}, extra='Union source; the CPJ counts by discipline were not cross-checked against the DGRH CPJ bilans (provisional bilans in PREC-03/series/ give CPJ totals for 2022, 2024, 2025).')
add('PREC-11', title='Changing demographics of scientific careers: The rise of the temporary workforce',
    cite='Milojević S, Radicchi F, Walsh JP (2018). PNAS 115(50):12616-12623. doi:10.1073/pnas.1800478115 (PMC6294951).',
    url='https://re.public.polimi.it/bitstream/11311/1313878/1/milojevic%cc%81-et-al-2018-changing-demographics-of-scientific-careers-the-rise-of-the-temporary-workforce.pdf (via Unpaywall; Politecnico di Milano repository)',
    access='downloaded', key='Half leave within ~5 years',
    found='"The time over which half of the cohort has left the field has shortened from 35 y in the 1960s to only 5 y in the 2010s" (PDF p1 abstract); fig.4D p4.',
    match='MATCH', figs={'PREC-11_fig1.png': 'PDF p4: Fig. 4, survival curves by cohort (A-C) and half-life by cohort year (D)', 'PREC-11_redraw.png': 'data/PREC-11.csv'},
    extra='Repository copy is the published PNAS PDF (Unpaywall labels it submittedVersion). Not in the PMC OA bucket (PNAS non-OA licence). page.html = PMC landing page from the first pass.')
add('PREC-12', title='The Postdoc Queue: A Labour Force in Waiting',
    cite='Andalib MA, Ghaffarzadegan N, Larson RC (2018). Systems Research and Behavioral Science 35(6):675-686. doi:10.1002/sres.2510.',
    url='https://dspace.mit.edu/server/api/core/bitstreams/215d27e9-9eaa-47ab-9281-489eaf2df3cc/content (MIT DSpace hdl 1721.1/122786, found via Unpaywall)',
    access='downloaded', key='~17% reach tenure track',
    found='"We find that only about 17% of postdocs ultimately land tenure-track positions" (PDF p2 abstract); Table 1 p9: P{reneging}=0.83 all fields, 0.69 biomedical.',
    match='MATCH', figs={'PREC-12_fig1.png': 'PDF p9: Table 1, queue properties by field', 'PREC-12_fig2.png': 'PDF p5: Figure 3, postdoc queue model (the "funnel")',
                         'PREC-12_redraw.png': 'data/PREC-12.csv'},
    extra='Author\'s final manuscript (CC BY-NC-SA 4.0), not the Wiley version of record; page numbers refer to the 13-page MIT PDF. dspace.html = repository landing page; page.html = EconPapers page from the first pass.')
add('PREC-13', title='Changes in the National Cancer Institute\'s R01 workforce: growth, aging, retention, and policy implications',
    cite='Antman KH et al. (2021). J Clin Invest 131(7):e146925. doi:10.1172/JCI146925 (PMC8011905).',
    url='https://jci.org/articles/view/146925/files/pdf (served from dm5migu4zj3pb.cloudfront.net JCI146925.v1.pdf); supplement JCI146925.sd.pdf',
    access='downloaded', key='Age at first R01 36.2 -> 44.9',
    found='"the age of PIs with PhDs at the time of first NCI R01 award increased from an average of 36.2 years in FY 1990 to 44.9 years in FY 2016. Likewise, the median age increased from 36 to 43 years" (PDF p5).',
    match='MATCH', figs={'PREC-13_fig1.png': 'supplementary/JCI146925.sd.pdf p3 (full rotated page): Suppl. Fig. 3, age at first R01 1990-2016',
                         'PREC-13_fig2.png': 'source.pdf p3: Figure 2, age distribution of NCI PIs 1990-2016',
                         'PREC-13_redraw.png': 'data/PREC-13.csv (medians read from Suppl. Fig. 3)'},
    extra='The JCI PDF first returned "website under heavy load (queue full)" (503); a later single retry succeeded. PMC and Europe PMC PDF routes return reCAPTCHA/Cloudflare challenges and were not used. figures/JCI146925.*.jpg are the journal\'s "large" web figure images (full set incl. tables).')
add('PREC-14', title='Postdocs in crisis: science cannot risk losing the next generation (Nature editorial) + survey feature',
    cite='Nature editorial, Nature 585:160 (2020), doi:10.1038/d41586-020-02541-9; survey feature: Woolston C, "Pandemic darkens postdocs\' work and career hopes", Nature 585:309-312 (2020), doi:10.1038/d41586-020-02548-2.',
    url='https://www.nature.com/articles/d41586-020-02541-9', access='downloaded', key='51% considered leaving over mental health',
    found='"51% of respondents to the latest survey have considered leaving active research because of work-related mental-health concerns" (editorial, page.html). Also 23% sought help for anxiety/depression, 26% would like help; >7,600 respondents.',
    match='MATCH', figs={'PREC-14_redraw.png': 'data/PREC-14.csv (numbers from the free editorial)'},
    extra='The editorial is free. The survey feature with the original bar charts (page_survey-feature_d41586-020-02548-2.html) is paywalled: only the first paragraph is visible, so its charts were NOT downloaded (institutional access needed for the chart images).')
add('PREC-15', title='Age dynamics in scientific creativity',
    cite='Jones BF, Weinberg BA (2011). PNAS 108(47):18910-18914. doi:10.1073/pnas.1102895108 (PMC3223465). Summary: Lindau Nobel Laureate Meetings blog "Geniuses are getting older", 22 June 2016.',
    url='https://pmc.ncbi.nlm.nih.gov/articles/PMC3223465/ (full-text HTML) ; https://www.lindau-nobel.org/?p=22157',
    access='downloaded', key='Age at Nobel work 36.9 -> 50.3 (physics)',
    found='Lindau page: physics laureates made their discoveries at 36.9 (early period) vs 50.3 (later period); PNAS text (Results, Fig. 1B): mean age of prize-winning work rose by 13.4 y in physics, 10.2 y chemistry, 7.4 y medicine (early = work before 1905, late = after 1985). 36.9 + 13.4 = 50.3.',
    match='MATCH (the 36.9/50.3 levels are from the Lindau summary; the paper text gives the 13.4-year difference, consistent; levels are shown in Fig. 1A)',
    figs={'PREC-15_fig1.jpg': 'PMC figure image for Fig. 1 (low resolution, 428 px; the PDF could not be fetched)', 'PREC-15_redraw.png': 'data/PREC-15.csv'},
    extra='access_status=downloaded refers to the full-text HTML on PMC (page_pmc.html) plus PMC figure images; the PDF is NOT available: pnas.org returns 403 (bot protection), PMC PDF route returns a reCAPTCHA page, Europe PMC a Cloudflare challenge, and the article is not in the PMC OA bucket. A high-resolution Fig. 1 needs the PDF via institutional access.')

add('DIS-01', title='Plan "handicap" 2026-2031, quelles ambitions ? (Le Snesup n°743, Métier p18)',
    cite='SNESUP-FSU, Le Snesup n°743, June-Aug 2026, p18.', url='https://www.snesup.fr/sites/default/files/2026-06/metier_snesup-ndeg743p18.pdf',
    access='downloaded', key='ESR disability rate 4.49% vs 6%',
    found='"l\'obligation d\'emploi dans l\'ESR atteint péniblement les 4,49 %, un chiffre bien en deçà des 6 % exigés par la loi ... (3,67 % à l\'université de Strasbourg et 5,25 % à Toulouse Paul-Sabatier)" (PDF p1).',
    match='MATCH. Official cross-check: no national official ESR rate found online (MESR bilan social pages blocked; the 2026-2031 plan page is behind Cloudflare). Partial official checks in crosscheck/: Université de Lorraine direct rate 3.68% in 2023 (its own bilan, p4); MEN+MESR combined declared rate 3.31% in 2008 (AN answer to question 13-52233); SNESUP fiche cites "about 3%" for 2018-19. These are consistent with an ESR rate below 6% but do not verify 4.49% itself (year and definition, e.g. direct vs legal rate, not stated by SNESUP).',
    figs={'DIS-01_redraw.png': 'data/DIS-01.csv (union figures grey, official black, 6% quota line)'}, extra='The source page has no chart, so there is no crop.')
add('DIS-02', title='Compte rendu AG section Handicap SNCS, 17 June 2025', cite='SNCS-FSU, 2025.',
    url='https://sncs.fr/wp-content/uploads/2025/09/250617-CR_AG-Hand-SNCS_Internet.pdf', access='failed', key='CNRS 5.3%; ~1.5% among DR',
    found='Not verified: sncs.fr returns HTTP 403 (server-side block) to this client, with the standard and with a browser user-agent. A web-search summary of the document reports "CNRS at 5.3% in 2023" and an earlier SNCS report "5.7% in 2022, 1,382 BOE agents"; the ~1.5% among DR could not be seen.',
    match='UNVERIFIED (document not obtained). Official cross-check: no CNRS bilan social with a BOE rate could be retrieved; the Cour des comptes CNRS report (PREC-07) gives no disability rate.',
    figs={}, extra='Needs the user to download the PDF in a browser (sncs.fr blocks automated clients). The CNRS "bilan social"/RSU (intranet) is the official source to cross-check.')
add('DIS-03', title='Plan handicap Inserm 2023-2025 (prorogé en 2026) - suivi des axes, objectifs et actions',
    cite='Inserm DRH, plan handicap 2023-2025 (FIPHFP-Inserm convention), follow-up version updated 03.09.2026.',
    url='https://pro.inserm.fr/wp-content/uploads/2025/03/Suivi-des-axes-objectifs-et-actions-du-plan-handicap_Actualise-au-03.09.2026.pdf',
    access='downloaded', key='Not verified',
    found='The listed URL (PlanHandicapInserm_2023- 2025.pdf) is now 404 with both encodings; the plan page links an updated follow-up PDF (source.pdf, 7 p) which only states the target "taux d\'emploi supérieur aux 6 %" (p2), no actual rate. Official Inserm rate found elsewhere on pro.inserm.fr: "taux d\'emploi ... qui atteint 6,12 % pour l\'année 2020" (page_gilles-bloch-2021.html).',
    match='No key number to match; Inserm rate = 6.12% (2020), official Inserm web page. No more recent rate online.',
    figs={}, extra='web_images/ holds the Inserm infographic PNGs (barometer: e.g. 49% Inserm vs 56% national, 70% adapted workstations, 79% satisfaction) - survey indicators, not employment rates. No figure extracted (no chart of the rate exists).')
add('DIS-04', title='ACADISCRI first results (= ETH-04)', cite='Cognet M, Hajjat A, Hamel C et al. (2022), ACADISCRI, first results.',
    url='see other-biases-data/03-ethnic/ETH-04/source.pdf', access='downloaded', key='13.8% of LGBTQ+ staff face LGBT-phobic treatment',
    found='LGBTQI-phobic unequal treatment affects 2.1% of staff (women 2.9%), but 13.8% of people identifying as homosexual, bisexual, asexual or trans; ableist treatment 9.4% of staff with a significant health problem vs 1.8% in good health (ETH-04 PDF p11; all-staff ableist 4.2% p9).',
    match='MATCH', figs={'DIS-04_fig1.png': 'copy of ETH-04_fig3.png = ETH-04 PDF p10, Tableau 1 (acts by perceived motive incl. LGBTphobia, validisme)',
                         'DIS-04_redraw.png': 'data/DIS-04.csv'}, extra='Staff of one university (2019-20). The PDF is not duplicated; see ETH-04.')
add('DIS-05', title='Dénoncer les discriminations vécues à l\'université (Défenseur des droits, Éclairages 2024) (= ETH-05)',
    cite='Défenseur des droits, April 2024.', url='see other-biases-data/03-ethnic/ETH-05/source.pdf', access='downloaded',
    key='Reporting: students 17-21%, staff 43-51%',
    found='Victims who reported: LGBT-phobia students 17.1% / staff 42.5%; ableism students 20.6% / staff 51.0% (ETH-05 PDF p17, Graphiques 5-6); all motives 13.2% / 46.5% (p12).',
    match='MATCH (17-21% = LGBT-phobia 17.1 and ableism 20.6 for students; 43-51% = 42.5 and 51.0 for staff)',
    figs={'DIS-05_fig1.png': 'copy of ETH-05_fig2.png = ETH-05 PDF p17, Graphique 5 (students, by motive)',
          'DIS-05_fig2.png': 'copy of ETH-05_fig3.png = ETH-05 PDF p17, Graphique 6 (staff, by motive)', 'DIS-05_redraw.png': 'data/DIS-05.csv'},
    extra='The PDF is not duplicated; see ETH-05.')
add('DIS-06', title='Fiche 2.4 - Les étudiants handicapés (DREES, Le handicap en chiffres, édition 2024, mise à jour août 2025)',
    cite='DREES, Panorama "Le handicap en chiffres", fiche 2.4.',
    url='https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-08/Fiche%202.4%20-%20Les%20%C3%A9tudiants%20handicap%C3%A9s.pdf',
    access='failed', key='~58,880 (~2%)',
    found='Not obtained: drees.solidarites-sante.gouv.fr (with and without www) is unreachable from this session (the egress proxy connection is closed before any HTTP response, i.e. a network/policy failure, not a site answer). The MESR open-data portal (alternative source) was also unreachable. A web-search summary of the fiche says ~59,000 disabled students at the 2022 start of year, 2% of students.',
    match='UNVERIFIED (approximately consistent with the search summary: 59,000, 2%)', figs={},
    extra='User action: download the fiche in a browser (or allow drees.solidarites-sante.gouv.fr in the session network settings). An earlier copy exists at .../2025-01/Fiche 2.4 ... .pdf (same host).')
add('DIS-07', title='Lutter contre les violences et les discriminations fondées sur l\'orientation sexuelle, l\'identité de genre et la sexuation dans l\'ESR (guide MESR, 2026)',
    cite='MESR, guide, July 2026. References followed: MILDECA-UGA (Bègue-Shankland L. et al.), "Violences sexuelles dans l\'enseignement supérieur en France : un focus sur l\'alcool et le cannabis", Oct 2024; Caélif, Baromètre 2020 des LGBTIphobies dans l\'ESR.',
    url='https://www.etudiant.gouv.fr/sites/default/files/2026-07/lutter-contre-les-violences-et-les-discriminations-fond-es-sur-l-orientation-sexuelle-l-identit-de-genre-et-la-sexuation-dans-l-enseignement-sup-rieur-et-la-recherche-8353.pdf',
    access='downloaded', key='33% of trans/non-binary students faced sexual violence',
    found='"33 % des personnes s\'identifiant comme trans/non binaires/queer ont subi au moins une violence sexuelle depuis leur arrivée dans l\'enseignement supérieur, contre 9 % des hommes et 24 % des femmes" (guide PDF p11), citing MILDECA 2024 (report p4 and p13, Figure 3).',
    match='MATCH (confirmed in the primary MILDECA report)',
    figs={'DIS-07_fig1.png': 'references/MILDECA-UGA_2024_VSS_alcool_cannabis.pdf p13: Figure 3, sexual victimisation by gender identity',
          'DIS-07_fig2.png': 'source.pdf p11: key paragraph (text crop)', 'DIS-07_redraw.png': 'data/DIS-07.csv'},
    extra='MILDECA report from drogues.gouv.fr; Caélif 2020 barometer from the Université Paris Nanterre equality mission (references/). The guide has no chart of its own.')
add('DIS-08', title='Intersecting systems of disadvantage: LGBTQ STEM professionals', cite='Cech EA, Waidzunas TJ (2021). Science Advances 7(3):eabe0933. doi:10.1126/sciadv.abe0933 (PMC7810386).',
    url='https://pmc-oa-opendata.s3.amazonaws.com/PMC7810386 (first pass)', access='downloaded', key='22% vs 15% considered leaving',
    found='"22% of LGBTQ professionals, versus 15% of their non-LGBTQ peers, had thought about leaving their STEM job at least once in the last month, and 12% ... (versus 8%) planned to leave their STEM profession within the next 5 years" (PDF p4).',
    match='MATCH', figs={'DIS-08_fig1.png': 'PDF p6: Fig. 6, intentions to leave STEM by LGBTQ status (predicted means)', 'DIS-08_redraw.png': 'data/DIS-08.csv'},
    extra='abe0933-F*.jpg are the PMC figure images (low resolution, from the first pass); the crop from the PDF is preferred.')
add('DIS-09', title='Exploring the workplace for LGBT+ physical scientists', cite='Institute of Physics, Royal Astronomical Society, Royal Society of Chemistry (2019).',
    url='https://www.ras.ac.uk/sites/default/files/2019-06/LGBT%20Report_Web.pdf (RAS copy; the RSC URL returns 404)', access='downloaded', key='~1 in 3 considered leaving',
    found='"28% of LGBT+ respondents stated that they had at some point considered leaving their workplace because of the climate or discrimination towards LGBT+ people"; trans respondents: nearly half, 20% often (PDF p5). 16% of all respondents experienced exclusionary behaviour in the last 12 months (p14).',
    match='MISMATCH (minor): the report says 28%, i.e. a bit more than 1 in 4; "~1 in 3" (and press "almost a third") overstates it. Use 28%.',
    figs={'DIS-09_fig1.png': 'PDF p5: key-findings graphic (28% / 20%)', 'DIS-09_fig2.png': 'PDF p14: Figure 5, exclusionary behaviour by sexual orientation', 'DIS-09_redraw.png': 'data/DIS-09.csv (Figure 5)'},
    extra='page.html = Nature Index news page from the first pass.')
add('DIS-10', title='A decade of decline: Grant funding for researchers with disabilities 2008 to 2018', cite='Swenor BK, Munoz B, Meeks LM (2020). PLOS ONE 15(3):e0228686. doi:10.1371/journal.pone.0228686 (PMC7053734).',
    url='https://pmc-oa-opendata.s3.amazonaws.com/ (PMC7053734.1: PDF, XML, figures)', access='downloaded', key='NIH applicants with disability 1.9% -> 1.2%',
    found='"The percentage of NIH grant applicants with PIs reporting a disability significantly declined from 1.9% in 2008, to 1.2% in 2018" (PDF p1); Table 1 p4.',
    match='MATCH', figs={'DIS-10_fig1.jpg': 'PMC image of Fig 1 (PDF p5): % of applications and awards with PIs reporting disability',
                         'DIS-10_fig2.jpg': 'PMC image of Fig 3 (PDF p7): success rate by disability status', 'DIS-10_redraw.png': 'data/DIS-10.csv (Tables 1-2 from article.xml)'},
    extra='page.html is the IDEAS/RePEc landing page from the first pass (it contains captcha script code but also the full abstract; not a challenge page).')
add('DIS-11', title='Diversity and STEM: Women, Minorities, and Persons with Disabilities 2023 (NSF 23-315)', cite='NCSES, National Science Foundation, January 2023.',
    url='https://ncses.nsf.gov/pubs/nsf23315/assets/nsf23315-report.pdf', access='downloaded', key='Disabled: 11% of S&E PhDs, 3% of workforce',
    found='"Individuals with at least one disability earned 11% of S&E doctorate degrees" (PDF p56; Fig. 7-10: 10.8% S&E, 11.3% all fields, 2021); "9% of the population had one or more disabilities ..., 3% of those who work in STEM occupations did" (p5; Fig. 1-1 p6).',
    match='MATCH, with a caveat: the 3% (CPS, all STEM workers incl. the skilled technical workforce) and the 11% (SED doctorates) come from different surveys and definitions; among college-educated workers in S&E occupations (NSCG) the disability share is also 11% (p37). Do not present 11% vs 3% as a PhD-to-workforce leak.',
    figs={'DIS-11_fig1.png': 'PDF p6: Figure 1-1, population vs STEM workforce by sex, race, disability (2021)', 'DIS-11_fig2.png': 'PDF p56: Figure 7-10, doctorate recipients with disability by field (2021)',
          'DIS-11_redraw.png': 'data/DIS-11.csv'},
    extra='The XLSX data tables could not be fetched: the pubs/nsf23315 landing page and the data-tables PDF now return 404 (NCSES site reorganised); only the report PDF URL still works. Numbers were transcribed from the report figures instead.')
add('DIS-12', title='Equality in higher education: staff statistical report 2024', cite='Advance HE, 14 Nov 2024 (UK HE staff data 2022-23).',
    url='https://advance-he.ac.uk/news-and-views/equality-higher-education-staff-statistical-report-2024', access='failed', key='UK staff declaring disability 3.2% -> 7.2%',
    found='Not obtained: advance-he.ac.uk serves a Cloudflare "Just a moment" bot challenge (HTTP 403); not bypassed. The underlying HESA staff data (hesa.ac.uk) is behind the same kind of challenge.',
    match='UNVERIFIED', figs={}, extra='User action: download the report PDF and data tables in a browser from advance-he.ac.uk (free registration may be needed), or the HESA staff open data tables (disability by year).')

for i, k in M.items():
    folder = glob.glob(f'{D}/*/{i}')[0]
    files = sorted(os.path.relpath(p, ROOT) for p in glob.glob(folder + '/**/*', recursive=True) if os.path.isfile(p) and '/figures/' not in p and not p.endswith('notes.md'))
    figs = sorted(os.path.relpath(p, ROOT) for p in glob.glob(folder + '/figures/*') if os.path.isfile(p))
    note = [f'# {i}: {k["title"]}', '', f'- **Citation:** {k["cite"]}', f'- **url_used:** {k["url"]}', f'- **Access status:** {k["access"]}',
            f'- **Key number (list):** {k["key"]}', f'- **Headline number found:** {k["found"]}', f'- **Check:** {k["match"]}', '', '## Files']
    note += [f'- {os.path.relpath(os.path.join(ROOT, f), folder)}' for f in files] or ['- (none)']
    note += ['', '## Figures', '| File | From (PDF page) |', '|---|---|']
    note += [f'| figures/{f} | {d} |' for f, d in k['figs'].items()] or ['| (none) | |']
    if k['extra']: note += ['', '## Notes', k['extra']]
    note += ['', 'Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).', '']
    open(f'{folder}/notes.md', 'w').write('\n'.join(note))
    one = k['match'] if len(k['match']) <= 240 else k['match'][:237] + '...'
    st = dict(id=i, title=k['title'], url_used=k['url'], file_paths=files + [os.path.relpath(f'{folder}/notes.md', ROOT)], access_status=k['access'],
              figures_extracted=figs, notes=f'Key "{k["key"]}": {one}'.replace('\n', ' '))
    os.makedirs(f'{D}/_status', exist_ok=True)
    json.dump(st, open(f'{D}/_status/{i}.json', 'w'), indent=1, ensure_ascii=False)
    print(i, k['access'], len(files), 'files', len(figs), 'figs')
