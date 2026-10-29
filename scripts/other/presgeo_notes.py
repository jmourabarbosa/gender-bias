"""Write notes.md and _status/<ID>.json for PRES-01..11 and GEO-01..11.
Run: python3 -I scripts/other/presgeo_notes.py
File lists are taken from each folder; figure list = figures/<ID>_*.{png,jpg}."""
import json, glob, os
ROOT = "/home/user/gender-bias"
B = f"{ROOT}/other-biases-data"
DATE = "2026-10-29"

S = {}
def add(i, **kw): S[i] = kw

add("PRES-01", sec="05-prestige", title="Nobel and novice: Author prominence affects peer review",
    cit="Huber J, Inoua S, Kerschbamer R, König-Kersting C, Palan S, Smith VL (2022). PNAS 119(41):e2205779119. DOI 10.1073/pnas.2205779119 (PMC9564227, CC BY)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC9564227 (PMC OA bucket, first pass)", access="downloaded",
    figs={"PRES-01_fig1.jpg": "Fig. 1 'Recommendation percentages by condition' (PMC JPG; PDF p.3)",
          "PRES-01_redraw.png": "greyscale redraw of Fig. 1 from its data labels (data/PRES-01.csv)"},
    head="Abstract (PDF p.1): 'only 23% recommended reject when the prominent researcher was the only author shown, 48% ... anonymized, and 65% ... little-known author'. Fig. 1 labels: reject 22.5% (AH) / 48.2% (AA) / 65.4% (AL).",
    check="MATCHES (23% vs 65%)", extra=["page.html is the PMC landing page (genuine, not a challenge)."])

add("PRES-02", sec="05-prestige", title="Reviewer bias in single- versus double-blind peer review",
    cit="Tomkins A, Zhang M, Heavlin WD (2017). PNAS 114(48):12708-12713. DOI 10.1073/pnas.1707323114; source.pdf = arXiv:1702.00502v6",
    url="https://arxiv.org/pdf/1702.00502", access="downloaded",
    figs={"PRES-02_fig1.png": "Table 5 'Learned coefficients and significance for review score prediction' (PDF p.7), copied from gender-bias-data INT-04_table5.png",
          "PRES-02_redraw.png": "forest plot of Table 5 odds multipliers with 95% CI (copied from INT-04_redraw.png; data/PRES-02.csv)"},
    head="Table 5 (PDF p.7) / abstract: single-blind reviewers' odds multiplier 1.63 for famous authors, 1.58 top universities, 2.10 top companies.",
    check="MATCHES (OR 1.63)", extra=["Same document as gender-bias-data/09-interventions/INT-04 (identical source.pdf); figures and CSV copied, not re-downloaded."])

add("PRES-03", sec="05-prestige", title="The Matthew Effect in Science",
    cit="Merton RK (1968). Science 159(3810):56-63. DOI 10.1126/science.159.3810.56 (PMID 5634379)",
    url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=5634379 (record only)", access="paywalled",
    figs={}, head="No full text obtained. PubMed record has no abstract (1968).",
    check="Concept only - nothing to check (no number).",
    extra=["Unpaywall: is_oa=false. Tried Eugene Garfield's mirror (garfield.library.upenn.edu/merton/matthew1.pdf): host no longer resolves. pubmed.ncbi.nlm.nih.gov landing page returned 403 to plain HTTP, so the E-utilities XML record is saved instead (pubmed_record.xml).",
           "Web search found no other clearly legal OA copy (a Stony Brook repository record appears to be course material, access-restricted). Needs institutional access (JSTOR / Science archive).",
           "Quote for the slide: the paper's epigraph is Matthew 25:29 (KJV), 'For unto every one that hath shall be given, and he shall have abundance: but from him that hath not shall be taken away even that which he hath.' Merton's own wording should be taken from the PDF once obtained."])

