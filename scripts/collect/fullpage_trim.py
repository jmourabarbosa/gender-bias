"""Render a (possibly rotated) PDF page at 300 dpi and trim to non-white content, skipping a header band.
usage: python3 -I fullpage_trim.py <pdf> <page1based> <out.png> [skip_top_frac=0.08]"""
import sys, pymupdf
from PIL import Image, ImageOps
pdf, pg, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
skip = float(sys.argv[4]) if len(sys.argv) > 4 else 0.08
pix = pymupdf.open(pdf)[pg - 1].get_pixmap(dpi=300)
im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
top = int(im.height * skip); im = im.crop((0, top, im.width, im.height))
bb = ImageOps.invert(im.convert("L")).point(lambda v: 255 if v > 40 else 0).getbbox()
im.crop((max(bb[0]-30,0), max(bb[1]-30,0), min(bb[2]+30, im.width), min(bb[3]+30, im.height))).save(out); print("saved", out)
