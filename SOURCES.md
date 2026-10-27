# Gender bias in academia data sources

Source list for a data-driven talk on gender bias in academia, compiled 2026-10-27. It has 126 sources in 10 sections. Each entry gives a stable ID, a link, how open the source is, how to download it, and what to extract (the figure or table worth a slide).

---

## Instructions for the collecting agent

1. **Folder layout.** Use one folder per section and one subfolder per source ID:
   ```
   gender-bias-data/
     manifest.csv
     01-pipeline/PIPE-01/{source.pdf|data.csv|page.html, figures/, notes.md}
     ...
   ```
2. **Manifest.** Keep `manifest.csv` with these columns: `id, title, url_used, file_paths, access_status (downloaded|abstract_only|paywalled|failed), figures_extracted, notes`. Write one row per ID, even when the download failed.
3. **Download order for papers with a DOI.**
   1. Resolve the open-access copy through Unpaywall: `https://api.unpaywall.org/v2/<DOI>?email=<your-email>`. Take `best_oa_location.url_for_pdf`.
   2. If that gives nothing, try the "OA copy" link listed for the entry (PMC, arXiv, bioRxiv, SSRN/NBER, the author's site or a repository).
   3. For PMC articles, use the PMC OA service: `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC<id>`. It returns a tar.gz containing the PDF and figure files.
   4. For arXiv, use `https://arxiv.org/pdf/<id>`. For bioRxiv, use `https://www.biorxiv.org/content/<DOI>v<N>.full.pdf`.
   5. If the paper is still paywalled, save the abstract page as HTML and set `access_status=paywalled`. Do not use shadow libraries; the user can fetch the paper through institutional access.
4. **Figures.** For each "Extract" item, crop the named figure from the PDF at 300 dpi or more, saved as `figures/<ID>_fig<N>.png`. When the source provides data (CSV, supplementary tables, a source-data file), save the data as well, so the plot can be redrawn in a consistent style.
5. **Datasets.** Prefer API or bulk CSV exports over screenshots. Record the query or filters used in `notes.md` so the plot can be reproduced.
6. **Verify.** Record one headline number per source in `notes.md` and check it against the "Key number" column. Flag any mismatch.
7. **Press pages.** Some links point to a press release or mirror, because the original was unreachable when this list was made. In those cases always try the DOI first. Where a DOI is marked *(unverified)*, confirm it before use.

Access codes used below: **OA** = open access · **PW** = paywalled (OA copy may exist) · **DATA** = downloadable dataset · **WEB** = web page or interactive (export or screenshot).

---

## 01 Pipeline and representation

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PIPE-01 | She Figures 2024 (European Commission) | EU women 48% of PhDs, 30% of grade A | WEB / DATA | https://projects.research-and-innovation.ec.europa.eu/en/knowledge-publications-tools-and-data/interactive-reports/she-figures-2024 | Download the full report PDF from the page. Look for a "data"/"download" link for the underlying tables (Excel); else search the EC Publications Office for "She Figures 2024" | Ch. 6 scissor chart (ISCED 8 → grades D/C/B/A); Glass Ceiling Index table |
| PIPE-02 | She Figures 2024 infographics | Women ~⅓ of authors, 9% of patent applicants | OA PDF | https://european-research-area.ec.europa.eu/sites/default/files/documents/2025-03/she%20figures%202024-KI0924569ENN-infographics.pdf | Direct PDF | Pipeline infographic |
| PIPE-03 | She Figures 2024 France country fiche | France 44% PhDs, 30% grade A | OA PDF | https://ec.europa.eu/assets/rtd/shefigures/2024/files/shefigures2024fiche-fr.pdf | Direct PDF | France vs EU-27 values (redraw as bars) |
| PIPE-04 | MESR, *Vers l'égalité femmes-hommes ? Chiffres clés 2026* | 33% of PR women (17% in 2000) | OA PDF | https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-03/vers-l-galit-femmes-hommes-chiffres-cl-s-2026-39611.pdf | Direct PDF. Earlier editions are on the same site for a time series | Doctorates by discipline (p. 28); researchers by discipline (p. 42); MCF/PR shares |
| PIPE-05 | CNRS Plan d'action égalité professionnelle 2024–2026 | 34.7% researchers, 31.7% DR women | OA PDF | https://parite.math.cnrs.fr/References/CNRS_Plan_action_2024-26.pdf | Direct PDF | Women share CR vs DR, 2019→2022 |
| PIPE-06 | Inserm, Journée Inserm 2024 parity slides | Equality index 72/100; 13.1% pay gap | OA PDF | https://pro.inserm.fr/wp-content/uploads/2024/03/JI2024_Parite.pdf | Direct PDF. Also look for the Inserm "Rapport social unique" (grade-level CR/DR shares) on pro.inserm.fr | Index breakdown slide |
| PIPE-07 | NCSES, Doctorate Recipients from US Universities 2024 (NSF 26-315) | Women 48% of US research doctorates | DATA | https://ncses.nsf.gov/pubs/nsf26315 | The page has "Data tables" (Excel/CSV downloads) | Fig. 4 doctorates by sex and field 2004–24 (redraw from tables) |
| PIPE-08 | NCSES, Diversity and STEM 2023 (NSF 23-315) | Women ~35% of US STEM workforce | DATA | https://ncses.nsf.gov/pubs/nsf23315 (press: https://www.eurekalert.org/news-releases/978111) | Report hub has data tables (Excel) | STEM workforce share by occupation |
| PIPE-09 | ASEE *By the Numbers 2024* via SWE | Engineering: 28.7% asst, 21.8% assoc, 15.6% full | WEB | https://swe.org/research/2026/tenure-tenure-track-faculty/ | Save page; numbers are in the text | Rank-by-rank bars (redraw) |
| PIPE-10 | UNESCO 2025, *Status and trends of women in science* | Women 31.1% of researchers worldwide | OA PDF | https://unesdoc.unesco.org/ark:/48223/pf0000393768 | Download PDF from UNESDOC | Fig. 3 regions 2012 vs 2022 |
| PIPE-11 | OECD *Education at a Glance 2025*, indicator D5 | Women 46% of academic staff | DATA | https://www.oecd-ilibrary.org/en/publications/education-at-a-glance-2025_1c0d9c79-en/full-report/how-do-academic-staff-profiles-and-institutional-characteristics-shape-tertiary-education_4128fd24 | Each figure/table has a StatLink (Excel). Also OECD Data Explorer, "Education and training" | Fig. D5.5 trend; Table D5.3 by age |
| PIPE-12 | Elsevier, *Progress Towards Gender Equality in Research & Innovation, 2024 Review* | Women 41% of active researchers (2022) | WEB / PDF | https://www.elsevier.com/about/press-releases/latest-elsevier-gender-equality-study-reveals-20-years-of-progress-but-challenges-remain-for-women-in-research-and-innovation | Follow the report link (may require a free form) | Trend by country 2001–2022 |
| PIPE-13 | Huang, Gates, Sinatra & Barabási 2020, PNAS | Dropout 10.8% vs 9.0%/yr; productivity gap 27%→9% | OA | DOI 10.1073/pnas.1914221117 *(unverified)*; OA: https://pmc.ncbi.nlm.nih.gov/articles/PMC7060730 ; arXiv 1907.04103 | PMC OA service or arXiv PDF; SI has data descriptions | Fig. 4 dropout and survival curves |
| PIPE-14 | Spoon et al. 2023, Science Advances, gender and retention among US faculty | Women 6% (asst) / 19% (full) more likely to leave | OA | DOI 10.1126/sciadv.adi2205 ; press: https://www.colorado.edu/today/2023/10/20/harsh-workplace-climate-pushing-women-out-academia ; PMC10588949 | Sci Adv is OA; PMC copy. Check the paper's data availability statement for a code/data repo | Attrition by stage; push vs pull bars |
| PIPE-15 | LaBerge, Wapman, Clauset & Larremore 2024, eLife | Women 36% of US tenure-track; parity not by 2060 | OA | https://elifesciences.org/articles/93755 | eLife PDF + figure source data; check its data/code links | Fig. 3 projections under 5 scenarios |
| PIPE-16 | Wapman, Zhang, Clauset & Larremore 2022, Nature | 103/107 fields: hires more female than departures | OA | DOI 10.1038/s41586-022-05222-x ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9534765 | PMC OA service; the faculty census data are released with the paper (see Data availability) | Fig. 4c women share by career age |
| PIPE-17 | Shaw & Stanton 2012, Proc R Soc B, leaks in the pipeline | 28% observed vs 39% predicted asst profs | OA | Postprint: https://allisonkshaw.github.io/files/2012_ShawStanton_ProcRSocB_postprint.pdf ; DOI 10.1098/rspb.2012.0822 *(unverified)* | Direct PDF | Fig. 2 model vs data; Fig. 3 leak index |

## 02 Hiring and evaluation

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| HIRE-01 | Moss-Racusin et al. 2012, PNAS, science faculty's subtle gender biases | $26.5k vs $30.2k offered | OA | DOI 10.1073/pnas.1211286109 ; summary: https://gap.hks.harvard.edu/science-faculty%E2%80%99s-subtle-gender-biases-favor-male-students | PNAS is free after 6 months; Unpaywall / PMC | Fig. 1 competence/hireability/mentoring; Fig. 2 salary |
| HIRE-02 | Steinpreis, Anders & Ritzke 1999, Sex Roles, CV review | Same CV: "male" more likely hired | OA copy | https://www.engr.washington.edu/files/mycoe/faculty/docs/ImpactofGenderdoc.pdf | Direct file (doc/PDF) | Fig. 5 hire votes by name × rater |
| HIRE-03 | Williams & Ceci 2015, PNAS, national hiring experiments | 2:1 preference for women | OA | DOI 10.1073/pnas.1418878112 ; PMC4418903 ; press: https://news.cornell.edu/node/284291 | PMC OA service | Preference by field and rater gender |
| HIRE-04 | Régner et al. 2019, Nature Human Behaviour, CNRS promotion committees | Implicit bias hurts only where bias is denied | OA PDF | DOI 10.1038/s41562-019-0686-3 ; https://www.nature.com/articles/s41562-019-0686-3.pdf ; CNRS release: https://www.cnrs.fr/en/press/even-scientists-have-gender-stereotypes-which-can-hamper-career-women-researchers | Direct PDF; also check supplementary info | Interaction plot (implicit bias × belief) and supp. Fig. 1; Fig. 1 % women by discipline |
| HIRE-05 | Schmader, Whitehead & Wysocki 2007, Sex Roles, recommendation letters | More "standout" words for men | OA copy | DOI 10.1007/s11199-007-9291-4 ; https://link.springer.com/content/pdf/10.1007/s11199-007-9291-4.pdf ; PMC2572075 | PMC OA service | Standout words per letter |
| HIRE-06 | Madera, Hebl & Martin 2009, J Appl Psychol, letters for academia | Women described as more communal | PW | DOI 10.1037/a0016539 ; https://pubmed.ncbi.nlm.nih.gov/19916666/ | Unpaywall; else abstract only | Agentic vs communal counts |
| HIRE-07 | Dutt et al. 2016, Nature Geoscience, postdoc letters | 15% "excellent" (women) vs 24% (men) | PW | DOI 10.1038/ngeo2819 ; https://serc.carleton.edu/details/files/138789.html | Unpaywall; serc.carleton.edu may host a copy | Stacked letter categories |
| HIRE-08 | Lerchenmueller, Sorenson & Jena 2019, BMJ, self-promotion | 12.3% fewer positive terms (WW papers) | OA | DOI 10.1136/bmj.l6573 | BMJ research is OA; Unpaywall | Positive terms over time by author-gender pair |

## 03 Funding

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| FUND-01 | Witteman et al. 2019, Lancet, applicant vs science | Gap 4.0 pts (applicant) vs 0.9 (science) | PW | DOI 10.1016/S0140-6736(18)32611-4 ; mirror: https://prod.sdgresources.relx.com/node/997 | Unpaywall; else the relx mirror | Success rate by review type (key slide) |
| FUND-02 | Wennerås & Wold 1997, Nature, nepotism and sexism | +64 impact points needed | OA copy | https://www.cs.utexas.edu/~mckinley/notes/ww-nature-1997.pdf | Direct PDF | Competence vs productivity figure |
| FUND-03 | Grant, Burden & Breen 1997, Nature, no evidence of sexism | 27.5% vs 26.9% | PW | https://www.nature.com/articles/37216.pdf | Direct PDF (may be paywalled) | Success-rate numbers (redraw) |
| FUND-04 | van der Lee & Ellemers 2015, PNAS, NWO Veni | 17.7% vs 14.9% | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC4603485 | PMC OA service; check comments/replies in PNAS too | Success by discipline |
| FUND-05 | Hechtman et al. 2018, PNAS, NIH funding longevity | No gap after matching | OA | PMC6077749 ; blog: https://nigms.nih.gov/node/137966 | PMC OA service | Funding survival curves |
| FUND-06 | Oliveira, Ma, Woodruff & Uzzi 2019, JAMA, NIH award size | $165.7k vs $126.6k median | OA | https://jamanetwork.com/journals/jama/fullarticle/2726973 | JAMA research letters often free; Unpaywall | Median award by institution tier |
| FUND-07 | Ginther, Kahn & Schaffer 2016, Academic Medicine | Race, not gender, main factor | PW | press: https://news.ku.edu/2016/07/07/ku-study-finds-race-not-gender-key-factor-nih-awards | Find DOI via PubMed search "Ginther Kahn Schaffer 2016 Academic Medicine"; Unpaywall | Award probability by race × gender |
| FUND-08 | Forscher et al. 2019, Nature Human Behaviour, R01 name-swap | Little/no gender bias | OA copy | https://www.omicsdi.org/dataset/biostudies-literature/S-EPMC6699508 (PMC6699508) | PMC OA service; data on OSF (see paper) | Scores by manipulated PI identity |
| FUND-09 | Kolev, Fuentes-Medel & Murray 2019, NBER w25759, Gates review | Women 16% less likely to score high | OA | https://nber.org/papers/w25759 | NBER PDF: https://www.nber.org/system/files/working_papers/w25759/w25759.pdf | Gap before/after text controls |
| FUND-10 | Severin et al. 2020, BMJ Open, SNSF peer review | +0.18 on 1–6 scale for men | OA PDF | https://boris.unibe.ch/146089/1/Severin%20BMJOpen%202020.pdf | Direct PDF | Score by applicant × reviewer gender |
| FUND-11 | Bornmann, Mutz & Daniel 2007, J Informetrics, meta-analysis | Men +7% odds | OA | https://arxiv.org/abs/math/0701537 | arXiv PDF | Forest plot |
| FUND-12 | Schmaling & Gallo 2023, Research Integrity & Peer Review | Award rate gap ~1 pt; amounts differ | OA PDF | https://link.springer.com/content/pdf/10.1186/s41073-023-00127-3.pdf | Direct PDF + supplementary data | Forest plots (rates vs amounts) |
| FUND-13 | Tricco et al. 2017, PLOS ONE, interventions in grant review | 1 tested intervention in 5,524 records | OA | https://econpapers.repec.org/RePEc:plo:pone00:0169718 | Get DOI from page → journals.plos.org PDF | (cite only) |
| FUND-14 | ERC gender flyer 2022 | StG 24% vs AdG 12% women grantees | OA PDF | https://erc.europa.eu/sites/default/files/2022-09/gender_flyer.pdf | Direct PDF | Applicants vs grantees, StG vs AdG |
| FUND-15 | ERC gender statistics June 2022 | Values in charts only | OA PDF | https://erc.europa.eu/sites/default/files/2022-11/Gender_statistics_June_2022.pdf | Direct PDF; digitise charts if needed | Success by gender per call/domain |
| FUND-16 | Jesus-Rydin et al. (ERCEA), EGU24-16168 | StG 0.5–1 pt lower for women | OA PDF | https://presentations.copernicus.org/EGU24/EGU24-16168_presentation.pdf | Direct PDF | Success by gender and extension |
| FUND-17 | ERC 2024 StG results | Women 44% of StGs | WEB | https://erc.europa.eu/news-events/news/erc-2024-starting-grants-results | Save page + linked statistics PDF | Female share of StG over years (build series from yearly releases) |
| FUND-18 | ERC AdG 2023/2024 facts and figures | Women 23.5% of AdG 2023 | WEB | https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2024-facts-and-figures ; https://timeshighereducation.com/news/proportion-female-winners-top-erc-grants-dips | Save pages | StG vs AdG share |
| FUND-19 | ANR 2026, *Femmes et hommes dans l'AAPG 2015–2025* | Success 26% vs 24% (2024) | OA PDF | https://anr.fr/fileadmin/documents/2026/ANR-femmes-et-hommes-aapg-2015-2025-04206.pdf | Direct PDF | Success by gender 2015–2025, JCJC / PRC |
| FUND-20 | Wellcome funding data 2024/25 | 10.4% vs 9.4% | DATA | https://wellcome.org/research-funding/funding-portfolio/funding-data-2024 | Download CSV/Excel linked on the page | Success over time |
| FUND-21 | NIH RePORT, gender report | Funding rate by gender | DATA | https://report.nih.gov/reportweb/web/displayreport?rId=1005 | Report pages have Excel export | Success rate by gender over FYs |

## 04 Publishing and peer review

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PUB-01 | Larivière et al. 2013, Nature, global disparities | Women <30% of authorships | PW | DOI 10.1038/504211a | Unpaywall; the authors' lab site may host a copy | World map of authorship share |
| PUB-02 | Holman, Stuart-Fox & Hauser 2018, PLoS Biol, how long until parity | Physics ~258 years to parity | OA + DATA | DOI 10.1371/journal.pbio.2004956 ; tool https://lukeholman.github.io/genderGap/ | PLoS PDF; data/code linked in the paper (GitHub/OSF) | Trajectories to parity by field |
| PUB-03 | Ross et al. 2022, Nature, women credited less | 13% less likely named on articles | OA | https://www.nature.com/articles/s41586-022-04966-w | Direct (OA); source data files | Authorship probability by stage |
| PUB-04 | Helmer et al. 2017, eLife, peer review | Women 28% of reviews vs 37% of authorships | OA | https://elifesciences.org/articles/21718 | eLife PDF + source data | Authors → reviewers → editors |
| PUB-05 | Squazzoni et al. 2021, Science Advances, 145 journals | No penalty for women | OA | DOI 10.1126/sciadv.abd0299 | Sci Adv OA | Acceptance odds by team composition |
| PUB-06 | Fox & Paine 2019, Ecology & Evolution | 16.4% vs 18.3% invited to revise | OA | DOI 10.1002/ece3.4993 ; PMC6434606 | PMC OA service; data on Dryad (see paper) | Success by review stage |
| PUB-07 | Lerback & Hanson 2017, Nature, reviewers | Women 20% of reviewers vs 27% of first authors | PW | DOI 10.1038/541455a | Unpaywall | Reviewer vs author share by age |
| PUB-08 | Viglione 2020, Nature news, pandemic publishing | arXiv +2.7% women vs +6.4% men | OA | DOI 10.1038/d41586-020-01294-9 | Nature news is free | Preprint growth bars |
| PUB-09 | Andersen et al. 2020, eLife, COVID first authors | 23% lower in Mar–Apr 2020 | OA | https://elifesciences.org/articles/58807 | eLife PDF + source data | Expected vs observed by month |
| PUB-10 | Myers et al. 2020, Nature Human Behaviour, pandemic effects | Child <5: −17% research time | PW | DOI 10.1038/s41562-020-0921-y | Unpaywall; SSRN/HBS working paper version | Research time by field and childcare |
| PUB-11 | Vincent-Lamarre, Sugimoto & Larivière 2020, Nature Index blog | Women's first-author share fell | WEB | https://www.natureindex.com/news-blog/decline-women-scientist-research-publishing-production-coronavirus-pandemic | Save page (numbers unverified) | 2019 vs 2020 share |

## 05 Citations, recognition and visibility

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| CIT-01 | Dworkin et al. 2020, Nature Neuroscience, neuro reference lists | WW −13.9%, MM +5.2% | OA preprint | DOI 10.1038/s41593-020-0658-y ; bioRxiv: https://www.biorxiv.org/content/10.1101/2020.01.03.894378v2.full.pdf ; arXiv 2001.01002 | bioRxiv PDF; code/data on GitHub (see paper) | Over/under-citation by citing-team gender; time trend |
| CIT-02 | Chatterjee & Werner 2021, JAMA Netw Open | Median 36 vs 54 citations | OA | DOI 10.1001/jamanetworkopen.2021.14509 ; PMC8254129 | PMC OA service | Median citations by author pair |
| CIT-03 | Caplar, Tacchella & Birrer 2017, Nature Astronomy | Women-led −10.4% citations | OA preprint | https://ui.adsabs.harvard.edu/abs/2017NatAs...1E.141C/abstract ; DOI 10.1038/s41550-017-0141 *(unverified)* | arXiv link from the ADS page | Citation residuals |
| CIT-04 | King et al. 2017, Socius, self-citation | Men self-cite 56% more | OA | DOI 10.1177/2378023117738903 ; arXiv 1607.00376 | Socius is OA | Self-citation ratio over time |
| CIT-05 | Lincoln et al. 2012, Soc Stud Sci, Matilda effect | Women ~10% of research awards | PW | DOI 10.1177/0306312711435830 | Unpaywall | Research vs service awards |
| CIT-06 | Ma, Oliveira, Woodruff & Uzzi 2019, Nature (Comment), prizes | 64 cents per prize dollar | OA PDF | https://media.nature.com/original/magazine-assets/d41586-019-00091-3/d41586-019-00091-3.pdf | Direct PDF | Money ratio and share by decade |
| CIT-07 | Meho 2021, Quantitative Science Studies, top awards | ~11.5% women; 6%→19% | OA | DOI 10.1162/qss_a_00148 ; https://doaj.org/article/bf4b2a626a78490eb4d41223d91abab6 | QSS is OA | Women's share in 5-year bins |
| CIT-08 | Nittrouer et al. 2018, PNAS, colloquium speakers | Men 69% of talks | OA | DOI 10.1073/pnas.1708414115 | PNAS/PMC | Speaker share by host gender |
| CIT-09 | Carter et al. 2018, PLoS ONE, seminar questions | Women 2.5× less likely to ask | OA | DOI 10.1371/journal.pone.0202743 | PLoS PDF + data | Question share vs audience share |
| CIT-10 | Davidson & Greene 2024, eLife, science journalism | Women's quote share ~13%→~31% | OA | https://elifesciences.org/articles/84855 | eLife PDF; code/data on GitHub (see paper) | Quote share over time |
| CIT-11 | Tripodi 2021, New Media & Society, Wikipedia notability | 19% of bios vs 25% of deletion noms | PW | press: https://www.marketplace.org/shows/marketplace-tech/why-its-so-hard-for-biographies-about-women-to-stay-on-wikipedia | Find DOI via journal search "Ms. Categorized Tripodi"; Unpaywall | Bio share vs deletion share |
| CIT-12 | Alvarez-Ponce & Iyengar 2026, Proc R Soc B (art. 20252566), Wikipedia biology faculty | 9.4% vs 7.5% have a page | PW | press: https://theprint.in/feature/wikipedia-gender-gap-women-scientists-study/2945729/ | Search royalsocietypublishing.org for article 20252566 | Pages by gender over time |

## 06 Pay, promotion and attrition

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| PAY-01 | AAUP 2025–26 Annual Report on the Economic Status of the Profession | Women earn 83.6% of men's average | OA + DATA | https://www.aaup.org/reports-publications/aaup-policies-reports/topical-reports/annual-report-economic-status-profession-25-26 | Report PDF + survey tables (Excel) linked on page | Women's salary as % of men's by rank |
| PAY-02 | UCEA, Intersectional Pay Gaps in Higher Education 2023–24 | UK HE median gap 11.5% | WEB / PDF | https://www.ucea.ac.uk/our-work/employee-experience/intersectional-pay-gaps-in-higher-education/ | Download report PDF from page | HE vs national gap |
| PAY-03 | CNRS MPDF, Analyse des rémunérations 2023 | Women −13.9% (−€557/month) | OA PDF | https://mpdf.cnrs.fr/wp-content/uploads/2023/12/MPDF-analyse-remunerations-synthese-2023.pdf | Direct PDF | Gap by staff category; primes by gender |
| PAY-04 | Cech & Blair-Loy 2019, PNAS, new parents in STEM | 43% mothers vs 23% fathers leave | OA | https://pmc.ncbi.nlm.nih.gov/articles/PMC6410805 | PMC OA service | Figs 1–2 employment trajectories |
| PAY-05 | Morgan et al. 2021, Science Advances, parenthood in academia | Mothers' output −20% after a child | OA | DOI 10.1126/sciadv.abd1996 ; PMC7904257 ; press: https://www.colorado.edu/today/2021/02/25/why-do-men-publish-more-papers-women-motherhood-plays-key-role | Sci Adv OA / PMC | Productivity aligned to birth |
| PAY-06 | Kim & Moser 2021/2025, NBER w29436 / Econometrica | Tenure: mothers 27% vs fathers 48% | OA | https://www.nber.org/system/files/working_papers/w29436/w29436.pdf | Direct PDF | Productivity over age by parent status |
| PAY-07 | Sege, Nykiel-Bub & Selk 2015, JAMA, start-up packages | $889k vs $350k median | PW | https://jamanetwork.com/journals/jama/fullarticle/2441254 | JAMA research letter, often free; Unpaywall | Paired bars |
| PAY-08 | Ceci, Ginther, Kahn & Williams 2014, Psych Sci Public Interest | Counterpoint: parity once hired in math-intensive fields | OA | https://inclusionandbelongingtaskforce.harvard.edu/publications/women-academic-science-changing-landscape | PSPI is usually free (SAGE); Unpaywall via DOI (search "Women in Academic Science: A Changing Landscape") | Leak by field and stage |
| PAY-09 | Derrick et al. 2022, eLife, parenthood and gender gaps (not checked) | — | OA | https://elifesciences.org/articles/78909 | eLife PDF | Check for a usable figure |

## 07 Teaching evaluations and service load

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| TEACH-01 | MacNell, Driscoll & Hunt 2015, Innovative Higher Education | 4.35 vs 3.55 promptness | PW | press: https://news.ncsu.edu/2014/12/macnell-gender-2014 | Find DOI on the press page; Unpaywall | 2×2 perceived vs actual gender |
| TEACH-02 | Boring 2017, J Public Economics, Sciences Po | Male students ~30% more likely to rate men "excellent" | OA copy | DOI 10.1016/j.jpubeco.2016.11.006 ; copy: https://www.unlv.edu/sites/default/files/page_files/27/Engineering-GenderBiases-AnneBoring.pdf | Direct PDF (copy) | Satisfaction vs exam grades |
| TEACH-03 | Mengel, Sauermann & Zölitz 2019, JEEA | Women rated lower, esp. junior | OA copy | DOI 10.1093/jeea/jvx057 ; https://repository.essex.ac.uk/20359/ | Repository PDF; IZA discussion paper version | Gap by seniority and student gender |
| TEACH-04 | Guarino & Borden 2017, Res High Educ, service loads | +0.6 h/week service | PW | DOI 10.1007/s11162-017-9454-2 ; press: https://www.sciencedaily.com/releases/2017/04/170412144832.htm | Unpaywall | Service by gender and rank |
| TEACH-05 | Babcock, Recalde, Vesterlund & Weingart 2017, AER | Women accept 76% vs men 51% of requests | PW | DOI 10.1257/aer.20141734 ; https://econpapers.repec.org/RePEc:aea:aecrev:v:107:y:2017:i:3:p:714-47 | Unpaywall; NBER/authors' working paper version | Volunteering mixed vs single-gender |
| TEACH-06 | Misra et al. 2011, Academe (AAUP), ivory ceiling of service | 25% vs 37% time on research | OA | summary: https://www.federationhss.ca/en/blog/status-women-gender-and-ivory-ceiling-service-work-academy ; https://www.insidehighered.com/node/76466 | Search aaup.org for "The Ivory Ceiling of Service Work" | Stacked time-use bars |

## 08 Neuroscience

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| NEURO-01 | Nature Neuroscience editorial 2020, "Widening the scope of diversity" | Authorship ratio flat for 20 years | OA | https://www.nature.com/articles/s41593-020-0670-2 | Direct | Quote |
| NEURO-02 | Churchland & Davatolhagh 2024, The Transmitter | Women first/last 36%→50%; gap widens 0.41 pt/yr | WEB | https://www.thetransmitter.org/publishing/women-are-systematically-under-cited-in-neuroscience-new-tools-can-change-that/ | Save page | Authorship share vs citation gap |
| NEURO-03 | Fulvio, Akinnola & Postle 2021, J Cogn Neurosci | Women-led papers under-cited (GCBI) | OA preprint | DOI 10.1162/jocn_a_01643 ; https://www.biorxiv.org/content/10.1101/2020.08.19.257402.full.pdf | bioRxiv PDF | GCBI by category over years |
| NEURO-04 | Bertolero et al. 2020, bioRxiv, race and citation | White-led papers over-cited | OA | https://biorxiv.org/content/10.1101/2020.10.12.336230v1 | bioRxiv PDF | Race × gender citation |
| NEURO-05 | Llorens et al. 2021, Neuron, a lifetime problem | 57% of PhD applicants vs 30% of faculty | OA copy | DOI 10.1016/j.neuron.2021.06.002 ; https://www.cns.nyu.edu/wanglab/publications/pdf/llorens.neuron2021.pdf | Direct PDF | Fig. 1 timeline of biases; Table 2 solutions |
| NEURO-06 | Schrouff et al. 2019, Eur J Neurosci | Under-representation across 295 conferences | OA preprint | DOI 10.1111/ejn.14397 ; https://discovery.ucl.ac.uk/id/eprint/10071146/ ; preprint https://iris.unitn.it/retrieve/e3835195-58e6-72ef-e053-3705fe0ad821/Schrouff%26al_2019_Pre-rev_version.pdf | Repository PDF | Figs 1–2 % women by venue |
| NEURO-07 | SfN NDP survey 2016, executive summary | Women 30% of tenure-stream faculty | OA PDF | https://www.sfn.org/-/media/SfN/Documents/Survey-Reports/Final-SfN_2016-NDP-Survey-Executive-Summary.pdf | Direct PDF | Pipeline bars |
| NEURO-08 | SfN 2018, Supporting female neuroscientists | 58% of PhD enrollees | WEB | https://sfn.org/publications/neuroscience-quarterly/spring-2018/women-in-neuroscience | Save page | 2010 vs 2016 pipeline |
| NEURO-09 | Machlovi et al. 2021, J Neurosci Res | 13.8% of tenured full profs; 18.1% last authors | OA | https://rcastoragev2.blob.core.windows.net/904567a72136304394b5d2782423da04/PMC7754118.pdf ; PubMed 32267025 | Direct PDF / PMC OA service | First vs last author share |
| NEURO-10 | Else 2019, Nature news, making meetings more equal | Speakers 24%→42% women | OA PDF | https://media.nature.com/original/magazine-assets/d41586-019-02658-6/d41586-019-02658-6.pdf | Direct PDF | Speaker share over time |
| NEURO-11 | Hoy, Fitzgibbon & Brem 2022, eLife | 2/39 and 0/10 women speakers | OA | https://elifesciences.org/articles/75818 | eLife PDF | Before/after counts |
| NEURO-12 | Frye 2019, Cosyne 2019 acceptance analysis | 31.4% vs 37.7% acceptance | WEB | https://charlesfrye.github.io/stats/2019/03/06/cosyne19-gender-bias.html | Save page; data may be linked in the post | Two-bar acceptance chart |
| NEURO-13 | Simons Foundation SCGB 2020, Cosyne bias | Double-blind did not close gender gap | WEB | https://www.simonsfoundation.org/2020/08/28/addressing-gender-and-institutional-bias-at-cosyne/ | Save page + any linked report | Score gap single vs double blind |
| NEURO-14 | UChicago Neuroscience Institute 2020, Bias in neuroscience | 50% podium talks guaranteed | WEB | https://neuroscience.uchicago.edu/biasinneuroscience | Save page | Policy → outcome |
| NEURO-15 | BiasWatchNeuro | Speaker ratios at neuro conferences | WEB | https://biaswatchneuro.com | Scrape conference posts (speaker counts, base rate) into a CSV | Speaker share by conference |
| NEURO-16 | anneslist | Directory of women systems neuroscientists | WEB | https://anneslist.net | Screenshot only (no statistics) | Visibility-tool example |

## 09 Interventions with evidence

| ID | Source | Key number | Access | Primary link | How to get it | Extract |
|---|---|---|---|---|---|---|
| INT-01 | Goldin & Rouse 2000, AER, blind auditions | +11 pts preliminaries | OA copy | https://dash.harvard.edu/bitstream/handle/1/30703974/aer.90.4.715.pdf?sequence=1 | Direct PDF | Women's share of new hires over time; Tables 4–6 |
| INT-02 | Pallesen 2019 critique (blog) | p 0.042 → ~0.33 after correction | WEB | https://gwern.net/doc/www/jsmp.medium.com/0b9410ad1a51bf0a5a52c96c3177223217b013af.html | Save page | Original vs corrected p-values |
| INT-03 | Gelman via Reason 2019 | Evidence "not very impressive" | WEB | https://reason.com/2019/10/22/orchestra-study-blind-auditions-gelman/ | Save page | Quote |
| INT-04 | Tomkins, Zhang & Heavlin 2017, PNAS, single vs double blind | Famous author OR 1.63; female OR 0.78 | OA | https://arxiv.org/pdf/1702.00502 | arXiv PDF | Forest plot of odds ratios |
| INT-05 | PeerJ 2019 follow-up on double-blind review (Behavioral Ecology) | No gain in female first authors | OA | https://peerj.com/articles/6702 | PeerJ PDF + data | Female first authorship by review type |
| INT-06 | Bagues, Sylos-Labini & Zinovyeva 2017, AER, committee composition | No benefit of more women evaluators | PW | press: https://www.aalto.fi/en/news/women-in-tenure-committees-do-not-speed-up-womens-science-careers | Search AER 107:1207; Unpaywall; working-paper version (IZA/SSRN) | Success vs # women on committee |
| INT-07 | Antecol, Bedard & Stearns 2018, AER, tenure clock stopping | Men +17 pts, women −19 pts | PW | https://www.aeaweb.org/doi/10.1257/aer.20160613 | Unpaywall; IZA working paper version | Effect by gender |
| INT-08 | Carnes et al. 2015, Academic Medicine, habit-breaking RCT | Awareness up at 3 months | OA copy | https://advance.washington.edu/liy/sites/default/files/Carnesetal_2015_0.pdf | Direct PDF | Pre/post, treated vs control |
| INT-09 | Devine et al. 2017, J Exp Soc Psych, hiring follow-up | 32%→47% women hires (treated) | OA copy | https://core.ac.uk/download/225400929.pdf | Direct PDF | Before/after hiring bars |
| INT-10 | Xiao et al. 2020, BMJ Open, Athena SWAN | UK women profs 24.2%→26.8% | OA | https://hub.hku.hk/bitstream/10722/290849/1/content.pdf ; https://bmjopen.bmj.com/content/10/2/e032915 | Direct PDF | Share by award level over time |
| INT-11 | Ovseiko et al. 2017, Health Res Policy Syst, Athena SWAN at Oxford | Qualitative | OA | https://www.rdm.ox.ac.uk/people/pavel-ovseiko/publication_modal/681749 | Follow to BMC (OA) | Quote |
| INT-12 | ERC eligibility window extension | 18 months per child | WEB | https://erc.europa.eu/node/1965 | Save page | Policy box |

Régner 2019 (HIRE-04) and Tricco 2017 (FUND-13) also belong here; they are not duplicated.

## 10 Datasets and tools for redrawing plots

| ID | Dataset / tool | Maintainer | Link | How to download | What to plot |
|---|---|---|---|---|---|
| DATA-01 | MESR tenured teaching staff open data | MESR-SIES (France) | https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-enseignants-titulaires-esr-public | Opendatasoft API, full CSV: `https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public/exports/csv` (or the "Export" tab) | MCF → PR scissor curve by sex × CNU section × year (filter to neuro-relevant sections, e.g. 69, 44, 27, 16) |
| DATA-02 | MESR parity study of enseignants-chercheurs | MESR | https://www.enseignementsup-recherche.gouv.fr/fr/analyse-quantitative-de-la-parite-entre-les-femmes-et-les-hommes-parmi-les-enseignants-chercheurs-82324 | Save page + linked PDF | Reference values (2014: 43% MCF, 24% PR) |
| DATA-03 | She Figures 2024 data | European Commission | see PIPE-01 | Data tables from the report / EC data portal | EU and country pipelines |
| DATA-04 | UNESCO UIS data browser | UNESCO | https://databrowser.uis.unesco.org | Use the browser export (CSV) or the UIS bulk data download service / API; indicator "female researchers as % of total" | Country shares over time |
| DATA-05 | Holman gender-gap app and data | Luke Holman | https://lukeholman.github.io/genderGap/ | Data/code links from the app or the PLoS Biol paper's data statement (GitHub/OSF) | % women authors by field and position; years to parity |
| DATA-06 | Nature Index author gender ratio | Springer Nature | https://www.nature.com/nature-index/author-gender-ratio/author-position-by-topic ; https://www.nature.com/nature-index/author-gender-ratio/subjects-and-topics | Dynamic page: use a headless browser to capture values for neuroscience, or screenshot | Female authorship by topic and position |
| DATA-07 | cleanBib | Zhou, Bertolero, Bassett et al. | https://github.com/dalejn/cleanBib | `git clone https://github.com/dalejn/cleanBib` ; run on the user's own .bib | Gender balance of own reference lists vs benchmarks |
| DATA-08 | GCBI-alyzer | Fulvio & Postle | https://psych.wisc.edu/gcbialyzer/ | Web tool; record base rates from the page | Citation balance vs JoCN base rates |
| DATA-09 | NIH RePORT funding-rate report (Jul 2024) | NIH OER | https://report.nih.gov/reportweb/web/displayreport?rId=1021 | Excel export on the report page | FY2023 applicants and funding rate by gender |
| DATA-10 | ERC dashboard | ERC | https://erc.europa.eu/node/21010 | Dashboard export; gender values come from ERC statistics PDFs (FUND-14 to FUND-18) | Projects by panel (LS5), country, year |
| DATA-11 | ERC gender actions and data (slides) | ERC Scientific Council | https://erc.europa.eu/sites/default/files/document/file/ERC_gender_actions_and_data.pdf | Direct PDF; digitise charts if needed | Success and applicant shares by gender |
| DATA-12 | HESA staff open data | HESA (UK) | https://www.hesa.ac.uk/node/136617 | CSV links on the page (CC-BY) | Staff by sex and grade |
| DATA-13 | Advance HE staff statistical report 2024 | Advance HE | https://advance-he.ac.uk/news-and-views/equality-higher-education-staff-statistical-report-2024 | Report PDF + data tables | Women 30.8% of UK professors |
| DATA-14 | OpenAlex | OurResearch | https://api.openalex.org | Free API; join author names to a gender-inference tool (e.g. genderize.io) to rebuild authorship or citation shares for neuroscience journals | Custom authorship/citation trends (see Rusti et al. 2026, https://arxiv.org/abs/2606.26469) |

---

## Known gaps

- No FENS gender statistics and no Cosyne 2021–2023 gender analyses were found online.
- Inserm's grade-level (CR/DR) shares are in its Rapport social unique, which was not located.
- RIPEC bonuses have not yet been analysed by gender in CNRS reports.