add("PRES-04", sec="05-prestige", title="The Matthew effect in science funding",
    cit="Bol T, de Vaan M, van de Rijt A (2018). PNAS 115(19):4887-4890. DOI 10.1073/pnas.1719557115 (PMC5948972); source.pdf = SocArXiv preprint 10.31235/osf.io/nur8p (accepted version per Unpaywall)",
    url="https://osf.io/nur8p/download", access="downloaded",
    figs={"PRES-04_fig1.png": "Fig. 1 effect of an early-career grant on winning / applying for a mid-career grant (preprint PDF p.4)",
          "PRES-04_fig3.png": "Fig. 3 'Accumulation of grant money by early-career grant applicants' = funding over time (preprint PDF p.6)"},
    head="Preprint p.2 (abstract) and p.6: 'winners just above the funding threshold accumulating more than twice as much research funding (EUR 180,000) during the following eight years as non-winners just below it'; gap EUR 40,000 after 4 years.",
    check="MATCHES (>2x later funding)",
    extra=["PMC5948972 is not in the PMC OA bucket; pnas.org and Europe PMC render returned 403 / challenge pages, so the SocArXiv preprint is used. Figure numbering in the preprint: Fig. 1 = mid-career grant RD plot, Fig. 3 = cumulative funding over time (the 'funding over time' item). Check numbering against the PNAS version if the published figure is needed.",
           "page.html = UvA-DARE record page (genuine). No redraw: Fig. 3 lines are not tabulated in the paper."])

add("PRES-05", sec="05-prestige", title="Systematic inequality and hierarchy in faculty hiring networks",
    cit="Clauset A, Arbesman S, Larremore DB (2015). Science Advances 1(1):e1400005. DOI 10.1126/sciadv.1400005 (PMC4644075)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC4644075 (PMC OA bucket, first pass)", access="downloaded",
    figs={"PRES-05_fig1.jpg": "Fig. 1 prestige hierarchy network, computer science (PMC JPG; PDF p.2)",
          "PRES-05_fig2.jpg": "Fig. 2 inequality in faculty production, (A) Lorenz curves (PMC JPG; PDF p.2)",
          "PRES-05_redraw.png": "Lorenz curves recomputed from the paper's Datasets 1-6 (data/PRES-05_lorenz.csv, data/PRES-05_top25_share.csv)"},
    head="PDF p.2: 'only 25% of institutions producing 71 to 86% of all tenure-track faculty'. Recomputed from Datasets 1-6 (in-sample PhD origins only, 'All others' vertex excluded): top 25% of institutions produce 71.2% (business), 78.3% (computer science), 85.7% (history).",
    check="MATCHES (71-86%; recomputation reproduces 71.2-85.7%)",
    extra=["supplementary/datasets/ = unzipped 1400005_Datasets.zip (edge lists u=PhD institution, v=hiring institution; vertex lists with prestige pi).",
           "The redraw counts, for each in-sample institution, the faculty (edges) it produced; top 25% = round(0.25 x n institutions)."])

add("PRES-06", sec="05-prestige", title="Quantifying hierarchy and dynamics in US faculty hiring and retention",
    cit="Wapman KH, Zhang S, Clauset A, Larremore DB (2022). Nature 610:120-127. DOI 10.1038/s41586-022-05222-x (PMC9534765, CC BY)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC9534765 (PMC OA bucket, first pass)", access="downloaded",
    figs={"PRES-06_fig2.jpg": "Fig. 2 'Universal inequality in the production of US-trained faculty' (a: production by university; b: Lorenz curves by field/domain) (PMC JPG; PDF p.3)",
          "PRES-06_redraw.png": "Lorenz curve redrawn from Fig. 2 source data MOESM4 (academia from panel a, 8 domains from panel b umbrella curves; data/PRES-06_lorenz.csv)"},
    head="PDF p.2: 'Overall, 80% of all domestically trained faculty in our data were trained at just 20.4% of universities'; domains: 80% from 19-28%. Recomputed from MOESM4 panel a: 80% reached at 20.4% of universities.",
    check="MATCHES (80% from 20%)",
    extra=["The listing says 'Fig. 1 Lorenz curve' but in the paper the Lorenz curves are Fig. 2 (Fig. 1 = composition/dynamics of the professoriate). Minor figure-number MISMATCH in the source list, number itself matches.",
           "Same document as gender-bias-data/01-pipeline/PIPE-16 (identical source.pdf). Deleted page.html: it was a reCAPTCHA 'Checking your browser' page."])

