# ETH-13: NCES Fast Facts, race/ethnicity of college faculty (fall 2022)

- **Citation:** National Center for Education Statistics, Fast Facts "Race/ethnicity of college faculty" (id=61), based on *Condition of Education 2024, Characteristics of Postsecondary Faculty*. Underlying table: *Digest of Education Statistics 2023*, Table 315.20 (IPEDS Human Resources, fall 2022; prepared Nov 2023).
- **url_used:**
  - page.html: https://nces.ed.gov/FastFacts/display.asp?id=61 (first pass, checked as genuine)
  - dt23_315.20.xlsx: https://nces.ed.gov/programs/digest/d23/tables/xls/tabn315.20.xlsx
  - dt23_315.20.html: https://nces.ed.gov/programs/digest/d23/tables/dt23_315.20.asp
- **Access status:** downloaded
- **Headline number found:** of full-time faculty in fall 2022, 72% were White, 13% Asian, 7% Black, 6% Hispanic and 1% two or more races (page.html). Recomputed from Table 315.20, excluding race-unknown and nonresident faculty: White 72.4%, Asian 12.6%, Black 6.5%, Hispanic 6.4%. Among full professors: Black 4.3%, Hispanic 4.5%, White 77.0%.
- **Key number check (72% White, 7% Black, 6% Hispanic):** MATCH
- **Faculty vs population:** not added. The Census API (api.census.gov) now requires a key ("Missing Key" page), so ACS population shares were not downloaded. If a key is available, use ACS 2022 1-yr DP05: DP05_0073PE (Hispanic), DP05_0079PE (White non-Hispanic), DP05_0080PE (Black non-Hispanic), DP05_0082PE (Asian non-Hispanic).

## Figures

| File | From | Page |
|---|---|---|
| figures/ETH-13_redraw.png | redraw of data/ETH-13.csv (all FT faculty, full professors, assistant professors) | n/a (web table) |

## Data

- data/ETH-13.csv: shares by race for all full-time faculty, full professors and assistant professors, fall 2022. Computed from Table 315.20 as count / (total - race unknown - nonresident).
