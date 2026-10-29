"""Digitise graph 6 (p.4) of DGRH Note 2-2026 (LOC-01/source.pdf): prints (x, value%) of each line's anchor points.
Calibration: 0% gridline at y=228pt, 10 points of % = 30pt."""
import sys, pymupdf
p = pymupdf.open(sys.argv[1])[3]
for d in p.get_drawings():
    r = d['rect']
    if 245 <= r.x0 <= 560 and 70 < r.y0 < 230 and r.width > 100 and r.height > 0.5:
        pts = []
        for it in d['items']:
            if it[0] == 'c': pts += [it[1], it[4]]
            elif it[0] == 'l': pts += [it[1], it[2]]
        xs = sorted(set((round(pt.x, 1), round(pt.y, 2)) for pt in pts))
        print(d.get('color'), d.get('dashes'), [(x, round((228 - y) / 3, 2)) for x, y in xs])
