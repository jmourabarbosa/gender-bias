# DATA-01 — MESR tenured teaching staff open data (France)

- **Title:** Les enseignants titulaires dans les établissements publics de l'enseignement supérieur (`fr-esr-enseignants-titulaires-esr-public`)
- **Maintainer:** MESR – SIES / DGRH (France). Licence Ouverte (Etalab). Dataset modified 2026-09-04; 337,160 records; rentrées 2010–2024.
- **url_used (full export, all records, no filters):**
  `https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public/exports/csv?delimiter=%3B`
  Metadata: `https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public` → `data/dataset_metadata.json`.
  (The host intermittently reset connections through the proxy; succeeded on the 3rd retry via `scripts/fetch_mesr_ec.py`.)
- **Access status:** downloaded
- **Files:**
  - `data/fr-esr-enseignants-titulaires-esr-public.csv.gz` — full export (115.5 MB raw → 5.5 MB gzip, `;`-separated, UTF-8 with BOM; md5 of raw CSV 6d1b516cff9b1782e1107ce3e4c49b8a). Raw CSV removed (> 90 MB).
  - `data/aggregated_by_year_sex_category_section.csv` — our aggregate: sum of `effectif` by rentree × sexe × categorie (MCF / PR / AM2D) × groupe CNU × section CNU × grande discipline.
- **Columns (full file):** rentree (year of academic-year start), annee_universitaire, etablissement_* (name, type, UAI, Paysage IDs, académie, région, coordinates), sexe (Femme/Homme), categorie_assimilation + code_categorie_assimil (MCF = Maître de conférences et assimilés; PR = Professeur et assimilés; AM2D = 2nd-degree teachers), grande_discipline, groupe_cnu/code_groupe_cnu, section_cnu/code_section_cnu, classe_age3, quotite, effectif (head count).

## Figures
- `figures/DATA-01_redraw_trend.png` — % women among MCF and PR, 2010–2024, all sections vs CNU 69 (Neurosciences).
- `figures/DATA-01_redraw_sections.png` — % women MCF vs PR in 2024 for all sections and neuro-relevant sections 69, 16, 44, 27 (scissor gap).

## Values (rentrée 2024, our computation)
| Section | % women MCF | % women PR | n MCF / n PR |
|---|---|---|---|
| All | 45.5 (42.5 in 2010) | 31.5 (20.7 in 2010) | 33,526 / 21,895 |
| 69 Neurosciences | 54.6 | 42.2 | 251 / 135 |
| 16 Psychologie & ergonomie | 63.4 | 56.8 | 934 / 472 |
| 44 Biochimie, biol. cell. & mol., physiologie & nutrition | 57.9 | 32.1 | 195 / 280 |
| 27 Informatique | 26.1 | 21.1 | 2,216 / 1,124 |
- Consistency: PIPE-04 (MESR Chiffres clés 2026) gives PR 33 % / MCF 45 % in 2024; this dataset gives 31.5 % / 45.5 % — the brochure's PR share is ~1.5 pp higher (different field/scope, e.g. inclusion of other "assimilés"/health corps). DATA-02 (2014: 43 % MCF, 24 % PR) vs this dataset 2014: 43.9 % / 23.2 %.
