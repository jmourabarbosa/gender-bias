# NAT-02: MESR-DGRH Note n°2-2026, foreign share of EC recruits (cross-reference to LOC-01)

- **Cross-reference:** same document as **LOC-01**. The PDF lives at `other-biases-data/01-localism/LOC-01/source.pdf` and is not duplicated here.
- **Citation:** MESR, DGRH A1-1 (2026). *Trajectoire professionnelle des enseignants-chercheurs recrutés en 2024*. Note de la DGRH - Enseignement supérieur n°2-2026. 4 pages. No DOI.
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B02%20-%202026%20-%20Trajectoire%20professionnelle%20des%20enseignants-chercheurs%20recrut%C3%A9s%20en%202024.pdf (via LOC-01)
- **Access status:** downloaded (in LOC-01)
- **Headline number found:** 23.5% of MCF recruited in 2024 were foreign nationals (17.5% in 2020); PR 7.9% (10.0% in 2020); PR not previously MCF 30.9% (39.6% in 2020). Graph 6, PDF p.4; summary p.1 ("23 % des MCF et 8 % des PR recrutés sont étrangers"); text p.3 (MCF: -4 pts in 2023 vs 2022, +5 pts in 2024). Most foreign recruits are European (73% of foreign PR, 40% of foreign MCF; Italians 33% / 18%), with 27% of nationalities missing in 2024 (p.4).
- **Key number check (23.5% of MCF vs 7.9% of PR foreign):** MATCH
- **Series 2020-2024:** the note prints only the 2020 and 2024 values. 2021-2023 were digitised from the vector paths of graph 6. Calibration: 0% at y=228pt, 3pt per percentage point. The printed endpoints are reproduced within 0.15 pt, so the digitised values are accurate to about 0.2 pt. The MCF 2022 to 2023 drop (-4.2) matches the text ("baisse de 4 points"). The DGRH "Tableaux Excel détaillés" mentioned on p.4 would give exact values. The note links no URL for them, so they were not fetched.
- **Comparison with NAT-01:** NAT-01 Tableau 11 gives 22.6% foreign among 2022 MCF recruits (this note: ~22.7% for 2022). It gives 39.2% for PR recruits (20 people), which corresponds to this note's "PR not previously MCF" (~39.2% in 2022), not to all PR.

## Figures

| File | From | PDF page |
|---|---|---|
| figures/NAT-02_fig1.png | Graph 6: foreign share among recruits (MCF, PR, PR not previously MCF), 2020-2024 | 4 (LOC-01/source.pdf) |
| figures/NAT-02_redraw.png | redraw of data/NAT-02.csv | 4 |

## Data

- data/NAT-02.csv: series 2020-2024. The 2020 and 2024 values are printed labels; 2021-2023 are digitised.
- Digitising script: scripts/other/nat02_digitise.py (run on LOC-01/source.pdf). Redraw script: scripts/other/nat02_redraw.py.
