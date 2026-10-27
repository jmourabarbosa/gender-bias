"""Write notes.md and _status/<ID>.json for PUB-01..11 and CIT-01..12 (sections 04/05)."""
import json, os
ROOT = "/home/user/gender-bias"
GD = f"{ROOT}/gender-bias-data"
S = {}
def add(id_, sec, title, cite, url, status, headline, check, extra="", data_note=""):
    S[id_] = dict(sec=sec, title=title, cite=cite, url=url, status=status, headline=headline,
                  check=check, extra=extra, data_note=data_note)

add("PUB-01", "04-publishing", "Bibliometrics: Global gender disparities in science",
    "Lariviere V, Ni C, Gingras Y, Cronin B, Sugimoto CR (2013). Nature 504:211-213. doi:10.1038/504211a",
    "https://www.nature.com/articles/504211a ; figures/supplement from https://media.springernature.com/ (Figb_HTML world map; MOESM105-107)",
    "paywalled",
    "Main text paywalled (Unpaywall/OpenAlex/Semantic Scholar: closed; no author/repository copy found). Supplementary Table S5 (free): WORLD row F=5,546,226 vs M=12,264,088 gendered author-paper combinations = 31.1% women (full counting; the paper's headline uses fractional counting).",
    "UNVERIFIED (main text paywalled); free Table S5 gives 31.1% women by full counting - close to but not below 30%",
    "World map (Figb) and citation chart (Figc) are the Nature graphics served openly on the article page.",
    "data/: Supplementary Tables S4 and S5 (country-level F/M/unisex/unknown/initials counts, xlsx).")
add("PUB-02", "04-publishing", "The gender gap in science: How long until women are equally represented?",
    "Holman L, Stuart-Fox D, Hauser CE (2018). PLoS Biol 16(4):e2004956. doi:10.1371/journal.pbio.2004956",
    "PMC OA bucket PMC5908072 (first pass); data: https://github.com/lukeholman/genderGap , https://github.com/lukeholman/genderGapCode , https://osf.io/bt9ya/",
    "downloaded",
    "p.6: last-author share in physics ~13%, rising ~0.1%/yr; model predicts 258 years (95% CI 194-383) to come within 5% of parity (S3 Data).",
    "MATCH (258 years refers to senior/last authors in physics, arXiv data)",
    "Fig 1 and Fig 2 = trajectories/years-to-parity by discipline.",
    "data/: S1-S3 Data CSVs (pbio.2004956.s027-s029); web-app data JSON (25 MB, genderGap repo); 'Author counts for journal country and position.csv.zip' (23 MB, genderGapCode repo); OSF arxiv data.csv (70 MB, https://osf.io/download/y9zsn/). NOT downloaded: OSF pubmed_gender_data.sqlite3 (2.46 GB) https://osf.io/download/7kbyf/")
add("PUB-03", "04-publishing", "Women are credited less in science than men",
    "Ross MB, Glennon BM, Murciano-Goroff R, Berkes EG, Weinberg BA, Lane JI (2022). Nature 608:135-145. doi:10.1038/s41586-022-04966-w",
    "https://www.nature.com/articles/s41586-022-04966-w (PMC9352587)",
    "downloaded",
    "p.2: 13.24% gap for articles (58.40% for patents) in the likelihood that women are named on a document produced by their team (Extended Data Table 4, col. 5).",
    "MATCH",
    "Fig 1 = actual vs potential female authorship share by career stage (a) and field (b).",
    "data/: MOESM3 xlsx = source data for Figs 1-2, 4-5 and tables (Fig 3 'NEED TO DISCLOSE FROM VDE'). Underlying microdata only via IRIS Virtual Data Enclave (restricted).")
add("PUB-04", "04-publishing", "Gender bias in scholarly peer review",
    "Helmer M, Schottdorf M, Neef A, Battaglia D (2017). eLife 6:e21718. doi:10.7554/eLife.21718",
    "PMC OA bucket PMC5360442 (first pass)",
    "downloaded",
    "p.2 / Fig 1b: women account for 37% of authoring, 28% of reviewing and 26% of editing contributions (Frontiers data to 2015).",
    "MATCH",
    "Fig 1 = authors/reviewers/editors share.",
    "data/: supp1.csv (country comparison), supp2.csv (literature values), graph/graph_edges.csv + graph_nodes.csv (from supp3.zip, 13 MB).")
