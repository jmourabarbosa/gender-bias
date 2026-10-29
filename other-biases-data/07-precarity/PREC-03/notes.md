# PREC-03: La campagne de recrutement et d'affectation des MCF et des PR - Session 2023 (Note de la DGRH n°2-2025) + all campaign reports back to 2008

- **Citation:** MESR-DGRH (M. Le Gendre), Note de la DGRH n°2-2025, Oct 2025; series of DGRH campaign reports 2006-2026 (series/).
- **url_used:** https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2025-10/note-dgrh-n-2---2025---campagne-2023-pdf-38079.pdf
- **Access status:** downloaded
- **Key number (list):** 1,567 MCF posts, 8,110 candidates
- **Headline number found:** 2023: 1,567 MCF posts published, 49,141 applications by 8,110 candidates, 5.2 candidates per post (p2 and fig.2 table p2); 2,280 posts published, 2,378 authorised (p1).
- **Check:** MATCH

## Files
- data/posts_candidates_series.csv
- series/bilan-provisoire-2022.pdf
- series/bilan-provisoire-2024.pdf
- series/bilan-provisoire-2025.pdf
- series/bilan1998-2007_bilrec072.pdf
- series/bilan_bilrec061.pdf
- series/campagne2011_bilan.pdf
- series/campagne2013_bilrec13.pdf
- series/campagne2014_bilan.pdf
- series/campagne2015_note-dgrh-n5-2016.pdf
- series/campagne2016_note-dgrh-n6-2017.pdf
- series/campagne2017_note-dgrh-n6-2018.pdf
- series/campagne2018_note-dgrh-n7-2019.pdf
- series/campagne2020_note-dgrh-n7-2021_univ-lorraine-copy.pdf
- series/campagne2024_note-dgrh-n1-2026.pdf
- series/candidatures2008_bilcandrec08.pdf
- series/trajectoire2015_note-dgrh-n6-2016.pdf
- series/trajectoire2019_note-dgrh-n7-2020.pdf
- source.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-03_fig1.png | PDF p1: fig.1 posts authorised/published/filled 2014-2023 |
| figures/PREC-03_fig2.png | PDF p2: fig.2 table posts, applications, candidates by discipline 2023 |
| figures/PREC-03_redraw.png | data/posts_candidates_series.csv |

## Notes
SERIES (data/posts_candidates_series.csv; year, MCF posts, PR posts, total published, authorised, MCF candidates, candidates per MCF post, status, basis, source+page). Files in series/: campaign reports 2011 (bilan, 103 p), 2013 (bilrec13, 98 p; holds 2004-2013 posts chart p10 and candidate changes 2007-2013 p12), 2014 (bilan), 2015 (Note n°5-2016), 2016 (Note n°6-2017), 2017 (Note n°6-2018), 2018 (Note n°7-2019), 2020 (Note n°7-2021, copy hosted by Université de Lorraine), 2024 (Note n°1-2026), provisional bilans 2022/2024/2025, plus 2006/2007 bilans and the 2008 candidate study. 2021 = PREC-04, 2023 = this source. trajectoire*.pdf are the companion "trajectoire professionnelle" notes (2015, 2019), downloaded by mistake but kept (previous status of recruits, useful for PREC-05).
Gaps and caveats: (1) no separate campaign PDFs found for 2008, 2009, 2010, 2012 (their posts come from the 2013 report chart labels, their candidate counts are back-computed from the year-on-year changes printed in the 2011/2013 reports; the back-computed 2010-2012 ratios reproduce the official 5.08/5.52/5.53, which validates the method); (2) 2019 and 2022 final campaign notes (Notes d'information DGRH 20-06 and 23-06) are listed on the ministry site but the site's HTML pages are behind a Cloudflare block for this client and no PDF URL could be found, so 2019 has no candidate figure and 2022 uses the provisional July bilan (6.1); 2019/2022 posts and 2014/2022 authorised posts were read from the vector lines of fig.1 of the 2023 note (script scripts/other/prec03_fig1_vector.py; it reproduces the stated values for 2015, 2016, 2019, 2022 exactly); (3) the post base of the official ratio changes: 2014-2015 use synchronised-session posts only (on all published posts the ratio would be 6.4 and 6.9), 2018 excludes art. 29 posts.

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
