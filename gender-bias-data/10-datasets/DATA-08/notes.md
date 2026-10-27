# DATA-08 — GCBI-alyzer (Fulvio & Postle)

- **Title:** GCBI-alyzer — Gender Citation Balance Index analyzer for reference lists (Journal of Cognitive Neuroscience)
- **Maintainers:** Jacqueline M. Fulvio & Bradley R. Postle (Univ. Wisconsin–Madison; JoCN editors). Related editorials: Fulvio, Akinnola & Postle (2021) "Gender (im)balance in citation practices in cognitive neuroscience", *J Cogn Neurosci* 33(1):3–7, DOI 10.1162/jocn_a_01643; Postle & Fulvio (2021/22) follow-up editorial (JoCN, proof at old.postlab.psych.wisc.edu/files/9316/3563/1172/JOCN-2021-0273_Proof_hi.pdf).
- **url tried:** https://psych.wisc.edu/gcbialyzer/ — curl fails TLS verification ("unable to get local issuer certificate": the server appears not to send its intermediate certificate); WebFetch reports the host is not in this session's allowed network domains. Old host https://old.postlab.psych.wisc.edu/gcbialyzer — connection reset through the egress proxy. TLS verification was **not** disabled.
- **Access status:** failed (page not saved). It is a web tool; there is no downloadable dataset.

## Base rates (NOT verified from the page — taken from a web-search summary of the tool page; re-check on the live page)
- Current version (updated spring 2025; JoCN authorship Jan 2009 – Dec 2024): **M/M 40.7 %, M/W 11.6 %, W/M 30.7 %, W/W 17.1 %** (first/last author gender).
- 2020 launch (2009 – July 2020): M/M 40.8 %, M/W 10.8 %, W/M 33.5 %, W/W 14.9 %.
- 2021 version: M/M 40.7 %, M/W 11.5 %, W/M 32.0 %, W/W 15.9 %.
- Neuroscience-wide comparison cited on the page (Dworkin et al. 2020): M/M 55.3 %, M/W 10.2 %, W/M 26.2 %, W/W 8.3 % (note: cleanBib README (DATA-07) quotes a different Dworkin breakdown, 58.4/9.4/25.5/6.7, which is the *expected* reference-list proportions. Check which one is meant before using).
- To fix: open https://psych.wisc.edu/gcbialyzer/ in a normal browser and save the page (or allow psych.wisc.edu in the session network settings).
