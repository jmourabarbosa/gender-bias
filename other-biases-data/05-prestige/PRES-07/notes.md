# PRES-07: La position scientifique de la France dans le monde et en Europe 2005-2018 (Hcéres-OST, édition 2021)

- **Citation:** Hcéres - Observatoire des sciences et techniques (2021). La position scientifique de la France dans le monde et en Europe, 2005-2018. Paris: Hcéres, ISBN 978-2-492781-00-1
- **url_used:** https://www.hceres.fr/sites/default/files/media/downloads/hceres_ost_positionnement_scientifique_france_edition_2021.pdf (failed); secondary: https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2023-11/-le-de-france-pdf-30114.pdf
- **Access status:** failed
- **Headline number (from source):** Secondary source secondary_mesr_strater_idf.pdf (MESR diagnostic territorial Île-de-France, Nov 2023), PDF p.3: 'Les publications scientifiques régionales représentent 34,5 % de la production nationale (1er rang) en 2019' (OST data). Same page also says 3.6% of European output in the text but 16.1% of European publications in the key-figures box (internal inconsistency, not used).
- **Check vs key number:** MATCHES via secondary source (34.5%, year 2019); primary Hcéres report not verified

## Files
- data/PRES-07.csv
- secondary_mesr_strater_idf.pdf

## Figures extracted (with PDF page)
- figures/PRES-07_redraw.png: Île-de-France vs rest of France share of French publications, 2019 (data/PRES-07.csv, from the secondary MESR document)

## Notes
- hceres.fr returned HTTP 503 'Hcéres - En maintenance' (site maintenance page, not saved) on every try; Wayback Machine API returned 429 Too Many Requests; HAL search found no deposit. Retry the primary PDF later (direct download, no bot protection) for the regional table/map and the France world-share series.
- Regional table for the other regions is not in the secondary document, so the CSV only has Île-de-France vs rest.

Collected 2026-10-29 with plain HTTP (requests/curl, browser User-Agent; email for APIs joaoifodase@gmail.com). Scripts: scripts/other/fetchlib.py, captions.py, presgeo_redraw.py, presgeo_notes.py; crops via scripts/pdfpeek.py at 300 dpi.
