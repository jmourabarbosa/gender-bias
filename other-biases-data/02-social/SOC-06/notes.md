# SOC-06 - Morgan et al. (2022), Socioeconomic roots of academic faculty

- **Citation:** Morgan A.C., LaBerge N., Larremore D.B., Galesic M., Brand J.E., Clauset A. (2022), Nature Human Behaviour 6: 1625-1633. DOI 10.1038/s41562-022-01425-4. PMC9755046.
- **url_used:** https://pmc-oa-opendata.s3.amazonaws.com/PMC9755046 (PMC OA bucket, first pass)
- **access_status:** downloaded

## Headline number
22.2% of US faculty report at least one parent with a PhD (PDF p.2-3); share with a PhD parent is ~32% at the top-20% prestige institutions vs ~20% at the bottom 20% for faculty born in the 1980s (fig. 6a p.6).

**Key-number check:** **MATCH** (22.2%).

## Figures (PDF page of origin)
- `figures/SOC-06_fig1.png`: Figure 6, PDF p.6: % faculty with a PhD parent by birth decade and prestige (a) and by prestige rank (b), 300 dpi crop
- `figures/SOC-06_fig2.png`: Figures 1-2, PDF p.3 (same strip): ratio of parents' education to benchmarks; college-educated parents by gender
- `figures/SOC-06_redraw.png`: B/W redraw of fig. 6a
- other files in figures/: 41562_2022_1425_Fig1_HTML.jpg, 41562_2022_1425_Fig2_HTML.jpg, 41562_2022_1425_Fig3_HTML.jpg, 41562_2022_1425_Fig4_HTML.jpg, 41562_2022_1425_Fig5_HTML.jpg, 41562_2022_1425_Fig6_HTML.jpg

## Data
data/SOC-06.csv: fig. 6a values read from the vector markers (approximate; axis calibrated on tick labels). Original PMC JPGs kept in figures/ (41562_2022_1425_Fig1-6_HTML.jpg). Supplementary PDFs in supplementary/.

## Notes
Data availability: survey microdata only under an IRB-approved data-sharing agreement (not public); code at https://github.com/allisonmorgan/faculty_ses.

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
