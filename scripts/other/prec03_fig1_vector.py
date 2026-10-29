"""Read year values from the vector lines of PREC-03 figure 1 (Note DGRH n°2-2025 p1).
Scale calibrated on the stated totals (2014: 2 358 published, 2023: 2 280 published)."""
import sys, pymupdf
d = pymupdf.open(sys.argv[1]); p = d[0]
names = {(0.0, 0.0, 0.0): 'authorised', (0.122, 0.286, 0.49): 'published_total', (0.498, 0.498, 0.498): 'published_MCF',
         (0.557, 0.706, 0.89): 'published_PR', (0.31, 0.506, 0.741): 'filled_MCF', (0.776, 0.851, 0.945): 'filled_PR'}
y0 = 747.0; tot = None; lines = {}
for dr in p.get_drawings():
    r = dr['rect']
    if not (r.y0 > 615 and r.y1 < 760 and r.x0 > 220 and r.width > 200 and len(dr['items']) > 5): continue
    key = tuple(round(c, 3) for c in dr['color']); name = next(v for k, v in names.items() if all(abs(a - b) < 0.01 for a, b in zip(k, key)))
    pts = [dr['items'][0][1]] + [it[-1] for it in dr['items']]
    xs = [234.4 + i * (553.7 - 234.4) / 9 for i in range(10)]
    lines[name] = [min(pts, key=lambda q: abs(q.x - x)).y for x in xs]
s = ((y0 - lines['published_total'][0]) / 2358 + (y0 - lines['published_total'][-1]) / 2280) / 2
print('year,' + ','.join(lines))
for i, yr in enumerate(range(2014, 2024)):
    print(yr, *[round((y0 - lines[k][i]) / s) for k in lines], sep=',')
