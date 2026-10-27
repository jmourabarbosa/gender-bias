# DATA-12 — HESA staff open data (UK)

- **Title:** HESA Higher Education Staff Data — open data tables (CC BY 4.0)
- **Maintainer:** HESA / Jisc
- **url tried:** https://www.hesa.ac.uk/node/136617 and direct CSV patterns https://www.hesa.ac.uk/data-and-analysis/staff/table-9.csv , .../table-10.csv — all return a Cloudflare "Just a moment..." challenge (HTTP 403). Not bypassed; challenge pages were not saved.
- **Access status:** failed
- **Which tables to get (from search of HESA's table list):**
  - Table 9 — academic staff (excluding atypical) by sex, academic employment function, **contract level**, country of provider, mode of employment, source of basic salary.
  - Table 10 — academic staff by mode of employment, source of salary, clinical status, **contract level and sex**.
  - Caveat: from 2022/23 sex includes "Not known"; earlier years show 0 for that category. Some tables exceed Excel's row limit.
- **To fix:** download the CSVs from https://www.hesa.ac.uk/data-and-analysis/staff (detailed tables) in a normal browser and drop them into `data/`. Advance HE's staff report (DATA-13) is derived from the same HESA staff record.
