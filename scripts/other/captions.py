"""captions.py PDF [regex] -> list page, bbox and first chars of text blocks starting with Fig/Table (or regex)."""
import sys, re, pymupdf
pdf = sys.argv[1]
pat = re.compile(sys.argv[2] if len(sys.argv) > 2 else r'^\s*(Fig(ure|\.)?|FIG|Table|TABLE|Graphique|GRAPHIQUE|Carte|CARTE|Tableau|TABLEAU)\s*\.?\s*[0-9IVX]', re.I)
d = pymupdf.open(pdf)
print(pdf, 'pages', len(d), 'size', d[0].rect)
for i, p in enumerate(d):
    for b in p.get_text('blocks'):
        if pat.search(b[4]):
            print(i + 1, [round(v) for v in b[:4]], b[4][:110].replace('\n', ' '))
