"""Recover Mantel-Haenszel odds ratios per CNU section from the vector Figure 1 (PDF p.15) of Godechot et al. 2025.
x-axis is log scale; calibrated on tick labels. Markers = filled squares/circles (2.9pt); CI caps = vertical 2.6pt strokes."""
import sys, re, math, csv, pymupdf
D = '/home/user/gender-bias/other-biases-data/01-localism/LOC-06'
p = pymupdf.open(f'{D}/source.pdf')[14]
ticks = {}
for w in p.get_text('words'):
    if re.fullmatch(r'\d+\.\d', w[4]) and w[1] > 740: ticks[float(w[4])] = (w[0] + w[2]) / 2
xs = sorted(ticks.items())
# least squares x = a + b*log(v)
n = len(xs); lx = [math.log(v) for v, _ in xs]; px = [x for _, x in xs]
mb = sum(lx) / n; mp = sum(px) / n
b = sum((l - mb) * (q - mp) for l, q in zip(lx, px)) / sum((l - mb) ** 2 for l in lx); a = mp - b * mb
resid = max(abs(a + b * l - q) for l, q in zip(lx, px))
inv = lambda x: math.exp((x - a) / b)
dr = p.get_drawings()
marks = [d['rect'] for d in dr if d['type'] == 'f' and abs(d['rect'].width - 2.9) < 0.3]
caps = [d['rect'] for d in dr if d['type'] == 's' and d['rect'].width < 0.1 and abs(d['rect'].height - 2.6) < 0.2]
labels = []
for bl in p.get_text('blocks'):
    for line in bl[4].strip().split('\n'):
        pass
for l in p.get_text('dict')['blocks']:
    for li in l.get('lines', []):
        t = ''.join(s['text'] for s in li['spans']).strip()
        m = re.match(r'(\d+)\. (.+) \((\d+)-(\d+)-([\d.]+)\)$', t)
        if m: labels.append(((li['bbox'][1] + li['bbox'][3]) / 2, m.groups()))
rows = []
for yc, (sec, name, nrec, nloc, nexp) in sorted(labels):
    mk = min(marks, key=lambda r: abs((r.y0 + r.y1) / 2 - yc))
    cy = (mk.y0 + mk.y1) / 2
    cp = sorted([r for r in caps if abs((r.y0 + r.y1) / 2 - cy) < 1.5], key=lambda r: r.x0)
    lo = inv(cp[0].x0) if len(cp) >= 2 else ''
    hi = inv(cp[-1].x0) if len(cp) >= 2 else ''
    rows.append([int(sec), name, int(nrec), int(nloc), float(nexp), round(inv((mk.x0 + mk.x1) / 2), 1),
                 round(lo, 1) if lo else '', round(hi, 1) if hi else '', round(abs(cy - yc), 1)])
with open(f'{D}/data/LOC-06.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['cnu_section', 'section_label', 'n_recrues', 'n_recrues_locales', 'recrues_locales_attendues',
                'mh_odds_ratio_digitized', 'ci_low_digitized', 'ci_high_digitized', 'row_match_offset_pt'])
    w.writerows(rows)
print('axis calib max residual (pt):', round(resid, 2), 'markers', len(marks), 'caps', len(caps), 'labels', len(labels))
for r in rows: print(r)
