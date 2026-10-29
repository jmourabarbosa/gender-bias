# PRES-05: Systematic inequality and hierarchy in faculty hiring networks

- **Citation:** Clauset A, Arbesman S, Larremore DB (2015). Science Advances 1(1):e1400005. DOI 10.1126/sciadv.1400005 (PMC4644075)
- **url_used:** https://pmc-oa-opendata.s3.amazonaws.com/PMC4644075 (PMC OA bucket, first pass)
- **Access status:** downloaded
- **Headline number (from source):** PDF p.2: 'only 25% of institutions producing 71 to 86% of all tenure-track faculty'. Recomputed from Datasets 1-6 (in-sample PhD origins only, 'All others' vertex excluded): top 25% of institutions produce 71.2% (business), 78.3% (computer science), 85.7% (history).
- **Check vs key number:** MATCHES (71-86%; recomputation reproduces 71.2-85.7%)

## Files
- article.json
- article.xml
- data/PRES-05_lorenz.csv
- data/PRES-05_top25_share.csv
- source.pdf
- supplementary/1400005_Datasets.zip
- supplementary/1400005_SM.pdf
- supplementary/datasets/Dataset 1. Business_edgelist.txt
- supplementary/datasets/Dataset 2. Business_vertexlist.txt
- supplementary/datasets/Dataset 3. ComputerScience_edgelist.txt
- supplementary/datasets/Dataset 4. ComputerScience_vertexlist.txt
- supplementary/datasets/Dataset 5. History_edgelist.txt
- supplementary/datasets/Dataset 6. History_vertexlist.txt
- supplementary/supp_1_1_e1400005__index.html

## Figures extracted (with PDF page)
- figures/PRES-05_fig1.jpg: Fig. 1 prestige hierarchy network, computer science (PMC JPG; PDF p.2)
- figures/PRES-05_fig2.jpg: Fig. 2 inequality in faculty production, (A) Lorenz curves (PMC JPG; PDF p.2)
- figures/PRES-05_redraw.png: Lorenz curves recomputed from the paper's Datasets 1-6 (data/PRES-05_lorenz.csv, data/PRES-05_top25_share.csv)

## Notes
- supplementary/datasets/ = unzipped 1400005_Datasets.zip (edge lists u=PhD institution, v=hiring institution; vertex lists with prestige pi).
- The redraw counts, for each in-sample institution, the faculty (edges) it produced; top 25% = round(0.25 x n institutions).

Collected 2026-10-29 with plain HTTP (requests/curl, browser User-Agent; email for APIs joaoifodase@gmail.com). Scripts: scripts/other/fetchlib.py, captions.py, presgeo_redraw.py, presgeo_notes.py; crops via scripts/pdfpeek.py at 300 dpi.
