# PRES-08: Les dépenses de R&D des entreprises en 2024 (données provisoires)

- **Citation:** Chanteloup G (2026). MESRE-SIES Note Flash n°06, avril 2026. DOI 10.5281/zenodo.19251000
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-04/nf-sies-2026-06-39988.pdf
- **Access status:** downloaded
- **Headline number (from source):** PDF p.2: 'En Île-de-France, les entreprises réalisent 17,5 Md€ de dépenses intérieures de R&D en 2024, soit 42 % de la DIRDE totale et emploient 39 % des effectifs de R&D'. Map values sum to 41.87 bn (metropolitan) vs 41.9 bn total; IdF 17.52/41.87 = 41.8%.
- **Check vs key number:** MATCHES (~42%)

## Files
- data/PRES-08.csv
- source.pdf

## Figures extracted (with PDF page)
- figures/PRES-08_fig1.png: Carte 1 'Dépenses intérieures de R&D des entreprises par région en 2024 (p) en Md€' (PDF p.2)
- figures/PRES-08_redraw.png: bar chart of the 13 metropolitan regions transcribed from Carte 1 (data/PRES-08.csv)

## Notes
- Rest of France = 24.35 bn (58%); top 3 regions (IdF, AURA, Occitanie) = 68%.

Collected 2026-10-29 with plain HTTP (requests/curl, browser User-Agent; email for APIs joaoifodase@gmail.com). Scripts: scripts/other/fetchlib.py, captions.py, presgeo_redraw.py, presgeo_notes.py; crops via scripts/pdfpeek.py at 300 dpi.
