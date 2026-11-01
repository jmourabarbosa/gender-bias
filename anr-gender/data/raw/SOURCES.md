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
