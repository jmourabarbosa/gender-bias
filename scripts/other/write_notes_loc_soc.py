"""Write notes.md + _status/<ID>.json for LOC-01..13 and SOC-01..09 (other-biases collection)."""
import json, glob, os
ROOT = '/home/user/gender-bias'
OB = f'{ROOT}/other-biases-data'
M = '**MATCH**'
S = {}

def add(i, **k): S[i] = k

add('LOC-01', title="MESR-DGRH Note n°2-2026: Trajectoire professionnelle des enseignants-chercheurs recrutés en 2024",
    cite="Pépin C. (2026), Note de la DGRH - Enseignement supérieur n°2-2026, MESR/DGRH A1-1.",
    url="https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B02%20-%202026%20-%20Trajectoire%20professionnelle%20des%20enseignants-chercheurs%20recrut%C3%A9s%20en%202024.pdf",
    access='downloaded',
    head="23% of MCF recruited in 2024 are endo-recruited (PhD defended at the recruiting institution); 54% of PR were already MCF in the recruiting institution (p.1 summary, p.2 text, fig. 4 p.3). Foreign nationals: 23.5% of new MCF, 7.9% of new PR (fig. 6 p.4). Mean age at hiring 35 (MCF) / 47 (PR) (fig. 5 p.3).",
    check=f"{M} (23% / 54%).",
    figs={'LOC-01_fig1.png': 'Figure 4, PDF p.3: néo-/endo-recrutement/mutation by discipline group (MCF, PR), 2024',
          'LOC-01_fig2.png': 'Figure 6, PDF p.4: foreign share among recruits 2020-2024 (MCF, PR, PR not previously MCF)',
          'LOC-01_fig3.png': 'Figure 5, PDF p.3: mean age at hiring by discipline group',
          'LOC-01_redraw.png': 'B/W redraw of fig. 4 (data/LOC-01.csv)'},
    data="data/LOC-01.csv (local-hiring table by discipline group, read from the labelled bars of fig. 4); data/LOC-01_age_foreign.csv (fig. 5 ages; fig. 6 endpoints 2020/2024 - intermediate years are not labelled). The series across years is in ../LOC-03/data/local_hiring_series.csv.",
    extra="Definition (p.4): endo-recruitment rate = local recruits / all posts filled incl. transfers. From 2022 all routes (incl. art. 46-3 and agrégation) are included. The note links Excel tables ('Tableaux Excel détaillés') but the MESR landing pages are behind a Cloudflare challenge, so they were not fetched.",
    notes="2024 recruits: MCF endo 23%, PR endo 54% MATCH (p.1-3); foreign 23.5%/7.9% (fig.6 p.4); fig.4/5/6 cropped; data/LOC-01.csv")

add('LOC-02', title="MESR-DGRH Note n°3-2025: Trajectoire professionnelle des enseignants-chercheurs recrutés en 2023",
    cite="MESR-DGRH (2025), Note de la DGRH - Enseignement supérieur n°3-2025.",
    url="https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-10/note-dgrh-n-3---2025---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2023-pdf-38087.pdf",
    access='downloaded',
    head="19% of MCF and 54% of PR recruited in 2023 were endo-recruited (p.1 summary; p.2 text; fig. 4 p.3). Foreign: 18.5% of MCF, 11% of PR (p.4). 1,836 recruits.",
    check=f"{M} (19% / 54%).",
    figs={'LOC-02_fig1.png': 'Figure 4, PDF p.3: néo-/endo-recrutement/mutation by discipline group, 2023',
          'LOC-02_fig2.png': 'Figure 5, PDF p.3: mean age at hiring by discipline group, 2023',
          'LOC-02_redraw.png': 'B/W redraw of fig. 4 (data/LOC-02.csv)'},
    data="data/LOC-02.csv (fig. 4 bar labels). Series: ../LOC-03/data/local_hiring_series.csv.",
    extra="PR endo by discipline: Sciences-Tech 67%, Lettres-SH 45%, Droit-Éco-Gestion 26% (p.2).",
    notes="2023 recruits: MCF endo 19%, PR 54% MATCH (p.1-3); foreign 18.5%/11% (p.4); fig.4/5 cropped; data/LOC-02.csv")

