# PREC-15: Age dynamics in scientific creativity

- **Citation:** Jones BF, Weinberg BA (2011). PNAS 108(47):18910-18914. doi:10.1073/pnas.1102895108 (PMC3223465). Summary: Lindau Nobel Laureate Meetings blog "Geniuses are getting older", 22 June 2016.
- **url_used:** https://pmc.ncbi.nlm.nih.gov/articles/PMC3223465/ (full-text HTML) ; https://www.lindau-nobel.org/?p=22157
- **Access status:** downloaded
- **Key number (list):** Age at Nobel work 36.9 -> 50.3 (physics)
- **Headline number found:** Lindau page: physics laureates made their discoveries at 36.9 (early period) vs 50.3 (later period); PNAS text (Results, Fig. 1B): mean age of prize-winning work rose by 13.4 y in physics, 10.2 y chemistry, 7.4 y medicine (early = work before 1905, late = after 1985). 36.9 + 13.4 = 50.3.
- **Check:** MATCH (the 36.9/50.3 levels are from the Lindau summary; the paper text gives the 13.4-year difference, consistent; levels are shown in Fig. 1A)

## Files
- data/PREC-15.csv
- page.html
- page_pmc.html

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-15_fig1.jpg | PMC figure image for Fig. 1 (low resolution, 428 px; the PDF could not be fetched) |
| figures/PREC-15_redraw.png | data/PREC-15.csv |

## Notes
access_status=downloaded refers to the full-text HTML on PMC (page_pmc.html) plus PMC figure images; the PDF is NOT available: pnas.org returns 403 (bot protection), PMC PDF route returns a reCAPTCHA page, Europe PMC a Cloudflare challenge, and the article is not in the PMC OA bucket. A high-resolution Fig. 1 needs the PDF via institutional access.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
