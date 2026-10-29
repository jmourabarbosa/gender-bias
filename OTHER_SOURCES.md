# Biases in French academia beyond gender: data sources

Source list for a data-driven talk on biases in academia other than gender, with French data first. Compiled 2026-10-29. It has 126 entries in 10 sections; 4 of them point to sources listed elsewhere so the extraction can be reused. Each entry gives a stable ID, a link, an access type, how to download it, and what to extract (the figure or table worth a slide).

Companion to `gender-bias-sources.md`. Use the same folder layout and manifest, under a separate root (`other-biases-data/`).

---

## Instructions for the collecting agent

1. **Folder layout.** Use one folder per section and one subfolder per source ID:
   ```
   other-biases-data/
     manifest.csv
     01-localism/LOC-01/{source.pdf|data.csv|page.html, figures/, notes.md}
     ...
   ```
2. **Manifest.** Keep `manifest.csv` with these columns: `id, title, url_used, file_paths, access_status (downloaded|abstract_only|paywalled|failed), figures_extracted, notes`. Write one row per ID, even when the download failed.
3. **Download order for papers with a DOI.**
   1. Try the open-access copy from Unpaywall: `https://api.unpaywall.org/v2/<DOI>?email=<your-email>`, field `best_oa_location.url_for_pdf`.
   2. Otherwise use the "OA copy" link listed for the entry (PMC, arXiv, bioRxiv, NBER, repository, author site).
   3. For a PMC article, use the PMC OA service: `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC<id>`. It returns a tar.gz with the PDF and figures.
   4. If the paper is still paywalled, save the abstract page as HTML and set `access_status=paywalled`. Do not use shadow libraries; the user can fetch it through institutional access.
4. **French official PDFs** (MESR, DGRH, Hcéres, Cour des comptes, Défenseur des droits) are direct downloads. The MESR site sometimes blocks automated clients. If it does, retry with a browser user-agent, or look for the same note on `data.enseignementsup-recherche.gouv.fr` or HAL.
5. **Figures.** For each "Extract" item, crop the named figure from the PDF at 300 dpi or more, saved as `figures/<ID>_fig<N>.png`. When a table holds the numbers, also transcribe it to CSV (`figures/<ID>_table<N>.csv`) so the plot can be redrawn in one consistent style.
6. **Time series.** Where an entry says "series", download every edition listed (for example the yearly DGRH notes) and merge the indicator into one CSV with a `year` column.
7. **Datasets.** Prefer API or bulk CSV exports over screenshots. Record the exact query and filters in `notes.md`.
8. **Verify.** Record one headline number per source in `notes.md` and check it against the "Key number" column. Flag any mismatch.
9. **Weak sources.** Some links point to a press page, a union document or a secondary summary, because the original was unreachable when this list was made. For those, also try to find the primary source. Union figures (SNESUP, SNCS) should be cross-checked against official MESR or CNRS data where possible.

Access codes used below:
- **OA**: open access.
- **PW**: paywalled; an OA copy may exist.
- **DATA**: downloadable dataset.
- **WEB**: web page; save as HTML or PDF.
- **PDF**: direct official PDF.

---