add('LOC-03', title="MESR-DGRH trajectory notes, recruits 2018-2022 (series)",
    cite="MESR-DGRH, Notes de la DGRH: n°8 juillet 2019 (recrutés 2018); n°7 septembre 2020 (2019); n°8 septembre 2021 (2020); n°8 septembre 2022 (2021); n°7 septembre 2023 (2022).",
    url="https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2022-12/note-dgrh-n8-septembre-2022--trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2021-25546.pdf (+ 4 other editions, URLs below)",
    access='downloaded',
    head="Series of endo-recruitment rates, recruits 2018-2024: MCF 18, 17, 20, 18, 19, 19, 23%; PR 45, 41, 47, 46, 57, 54, 54%. Foreign MCF 14, 16, 18, 20, 23, 18.5, 23.5%; foreign PR 12, 11, 12, 11, 10, 11, 7.9%. See data/local_hiring_series.csv for page refs.",
    check="'Series' - no single key number; series assembled for 2018-2024 (7 editions incl. LOC-01 and LOC-02).",
    figs={'LOC-03_fig1.png': '2018 note, Figure 3, PDF p.3 (néo/endo/mutation by discipline, 2018)',
          'LOC-03_fig2.png': '2019 note, Figure 4, PDF p.3 (endo-recruitment by discipline 2008-2019, trend)',
          'LOC-03_fig3.png': '2020 note, Figure 4, PDF p.3 (by discipline, 2020)',
          'LOC-03_fig4.png': '2021 note (source.pdf), Figure 4, PDF p.3 (by discipline, 2021)',
          'LOC-03_fig5.png': '2021 note (source.pdf), Figure 5, PDF p.3 (endo-recruitment by discipline 2015-2021)',
          'LOC-03_fig6.png': '2022 note, Figure 4, PDF p.3 (by discipline, 2022)',
          'LOC-03_redraw.png': 'B/W redraw of the 2018-2024 series (data/local_hiring_series.csv)'},
    data="data/local_hiring_series.csv (year, n recruited, MCF and PR endo %, PR scope, MCF/PR foreign %, source note, file, pages; 2023 and 2024 from LOC-02/LOC-01); data/local_hiring_by_discipline.csv (néo/endo/mutation % by corps x discipline group, 2018-2024, read from the labelled bars).",
    extra=("Files: source.pdf = 2021 recruits (n°8 sept 2022); series/dgrh_trajectoire_recrutes_2018.pdf (https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2022-01/note-dgrh-n-8-juillet-2019---campagne-2018-16084.pdf), "
           "_2019.pdf (.../2022-01/note-dgrh-n-7-septembre-2020---campagne-2019-16078.pdf), _2020.pdf (.../2022-01/note-dgrh-n-8-septembre-2021---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2020-16072.pdf), "
           "_2022.pdf (.../2023-11/note-dgrh-n-7-septembre-2023---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2022-pdf-30093.pdf). Despite the 'campagne' file names, the 2018/2019 PDFs are the trajectory notes (titles checked p.1).\n\n"
           "**Comparability caveats.** (1) The PR rate includes agrégés du supérieur in 2018-2019 and 2022-2024 but EXCLUDES them in 2020-2021 (notes say 'calculé hors agrégés'), so the 2021->2022 jump (46->57%) is partly a scope change. (2) From 2022 the notes include art. 46-3 recruitments. "
           "(3) 2019: summary p.1 and fig. 3 say MCF 17%, body text p.2 says 18% (internal inconsistency; CSV uses 17). (4) Foreign shares were revised later: LOC-01 fig. 6 gives MCF 17.5% / PR 10.0% for 2020 vs 18% / 12% in the 2020 note (PR excl. agrégés); the CSV keeps the value published in each year's note. "
           "MESR HTML landing pages return a Cloudflare challenge (not bypassed); the PDFs download directly with a browser UA."),
    notes="Series 2018-2024 assembled (5 notes here + LOC-01/02): data/local_hiring_series.csv + by_discipline.csv; PR scope excl. agrégés in 2020-21 (break); 2019 MCF 17% (p.1) vs 18% (p.2) inconsistency")

add('LOC-04', title="MESR-DGRH Note n°1-2026: Campagne de recrutement et d'affectation des MCF et PR, session 2024",
    cite="MESR-DGRH (2026), Note de la DGRH - Enseignement supérieur n°1-2026.",
    url="https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B01%20-%202026%20-%20Campagne%202024.pdf",
    access='downloaded',
    head="233 posts filled by transfer (mutation) in 2024 = 10% of posts filled (12% in 2023); MCF 150/1,487 = 10%, PR 83/764 = 11% (p.3-4; table fig. 6 p.3). 2,251 posts filled of 2,476 published (90.9%).",
    check=f"{M} (~10% by mutation).",
    figs={'LOC-04_fig1.png': 'Figure 6 (table), PDF p.3: posts published and filled by corps, article and route',
          'LOC-04_redraw.png': 'B/W redraw: share of posts filled by concours / mutation / détachement'},
    data="data/LOC-04.csv (full transcription of fig. 6 table).",
    extra="32% of the 233 mutations were 'prioritaires' (73 of 74 for rapprochement de conjoint) (p.4).",
    notes="Hiring routes table transcribed; mutation 233/2,251 = 10% MATCH (p.3); fig.6 cropped")

