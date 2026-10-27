"""Render a page preview or crop a region of a PDF page.
preview: python3 -I pubcit_crop.py preview file.pdf PAGE out.png
crop:    python3 -I pubcit_crop.py crop file.pdf PAGE x0 y0 x1 y1 out.png [dpi]
Coordinates are PDF points (page.rect). Default 300 dpi."""
import sys, pymupdf
mode, pdf, pno = sys.argv[1], sys.argv[2], int(sys.argv[3])
page = pymupdf.open(pdf)[pno]
if mode == "preview":
    pix = page.get_pixmap(dpi=72)
    pix.save(sys.argv[4]); print(page.rect)
else:
    x0, y0, x1, y1 = map(float, sys.argv[4:8])
    dpi = int(sys.argv[9]) if len(sys.argv) > 9 else 300
    pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(x0, y0, x1, y1))
    pix.save(sys.argv[8]); print(pix.width, pix.height)
