# PREC-05: Trajectoire professionnelle des enseignants-chercheurs recrutés en 2023 (Note de la DGRH n°3-2025) (= LOC-02)

- **Citation:** MESR-DGRH, Note de la DGRH n°3-2025 (same document as LOC-02).
- **url_used:** see other-biases-data/01-localism/LOC-02/source.pdf
- **Access status:** downloaded
- **Key number (list):** New MCF age 35; 42% from postdoc
- **Headline number found:** MCF recruited at 35 on average (PR 47), up from 33 a decade earlier (LOC-02 PDF p1-2, fig.5 p3); 42% of 2023 MCF recruits were postdocs (p1, fig.3 p2); ATER non-civil-servants 13% in 2023 vs 37% in 2005 (p1).
- **Check:** MATCH

## Files
- data/PREC-05.csv

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-05_fig1.png | LOC-02 PDF p2: fig.2 (previous activity of MCF recruits 2003-2023) and fig.3 (2023 by discipline) |
| figures/PREC-05_fig2.png | LOC-02 PDF p3: fig.5 mean age at hiring by discipline, MCF and PR, 2023 |
| figures/PREC-05_redraw.png | data/PREC-05.csv (postdoc share by discipline) |

## Notes
No file duplicated: the PDF stays in ../../01-localism/LOC-02/source.pdf; crops were made from it. The 2005 postdoc share (~24%) is read off the fig.2 curve and is approximate; the ATER 37% (2005) is stated in the text.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
