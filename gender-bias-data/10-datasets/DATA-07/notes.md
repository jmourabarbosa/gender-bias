# DATA-07 — cleanBib

- **Title:** cleanBib — clean a .bib file and estimate gender (and race) balance of your reference list
- **Maintainers:** Dale Zhou, Jeni Stiso, Max Bertolero, Eli Cornblath, Erin Teich, Ann Sizemore Blevins, Kendra Oudyk, Cleanthis Michael, Anne Urai, Jordan Dworkin, Danielle Bassett et al. MIT licence.
- **url_used:** https://github.com/dalejn/cleanBib — `git clone --depth 1` at commit **1b4b52f806eee62ea593d4c29e485efdda13321b** (2026-09-21). The `.git` directory was removed so the copy does not become a nested repository.
- **Access status:** downloaded (code repository, 2.5 MB)
- **Files:** `data/cleanBib/` (README, `cleanBib.ipynb` notebook, `utils/`, `diversityStatement/` LaTeX template, `checkcites.lua`, `tests/`, `img/`). **Not executed** — run it on your own .bib (the notebook queries genderize.io / ethnicolr; a genderize API key may be needed for more than the free quota).

## Figure
- `figures/DATA-07_redraw.png` — the README's expected (benchmark) first/last-author gender categories for reference lists in the top-5 neuroscience journals.

## Benchmark values (README "Benchmark across neuroscience", from Dworkin et al. 2020, *Nat Neurosci*, DOI 10.1038/s41593-020-0658-y)
- Expected shares of references: woman/woman 6.7 %, man/woman 9.4 %, woman/man 25.5 %, man/man 58.4 % (Nature Neurosci, Neuron, Brain, J Neurosci, NeuroImage; 28,505 articles).
- Race benchmark (Bertolero et al. 2020): white/white 51.8 %, white/AoC 12.8 %, AoC/white 23.5 %, AoC/AoC 11.9 %.
