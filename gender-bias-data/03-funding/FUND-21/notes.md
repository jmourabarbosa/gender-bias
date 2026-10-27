# FUND-21 — NIH Data Book: success rates by sex

- **Citation:** NIH Office of Extramural Research, NIH Data Book (RePORT), reports 131 and 132, updated March 2026.
- **url_used:** API https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=132 (RPG applications/awards/success rate by sex, FY1998-2025) and reportId=131 (R01-equivalent success by sex and type); metadata https://report.nih.gov/reportweb/api/report/Get/<id>. Script: scripts/collect/nih_databook.py. NOTE: the listed link displayreport?rId=1005 redirects to a 2007 PDF 'Women supported by Kirschstein-NRSA training grants and fellowships' (kept as source.pdf), not a funding-rate report.
- **Access status:** downloaded

## Files
- `data/nih_databook_report131.csv`
- `data/nih_databook_report131.json`
- `data/nih_databook_report132.csv`
- `data/nih_databook_report132.json`
- `figures/FUND-21_redraw.png`
- `notes.md`
- `source.pdf`

## Figures
- FUND-21_redraw.png = RPG success rate by sex FY1998-2025 from data/nih_databook_report132.csv.

## Headline number
- RPG success rate FY2024: women 20% (3,898/19,426) vs men 18% (6,077/33,710); FY1998: 30% vs 32%. FY2025: 14% vs 13%.
- Key number in SOURCES.md: check → **n.a. (no number given); LINK MISMATCH: rId=1005 is the 2007 NRSA report**
