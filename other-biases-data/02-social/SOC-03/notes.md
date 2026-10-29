# SOC-03 - RERS 2025 (DEPP-SIES), fiche 7.16 'L'origine sociale des étudiants français'

- **Citation:** MENESR DEPP & SIES (2025), Repères et références statistiques 2025, chapitre 7, fiche 7.16, pp. 256-257.
- **url_used:** https://rers.depp.education.fr/data/2025/RERS.pdf (full volume, 470 pp.; fiche extracted to source_rers2025_fiche7-16.pdf)
- **access_status:** downloaded

## Headline number
2024-25, French students: 36.1% have cadre parents, 9.1% ouvrier parents; ENS 64.7% cadres / 1.9% ouvriers; university cursus licence -> doctorat: cadres 31.1% -> 41.6%, ouvriers 10.1% -> 3.9% (tables 1 and 3, fiche p.2 = RERS p.257).

**Key-number check:** Primary source for SOC-01/02: confirms the pattern (ENS cadres 64.7% vs SOC-02's 64.9%, ouvriers 1.9% vs 2.0%; small differences = different year/perimeter).

## Figures (PDF page of origin)
- `figures/SOC-03_fig1.png`: Table 1 (fiche p.2 = RERS PDF p.258): social origin by track, 2024-25
- `figures/SOC-03_fig2.png`: Table 3 (fiche p.2 = RERS PDF p.258): university students by sex and LMD level
- `figures/SOC-03_redraw.png`: B/W redraw: cadres/employés/ouvriers by LMD level

## Data
data/SOC-03.csv (table 3, LMD x sex); data/SOC-03_table1_filieres.csv (table 1); data/SOC-03_table2_disciplines.csv (table 2, by discipline, with headcounts). Transcribed from the PDF text layer.

## Notes
The education.gouv.fr RERS landing pages are behind Cloudflare (403) and education.gouv.fr does not resolve from this sandbox; the full volume came from rers.depp.education.fr. The XLSX per fiche could not be located (the RERS web app serves an SPA shell for guessed paths), so tables were transcribed from the PDF. The full 30 MB volume was not kept (only the 2-page fiche).

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
