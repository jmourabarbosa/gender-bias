# DATA-06 — Nature Index author gender ratio

- **Title:** Nature Index — Author gender ratio (author positions by topic; subjects and research topics)
- **Maintainer:** Springer Nature (Nature Index). Data are for the 2025 index year (page text: "top 50 topics by total authorships in the Nature Index in 2025"; gender inferred from first name, last name and country by an algorithm; counts authorship instances, not individuals). Licence shown on page: CC (see page footer).
- **Pages (saved, valid):** `page.html` = https://www.nature.com/nature-index/author-gender-ratio/author-position-by-topic ; `page1.html` = https://www.nature.com/nature-index/author-gender-ratio/subjects-and-topics
- **url_used (data):** the pages' own JSON endpoints (named in the pages' inline scripts), fetched with plain GET — no headless browser needed:
  - https://www.nature.com/nature-index/gender-ratio-author-position-by-topic-api → `data/gender-ratio-author-position-by-topic-api.{json,csv}` (124 topics; columns topic, proportion_first_female, proportion_last_female)
  - https://www.nature.com/nature-index/gender-ratio-by-research-topic-api → `data/gender-ratio-by-research-topic-api.{json,csv}` (70 topics; topic_name, proportion_of_female_authorship)
  - https://www.nature.com/nature-index/gender-ratio-by-subject-api → `data/gender-ratio-by-subject-api.{json,csv}` (8 subjects; subject, proportion_of_female_authorship)
  - (one request got HTTP 429 rate-limit; succeeded after a pause.)
- **Access status:** downloaded

## Figure
- `figures/DATA-06_redraw.png` — % female first vs last authorships for Neurosciences and comparison topics (grey bars).

## Headline values (Nature Index 2025)
- **Neurosciences: 41.8 % of first authorships, 28.5 % of last authorships** female; 41.6 % of all authorships.
- All subjects: 32.2 % female authorship; Health Sciences 40.7 %, Physical Sciences 26.2 %.
