"""Write notes.md + _status/<ID>.json for HIRE-01..08 and FUND-01..21 (second collection pass).
usage: python3 -I write_notes_hire_fund.py <repo_root>"""
import json, os, sys, glob
ROOT = sys.argv[1]
D = os.path.join(ROOT, "gender-bias-data")
S = {}
def e(i, sec, **k): S[i] = dict(sec=sec, **k)

e("HIRE-01","02-hiring",title="Science faculty's subtle gender biases favor male students",
  cit="Moss-Racusin CA, Dovidio JF, Brescoll VL, Graham MJ, Handelsman J (2012). PNAS 109(41):16474-16479. DOI 10.1073/pnas.1211286109",
  url="https://research.engineering.nyu.edu/~jbain/scitechsoc/readings/12MDBGH.pdf (NYU course-reading copy of the publisher PDF incl. SI). PNAS PDF (Cloudflare 403), Europe PMC render (Cloudflare challenge) and PMC3478626 (reCAPTCHA) were blocked; Yale Poorvu copy 404.",
  status="downloaded", head="p.3: 'The mean starting salary offered the female student, $26,507.94, was significantly lower than that of $30,238.10 to the male student' (Fig. 2).",
  check="OK", figs="HIRE-01_fig1.png = Fig. 1 competence/hireability/mentoring (p.2); HIRE-01_fig2.png = Fig. 2 salary (p.3).", short="Key number OK ($26,508 vs $30,238).")
e("HIRE-02","02-hiring",title="The impact of gender on the review of the curricula vitae of job applicants and tenure candidates: a national empirical study",
  cit="Steinpreis RE, Anders KA, Ritzke D (1999). Sex Roles 41(7/8):509-528. DOI 10.1023/A:1018839203698",
  url="none. Listed UW link https://www.engr.washington.edu/files/mycoe/faculty/docs/ImpactofGenderdoc.pdf now 404; Wayback snapshot exists (http://web.archive.org/web/20241203003452/...) but web.archive.org is unreachable from this sandbox (TLS tunnel closed); Springer DOI page returns a bot challenge (deleted). Unpaywall: not OA. A copy on education.newstank.fr (news site, not author/institution) was not used.",
  status="paywalled", head="not verified (no full text). Secondary summaries (USU ADVANCE library, search snippets) agree: both men and women more likely to vote to hire the male applicant; tenure-candidate CVs rated equally.",
  check="n.a. (unverified)", figs="none (Fig. 5 needs the PDF).", short="Paywalled; UW copy 404, Wayback copy exists but archive host unreachable here; key number unverified.")
e("HIRE-03","02-hiring",title="National hiring experiments reveal 2:1 faculty preference for women on STEM tenure track",
  cit="Williams WM, Ceci SJ (2015). PNAS 112(17):5360-5365. DOI 10.1073/pnas.1418878112. PMC4418903",
  url="https://pmc.ncbi.nlm.nih.gov/articles/PMC4418903/ (full-text HTML saved as pmc_article.html; figures from cdn.ncbi.nlm.nih.gov/pmc/blobs/...). No PDF: PNAS 403 Cloudflare, PMC OA bucket has no record (not OA subset), Europe PMC not OA.",
  status="downloaded", head="Results: 'female applicants ... ranked first by 67.3% of faculty, representing a highly significant 2:1 advantage (n = 339; chi2 = 40.38; P < 0.0001)'; abstract: '2:1 preference for women by faculty of both genders ... exception of male economists'.",
  check="OK", figs="HIRE-03_fig1.jpg = Fig. 1 (preference by field x faculty gender), PMC JPG.", short="Key number OK (2:1, 67.3%). Full text is PMC HTML, no PDF.")
