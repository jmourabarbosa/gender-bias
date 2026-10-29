# PREC-02: Dossier "Les effectifs d'enseignant-es titulaires en baisse depuis 2010" / "Des choix budgétaires qui structurent l'emploi", Le Snesup n°734

- **Citation:** SNESUP-FSU (R. Grüber; P. Aubry), Le Snesup n°734, June-Aug 2025, pp.10-15.
- **url_used:** https://www.snesup.fr/sites/default/files/2025-06/dossier-mensuel-snesup734.pdf
- **Access status:** downloaded
- **Key number (list):** EC posts 3,613 (2011) -> 2,378 (2023)
- **Headline number found:** "le nombre d'ouvertures d'emplois d'EC autorisées est passé de 3 613 (campagne 2011) à 2 378 (campagne 2023), soit une baisse de plus de 34 %" (printed p11 = PDF p3). Teachers per 100 students 5.6 -> 4.4 (2008-09 to 2022-23, PDF p7).
- **Check:** MATCH. Cross-check against official DGRH notes: 3,613 = posts AUTHORISED in 2010 and 2011 (DGRH bilan 2011 p6, bilan 2013 p10) and 2,378 = posts authorised in 2023 (Note DGRH n°2-2025 p1). The union figures are correct but are authorised ceilings; posts actually PUBLISHED were 2,792 (2011) and 2,280 (2023), a 18% fall (see PREC-03/data/posts_candidates_series.csv).

## Files
- data/PREC-02.csv
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-02_fig1.png | PDF p7 (printed p15): staff-student ratio and budget per student 2008-09 to 2023-24 |
| figures/PREC-02_fig2.png | PDF p3 (printed p11): table, change in headcount by body 2010-2023 |
| figures/PREC-02_fig3.png | PDF p2 (printed p10): map of EC/E2D headcount change by académie |
| figures/PREC-02_redraw.png | data/PREC-02.csv (p11 table) |

## Notes
The infographic on p7 is a dual-axis chart in the original (left: euros, right: teachers per 100 students); the redraw only shows the table of changes by body to avoid a dual axis.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
