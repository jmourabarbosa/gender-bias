"""Render a page preview at low dpi with a coordinate grid (every 50pt). usage: PDF PAGE OUT [dpi]"""
import sys, pymupdf
pdf, pg, out = sys.argv[1:4]
dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 70
d = pymupdf.open(pdf); p = d[int(pg) - 1]
sh = p.new_shape()
for y in range(0, int(p.rect.height), 50):
    sh.draw_line((0, y), (p.rect.width, y))
    p.insert_text((2, y + 8), str(y), fontsize=7, color=(1, 0, 0))
for x in range(0, int(p.rect.width), 50):
    sh.draw_line((x, 0), (x, p.rect.height))
    p.insert_text((x + 1, 8), str(x), fontsize=7, color=(1, 0, 0))
sh.finish(color=(1, 0.6, 0.6), width=0.3); sh.commit()
p.get_pixmap(dpi=dpi).save(out); print(out, p.rect)
