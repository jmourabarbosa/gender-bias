"""OpenAlex example pull for DATA-14: neuroscience journals -> yearly work counts + first/last author sample.
Usage: openalex_neuro_sample.py OUTDIR"""
import sys, os, csv, json, time, requests
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
S = requests.Session(); S.headers['User-Agent'] = 'gender-bias-source-collector/1.0 (mailto:joaoifodase@gmail.com)'
API = 'https://api.openalex.org'; M = {'mailto': 'joaoifodase@gmail.com'}
journals = ['Nature Neuroscience', 'Neuron', 'Brain', 'The Journal of Neuroscience', 'NeuroImage', 'eLife']
src = {}
for j in journals:
    r = S.get(f'{API}/sources', params={**M, 'search': j, 'per-page': 5}).json()['results']
    best = next((x for x in r if x['display_name'].lower() == j.lower()), r[0])
    src[j] = (best['id'].split('/')[-1], best['display_name'], best.get('issn_l'))
    time.sleep(0.2)
json.dump(src, open(f'{out}/sources.json', 'w'), indent=1)
with open(f'{out}/works_per_year.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['journal', 'source_id', 'year', 'n_articles'])
    for j, (sid, name, issn) in src.items():
        r = S.get(f'{API}/works', params={**M, 'filter': f'primary_location.source.id:{sid},type:article,publication_year:2000-2025', 'group_by': 'publication_year'}).json()
        for g in sorted(r['group_by'], key=lambda g: g['key']): w.writerow([name, sid, g['key'], g['count']])
        time.sleep(0.2)
# first/last author sample: J Neurosci 2015 and 2024, up to 1000 research articles each
sid = src['The Journal of Neuroscience'][0]
with open(f'{out}/jneurosci_first_last_authors_2015_2024.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['work_id', 'doi', 'year', 'n_authors', 'first_author', 'first_author_id', 'first_country', 'last_author', 'last_author_id', 'last_country', 'cited_by_count'])
    for yr in (2015, 2024):
        cursor, n = '*', 0
        while cursor and n < 1000:
            r = S.get(f'{API}/works', params={**M, 'filter': f'primary_location.source.id:{sid},type:article,publication_year:{yr}', 'per-page': 200, 'cursor': cursor, 'select': 'id,doi,publication_year,authorships,cited_by_count'}).json()
            for x in r['results']:
                a = x['authorships']
                if not a: continue
                fa, la = a[0], a[-1]
                w.writerow([x['id'].split('/')[-1], x.get('doi'), x['publication_year'], len(a), fa['author'].get('display_name'), (fa['author'].get('id') or '').split('/')[-1], ';'.join(fa.get('countries') or []),
                            la['author'].get('display_name'), (la['author'].get('id') or '').split('/')[-1], ';'.join(la.get('countries') or []), x.get('cited_by_count')])
                n += 1
            cursor = r['meta'].get('next_cursor'); time.sleep(0.2)
        print(yr, n)
print(src)