## 01 Localism and inbreeding

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| LOC-01 | MESR-DGRH Note n°2-2026, trajectories of EC recruited in 2024 | 23% of new MCF hired where they did their PhD; 54% of new PR hired where already MCF | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B02%20-%202026%20-%20Trajectoire%20professionnelle%20des%20enseignants-chercheurs%20recrut%C3%A9s%20en%202024.pdf | Direct PDF | Local-hiring table by discipline group (MCF and PR); foreign-share table; age at hiring |
| LOC-02 | MESR-DGRH Note n°3-2025, recruits of 2023 | 19% local MCF; 54% local PR | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-10/note-dgrh-n-3---2025---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2023-pdf-38087.pdf | Direct PDF | Same tables as LOC-01 (series) |
| LOC-03 | MESR-DGRH trajectory notes, earlier years (recruits 2018–2022) | Series | PDF | 2021 recruits: https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2022-12/note-dgrh-n8-septembre-2022--trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2021-25546.pdf | Download that PDF. Search enseignementsup-recherche.gouv.fr for "Trajectoire professionnelle des enseignants-chercheurs recrutés en" for each year back to 2018 | Merge local-hiring % into one CSV by year (series) |
| LOC-04 | MESR-DGRH Note n°1-2026, 2024 hiring campaign | ~10% of posts filled by transfer (mutation) | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B01%20-%202026%20-%20Campagne%202024.pdf | Direct PDF | Hiring routes table |
| LOC-05 | Godechot & Louvet 2008, Le localisme dans le monde académique | Locals 18× more likely hired; 6.3% vs 0.24% per application | OA (WEB) | https://laviedesidees.fr/Le-localisme-dans-le-monde.html | Save page; download the PDF version linked on the page | Success-rate table, local vs external |
| LOC-06 | Godechot, Issiakou, Renisio & Rougier 2025, Le localisme universitaire, nouvelles estimations | Locals 9.5–10.7× the odds (2017–24); physiology OR ~29 | OA PDF | https://booksandideas.net/IMG/pdf/20251118_godechot-2.pdf | Direct PDF; also look for the French original on laviedesidees.fr and any replication data | Odds ratio by discipline (best slide); local-rate trend 2002–2022 |
| LOC-07 | Combes, Linnemer & Visser 2008, Publish or peer-rich? (agrégation, economics) | Jury link raises the pass rate | OA (WP) | https://ideas.repec.org/p/lea/leawpi/0604.html ; journal: https://econpapers.repec.org/RePEc:eee:labeco:v:15:y:2008:i:3:p:423-441 | Working-paper PDF from RePEc | Effect size table (pass probability with vs without a jury link) |
| LOC-08 | Horta, Veloso & Grediaga 2010, Navel gazing (inbreeding and productivity) | Inbred faculty publish less | PW | https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.1090.1109 | Unpaywall (DOI 10.1287/mnsc.1090.1109) | Productivity regression table |
| LOC-09 | Horta 2022, Academic inbreeding: the state of the art | Review | PW | https://emerald.com/insight/content/doi/10.1108/S1479-362820220000015002 | Unpaywall; else abstract only | — |
| LOC-10 | Yudkevich, Altbach & Rumbley 2015, Academic Inbreeding and Mobility in Higher Education | Country cases | PW (book) | https://palgrave.com/us/book/9781137461247 | Save page; the user can get it through the library | Country comparison table if available |
| LOC-11 | Spain, ministry EPU data via El Salto | 72.9% of Spanish faculty work where they got their PhD | WEB | https://www.elsaltodiario.com/educacion/enclaustramiento-universidad-publica-espanola | Save page. Also find the underlying ministry "Estadística de Personal de las Universidades (EPU)" tables | Spain vs France comparison |
| LOC-12 | Sanz-Menéndez & Cruz-Castro 2006 (CSIC), via press | 96% of Spanish permanent-post winners already worked there | WEB/PDF | https://www.ucm.es/data/cont/media/www/pag-50946/ENDOGAMIA%20PAIS.pdf | Direct PDF; search for the CSIC working paper | — |
| LOC-13 | Portugal inbreeding report (DGES) | Not verified | PDF | https://www.dges.gov.pt/sites/default/files/endogamiaacademica_20212022.pdf (redirects) | Search iesuperior.pt for "endogamia académica" | Inbreeding rate by institution |

## 02 Social origin and class

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| SOC-01 | Observatoire des inégalités, from MEN data 2019–20 | Workers' children 12.3% (licence) → 5.9% (doctorate) | WEB | https://www.inegalites.fr/Les-milieux-populaires-largement-sous-representes-dans-l-enseignement-superieur | Save page; transcribe table | Social origin by degree level |
| SOC-02 | Martin-Kleinbauer & Maurin 2025, composition sociale des filières | ENS: cadres 65%, workers 2% (2024) | WEB | https://www.inegalites.fr/Enseignement-superieur-comment-evolue-la-composition-sociale-des-filieres | Save page; transcribe table | 2009 vs 2024 by track |
| SOC-03 | MESR RERS (Repères et références statistiques), chapter on students' social origin | Primary source for SOC-01/02 | DATA/PDF | https://www.enseignementsup-recherche.gouv.fr (search "RERS origine sociale des étudiants") | Download the latest RERS chapter 6 fiche and its XLS data. The site may block bots; retry with a browser user-agent | Social origin by level and track (official numbers) |
| SOC-04 | Céreq Bref n°452, 2024 (Génération 2017) | Doctoral students: 41% cadre parent vs 8% worker parent | PDF | https://www.cereq.fr/sites/default/files/2024-11/C%C3%A9req%20Bref%20452.pdf | Direct PDF | Cadre vs worker parent by level |
| SOC-05 | Bonneau, Charousset, Grenet & Thebault 2021, IPP report n°30 | Grandes écoles: 64% very privileged vs 23% of age group | OA PDF | https://www.ipp.eu/wp-content/uploads/2021/01/synthese-ipp-rapport-30-democratisation-grandes-ecoles.pdf | Direct PDF; also download the full report from ipp.eu | Students vs age group by class; trend 2006–2016 |
| SOC-06 | Morgan et al. 2022, Socioeconomic roots of academic faculty | 22.2% of US faculty have a PhD parent | OA PDF | https://escholarship.org/content/qt8pj425n7/qt8pj425n7.pdf ; DOI 10.1038/s41562-022-01425-4 | Direct PDF; check data availability statement | PhD-parent share by prestige decile |
| SOC-07 | Stansbury & Schultz 2023, economics' socioeconomic diversity problem | 48% of US econ PhDs have a parent with a graduate degree | OA | https://www.aeaweb.org/doi/10.1257/jep.37.4.207 ; summary https://cepr.org/voxeu/columns/us-economics-professions-socioeconomic-diversity-problem | JEP is free | Share by field over time |
| SOC-08 | Sutton Trust 2009, via Times Higher Education | 40% of RS/BA fellows privately educated vs 7% | WEB | https://www.timeshighereducation.com/news/four-in-ten-top-scholars-educated-privately/408584.article | Save page; search suttontrust.com for the original report | — |
| SOC-09 | DEPP, social origin of teachers vs working population 2015 | Not verified | OA | https://hal.science/hal-03097223 | HAL PDF | Check whether higher-education staff are included |