add("PUB-05", "04-publishing", "Peer review and gender bias: A study on 145 scholarly journals",
    "Squazzoni F, Bravo G, Farjam M, et al. (2021). Sci Adv 7(2):eabd0299. doi:10.1126/sciadv.abd0299",
    "PMC OA bucket PMC7787493 (first pass)", "downloaded",
    "Abstract p.1: 'our findings suggest that peer review and editorial processes do not penalize manuscripts by women'; all-women/cross-gender teams often had higher success.",
    "MATCH", "Fig 1 = editorial decisions by gender of first and last author.")
add("PUB-06", "04-publishing", "Gender differences in peer review outcomes and manuscript impact at six journals of ecology and evolution",
    "Fox CW, Paine CET (2019). Ecol Evol 9(6):3599-3619. doi:10.1002/ece3.4993",
    "PMC OA bucket PMC6434606 (first pass); data https://doi.org/10.5061/dryad.7p048mk", "downloaded",
    "p.6 / Fig 4a: female first-authored papers invited for revision 16.4 +/- 1.9% of the time vs 18.3 +/- 2.4% for male first authors.",
    "MATCH", "fig1 = Fig 1 (sent to review), fig2 = Fig 3 (post-review outcomes), fig3 = Fig 4 (cumulative success).",
    "Dryad data NOT downloaded: Dryad API now requires a bearer token (401) and file_stream returned 403. File: 'Gender outcomes_anonymized.xlsx' (1.4 MB) at https://datadryad.org/dataset/doi:10.5061/dryad.7p048mk")
add("PUB-07", "04-publishing", "Journals invite too few women to referee",
    "Lerback J, Hanson B (2017). Nature 541:455-457. doi:10.1038/541455a",
    "source.pdf from first pass (Unpaywall/existing); landing https://doi.org/10.1038/541455a", "downloaded",
    "Graphic panel D (p.2): women 20% of reviewers vs 27% of published first authors (all ages, AGU journals 2012-2015).",
    "MATCH", "fig1 = whole 'Unequal opportunities' graphic (panels A-E), cropped at 300 dpi.")
add("PUB-08", "04-publishing", "Are women publishing less during the pandemic? Here's what the data say",
    "Viglione G (2020). Nature 581:365-366 (News). doi:10.1038/d41586-020-01294-9",
    "https://www.nature.com/articles/d41586-020-01294-9 ; graphic https://media.nature.com/original/magazine-assets/d41586-020-01294-9/d41586-020-01294-9_17998804.png",
    "paywalled",
    "News text is now behind Nature's paywall (only first paragraph visible). The open 'Preprint drop-off' graphic shows female first-author % on EarthArXiv/medRxiv/arXiv/bioRxiv, Jan-Feb & Mar-Apr 2019 vs 2020 (arXiv ~14.6-14.9% throughout).",
    "UNVERIFIED (the arXiv +2.7% women vs +6.4% men figure is in the paywalled text; not in the open graphic)",
    "fig1 = Nature 'Preprint drop-off' graphic (same data as PUB-11).")
add("PUB-09", "04-publishing", "COVID-19 medical papers have fewer women first authors than expected",
    "Andersen JP, Nielsen MW, Simone NL, Lewiss RE, Jagsi R (2020). eLife 9:e58807. doi:10.7554/eLife.58807",
    "PMC OA bucket PMC7304994 (first pass)", "downloaded",
    "p.3 / Fig 1d: women's share of first authorship 23% lower for COVID-19 papers published Mar-Apr 2020 vs 2019 papers in the same journals.",
    "MATCH", "Fig 1 = observed vs expected share; no separate source-data files (supp1.docx only).")
add("PUB-10", "04-publishing", "Unequal effects of the COVID-19 pandemic on scientists",
    "Myers KR, Tham WY, Yin Y, et al. (2020). Nat Hum Behav 4:880-883. doi:10.1038/s41562-020-0921-y",
    "source.pdf from first pass (OA copy); landing https://doi.org/10.1038/s41562-020-0921-y", "downloaded",
    "p.2 text: 'Having a young dependent ... child 5 years old or younger experienced a 17% larger decline in research time, all else being equal.'",
    "MATCH (note: 17% LARGER decline, not -17% research time overall)",
    "fig1 = Fig 2 (field- and group-level changes in research time; Lasso panel c).")
