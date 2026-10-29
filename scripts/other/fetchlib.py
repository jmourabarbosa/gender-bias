"""Plain-HTTP helpers for PRES/GEO collection. Usage:
  python3 -I fetchlib.py pmc PMCID OUTDIR
  python3 -I fetchlib.py get URL OUTFILE
  python3 -I fetchlib.py unpaywall DOI
  python3 -I fetchlib.py idconv DOI
"""
import sys, re, json, requests
from pathlib import Path
from urllib.parse import quote

EMAIL = "joaoifodase@gmail.com"
BROWSER = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
H = {"User-Agent": BROWSER, "Accept": "*/*", "Accept-Language": "fr,en;q=0.8"}
S3 = "https://pmc-oa-opendata.s3.amazonaws.com"


def get(url, **kw):
    try:
        r = requests.get(url, headers=H, timeout=90, allow_redirects=True, **kw)
        print(r.status_code, r.headers.get("content-type"), len(r.content), r.url, file=sys.stderr)
        return r if r.status_code == 200 and r.content else None
    except requests.RequestException as e:
        print("ERR", e, file=sys.stderr)
        return None


def fetch_pmc(pmc, out):
    out = Path(out)
    r = get(f"{S3}/?list-type=2&prefix={pmc}.")
    keys = re.findall(r"<Key>([^<]+)</Key>", r.text) if r else []
    if not keys:
        print("no keys"); return False
    latest = sorted({k.split("/")[0] for k in keys}, key=lambda v: int(v.split(".")[-1]))[-1]
    for k in keys:
        if not k.startswith(latest + "/"):
            continue
        name = k.split("/")[1]
        if name.endswith((".jpg", ".gif", ".png", ".tif")):
            dest = out / "figures" / name
        elif name == f"{latest}.pdf":
            dest = out / "source.pdf"
        elif name.endswith((".xml", ".json")):
            dest = out / ("article" + Path(name).suffix)
        elif name.endswith(".txt"):
            continue
        else:
            dest = out / "supplementary" / name
        if dest.exists():
            continue
        f = get(f"{S3}/{k}")
        if f:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(f.content)
            print("saved", dest)
    return (out / "source.pdf").exists()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pmc":
        print(fetch_pmc(sys.argv[2], sys.argv[3]))
    elif cmd == "get":
        r = get(sys.argv[2])
        if r:
            Path(sys.argv[3]).write_bytes(r.content); print("saved", sys.argv[3], r.content[:5])
    elif cmd == "unpaywall":
        r = get(f"https://api.unpaywall.org/v2/{sys.argv[2]}?email={EMAIL}")
        if r:
            j = r.json()
            print(json.dumps({"title": j.get("title"), "is_oa": j.get("is_oa"), "best": j.get("best_oa_location"),
                              "locs": [(l.get("url_for_pdf"), l.get("url")) for l in j.get("oa_locations", [])]}, indent=1))
    elif cmd == "idconv":
        r = get(f"https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={quote(sys.argv[2])}&format=json&tool=other-biases&email={EMAIL}")
        print(r.text if r else None)