add("PRES-07", sec="05-prestige", title="La position scientifique de la France dans le monde et en Europe 2005-2018 (Hcéres-OST, édition 2021)",
    cit="Hcéres - Observatoire des sciences et techniques (2021). La position scientifique de la France dans le monde et en Europe, 2005-2018. Paris: Hcéres, ISBN 978-2-492781-00-1",
    url="https://www.hceres.fr/sites/default/files/media/downloads/hceres_ost_positionnement_scientifique_france_edition_2021.pdf (failed); secondary: https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2023-11/-le-de-france-pdf-30114.pdf",
    access="failed",
    figs={"PRES-07_redraw.png": "Île-de-France vs rest of France share of French publications, 2019 (data/PRES-07.csv, from the secondary MESR document)"},
    head="Secondary source secondary_mesr_strater_idf.pdf (MESR diagnostic territorial Île-de-France, Nov 2023), PDF p.3: 'Les publications scientifiques régionales représentent 34,5 % de la production nationale (1er rang) en 2019' (OST data). Same page also says 3.6% of European output in the text but 16.1% of European publications in the key-figures box (internal inconsistency, not used).",
    check="MATCHES via secondary source (34.5%, year 2019); primary Hcéres report not verified",
    extra=["hceres.fr returned HTTP 503 'Hcéres - En maintenance' (site maintenance page, not saved) on every try; Wayback Machine API returned 429 Too Many Requests; HAL search found no deposit. Retry the primary PDF later (direct download, no bot protection) for the regional table/map and the France world-share series.",
           "Regional table for the other regions is not in the secondary document, so the CSV only has Île-de-France vs rest."])

add("PRES-08", sec="05-prestige", title="Les dépenses de R&D des entreprises en 2024 (données provisoires)",
    cit="Chanteloup G (2026). MESRE-SIES Note Flash n°06, avril 2026. DOI 10.5281/zenodo.19251000",
    url="https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-04/nf-sies-2026-06-39988.pdf", access="downloaded",
    figs={"PRES-08_fig1.png": "Carte 1 'Dépenses intérieures de R&D des entreprises par région en 2024 (p) en Md€' (PDF p.2)",
          "PRES-08_redraw.png": "bar chart of the 13 metropolitan regions transcribed from Carte 1 (data/PRES-08.csv)"},
    head="PDF p.2: 'En Île-de-France, les entreprises réalisent 17,5 Md€ de dépenses intérieures de R&D en 2024, soit 42 % de la DIRDE totale et emploient 39 % des effectifs de R&D'. Map values sum to 41.87 bn (metropolitan) vs 41.9 bn total; IdF 17.52/41.87 = 41.8%.",
    check="MATCHES (~42%)", extra=["Rest of France = 24.35 bn (58%); top 3 regions (IdF, AURA, Occitanie) = 68%."])

add("PRES-09", sec="05-prestige", title="Résultats de l'appel ERC Starting Grants 2024",
    cit="Horizon Europe France (MESR portal), 'Résultats de l'appel ERC Starting Grants 2024', horizon-europe.gouv.fr (Sept 2024)",
    url="https://www.horizon-europe.gouv.fr/resultats-de-l-appel-erc-starting-grants-2024-37575", access="downloaded",
    figs={"PRES-09_redraw.png": "ERC StG 2024 France winners by host institution (data/PRES-09_erc_stg2024_france_hosts.csv)"},
    head="page.html: '49 lauréats (soit 9,9% des projets financés), la France se classe 4e'; 'la principale institution d'accueil ... est le CNRS (25). Viennent ensuite l'INRIA (3), l'Inserm (2) et l'Ecole Polytechnique (2). Les 17 autres établissements hébergeant chacun un projet'. 253 French proposals, success rate 19.4% (EU 14.2%).",
    check="MATCHES (49 winners, 25 at CNRS)",
    extra=["CSV: 21 host institutions summing to 49 (the 17 single-project hosts are named on the page: 8 universities SU, UHA, UVSQ, Paris-Saclay, Bordeaux, Lorraine, Lyon 1, Rennes; FNSP, JJ Laffont-TSE, Armines; ENS, ENSAI; Institut Pasteur, ICM; Observatoire de la Côte d'Azur; CEA). Full names expanded from the page's abbreviations.",
           "The page says 'mardi 5 septembre 2024' (5 Sept 2024 was a Thursday; ERC announced on 5 Sept 2024).",
           "The page's 'captcha' string is from an embedded form widget; the page content is genuine."])