## 03 Ethnic and racial discrimination

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| ETH-01 | Insee, statistiques ethniques (legal framework) | Ethnic categories not allowed in public statistics | WEB | https://www.insee.fr/fr/information/2108548 | Save page | Text slide |
| ETH-02 | Chareyron, Erb & L'Horty 2022, testing access to master's programmes | 69.7% vs 61.1% reply rate | OA PDF | https://mission-egalite.univ-gustave-eiffel.fr/fileadmin/contributeurs/ONDES/Publications/Synthese-etude-discriminations-masters.pdf | Direct PDF; also look for the full TEPP report and the 2022 follow-up (2,100 programmes) | Reply rates by profile and discipline |
| ETH-03 | Dares Analyses n°67, 2021, hiring testing | Callbacks 33.3% vs 22.8% | OA PDF | https://migrant-integration.ec.europa.eu/system/files/2022-01/Dares%20Analyses_testing_discrimination_embauche.pdf | Direct PDF; original also on dares.travail-emploi.gouv.fr | Callback bars |
| ETH-04 | Cognet, Hajjat, Hamel et al. 2022, ACADISCRI first results | Racist incidents 27.8% vs 5.3% (staff, one university) | OA PDF | https://parite.math.cnrs.fr/References/2022_10_20_Rapport_Acadiscri.pdf | Direct PDF | Prevalence tables by group (also used in DIS-04) |
| ETH-05 | Défenseur des droits 2024, Dénoncer les discriminations vécues à l'université | 13.2% of students vs 46.5% of staff report | OA PDF | https://www.defenseurdesdroits.fr/sites/default/files/2024-04/ddd_eclairages_denoncer-les-discriminations-vecues-a-l-universite_20240423.pdf | Direct PDF | Reporting rate by motive (also used in DIS-05) |
| ETH-06 | TeO2 via Observatoire des inégalités 2023 | Discrimination: 37–42% (children of African immigrants) vs 15% | WEB | https://www.inegalites.fr/Pres-d-une-personne-sur-cinq-declare-avoir-ete-discriminee | Save page; also get the Insee Première / INED "Population & Sociétés" on TeO2 | Bars by origin |
| ETH-07 | INED December 2025, three-generation mobility (ASR paper) | 46% vs 55% reach higher education | OA PDF | https://www.ined.fr/sites/default/files/imported_images/ined.cpr.decembre.2025.vdef.fr.pdf | Direct PDF; find the American Sociological Review paper DOI | Mobility by origin |
| ETH-08 | Ginther et al. 2011, Race, ethnicity, and NIH awards | Black applicants ~10 points less likely funded | OA | press: https://news.ku.edu/news/article/2011/08/18/black-scientists-less-likely-white-counterparts-receive-nih-funding-study-shows ; DOI 10.1126/science.1196783 | PMC OA service (search PMC for the DOI) | Award rate by race |
| ETH-09 | Hoppe et al. 2019, topic choice and NIH awards | 10.7% vs 17.7%; topic explains ~20% | OA | https://www.stat.cmu.edu/~brian/valerie/617-2022/617-2021/0%20-%20NIH%20Peer%20review/Topic%20Choice%20-%20eaaw7238.full.pdf ; DOI 10.1126/sciadv.aaw7238 | Direct PDF | Award rate by topic cluster |
| ETH-10 | Erosheva et al. 2020, NIH review criteria scores | ~75% as successful after controls | OA | https://csss.uw.edu/about/news/interdisciplinary-research-team-examines-racial-disparities-nih-peer-review ; DOI 10.1126/sciadv.aaz4868 | Sci Adv OA | Criterion scores by race |
| ETH-11 | Taffe & Gilpin 2021, racial inequity at NIH | 1.7-fold gap unchanged 2011–19 | OA | https://elifesciences.org/articles/65697 | eLife PDF and figure source data | Award rates side by side |
| ETH-12 | Kozlowski et al. 2022, intersectional inequalities in science | +29% public-health papers if representative | OA | https://phys.org/news/2022-01-diversity-publishing.html ; DOI 10.1073/pnas.2113067119 | PMC OA service; check for data/code | Counterfactual topic output |
| ETH-13 | NCES Fast Facts, US faculty race (fall 2022) | 72% White, 7% Black, 6% Hispanic | WEB/DATA | https://nces.ed.gov/FastFacts/display.asp?id=61 | Save page; underlying IPEDS table (Digest table 315.20) | Faculty vs population |
| ETH-14 | HESA staff statistics 2022/23 | Black academics ~1% of UK professors | WEB/DATA | https://hesa.ac.uk/node/142008 | Save page; HESA open data CSV | Single statistic |