add('LOC-05', title="Godechot & Louvet (2008), Le localisme dans le monde académique : un essai d'évaluation",
    cite="Godechot O., Louvet A. (2008), La Vie des idées, 22 avril 2008.",
    url="https://laviedesidees.fr/IMG/pdf/20080422_localisme.pdf (PDF linked from https://laviedesidees.fr/Le-localisme-dans-le-monde.html)",
    access='downloaded',
    head="Local applications succeed 6.30% of the time vs 0.24% for external ones; Mantel-Haenszel odds ratio 18.02 (crude OR 27); locals = 55% of recruits vs 8% expected under independence (Tableau 5, PDF p.12; DOCTHESE, PhDs defended 1972-1996). Proxy: becoming a thesis supervisor in a department, not hiring itself.",
    check=f"{M} (18x; 6.3% vs 0.24%).",
    figs={'LOC-05_fig1.png': 'Tableau 5, PDF p.12: success rates local vs external, MH odds ratio',
          'LOC-05_fig2.png': 'Tableau 7, PDF p.15: localism by discipline (MH odds ratios 6.0 philosophy to 51.2 engineering)',
          'LOC-05_redraw.png': 'B/W redraw of Tableau 7 odds ratios'},
    data="data/LOC-05.csv (Tableau 7, all 24 rows); data/LOC-05_table5_summary.csv (Tableau 5 key rows). Also Tableau 3 p.5: EHESS 1991-2005 local success 16% vs 6% external.",
    extra="page.html = the La Vie des idées article page (valid).",
    notes="PDF from laviedesidees; 6.30% vs 0.24%, MH OR 18.02 MATCH (Tableau 5 p.12); Tableau 7 by discipline transcribed")

add('LOC-06', title="Godechot, Issiakou, Renisio & Rougier (2025), Le localisme universitaire, nouvelles évaluations",
    cite="Godechot O., Issiakou R., Renisio Y., Rougier A. (2025), La Vie des idées / Books & Ideas, 18 novembre 2025 (French text).",
    url="https://booksandideas.net/IMG/pdf/20251118_godechot-2.pdf (byte-identical to https://laviedesidees.fr/IMG/pdf/20251118_godechot-2.pdf)",
    access='downloaded',
    head="On ~7,900 MCF hirings 2017-2024, local candidates have 9.5 (wide scope) to 10.7 (narrow scope) times the odds of external ones (Mantel-Haenszel; Tableau 2, PDF p.12). By CNU section the OR ranges from 0.5 (mathematics) to 29 (physiology) (p.13, fig. 1 p.15). MESR local-recruitment rate fell from 32% (2002) to 27% (2008) and 21% (2010), ~20-22% since 2018 (fig. 3 p.19, text p.20).",
    check=f"{M} (9.5-10.7; physiology OR ~29).",
    figs={'LOC-06_fig1.png': 'Figure 1, PDF p.15: MH odds ratio by CNU section (log scale)',
          'LOC-06_fig2.png': 'Figure 3, PDF p.19: MCF local-recruitment rate 2002-2022 (MESR data)',
          'LOC-06_fig3.png': 'Figure 4, PDF p.21: odds ratios 1970-80 (2008 article) vs 2017-24 by discipline',
          'LOC-06_redraw.png': 'B/W redraw of fig. 1 with 95% CIs'},
    data=("data/LOC-06.csv: per CNU section N recruits, N local recruits, expected locals (printed in the figure labels) + odds ratio and 95% CI **read from the vector drawing** of fig. 1 (log axis calibrated on tick labels, max residual 0.08 pt); checks: physiology 29.0, biochemistry 22.5, maths 0.5 match the text (p.13). "
          "CI lower bounds equal to 0.5/1.0 (maths, anthropology, constituants élémentaires) may be clipped at the axis. The ORs are not printed as numbers in the source, so treat as approximate. data/LOC-06_fig3_local_rate.csv: local-recruitment rate 2002-2022 digitized from fig. 3 (no 2013 point in the figure)."),
    extra="French original page saved as page_laviedesidees.html. It links a replication archive http://olivier.godechot.free.fr/hopfichiers/localisme_2025.zip - NOT fetched: plain-HTTP host does not resolve through the sandbox proxy and HTTPS is refused. The user can download it manually.",
    notes="Tableau 2 p.12 MH OR 9.5/10.7 MATCH; physiology 29 MATCH (p.13); odds ratios by CNU section digitized from vector fig.1 (approx.) -> data/LOC-06.csv; replication zip not reachable")

add('LOC-07', title="Combes, Linnemer & Visser (2008), Publish or peer-rich? The role of skills and networks in hiring economics professors",
    cite="Combes P.-P., Linnemer L., Visser M. (2008), Labour Economics 15(3): 423-441. DOI 10.1016/j.labeco.2007.04.003. WP: INRA-LEA Research Unit WP 0604 (2006).",
    url="https://ideas.repec.org/p/lea/leawpi/0604.html",
    access='paywalled',
    head="Not verifiable without the full text. Abstract (RePEc page): links to the jury significantly raise the probability of passing the agrégation in economics (1984-2003); a substantial improvement of the publication record is needed to compensate for not being linked to the jury.",
    check="Key number 'Jury link raises the pass rate' consistent with the abstract; effect-size table NOT extracted.",
    figs={}, data="none",
    extra="Tried: Unpaywall/OpenAlex (closed); WP PDF http://www.inra.fr/Internet/Departements/ESR/UR/lea/documents/wp/wp0604.pdf (host no longer resolves; https returns INRAE homepage); Wayback Machine (connection reset by proxy); HAL hal-00558189 (metadata only, link to ISTEX full text that needs institutional login). page.html = RePEc abstract page. **User action:** get the Labour Economics article via institutional access.",
    notes="Paywalled: WP link dead, HAL record has no file (ISTEX needs login); abstract page only; effect-size table needs institutional access")