add("PRES-10", sec="05-prestige", title="Idex : des milliards qui coûtent cher (bilan des initiatives d'excellence, saison 1)",
    cit="L'Etudiant / EducPros (2014), 'Idex : des milliards qui coûtent cher' (enquête, Idex saison 1)",
    url="https://www.letudiant.fr/educpros/enquetes/idex-le-bilan-des-initiatives-d-excellence-saison-1-pour-les-universites.html", access="downloaded",
    figs={"PRES-10_redraw.png": "Île-de-France vs rest among the 8 first-wave Idex (data/PRES-10.csv)"},
    head="page.html: 'Les huit regroupements qui ont obtenu des Idex au premier tour - Bordeaux, Strasbourg, PSL, Sorbonne Universités, Sorbonne Paris Cité, Saclay, Aix-Marseille et Toulouse'; 4 of 8 (PSL, SU, SPC, Saclay) in Île-de-France.",
    check="MATCHES (4 of first 8 Idex in Île-de-France)",
    extra=["Page title differs from the URL slug but canonical URL is the listed one. No map in the article; the redraw replaces the 'Idex map' item. Consider an official ANR/SGPI Idex list for the slide."])

add("PRES-11", sec="05-prestige", title="ANR: Atlas régional des projets 2014-2020 + Synthèse du suivi France 2030, région Île-de-France 2011-2022",
    cit="Agence nationale de la recherche (2021) Atlas régional des projets financés par l'ANR 2014-2020 (web/Tableau); ANR (Oct 2023) Synthèse du suivi 2011-2022 du Plan France 2030 - Région Île-de-France",
    url="https://anr.fr/fileadmin/documents/2023/ANR-FRANCE2030-Synthese-regionale-2022-IDF-oct2023.pdf ; https://anr.fr/fr/projets-finances-et-impact/donnees-analyses-et-etudes/atlas-des-projets-anr-2014-2020/",
    access="downloaded",
    figs={"PRES-11_fig1.png": "map of the 401 France 2030/PIA projects in Île-de-France by département (PDF p.2)",
          "PRES-11_fig2.png": "projects and amounts by theme, donut chart (PDF p.2)"},
    head="source.pdf p.1: Île-de-France: 401 France 2030/PIA projects, 4,835 M€ of funding 2011-2022 (3,393.7 M€ disbursed, 70.2%). No national total or regional share is given in this document.",
    check="Key number 'Not verified' - still not verified: no IdF share of ANR funding found",
    extra=["The atlas page holds only an embedded Tableau Public viz (no PDF/Excel link in the HTML) plus a methodology PDF; the 'PDF détaillées par région' link goes to a generic listing. ANR open data on data.gouv.fr could give the regional share but data.gouv.fr connections were reset by the network during this session; retry later (dataset 'ANR - projets financés', partner region field)."])

add("GEO-01", sec="06-geography", title="Leading countries in global science increasingly receive more citations than other countries doing similar research",
    cit="Gomez CJ, Herman AC, Parigi P (2022). Nature Human Behaviour 6(7):919-929. DOI 10.1038/s41562-022-01351-5 (PMC9314251)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC9314251 (PMC OA bucket, first pass)", access="downloaded",
    figs={"GEO-01_fig6.jpg": "Fig. 6 'Comparing citational distortion between core and periphery countries' (PMC JPG; PDF p.7)",
          "GEO-01_fig8.jpg": "Fig. 8 'Citational distortion within transnational regions in 2012' (country maps; PMC JPG)"},
    head="PDF p.3: 'the gap between core and periphery countries is growing substantially over time, as core countries are increasingly overcited ... while peripheral countries are increasingly undercited' (Fig. 3b).",
    check="MATCHES (periphery under-cited, gap growing)",
    extra=["The paper has no single country-pair citation map; Fig. 3b (core vs periphery trend) is in 41562_2022_1351_Fig3_HTML.jpg and Fig. 8 gives per-country maps. page.html (RePEc) and page1.html (nature.com) are genuine pages."])

add("GEO-02", sec="06-geography", title="Non-White scientists appear on fewer editorial boards, spend more time under review, and receive fewer citations",
    cit="Liu F, Rahwan T, AlShebli B (2023). PNAS 120(13):e2215324120. DOI 10.1073/pnas.2215324120 (PMC10068789, CC BY-NC-ND)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC10068789", access="downloaded",
    figs={"GEO-02_fig1.jpg": "Fig. 1 'Representation of countries among editors' (editor-to-author ratio map + bars; PMC JPG; PDF p.3)"},
    head="Abstract (PDF p.1): 'most countries in Asia, Africa, and South America ... have fewer editors than would be expected based on their share of authorship'. Fig. 1B: France has an editorship/authorship ratio just below 1.",
    check="MATCHES",
    extra=["DOI found from the Physics World article (page.html, genuine) via Unpaywall/PMC idconv. The 'editor vs author share scatter' is shown in the paper as a ratio map + bar chart (Fig. 1), not a scatter."])

