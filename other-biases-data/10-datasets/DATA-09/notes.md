# DATA-09 - US faculty hiring networks (Larremore lab; Wapman et al. 2022)

- **Citation:** Wapman K.H., Zhang S., Clauset A., Larremore D.B. (2022), "Quantifying hierarchy and dynamics in US faculty hiring and retention", Nature 610:120-127. Data: Zenodo 10.5281/zenodo.6941650 (concept record; latest version v2026.08 = record 22099839, published 2026-08-25).
- **url_used:** https://zenodo.org/api/records/6941650 -> https://zenodo.org/api/records/22099839/files/us-faculty-hiring-networks-v2026.08.zip/content (3.7 MB)
- **access_status:** downloaded

## Files
- `data/us-faculty-hiring-networks-v2026.08.zip` and its extracted folder (README.md, data/edge-lists.csv 30.6 MB, institution-stats.csv, stats.csv, yearly-stats.csv); `data/zenodo_record.json`.
- `data/DATA-09_lorenz_academia.csv`: our Lorenz curve (Academia level).
- Script: `scripts/other/data09_lorenz.py`.

## Headline number (our computation)
Among the 368 US PhD-granting employing institutions, the most productive 21.5% trained 80% of the 238,986 US-trained faculty in the edge lists (Academia level). stats.csv gives a production Gini of 0.748 for academia. The paper reports 80% of faculty from 20.4% of universities - consistent (small difference from denominator choice and the 2026.08 re-export, which the README says fixed export bugs without changing the data).

**Key-number check (PRES-06 "80% from 20% of universities"):** **MATCH** (21.5% in our recomputation).

## Figures
- `figures/DATA-09_redraw.png`: Lorenz curve of faculty production.