## 04 Nationality, language and foreign researchers

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| NAT-01 | MESR, L'état de l'emploi scientifique en France 2025 | Foreign share: 42% PhD graduates → 20.8% recruits → 7.8% tenured EC | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-05/l-tat-de-l-emploi-scientifique-en-france---rapport-2025-36858.pdf | Direct PDF (large) | Foreign-share tables along the pipeline; also age, contract status (cross-use in PREC) |
| NAT-02 | MESR-DGRH Note n°2-2026 (= LOC-01) | 23.5% of MCF vs 7.9% of PR foreign | PDF | see LOC-01 | — | Foreign share MCF vs PR, series 2020–2024 |
| NAT-03 | CNRS guide concours chercheurs 2023 | ~⅓ of recruits foreign; interview in French by default | PDF | https://www.cnrs.fr/sites/default/files/download-file/Guide%20concours%20chercheurs%202023_FR_V3.pdf | Direct PDF; also get CNRS bilan social (foreign share of recruits by year) | Callout; series if bilan social found |
| NAT-04 | Petit (CNRS CEO) interview | ~⅓ non-French recruits | WEB | https://www.researchprofessionalnews.com/?p=443189 | Save page | Quote |
| NAT-05 | Passeport talent testimony 2026 | ~5-month permit wait | WEB | https://www.plus.transformation.gouv.fr/experiences/7327070_delai-5-mois-passeport-talent-sous-prefecture-de-saint-denis | Save page (anecdotal) | Timeline |
| NAT-06 | Campus France, Chiffres clés 2025 | >430,000 foreign students | PDF | https://www.campusfrance.org/system/files/medias/documents/2025-05/CP_Chiffres_cles_2025_FR_vdef.pdf | Direct PDF | Origin breakdown |
| NAT-07 | Amano et al. 2023, costs of being a non-native English speaker | Up to 90.8% more reading time; 2.5× language rejections | OA | DOI 10.1371/journal.pbio.3002184 ; press https://www.eurekalert.org/news-releases/995037 | PLOS PDF and supporting data | Extra time by proficiency group; rejection odds |
| NAT-08 | Politzer-Ahles, Girolamo & Ghali 2020, linguistic bias in reviewing | Inconclusive (caveat) | PW | https://research.polyu.edu.hk/en/publications/preliminary-evidence-of-linguistic-bias-in-academic-reviewing/ | Repository PDF if available; Unpaywall | — |
| NAT-09 | Zumel Dumlao & Teplitskiy 2025, reviewer geography and author success | Same-country reviewer +4.78 points | PW/OA | DOI 10.1073/pnas.2507394122 ; abstract https://peerreviewcongress.org/abstract/geographical-representation-of-author-country-among-peer-reviewers-and-publishing-success-at-60-stem-journals/ | Unpaywall; arXiv/SSRN preprint | Same-country reviewer rate by income group |
| NAT-10 | Murray et al. 2019, author–reviewer homophily (eLife) | 39.2% (US) vs 12.6% (China) sent to full review | OA | https://elifesciences.org/inside-elife/f3645452/meta-research-researchers-study-implicit-bias-in-peer-review ; bioRxiv 10.1101/400515 | bioRxiv PDF | Encourage rate by country |
| NAT-11 | McGillivray & De Ranieri 2018, double-blind uptake at Nature journals | France 8% vs India 32% opt in | OA | https://arxiv.org/abs/1802.02188 | arXiv PDF | Uptake by country |
| NAT-12 | Lee, Sugimoto, Zhang & Cronin 2013, Bias in peer review | Review (caveat) | PW | https://ideas.repec.org/a/bla/jamist/v64y2013i1p2-17.html | Unpaywall (DOI 10.1002/asi.22784) | — |

## 05 Prestige and institutional bias

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PRES-01 | Huber et al. 2022, Nobel and novice | Reject: 23% (Nobel) vs 65% (junior) | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC9564227 ; release https://sowi.uni-graz.at/en/news/nobel-and-novice-author-prominence-affects-peer-review | PMC OA service | Three-bar recommendation chart |
| PRES-02 | Tomkins, Zhang & Heavlin 2017, single vs double blind | OR 1.63 famous author | OA | https://arxiv.org/pdf/1702.00502 | arXiv PDF | Odds-ratio table |
| PRES-03 | Merton 1968, The Matthew effect in science | Concept | PW | https://pubmed.ncbi.nlm.nih.gov/5634379 | Many OA copies; search "Merton 1968 Matthew effect pdf" | Quote |
| PRES-04 | Bol, de Vaan & van de Rijt 2018, Matthew effect in funding | Narrow winners >2× later funding | OA | https://dare.uva.nl/id/0a28688b-2628-4f9f-b0a3-206c5b388d7f ; PMC5948972 | Repository PDF | Fig. 1 funding over time |
| PRES-05 | Clauset, Arbesman & Larremore 2015, faculty hiring networks | 25% of institutions → 71–86% of faculty | OA | https://www.stat.cmu.edu/~brian/rm/764-2018/clauset-fac-hiring-2015.pdf ; DOI 10.1126/sciadv.1400005 | PDF; data on the authors' site | Lorenz curve; network |
| PRES-06 | Wapman et al. 2022, US faculty hiring | 80% from 20% of universities | OA + DATA | https://pmc.ncbi.nlm.nih.gov/articles/PMC9534765 | PMC OA service; data in DATA-09 | Fig. 1 Lorenz curve |
| PRES-07 | Hcéres-OST 2021, position scientifique de la France | Île-de-France 34.5% of publications | PDF | https://www.hceres.fr/sites/default/files/media/downloads/hceres_ost_positionnement_scientifique_france_edition_2021.pdf | Direct PDF | Regional share table/map; France world share over time |
| PRES-08 | MESR-SIES Note Flash 2026-06, business R&D 2024 | Île-de-France ~42% of business R&D | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-04/nf-sies-2026-06-39988.pdf | Direct PDF | Regional table |
| PRES-09 | ERC StG 2024 French results | 49 French winners, 25 at CNRS | WEB | https://www.horizon-europe.gouv.fr/resultats-de-l-appel-erc-starting-grants-2024-37575 | Save page; build host-institution table | By host institution |
| PRES-10 | L'Etudiant, Idex season 1 | 4 of first 8 Idex in Île-de-France | WEB | https://www.letudiant.fr/educpros/enquetes/idex-le-bilan-des-initiatives-d-excellence-saison-1-pour-les-universites.html | Save page | Idex map |
| PRES-11 | ANR atlas of projects 2014–2020 and Île-de-France summary | Not verified | PDF | https://anr.fr/fr/projets-finances-et-impact/donnees-analyses-et-etudes/atlas-des-projets-anr-2014-2020/ ; https://anr.fr/fileadmin/documents/2023/ANR-FRANCE2030-Synthese-regionale-2022-IDF-oct2023.pdf | Download atlas PDF and regional synthesis | ANR funding share by region |

