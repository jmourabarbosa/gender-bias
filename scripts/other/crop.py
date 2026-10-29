"""crop.py PDF PAGE(1-based) START_TEXT END_TEXT OUT.png [dpi] [x0 x1]
Crops from top of START_TEXT to bottom of END_TEXT (first match below start). Use 'TOP'/'BOTTOM' for page edges,
or a number for an absolute y coordinate (points)."""
import sys, pymupdf
pdf, pno, s, e, out = sys.argv[1:6]
dpi = int(sys.argv[6]) if len(sys.argv) > 6 else 300
doc = pymupdf.open(pdf); page = doc[int(pno) - 1]; W, H = page.rect.width, page.rect.height
x0, x1 = (float(sys.argv[7]), float(sys.argv[8])) if len(sys.argv) > 8 else (20, W - 20)
def y(t, after=0, top=True):
    if t == 'TOP': return 0
    if t == 'BOTTOM': return H
    try: return float(t)
    except ValueError: pass
    hits = [r for r in page.search_for(t) if r.y0 >= after - 1]
    if not hits: sys.exit(f'not found: {t!r} on page {pno}')
    return hits[0].y0 if top else hits[0].y1
y0 = y(s); y1 = y(e, after=y0, top=False)
clip = pymupdf.Rect(x0, max(0, y0 - 6), x1, min(H, y1 + 6))
page.get_pixmap(dpi=dpi, clip=clip).save(out)
print(out, 'page', pno, 'clip', [round(v) for v in clip])