e("HIRE-04","02-hiring",title="Committees with implicit biases promote fewer women when they do not believe gender bias exists",
  cit="Régner I, Thinus-Blanc C, Netter A, Schmader T, Huguet P (2019). Nature Human Behaviour 3:1171-1179. DOI 10.1038/s41562-019-0686-3",
  url="https://hal.science/hal-04860219/document (author accepted manuscript, HAL; no embedded figures). Figures: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41562-019-0686-3/MediaObjects/41562_2019_686_Fig1_HTML.png ; SI: .../41562_2019_686_MOESM1_ESM.pdf, MOESM2 (reporting summary), MOESM3_ESM.xlsx (Supp Table 1). nature.com PDF returned 429.",
  status="downloaded", head="Abstract: 'committees with strong implicit gender biases promoted fewer women at year 2 ... if those committees did not explicitly believe that external barriers hold women back. When committees believed that women face external barriers, implicit biases did not predict selecting more men over women.'",
  check="OK", figs="HIRE-04_fig1.png = Fig. 1 (% women by discipline + timeline, publisher PNG); HIRE-04_suppfig1ab.png = Supp. Fig. 1a,b (implicit bias x belief interaction on AI ratio, Year 1/Year 2; panel b is the key interaction plot); HIRE-04_suppfig1c.png = Supp. Fig. 1c.", short="Key claim OK; AAM from HAL + publisher Fig.1 and SI.")
e("HIRE-05","02-hiring",title="A linguistic comparison of letters of recommendation for male and female chemistry and biochemistry job applicants",
  cit="Schmader T, Whitehead J, Wysocki VH (2007). Sex Roles 57:509-514. DOI 10.1007/s11199-007-9291-4. PMC2572075",
  url="https://www.oacd.health.pitt.edu/sites/default/files/linguistic_comparison_of_letters_of_recommendation.pdf (Univ. of Pittsburgh copy of the publisher PDF). Springer and PMC blocked by bot checks.",
  status="downloaded", head="p.512: 'recommenders described male candidates (M=.70) with significantly more standout adjectives compared to female candidates (M=.60)', F(1,278)=3.95, p=.05; Table 2.",
  check="OK", figs="No figure in paper. HIRE-05_table2.png = Table 2 crop (p.512); HIRE-05_redraw.png from data/HIRE-05.csv (standout words, % of words).", short="Key claim OK (.70 vs .60% standout words); table crop + redraw.")
e("HIRE-06","02-hiring",title="Gender and letters of recommendation for academia: agentic and communal differences",
  cit="Madera JM, Hebl MR, Martin RC (2009). J Appl Psychol 94(6):1591-1599. DOI 10.1037/a0016539",
  url="https://www.mikkihebl.com/uploads/9/0/2/3/90238177/43.pdf (author-hosted manuscript, 39 pp). Unpaywall: not OA; PubMed landing returned an Incapsula block page (deleted).",
  status="downloaded", head="Study 1 (Table 2): applicant gender predicted communal adjectives (beta=-.16, p<.05; female coded 1) and agentic adjectives (beta=.16, p<.05): women described as more communal, less agentic.",
  check="OK", figs="HIRE-06_table2.png = Table 2 (HLM, agentic vs communal by applicant gender); HIRE-06_fig2.png = Figure 2 mediation diagram (Study 2). Manuscript's Figure 1 page is blank (image missing in author file).", short="Key claim OK; author manuscript (not version of record); Fig.1 missing in manuscript.")
e("HIRE-07","02-hiring",title="Gender differences in recommendation letters for postdoctoral fellowships in geoscience",
  cit="Dutt K, Pfaff DL, Bernstein AF, Dillard JS, Block CJ (2016). Nature Geoscience 9:805-808. DOI 10.1038/ngeo2819",
  url="https://serc.carleton.edu/download/files/138789/gender_dierences_recommendation_let.pdf (SERC/Carleton hosted copy, linked from https://serc.carleton.edu/details/files/138789.html)",
  status="downloaded", head="Table 4 (p.3): excellent letters 53/362 (15%) for female vs 203/862 (24%) for male applicants.",
  check="OK", figs="No figure in paper. HIRE-07_table4.png = Table 4 crop; HIRE-07_redraw.png stacked bars from data/HIRE-07.csv.", short="Key number OK (15% vs 24%).")
