# LOC-03 - MESR-DGRH trajectory notes, recruits 2018-2022 (series)

- **Citation:** MESR-DGRH, Notes de la DGRH: n°8 juillet 2019 (recrutés 2018); n°7 septembre 2020 (2019); n°8 septembre 2021 (2020); n°8 septembre 2022 (2021); n°7 septembre 2023 (2022).
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2022-12/note-dgrh-n8-septembre-2022--trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2021-25546.pdf (+ 4 other editions, URLs below)
- **access_status:** downloaded

## Headline number
Series of endo-recruitment rates, recruits 2018-2024: MCF 18, 17, 20, 18, 19, 19, 23%; PR 45, 41, 47, 46, 57, 54, 54%. Foreign MCF 14, 16, 18, 20, 23, 18.5, 23.5%; foreign PR 12, 11, 12, 11, 10, 11, 7.9%. See data/local_hiring_series.csv for page refs.

**Key-number check:** 'Series' - no single key number; series assembled for 2018-2024 (7 editions incl. LOC-01 and LOC-02).

## Figures (PDF page of origin)
- `figures/LOC-03_fig1.png`: 2018 note, Figure 3, PDF p.3 (néo/endo/mutation by discipline, 2018)
- `figures/LOC-03_fig2.png`: 2019 note, Figure 4, PDF p.3 (endo-recruitment by discipline 2008-2019, trend)
- `figures/LOC-03_fig3.png`: 2020 note, Figure 4, PDF p.3 (by discipline, 2020)
- `figures/LOC-03_fig4.png`: 2021 note (source.pdf), Figure 4, PDF p.3 (by discipline, 2021)
- `figures/LOC-03_fig5.png`: 2021 note (source.pdf), Figure 5, PDF p.3 (endo-recruitment by discipline 2015-2021)
- `figures/LOC-03_fig6.png`: 2022 note, Figure 4, PDF p.3 (by discipline, 2022)
- `figures/LOC-03_redraw.png`: B/W redraw of the 2018-2024 series (data/local_hiring_series.csv)

## Data
data/local_hiring_series.csv (year, n recruited, MCF and PR endo %, PR scope, MCF/PR foreign %, source note, file, pages; 2023 and 2024 from LOC-02/LOC-01); data/local_hiring_by_discipline.csv (néo/endo/mutation % by corps x discipline group, 2018-2024, read from the labelled bars).

## Notes
Files: source.pdf = 2021 recruits (n°8 sept 2022); series/dgrh_trajectoire_recrutes_2018.pdf (https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2022-01/note-dgrh-n-8-juillet-2019---campagne-2018-16084.pdf), _2019.pdf (.../2022-01/note-dgrh-n-7-septembre-2020---campagne-2019-16078.pdf), _2020.pdf (.../2022-01/note-dgrh-n-8-septembre-2021---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2020-16072.pdf), _2022.pdf (.../2023-11/note-dgrh-n-7-septembre-2023---trajectoire-professionnelle-des-enseignants-chercheurs-recrut-s-en-2022-pdf-30093.pdf). Despite the 'campagne' file names, the 2018/2019 PDFs are the trajectory notes (titles checked p.1).

**Comparability caveats.** (1) The PR rate includes agrégés du supérieur in 2018-2019 and 2022-2024 but EXCLUDES them in 2020-2021 (notes say 'calculé hors agrégés'), so the 2021->2022 jump (46->57%) is partly a scope change. (2) From 2022 the notes include art. 46-3 recruitments. (3) 2019: summary p.1 and fig. 3 say MCF 17%, body text p.2 says 18% (internal inconsistency; CSV uses 17). (4) Foreign shares were revised later: LOC-01 fig. 6 gives MCF 17.5% / PR 10.0% for 2020 vs 18% / 12% in the 2020 note (PR excl. agrégés); the CSV keeps the value published in each year's note. MESR HTML landing pages return a Cloudflare challenge (not bypassed); the PDFs download directly with a browser UA.

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
