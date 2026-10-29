# DATA-03 - ANR funded projects and partners (open data, data.gouv.fr)

- **Datasets:** "ANR_01 Projets ANR DOS et DGDS : détail des projets et des partenaires" (data.gouv.fr dataset 60ca2086030c7b7e52e2c02e; files dated 2026-10-02) and "ANR_02 Projets ANR DGPIE (PIA/France 2030)" (60ca244980d5c4f0aecd07d1). Note: the source list's "ANR_01 (projects) and ANR_02 (partners)" is a misreading - ANR_01 holds both the projects and the partners files for the regular calls (AAPG etc.); ANR_02 is the investment-programme (DGPIE) equivalent.
- **url_used / queries:**
  - Catalogue: `https://www.data.gouv.fr/api/1/organizations/agence-nationale-de-la-recherche/datasets/?page_size=50`
  - static.data.gouv.fr reset every connection through this proxy, so files were taken from the data.gouv.fr tabular API instead:
    - ANR_01 partners 2005-2009: `https://tabular-api.data.gouv.fr/api/resources/0d691519-9a6c-4d66-a2e0-b9a8b3938968/data/csv/`
    - ANR_02 partners since 2010: `https://tabular-api.data.gouv.fr/api/resources/51cba202-da27-4f95-9337-0ff5aae7e6ae/data/csv/`
    - ANR_01 partners since 2010 (resource 4b576f41-8f4a-4f0f-860a-98eca420f3b9) and projects since 2010 (resource 87d29a24-392e-4a29-a009-83eddcff3e66): the full CSV export answers 403, so they were exported year by year with `.../data/csv/?Projet.Code_Decision__contains=ANR-YY-` (YY = 10..26) and concatenated (`scripts/other/anr_fetch_by_year.py`). For projects only the columns `Projet.Code_Decision, AAP.Edition, Projet.Acronyme, Projet.Titre.Anglais, Programme.Acronyme, Projet.Montant.AF.Aide_allouee.ANR, Projet.T0 scientifique` were requested (abstracts dropped; full file is 140 MB). Row counts match the API totals (83,834 partners; 26,740 projects).
  - The partners file was first decoded as Latin-1 by the client and was repaired (re-encoded to UTF-8) before analysis; the fetch script now decodes UTF-8.
- **access_status:** downloaded

## Files (data/)
- `anr-dgds-depuis-2010-partenaires.csv` (16 MB), `anr-dgds-depuis-2010-projets.csv` (3.8 MB, no abstracts), `anr-dgds-2005-2009-partenaires.csv`, `anr-dgpie-depuis-2010-partenaires.csv`.
- `anr_region_share.csv`: Île-de-France share by call year (our computation, `scripts/other/data03_anr_region.py`).

## Method
Partner-level `Projet.Partenaire.Aide_allouee.ANR`, partners with `Financement.Source == "ANR"`, year = `AAP.Edition` joined from the projects file on `Projet.Code_Decision` (identical to the year in the decision code for all projects). Share = Île-de-France allocations / allocations with a known partner region. Check: partner sums equal project totals per year (e.g. 2025: 951.7 vs 951.9 M EUR).
Caveats: 2010 has a region for only 84% of the funding (French partners without address), 2011 90%; 2026 results are still partial (443 M EUR so far). The 2005-2009 partners file has almost no regions (247 of 21,343 rows), so no share before 2010.

## Headline number
Île-de-France partners received 33.5%-38.1% of regional ANR project funding every year 2011-2025 (36.4% in 2025; 951.7 M EUR in total), versus ~18% of the French population and ~25-28% of tenured academic staff (DATA-01).

**Key-number check:** no key number listed (dataset entry).

## Figures
- `figures/DATA-03_redraw.png`: Île-de-France share of ANR funding by call year, 2010-2026.
