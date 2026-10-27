"""Turn deck/slides.json into Google Slides batchUpdate requests (plain black on white).

Usage: python3 scripts/build_deck.py deck/slides.json <first_index> [slide_id ...] > requests.json
Images are referenced by repo path and served from raw.githubusercontent.com, so push first.
Slide kinds: section, text, fig (bullets left, figure right), wide (figure under title).
"""
import json, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/jmourabarbosa/gender-bias/claude/epic-cannon-fl66g4/"
EMU = 914400
BLACK = {"opaqueColor": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}
GREY = {"opaqueColor": {"rgbColor": {"red": 0.35, "green": 0.35, "blue": 0.35}}}


def box(oid, page, x, y, w, h):
    return {"createShape": {"objectId": oid, "shapeType": "TEXT_BOX", "elementProperties": {
        "pageObjectId": page,
        "size": {"width": {"magnitude": int(w * EMU), "unit": "EMU"}, "height": {"magnitude": int(h * EMU), "unit": "EMU"}},
        "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * EMU), "translateY": int(y * EMU), "unit": "EMU"}}}}


def text(oid, page, x, y, w, h, s, size, bold=False, color=BLACK, align="START", bullets=False, valign=None):
    reqs = [box(oid, page, x, y, w, h), {"insertText": {"objectId": oid, "text": s}},
            {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                                 "style": {"fontFamily": "Arial", "fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold, "foregroundColor": color},
                                 "fields": "fontFamily,fontSize,bold,foregroundColor"}},
            {"updateParagraphStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                                      "style": {"alignment": align, "spaceBelow": {"magnitude": 6 if bullets else 0, "unit": "PT"}},
                                      "fields": "alignment,spaceBelow"}}]
    if bullets:
        reqs.append({"createParagraphBullets": {"objectId": oid, "textRange": {"type": "ALL"}, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
    if valign:
        reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": {"contentAlignment": valign}, "fields": "contentAlignment"}})
    # bold **marked** spans
    return reqs


def bold_spans(oid, s):
    out, plain, i = [], "", 0
    parts = s.split("**")
    pos = 0
    for k, part in enumerate(parts):
        if k % 2 == 1:
            out.append({"updateTextStyle": {"objectId": oid, "textRange": {"type": "FIXED_RANGE", "startIndex": pos, "endIndex": pos + len(part)},
                                            "style": {"bold": True}, "fields": "bold"}})
        pos += len(part)
    return "".join(parts), out


def image(oid, page, path, x, y, w, h):
    im = Image.open(ROOT / path)
    ar = im.width / im.height
    if w / h > ar:
        nw, nh = h * ar, h
    else:
        nw, nh = w, w / ar
    x += (w - nw) / 2
    return {"createImage": {"objectId": oid, "url": RAW + path, "elementProperties": {
        "pageObjectId": page,
        "size": {"width": {"magnitude": int(nw * EMU), "unit": "EMU"}, "height": {"magnitude": int(nh * EMU), "unit": "EMU"}},
        "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * EMU), "translateY": int(y * EMU), "unit": "EMU"}}}}


def slide(s, idx):
    sid = s["id"]
    reqs = [{"createSlide": {"objectId": sid, "insertionIndex": idx, "slideLayoutReference": {"predefinedLayout": "BLANK"}}}]
    if s["kind"] == "section":
        reqs += text(sid + "_t", sid, 0.6, 1.6, 8.8, 1.2, s["title"], 32, bold=True, align="CENTER", valign="MIDDLE")
        if s.get("sub"):
            reqs += text(sid + "_s", sid, 0.6, 2.9, 8.8, 0.8, s["sub"], 16, color=GREY, align="CENTER")
        return reqs
    reqs += text(sid + "_t", sid, 0.4, 0.25, 9.2, 0.9, s["title"], 22, bold=True, valign="MIDDLE")
    top, bottom = 1.25, 5.0
    if s["kind"] == "text":
        body, b = bold_spans(sid + "_b", "\n".join(s["bullets"]))
        reqs += text(sid + "_b", sid, 0.5, top, 9.0, bottom - top - 0.1, body, s.get("size", 16), bullets=True) + b
    elif s["kind"] == "fig":
        body, b = bold_spans(sid + "_b", "\n".join(s["bullets"]))
        bw = s.get("text_w", 3.4)
        reqs += text(sid + "_b", sid, 0.4, top, bw, bottom - top - 0.1, body, s.get("size", 14), bullets=True) + b
        if s["image"]: reqs.append(image(sid + "_img", sid, s["image"], 0.4 + bw + 0.2, top, 9.6 - (0.4 + bw + 0.2), bottom - top - 0.05))
    elif s["kind"] == "wide":
        h = bottom - top
        if s.get("bullets"):
            body, b = bold_spans(sid + "_b", "\n".join(s["bullets"]))
            reqs += text(sid + "_b", sid, 0.5, bottom - 0.55, 9.0, 0.5, body, 13) + b
            h -= 0.6
        if s["image"]: reqs.append(image(sid + "_img", sid, s["image"], 0.4, top, 9.2, h - 0.05))
    if s.get("source"):
        reqs += text(sid + "_src", sid, 0.4, 5.1, 9.2, 0.4, s["source"], 9, color=GREY)
    return reqs


def templates(idx):
    """Styled template slides (moved to the end of the deck; skipped when presenting)."""
    T = [{"id": "tpl_sec", "kind": "section", "title": "{{title}}", "sub": "{{sub}}"},
         {"id": "tpl_text", "kind": "text", "title": "{{title}}", "bullets": ["{{body}}"]},
         {"id": "tpl_fig", "kind": "fig", "title": "{{title}}", "bullets": ["{{body}}"], "source": "{{source}}", "image": None},
         {"id": "tpl_wide", "kind": "wide", "title": "{{title}}", "bullets": ["{{body}}"], "source": "{{source}}", "image": None}]
    reqs = []
    for k, t in enumerate(T):
        r = slide(t, idx + k)
        reqs += [q for q in r if "createImage" not in q]
        if t["kind"] in ("fig", "wide"):
            x, y, w, h = (4.0, 1.25, 5.6, 3.65) if t["kind"] == "fig" else (0.4, 1.25, 9.2, 3.1)
            reqs += [box(t["id"] + "_img", t["id"], x, y, w, h), {"insertText": {"objectId": t["id"] + "_img", "text": "{{img}}"}}]
        reqs.append({"updateSlideProperties": {"objectId": t["id"], "slideProperties": {"isSkipped": True}, "fields": "isSkipped"}})
    return reqs


ELEMS = {"section": ["_t", "_s"], "text": ["_t", "_b"], "fig": ["_t", "_b", "_src", "_img"], "wide": ["_t", "_b", "_src", "_img"]}


def compact(s, idx):
    """Duplicate the template for s['kind'], fill text and image, move it to idx."""
    sid, kind = s["id"], s["kind"]
    tpl = "tpl_" + {"section": "sec"}.get(kind, kind)
    ids = {tpl: sid, **{tpl + e: sid + e for e in ELEMS[kind]}}
    reqs = [{"duplicateObject": {"objectId": tpl, "objectIds": ids}},
            {"updateSlideProperties": {"objectId": sid, "slideProperties": {"isSkipped": False}, "fields": "isSkipped"}},
            {"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": idx}}]
    body, bolds = bold_spans(sid + "_b", "\n".join(s.get("bullets", [])))
    fills = {"{{title}}": s["title"], "{{sub}}": s.get("sub", ""), "{{body}}": body, "{{source}}": s.get("source", "")}
    for k, v in fills.items():
        if k == "{{sub}}" and kind != "section":
            continue
        reqs.append({"replaceAllText": {"containsText": {"text": k, "matchCase": True}, "replaceText": v, "pageObjectIds": [sid]}})
    if body:
        reqs += bolds
    elif kind == "wide":
        reqs.append({"deleteObject": {"objectId": sid + "_b"}})
    if kind in ("fig", "wide"):
        reqs.append({"replaceAllShapesWithImage": {"imageUrl": RAW + s["image"], "imageReplaceMethod": "CENTER_INSIDE",
                                                   "containsText": {"text": "{{img}}", "matchCase": True}, "pageObjectIds": [sid]}})
    return reqs


if __name__ == "__main__" and sys.argv[1] == "templates":
    print(json.dumps(templates(int(sys.argv[2]))))
    sys.exit()

if __name__ == "__main__" and sys.argv[1] == "compact":
    spec = json.load(open(sys.argv[2]))
    idx = int(sys.argv[3])
    wanted = sys.argv[4:]
    reqs = []
    for s in spec["slides"]:
        if wanted and s["id"] not in wanted:
            continue
        reqs += compact(s, idx)
        idx += 1
    print(json.dumps(reqs, separators=(",", ":")))
    sys.exit()

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    first = int(sys.argv[2])
    wanted = set(sys.argv[3:])
    reqs, idx = [], first
    for s in spec["slides"]:
        if wanted and s["id"] not in wanted:
            continue
        reqs += slide(s, idx)
        idx += 1
    print(json.dumps(reqs))