e("HIRE-08","02-hiring",title="Gender differences in how scientists present the importance of their research: observational study",
  cit="Lerchenmueller MJ, Sorenson O, Jena AB (2019). BMJ 367:l6573. DOI 10.1136/bmj.l6573. PMC7190066",
  url="https://madoc.bib.uni-mannheim.de/53361/1/bmj.l6573.full.pdf (Mannheim repository copy of BMJ PDF; Unpaywall location). JATS XML + figure JPGs from PMC OA bucket (first pass). bmj.com page was a bot check (deleted).",
  status="downloaded", head="'Articles in which the first and last authors were both women were, on average, 12.3% less likely to use positive terms' (10.9% vs 12.2%; 95% CI 5.7% to 18.9%).",
  check="OK", figs="HIRE-08_fig1.jpg = Fig. 1 positive terms over time 2002-17 (overall, by journal type); HIRE-08_fig4.jpg = Fig. 4 gender difference by journal type. A by-gender time series is in the appendix (supplementary/lerm051129.w1.pdf).", short="Key number OK (12.3%).")

e("FUND-01","03-funding",title="Are gender gaps due to evaluations of the applicant or the science? A natural experiment at a national funding agency",
  cit="Witteman HO, Hendricks M, Straus S, Tannenbaum C (2019). Lancet 393:531-540. DOI 10.1016/S0140-6736(18)32611-4. Preprint: bioRxiv 10.1101/232868",
  url="https://www.biorxiv.org/content/10.1101/232868v2.full.pdf (preprint v2 = source_preprint_biorxiv_v2.pdf). Lancet version paywalled; relx mirror gave 502; Unpaywall's biorxiv 'early' link returned 429.",
  status="downloaded", head="Preprint p.5: gap 0.9 points in traditional programmes, 0.9% in Project and 4.0% in Foundation program (OR 0.705), where review focused on the PI.",
  check="OK (preprint values; published Lancet text not checked)", figs="FUND-01_fig1.png = Fig. 1 success rate by programme and sex; FUND-01_fig2.png = Fig. 2 Foundation results by review stage.", short="Key numbers OK in preprint v2 (4.0 vs 0.9 pts); Lancet version of record paywalled.")
e("FUND-02","03-funding",title="Nepotism and sexism in peer-review",
  cit="Wennerås C, Wold A (1997). Nature 387:341-343. DOI 10.1038/387341a0",
  url="https://www.ehu.eus/documents/1775594/2032981/Nepotism_and_sexism_in_peer_review.pdf (Univ. of the Basque Country re-typeset copy, 'Reprinted by permission from Nature'; text + Table 1, figure not included). Listed cs.utexas.edu copy fails TLS verification (server chain) from this sandbox; nature.com is paywalled.",
  status="downloaded", head="'for a female scientist to be awarded the same competence score as a male colleague, she needed to exceed his scientific productivity by 64 impact points (95 per cent confidence interval: 35-93 impact points)'; Table 1.",
  check="OK", figs="FUND-02_redraw.png = model-based redraw of Fig. 1 from Table 1 regression (intercept 2.09, +0.21 male, 0.0033/impact point) in data/FUND-02.csv; the original scatter is not in this copy.", short="Key number OK (+64 impact points); re-typeset copy without original figure; redraw from Table 1.")
e("FUND-03","03-funding",title="No evidence of sexism in peer review (correspondence)",
  cit="Grant J, Burden S, Breen G (1997). Nature 390:438. DOI 10.1038/37213 (the listed nature.com/articles/37216.pdf is a different item: 'The hole truth')",
  url="https://www.nature.com/articles/37213.pdf -> landing page (paywalled), saved as page.html. Unpaywall: not OA.",
  status="paywalled", head="not verified; landing page has no abstract numbers.",
  check="n.a. (unverified)", figs="none", short="Paywalled; listed link 37216 is the wrong article (correct DOI 10.1038/37213); 27.5% vs 26.9% unverified.")
