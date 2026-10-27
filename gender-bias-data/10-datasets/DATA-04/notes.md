# DATA-04 — UNESCO UIS data (female researchers as % of total)

- **Title:** UNESCO Institute for Statistics (UIS) — R&D statistics, "Researchers (HC/FTE) – % Female" (SDG 9.5-related)
- **Maintainer:** UNESCO Institute for Statistics. Browser: https://databrowser.uis.unesco.org (saved as `page.html`, valid landing page from first pass).
- **url_used (API, no key needed):**
  `https://api.uis.unesco.org/api/public/data/indicators?indicator=FRESP.THC&indicator=FRESP.TFTE&indicator=FRESP.SP.THC.BUSENTSP&indicator=FRESP.SP.THC.GOVSP&indicator=FRESP.SP.THC.HIEDUSP&indicator=FRESP.SP.THC.PRNPSP&footnotes=true&indicatorMetadata=false`
  Indicator codes found via `https://api.uis.unesco.org/api/public/definitions/indicators`; geo names via `https://api.uis.unesco.org/api/public/definitions/geounits` (both saved: `data/uis_geounits.json`).
- **Access status:** downloaded
- **Files:**
  - `data/uis_api_response.json` — raw API response (8,756 records).
  - `data/uis_female_researchers_pct.csv` — flattened. Columns: indicatorId (FRESP.THC = researchers HC % female; FRESP.TFTE = FTE % female; FRESP.SP.THC.{BUSENTSP, GOVSP, HIEDUSP, PRNPSP} = % female by sector: business, government, higher education, private non-profit), geoUnit (ISO3 or aggregate code e.g. "UIS: World", "SDG: Europe"), geoName, geoUnitType (NATIONAL/REGIONAL), year, value (%), qualifier, footnotes.
  - National series run ~1996–2023; regional/world aggregates are only published for **2013 and 2023** in the current release.

## Figure
- `figures/DATA-04_redraw.png` — UIS regions, % women among researchers (HC), 2013 vs 2023 (grey bars).

## Headline values
- UIS World: 29.5 % (2013) → **31.4 % (2023)**. France 30.6 % (2023).
- Cross-check with PIPE-10 (UNESCO 2025 factsheet: 29.4 % in 2012 → 31.1 % in 2022): the current UIS release (data year 2023) gives slightly different, later values; regional values also shift (e.g. Central Asia 51.2 % vs 50.8 %). Use the factsheet values when quoting the factsheet, and this file for redraws — note the year difference.
