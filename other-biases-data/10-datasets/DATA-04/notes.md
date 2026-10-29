# DATA-04 - ERC call statistics (host country of grantees)

- **Source:** European Research Council, call statistics PDFs ("Grantees by Country of Host Institution and Domain").
- **url_used:**
  - https://erc.europa.eu/system/files/2026-09/erc-2026-stg-statistics.pdf (source.pdf, first pass)
  - https://erc.europa.eu/system/files/2025-09/erc-2025-stg-statistics.pdf
  - https://erc.europa.eu/system/files/2025-12/erc-2025-cog-statistics.pdf
  - https://erc.europa.eu/system/files/2026-06/erc-2025-adg-statistics.pdf
  (erc.europa.eu answered normally this time.) Earlier calls (2021-2024) were not found: guessing `system/files/<YYYY-MM>/erc-<year>-<type>-statistics.pdf` returned nothing for 2021-2022, so the probe was stopped; older files use other names (find them in the ERC document library).
- **access_status:** downloaded

## Files
- `data/erc-2025-{stg,cog,adg}-statistics.pdf`; `data/erc_host_country.csv` (call, host country, grants, share, total, page) parsed from the chart text layer and checked against each call's stated total (421 / 478 / 349 / 319). Script `scripts/other/data04_erc.py`.

## Headline number
France hosts 38 of 421 StG 2026 grants (9.0%; source.pdf p.3), 41/478 StG 2025 (8.6%), 25/349 CoG 2025 (7.2%), 26/319 AdG 2025 (8.2%). Germany 89 (21%) and UK 47 (11%) in StG 2026. StG 2026 success rate ~8.8% (4,807 submitted, 421 selected; p.2).

**Key-number check:** no key number listed.

## Figures (PDF page of origin)
- `figures/DATA-04_fig1.png`: StG 2026, grantees by country of host institution and domain, source.pdf p.3 (full slide, 300 dpi).
- `figures/DATA-04_fig2.png`: StG 2026, grantees by nationality, source.pdf p.4 (full slide; bar values are not in the text layer, so not transcribed; read visually, about 30 French nationals vs 38 grants hosted in France).
- `figures/DATA-04_redraw.png`: % of grants hosted, 7 largest host countries, 4 calls.