## 06 Geography

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| GEO-01 | Gomez, Herman & Parigi 2022, citational lensing | Periphery under-cited, gap growing | PW | https://ideas.repec.org/a/nat/nathum/v6y2022i7d10.1038_s41562-022-01351-5.html ; DOI 10.1038/s41562-022-01351-5 | Unpaywall; SocArXiv preprint | Country-pair citation map |
| GEO-02 | Liu, Rahwan & AlShebli 2023, non-White scientists in publishing | Editors under-represent most African/Asian/S. American countries | OA | https://physicsworld.com/a/significant-inequalities-affect-non-white-researchers-when-publishing-their-work/ | Find the PNAS DOI from the article; PMC OA service | Editor vs author share scatter |
| GEO-03 | Harris et al. 2017, explicit bias toward high-income-country research | Up to 25% less recommended | PW | https://pubmed.ncbi.nlm.nih.gov/29137509 ; https://www.imperial.ac.uk/news/183046/research-from-poor-countries-deserves-fairer/ | Unpaywall (Health Affairs) | Paired ratings |
| GEO-04 | Harris et al. 2017, implicit association test | IAT 0.57 | OA | https://doaj.org/article/ca6c442de8c642d885cb15838619212b | Follow DOAJ link to Globalization and Health PDF | IAT distribution |
| GEO-05 | Skopec et al. 2020, geographic bias systematic review | 3 RCTs, 2 found bias | OA | https://doaj.org/article/fa26f5d855164c86ba283e60e5849ea6 | BMC PDF | — |
| GEO-06 | Smith et al. 2022, APCs and author geography | Zero OA mirror articles from low-income authors | OA | https://geog.ufl.edu/2022/02/21/assessing-the-effect-of-article-processing-charges-on-the-geographic-diversity-of-authors-using-elseviers-mirror-journal-system | Find QSS article (OA) from the page | Diversity OA vs non-OA |
| GEO-07 | Ross-Hellauer 2022, Open science, done wrong | APCs ~3× a Ukrainian professor's salary | OA PDF | https://media.nature.com/original/magazine-assets/d41586-022-00724-0/d41586-022-00724-0.pdf | Direct PDF | Quote |
| GEO-08 | Stefanoudis et al. 2021, parachute science | ~40% of papers with no local author | PW | https://www.eurekalert.org/news-releases/770393 ; DOI 10.1016/j.cub.2021.01.029 | Current Biology often free; Unpaywall | No-local-author share by country |
| GEO-09 | Mbaye et al. 2019, Who is telling the story? | 49.8% African first authors | OA | https://doaj.org/article/9f5b2b18d0df475ca5e313f14276f450 | BMJ Global Health PDF | Author positions |
| GEO-10 | Owusu-Gyamfi 2024, EU visa ordeal | 4 of 10 LMIC speakers got visas | OA PDF | https://www.nature.com/articles/d41586-024-00892-1.pdf | Direct PDF | Quote |
| GEO-11 | VentureBeat 2019, NeurIPS visa denials | 15 of 44 denied | WEB | https://venturebeat.com/ai/canada-is-denying-travel-visas-to-ai-researchers-headed-to-neurips-again | Save page | Icon graphic |

