# PREC-07: Le Centre national de la recherche scientifique (CNRS), exercices 2013-2023 - rapport d'observations définitives

- **Citation:** Cour des comptes, 2025 (copy hosted by Campus Matin).
- **url_used:** https://campusmatin.com/file/a706bd62d95ab4dcc9c1a4df08973ee9/rapport-cour-comptes-exercices-2013-2023-cnrs.pdf
- **Access status:** downloaded
- **Key number (list):** Contract staff 23% -> 29%
- **Headline number found:** "la part des contractuels financés sur ressources propres augmente peu à peu (29 % des effectifs en 2023 contre 23 % en 2013)" (PDF p7). Annex table 2 (p114): contract staff 9,445 ETPT (27.8%) in 2013 -> 11,034 (32.2%) in 2023. CR recruitment age 30 (2006) -> 33.9 (2013) -> 34.4 (2020) (p44).
- **Check:** MATCH (note: 23%->29% is the share funded on own resources; all contract staff are 27.8%->32.2% of ETPT)

## Files
- data/PREC-07_selection_rate.csv
- data/PREC-07_staff_age.csv
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-07_fig1.png | PDF p49: Graphique 11, selection rate of CNRS competitions 2013-2022 |
| figures/PREC-07_fig2.png | PDF p114: annex Tableau 2, staff in ETPT 2013/2022/2023 by status |
| figures/PREC-07_redraw.png | data/PREC-07_selection_rate.csv |

## Notes
The age-at-recruitment "series" exists only as three numbers in the text (p44); they are in data/PREC-07_staff_age.csv. "Applications vs posts" is given as selection rates (Graphique 11), read from the vector chart by scripts/other/prec07_fig11_vector.py (+-0.05 pt). The ccomptes.fr copy was not fetched (the Campus Matin copy is the full report, 131 pages).

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
