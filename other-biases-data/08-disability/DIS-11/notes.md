# DIS-11: Diversity and STEM: Women, Minorities, and Persons with Disabilities 2023 (NSF 23-315)

- **Citation:** NCSES, National Science Foundation, January 2023.
- **url_used:** https://ncses.nsf.gov/pubs/nsf23315/assets/nsf23315-report.pdf
- **Access status:** downloaded
- **Key number (list):** Disabled: 11% of S&E PhDs, 3% of workforce
- **Headline number found:** "Individuals with at least one disability earned 11% of S&E doctorate degrees" (PDF p56; Fig. 7-10: 10.8% S&E, 11.3% all fields, 2021); "9% of the population had one or more disabilities ..., 3% of those who work in STEM occupations did" (p5; Fig. 1-1 p6).
- **Check:** MATCH, with a caveat: the 3% (CPS, all STEM workers incl. the skilled technical workforce) and the 11% (SED doctorates) come from different surveys and definitions; among college-educated workers in S&E occupations (NSCG) the disability share is also 11% (p37). Do not present 11% vs 3% as a PhD-to-workforce leak.

## Files
- data/DIS-11.csv
- page.html
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/DIS-11_fig1.png | PDF p6: Figure 1-1, population vs STEM workforce by sex, race, disability (2021) |
| figures/DIS-11_fig2.png | PDF p56: Figure 7-10, doctorate recipients with disability by field (2021) |
| figures/DIS-11_redraw.png | data/DIS-11.csv |

## Notes
The XLSX data tables could not be fetched: the pubs/nsf23315 landing page and the data-tables PDF now return 404 (NCSES site reorganised); only the report PDF URL still works. Numbers were transcribed from the report figures instead.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
