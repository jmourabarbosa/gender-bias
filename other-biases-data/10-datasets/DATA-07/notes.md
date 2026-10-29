# DATA-07 - OpenAlex API (OurResearch)

- **url_used:** https://help.openalex.org/api/grouping/ (page.html, first pass: documentation)
- **Query tried once (2026-10-29):** `https://api.openalex.org/works?filter=institutions.country_code:FR,publication_year:2023&group_by=authorships.institutions.id&mailto=joaoifodase@gmail.com`
- **Result:** HTTP 429 "Rate limit exceeded ... Insufficient budget. This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address ... resets at midnight UTC". Skipped as instructed.
- **access_status:** failed (rate-limited)

## To do
Re-run the query above after midnight UTC, or with a free OpenAlex API key (`api_key=` parameter). Useful follow-ups: `group_by=authorships.institutions.id` for FR 2015-2025, and `filter=authorships.countries:FR&group_by=publication_year` for country shares.
