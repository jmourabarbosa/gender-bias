# DATA-03 — She Figures 2024 data (European Commission)

- **Title:** She Figures 2024 indicators (data tables)
- **Maintainer:** European Commission, DG Research & Innovation (Women in Science (WiS) database, Scopus/PATSTAT, Eurostat); tables republished in EIGE's Gender Statistics Database.
- **Report:** see PIPE-01 (statistics volume PDF, `01-pipeline/PIPE-01/source.pdf`).
- **Why not EC Excel:** the EC interactive-report page (projects.research-and-innovation.ec.europa.eu) returns HTTP 403 (CloudFront block) to this IP; no Excel tables were found on the ERA platform page (only PDFs). The same She Figures indicator tables are published in EIGE's Gender Statistics Database (theme "Research and digital → Science and technology", dataset IDs `sf_*`, source metadata: "Collected from the She Figures publications, based on the Women in Science (WiS) questionnaire").
- **Access status:** downloaded

## Download method (reproducible) — script `scripts/fetch_eige_shefigures.py`
- Indicator list: 46 indicator IDs containing `__sf_` scraped from https://eige.europa.eu/gender-statistics/dgs/indicator/ta_resdig_sctech_rdperes_seniority__sf_acadstaff_grades_abs
- Metadata: `https://eige.europa.eu/gender-statistics/dgs/json/db-data?path=indicator/<indicator_id>` (→ `data/<data_set>.meta.json`, includes criteria/categories, years, source notes)
- Data: `https://eige.europa.eu/gender-statistics/dgs/json/db-data?path=indicator-data/<data_set>/<criterion>:<category>/...`, looping over every combination of criteria categories (this is the public JSON endpoint the EIGE web app calls). Row counts match EIGE's `value_count` for all 46 datasets.
- Extra: Eurostat doctoral graduates by sex (ISCED 8), `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_grad02/A.NR.ED8..F+M+T.?format=SDMX-CSV`, filtered to iscedf13 = TOTAL and 3-character broad fields (F00–F10) → `data/eurostat_educ_uoe_grad02_ED8_broadfields.csv` (columns: DATAFLOW, LAST UPDATE, freq, unit, isced11, iscedf13, sex, geo, TIME_PERIOD, OBS_VALUE, OBS_FLAG, CONF_STATUS).

## Files (`data/`)
- `_index.csv` — one row per dataset: data_set, eige_indicator_id, name, unit, n_rows, eige_value_count, columns.
- `sf_*.csv` (46 files) — long format: `geo` (Eurostat country code; EU27_2020, EU28 aggregates), `year`, one column per criterion (e.g. `acad_grade` GRADE_A/B/C/D/TOTAL; `sex`; `ford` field of R&D; `sen_yrs` seniority; `age`; `sdg`; `teamcomp`; `hei_type`; `unit`), `value`, `flag`.
- Key tables: `sf_acadstaff_grades.csv` (% women by grade), `sf_acadstaff_grades_abs.csv` (head counts), `sf_acadstaff_gci.csv` (Glass Ceiling Index 2015–2022), `sf_acadstaff_grade_a_field.csv`, `sf_acadstaff_grade_a_age.csv`, `sf_auth_act_rd.csv` (women among active authors by field × seniority), `sf_fundrates.csv`, `sf_index.csv` (She Figures Index), `sf_hei_heads.csv`, `sf_resorg_boards.csv`.
- Caveat: EIGE stores the previous edition's academic-staff values under year **2018** (She Figures 2021), whereas the 2024 report text compares with **2019**; 2022 values match the report (EU-27 grade A 29.6 % here vs 29.7 % in Fig. 6.1 — rounding / revision).

## Figure
- `figures/DATA-03_redraw.png` — EU-27 2022 pipeline, women vs men: ISCED 8 graduates 48.5 % (Eurostat 2022, 48,079 / 99,204), grade C 46.8 %, grade B 42.0 %, grade A 29.6 %.

## Headline values (check vs PIPE-01 key number "48% PhDs, 30% grade A")
- Grade A EU27 2022 = 29.6 %; ISCED 8 graduates 2022 = 48.5 % (report uses 2021/2022 mix: 47.6 %). → consistent (**OK**).
