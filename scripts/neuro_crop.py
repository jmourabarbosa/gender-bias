"""Crop NEURO-section figures from source PDFs at 300 dpi with PyMuPDF.
Usage: python3 -I scripts/neuro_crop.py  (run from repo root)"""
import pymupdf, sys
B = 'gender-bias-data/08-neuroscience/'

def graphics_bbox(page, above_y=None, below_y=None, xmin=None, xmax=None):
    rects = [page.get_image_bbox(im) for im in page.get_images(full=True)]
    rects += [d['rect'] for d in page.get_drawings()]
    W, H = page.rect.width, page.rect.height
    out = []
    for r in rects:
        if r.is_empty or r.is_infinite: continue
        if r.width > 0.95 * W and r.height > 0.9 * H: continue
        if above_y is not None and r.y0 >= above_y: continue
        if below_y is not None and r.y1 <= below_y: continue
        if xmin is not None and r.x1 < xmin: continue
        if xmax is not None and r.x0 > xmax: continue
        out.append(r)
    u = pymupdf.Rect(out[0])
    for r in out[1:]: u |= r
    return u

def grow_with_text(page, rect, pad=6, limit=None):
    # add text lines (axis labels, legends) touching the graphics box
    changed = True
    while changed:
        changed = False
        big = rect + (-pad, -pad, pad, pad)
        for b in page.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                r = pymupdf.Rect(l['bbox'])
                if limit is not None and not limit.contains(r): continue
                if r.intersects(big) and not rect.contains(r):
                    rect |= r; changed = True
    return rect

def save(page, rect, out, margin=4):
    rect = (rect + (-margin, -margin, margin, margin)) & page.rect
    page.get_pixmap(dpi=300, clip=rect).save(out)
    print(out, [round(v) for v in rect])

def caption_y(page, text):
    hits = page.search_for(text)
    return hits[0] if hits else None

jobs = []
# NEURO-03 Fig 1-3 (bioRxiv v1); Fig 2 is the GCBI by category
d = pymupdf.open(B + 'NEURO-03/source.pdf')
for n, pn in [(1, 8), (2, 9), (3, 10)]:
    p = d[pn - 1]; c = caption_y(p, f'Figure {n}.')
    g = graphics_bbox(p, above_y=c.y0, below_y=60)
    g = grow_with_text(p, g, limit=pymupdf.Rect(0, 60, p.rect.width, c.y0 - 1))
    if n == 3: g.x1 = min(g.x1, 558)
    save(p, g, B + f'NEURO-03/figures/NEURO-03_fig{n}.png')

# NEURO-05 Fig 1 (page 3) and Table 2 (pages 5-10)
d = pymupdf.open(B + 'NEURO-05/source.pdf')
p = d[2]
img = [p.get_image_bbox(im) for im in p.get_images(full=True)][0]
cap_end = max(r.y1 for r in p.search_for('estimated peak in time of a given aspect'))
cap = p.search_for('Figure 1.')[0]
save(p, pymupdf.Rect(cap.x0, img.y0, img.x1 + 60, cap_end), B + 'NEURO-05/figures/NEURO-05_fig1.png')
if len(sys.argv) > 1 and sys.argv[1] == 'tables':
    pass
for k, pn in enumerate(range(5, 11), 1):
    p = d[pn - 1]
    # pages are rotated 90 deg: the table text runs vertically in unrotated (mediabox) space, while the
    # journal sidebar and running footer are horizontal there. Keep vertical lines, then map to the rotated page.
    body = [pymupdf.Rect(l['bbox']) for b in p.get_text('dict')['blocks'] for l in b.get('lines', [])
            if abs(l['dir'][0]) < 0.01
            and not any(w in ''.join(sp['text'] for sp in l['spans']) for w in ('Neuron', 'Perspective', 'CellPress'))]
    # table rules / row shading only (long thin or wide shapes); skips the logo and the blue corner box
    body += [d['rect'] for d in p.get_drawings() if max(d['rect'].width, d['rect'].height) > 300
             and d['rect'].height < p.mediabox.height * 0.95]
    body = [r * p.rotation_matrix for r in body]
    body = [r for r in body if r.y1 < p.rect.height - 20]
    u = body[0]
    for r in body[1:]: u |= r
    save(p, u, B + f'NEURO-05/figures/NEURO-05_table2_part{k}.png')

# NEURO-06 Fig 1 (p2) and Fig 2 (image on p6, caption top of p7)
d = pymupdf.open(B + 'NEURO-06/source.pdf')
p = d[1]; c = caption_y(p, 'Figure 1:')
g = graphics_bbox(p, above_y=c.y0, below_y=100)
g = grow_with_text(p, g, limit=pymupdf.Rect(0, 100, p.rect.width, c.y0 - 1))
g.y1 = min(g.y1, c.y0 - 5)
save(p, g, B + 'NEURO-06/figures/NEURO-06_fig1.png', margin=2)
p = d[5]; g = graphics_bbox(p)
imgs = [p.get_image_bbox(im) for im in p.get_images(full=True)]
save(p, imgs[0], B + 'NEURO-06/figures/NEURO-06_fig2.png')

# NEURO-10 "A changing balance" graphic (page 2, right column)
d = pymupdf.open(B + 'NEURO-10/source.pdf')
p = d[1]
# right column graphic: from the 'A CHANGING BALANCE' heading (y~52) to the footnote (y~759)
region = pymupdf.Rect(p.search_for('Nature’s analysis')[0].x0 - 30, 48, p.rect.width - 25, 762)
g = graphics_bbox(p, above_y=region.y1, below_y=region.y0, xmin=region.x0, xmax=region.x1) & region
for b in p.get_text('dict')['blocks']:
    for l in b.get('lines', []):
        r = pymupdf.Rect(l['bbox'])
        if region.contains(r): g |= r
save(p, g, B + 'NEURO-10/figures/NEURO-10_fig1.png')