e("FUND-04","03-funding",title="Gender contributes to personal research funding success in The Netherlands",
  cit="van der Lee R, Ellemers N (2015). PNAS 112(40):12349-12353. DOI 10.1073/pnas.1510159112. PMC4603485",
  url="https://pmc.ncbi.nlm.nih.gov/articles/PMC4603485 (full-text HTML saved as page.html in first pass; figures from cdn.ncbi.nlm.nih.gov/pmc/blobs/786c/4603485/...). No PDF: PNAS 403, PMC not in OA bucket, Utrecht/Leiden repositories without file. Authors' reply to Volker & Steenbeek: https://scholarlypublications.universiteitleiden.nl/download/1887/45129/1?col=81522199280002711 (supplementary/reply_to_Volker_Steenbeek_Leiden.pdf). Critique: Volker & Steenbeek PNAS 112:E7036 (P = 0.045, Simpson's paradox).",
  status="downloaded", head="Results: 'success rate was systematically lower for female applicants than for male applicants [14.9% vs. 17.7%; chi2(1) = 4.01, P = 0.045]'.",
  check="OK", figs="FUND-04_fig1.jpg = Fig. 1 % women applications->awards; FUND-04_fig3.jpg = Fig. 3 applicants/awardees by discipline and gender (PMC JPGs).", short="Key number OK (14.9% vs 17.7%); note contested (P=0.045).")
e("FUND-05","03-funding",title="NIH funding longevity by gender",
  cit="Hechtman LA, Moore NP, Schulkey CE et al. (2018). PNAS 115(31):7943-7948. DOI 10.1073/pnas.1800615115. PMC6077749",
  url="PMC OA bucket https://pmc-oa-opendata.s3.amazonaws.com/PMC6077749 (first pass)",
  status="downloaded", head="Abstract: 'women had similar funding longevity as men after they received their first major NIH grants'; women 31% of grantees.",
  check="OK", figs="FUND-05_fig1.jpg = Fig. 1 survival by gender (PMC JPG).", short="Key claim OK (similar longevity).")
e("FUND-06","03-funding",title="Comparison of NIH grant amounts to first-time male and female principal investigators",
  cit="Oliveira DFM, Ma Y, Woodruff TK, Uzzi B (2019). JAMA 321(9):898-900. DOI 10.1001/jama.2018.21944. PMC6439593",
  url="https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/jama_oliveira_2019_ld_180068.pdf (author's Kellogg page, publisher PDF). jamanetwork.com 403; PMC reCAPTCHA.",
  status="downloaded", head="p.898: 'women received a median of $126 615 vs $165 721 for men (median difference -$39 106)'; Table 2: Big Ten $148,076 vs $66,365; Ivy $71,703 vs $52,190; top-50 $134,919 vs $93,916.",
  check="OK", figs="No figure in letter. FUND-06_table1.png (by grant type), FUND-06_table2.png (by institution tier); FUND-06_redraw.png from data/FUND-06.csv.", short="Key number OK ($165,721 vs $126,615 median).")
e("FUND-07","03-funding",title="Gender, race/ethnicity, and NIH R01 research awards: is there evidence of a double bind for women of color?",
  cit="Ginther DK, Kahn S, Schaffer WT (2016). Academic Medicine 91(8):1098-1107. DOI 10.1097/ACM.0000000000001278. PMC4965301",
  url="PMC author manuscript: JATS XML (article.xml, PMC OA bucket, first pass) + https://pmc.ncbi.nlm.nih.gov/articles/PMC4965301/ HTML (pmc_article.html) with figure JPGs from cdn.ncbi.nlm.nih.gov. No PDF: LWW not OA, ucdenver workshop copy 404.",
  status="downloaded", head="White women PhDs/MDs as likely as white men to get R01; e.g. 'applications from black women MDs were 12.9 ppt. less likely to receive NIH funding than applications from white women MDs'.",
  check="OK", figs="FUND-07_fig1.jpg = Fig. 1 R01 award probability by race x gender, PhD and MD samples (PMC JPG).", short="Key claim OK (race, not gender); full text XML/HTML, no PDF.")