add('LOC-08', title="Horta, Veloso & Grediaga (2010), Navel gazing: academic inbreeding and scientific productivity",
    cite="Horta H., Veloso F.M., Grediaga R. (2010), Management Science 56(3): 414-429. DOI 10.1287/mnsc.1090.1109.",
    url="https://ndownloader.figshare.com/files/10942667 (CMU KiltHub/figshare record 6073232, submitted version, CC BY)",
    access='downloaded',
    head="Inbred faculty publish 15% fewer peer-reviewed articles than non-inbred (marginal effect -0.41 on a mean of 2.82, p<0.05) but have 46% more consulting contracts (Table 3, PDF p.17); ~40% less likely to exchange information with external colleagues (Table 4 p.16). Data: Mexico (incl. UNAM), 1999-2002.",
    check=f"{M} (inbred faculty publish less: -15%).",
    figs={'LOC-08_fig1.png': 'Table 3, PDF p.17: effect of inbreeding on academic output',
          'LOC-08_fig2.png': 'Figure 1, PDF p.18: predicted publications by field, inbred vs non-inbred',
          'LOC-08_redraw.png': 'B/W redraw of Table 3 (effect as % of sample mean)'},
    data="data/LOC-08.csv (Table 3).",
    extra="This is the pre-publication (submitted) version from the CMU repository; page numbers refer to it, not to the journal. Full regressions in appendix Table A3 (p.31).",
    notes="OA submitted version via figshare/CMU; -15% publications MATCH (Table 3 p.17); Mexican data")

add('LOC-09', title="Horta (2022), Academic inbreeding: the state of the art",
    cite="Horta H. (2022), in Blair, Evans, Hughes & Tight (eds), International Perspectives on Leadership in Higher Education, Emerald, pp. 23-39. DOI 10.1108/S1479-362820220000015002.",
    url="https://doi.org/10.1108/S1479-362820220000015002 (metadata via api.crossref.org)",
    access='abstract_only',
    head="Review chapter; abstract only: inbreeding is prevalent worldwide, effects mostly detrimental for creative/engaged universities; leaders struggle to curb it because of entrenched traditions and power structures.",
    check="Key number 'Review' - nothing to check.",
    figs={}, data="none",
    extra="Unpaywall/OpenAlex: closed. Emerald page returns a Cloudflare challenge (not saved). crossref.json holds the metadata and abstract. **User action:** institutional access if the chapter text is needed.",
    notes="Closed; Emerald behind Cloudflare challenge; Crossref abstract saved (crossref.json)")

add('LOC-10', title="Yudkevich, Altbach & Rumbley (eds) (2015), Academic Inbreeding and Mobility in Higher Education: Global Perspectives",
    cite="Palgrave Macmillan, 2015. DOI 10.1057/9781137461254. ISBN 978-1-137-46124-7.",
    url="https://doi.org/10.1057/9781137461254 (metadata via api.crossref.org)",
    access='paywalled',
    head="Book (country cases: Argentina, China, Japan, Russia, Slovenia, South Africa, Spain, Ukraine + literature review). No numbers available without the book.",
    check="Key number 'Country cases' - consistent with TOC; country comparison table NOT extracted.",
    figs={}, data="toc.csv (chapter DOIs, authors, pages from Crossref); crossref_book.json",
    extra="palgrave.com and link.springer.com return a 'Client Challenge' page (the earlier page.html was such a challenge page and was deleted). **User action:** library copy; ch. 1 (Altbach, Yudkevich, Rumbley, pp.1-16) likely holds the cross-country comparison.",
    notes="Paywalled book; publisher pages are bot challenges (deleted); Crossref metadata + TOC saved; needs library access")

add('LOC-11', title="Spain: El Salto (2023) 'El enclaustramiento de la universidad pública española' + ministry EPU tables",
    cite="Minguito Á., Borra A. (2023), El Salto, 29 Jan 2023. Primary: Ministerio de Ciencia, Innovación y Universidades, SIIU - Estadística de Personal de las Universidades (EPU), table PDITESIS.",
    url="https://www.elsaltodiario.com/educacion/enclaustramiento-universidad-publica-espanola ; https://estadisticas.ciencia.gob.es/jaxiPx/files/_px/es/px/Universitaria/RRHH/PDITESIS/l0/px_rrhh_pditesis_tipo_centro_tot.px (+3 other PDITESIS tables)",
    access='downloaded',
    head="El Salto: 72.94% of public-university teaching staff teach at the university where they read their thesis; 87.04% in the same region (2020-21). Ministry PDITESIS table: public universities 72.94% / 87.04% in 2020-21 (exact match); latest 2024-25: 72.77% / 86.58%; all universities 66.01% (2024-25).",
    check=f"{M} (72.9%).",
    figs={'LOC-11_redraw.png': 'B/W redraw of the ministry series 2015-16 to 2024-25 (public universities)'},
    data="data/*.px (PC-Axis originals) and their CSV conversions: national by type of university/centre, by staff type, by region (CCAA), by university; data/LOC-11.csv = public-university series. Indicator computed for presential universities (note in the PX file).",
    extra="Spain vs France: Spain's figure is a STOCK (all current staff); the French MESR rates (LOC-01..03) are FLOWS (new hires in a year: ~19-23% of MCF). Not directly comparable; a French stock measure is not published.",
    notes="El Salto 72.94% MATCH, confirmed in ministry SIIU PDITESIS table (2020-21); 2024-25 = 72.77%; px+csv saved")

