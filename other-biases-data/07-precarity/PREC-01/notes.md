# PREC-01: Les enseignants contractuels affectés dans l'enseignement supérieur - Année 2024 (Note de la DGRH n°6-2025)

- **Citation:** MESR-DGRH (A.-S. Beaurenaut), Note de la DGRH - Enseignement supérieur n°6-2025, published Jan 2026.
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-01/note-dgrh-n-6---2025---enseignants-contractuels-ann-e-2024-pdf-39144.pdf
- **Access status:** downloaded
- **Key number (list):** 21,080 contract vs 61,879 tenured
- **Headline number found:** 2024: 21,080 contract teachers (text p1; table fig.2 p2 gives 21,084) vs 61,879 tenured; 25% of teachers (25.4% in table). Excludes 164,500 vacataires (p5).
- **Check:** MATCH

## Files
- data/PREC-01.csv
- series/contractuels2020-2021_note-dgrh-n5-2022.pdf
- series/contractuels2022_note-dgrh-n4-2023.pdf
- series/contractuels2023_note-dgrh-n3-2024.pdf
- series/nonpermanents2015-2016_note-dgrh-n4-2017.pdf
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-01_redraw.png | data/PREC-01.csv (fig.2 table p2 of this note + 3 earlier editions) |

## Notes
Series: earlier editions downloaded to series/ (Note DGRH n°4-2017 "enseignants non permanents 2015-2016", n°5-2022 (2020-2021), n°4-2023 (2022), n°3-2024 (2023)). data/PREC-01.csv merges contract vs tenured headcounts for 2000, 2005, 2010, 2012-2024 (2011 not in any edition retrieved). The 2016 value is the first year that includes L954-3 contract staff (break in series). Figure 1 (p1) is a chart of contract headcount since 2008; the fig.2 table on p2 holds the numbers, so no crop was made beyond the redraw.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