add("GEO-03", sec="06-geography", title="Explicit Bias Toward High-Income-Country Research: A Randomized, Blinded, Crossover Experiment Of English Clinicians",
    cit="Harris M, Marti J, Watt H, Bhatti Y, Macinko J, Darzi AW (2017). Health Affairs 36(11):1997-2004. DOI 10.1377/hlthaff.2017.0773; source.pdf = author accepted manuscript from Imperial Spiral (hdl 10044/1/54102)",
    url="https://spiral.imperial.ac.uk/server/api/core/bitstreams/74c1c6fe-82f7-451b-b6eb-a776ec80d106/content", access="downloaded",
    figs={"GEO-03_fig1.png": "Table 2 'Ratings, according to stated source, by research abstract (n=347)', abstracts 1-3 (manuscript PDF p.36)",
          "GEO-03_fig2.png": "Table 2 continued: abstract 4 + combined results (PDF p.37)",
          "GEO-03_redraw.png": "paired mean ratings LIC vs HIC source, combined across abstracts (data/GEO-03.csv = full Table 2)"},
    head="PDF p.18: 'The change in rating was up to 25% of the mean score for the abstract, in some instances.' Abstract (p.3): HIC source raised relevance by 4.50 (3.16-5.83) and recommendation to a peer by 3.05 (1.77-4.33) points on 0-100; strength n.s. (1.35, p=0.053).",
    check="MATCHES (up to 25%; note it is relevance more than recommendation: largest gaps 8.09/34.4 = 23.5% relevance, 5.50/33.6 = 16.4% recommendation, abstract 3)",
    extra=["Health Affairs version is paywalled (Unpaywall is_oa=false); the Spiral copy is the accepted manuscript (watermarked 'For Review Only'), page numbers refer to that PDF. The publisher's figures/Exhibit numbering may differ."])

add("GEO-04", sec="06-geography", title="Measuring the bias against low-income country research: an Implicit Association Test",
    cit="Harris M, Macinko J, Jimenez G, Mullachery P (2017). Globalization and Health 13:80. DOI 10.1186/s12992-017-0304-y (PMC5674740, CC BY)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC5674740", access="downloaded",
    figs={"GEO-04_table3.png": "Table 3 'Respondent characteristics, IAT effect and explicit survey measures' (PDF p.5)",
          "GEO-04_redraw.png": "IAT distribution by response category from Table 3 (data/GEO-04.csv)"},
    head="Abstract (PDF p.1) and p.4: 'The mean IAT score was 0.57 (95% CI 0.52 to 0.61) ... moderately strong implicit associations between Rich Countries and Good Research'. Table 3: 86% of 321 respondents pro-rich, 3.7% pro-poor.",
    check="MATCHES (IAT 0.57)",
    extra=["The paper has no figure of the IAT distribution; Table 3's response categories are used instead. The PMC bucket entry has no figure images."])

add("GEO-05", sec="06-geography", title="The role of geographic bias in knowledge diffusion: a systematic review and narrative synthesis",
    cit="Skopec M, Issa H, Reed J, Harris M (2020). Research Integrity and Peer Review 5:2. DOI 10.1186/s41073-019-0088-0 (PMC6961296, CC BY)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC6961296", access="downloaded",
    figs={}, head="Abstract (PDF p.1): 'only three were randomized and controlled studies'; 'Two of the three included studies identified that geographic bias in some form was impacting on peer review'.",
    check="MATCHES (3 RCTs, 2 found bias)",
    extra=["No extract requested ('-'). PMC figure JPGs kept in figures/ under their original names (Fig. 2 = Harris et al. results, Fig. 3 = Tomkins et al. results) in case a slide needs them."])

