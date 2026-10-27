"""Build Slides requests that hyperlink each citation in a slide's source line.

Link target per source ID: its PDF on GitHub when one was downloaded; the publisher page (DOI) when
there is no PDF on GitHub (paywalled, or full text only) and the source has a DOI; otherwise its GitHub folder
(saved web page, data).
Usage: python3 scripts/link_sources.py > requests.json   (writes deck/source_links_resolved.csv too)
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "gender-bias-data"
GH = "https://github.com/jmourabarbosa/gender-bias/"
BRANCH = "claude/epic-cannon-fl66g4"
GREY = {"opaqueColor": {"rgbColor": {"red": 0.35, "green": 0.35, "blue": 0.35}}}
BLACK = {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}

sources = {r["id"]: r for r in csv.DictReader(open(ROOT / "sources.csv"))}
manifest = {r["id"]: r for r in csv.DictReader(open(DATA / "manifest.csv"))}
overrides = json.loads((ROOT / "scripts" / "doi_overrides.json").read_text())
spec = {s["id"]: s for s in json.load(open(ROOT / "deck" / "slides.json"))["slides"]}
links = json.load(open(ROOT / "deck" / "source_links.json"))


def target(sid):
    src = sources[sid]
    folder = DATA / src["section"] / sid
    status = manifest[sid]["access_status"]
    pdfs = [p for p in [folder / "source.pdf"] + sorted(folder.glob("*.pdf")) if p.exists()]
    rel = lambda p: p.relative_to(ROOT).as_posix()
    if status == "downloaded" and pdfs:
        return "github-pdf", f"{GH}blob/{BRANCH}/{rel(pdfs[0])}"
    doi = overrides.get(sid) or (src["dois"].split() or [None])[0]
    if status != "downloaded" or doi:  # no PDF on GitHub: link the paper itself
        if doi:
            return "publisher", f"https://doi.org/{doi.rstrip('.')}"
        return "publisher", src["links"].split()[0]
    return "github-folder", f"{GH}tree/{BRANCH}/{rel(folder)}"


reqs, rows = [], []
for slide_id, refs in links.items():
    s = spec[slide_id]
    if s.get("source"):
        box, text, color = slide_id + "_src", s["source"], GREY
    else:  # text slides carry the citation as the last bullet
        box, text, color = slide_id + "_b", "\n".join(b.replace("**", "") for b in s["bullets"]), BLACK
    for cite, sid in refs:
        start = text.find(cite)
        if start < 0:
            sys.exit(f"{slide_id}: citation not found: {cite}")
        kind, url = target(sid)
        rows.append([slide_id, sid, kind, url])
        reqs.append({"updateTextStyle": {"objectId": box, "textRange": {"type": "FIXED_RANGE", "startIndex": start, "endIndex": start + len(cite)},
                     "style": {"link": {"url": url}}, "fields": "link"}})
    # links take the theme's blue; keep the deck black and white
    reqs.append({"updateTextStyle": {"objectId": box, "textRange": {"type": "ALL"}, "style": {"foregroundColor": color}, "fields": "foregroundColor"}})
with open(ROOT / "deck" / "source_links_resolved.csv", "w", newline="") as f:
    csv.writer(f).writerows([["slide", "id", "link_type", "url"]] + rows)
print(json.dumps(reqs, ensure_ascii=False, separators=(",", ":")))