add("PUB-11", "04-publishing", "The decline of women's research production during the coronavirus pandemic",
    "Vincent-Lamarre P, Sugimoto CR, Lariviere V (2020). Nature Index news blog, 19 May 2020",
    "https://www.natureindex.com/news-blog/decline-women-scientist-research-publishing-production-coronavirus-pandemic ; chart data https://flo.uri.sh/visualisation/{2386034,2390460,2406024}/embed",
    "downloaded",
    "Page: medRxiv women first authorship fell from 35.9% (Dec 2019) to 20.2% (Apr 2020); Flourish data: medRxiv Mar-Apr 34.2% (2019) -> 22.2% (2020), EarthArXiv 21.3% -> 13.3%.",
    "MATCH (qualitative: first-author share fell)",
    "No static figures on the page (interactive Flourish charts). PUB-11_redraw.png from data/flourish_2386034.csv. CAUTION: in that Flourish export the column names read 'Jan-Feb 2019, Jan-Feb 2020, Mar-Apr 2019, Mar-Apr 2020' but the values match the Nature graphic (PUB-08) in the order Jan-Feb 2019, Mar-Apr 2019, Jan-Feb 2020, Mar-Apr 2020; the redraw uses the Nature order.",
    "data/: flourish_2386034.csv (platform x period), flourish_2390460.csv (monthly first-author share medRxiv/bioRxiv/arXiv), flourish_2406024.csv (COVID vs other).")
add("CIT-01", "05-citations", "The extent and drivers of gender imbalance in neuroscience reference lists",
    "Dworkin JD, Linn KA, Teich EG, Zurn P, Shinohara RT, Bassett DS (2020). Nat Neurosci 23:918-926. doi:10.1038/s41593-020-0658-y (preprint bioRxiv 10.1101/2020.01.03.894378 / arXiv 2001.01002)",
    "source.pdf = preprint (first pass); data https://osf.io/h79g8/?view_only=2222e015f63a4f41b1276a34c9b0c3a3 (via https://bit.ly/2O2xEFi)",
    "downloaded",
    "Preprint p.5: after controls, MM papers cited 5.2% more than expected, WW papers 13.9% less (95% CI -15.2,-12.5).",
    "MATCH (preprint numbers; published version not checked)",
    "fig1 = Fig 2 (over/undercitation construction + bars), fig2 = Fig 4 (time trends by citing-team gender).",
    "data/: NeuroCitation.RData (85 MB), NeuroCitation.R, NeuroCitation_HelperFunctions.R from OSF.")
add("CIT-02", "05-citations", "Gender Disparity in Citations in High-Impact Journal Articles",
    "Chatterjee P, Werner RM (2021). JAMA Netw Open 4(7):e2114509. doi:10.1001/jamanetworkopen.2021.14509",
    "PMC OA bucket PMC8254129 XML (first pass). PDF attempts: jamanetwork.com (Cloudflare 403), europepmc render (403), PMC pdf (reCAPTCHA)",
    "downloaded",
    "Table 2: overall median citations 36 (IQR 17-82) for women primary authors vs 54 (22-141) for men; Table 3 by pair: WW 33, WM 38.5, MW 42, MM 59.",
    "MATCH",
    "Full text = article.xml (CC BY, no PDF). Article has no figures; CIT-02_redraw.png from Table 3.",
    "data/: table3_median_citations_by_author_pair.csv")
add("CIT-03", "05-citations", "Quantitative evaluation of gender bias in astronomical publications from citation counts",
    "Caplar N, Tacchella S, Birrer S (2017). Nature Astronomy 1:0141. doi:10.1038/s41550-017-0141 (DOI verified via Nature page title)",
    "source.pdf = arXiv preprint (first pass); landing page.html", "downloaded",
    "Abstract p.1: papers authored by females receive 10.4 +/- 0.9% fewer citations than expected.",
    "MATCH", "fig1 = Figure 6 (measured/predicted citations for female-first-author papers by year).")
add("CIT-04", "05-citations", "Men Set Their Own Cites High: Gender and Self-citation across Fields and over Time",
    "King MM, Bergstrom CT, Correll SJ, Jacquet J, West JD (2017). Socius 3. doi:10.1177/2378023117738903",
    "source.pdf (first pass, Socius OA)", "downloaded",
    "Abstract p.1 & p.8: men cited their own papers 56% more than women (1779-2011); 70% more in last two decades.",
    "MATCH", "fig1 = Figure 4 (ratio of men's:women's self-citations per authorship by year).")
