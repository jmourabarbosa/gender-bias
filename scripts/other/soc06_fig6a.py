"""Digitize Morgan et al. 2022 Fig. 6a (PDF p.6, vector): % faculty with a PhD parent by birth decade, top/bottom 20% prestige and average."""
import csv, re, pymupdf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/02-social/SOC-06'
p = pymupdf.open(f'{D}/source.pdf')[5]
W = [w for w in p.get_text('words') if w[0] < 300]
yt = {int(w[4]): (w[1] + w[3]) / 2 for w in W if w[0] < 113 and re.fullmatch(r'\d+', w[4]) and 70 < w[1] < 185}
xt = {int(w[4]): (w[0] + w[2]) / 2 for w in W if re.fullmatch(r'19\d0', w[4]) and w[1] > 183}
(y0v, y0), (y1v, y1) = (0, yt[0]), (40, yt[40]); (x0v, x0), (x1v, x1) = (1940, xt[1940]), (1980, xt[1980])
fy = lambda y: y0v + (y - y0) * (y1v - y0v) / (y1 - y0); fx = lambda x: x0v + (x - x0) * (x1v - x0v) / (x1 - x0)
groups = {}
for d in p.get_drawings():
    r = d['rect']
    if d['type'] == 'fs' and abs(r.width - 2.9) < 0.2 and r.x1 < 300 and 60 < r.y0 < 168:  # y<168 excludes legend markers
        f = d['fill']; key = 'Average' if f == (0.0, 0.0, 0.0) else ('Bottom 20% prestige' if f[1] < 0.7 else 'Top 20% prestige')
        groups.setdefault(key, []).append((round(fx((r.x0 + r.x1) / 2)), round(fy((r.y0 + r.y1) / 2), 1)))
rows = []
for k, pts in groups.items():
    for yr, v in sorted(pts): rows.append([k, yr, v])
with open(f'{D}/data/SOC-06.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['group', 'faculty_birth_decade', 'pct_faculty_with_phd_parent_digitized']); w.writerows(rows)
for r in rows: print(r)
fig, ax = plt.subplots(figsize=(7, 4.4))
for k, st in (('Top 20% prestige', '-^'), ('Average', '-o'), ('Bottom 20% prestige', '--v')):
    pts = sorted(groups[k]); ax.plot([a for a, _ in pts], [b for _, b in pts], st, color='black' if k != 'Average' else '0.5', label=k.replace(' prestige', ' institutions by prestige'))
    ax.annotate(f'{pts[-1][1]:.0f}%', pts[-1], textcoords='offset points', xytext=(8, -3), fontsize=9)
ax.set_xticks([1940, 1950, 1960, 1970, 1980]); ax.set_xlabel('Faculty year of birth (decade)'); ax.set_ylim(0, 42); ax.set_xlim(1937, 1986)
ax.set_ylabel('% of US faculty with a PhD parent'); ax.legend(frameon=False, fontsize=9, loc='upper left')
ax.set_title('US faculty with a PhD parent, by institutional prestige', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Morgan et al. (2022), Nature Human Behaviour 6:1625, fig. 6a p. 6 (values read from vector figure)', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/SOC-06_redraw.png', dpi=200)
