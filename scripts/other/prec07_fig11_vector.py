"""Read yearly values of Cour des comptes CNRS report Graphique 11 (p49) from its vector polylines.
y axis: 0% at y=269.5? calibrated from tick labels (0% label centre y=269, 12% y=108)."""
import sys, pymupdf
p = pymupdf.open(sys.argv[1])[48]
lab = {b[4].strip(): (b[1] + b[3]) / 2 for b in p.get_text('blocks', clip=pymupdf.Rect(100, 95, 130, 280))}
y0, y12 = lab['0%'], lab['12%']
for d in p.get_drawings():
    r = d['rect']
    if r.x0 > 140 and r.x1 < 440 and r.height > 10 and d['items'][0][0] == 'l':
        pts = [d['items'][0][1]] + [it[2] for it in d['items']]
        print(d.get('color'), [round(12 * (y0 - q.y) / (y0 - y12), 2) for q in pts])