add('LOC-12', title="El País press article citing Sanz-Menéndez & Cruz-Castro (CSIC 2006): 'La endogamia enferma el campus'",
    cite="García de Blas E., Mora A.J., El País (c. 2013-2014), PDF hosted by UCM; cites Sanz-Menéndez L., Cruz-Castro L. (2006), CSIC-IPP study.",
    url="https://www.ucm.es/data/cont/media/www/pag-50946/ENDOGAMIA%20PAIS.pdf",
    access='downloaded',
    head="'En el 96% de los casos el profesor que ganó una plaza ya trabajaba en la universidad donde se colocó de forma indefinida' (study of 2006 by L. Sanz-Menéndez and L. Cruz-Castro, CSIC) (PDF p.1). Also: new CSIC study of 1,300 professors tenured 1997-2001: productivity of inbred staff declines in the medium term (p.1).",
    check=f"{M} (96%), but only via press.",
    figs={}, data="none",
    extra="Primary 2006 CSIC working paper not found online (searches; CORE copy behind a JS challenge). Related peer-reviewed paper: Cruz-Castro & Sanz-Menéndez (2010), 'Mobility versus job stability: assessing tenure and productivity outcomes', Research Policy 39(1): 27-38 (not downloaded).",
    notes="Press PDF (UCM-hosted El País article) 96% MATCH p.1; primary CSIC 2006 WP not found")

add('LOC-13', title="Portugal: DGEEC report on academic inbreeding (endogamia académica), public universities 2021/2022",
    cite="DGEEC (2023), 'Endogamia académica nas instituições de ensino superior universitárias públicas 2021/2022' (primary, not retrieved); secondary: SEDES (2024), Policy Paper 5/2024 'Endogamia académica no ensino superior', Observatório da Educação, Ciência e Ensino Superior.",
    url="https://sedes.pt/wp-content/uploads/2024/01/Policy-Paper-5-2024.pdf (primary https://www.dges.gov.pt/sites/default/files/endogamiaacademica_20212022.pdf now redirects to a landing page)",
    access='downloaded',
    head="2021/22, career PhD faculty in Portuguese public universities: ~68% obtained their PhD at the institution where they work, 19% abroad, 14% at another Portuguese institution (SEDES p.3-4, citing DGEEC). Extremes: Law faculties Coimbra 100%, Lisboa 99%; Nova SBE 4% (p.4).",
    check="Key number 'Not verified' -> now 68% (secondary source). Per-institution table NOT obtained (primary report unreachable).",
    figs={'LOC-13_redraw.png': 'B/W bar: Spain (LOC-11) vs Portugal stock inbreeding rates'},
    data="data/LOC-13.csv (national shares + faculty examples from SEDES).",
    extra="dges.gov.pt redirects to landing.dges.gov.pt (saved as dges_redirect_page.html for the record); iesuperior.pt path returns 404; dgeec.medu.pt is a JavaScript app (no static file list). **User action:** obtain the DGEEC 2021/22 PDF (maybe via DGEEC/IES contact) for the per-institution table.",
    notes="Primary DGEEC PDF unreachable (redirect/404); secondary SEDES 2024 policy paper saved: 68% PhD from own institution (p.3)")

add('SOC-01', title="Observatoire des inégalités: Les milieux populaires largement sous-représentés dans l'enseignement supérieur",
    cite="Observatoire des inégalités, first written 6 Sept 2011, updated (datePublished 2021-09-24, modified 2023-01-17); source MEN/MESRI data 2019-2020.",
    url="https://www.inegalites.fr/Les-milieux-populaires-largement-sous-representes-dans-l-enseignement-superieur",
    access='downloaded',
    head="Workers' (ouvriers) children: 12.3% of university students in licence, 8.5% in master, 5.9% in doctorate; senior managers' children 29.3% -> 40.2% -> 40.3% (table 'Origine sociale des étudiants à l'université par cursus'). All students: ouvriers 11.5%, cadres 34.4%.",
    check=f"{M} (12.3% -> 5.9%).",
    figs={'SOC-01_redraw.png': 'B/W redraw: cadres vs ouvriers children by LMD level (data/SOC-01.csv)'},
    data="data/SOC-01.csv (by LMD level); data/SOC-01_table1_filieres.csv (by track: business schools, engineering, CPGE, university, IUT, BTS). Parsed from the HTML tables of page.html (no PDF page numbers: web page).",
    extra="Newer official numbers (2024-25): RERS 2025 fiche 7.16 -> ouvriers 10.1% licence, 6.3% master, 3.9% doctorate (see SOC-03).",
    notes="Web tables transcribed; 12.3% licence -> 5.9% doctorate MATCH; data 2019-20")