add("GEO-06", sec="06-geography", title="Assessing the effect of article processing charges on the geographic diversity of authors using Elsevier's 'Mirror Journal' system",
    cit="Smith AC, Merz L, Borden JB, Gulick CK, Kshirsagar AR, Bruna EM (2021). Quantitative Science Studies 2(4):1123-1143. DOI 10.1162/qss_a_00157; source.pdf = MetaArXiv preprint osf.io/s7cx4 ('Revision 2')",
    url="https://osf.io/s7cx4/download", access="downloaded",
    figs={"GEO-06_fig3.png": "Figure 3 Geographic Diversity (D2) of authors, OA Mirror vs bootstrapped non-OA Parent (preprint PDF p.34)",
          "GEO-06_table5.png": "Table 5 % of articles by World Bank lending group, non-OA Parent vs OA Mirror (preprint PDF p.31)",
          "GEO-06_redraw.png": "first-author income group, non-OA Parent vs OA Mirror, from Table 5 (data/GEO-06.csv)"},
    head="Abstract (preprint p.3): 'Author Geographic Diversity of OA articles was significantly lower than that of non-OA articles. Most OA articles were written by authors in high-income countries, and there were no articles in Mirror journals by authors in low-income countries.' p.13: none of 975 Mirror articles and 0.15% of Parent articles had lead authors in low-income countries.",
    check="MATCHES (zero OA Mirror articles from low-income authors) - but see inconsistency note",
    extra=["INCONSISTENCY in the preprint: Table 5 (p.31) lists 0.51% of first authors of OA Mirror articles in Low-income countries, contradicting the text. Check against the published QSS version (direct.mit.edu returned 403 to plain HTTP; the article is CC BY, so the user can download it in a browser).",
           "page.html = UF Geography news page (genuine)."])

add("GEO-07", sec="06-geography", title="Open science, done wrong, will compound inequities",
    cit="Ross-Hellauer T (2022). Nature 603(7901):363. DOI 10.1038/d41586-022-00724-0",
    url="https://media.nature.com/original/magazine-assets/d41586-022-00724-0/d41586-022-00724-0.pdf", access="downloaded",
    figs={}, head="PDF p.1: 'difficult conversations about how to pay publication fees that are three times a professor's monthly salary' (Ukrainian universities).",
    check="MATCHES with precision: it is 3x a professor's MONTHLY salary (the list says 'salary')",
    extra=["Quote-only source; no figure."])

add("GEO-08", sec="06-geography", title="Turning the tide of parachute science",
    cit="Stefanoudis PV, Licuanan WY, Morrison TH, Talma S, Veitayaki J, Woodall LC (2021). Current Biology 31(4):R184-R185. DOI 10.1016/j.cub.2021.01.029 (CC BY)",
    url="https://researchonline.jcu.edu.au/66906/1/66906.pdf (JCU repository, first pass)", access="downloaded",
    figs={"GEO-08_fig1.png": "Figure 1 bibliographic analysis of coral reef publications; panel C = % publications with no host-nation scientists, Indonesia/Australia/Philippines (PDF p.1)"},
    head="PDF p.1: 'approximately 40% of publications with fieldwork conducted in Indonesia or Philippines had no host nation scientist included, whereas the respective figure for Australia was half'.",
    check="MATCHES (~40%, for Indonesia and the Philippines specifically)",
    extra=["page.html = EurekAlert press release (genuine). Deleted page1.html (Elsevier 'Redirecting' interstitial). No redraw: panel C values are only shown graphically (~40/22/43%)."])

add("GEO-09", sec="06-geography", title="Who is telling the story? A systematic review of authorship for infectious disease research conducted in Africa, 1980-2016",
    cit="Mbaye R, Gebeyehu R, Hossmann S, Mbarga N, Bih-Neh E, Eteki L, et al. (2019). BMJ Global Health 4(5):e001855. DOI 10.1136/bmjgh-2019-001855 (PMC6830283, CC BY-NC)",
    url="https://pmc-oa-opendata.s3.amazonaws.com/PMC6830283", access="downloaded",
    figs={"GEO-09_fig3.jpg": "Figure 3 number and proportion of first authors by country, six diseases (PMC JPG; PDF p.6)",
          "GEO-09_fig4.jpg": "Figure 4 number and proportion of last authors by country (PMC JPG; PDF p.6)",
          "GEO-09_redraw.png": "African authorship by position (data/GEO-09.csv)"},
    head="Abstract (PDF p.1), Results p.3: of 1182 articles, 1109 (93.2%) had at least one Africa-based author, 552 (49.8%) an African first author, 41.3% (n=458) an African last author.",
    check="MATCHES (49.8%)",
    extra=["Percentages are of all 1182 articles (p.3); the Discussion (p.6) phrases them as 'of those that did include an African author', which is inconsistent with the denominators - use the Results wording."])

