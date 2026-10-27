"""Crop a table/figure starting at a caption: from caption top, include drawings and text blocks
that follow contiguously (gap < GAP pt) in the same column span. usage: PDF PAGE "caption" OUT [gap] [x0 x1]"""
import sys, pymupdf
pdf, pg, cap, out = sys.argv[1:5]
gap = float(sys.argv[5]) if len(sys.argv) > 5 else 18
d = pymupdf.open(pdf); p = d[int(pg) - 1]
hits = p.search_for(cap)
if not hits: sys.exit('caption not found')
c = sorted(hits, key=lambda h: h.y0)[0]
r = pymupdf.Rect(c)
items = [pymupdf.Rect(b[:4]) for b in p.get_text('blocks') if b[3] - b[1] < p.rect.height * 0.9]
items += [dr['rect'] for dr in p.get_drawings() if dr['rect'].width < p.rect.width * 0.95]
items += [rr for im in p.get_images(full=True) for rr in p.get_image_rects(im[0])]
items = sorted([i for i in items if i.y0 >= c.y0 - 2], key=lambda i: i.y0)
if len(sys.argv) > 7:
    xa, xb = float(sys.argv[6]), float(sys.argv[7])
    items = [i for i in items if i.x1 > xa and i.x0 < xb]
for i in items:
    if i.y0 > r.y1 + gap: break
    if i.y1 > p.rect.height - 40: continue  # page footer
    r |= i
r = pymupdf.Rect(r.x0 - 3, r.y0 - 3, r.x1 + 3, r.y1 + 3) & p.rect
pix = p.get_pixmap(dpi=300, clip=r); pix.save(out); print(out, r, pix.width, pix.height)