add('SOC-02', title="Martin-Kleinbauer & Maurin (2025), Enseignement supérieur : comment évolue la composition sociale des filières ?",
    cite="Martin-Kleinbauer J., Maurin L. (2025), Observatoire des inégalités, 27 Feb 2025; source MEN data 2023-2024.",
    url="https://www.inegalites.fr/Enseignement-superieur-comment-evolue-la-composition-sociale-des-filieres",
    access='downloaded',
    head="ENS: children of cadres 64.9%, of ouvriers 2.0% in '2024' (= 2023-24 data); 61.4% / 2.8% in 2009. CPGE cadres 50.9% -> 53.7%; university ouvriers 11.4% -> 8.7%.",
    check=f"{M} (65% / 2%).",
    figs={'SOC-02_redraw.png': 'B/W redraw: cadres and ouvriers shares by track, 2009 vs 2024'},
    data="data/SOC-02.csv (all rows: university, BTS, CPGE, ENS x 6 social groups x 2009/2014/2019/2024 + change). Note: the 2014 column for CPGE and ENS is printed in whole numbers in the source.",
    extra="Web page (no PDF page numbers).",
    notes="Web table transcribed; ENS cadres 64.9%, ouvriers 2.0% MATCH")

add('SOC-03', title="RERS 2025 (DEPP-SIES), fiche 7.16 'L'origine sociale des étudiants français'",
    cite="MENESR DEPP & SIES (2025), Repères et références statistiques 2025, chapitre 7, fiche 7.16, pp. 256-257.",
    url="https://rers.depp.education.fr/data/2025/RERS.pdf (full volume, 470 pp.; fiche extracted to source_rers2025_fiche7-16.pdf)",
    access='downloaded',
    head="2024-25, French students: 36.1% have cadre parents, 9.1% ouvrier parents; ENS 64.7% cadres / 1.9% ouvriers; university cursus licence -> doctorat: cadres 31.1% -> 41.6%, ouvriers 10.1% -> 3.9% (tables 1 and 3, fiche p.2 = RERS p.257).",
    check="Primary source for SOC-01/02: confirms the pattern (ENS cadres 64.7% vs SOC-02's 64.9%, ouvriers 1.9% vs 2.0%; small differences = different year/perimeter).",
    figs={'SOC-03_fig1.png': 'Table 1 (fiche p.2 = RERS PDF p.258): social origin by track, 2024-25',
          'SOC-03_fig2.png': 'Table 3 (fiche p.2 = RERS PDF p.258): university students by sex and LMD level',
          'SOC-03_redraw.png': 'B/W redraw: cadres/employés/ouvriers by LMD level'},
    data="data/SOC-03.csv (table 3, LMD x sex); data/SOC-03_table1_filieres.csv (table 1); data/SOC-03_table2_disciplines.csv (table 2, by discipline, with headcounts). Transcribed from the PDF text layer.",
    extra="The education.gouv.fr RERS landing pages are behind Cloudflare (403) and education.gouv.fr does not resolve from this sandbox; the full volume came from rers.depp.education.fr. The XLSX per fiche could not be located (the RERS web app serves an SPA shell for guessed paths), so tables were transcribed from the PDF. The full 30 MB volume was not kept (only the 2-page fiche).",
    notes="RERS 2025 fiche 7.16 extracted from rers.depp.education.fr full PDF; 3 tables transcribed; XLS not found (site SPA/Cloudflare)")

add('SOC-04', title="Céreq Bref n°452 (2024): origine sociale, parcours scolaires et insertion (Génération 2017)",
    cite="Dabet G., Épiphane D., Personnaz E. (2024), Céreq Bref n°452.",
    url="https://www.cereq.fr/sites/default/files/2024-11/C%C3%A9req%20Bref%20452.pdf",
    access='downloaded',
    head="'en 2023, les étudiant·es en 3e cycle universitaire comptent 41 % d'enfants de cadres et 8 % d'enfants d'ouvrier·es' (PDF p.1, citing ref. [3], MESR data, not Génération 2017); CPGE 54% / 7%; ENS 63% / 2%. Génération 2017: 55% of children of two cadres hold a bac+5 or more vs 11% of children of working-class households (fig. 2 p.2).",
    check=f"{M} (41% vs 8%), but the figure is quoted from MESR data, not from the Céreq survey itself.",
    figs={'SOC-04_fig1.png': 'Figure 2, PDF p.2: no diploma / short / long higher education by social origin',
          'SOC-04_redraw.png': 'B/W redraw of figure 2'},
    data="data/SOC-04.csv (figure 2 labels).",
    extra="",
    notes="41% cadres vs 8% ouvriers in doctorate MATCH (p.1, quoting MESR 2023); fig.2 transcribed")