e("FUND-08","03-funding",title="Little race or gender bias in an experiment of initial review of NIH R01 grant proposals",
  cit="Forscher PS, Cox WTL, Brauer M, Devine PG (2019). Nature Human Behaviour 3:257-264. DOI 10.1038/s41562-018-0517-y. PMC6699508",
  url="Preprint PDF https://osf.io/download/aj4hy/ (PsyArXiv r2xvb, via https://api.osf.io/v2/preprints/r2xvb/) = source_preprint_osf.pdf; published text = article.xml (PMC). scholarworks.uark.edu copy blocked by bot check; PMC HTML reCAPTCHA.",
  status="downloaded", head="'we found no evidence that white male PIs received different Overall Impact scores than PIs who were not white males' (Fig. 1).",
  check="OK", figs="FUND-08_fig1.png = Fig. 1 (white-male advantage vs white female / black male / black female PIs), cropped from preprint p.4.", short="Key claim OK; figure from OSF preprint (published PDF not retrieved).")
e("FUND-09","03-funding",title="Is blinded review enough? How gendered outcomes arise even under anonymous evaluation",
  cit="Kolev J, Fuentes-Medel Y, Murray F (2019). NBER Working Paper 25759. DOI 10.3386/w25759",
  url="NBER PDF (first pass): https://www.nber.org/system/files/working_papers/w25759/w25759.pdf",
  status="downloaded", head="p.18: female applicants' log-odds of higher scores 'approximately 16% lower than male applicants ... female applicants being approximately 15% less likely to receive a silver rating and 20% less likely to receive a gold rating'. Table 6: female coefficient -0.163*** (col 1) -> -0.076 (n.s.) once word-choice controls are added (col 7).",
  check="OK (minor nuance: 16% refers to the log-odds/ordered-logit effect, not a probability)", figs="FUND-09_table6.png = Table 6 (gap before/after text controls); FUND-09_table2.png = Table 2.", short="Key number OK with nuance (16% = log-odds effect).")
e("FUND-10","03-funding",title="Gender and other potential biases in peer review: cross-sectional analysis of 38 250 external peer review reports",
  cit="Severin A, Martins J, Heyard R, Delavy F, Jorstad A, Egger M (2020). BMJ Open 10:e035058. DOI 10.1136/bmjopen-2019-035058. PMC7440717",
  url="PMC OA bucket https://pmc-oa-opendata.s3.amazonaws.com/PMC7440717 (first pass). bmj.com landing page was a bot check (deleted).",
  status="downloaded", head="'male applicants received more favourable evaluation scores than female applicants (+0.18 points; 95% CI 0.14 to 0.23)'; adjusted difference 0.08.",
  check="OK", figs="FUND-10_fig1.jpg = Fig. 1 scores by applicant gender x reviewer gender (PMC JPG).", short="Key number OK (+0.18; adjusted 0.08).")
e("FUND-11","03-funding",title="Gender differences in grant peer review: a meta-analysis",
  cit="Bornmann L, Mutz R, Daniel H-D (2007). Journal of Informetrics 1(3):226-238. DOI 10.1016/j.joi.2007.03.001. arXiv math/0701537",
  url="arXiv PDF (first pass): https://arxiv.org/pdf/math/0701537",
  status="downloaded", head="'men have statistically significant greater odds of receiving grants than women by about 7%' (OR exp(0.07)=1.07).",
  check="OK", figs="FUND-11_fig1.png = Figure 1 forest plot (log-odds ratios per procedure), p.26.", short="Key number OK (+7% odds).")
