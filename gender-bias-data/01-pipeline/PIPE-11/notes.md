# PIPE-11 — OECD *Education at a Glance 2025*, indicator D5 (academic staff)

- **Title:** Education at a Glance 2025: OECD Indicators — Indicator D5 "How do academic staff profiles and institutional characteristics shape tertiary education?"
- **Citation:** OECD (2025). *Education at a Glance 2025: OECD Indicators*. Paris: OECD Publishing. https://doi.org/10.1787/1c0d9c79-en
- **url_used (data):** OECD Data Explorer SDMX API, dataflow `OECD.EDU.IMEP:DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_SEX(1.1)` "Share of teachers by gender and age range":
  `https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_SEX,1.1/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels`
- **Access status:** downloaded (data). **The chapter text / StatLink Excel files were NOT obtained**: oecd-ilibrary.org and oecd.org publication pages returned a Cloudflare "Just a moment..." challenge (HTTP 403); not bypassed. So Fig. D5.5 / Table D5.3 themselves are not cropped — redrawn from the same underlying UOE data instead.
- **Files:**
  - `data/oecd_DF_UOE_NF_PERS_SEX_all.csv.gz` — full dataflow, all ISCED levels (131 MB raw, gzipped to 2 MB)
  - `data/oecd_women_share_academic_staff_tertiary.csv` — filtered: EDUCATION_LEV in {ISCED11_5 short-cycle, ISCED11_5T8 tertiary, ISCED11_6T8 bachelor-doctoral}, non-empty values. Columns: REF_AREA, Reference area, EDUCATION_LEV, Education level, MEASURE (TEACH = classroom teachers/academic staff), UNIT_MEASURE (PT_ST_SUB = % of staff in same subgroup), SEX (F/M), AGE (_T total or age band), Age, TIME_PERIOD (2013–2024), OBS_VALUE (%), OBS_STATUS. Countries: 43 + OECD, EU25, G20 aggregates.

## Figures
- `figures/PIPE-11_redraw_trend.png` — % women among tertiary academic staff (ISCED 5–8), 2013–2024: OECD average, EU25, France, USA (≈ Fig. D5.5 trend).
- `figures/PIPE-11_redraw_age.png` — OECD average % women by age band, 2023 (≈ Table D5.3 by age): <30 52.1 %, 30–34 49.0 %, 50–54 47.8 %, 55–59 45.3 %, 60–64 40.7 %, 65+ 31.3 %.
- Caveat: OECD/EU "averages" in this dataflow are unweighted means over countries with data in that year/age band, so composition changes (e.g. the 2019 dip) are partly artefacts.

## Headline number
- From the data: OECD average share of women among tertiary academic staff = **46.1 % (2023)**, 46.3 % (2024); EU25 46.9 % (2023); France 43.0 % (2023); USA 51.7 % (2023).
- Key number "Women 46% of academic staff" → **MATCHES** (EAG 2025 reference year presumably 2023 → 46 %). Verified from the database, not from the chapter text (blocked).