add('SOC-05', title="Bonneau, Charousset, Grenet & Thebault (2021), Quelle démocratisation des grandes écoles depuis le milieu des années 2000 ? (IPP report n°30)",
    cite="Bonneau C., Charousset P., Grenet J., Thebault G. (2021), Rapport IPP n°30, janvier 2021. HAL halshs-03119054.",
    url="https://www.ipp.eu/wp-content/uploads/2025/06/30_democratisation-grandes-ecoles-depuis-milieu-annees-2000-ipp-janvier-2021.pdf (full report, 308 pp.); slides https://www.ipp.eu/wp-content/uploads/2021/01/democratisation-grandes-ecoles-ipp-slides-debats-egalite-mars-2021.pdf",
    access='downloaded',
    head="2016-17: students from very advantaged backgrounds = 64% of grandes écoles students vs 23% of the 20-24 age group and 47% of all bac+3-5 students (PDF p.11 and fig. 4.1 p.93; ENS 72%). Trend: 64% (2006) -> 65% (2016) in grandes écoles (constant 2006 scope), top 10% most selective 77% -> 78% (fig. 7.17 p.215).",
    check=f"{M} (64% vs 23%).",
    figs={'SOC-05_fig1.png': 'Figure 4.1, PDF p.93: social composition by type of grande école vs age group, 2016-17',
          'SOC-05_fig2.png': 'Figure 7.17, PDF p.215: social composition 2006-2016 (grandes écoles, university, by type, top 10%)',
          'SOC-05_redraw.png': 'B/W redraw of fig. 4.1 (age group, bac+3-5, grandes écoles, ENS)',
          'SOC-05_redraw_trend.png': 'B/W redraw of the 2006-2016 trend (fig. 7.17)'},
    data="data/SOC-05.csv (fig. 4.1, 4 social groups x 8 columns); data/SOC-05_fig7-17_trend.csv (fig. 7.17, 6 panels x 2006-2016). Values are the bar labels printed in the vector figures.",
    extra="The listed synthesis PDF (2021/01/synthese-ipp-rapport-30-...pdf) now 404s; vie-publique copy and HAL file are behind JS/Anubis bot challenges (not bypassed). The full report was found via the ipp.eu media API. slides.pdf = IPP presentation (March 2021).",
    notes="Full IPP report (synthesis URL 404); 64% vs 23% MATCH (p.11, fig.4.1 p.93); fig.4.1 + 7.17 trend transcribed")

add('SOC-06', title="Morgan et al. (2022), Socioeconomic roots of academic faculty",
    cite="Morgan A.C., LaBerge N., Larremore D.B., Galesic M., Brand J.E., Clauset A. (2022), Nature Human Behaviour 6: 1625-1633. DOI 10.1038/s41562-022-01425-4. PMC9755046.",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC9755046 (PMC OA bucket, first pass)",
    access='downloaded',
    head="22.2% of US faculty report at least one parent with a PhD (PDF p.2-3); share with a PhD parent is ~32% at the top-20% prestige institutions vs ~20% at the bottom 20% for faculty born in the 1980s (fig. 6a p.6).",
    check=f"{M} (22.2%).",
    figs={'SOC-06_fig1.png': 'Figure 6, PDF p.6: % faculty with a PhD parent by birth decade and prestige (a) and by prestige rank (b), 300 dpi crop',
          'SOC-06_fig2.png': 'Figures 1-2, PDF p.3 (same strip): ratio of parents\' education to benchmarks; college-educated parents by gender',
          'SOC-06_redraw.png': 'B/W redraw of fig. 6a'},
    data="data/SOC-06.csv: fig. 6a values read from the vector markers (approximate; axis calibrated on tick labels). Original PMC JPGs kept in figures/ (41562_2022_1425_Fig1-6_HTML.jpg). Supplementary PDFs in supplementary/.",
    extra="Data availability: survey microdata only under an IRB-approved data-sharing agreement (not public); code at https://github.com/allisonmorgan/faculty_ses.",
    notes="PMC OA PDF+figs; 22.2% PhD parent MATCH (p.2); fig.6 cropped from PDF, fig.6a digitized; data only via IRB agreement")

add('SOC-07', title="Stansbury & Schultz (2023), The economics profession's socioeconomic diversity problem (JEP) - working-paper version used",
    cite="Stansbury A., Schultz R. (2023), Journal of Economic Perspectives 37(4): 207-230, DOI 10.1257/jep.37.4.207. File used: Schultz R., Stansbury A. (2022), 'Socioeconomic Diversity of Economics PhDs', PIIE Working Paper 22-4.",
    url="https://www.piie.com/sites/default/files/documents/wp22-4.pdf",
    access='downloaded',
    head="All US PhD recipients 2010-18: 48% of economics PhDs had a parent with a graduate degree vs 43% across all fields (Table A1, PDF p.65). US-born only: 65% vs 50% (p.2); first-generation 14% vs 26%; top-15 programs 78% (p.4).",
    check=f"{M} (48% = all economics PhD recipients, Table A1 p.65). Note the paper's headline is 65% for US-born PhDs.",
    figs={'SOC-07_fig1.png': 'Figure 3, PDF p.12: parental education of US-born PhDs by field, 1970-2018 (share over time)',
          'SOC-07_fig2.png': 'Table A1, full page PDF p.65 (300 dpi)',
          'SOC-07_redraw.png': 'B/W redraw: share with a graduate-degree parent by field (Table A1)'},
    data="data/SOC-07.csv (Table A1, all 16 rows).",
    extra="The JEP PDF (aeaweb / pubs.aeaweb.org) returns a Cloudflare challenge (not bypassed); page.html is the AEA abstract page; page_piie.html is the PIIE WP page. The WP (2022) predates the JEP article; numbers may differ slightly in the JEP version. **User action (optional):** download the JEP PDF in a browser (free).",
    notes="JEP behind Cloudflare; PIIE WP 22-4 used; 48% (all econ PhDs, Table A1 p.65) MATCH, 65% for US-born (p.2); Table A1 transcribed")

