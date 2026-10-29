# LOC-01 - MESR-DGRH Note n°2-2026: Trajectoire professionnelle des enseignants-chercheurs recrutés en 2024

- **Citation:** Pépin C. (2026), Note de la DGRH - Enseignement supérieur n°2-2026, MESR/DGRH A1-1.
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-09/Note%20DGRH%20n%C2%B02%20-%202026%20-%20Trajectoire%20professionnelle%20des%20enseignants-chercheurs%20recrut%C3%A9s%20en%202024.pdf
- **access_status:** downloaded

## Headline number
23% of MCF recruited in 2024 are endo-recruited (PhD defended at the recruiting institution); 54% of PR were already MCF in the recruiting institution (p.1 summary, p.2 text, fig. 4 p.3). Foreign nationals: 23.5% of new MCF, 7.9% of new PR (fig. 6 p.4). Mean age at hiring 35 (MCF) / 47 (PR) (fig. 5 p.3).

**Key-number check:** **MATCH** (23% / 54%).

## Figures (PDF page of origin)
- `figures/LOC-01_fig1.png`: Figure 4, PDF p.3: néo-/endo-recrutement/mutation by discipline group (MCF, PR), 2024
- `figures/LOC-01_fig2.png`: Figure 6, PDF p.4: foreign share among recruits 2020-2024 (MCF, PR, PR not previously MCF)
- `figures/LOC-01_fig3.png`: Figure 5, PDF p.3: mean age at hiring by discipline group
- `figures/LOC-01_redraw.png`: B/W redraw of fig. 4 (data/LOC-01.csv)

## Data
data/LOC-01.csv (local-hiring table by discipline group, read from the labelled bars of fig. 4); data/LOC-01_age_foreign.csv (fig. 5 ages; fig. 6 endpoints 2020/2024 - intermediate years are not labelled). The series across years is in ../LOC-03/data/local_hiring_series.csv.

## Notes
Definition (p.4): endo-recruitment rate = local recruits / all posts filled incl. transfers. From 2022 all routes (incl. art. 46-3 and agrégation) are included. The note links Excel tables ('Tableaux Excel détaillés') but the MESR landing pages are behind a Cloudflare challenge, so they were not fetched.

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
