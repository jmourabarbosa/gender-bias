# NAT-01: L'état de l'emploi scientifique en France, rapport 2025 (MESR)

- **Citation:** Ministère de l'Enseignement supérieur et de la Recherche (MESR-SIES) (2025). *L'état de l'emploi scientifique en France, rapport 2025*. 176 pages. No DOI.
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-05/l-tat-de-l-emploi-scientifique-en-france---rapport-2025-36858.pdf (first pass, source.pdf, 7.7 MB)
- **Access status:** downloaded
- **Headline number found (synthesis p.11; Partie 6, pp.139-147):**
  - 42% of the 2018 PhD graduates were foreign nationals (p.11; Tableau 17, p.147).
  - 20.8% of permanent researchers recruited in the public sector in 2022 were foreign nationals (p.11; Tableau 11, p.143). MCF recruits: 22.6%; CR (EPST) recruits: 24.5%.
  - 7.8% of tenured enseignants-chercheurs in MESR establishments were foreign nationals at 31/12/2022 (p.11; Tableaux 09-10, pp.142-143). PR: 6.8%; MCF: 8.3%.
  - Also: 36.2% of doctoral students are foreign "mobile" students (2023, Graphique 01, p.139); 15.1% of all paid public researchers incl. contract staff (Tableau 09, p.142).
- **Key number check (foreign share: 42% PhD graduates, 20.8% recruits, 7.8% tenured EC):** MATCH (all three)
- **Caveat for the slide:** the pipeline mixes definitions and years: "mobile" foreign doctoral students vs foreign nationality, 2018 graduates vs 2022 recruits vs the end-2022 stock. It is not a cohort. Naturalisation also lowers measured foreign shares further along the pipeline.
- **Not extracted here:** age and contract-status tables (cross-use in the PREC section).

## Figures

| File | From | PDF page |
|---|---|---|
| figures/NAT-01_fig1.png | Graphique 01 (share of foreign mobile students among doctoral students and doctorates, 2002-2023) + Tableau 02 (mobile doctoral students by origin) | 139 |
| figures/NAT-01_fig2.png | Tableau 09: origin of foreign researchers and EC in the public sector, end 2022 (incl. "% dans le total chercheurs") | 142 |
| figures/NAT-01_fig3.png | Tableau 10: foreign EC in EPSCP by corps (PR/MCF) and discipline, end 2022 | 143 |
| figures/NAT-01_fig4.png | Tableau 11: new permanent researcher recruits of foreign nationality, 2022 | 143 |
| figures/NAT-01_fig5.png | Tableau 17: employment of 2016/2018 PhD graduates by nationality (42.0% foreign) | 147 |
| figures/NAT-01_redraw.png | redraw of data/NAT-01_redraw.csv (pipeline) | 11, 139, 142, 143, 147 |

## Data

- data/NAT-01_foreign_pipeline.csv: foreign share at each stage, with sub-rows (MCF/CR/PR recruits, EPST researchers, tenured MCF/PR), definitions and page references.
- data/NAT-01_redraw.csv: the five main stages used in the redraw.
