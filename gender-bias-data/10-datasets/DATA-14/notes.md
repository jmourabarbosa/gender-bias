# DATA-14 — OpenAlex (OurResearch)

- **Title:** OpenAlex — open bibliographic database and REST API (https://api.openalex.org), CC0 data.
- **Reference paper (first pass, `source.pdf`):** Rusti C, Hussain H, Ahrabian K, Pujara J, Percus AG, Nettasinghe B, Lerman K (2026). "The Tilted Playing Field for Women in Science". arXiv:2606.26469 (preprint, under review). Uses the OpenAlex bulk snapshot of 21 July 2025, papers 1980–2024 in the top-100 Google Scholar Metrics venues, ~5 M papers / 6.5 M authors / 65k institutions; author gender inferred from first names of OpenAlex author records.
- **Access status:** downloaded (reference preprint + ready-to-run query script). **The OpenAlex API pull itself was NOT done:** every request returned `"Rate limit exceeded … no API key … free daily budget shared by everyone on your network's IP address … used up (resets at midnight UTC)"`. I did not create an API key on the user's behalf (OpenAlex keys are free: https://help.openalex.org/api/authentication/).
- **Script:** `scripts/openalex_neuro_sample.py OUTDIR` (repo root). It:
  1. resolves source IDs for Nature Neuroscience, Neuron, Brain, J Neurosci, NeuroImage, eLife via `GET /sources?search=<name>`;
  2. counts research articles per year: `GET /works?filter=primary_location.source.id:<Sxxxx>,type:article,publication_year:2000-2025&group_by=publication_year`;
  3. pulls first/last-author names, OpenAlex author IDs and countries for J Neurosci 2015 and 2024 (≤1000 articles each) with cursor paging: `GET /works?filter=primary_location.source.id:<Sxxxx>,type:article,publication_year:<yr>&per-page=200&cursor=*&select=id,doi,publication_year,authorships,cited_by_count`.
  Add `api_key=<key>` (or `mailto` once the shared budget resets) and rerun; then join first names to a gender-inference tool (genderize.io / NamSor / gender-guesser) with a probability threshold (e.g. ≥0.7 as in GCBI-alyzer) to rebuild authorship or citation shares.
- **Headline number:** n.a. (tool / data source).