add("CIT-05", "05-citations", "The Matilda Effect in science: Awards and prizes in the US, 1990s and 2000s",
    "Lincoln AE, Pincus S, Koster JB, Leboy PS (2012). Soc Stud Sci 42(2):307-320. doi:10.1177/0306312711435830",
    "https://pubmed.ncbi.nlm.nih.gov/22849001 (abstract via eutils)", "paywalled",
    "Abstract only: men win a higher proportion of scholarly research awards than expected from the nomination pool; women's awards concentrated in service/teaching.",
    "UNVERIFIED (~10% figure not in abstract)",
    "Closed per Unpaywall/OpenAlex/S2. A copy is hosted by UW ADVANCE (https://advance.washington.edu/liy/sites/default/files/Lincoln%20et%20al.%20%282012%29%20The%20Matilda%20Effect%20in%20Science%20Awards%20and%20prizes%20in%20the%20US%2C%201990s%20and%202000s.pdf) but TLS failed (server chain to emSign root not trusted here) and host not resolvable for WebFetch - try in a browser.")
add("CIT-06", "05-citations", "Women who win prizes get less money and prestige",
    "Ma Y, Oliveira DFM, Woodruff TK, Uzzi B (2019). Nature 565:287-288 (Comment). doi:10.1038/d41586-019-00091-3",
    "https://media.nature.com/original/magazine-assets/d41586-019-00091-3/d41586-019-00091-3.pdf (first pass)", "downloaded",
    "p.2: female prizewinners received on average 64.4 cents per dollar won by men; women's share of research vs service prizes by decade (graphic).",
    "MATCH", "fig1 = full 'Awards gap' graphic (prizes by decade, research vs service, cash); fig2 = 'Women get less cash' panel.")
add("CIT-07", "05-citations", "The gender gap in highly prestigious international research awards, 2001-2020",
    "Meho LI (2021). Quantitative Science Studies 2(3):976-989. doi:10.1162/qss_a_00148",
    "https://scholarworks.aub.edu.lb/items/18d28692-a53d-4e17-909b-d17a78f3a265 (AUB ScholarWorks; publisher PDF at direct.mit.edu and CORE copy both Cloudflare-blocked)",
    "downloaded",
    "Abstract: 3,445 awards to 2,011 men and 262 women (262/2,273 = 11.5% of recipients); women's share rose from 6% (2001-05) to 19% (2016-20). Fig 2: 6%, 9%, 11%, 19% by 5-year bin.",
    "MATCH",
    "fig1 = Figure 2 (share of awards by women vs share of women professors, 5-year bins). Note AUB PDF is the published version as downloaded from MIT Press (watermark 'by Georgetown University user').",
    "data/: Meho_AwardRecipientsData.xlsx (award recipients, from AUB ScholarWorks).")
add("CIT-08", "05-citations", "Gender disparities in colloquium speakers at top universities",
    "Nittrouer CL, Hebl MR, Ashburn-Nardo L, Trump-Steele RCE, Lane DM, Valian V (2018). PNAS 115(1):104-108. doi:10.1073/pnas.1708414115",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC5776791/ (full-text HTML); fig https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30bf/5776791/758a91744b1f/pnas.1708414115fig01.jpg",
    "downloaded",
    "Results: men gave 69% of colloquium talks (n=2,519) vs women 31% (n=1,133). Female chairs -> 49% women speakers vs male chairs -> 30%.",
    "MATCH",
    "PDF not obtained: pnas.org and europepmc PDF are Cloudflare-blocked, PMC PDF gives reCAPTCHA; not in PMC OA subset. page.html = PMC full text. fig1 = Fig 1 (speakers by department); CIT-08_redraw.png = speaker share by chair gender (text numbers).",
    "data/: speakers_by_chair_gender.csv")
add("CIT-09", "05-citations", "Women's visibility in academic seminars: Women ask fewer questions than men",
    "Carter AJ, Croft A, Lukas D, Sandstrom GM (2018). PLoS ONE 13(9):e0202743. doi:10.1371/journal.pone.0202743",
    "PLoS PDF + PMC6159863 (first pass); data https://dx.doi.org/10.17617/3.12 (Edmond, MPG)", "downloaded",
    "p.8: male attendees over two and a half times more likely to ask a question than women attendees (odds ratio 2.57).",
    "MATCH", "fig1 = Fig 1 (question share vs audience share).",
    "data/: observational + survey data (txt) and R scripts from Edmond dataset doi:10.17617/3.12.")
