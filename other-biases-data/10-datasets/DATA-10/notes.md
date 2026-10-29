# DATA-10 - Nature Index 2026 Research Leaders (Springer Nature)

- **url_used:** https://www.nature.com/nature-index/research-leaders/2026/country/all/global (page.html, first pass). The "Export CSV" link (`/nature-index/research-leaders/export/2026/country/all/global`) answered HTTP 403 to a plain request; no browser automation used.
- **access_status:** downloaded (table parsed from the saved HTML page)

## Files
- `data/nature_index_2026_country_all_global.csv`: top-50 countries/territories table parsed from page.html (position, country, Share 2024, Share 2025, Count 2025, change in share). Script `scripts/other/data10_parse.py`.

## Headline number
2025 Share (2026 Research Leaders, all subjects): China 52,735; USA 26,006; Germany 5,827; UK 4,820; Japan 3,890; France 2,851 (6th, +4.6% vs 2024).

**Key-number check:** no key number listed. Institution tables were not exported (the 403 export link; the institution page was not saved).

## Figures
- `figures/DATA-10_redraw.png`: top-15 countries by 2025 Share, France highlighted.