add("GEO-10", sec="06-geography", title="'Exhausted and insulted': how harsh visa-application policies are hobbling global research",
    cit="Owusu-Gyamfi S (2024). Nature 627(8005):705. DOI 10.1038/d41586-024-00892-1",
    url="https://www.nature.com/articles/d41586-024-00892-1.pdf", access="downloaded",
    figs={}, head="PDF p.1 (pull quote): 'Of the ten speakers from low- and middle-income countries invited to present at the session, only four got visas.' (European Conference of Tropical Ecology, Feb 2024)",
    check="MATCHES (4 of 10)", extra=["Quote-only source; no figure."])

add("GEO-11", sec="06-geography", title="Canada is denying travel visas to AI researchers headed to NeurIPS again (VentureBeat, 2019)",
    cit="VentureBeat (Nov 2019), 'Canada is denying travel visas to AI researchers headed to NeurIPS again' (author and exact date not verified: page not retrieved); secondary: The Canadian Press, 'Canada denies numerous researchers visas for AI conference for second year', 15 Nov 2019 (via CFJC Today)",
    url="https://venturebeat.com/ai/canada-is-denying-travel-visas-to-ai-researchers-headed-to-neurips-again (failed); secondary https://cfjctoday.com/2019/11/15/canada-denies-numerous-researchers-visas-for-ai-conference-for-second-year/",
    access="failed",
    figs={}, head="Secondary (page_canadianpress_cfjc.html): 'the government initially denied 30 researchers, mostly from African countries, but ... has since approved 15 on further review' (Black in AI figures); Black in AI 'saw about a third of its attendees denied visas for last year's conference in Montreal'.",
    check="NOT VERIFIED / possible MISMATCH: '15 of 44 denied' could not be checked against VentureBeat; search snippets attribute it to Timnit Gebru (15 of 44 Black in AI workshop attendees), while the Canadian Press (same week) reports 30 denied, 15 reversed; The Logic later reported 202 initial denials, 158 reversed (snippet only).",
    extra=["venturebeat.com returned HTTP 429 (rate limit) to plain HTTP; WebFetch could not resolve the host from this session; Wayback Machine API returned 429. Not retried with tricks. The user can open the VentureBeat page in a browser and save it.",
           "Icon graphic not made until the number is confirmed."])


for i, m in S.items():
    folder = f"{B}/{m['sec']}/{i}"
    figs_on_disk = sorted(os.path.relpath(p, folder) for p in glob.glob(f"{folder}/figures/{i}_*"))
    files = sorted(os.path.relpath(p, folder) for p in glob.glob(f"{folder}/**/*", recursive=True)
                   if os.path.isfile(p) and "/figures/" not in "/" + os.path.relpath(p, folder) and not p.endswith("notes.md"))
    lines = [f"# {i}: {m['title']}", "",
             f"- **Citation:** {m['cit']}",
             f"- **url_used:** {m['url']}",
             f"- **Access status:** {m['access']}",
             f"- **Headline number (from source):** {m['head']}",
             f"- **Check vs key number:** {m['check']}", "", "## Files"]
    lines += [f"- {f}" for f in files] or ["- (none)"]
    lines += ["", "## Figures extracted (with PDF page)"]
    lines += [f"- figures/{k}: {v}" for k, v in m["figs"].items()] or ["- (none)"]
    missing = [k for k in m["figs"] if f"figures/{k}" not in figs_on_disk]
    assert not missing, (i, missing)
    lines += ["", "## Notes"] + [f"- {x}" for x in m.get("extra", [])]
    lines += ["", f"Collected {DATE} with plain HTTP (requests/curl, browser User-Agent; email for APIs joaoifodase@gmail.com). Scripts: scripts/other/fetchlib.py, captions.py, presgeo_redraw.py, presgeo_notes.py; crops via scripts/pdfpeek.py at 300 dpi."]
    open(f"{folder}/notes.md", "w").write("\n".join(lines) + "\n")
    rel = lambda p: os.path.relpath(f"{folder}/{p}", ROOT)
    st = dict(id=i, title=m["title"], url_used=m["url"], file_paths=[rel(f) for f in files] + [rel("notes.md")],
              access_status=m["access"], figures_extracted=[rel(f) for f in figs_on_disk],
              notes=(m["check"] + ". " + m["head"]).replace("\n", " ")[:600])
    os.makedirs(f"{B}/_status", exist_ok=True)
    json.dump(st, open(f"{B}/_status/{i}.json", "w"), indent=1, ensure_ascii=False)
    print(i, m["access"], len(files), "files", len(figs_on_disk), "figs")
