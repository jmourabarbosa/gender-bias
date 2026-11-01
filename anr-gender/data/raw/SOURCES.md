# Raw data sources

Downloaded 2026-11-01. These files are not committed (size; the partner file names individual researchers). Re-download them into this folder to run `analysis.py`.

| File | Source | URL |
| --- | --- | --- |
| `anr01.api.json` | data.gouv.fr API, ANR_01 (DGDS, ex-DOS) | https://www.data.gouv.fr/api/1/datasets/anr-01-projets-anr-dos-detail-des-projets-et-des-partenaires/ |
| `anr-dgds-depuis-2010-projets-finances-20261002-projets.xlsx` | ANR_01 projects, 2010 onwards, extracted 2026-10-02 (49,077,415 bytes). The CSV version, 140 MB, failed to download repeatedly through the session proxy; the xlsx holds the same table. | https://static.data.gouv.fr/resources/anr-01-projets-anr-dos-et-dgds-detail-des-projets-et-des-partenaires/20261001-222023/anr-dgds-depuis-2010-projets-finances-20261002-projets.xlsx |
| `anr-dgds-depuis-2010-projets-finances-20261002-partenaires.csv` | ANR_01 partners, 2010 onwards (18,585,782 bytes) | https://static.data.gouv.fr/resources/anr-01-projets-anr-dos-et-dgds-detail-des-projets-et-des-partenaires/20261001-222140/anr-dgds-depuis-2010-projets-finances-20261002-partenaires.csv |
| `2026-10-08-notice-anr-dgds-projets-finances.pdf` | ANR field documentation (notice), October 2026 | https://static.data.gouv.fr/resources/anr-01-projets-anr-dos-et-dgds-detail-des-projets-et-des-partenaires/20261008-173014/2026-10-08-notice-anr-dgds-projets-finances.pdf |
| `anr02.api.json` | data.gouv.fr API, ANR_02 (DGPIE, France 2030 / PIA) | https://www.data.gouv.fr/api/1/datasets/anr-02-projets-anr-dgpie-detail-des-projets-et-des-partenaires/ |
| `anr-dgpie-depuis-2010-projets-finances-20261002-projets.csv` | ANR_02 projects (context only) | https://static.data.gouv.fr/resources/anr-02-projets-anr-dgpie-detail-des-projets-et-des-partenaires/20261001-225000/anr-dgpie-depuis-2010-projets-finances-20261002-projets.csv |
| `anr-dgpie-depuis-2010-projets-finances-20261002-partenaires.csv` | ANR_02 partners (context only) | https://static.data.gouv.fr/resources/anr-02-projets-anr-dgpie-detail-des-projets-et-des-partenaires/20261001-225001/anr-dgpie-depuis-2010-projets-finances-20261002-partenaires.csv |
| `nat2021_csv.zip` → `nat2021.csv` | Insee, Fichier des prénoms, édition 2022 (births 1900–2021), the latest national file on the page | https://www.insee.fr/fr/statistiques/fichier/2540004/nat2021_csv.zip (page: https://www.insee.fr/fr/statistiques/2540004) |
| `committee_labels_anr_fr.json` (committed) | Committee labels (CE01…CE57) read from one anr.fr project page per committee, e.g. https://anr.fr/Projet-ANR-22-CE16-0001. The ANR open data has no committee label field. The CE9x codes have no label on their pages. | https://anr.fr/Projet-{code} |

Not downloaded: the 2005–2009 ANR_01 files (outside the 2010+ scope; listed in `anr01.api.json`).

## Committee (CES) member lists, AAPG

Downloaded 2026-11-01 into `data/raw/committees/` (not committed: named individuals). Parsed by `parse_committees.py`.

| Call | URL |
| --- | --- |
| AAPG 2017 | https://anr.fr/fileadmin/comites/2017/CES-aapg2017-V2.pdf |
| AAPG 2018 | https://anr.fr/fileadmin/comites/2018/CES-aapg2018.pdf |
| AAPG 2019 | https://anr.fr/fileadmin/documents/2019/Ces-aapg-2019.pdf |
| AAPG 2020 | https://anr.fr/fileadmin/comites/2020/CE-AAPG-2020.pdf |
| AAPG 2022 | https://anr.fr/fileadmin/aap/2022/selection/Compilation_Listes_Mbres_AAPG2022_.pdf |
| AAPG 2023 | https://anr.fr/fileadmin/aap/2023/selection/Compilation_Listes_Mbres_1_56_AAPG2023.pdf |
| AAPG 2024 | https://anr.fr/fileadmin/aap/2024/selection/aapg-2024-CE.pdf |
| AAPG 2025 | https://anr.fr/fileadmin/aap/2025/selection/aapg-2025-selection-CE.pdf |

No member list was found for AAPG 2014–2016 or 2021: the archived call pages link none, and the URL patterns of other years return 404. A 2026 list exists (https://anr.fr/fileadmin/aap/2026/selection/aapg-2026-comites.pdf) but the 2026 awards are excluded.
