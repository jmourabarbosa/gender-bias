"""Generate docs/index.html: a plain index of every source, its key number, files, figures and data.

Files are linked on GitHub; figures load from raw.githubusercontent.com so the page stays small.
"""
import csv, html, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "gender-bias-data"
REPO = "jmourabarbosa/gender-bias"
BRANCH = "claude/epic-cannon-fl66g4"
BLOB = f"https://github.com/{REPO}/blob/{BRANCH}/"
TREE = f"https://github.com/{REPO}/tree/{BRANCH}/"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"
DECK = "https://docs.google.com/presentation/d/1yYIy91PrH9_lkR1q3tuOp8_XK4xGO43EG6yZG2MajyA/edit"
SECTIONS = {"01": "Pipeline and representation", "02": "Hiring and evaluation", "03": "Funding",
            "04": "Publishing and peer review", "05": "Citations, recognition and visibility",
            "06": "Pay, promotion and attrition", "07": "Teaching evaluations and service load",
            "08": "Neuroscience", "09": "Interventions with evidence", "10": "Datasets and tools"}
e = html.escape

sources = list(csv.DictReader(open(ROOT / "sources.csv")))
for s in sources:
    s["title"] = s["title"].replace("*", "")
manifest = {r["id"]: r for r in csv.DictReader(open(DATA / "manifest.csv"))}


def card(src):
    sid, folder = src["id"], DATA / src["section"] / src["id"]
    rel = folder.relative_to(ROOT).as_posix() + "/"
    m = manifest.get(sid, {})
    status = m.get("access_status", "pending")
    links = [f'<a href="{e(TREE + rel)}">folder</a>']
    if (folder / "notes.md").exists():
        links.append(f'<a href="{e(BLOB + rel)}notes.md">notes</a>')
    for pdf in sorted(folder.glob("*.pdf"))[:2]:
        links.append(f'<a href="{e(BLOB + rel + pdf.name)}">{e(pdf.name)}</a>')
    if (folder / "data").is_dir():
        links.append(f'<a href="{e(TREE + rel)}data">data</a>')
    first = (src["links"].split() or [""])[0]
    if first:
        links.append(f'<a href="{e(first)}">original</a>')
    figs = sorted(p for p in (folder / "figures").glob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg")) if (folder / "figures").is_dir() else []
    named = [p for p in figs if p.name.startswith(sid)] or figs[:4]
    thumbs = "".join(f'<a href="{e(BLOB + rel)}figures/{e(p.name)}"><img loading="lazy" src="{e(RAW + rel)}figures/{e(p.name)}" alt="{e(sid)} {e(p.stem)}"></a>' for p in named[:6])
    note = m.get("notes", "")
    return f'''<article class="src" data-text="{e((sid + " " + src["title"] + " " + src["key_number"] + " " + status).lower())}">
<h3><span class="id">{e(sid)}</span> {e(src["title"])}</h3>
<p class="key">{e(src["key_number"]) or "&nbsp;"}</p>
<p class="meta"><span class="status {e(status)}">{e(status)}</span> {" · ".join(links)}</p>
{f'<p class="note">{e(note)}</p>' if note else ""}
{f'<div class="figs">{thumbs}</div>' if thumbs else ""}
</article>'''


by_sec = {}
for s in sources:
    by_sec.setdefault(s["section"][:2], []).append(s)
counts = {}
for r in manifest.values():
    counts[r["access_status"]] = counts.get(r["access_status"], 0) + 1
toc = "".join(f'<li><a href="#s{k}">{k}. {e(v)}</a> ({len(by_sec.get(k, []))})</li>' for k, v in SECTIONS.items())
body = "".join(f'<section id="s{k}"><h2>{k}. {e(v)}</h2>{"".join(card(s) for s in by_sec.get(k, []))}</section>' for k, v in SECTIONS.items())
summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gender bias in academia: sources</title>
<style>
:root {{ --fg:#111; --bg:#fff; --muted:#555; --line:#ddd; }}
@media (prefers-color-scheme: dark) {{ :root {{ --fg:#eee; --bg:#111; --muted:#aaa; --line:#333; }} }}
body {{ margin:0 auto; max-width:1000px; padding:24px 16px; font:15px/1.5 Arial, Helvetica, sans-serif; color:var(--fg); background:var(--bg); }}
a {{ color:inherit; }}
h1 {{ font-size:28px; margin:0 0 8px; }} h2 {{ font-size:20px; margin:40px 0 8px; border-bottom:1px solid var(--line); padding-bottom:4px; }}
h3 {{ font-size:16px; margin:0 0 2px; }} .id {{ font-family:monospace; color:var(--muted); }}
.src {{ padding:12px 0; border-bottom:1px solid var(--line); }}
.key {{ margin:2px 0; font-weight:bold; }} .meta, .note {{ margin:2px 0; color:var(--muted); font-size:13px; }}
.status {{ font-family:monospace; border:1px solid var(--muted); padding:0 4px; }}
.figs {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:6px; }}
.figs img {{ height:110px; max-width:100%; border:1px solid var(--line); background:#fff; }}
input {{ width:100%; box-sizing:border-box; padding:8px; font:inherit; color:var(--fg); background:var(--bg); border:1px solid var(--muted); }}
ul.toc {{ columns:2; padding-left:18px; }} @media (max-width:600px) {{ ul.toc {{ columns:1; }} }}
</style></head><body>
<h1>Gender bias in academia: sources and data</h1>
<p>{len(sources)} sources in 10 sections, collected for a talk. Status: {e(summary)}.
Each source has a folder with the PDF or saved page, figures, any data, and a <code>notes.md</code> that checks the headline number.</p>
<p><a href="{DECK}">Slides (Google Slides)</a> · <a href="{BLOB}gender-bias-data/manifest.csv">manifest.csv</a> · <a href="{BLOB}SOURCES.md">annotated source list</a> · <a href="{TREE}scripts">scripts</a> · <a href="https://github.com/{REPO}/tree/{BRANCH}">repository</a></p>
<p>Paywalled sources were not downloaded; their folders hold the abstract or landing page.</p>
<input id="q" type="search" placeholder="Filter by ID, title, number or status (e.g. paywalled)">
<ul class="toc">{toc}</ul>
{body}
<script>
document.getElementById('q').addEventListener('input', ev => {{
  const q = ev.target.value.toLowerCase().trim();
  document.querySelectorAll('.src').forEach(a => a.style.display = !q || a.dataset.text.includes(q) ? '' : 'none');
}});
</script>
</body></html>'''
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs" / "index.html").write_text(page)
(ROOT / "docs" / ".nojekyll").write_text("")
print("docs/index.html", len(page) // 1024, "KB")
