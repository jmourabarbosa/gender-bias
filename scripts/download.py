"""Download every source in sources.csv into gender-bias-data/<section>/<ID>/.

Per source, in order:
  1. PMC open-access bucket (s3://pmc-oa-opendata): PDF, XML and every figure image
  2. eLife API: PDF and figure images (IIIF)
  3. Unpaywall: every OA location with a PDF
  4. PDF-looking links in the entry, arXiv/bioRxiv, PLoS printable
  5. Landing pages (saved as page*.html), then their citation_pdf_url
Sites that answer with a bot challenge are recorded as failed, not worked around.
Usage: python3 scripts/download.py <email> [ID ...]
"""
import csv, json, re, sys, concurrent.futures as cf
from pathlib import Path
from urllib.parse import urljoin, quote
import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "gender-bias-data"
EMAIL = sys.argv[1] if len(sys.argv) > 1 else "research@example.org"
UA = {"User-Agent": f"Mozilla/5.0 (compatible; gender-bias-sources; mailto:{EMAIL})", "Accept": "*/*"}
OVERRIDES = json.loads((ROOT / "scripts" / "doi_overrides.json").read_text())
S3 = "https://pmc-oa-opendata.s3.amazonaws.com"


def get(url, **kw):
    try:
        r = requests.get(url, headers=UA, timeout=90, allow_redirects=True, **kw)
        return r if r.status_code == 200 and r.content else None
    except requests.RequestException:
        return None


def is_pdf(r):
    return r is not None and r.content[:5] == b"%PDF-"


def pmcid_for(doi):
    r = get(f"https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={quote(doi)}&format=json&tool=gender-bias&email={EMAIL}")
    try:
        return r.json()["records"][0].get("pmcid") if r else None
    except (ValueError, KeyError, IndexError):
        return None


def fetch_pmc(pmc, out, log):
    r = get(f"{S3}/?list-type=2&prefix={pmc}.")
    keys = re.findall(r"<Key>([^<]+)</Key>", r.text) if r else []
    if not keys:
        return False
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
        elif name.endswith((".txt",)):
            continue
        else:
            dest = out / "supplementary" / name
        if dest.exists():
            continue
        f = get(f"{S3}/{k}")
        if f:
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes(f.content)
            log["files"].append(str(dest.relative_to(ROOT)))
    log["pmc"] = latest
    return (out / "source.pdf").exists()


def fetch_elife(num, out, log):
    r = get(f"https://api.elifesciences.org/articles/{num}")
    if not r:
        return False
    j = r.json()
    if "pdf" in j and not (out / "source.pdf").exists():
        p = get(j["pdf"])
        if is_pdf(p):
            (out / "source.pdf").write_bytes(p.content)
            log["pdf"] = j["pdf"]
    (out / "article.json").write_text(json.dumps(j))
    figs = re.findall(r'"uri":\s*"(https://iiif\.elifesciences\.org/[^"]+?)"', json.dumps(j))
    for u in dict.fromkeys(figs):
        name = u.rstrip("/").split("/")[-1].split("%2F")[-1]
        dest = out / "figures" / name
        if not dest.exists():
            f = get(u + "/full/1500,/0/default.jpg") if not u.endswith((".jpg", ".png")) else get(u)
            if f and f.content[:3] in (b"\xff\xd8\xff", b"\x89PN"):
                dest = dest.with_suffix(".jpg")
                dest.write_bytes(f.content)
                log["files"].append(str(dest.relative_to(ROOT)))
    return (out / "source.pdf").exists()


def pdf_candidates(row, dois):
    text = " ".join(row.values())
    for doi in dois:
        r = get(f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}")
        if r:
            for loc in r.json().get("oa_locations") or []:
                if loc.get("url_for_pdf"):
                    yield loc["url_for_pdf"]
        if doi.startswith("10.1371/"):
            journal = {"pbio": "plosbiology", "pone": "plosone"}.get(doi.split(".")[2], "plosone")
            yield f"https://journals.plos.org/{journal}/article/file?id={doi}&type=printable"
        if doi.startswith("10.1101/"):
            for v in (3, 2, 1):
                yield f"https://www.biorxiv.org/content/{doi}v{v}.full.pdf"
    for l in row["links"].split():
        if l.lower().endswith(".pdf") or "/pdf" in l or "bitstream" in l or "download" in l:
            yield l
    for ax in re.findall(r"arXiv (\d{4}\.\d{4,5})|arxiv\.org/abs/([\w./-]+)", text):
        yield f"https://arxiv.org/pdf/{ax[0] or ax[1]}"


def process(row):
    out = DATA / row["section"] / row["id"]
    (out / "figures").mkdir(parents=True, exist_ok=True)
    log = {"id": row["id"], "pdf": None, "pmc": None, "pages": [], "files": [], "tried": []}
    dois = [d.rstrip(".") for d in row["dois"].split()]
    if row["id"] in OVERRIDES and OVERRIDES[row["id"]] not in dois:
        dois.insert(0, OVERRIDES[row["id"]])
    log["dois"] = dois
    have = lambda: (out / "source.pdf").exists()
    if have():
        log["pdf"] = "existing"

    pmcs = set(re.findall(r"PMC(\d{5,})", " ".join(row.values())))
    for doi in dois:
        p = pmcid_for(doi)
        if p:
            pmcs.add(p[3:])
    for pmc in pmcs:
        if fetch_pmc(f"PMC{pmc}", out, log) and not log["pdf"]:
            log["pdf"] = f"{S3}/PMC{pmc}"
    m = re.search(r"elife\S*?(\d{5})", " ".join(row.values()) + " ".join(dois), re.I)
    if m:
        fetch_elife(m.group(1), out, log)

    for url in pdf_candidates(row, dois):
        if have():
            break
        if url in log["tried"]:
            continue
        log["tried"].append(url)
        r = get(url)
        if is_pdf(r):
            (out / "source.pdf").write_bytes(r.content)
            log["pdf"] = url

    for url in row["links"].split() + [f"https://doi.org/{d}" for d in dois]:
        r = get(url)
        if r is None or "html" not in r.headers.get("content-type", "") or "Just a moment" in r.text[:3000]:
            continue
        name = f"page{len(log['pages']) or ''}.html"
        (out / name).write_bytes(r.content)
        log["pages"].append(url)
        if have():
            continue
        m = re.search(r'<meta[^>]+name="citation_pdf_url"[^>]+content="([^"]+)"', r.text) or \
            re.search(r'content="([^"]+)"[^>]+name="citation_pdf_url"', r.text)
        if m:
            p = get(urljoin(r.url, m.group(1)))
            if is_pdf(p):
                (out / "source.pdf").write_bytes(p.content)
                log["pdf"] = m.group(1)
    if have() and not log["pdf"]:
        log["pdf"] = "existing"
    return log


if __name__ == "__main__":
    rows = list(csv.DictReader(open(ROOT / "sources.csv")))
    if len(sys.argv) > 2:
        rows = [r for r in rows if r["id"] in sys.argv[2:]]
    with cf.ThreadPoolExecutor(10) as ex:
        logs = list(ex.map(process, rows))
    logfile = ROOT / "download_log.json"
    old = {l["id"]: l for l in json.loads(logfile.read_text())} if logfile.exists() else {}
    old.update({l["id"]: l for l in logs})
    logfile.write_text(json.dumps(list(old.values()), indent=1))
    for l in logs:
        nfig = len([f for f in l["files"] if "/figures/" in f])
        print(f"{l['id']:9s} pdf={'Y' if l['pdf'] else '-'} pmc={l['pmc'] or '-':14s} figs={nfig:2d} pages={len(l['pages'])}")
