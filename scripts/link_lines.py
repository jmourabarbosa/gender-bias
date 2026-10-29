"""Add a 'Link to paper' line under each slide's source line.

Each cited source gets a short linked name; the source of the slide's figure also gets the PDF page
it was taken from (deck/figure_pages.json). The source line moves up to make room.
Usage: python3 scripts/link_lines.py > requests.json
"""
import csv, json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMU = 914400
GREY = {"opaqueColor": {"rgbColor": {"red": 0.35, "green": 0.35, "blue": 0.35}}}
spec = {s["id"]: s for s in json.load(open(ROOT / os.environ.get("DECK_DIR", "deck") / "slides.json"))["slides"]}
links = json.load(open(ROOT / os.environ.get("DECK_DIR", "deck") / "source_links.json"))
figs = json.load(open(ROOT / os.environ.get("DECK_DIR", "deck") / "figure_pages.json"))
urls = {(r["slide"], r["id"]): (r["link_type"], r["url"]) for r in csv.DictReader(open(ROOT / os.environ.get("DECK_DIR", "deck") / "source_links_resolved.csv"))}


NAMES = {"MESR, Vers l'égalité femmes-hommes ? Chiffres clés 2026": "MESR Chiffres clés 2026",
         "CNRS Plan d'action égalité 2024-2026": "CNRS Plan d'action 2024-2026", "Inserm, Journée Inserm 2024 (parité)": "Inserm parity slides 2024",
         "AAUP Annual Report on the Economic Status of the Profession 2025-26": "AAUP report 2025-26",
         "UCEA Intersectional Pay Gaps 2023-24": "UCEA pay gaps 2023-24", "CNRS MPDF pay analysis (2023)": "CNRS pay analysis 2023",
         "SfN 2016-17 Neuroscience Departments & Programs Survey": "SfN survey 2016-17", "C. Frye blog (6 Mar 2019)": "Frye blog 2019",
         "ERC results via EU-Büro": "ERC results (EU-Büro)", "Jesus-Rydin et al. EGU24-16168": "Jesus-Rydin et al. 2024",
         "biaswatchneuro.com posts": "BiasWatchNeuro", "Gelman via Reason (2019)": "Gelman in Reason 2019"}


def short(cite):
    if cite in NAMES:
        return NAMES[cite]
    m = re.match(r"(.+?) \(?(\d{4})\)?\b", cite)
    if not m or "," not in m.group(1) and "&" not in m.group(1) and " et al." not in m.group(1):
        return re.sub(r" \(.*", "", cite) if m is None else f"{m.group(1)} {m.group(2)}"
    authors, year = m.group(1), m.group(2)
    names = re.split(r", | & ", authors.replace(" et al.", ""))
    if len(names) == 2 and " et al." not in authors:
        return f"{names[0]} & {names[1]} {year}"
    return f"{names[0]} et al. {year}"


def box(oid, page, x, y, w, h):
    return {"createShape": {"objectId": oid, "shapeType": "TEXT_BOX", "elementProperties": {"pageObjectId": page,
            "size": {"width": {"magnitude": int(w * EMU), "unit": "EMU"}, "height": {"magnitude": int(h * EMU), "unit": "EMU"}},
            "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * EMU), "translateY": int(y * EMU), "unit": "EMU"}}}}


reqs = []
for slide, refs in links.items():
    fig = figs.get(slide, {})
    parts, spans = [], []
    for cite, sid in refs:
        name = short(cite)
        kind, url = urls[(slide, sid)]
        note = {"publisher": "publisher page", "github-folder": "saved page"}.get(kind)
        if sid == fig.get("id") and fig.get("page"):
            note = fig["page"] if not note else f"{note}, {fig['page']}"
        start = sum(len(p) for p in parts) + (len(" · ") * len(parts)) + len("Link to paper: " if len(refs) == 1 else "Links to papers: ")
        spans.append((start, start + len(name), url))
        parts.append(name + (f" ({note})" if note else ""))
    text = ("Link to paper: " if len(refs) == 1 else "Links to papers: ") + " · ".join(parts)
    oid = slide + "_lnk"
    if spec[slide].get("source"):
        reqs.append({"updatePageElementTransform": {"objectId": slide + "_src", "applyMode": "ABSOLUTE",
                     "transform": {"scaleX": 8412480 / 3000000, "scaleY": 365760 / 3000000, "translateX": int(0.4 * EMU), "translateY": int(4.92 * EMU), "unit": "EMU"}}})
    reqs += [box(oid, slide, 0.4, 5.24, 9.2, 0.3), {"insertText": {"objectId": oid, "text": text}},
             {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"},
              "style": {"fontFamily": "Arial", "fontSize": {"magnitude": 9, "unit": "PT"}, "foregroundColor": GREY}, "fields": "fontFamily,fontSize,foregroundColor"}}]
    reqs += [{"updateTextStyle": {"objectId": oid, "textRange": {"type": "FIXED_RANGE", "startIndex": a, "endIndex": b},
              "style": {"link": {"url": u}, "foregroundColor": GREY}, "fields": "link,foregroundColor"}} for a, b, u in spans]
    print(f"{slide}: {text}", file=__import__("sys").stderr)
print(json.dumps(reqs, ensure_ascii=False))
