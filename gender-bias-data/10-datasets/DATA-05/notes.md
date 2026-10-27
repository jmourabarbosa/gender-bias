# DATA-05 — Holman gender-gap app and data

- **Title:** The Gender Gap in Science (web app) — data behind Holman L, Stuart-Fox D, Hauser CE (2018) "The gender gap in science: How long until women are equally represented?" *PLoS Biology* 16(4):e2004956, DOI 10.1371/journal.pbio.2004956.
- **Maintainer:** Luke Holman (app: https://lukeholman.github.io/genderGap/ ; saved `page.html`, valid). Code: https://github.com/lukeholman/genderGapCode ; app repo https://github.com/lukeholman/genderGap ; full data on OSF https://osf.io/bt9ya/.
- **url_used:** https://lukeholman.github.io/genderGap/data_for_web_app_no_list.json (the JSON the web app loads; same file as `gh-pages/data_for_web_app_no_list.json` in the repo)
- **Access status:** downloaded (web-app aggregate data). Not downloaded (too large, linked only): OSF `pubmed_gender_data.sqlite3` (2.46 GB, https://osf.io/download/7kbyf/) and `arxiv data.csv` (70 MB, https://osf.io/download/y9zsn/). GitHub API access to the repo was not enabled in this session, but the data file is served from GitHub Pages.
- **Files:**
  - `data/data_for_web_app_no_list.json.gz` — raw app data (25,289 series; gzipped from 25 MB).
  - `data/genderGap_points_long.csv` — flattened (280,492 rows). Columns: Discipline (≈115 PubMed/arXiv discipline labels + "allDisciplines"; no "Neuroscience" label — closest are Neurology, Brain, Psychology, Psychophysiology), Country ("allCountries" or country), Journal ("allJournals" or journal abbrev.), Position (Overall/First/Last/Single author), curve_c, curve_r (fitted logistic-curve parameters from the app; r = rate of change, c = curve offset as in the app), year (2002–2016), pct_women_GR (% women authors), n_female, n_male, n_papers, ci_low, ci_high (95 % CI).
  - Filter used for plot: Country = allCountries, Journal = allJournals.

## Figure
- `figures/DATA-05_redraw.png` — % women among first and last authors, 2002–2016, all disciplines vs Neurology.

## Headline values (2016, all countries, all journals)
- All disciplines: first authors 44.3 %, last authors 31.2 %, overall 39.6 %.
- Neurology: first 40.9 %, last 27.2 %. Psychology: first 52.8 %, last 40.3 %. "Brain": first 47.0 %, last 29.7 %.
- Years-to-parity estimates are in the PLoS Biol paper (not recomputed here).
