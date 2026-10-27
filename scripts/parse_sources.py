"""Parse SOURCES.md into sources.csv and create the per-source folder layout."""
import csv, re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
md = (root / "SOURCES.md").read_text()
data_dir = root / "gender-bias-data"

rows, section = [], None
for line in md.splitlines():
    m = re.match(r"^## (\d\d) (.+)", line)
    if m:
        section = f"{m.group(1)}-" + re.sub(r"[^a-z]+", "-", m.group(2).lower()).strip("-").split("-")[0]
        continue
    if not line.startswith("| ") or line.startswith("| ID") or line.startswith("|---"):
        continue
    cells = [c.strip() for c in line.strip("|").split(" | ")]
    sid = cells[0]
    if section.startswith("10"):
        sid, title, maint, link, how, what = cells
        key, access, extract = "", "DATA", what
        title = f"{title} ({maint})"
    else:
        sid, title, key, access, link, how, extract = cells
    rows.append(dict(id=sid, section=section, title=title, key_number=key, access=access,
                     links=" ".join(re.findall(r"https?://[^\s)*;]+", link)),
                     dois=" ".join(re.findall(r"10\.\d{4,9}/[^\s;*]+", link)),
                     how=how, extract=extract))

with open(root / "sources.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

manifest = data_dir / "manifest.csv"
if not manifest.exists():
    data_dir.mkdir(exist_ok=True)
    with open(manifest, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "url_used", "file_paths", "access_status", "figures_extracted", "notes"])
        for r in rows:
            w.writerow([r["id"], r["title"], "", "", "pending", "", ""])
for r in rows:
    (data_dir / r["section"] / r["id"] / "figures").mkdir(parents=True, exist_ok=True)
print(len(rows), "sources;", ", ".join(sorted({r['section'] for r in rows})))
