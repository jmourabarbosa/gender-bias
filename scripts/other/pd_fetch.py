"""Fetch helpers for PREC/DIS. usage:
  python3 -I pd_fetch.py pmcid <doi>
  python3 -I pd_fetch.py pmc <ID> <PMCid>          -> PMC OA bucket PDF/XML/figures into the ID folder
  python3 -I pd_fetch.py unpaywall <doi>
  python3 -I pd_fetch.py get <url> <dest> [browserUA]
"""
import sys, re, json, glob, os
from pathlib import Path
from urllib.parse import quote
import requests
ROOT = Path('/home/user/gender-bias'); EMAIL = 'joaoifodase@gmail.com'
S3 = "https://pmc-oa-opendata.s3.amazonaws.com"
UA = {"User-Agent": f"Mozilla/5.0 (compatible; gender-bias-sources; mailto:{EMAIL})"}
BUA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
       "Accept": "text/html,application/pdf,*/*", "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"}
def get(url, browser=False):
    r = requests.get(url, headers=BUA if browser else UA, timeout=120, allow_redirects=True)
    return r
def folder(i): return Path(glob.glob(f'{ROOT}/other-biases-data/*/{i}')[0])
cmd = sys.argv[1]
if cmd == 'pmcid':
    r = get(f"https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={quote(sys.argv[2])}&format=json&tool=gender-bias&email={EMAIL}")
    print(r.json()['records'][0])
elif cmd == 'unpaywall':
    j = get(f"https://api.unpaywall.org/v2/{sys.argv[2]}?email={EMAIL}").json()
    print(j.get('is_oa'), j.get('oa_status'))
    for l in j.get('oa_locations') or []: print(' ', l.get('url_for_pdf'), l.get('url'), l.get('version'), l.get('host_type'))
elif cmd == 'pmc':
    out = folder(sys.argv[2]); pmc = sys.argv[3]
    keys = re.findall(r"<Key>([^<]+)</Key>", get(f"{S3}/?list-type=2&prefix={pmc}.").text)
    if not keys: sys.exit('no keys')
    latest = sorted({k.split("/")[0] for k in keys}, key=lambda v: int(v.split(".")[-1]))[-1]
    for k in keys:
        if not k.startswith(latest + "/"): continue
        name = k.split("/")[1]
        if name.endswith((".jpg", ".gif", ".png", ".tif")): dest = out / "figures" / name
        elif name == f"{latest}.pdf": dest = out / "source.pdf"
        elif name.endswith((".xml", ".json")): dest = out / ("article" + Path(name).suffix)
        elif name.endswith(".txt"): continue
        else: dest = out / "supplementary" / name
        if dest.exists(): continue
        f = get(f"{S3}/{k}")
        if f.status_code == 200:
            dest.parent.mkdir(exist_ok=True); dest.write_bytes(f.content); print('saved', dest.relative_to(ROOT))
    print('latest', latest)
elif cmd == 'get':
    r = get(sys.argv[2], browser=len(sys.argv) > 4)
    ct = r.headers.get('content-type', '')
    print(r.status_code, ct, len(r.content), r.url, r.content[:5])
    if r.status_code == 200 and r.content:
        Path(sys.argv[3]).parent.mkdir(parents=True, exist_ok=True)
        Path(sys.argv[3]).write_bytes(r.content); print('saved', sys.argv[3])
