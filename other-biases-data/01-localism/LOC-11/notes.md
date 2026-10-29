# LOC-11 - Spain: El Salto (2023) 'El enclaustramiento de la universidad pública española' + ministry EPU tables

- **Citation:** Minguito Á., Borra A. (2023), El Salto, 29 Jan 2023. Primary: Ministerio de Ciencia, Innovación y Universidades, SIIU - Estadística de Personal de las Universidades (EPU), table PDITESIS.
- **url_used:** https://www.elsaltodiario.com/educacion/enclaustramiento-universidad-publica-espanola ; https://estadisticas.ciencia.gob.es/jaxiPx/files/_px/es/px/Universitaria/RRHH/PDITESIS/l0/px_rrhh_pditesis_tipo_centro_tot.px (+3 other PDITESIS tables)
- **access_status:** downloaded

## Headline number
El Salto: 72.94% of public-university teaching staff teach at the university where they read their thesis; 87.04% in the same region (2020-21). Ministry PDITESIS table: public universities 72.94% / 87.04% in 2020-21 (exact match); latest 2024-25: 72.77% / 86.58%; all universities 66.01% (2024-25).

**Key-number check:** **MATCH** (72.9%).

## Figures (PDF page of origin)
- `figures/LOC-11_redraw.png`: B/W redraw of the ministry series 2015-16 to 2024-25 (public universities)

## Data
data/*.px (PC-Axis originals) and their CSV conversions: national by type of university/centre, by staff type, by region (CCAA), by university; data/LOC-11.csv = public-university series. Indicator computed for presential universities (note in the PX file).

## Notes
Spain vs France: Spain's figure is a STOCK (all current staff); the French MESR rates (LOC-01..03) are FLOWS (new hires in a year: ~19-23% of MCF). Not directly comparable; a French stock measure is not published.

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
