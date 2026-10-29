# NAT-10: Author-reviewer homophily in peer review (eLife)

- **Citation:** Murray D., Siler K., Larivière V., Chan W. M., Collings A. M., Raymond J., Sugimoto C. R. (2019). "Author-Reviewer Homophily in Peer Review". *bioRxiv* 400515, v3 (4 Aug 2019; v1 29 Aug 2018). DOI 10.1101/400515. Not published in a journal (bioRxiv API: published = NA). Data: 23,876 initial and 7,192 full submissions to eLife, 2012-2017.
- **url_used:**
  - page.html: https://elifesciences.org/inside-elife/f3645452/meta-research-researchers-study-implicit-bias-in-peer-review (eLife "Inside eLife" summary, 21 Sep 2018)
  - biorxiv_api.json: https://api.biorxiv.org/details/biorxiv/10.1101/400515 (metadata and full abstract for v1-v3)
- **Access status:** abstract_only. The preprint PDF and JATS XML on www.biorxiv.org (v1-v3 .full.pdf and .source.xml) returned HTTP 429 "error code: 1015" (Cloudflare rate limit) on every try in this session, including the first pass. Not retried aggressively and not bypassed. Europe PMC (PPR54230) has no full text.
- **Headline number found (page.html):** initial submissions with a corresponding author in the United States were most likely to be encouraged for in-depth review (39.2%), and those with a corresponding author in China the least (12.6%). Gender: 30.6% (male) vs 28.6% (female) encouraged; accept rate 15.4% vs 13.6%. The abstract (biorxiv_api.json) reports acceptance-rate homophily for country and gender.
- **Key number check (39.2% US vs 12.6% China sent to full review):** MATCH (from the eLife summary; the encourage-rate-by-country figure in the preprint itself was not retrieved).
- **To do by the user:** download https://www.biorxiv.org/content/10.1101/400515v3.full.pdf in a browser and crop the encourage-rate-by-country figure.

## Figures

| File | From | Page |
|---|---|---|
| figures/NAT-10_redraw.png | redraw of data/NAT-10.csv (encourage rates from the eLife summary) | n/a (web page) |

## Data

- data/NAT-10.csv: encourage rates by country and gender of the corresponding author (page.html).
