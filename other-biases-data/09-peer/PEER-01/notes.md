# PEER-01 - NeurIPS 2021 consistency experiment

- **Citation:** Beygelzimer A., Dauphin Y.N., Liang P., Wortman Vaughan J. (2023), "Has the Machine Learning Review Process Become More Arbitrary as the Field Has Grown? The NeurIPS 2021 Consistency Experiment", arXiv:2306.03262. Blog post: NeurIPS Program Chairs, 8 Dec 2021.
- **url_used:** https://blog.neurips.cc/2021/12/08/the-neurips-2021-consistency-experiment (page.html, first pass) ; https://arxiv.org/pdf/2306.03262 (source.pdf)
- **access_status:** downloaded

## Headline number
882 duplicated papers; 203 (23.0%) accepted by only one committee (random baseline 35.1%). 50.6% of papers accepted by one committee were rejected by the other (2014: 49.5%); 14.9% of rejected papers would have been accepted (blog; paper PDF p.4 Table 1, p.6 text).

**Key-number check:** **MATCH** (50.6%).

## Figures (PDF page of origin)
- `figures/PEER-01_fig1.png`: Table 1, PDF p.4: 5x5 recommendation table (oral/spotlight/poster/reject/withdrawn) for the two committees.
- `figures/PEER-01_fig2.png`: Figure 3, PDF p.7: fraction of accepted papers rejected by the other committee vs acceptance rate (random baseline line).
- `figures/PEER-01_redraw.png`: B/W 2x2 decision table (data/PEER-01.csv).
- `figures/web_*.png`: the three images embedded in the blog post (results table and two threshold plots), kept for reference.

## Data
- `data/PEER-01_table1_5x5.csv`: Table 1 transcribed (rows = original committee, columns = copy).
- `data/PEER-01.csv`: 2x2 aggregation (accept = oral+spotlight+poster; reject = reject+withdrawn): 99 / 107 / 96 / 580 (n = 882). Checks: 206 and 195 accepts, 203 inconsistent, (107/206 + 96/195)/2 = 50.6%.
