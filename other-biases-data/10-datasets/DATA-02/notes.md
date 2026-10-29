# DATA-02 - Other MESR open datasets (contract staff, doctoral students, qualification, recruitment)

- **Maintainer:** MESR-SIES / DGRH, portal https://data.enseignementsup-recherche.gouv.fr (Opendatasoft, Licence Ouverte).
- **access_status:** downloaded (8 of 9 selected datasets; thesis-duration dataset failed after repeated connection resets)

## Catalogue queries (2026-10-29)
`https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets?where=search("<term>")&limit=40` for
- "contractuels" -> connection reset on every try (host resets through the proxy); covered by the "doctorants"/"enseignants-chercheurs" hits below;
- "doctorants" -> 14 datasets; "recrutement" -> 19 (mostly Parcoursup); "enseignants-chercheurs" -> 9;
- "qualification" / "qualifi" -> 3, none on CNU qualification (no open dataset for qualification; use PEER-13 DGRH notes).

## Exports (full, no filter)
`https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/<id>/exports/csv?delimiter=%3B` + `<id>.metadata.json` (`scripts/other/mesr_export.py`, with retries). Row counts equal the catalogue `records_count`.

| dataset id | content | rows |
|---|---|---|
| fr-esr-enseignants-nonpermanents-esr-public | non-permanent teaching staff (ATER, doctoral contracts with teaching, associate/invited, LRU contracts...) by institution, rentrée 2012-2024 | 90,219 |
| fr-esr-effectifs-doctorants-docteurs-ecoles-doctorales-financements-doctorants-c | doctoral students and graduates by ED; funding of new doctoral students (2018-2025); cotutelles | 18,578 |
| fr-esr-nouveaux-inscrits-doctorat-diplome-de-plus-haut-niveau-france-etranger | new doctoral students by origin of highest previous degree | 4,252 |
| fr-esr-epst-epic-fondations-chercheurs-recrutements-nationalites | external researcher recruitments in research organisations by nationality group, 2014-2020 | 1,110 |
| fr-esr-epst-epic-fondations-recrutements-departs | recruitments and departures of permanent staff in research organisations | 9,044 |
| fr-esr-epst-epic-fondations-chercheurs-recrutements-departs-discipline | researcher recruitments/departures by discipline | 2,892 |
| fr-esr-tbes-personnels-epst-epic-fondation-par-type-contrat-emploi | research-organisation staff by contract type | 2,228 |
| fr-esr-iuf-les-membres | Institut universitaire de France nominations 1991-2026 (with institution region) | 3,583 |
| fr-esr-effectifs-doctorants-docteurs-ecoles-doctorales-durees-these-domaines | thesis durations by field | FAILED twice (15 connection resets each pass); not collected |

## Derived tables (data/) and headline numbers (our computation)
- `DATA-02_nonpermanent_vs_tenured.csv`: non-permanent teaching staff rose from 25,965 (2012) to 34,797 (2024) while tenured staff (MCF+PR+2nd-degree, DATA-01) fell from 69,622 to 68,057: non-permanent share 27.2% -> 33.8%. Excludes hourly "vacataires", who are not in this dataset. `DATA-02_nonpermanent_by_group.csv` by group.
- `DATA-02_doctorants_by_year.csv`: doctoral enrolment 81,243 (2010) -> 69,432 (2025); share of new doctoral students with dedicated funding 69.8% (2018) -> 80.5% (2025).
- `DATA-02_researcher_recruits_nationality.csv`: 25-31% of external CR recruits in research organisations are non-French (2014-2020; 2020: 106 of 384).
- `DATA-02_iuf_idf_share.csv`: 38.1% of all IUF nominations (1991-2026) go to Île-de-France institutions (41% in 2010-2019).
- `DATA-02_idf_concentration_comparison.csv`: Île-de-France share of population 18%, tenured MCF 25%, PR 28%, ANR funding 2020-25 35%, IUF nominations 2020-26 36%.
Scripts: `scripts/other/data02_precarity.py`, `data02_doctorants.py`, `data02_nationalites.py`, `data02_iuf_region.py`.

**Key-number check:** no key number listed (dataset entry).

## Figures
- `figures/DATA-02_redraw.png`: non-permanent vs tenured teaching staff, 2012-2024.
- `figures/DATA-02_redraw2_idf_concentration.png`: Île-de-France concentration across indicators.