## 07 Precarity, age and career stage

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PREC-01 | MESR-DGRH Note n°6-2025, contract teachers 2024 | 21,080 contract vs 61,879 tenured | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-01/note-dgrh-n-6---2025---enseignants-contractuels-ann-e-2024-pdf-39144.pdf | Direct PDF; get earlier editions for a series | Category table (series) |
| PREC-02 | SNESUP dossier n°734, 2025 | EC posts 3,613 (2011) → 2,378 (2023) | PDF | https://www.snesup.fr/sites/default/files/2025-06/dossier-mensuel-snesup734.pdf | Direct PDF; cross-check with DGRH campaign notes (PREC-03) | Posts and staff vs students, 2008–2023 |
| PREC-03 | MESR-DGRH Note n°2-2025, 2023 campaign | 1,567 MCF posts, 8,110 candidates | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-10/note-dgrh-n-2---2025---campagne-2023-pdf-38079.pdf | Direct PDF; collect every campaign note back to 2008 for posts opened per year | Posts opened by year (series) |
| PREC-04 | MESR-DGRH Note n°7-2022, 2021 campaign | 7.7 candidates per MCF post | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2023-01/note-dgrh-n-7-septembre-2022---campagne-2021-26095.pdf | Direct PDF | Candidates per post (series) |
| PREC-05 | MESR-DGRH Note n°3-2025 (= LOC-02) | New MCF age 35; 42% from postdoc | PDF | see LOC-02 | — | Previous status 2005 vs 2023; age at hiring |
| PREC-06 | Cour des comptes, CNRS 2013–2023 (via Acteurs Publics) | CR recruitment age 34.4 (2020) | WEB | https://acteurspublics.fr/articles/confronte-a-un-mur-du-vieillissement-le-cnrs-doit-revoir-sa-politique-dattractivite-pour-assurer-la-perennite-de-ses-activites/ | Save page | — |
| PREC-07 | Cour des comptes, CNRS 2013–2023 full report | Contract staff 23% → 29% | PDF | https://campusmatin.com/file/a706bd62d95ab4dcc9c1a4df08973ee9/rapport-cour-comptes-exercices-2013-2023-cnrs.pdf | Direct PDF; also from ccomptes.fr | Age at recruitment series; contract share; applications vs posts |
| PREC-08 | MESR-SIES Note Flash n°14, 2025, doctoral students | 81% funded; 53% in humanities | PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-06/nf-2025-14-37279.pdf | Direct PDF | Funded share by field |
| PREC-09 | Assemblée nationale question n°1155, 2025, vacataires | €8.37/h effective | PDF | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1155.pdf | Direct PDF | Effective hourly pay vs SMIC |
| PREC-10 | SNESUP, CPJ first review 2024 | 25% women in junior chairs | PDF | https://www.snesup.fr/sites/default/files/2024-11/cpjpremierbilan_p19ndeg728.pdf | Direct PDF | Women's share CPJ vs PR |
| PREC-11 | Milojević, Radicchi & Walsh 2018, changing demographics of scientific careers | Half leave within ~5 years | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC6294951 | PMC OA service | Survival curves by cohort |
| PREC-12 | Andalib, Ghaffarzadegan & Larson 2018, The postdoc queue | ~17% reach tenure track | PW | https://econpapers.repec.org/RePEc:bla:srbeha:v:35:y:2018:i:6:p:675-686 | Unpaywall | Funnel |
| PREC-13 | Antman et al. 2021, NCI R01 workforce | Age at first R01 36.2 → 44.9 | OA | https://jci.org/articles/view/146925 | JCI PDF | Age over time |
| PREC-14 | Nature postdoc survey 2020 | 51% considered leaving over mental health | OA | https://doi.org/10.1038/d41586-020-02541-9 | Nature news is free | Survey bars |
| PREC-15 | Jones & Weinberg 2011, age dynamics in scientific creativity | Age at Nobel work 36.9 → 50.3 (physics) | OA | DOI 10.1073/pnas.1102895108 ; summary https://www.lindau-nobel.org/?p=22157 | PMC OA service | Age-at-discovery trend |

