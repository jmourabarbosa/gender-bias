# NEURO-15: BiasWatchNeuro

- **Citation:** BiasWatchNeuro (2015-2023). Blog tracking speaker gender ratios at neuroscience meetings.
- **url_used:** https://biaswatchneuro.com ; posts via WordPress.com public REST API https://public-api.wordpress.com/wp/v2/sites/biaswatchneuro.com/posts?per_page=100&page=1..8 (site-local /wp-json returns 404)
- **Access status:** downloaded
- **Files:** api/posts_all.json, page.html
- **Figures:** figures/NEURO-15_redraw.png
- **Data:** ../../../data/biaswatchneuro.csv

**Headline number (from source):** 740 posts (Aug 2015 - Sep 2023); 676 parsed into data/biaswatchneuro.csv; pooled share of women among listed speakers 3859/11720 = 32.9%; 274 of 657 events with a base rate were below their estimated base rate.

**Key number in SOURCES.md check:** n.a.

**Notes:** Key number is descriptive; per-post ratio line chosen by label priority (overall/invited speakers over keynote-only); 6 rows flagged where the site's own % disagrees with its counts (e.g. AI & Brain Science 2020 lists 19 W : 7 M (27%) - probably swapped). 64 posts had no ratio line (essays, screenshot-only).

Parser: scripts/biaswatchneuro_scrape.py; raw API dump api/posts_all.json; redraw by post year in figures/NEURO-15_redraw.png (year = post date, not meeting date).