add('SOC-08', title="Sutton Trust (2009), The Educational Backgrounds of Leading Scientists and Scholars (via Times Higher Education)",
    cite="Sutton Trust (2009), September 2009 report; THE news article 'Four in ten top scholars educated privately' (2009).",
    url="https://dera.ioe.ac.uk/id/eprint/30358/1/ScientistScholars-1.pdf (report); THE page saved as page.html",
    access='downloaded',
    head="42% of FRS/FBA Fellows with known UK schooling attended independent schools (Royal Society 38%, British Academy 47%) vs 7% of pupils (Table 1, PDF p.6; p.3). 56% studied at Oxbridge (p.2, Table 4 p.8). Only 2% from non-selective state schools.",
    check="Minor MISMATCH: key number says 40% (THE's rounding); the report says 42% (Table 1 p.6). 7% matches.",
    figs={'SOC-08_fig1.png': 'Table 1, PDF p.6: Fellows with known UK school backgrounds',
          'SOC-08_fig2.png': 'Table 3, PDF p.8: school backgrounds vs other professions',
          'SOC-08_redraw.png': 'B/W redraw of Table 3 with 7% reference line'},
    data="data/SOC-08.csv (Table 3 + 7% benchmark); data/SOC-08_table1.csv. Note: in Table 1 the independent counts (293+267=560) do not add to the printed combined total 557 (source inconsistency).",
    extra="",
    notes="Original Sutton Trust report from DERA; 42% privately educated (Table 1 p.6) - minor MISMATCH vs key's 40% (THE rounding); 7% MATCH")

add('SOC-09', title="Delhomme (2020), L'origine sociale des enseignant.e.s comparée à la population active occupée en 2015 (DEPP)",
    cite="Delhomme B. (2020), Éducation & formations n°101, DEPP, pp. 27-51. DOI 10.48464/ef-101-02. HAL hal-03097223.",
    url="https://api.archives-ouvertes.fr/search/?q=halId_s:hal-03097223 (metadata); file https://hal.science/hal-03097223/file/depp-2020EF101-article-02.pdf not retrievable",
    access='abstract_only',
    head="Abstract only: teachers' social origin (EDP sample, 4 generations, 2015) is clearly higher than that of the employed population, but more often from intermediate groups than all cadres; working-class access has risen since the 1990s.",
    check="Key number 'Not verified' - still not verified. HAL keywords are primary/secondary teaching only, which suggests higher-education staff are NOT covered (to confirm with full text).",
    figs={}, data="hal_metadata.json (HAL API record with abstract and keywords)",
    extra="HAL (hal.science / shs.hal.science) answers with an Anubis 'Making sure you're not a bot' challenge (the first-pass page.html was this challenge and was deleted); the DEPP original on education.gouv.fr does not resolve from this sandbox. **User action:** open the HAL PDF in a browser.",
    notes="HAL behind Anubis bot challenge (challenge page deleted); abstract via HAL API; likely excludes higher-ed staff (keywords)")

SEC = {'LOC': '01-localism', 'SOC': '02-social'}
os.makedirs(f'{OB}/_status', exist_ok=True)
for i, s in S.items():
    folder = f'{OB}/{SEC[i[:3]]}/{i}'
    figs = sorted(os.path.relpath(p, ROOT) for p in glob.glob(folder + '/figures/*') if os.path.isfile(p))
    figlines = '\n'.join(f'- `figures/{k}`: {v}' for k, v in s['figs'].items()) or '- none'
    others = sorted(os.path.basename(p) for p in glob.glob(folder + '/figures/*') if os.path.basename(p) not in s['figs'])
    if others: figlines += '\n- other files in figures/: ' + ', '.join(others)
    md = f"""# {i} - {s['title']}

- **Citation:** {s['cite']}
- **url_used:** {s['url']}
- **access_status:** {s['access']}

## Headline number
{s['head']}

**Key-number check:** {s['check']}

## Figures (PDF page of origin)
{figlines}

## Data
{s['data']}

## Notes
{s['extra'] or '-'}

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
"""
    open(f'{folder}/notes.md', 'w').write(md)
    files = sorted(os.path.relpath(p, ROOT) for p in glob.glob(folder + '/**/*', recursive=True) if os.path.isfile(p) and '/figures/' not in p)
    json.dump(dict(id=i, title=s['title'], url_used=s['url'], file_paths=files, access_status=s['access'], figures_extracted=figs, notes=s['notes']),
              open(f'{OB}/_status/{i}.json', 'w'), indent=1, ensure_ascii=False)
    print(i, s['access'], len(files), 'files', len(figs), 'figs')