e("FUND-12","03-funding",title="Gender differences in peer reviewed grant applications, awards, and amounts: a systematic review and meta-analysis",
  cit="Schmaling KB, Gallo SA (2023). Research Integrity and Peer Review 8:2. DOI 10.1186/s41073-023-00127-3. PMC10155348",
  url="PMC OA bucket https://pmc-oa-opendata.s3.amazonaws.com/PMC10155348 (first pass); forest plots extracted from supplementary/41073_2023_127_MOESM1_ESM.docx (EMF -> PDF via LibreOffice -> PNG). Springer pages were bot challenges (deleted).",
  status="downloaded", head="'Award acceptance rates were 1% higher for men, which was not significantly different (95% CI 3% more for men to 1% more for women)'; women received smaller award amounts (g = -2.28).",
  check="OK", figs="FUND-12_efig1.png = eFigure 1 forest plot award acceptance rate (US vs non-US); FUND-12_efig7.png = eFigure 7 forest plot award amounts. (Main-text Fig. 1 is only the PRISMA flow.)", short="Key number OK (~1 pt rate gap; amounts differ).")
e("FUND-13","03-funding",title="Strategies to prevent or reduce gender bias in peer review of research grants: a rapid scoping review",
  cit="Tricco AC, Thomas SM, Antony J et al. (2017). PLOS ONE 12(1):e0169718. DOI 10.1371/journal.pone.0169718. PMC5218731",
  url="PMC OA bucket https://pmc-oa-opendata.s3.amazonaws.com/PMC5218731 (first pass)",
  status="downloaded", head="'After screening 5524 citations and 170 full-text articles, one article evaluating gender-blinding of grant applications ... was included'.",
  check="OK", figs="none required (cite only); pone.0169718.g001.jpg is the PRISMA flow.", short="Key number OK (1 study in 5,524 records); cite only.")
e("FUND-14","03-funding",title="ERC gender flyer (2022)",cit="European Research Council (2022). Gender flyer. https://erc.europa.eu/sites/default/files/2022-09/gender_flyer.pdf",
  url="none. erc.europa.eu returns CloudFront 403 'Request blocked' to this sandbox (all pages, also via WebFetch: host not allowed). Wayback snapshot http://web.archive.org/web/20251007025950/https://erc.europa.eu/sites/default/files/2022-09/gender_flyer.pdf exists but web.archive.org is unreachable here.",
  status="failed", head="not verified. A web-search summary claims the flyer's content dates from 2012-2013 (unverified); check the year when opening it.",
  check="n.a. (unverified)", figs="none. See FUND-17/data/erc_women_share_grantees.csv for an StG vs AdG series from other sources.", short="ERC site blocked (CloudFront 403); Wayback copy exists but unreachable; StG 24% vs AdG 12% unverified.")
e("FUND-15","03-funding",title="ERC gender statistics June 2022",cit="European Research Council (2022). Gender statistics, data as of June 2022. https://erc.europa.eu/sites/default/files/2022-11/Gender_statistics_June_2022.pdf",
  url="none. erc.europa.eu CloudFront 403; Wayback snapshot http://web.archive.org/web/20241212180718/https://erc.europa.eu/sites/default/files/2022-11/Gender_statistics_June_2022.pdf exists but unreachable from this sandbox.",
  status="failed", head="n.a.", check="n.a.", figs="none", short="ERC site blocked (CloudFront 403); Wayback copy unreachable.")
e("FUND-16","03-funding",title="Inclusive excellence at the European Research Council (ERC): latest actions and results of sustained measures (EGU24-16168 poster)",
  cit="Jesus-Rydin C, Fariña-Busto L, Harvey-Kelly R, Jansen E (2024). EGU General Assembly 2024, EGU24-16168.",
  url="https://presentations.copernicus.org/EGU24/EGU24-16168_presentation.pdf (first pass)",
  status="downloaded", head="StG 2018-23: success rates of women and men with and without extension 'comparable, with only minor differences (0.5% and 1% lower for women than men)' (SR 13.0/13.6% women vs 12.5/14.6% men by window); women with extensions = 40% of female StG grantees.",
  check="OK", figs="FUND-16_fig_stg_extension.png = StG 2018-23 funded projects by gender and years since PhD + pie by eligibility window.", short="Key number OK (0.5-1 pt lower).")
