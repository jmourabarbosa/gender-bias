"""Parse Spanish SIIU/EPU PC-Axis tables (PDI who read their thesis at the university where they teach) to long CSV; redraw."""
import re, csv, itertools, glob, os
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/home/user/gender-bias/other-biases-data/01-localism/LOC-11'
def parse(path):
    t = open(path, encoding='iso-8859-15').read()
    def strs(s): return re.findall(r'"((?:[^"])*)"', s)
    kv = {}
    for m in re.finditer(r'([A-Z\-]+(?:\("[^"]*"(?:,"[^"]*")?\))?)=(.*?);\s*(?=\n[A-Z]|\Z)', t, re.S):
        kv[m.group(1)] = m.group(2)
    stub = strs(kv['STUB']); head = strs(kv['HEADING'])
    vals = {k[8:-2]: [''.join(x) for x in re.findall(r'"([^"]*)"', v.replace('"\n"', ''))]
            for k, v in kv.items() if k.startswith('VALUES(')}
    data = kv['DATA'].split()
    dims = stub + head
    rows = []
    for combo, val in zip(itertools.product(*[vals[d] for d in dims]), data):
        rows.append(dict(zip(dims, combo), value=val))
    return kv['TITLE'].strip('"'), dims, rows
allrows = []
for f in sorted(glob.glob(f'{D}/data/*.px')):
    title, dims, rows = parse(f)
    out = f[:-3] + '.csv'
    with open(out, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=dims + ['value']); w.writeheader(); w.writerows(rows)
    print(os.path.basename(out), len(rows), dims)
    if 'tipo_centro_tot' in f: allrows = rows
pub = [r for r in allrows if r['Tipo de universidad'] == 'Pública' and r['Tipo de centro'] == 'Total']
same = [(r['Periodo'], float(r['value'])) for r in pub if 'universidad en la que' in r['Indicador']]
ccaa = [(r['Periodo'], float(r['value'])) for r in pub if 'CCAA' in r['Indicador']]
with open(f'{D}/data/LOC-11.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['curso', 'pct_pdi_thesis_same_university_public', 'pct_pdi_thesis_same_region_public'])
    for (p, a), (_, b) in zip(same, ccaa): w.writerow([p, a, b])
print(same, ccaa)
fig, ax = plt.subplots(figsize=(8, 4.8))
x = [p[:4] for p, _ in same]
ax.plot(x, [v for _, v in ccaa], '--s', color='0.5', label='PhD from a university in the same region')
ax.plot(x, [v for _, v in same], '-o', color='black', label='PhD from the same university')
for xi, (_, v) in zip(x, same): ax.annotate(f'{v:.1f}', (xi, v), textcoords='offset points', xytext=(0, -15), ha='center', fontsize=8)
ax.set_ylim(0, 100); ax.set_ylabel('% of teaching & research staff (PDI)')
ax.set_xlabel('Academic year starting'); ax.legend(frameon=False, loc='lower left', fontsize=9)
ax.set_title('Spain, public universities: staff teaching where they got their PhD', fontsize=11)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Source: Ministerio de Ciencia, Innovación y Universidades, SIIU - Estadística de Personal de las Universidades (PDITESIS)', fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f'{D}/figures/LOC-11_redraw.png', dpi=200)
