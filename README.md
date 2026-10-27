# Gender bias in academia: sources and data

Resources for a data-driven talk on gender bias in academia.

- **Browse:** `docs/index.html` (published with GitHub Pages) lists every source with its key number, access status, files, figures and data.
- **Slides:** plain black-and-white Google Slides deck built from these sources (link on the page).
- `SOURCES.md`: the annotated source list (126 sources, 10 sections); `sources.csv` is the same list as a table.
- `gender-bias-data/<section>/<ID>/`: one folder per source with `source.pdf` (or the saved page / full-text XML), `figures/` (paper figures and black-and-white redraws), `data/` (downloaded datasets and transcribed tables) and `notes.md` (citation, URL used, headline number checked against the key number).
- `gender-bias-data/manifest.csv`: one row per source with access status (`downloaded`, `abstract_only`, `paywalled`, `failed`).
- `deck/slides.json`: slide text, figures and sources used for the deck.

## Scripts

| Script | What it does |
|---|---|
| `scripts/parse_sources.py` | `SOURCES.md` → `sources.csv` and folder layout |
| `scripts/download.py <email> [ID ...]` | Unpaywall, PMC open-access bucket (PDF + figures), eLife API, publisher PDFs, landing pages |
| `scripts/build_manifest.py` | `_status/*.json` → `manifest.csv` |
| `scripts/build_site.py` | `docs/index.html` |
| `scripts/build_deck.py` | `deck/slides.json` → Google Slides API requests |

Paywalled papers were not downloaded and no bot checks were bypassed; those sources hold the abstract or landing page and are marked in the manifest.
