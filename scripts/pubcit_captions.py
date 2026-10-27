"""List figure captions (page, bbox) in a PDF. Usage: python3 -I pubcit_captions.py file.pdf"""
import sys, re, pymupdf
d = pymupdf.open(sys.argv[1])
for i, p in enumerate(d):
    for b in p.get_text("blocks"):
        t = b[4].strip().replace("\n", " ")
        if re.match(r"^(Fig\.?|Figure|FIG\.?|FIGURE|Table|TABLE)\s*\d", t) or re.match(r"^[A-Z ]{6,}$", t):
            print(i, [round(x) for x in b[:4]], t[:160])
    imgs = p.get_images()
    if imgs: print(i, "images:", len(imgs), "drawings:", len(p.get_drawings()))
