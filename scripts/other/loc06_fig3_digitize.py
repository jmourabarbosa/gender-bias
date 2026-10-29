"""Digitize Figure 3 (p.19) of Godechot et al. 2025: MCF local-recruitment rate 2002-2022 (MESR data), from vector markers."""
import csv, re, collections, pymupdf
D = '/home/user/gender-bias/other-biases-data/01-localism/LOC-06'
p = pymupdf.open(f'{D}/source.pdf')[18]
yt, xt = {}, {}
for w in p.get_text('words'):
    if w[1] > 380 and w[3] < 700:
        if re.fullmatch(r'(20|25|30)', w[4]) and w[0] < 110: yt[int(w[4])] = (w[1] + w[3]) / 2
        if re.fullmatch(r'20[012]\d', w[4]): xt[int(w[4])] = (w[0] + w[2]) / 2
print(yt, xt)
(ya, yb), (xa, xb) = sorted(yt.items())[::2], [(2005, xt[2005]), (2020, xt[2020])]
fy = lambda y: ya[0] + (y - ya[1]) * (yb[0] - ya[0]) / (yb[1] - ya[1])
fx = lambda x: xa[0] + (x - xa[1]) * (xb[0] - xa[0]) / (xb[1] - xa[1])
dr = p.get_drawings()
c = collections.Counter((d['type'], round(d['rect'].width, 1), round(d['rect'].height, 1)) for d in dr)
print(c.most_common(6))
pts = [d['rect'] for d in dr if d['type'] == 'f' and 1 < d['rect'].width < 3 and abs(d['rect'].width - d['rect'].height) < 0.2]
rows = sorted({(round(fx((r.x0 + r.x1) / 2)), round(fy((r.y0 + r.y1) / 2), 1)) for r in pts})
with open(f'{D}/data/LOC-06_fig3_local_rate.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['year', 'mcf_local_recruitment_rate_pct_digitized']); w.writerows(rows)
print(rows)