e("FUND-17","03-funding",title="ERC 2024 Starting Grants results + StG time series",
  cit="ERC press release 5 Sep 2024 'ERC grants EUR 780m to emerging science talent in Europe' (erc.europa.eu, blocked); numbers via German NCP (EU-Büro des BMFTR) pages.",
  url="https://www.eubuero.de/en/news-erc-2024-09-26-3895.html ; https://www.eubuero.de/en/ncp-erc-starting-grants-2436.html ; https://www.eubuero.de/en/news-erc-2022-11-23-3059.html ; https://www.eubuero.de/en/news-erc-2023-09-05-3388.html (saved as page_eubuero_*.html). Official https://erc.europa.eu/news-events/news/erc-2024-starting-grants-results and erc-2024-stg-statistics.pdf: CloudFront 403.",
  status="downloaded", head="EU-Büro: '44 percent of these Starting Grants went to female researchers. In the 2023 call, 43 percent were women and in 2022 39 percent'.",
  check="OK (from NCP mirror, not the ERC page itself)", figs="FUND-17_redraw.png = women % of StG vs AdG grantees by call year from data/erc_women_share_grantees.csv (each row cites source URL + the official ERC URL it summarises; NCP overview values marked medium confidence; StG 2010-13 and 2019-21 missing because the NCP pages give applicant shares only).", short="Key number OK (44%) via German NCP; ERC site blocked; StG/AdG series CSV built from NCP + THE.")
e("FUND-18","03-funding",title="ERC Advanced Grants 2023 results / AdG 2024 facts and figures",
  cit="Times Higher Education, 11 Apr 2024, 'Proportion of female winners of top ERC grants dips' (P. Jack); ERC AdG 2023 results press release (erc.europa.eu, blocked).",
  url="https://timeshighereducation.com/news/proportion-female-winners-top-erc-grants-dips (page.html, first pass); https://www.eubuero.de/en/ncp-erc-advanced-grants-2450.html ; https://www.eubuero.de/en/news-erc-2025-06-17-4232.html ; https://www.eubuero.de/en/news-erc-2023-03-30-3230.html. Official ERC page https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2024-facts-and-figures: CloudFront 403.",
  status="downloaded", head="THE: '195 (76.5 per cent) went to male applicants and 60 (23.5 per cent) to female researchers - down from a peak of 27.5 per cent the year before' (AdG 2023). AdG 2024 call: women 23.3% of applicants (EU-Büro).",
  check="OK", figs="FUND-18_redraw.png (same StG vs AdG series as FUND-17; data/erc_women_share_grantees.csv). EU-Büro AdG-2024 line '(191 funded)' for women looks wrong (281 grants total) and was not used.", short="Key number OK (23.5%); ERC site blocked; series in CSV.")
e("FUND-19","03-funding",title="Femmes et hommes dans l'AAPG 2015-2025 (ANR)",cit="Agence nationale de la recherche (2026). Femmes et hommes de science: AAPG 2015-2025.",
  url="https://anr.fr/fileadmin/documents/2026/ANR-femmes-et-hommes-aapg-2015-2025-04206.pdf (first pass)",
  status="downloaded", head="p.12: success rate of women exceeded men's 'en 2024 avec un taux de 26 % pour les femmes contre 24 % pour les hommes. En 2025, le taux de succès des femmes est de 3 points inférieur'.",
  check="OK", figs="FUND-19_fig7.png = Fig. 7 success rate by gender 2015-2025; FUND-19_fig8a/8b/8c.png = Fig. 8 by instrument (JCJC, PRC, PRCE).", short="Key number OK (26% vs 24% in 2024; 2025 women 3 pts lower).")
