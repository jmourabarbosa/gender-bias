"""Usage: pdfpeek.py PDF PAGE(1-based) OUT.png [dpi] [x0 y0 x1 y1]  -> renders page or clip; prints page size, image bboxes and caption text blocks."""
import sys, pymupdf
pdf, pno, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 60
d = pymupdf.open(pdf); p = d[pno-1]
clip = pymupdf.Rect(*map(float, sys.argv[5:9])) if len(sys.argv) > 8 else None
print('page rect', p.rect)
if clip is None:
    for img in p.get_images(full=True):
        try: print('img', img[0], p.get_image_bbox(img))
        except Exception as e: print('img err', e)
    for b in p.get_text('blocks'):
        print('blk', [round(v) for v in b[:4]], b[4][:80].replace('\n',' '))
p.get_pixmap(dpi=dpi, clip=clip).save(out)
