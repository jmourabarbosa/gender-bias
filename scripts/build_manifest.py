"""Rebuild gender-bias-data/manifest.csv from the per-source _status/<ID>.json files."""
import csv, json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / os.environ.get("DATA_DIR", "gender-bias-data")
rows = list(csv.DictReader(open(ROOT / os.environ.get("SOURCES_CSV", "sources.csv"))))
cols = ["id", "title", "url_used", "file_paths", "access_status", "figures_extracted", "notes"]
with open(DATA / "manifest.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in rows:
        p = DATA / "_status" / f"{r['id']}.json"
        s = json.loads(p.read_text()) if p.exists() else {"access_status": "pending"}
        join = lambda v: "; ".join(v) if isinstance(v, list) else (v or "")
        w.writerow({"id": r["id"], "title": s.get("title") or r["title"], "url_used": join(s.get("url_used")),
                    "file_paths": join(s.get("file_paths")), "access_status": s.get("access_status", "pending"),
                    "figures_extracted": join(s.get("figures_extracted")), "notes": s.get("notes", "")})
print(open(DATA / "manifest.csv").read().count("\n") - 1, "rows")
