# PREC-13: Changes in the National Cancer Institute's R01 workforce: growth, aging, retention, and policy implications

- **Citation:** Antman KH et al. (2021). J Clin Invest 131(7):e146925. doi:10.1172/JCI146925 (PMC8011905).
- **url_used:** https://jci.org/articles/view/146925/files/pdf (served from dm5migu4zj3pb.cloudfront.net JCI146925.v1.pdf); supplement JCI146925.sd.pdf
- **Access status:** downloaded
- **Key number (list):** Age at first R01 36.2 -> 44.9
- **Headline number found:** "the age of PIs with PhDs at the time of first NCI R01 award increased from an average of 36.2 years in FY 1990 to 44.9 years in FY 2016. Likewise, the median age increased from 36 to 43 years" (PDF p5).
- **Check:** MATCH

## Files
- data/PREC-13.csv
- page.html
- source.pdf
- supplementary/JCI146925.sd.pdf

## Figures
| File | From (PDF page) |
|---|---|
| figures/PREC-13_fig1.png | supplementary/JCI146925.sd.pdf p3 (full rotated page): Suppl. Fig. 3, age at first R01 1990-2016 |
| figures/PREC-13_fig2.png | source.pdf p3: Figure 2, age distribution of NCI PIs 1990-2016 |
| figures/PREC-13_redraw.png | data/PREC-13.csv (medians read from Suppl. Fig. 3) |

## Notes
The JCI PDF first returned "website under heavy load (queue full)" (503); a later single retry succeeded. PMC and Europe PMC PDF routes return reCAPTCHA/Cloudflare challenges and were not used. figures/JCI146925.*.jpg are the journal's "large" web figure images (full set incl. tables).

Scripts: scripts/other/pd_fetch.py (downloads), scripts/collect/figtools.py (crops), scripts/other/pd_redraw.py (redraws), scripts/other/pd_notes.py (this file).