## 08 Disability and LGBTQ+

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| DIS-01 | SNESUP Métier n°743, 2026 | ESR disability rate 4.49% vs 6% | PDF | https://www.snesup.fr/sites/default/files/2026-06/metier_snesup-ndeg743p18.pdf | Direct PDF; cross-check with the MESR or FIPHFP official rate | Institutions vs 6% line |
| DIS-02 | SNCS disability working group minutes, 2025 | CNRS 5.3%; ~1.5% among DR | PDF | https://sncs.fr/wp-content/uploads/2025/09/250617-CR_AG-Hand-SNCS_Internet.pdf | Direct PDF; cross-check with the CNRS bilan social | Rate by grade |
| DIS-03 | Inserm disability plan 2023–2025 | Not verified | PDF | https://pro.inserm.fr/wp-content/uploads/2025/03/PlanHandicapInserm_2023-%202025.pdf | Direct PDF (URL has a space; try both encodings) | Inserm disability rate |
| DIS-04 | ACADISCRI report 2022 (= ETH-04) | 13.8% of LGBTQ+ staff face LGBT-phobic treatment | OA PDF | see ETH-04 | — | Prevalence by group |
| DIS-05 | Défenseur des droits 2024 (= ETH-05) | Reporting: students 17–21%, staff 43–51% | OA PDF | see ETH-05 | — | Reporting by motive |
| DIS-06 | DREES fiche 2.4, 2025, disabled students | ~58,880 (~2%) | PDF | https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-08/Fiche%202.4%20-%20Les%20%C3%A9tudiants%20handicap%C3%A9s.pdf | Direct PDF | Students over time |
| DIS-07 | MESR guide on LGBTI-phobia in ESR, 2026 | 33% of trans/non-binary students faced sexual violence | PDF | https://www.etudiant.gouv.fr/sites/default/files/2026-07/lutter-contre-les-violences-et-les-discriminations-fond-es-sur-l-orientation-sexuelle-l-identit-de-genre-et-la-sexuation-dans-l-enseignement-sup-rieur-et-la-recherche-8353.pdf | Direct PDF; follow its references to the MILDECA and Caelif surveys | Bars by gender |
| DIS-08 | Cech & Waidzunas 2021, LGBTQ in STEM | 22% vs 15% considered leaving | OA | https://record.umich.edu/articles/social-exclusion-career-limitations-hinder-lgbtq-stem-professionals ; DOI 10.1126/sciadv.abe0933 | PMC OA service | LGBTQ vs non-LGBTQ bars |
| DIS-09 | IOP/RAS/RSC 2019, LGBT+ physical scientists | ~1 in 3 considered leaving | WEB/PDF | https://www.nature.com/nature-index/news/discrimination-drives-lgbt-plus-scientists-think-about-quitting ; report https://www.rsc.org/globalassets/04-campaigning-outreach/campaigning/lgbt-report/lgbt-report_web.pdf | Try the RSC PDF; else save the Nature Index page | Report figures |
| DIS-10 | Swenor, Munoz & Meeks 2020, a decade of decline | NIH applicants with disability 1.9% → 1.2% | OA | https://ideas.repec.org/a/plo/pone00/0228686.html | PLOS PDF | Line 2008–2018 |
| DIS-11 | NCSES Diversity and STEM 2023 | Disabled: 11% of S&E PhDs, 3% of workforce | DATA | https://www.eurekalert.org/news-releases/978111 ; https://ncses.nsf.gov/pubs/nsf23315 | Data tables (XLSX) from NCSES | PhDs vs workforce |
| DIS-12 | Advance HE 2024 staff statistical report | UK staff declaring disability 3.2% → 7.2% | PDF | https://advance-he.ac.uk/news-and-views/equality-higher-education-staff-statistical-report-2024 | Report PDF and data tables | Line 2010–2023 |

## 09 Peer review and evaluation

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PEER-01 | NeurIPS 2021 consistency experiment | 50.6% of accepted papers rejected by the other committee | WEB | https://blog.neurips.cc/2021/12/08/the-neurips-2021-consistency-experiment | Save page; get the follow-up arXiv paper (Beygelzimer et al. 2023) | 2×2 decision table |
| PEER-02 | Cortes & Lawrence 2021, NeurIPS 2014 revisited | ~50% of score variation subjective | OA | https://arxiv.org/abs/2109.09774 | arXiv PDF; data/code on GitHub (see paper) | Score vs citations |
| PEER-03 | Pier et al. 2018, NIH reviewer agreement | ICC = 0 | OA | https://www.Gwern.net/doc/statistics/peer-review/2018-pier.pdf ; DOI 10.1073/pnas.1714379115 | PDF | Scores per application |
| PEER-04 | Cole, Cole & Simon 1981, chance and consensus (via Harnad) | ~25% of NSF decisions reversed | PW | https://eprints.soton.ac.uk/253397/1/harnad85.peerev.html ; DOI 10.1126/science.7302566 | Unpaywall; else the Harnad page | Concordance matrix |
| PEER-05 | Boudreau et al. 2016, novelty and evaluation | Novel proposals scored lower | PW | https://ideas.repec.org/a/inm/ormnsc/v62y2016i10p2765-2783.html | Unpaywall; HBS working paper version | Score vs novelty |
| PEER-06 | Wang, Veugelers & Stephan 2017, bias against novelty | +39.8% odds of top-1% at 14 years | OA (WP) | https://www.nber.org/papers/w22180.pdf | Direct PDF | Crossing curves by citation window |
| PEER-07 | Mahoney 1977, confirmation bias in peer review | Confirming results rated higher | WEB | https://pages.stern.nyu.edu/~wstarbuc/Writing/Prejud.htm | Save page | Ratings by condition |
| PEER-08 | Fang & Casadevall 2016, modified lottery | Paylines >50% → ~10% | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC4959526 | PMC OA service | Payline over time |
| PEER-09 | Liu et al. 2020, NZ HRC lottery | 63% find the lottery acceptable | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC6996170/ | PMC OA service | Support by outcome |
| PEER-10 | SNSF 2021, drawing lots as tie-breaker | ~3% of proposals affected | WEB | https://snf.ch/en/JyifP2I9SUo8CPxI/news/news-210331-drawing-lots-as-a-tie-breaker | Save page; look for SNSF evaluation report | Draw-zone schematic |
| PEER-11 | Volkswagen Foundation partial randomization, via DORA 2025 | Same output; more diverse winners | WEB | https://sfdora.org/2025/03/27/insights-on-partial-randomization-in-research-funding-learnings-from-the-volkswagen-foundation/ | Save page; find the foundation's evaluation report | Cohort comparison |
| PEER-12 | McKiernan et al. 2019, impact factor in promotion | 40% of R1 documents mention JIF | OA + DATA | https://doaj.org/article/280ae1471f8b4a169addf4045882af42 ; https://elifesciences.org/articles/47338 | eLife PDF; data on OSF/Dryad (see paper) | By institution type |
| PEER-13 | MESR-DGRH CNU qualification 2024 (provisional) | 64.8% qualified; 33.8%–84.5% by discipline | PDF | https://enseignementsup-recherche.gouv.fr/sites/default/files/2024-09/bilan-provisoire-de-la-campagne-de-qualification-2024-pdf-34258.pdf | Direct PDF; earlier campaigns for a series | Rate by discipline |
| PEER-14 | CNRS evaluation reform | DORA 2018; narrative of selected outputs | WEB | https://www.cnrs.fr/en/node/6288 | Save page | Reform timeline |
| PEER-15 | DORA, Inserm profile | Metrics still dominant (2021) | WEB | https://sfdora.org/institutions/inserm/ | Save page; also get Inserm CSS criteria https://pro.inserm.fr/wp-content/uploads/2026/03/DR2-Criteres-Evaluation_CSS.pdf | Reform timeline; criteria text |
| PEER-16 | ANR and DORA | Signed 2018 | WEB | https://anr.fr/fr/lanr/engagements/la-declaration-de-san-francisco/ | Save page; check whether ANR now uses a narrative CV | Reform timeline |
| PEER-17 | CoARA French chapter | 49 French signatories (Aug 2023) | PDF | https://www.enssib.fr/bibliotheque-numerique/documents/71623-coara-french-chapter.pdf | Direct PDF; current list on coara.org | Signatories by type |
| PEER-18 | Hcéres-OST Inserm indicators 2020 | 14% of French output; impact 1.3 | WEB/PDF | https://hceres.fr/rapport-indicateurs-2020-Inserm | Save page and linked PDF | Example indicators |

