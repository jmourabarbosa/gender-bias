"""Fetch She Figures indicators hosted in EIGE's Gender Statistics Database via the public JSON
endpoint the site itself uses: https://eige.europa.eu/gender-statistics/dgs/json/db-data?path=...
  path=indicator/<indicator_id>                       -> metadata (dataset criteria + categories)
  path=indicator-data/<data_set>/<crit>:<cat>/...     -> rows {geo, year, value, flag}
Loops over every criteria-category combination and labels rows with them.
Usage: fetch_eige_shefigures.py IDS_FILE OUTDIR"""
import sys, json, csv, time, os, itertools, urllib.parse, requests
ids_file, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
S = requests.Session(); S.headers['User-Agent'] = 'gender-bias-source-collector/1.0 (mailto:joaoifodase@gmail.com)'
EP = 'https://eige.europa.eu/gender-statistics/dgs/json/db-data?path='
get = lambda p: S.get(EP + urllib.parse.quote(p, safe=''), timeout=120).json()
index = []
for ind in open(ids_file).read().split():
    meta = get('indicator/' + ind); dv, ds = meta['datasetView'], meta['dataset']
    name = ds['_id']; crit = ds.get('criteria', [])
    out = []
    for combo in itertools.product(*[[c['code'] for c in cr['categories']] for cr in crit]):
        path = '/'.join(['indicator-data/' + name] + [f"{cr['code']}:{v}" for cr, v in zip(crit, combo)])
        rows = get(path) or []
        for r in rows:
            r.update({cr['code']: v for cr, v in zip(crit, combo)}); out.append(r)
        time.sleep(0.2)
    cols = ['geo', 'year'] + [cr['code'] for cr in crit] + ['value', 'flag']
    cols += sorted({k for r in out for k in r} - set(cols))
    with open(f'{outdir}/{name}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
    json.dump(meta, open(f'{outdir}/{name}.meta.json', 'w'), indent=1)
    index.append((name, ind, dv.get('name'), dv['units'][0]['name'] if dv.get('units') else '', len(out), ds.get('value_count'), ';'.join(cols)))
    print(name, len(out), ds.get('value_count'), flush=True)
with open(f'{outdir}/_index.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['data_set', 'eige_indicator_id', 'name', 'unit', 'n_rows', 'eige_value_count', 'columns']); w.writerows(index)
