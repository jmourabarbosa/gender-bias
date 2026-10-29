# GEO-06: Assessing the effect of article processing charges on the geographic diversity of authors using Elsevier's 'Mirror Journal' system

- **Citation:** Smith AC, Merz L, Borden JB, Gulick CK, Kshirsagar AR, Bruna EM (2021). Quantitative Science Studies 2(4):1123-1143. DOI 10.1162/qss_a_00157; source.pdf = MetaArXiv preprint osf.io/s7cx4 ('Revision 2')
- **url_used:** https://osf.io/s7cx4/download
- **Access status:** downloaded
- **Headline number (from source):** Abstract (preprint p.3): 'Author Geographic Diversity of OA articles was significantly lower than that of non-OA articles. Most OA articles were written by authors in high-income countries, and there were no articles in Mirror journals by authors in low-income countries.' p.13: none of 975 Mirror articles and 0.15% of Parent articles had lead authors in low-income countries.
- **Check vs key number:** MATCHES (zero OA Mirror articles from low-income authors) - but see inconsistency note

## Files
- data/GEO-06.csv
- page.html
- source.pdf

## Figures extracted (with PDF page)
- figures/GEO-06_fig3.png: Figure 3 Geographic Diversity (D2) of authors, OA Mirror vs bootstrapped non-OA Parent (preprint PDF p.34)
- figures/GEO-06_table5.png: Table 5 % of articles by World Bank lending group, non-OA Parent vs OA Mirror (preprint PDF p.31)
- figures/GEO-06_redraw.png: first-author income group, non-OA Parent vs OA Mirror, from Table 5 (data/GEO-06.csv)

## Notes
- INCONSISTENCY in the preprint: Table 5 (p.31) lists 0.51% of first authors of OA Mirror articles in Low-income countries, contradicting the text. Check against the published QSS version (direct.mit.edu returned 403 to plain HTTP; the article is CC BY, so the user can download it in a browser).
- page.html = UF Geography news page (genuine).

Collected 2026-10-29 with plain HTTP (requests/curl, browser User-Agent; email for APIs joaoifodase@gmail.com). Scripts: scripts/other/fetchlib.py, captions.py, presgeo_redraw.py, presgeo_notes.py; crops via scripts/pdfpeek.py at 300 dpi.