## 10 Datasets and tools

| ID | Dataset / tool | Maintainer | Link | How to download | What to plot |
|---|---|---|---|---|---|
| DATA-01 | Tenured higher-education staff open data | MESR-SIES | https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-enseignants-titulaires-esr-public/ | API: `https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public/exports/csv` | Staff by age, CNU section, institution, region over years |
| DATA-02 | Other MESR open datasets (contract staff, doctoral students, qualification, recruitment) | MESR-SIES | https://data.enseignementsup-recherche.gouv.fr/explore/ | Search the catalogue for "contractuels", "doctorants", "qualification", "recrutement"; export each as CSV | Precarity and recruitment series |
| DATA-03 | ANR funded projects and partners | ANR | https://www.data.gouv.fr/organizations/agence-nationale-de-la-recherche/datasets | Download ANR_01 (projects) and ANR_02 (partners) as CSV. Join on project code and aggregate funding by partner region | Regional concentration of ANR funding (Île-de-France share by year) |
| DATA-04 | ERC call statistics | ERC | https://erc.europa.eu/system/files/2026-09/erc-2026-stg-statistics.pdf | Download the statistics PDF for each call (StG, CoG, AdG, last 5 years); transcribe host-country tables | Grants by host country and nationality |
| DATA-05 | TeO2 microdata | Insee / INED | https://www.insee.fr/fr/metadonnees/source/operation/s2086/acces-micro-donnees | Requires an application through Quetelet-Progedo or CASD. Do not attempt; note it as user action | Education and discrimination by origin |
| DATA-06 | Céreq Génération surveys | Céreq | https://www.insee.fr/fr/statistiques/fichier/5762573/BFE-presentation-enquetes-generation.pdf | Requires a Quetelet-Progedo account. Note it as user action; download the published Céreq Bref tables instead | Labour-market entry by social origin |
| DATA-07 | OpenAlex | OurResearch | https://help.openalex.org/api/grouping/ | Free API, e.g. `https://api.openalex.org/works?filter=institutions.country_code:FR,publication_year:2023&group_by=authorships.institutions.id` (add `mailto=` param) | French output by institution or region; country citation shares |
| DATA-08 | NCSES Survey of Earned Doctorates | NSF | https://www.ncses.nsf.gov/pubs/nsf24300/report/path-to-the-doctorate | Data tables (XLSX) linked on the report page | Parental education by race of US PhDs |
| DATA-09 | US faculty hiring networks | Larremore lab | https://larremorelab.github.io/us-faculty | `git clone` the `us-faculty-hiring-networks` repo or download Zenodo 10.5281/zenodo.6941650 | Prestige Lorenz curves; hiring networks |
| DATA-10 | Nature Index Research Leaders | Springer Nature | https://www.nature.com/nature-index/research-leaders/2026/country/all/global | "Export CSV" button on each table (may need a headless browser) | Country and institution shares |
| DATA-11 | CoARA/DORA by-numbers dataset | Zenodo | https://zenodo.org/records/17846515 | Direct file download | Reform uptake by institution |

---

## Known gaps

- No official ethnic data on French academics; this is barred by law (see ETH-01).
- No published data on the social origin of French enseignants-chercheurs or CNRS/Inserm researchers.
- No study of discrimination against foreigners in French academic hiring.
- No official Inserm disability rate online (try DIS-03).
- No Cour des comptes evaluation of localism or of the Idex programme with numbers.
- CNRS disability rates (DIS-02) and ESR-wide rate (DIS-01) come from union documents; cross-check with official sources.
