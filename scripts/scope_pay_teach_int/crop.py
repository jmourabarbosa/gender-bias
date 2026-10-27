"""Crop a region of a PDF page to PNG at >=300 dpi.
usage: python3 -I crop.py PDF PAGE(1-based) x0 y0 x1 y1 OUT.png [dpi]"""
import sys, pymupdf
pdf, pg, x0, y0, x1, y1, out = sys.argv[1:8]
dpi = int(sys.argv[8]) if len(sys.argv) > 8 else 300
d = pymupdf.open(pdf)
p = d[int(pg) - 1]
clip = pymupdf.Rect(float(x0), float(y0), float(x1), float(y1)) & p.rect
pix = p.get_pixmap(dpi=dpi, clip=clip)
pix.save(out)
print(out, pix.width, pix.height)
