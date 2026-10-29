# PREC-04: La campagne de recrutement et d'affectation des MCF et des PR - Session 2021 (Note de la DGRH n°7, Sept 2022)

- **Citation:** MESR-DGRH, Note de la DGRH - Enseignement supérieur n°7, September 2022.
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2023-01/note-dgrh-n-7-septembre-2022---campagne-2021-26095.pdf
- **Access status:** downloaded
- **Key number (list):** 7.7 candidates per MCF post
- **Headline number found:** "Pour les 1 106 postes de MCF publiés, 45 762 candidatures recevables ont été déposées par 8 504 candidats, soit 41,4 candidatures et 7,7 candidats par poste" (PDF p2; same in fig.2 table p2).
- **Check:** MATCH

## Files
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-04_fig1.png | PDF p2: fig.2 table by discipline 2021 (LSH 10.4 candidates per MCF post) |
| figures/PREC-04_redraw.png | candidates per MCF post 2008-2025 from PREC-03/data/posts_candidates_series.csv |

## Notes
The candidates-per-post series for all years lives in ../PREC-03/data/posts_candidates_series.csv (see PREC-03 notes for definitions and gaps). Peak 7.7-7.8 in 2015 and 2021; falls to ~5 in 2023-2024 as posts rose.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
