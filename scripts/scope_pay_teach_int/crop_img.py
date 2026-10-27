"""Crop an embedded image (largest on page, or the one nearest a caption) plus optionally its caption.
usage: python3 -I crop_img.py PDF PAGE "caption text" OUT.png [pad] [include_caption 0/1]"""
import sys, pymupdf
pdf, pg, cap, out = sys.argv[1:5]
pad = float(sys.argv[5]) if len(sys.argv) > 5 else 4
incl = sys.argv[6] == '1' if len(sys.argv) > 6 else True
d = pymupdf.open(pdf); p = d[int(pg) - 1]
hits = p.search_for(cap) if cap else []
boxes = []
for img in p.get_images(full=True):
    for r in p.get_image_rects(img[0]):
        if r.width > 50 and r.height > 50:
            boxes.append(r)
if not boxes:
    sys.exit('no image')
if hits:
    c = hits[0]
    box = min(boxes, key=lambda r: min(abs(r.y0 - c.y1), abs(c.y0 - r.y1)))
else:
    box = max(boxes, key=lambda r: r.width * r.height)
r = pymupdf.Rect(box)
if hits and incl:
    r |= hits[0]
r = pymupdf.Rect(r.x0 - pad, r.y0 - pad, r.x1 + pad, r.y1 + pad) & p.rect
pix = p.get_pixmap(dpi=300, clip=r); pix.save(out)
print(out, 'img', box, 'clip', r, pix.width, pix.height)