add("CIT-10", "05-citations", "Analysis of science journalism reveals gender and regional disparities in coverage",
    "Davidson NR, Greene CS (2024). eLife 12:RP84855. doi:10.7554/eLife.84855",
    "PMC OA bucket PMC11132680 (first pass); data https://zenodo.org/records/7387906 (code https://github.com/greenelab/nature_news_disparities)",
    "downloaded",
    "p.7: share of quotes predicted to be from men fell from 87.09% (2005) to 68.86% (2020), i.e. women ~12.9% -> ~31.1%.",
    "MATCH", "fig1 = Figure 2 (quote share by predicted gender over time).",
    "data/: nature_news_disparities_data.zip (89.6 MB, Zenodo 7387906; GitHub clone failed mid-transfer so Zenodo archive used).")
add("CIT-11", "05-citations", "Ms. Categorized: Gender, notability, and inequality on Wikipedia",
    "Tripodi F (2021/2023). New Media & Society 25(7). doi:10.1177/14614448211023772 (CC BY)",
    "https://api.openalex.org/works/doi:10.1177/14614448211023772 (abstract). Blocked: journals.sagepub.com (Cloudflare), cdr.lib.unc.edu https://doi.org/10.17615/5zx6-hs09 (connection reset), core.ac.uk/download/519758964.pdf (Cloudflare), marketplace.org press page (403)",
    "abstract_only",
    "Abstract: <19% of English Wikipedia's >1.5 million biographies are about women; women's biographies are more frequently nominated for deletion.",
    "PARTIAL: 19% bios MATCH; 25% of deletion nominations UNVERIFIED (full text not reachable)",
    "Article is open access (CC BY) - should download fine in a normal browser from SAGE or UNC CDR.")
add("CIT-12", "05-citations", "Monitoring the gender gap in the coverage of biology professors on Wikipedia",
    "Alvarez-Ponce D, Iyengar N (2026). Proc R Soc B 293(2071):20252566. doi:10.1098/rspb.2025.2566 (CC BY)",
    "Publisher PDF https://royalsocietypublishing.org/rspb/article-pdf/doi/10.1098/rspb.2025.2566/6141731/rspb.2025.2566.pdf Cloudflare-blocked; SI from https://doi.org/10.6084/m9.figshare.31281317 and 10.6084/m9.figshare.31281314; abstract PubMed 42191161",
    "abstract_only",
    "Recomputed from Table S1 (2024 census, 2,104 women / 3,721 men): 197 women (9.36%) vs 278 men (7.47%) have a Wikipedia biography. Abstract: women 25% more likely than men in 2024; men more likely until 2018.",
    "MATCH (9.36% vs 7.47%)",
    "CIT-12_redraw.png = cumulative % with page by page-creation year (approximation of 'pages by gender over time'; the paper's own time series may use earlier censuses). page.html = ThePrint press article.",
    "data/: rspb20252566_si_001_TableS1.xlsx (per-faculty census + Wikipedia data), rspb20252566_si_002_TablesS2-S9.pdf, cumulative_share_with_page_by_year.csv")

os.makedirs(f"{GD}/_status", exist_ok=True)
for id_, s in S.items():
    folder = f"{GD}/{s['sec']}/{id_}"
    files = []
    for dp, dn, fn in os.walk(folder):
        for f in sorted(fn):
            if f == "notes.md": continue
            files.append(os.path.relpath(os.path.join(dp, f), ROOT))
    files.sort()
    figs = sorted(f for f in files if f"/figures/{id_}_" in f)
    rel = os.path.relpath(folder, ROOT)
    md = [f"# {id_}: {s['title']}", "", f"- **Citation:** {s['cite']}", f"- **url_used:** {s['url']}",
          f"- **Access status:** {s['status']}", f"- **Headline number found:** {s['headline']}",
          f"- **Key number check (SOURCES.md):** {s['check']}"]
    if s["extra"]: md.append(f"- **Notes:** {s['extra']}")
    if s["data_note"]: md.append(f"- **Data:** {s['data_note']}")
    md += ["", "## Files", ""] + [f"- {f}" for f in files] + [f"- {rel}/notes.md", ""]
    open(f"{folder}/notes.md", "w").write("\n".join(md))
    files.append(f"{rel}/notes.md")
    st = {"id": id_, "title": s["title"], "url_used": s["url"], "file_paths": sorted(files),
          "access_status": s["status"], "figures_extracted": figs,
          "notes": f"Key number: {s['check']}. {s['headline']}".replace("\n", " ")}
    json.dump(st, open(f"{GD}/_status/{id_}.json", "w"), indent=2, ensure_ascii=False)
    print(id_, s["status"], len(files), "files,", len(figs), "figs")
