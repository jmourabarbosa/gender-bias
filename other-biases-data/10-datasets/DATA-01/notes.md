# DATA-01 - Tenured higher-education teaching staff open data (MESR-SIES/DGRH)

- **Dataset:** `fr-esr-enseignants-titulaires-esr-public` - "Les enseignants titulaires dans les établissements publics de l'enseignement supérieur", MESR (Licence Ouverte). Rentrées 2010-2024, 337,160 records.
- **url_used:** not re-downloaded. Copied from the sister collection `gender-bias-data/10-datasets/DATA-01/data/` (same document), which was exported with `https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public/exports/csv?delimiter=%3B` (full export, no filter; see that folder's notes.md).
- **access_status:** downloaded

## Files
- `data/fr-esr-enseignants-titulaires-esr-public.csv.gz` (full export, 115.5 MB raw -> 5.5 MB gzip, `;`-separated, UTF-8 BOM) - copy.
- `data/dataset_metadata.json`, `data/aggregated_by_year_sex_category_section.csv` - copies from the gender collection.
- `data/DATA-01_by_year_region_category.csv` - new aggregate: sum of `effectif` by rentree x etablissement_region x code_categorie_assimil (MCF / PR / AM2D).
- `data/DATA-01_by_year_age_category.csv` - new aggregate: rentree x classe_age3 x category.
- Script: `scripts/other/data01_aggregates.py`.

## Headline number (our computation)
Île-de-France institutions employ 28.1% of tenured PR and 24.7% of MCF in 2024 (28.2% / 24.9% in 2010) - essentially flat. Compare DATA-03: Île-de-France partners receive ~35% of ANR project funding.

**Key-number check:** no key number listed (dataset entry).

## Figures
- `figures/DATA-01_redraw.png`: Île-de-France share of tenured PR and MCF, 2010-2024.