e("FUND-20","03-funding",title="Wellcome grant funding data 2024/25",cit="Wellcome Trust (2026). Grant funding data for 2024/25.",
  url="https://wellcome.org/research-funding/funding-portfolio/funding-data-2024 ; CSVs from https://cms.wellcome.org/sites/default/files/2026-05/ (wellcome-gender-grant-data-25.csv etc.); older: https://wellcome.org/reports/grant-funding-data-2019-2020 , https://wellcome.org/reports/grant-funding-data-2018-2019 , https://cms.wellcome.org/sites/default/files/2021-03/Report_Wellcome_Grant_Funding_data_2019-20.pdf",
  status="downloaded", head="'Success rates for 2024/25 were: 10.4% for men and 9.4% for women'. Note: wellcome-gender-grant-data-25.csv is the share of awards by gender (women 52.4% in 2024/25), not success rates. Wellcome publishes no per-year success-rate CSV; data/FUND-20.csv collects the stated rates (2018/19 17% M vs 18% W; 2016/17-2019/20 pooled 13.0% vs 12.7%; 2024/25 10.4% vs 9.4%). 2020/21-2023/24 pages 404.",
  check="OK", figs="FUND-20_redraw.png from data/FUND-20.csv.", short="Key number OK (10.4% vs 9.4%); gender CSV is award shares, success rates only in text.")
e("FUND-21","03-funding",title="NIH Data Book: success rates by sex",cit="NIH Office of Extramural Research, NIH Data Book (RePORT), reports 131 and 132, updated March 2026.",
  url="API https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=132 (RPG applications/awards/success rate by sex, FY1998-2025) and reportId=131 (R01-equivalent success by sex and type); metadata https://report.nih.gov/reportweb/api/report/Get/<id>. Script: scripts/collect/nih_databook.py. NOTE: the listed link displayreport?rId=1005 redirects to a 2007 PDF 'Women supported by Kirschstein-NRSA training grants and fellowships' (kept as source.pdf), not a funding-rate report.",
  status="downloaded", head="RPG success rate FY2024: women 20% (3,898/19,426) vs men 18% (6,077/33,710); FY1998: 30% vs 32%. FY2025: 14% vs 13%.",
  check="n.a. (no number given); LINK MISMATCH: rId=1005 is the 2007 NRSA report", figs="FUND-21_redraw.png = RPG success rate by sex FY1998-2025 from data/nih_databook_report132.csv.", short="Data from NIH Data Book API (reports 131/132); listed rId=1005 link is the wrong report (2007 NRSA PDF).")

for i, v in S.items():
    folder = os.path.join(D, v["sec"], i)
    rel = lambda p: os.path.relpath(p, ROOT)
    nf = os.path.join(folder, "notes.md")
    lines = [f"# {i} — {v['title']}", "",
             f"- **Citation:** {v['cit']}",
             f"- **url_used:** {v['url']}",
             f"- **Access status:** {v['status']}", ""]
    files = sorted(p for p in glob.glob(os.path.join(folder, "**", "*"), recursive=True) if os.path.isfile(p))
    files_all = sorted(set(files + [nf]))
    lines += ["## Files"] + [f"- `{os.path.relpath(p, folder)}`" for p in files_all] + [""]
    lines += ["## Figures", f"- {v['figs']}", "", "## Headline number", f"- {v['head']}",
              f"- Key number in SOURCES.md: check → **{v['check']}**", ""]
    open(nf, "w").write("\n".join(lines))
    figs = sorted(rel(p) for p in glob.glob(os.path.join(folder, "figures", f"{i}_*")))
    st = dict(id=i, title=v["title"], url_used=v["url"], file_paths=[rel(p) for p in files_all],
              access_status=v["status"], figures_extracted=figs, notes=v["short"])
    os.makedirs(os.path.join(D, "_status"), exist_ok=True)
    json.dump(st, open(os.path.join(D, "_status", f"{i}.json"), "w"), indent=1, ensure_ascii=False)
print(len(S), "written")
