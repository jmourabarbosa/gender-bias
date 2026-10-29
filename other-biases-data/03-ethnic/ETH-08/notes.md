# ETH-08: Race, ethnicity, and NIH research awards

- **Citation:** Ginther D. K., Schaffer W. T., Schnell J., Masimore B., Liu F., Haak L. L., Kington R. (2011). "Race, ethnicity, and NIH research awards". *Science* 333(6045): 1015-1019. DOI 10.1126/science.1196783. PMID 21852498. PMCID PMC3412416 (NIH author manuscript NIHMS392536).
- **url_used:**
  - article.xml / article.txt / article.json: PMC open-data bucket, s3://pmc-oa-opendata/PMC3412416.1/ (licence "TDM", author manuscript). The bucket has XML and plain text only, no PDF and no figure images.
  - page.html: KU press release https://news.ku.edu/news/article/2011/08/18/black-scientists-less-likely-white-counterparts-receive-nih-funding-study-shows (genuine page; the page title is generic but it holds the article).
  - Not obtained: PDF and figure images. pmc.ncbi.nlm.nih.gov article and /pdf/ URLs serve a reCAPTCHA / "Preparing to download" challenge, and europepmc.org ?pdf=render returns 403. Neither was bypassed. Science (AAAS) version is paywalled.
- **NCBI idconv:** DOI 10.1126/science.1196783 maps to PMC3412416 (found via the first-pass log; the old idconv endpoint now redirects to pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/).
- **Access status:** downloaded (full text of the author manuscript as XML/TXT, no PDF)
- **Headline number found:** black applicants were 13.2 percentage points less likely than white applicants to receive an R01 award (raw), and 10.4 pp less likely after all controls (Model 5); 10.7 pp among US citizens. White R01 award probability = 29.3%. Results section, paragraphs on Fig. 1 and table S5 (article.txt lines 66, 74, 82).
- **Key number check (black applicants about 10 points less likely to be funded):** MATCH (10.4 pp with full controls; 13.2 pp raw).

## Figures

| File | From | Page |
|---|---|---|
| figures/ETH-08_redraw.png | redraw of data/ETH-08.csv (award probability by race, Fig. 1 values from text) | n/a (no PDF; results text) |

- The original Fig. 1 image is not available legally without a challenge. If needed, the user can download it from Science or PMC in a browser.
- The text does not state the Hispanic award rate (Fig. 1 shows it), so it is not in the redraw.

## Data

- data/ETH-08.csv: award probability. The white value is stated; the Asian and Black values are derived from the stated percentage-point gaps.
- Note: Taffe & Gilpin 2021 (ETH-11) cite Ginther's Table S2 as 17.1% for Black applicants (vs 29.3% white). The 16.1% here is derived from the text gap of 13.2 pp in the analysis sample; for a slide, prefer 17.1% vs 29.3% (1.7-fold).
- data/ETH-08_models.csv: marginal effects, Model 1 vs Model 5.
