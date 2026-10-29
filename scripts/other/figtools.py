"""Figure helpers. Usage:
  python3 -I figtools.py find <pdf> <regex>            -> pages/positions of captions
  python3 -I figtools.py layout <pdf> <page1based>     -> page size, image bboxes, drawing union, text blocks
  python3 -I figtools.py preview <pdf> <page> <out.png> [dpi]
  python3 -I figtools.py crop <pdf> <page> x0 y0 x1 y1 <out.png> [dpi=300]
"""
import sys, re, pymupdf
cmd, pdf = sys.argv[1], sys.argv[2]
doc = pymupdf.open(pdf)
if cmd == "find":
    rx = re.compile(sys.argv[3])
    for i, p in enumerate(doc):
        for b in p.get_text("blocks"):
            if rx.search(b[4].strip()[:40]):
                print(i + 1, [round(v) for v in b[:4]], b[4].strip().replace("\n", " ")[:90])
elif cmd == "layout":
    p = doc[int(sys.argv[3]) - 1]
    print("rect", p.rect)
    for im in p.get_image_info():
        print("img", [round(v) for v in im["bbox"]])
    dr = [d["rect"] for d in p.get_drawings()]
    if dr:
        u = dr[0]
        for r in dr[1:]: u |= r
        print("drawings", len(dr), [round(v) for v in u])
    for b in p.get_text("blocks"):
        print("txt", [round(v) for v in b[:4]], b[4].strip().replace("\n", " ")[:70])
elif cmd == "preview":
    p = doc[int(sys.argv[3]) - 1]
    dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 50
    p.get_pixmap(dpi=dpi).save(sys.argv[4])
elif cmd == "crop":
    p = doc[int(sys.argv[3]) - 1]
    x0, y0, x1, y1 = map(float, sys.argv[4:8])
    dpi = int(sys.argv[9]) if len(sys.argv) > 9 else 300
    p.get_pixmap(dpi=dpi, clip=pymupdf.Rect(x0, y0, x1, y1)).save(sys.argv[8])
    print("saved", sys.argv[8])
