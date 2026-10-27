# DATA-10 — ERC dashboard

- **Title:** ERC Dashboard (funded projects by panel, country, host institution, year)
- **Maintainer:** European Research Council Executive Agency (ERCEA)
- **url tried:** https://erc.europa.eu/node/21010 — HTTP 403 "Request blocked" (CloudFront) for this IP. Not bypassed. The dashboard is an interactive (Qlik/Power BI-type) page; no static CSV endpoint could be identified without loading the page.
- **Access status:** failed
- **Notes:** SOURCES.md says the gender values come from the ERC statistics PDFs (FUND-14 to FUND-18, another section) — use those for gender. For panel LS5 project counts, open the dashboard from a normal browser and use its export; alternatively CORDIS bulk project data (https://cordis.europa.eu/data — Horizon Europe / H2020 projects, filter `fundingScheme` ERC-*) gives project lists by panel/country but **no applicant gender**.
