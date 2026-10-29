"""usage: python3 -I pdfgrep.py <pdf> <regex> [ctx=200] -> page: context"""
import sys, re, pymupdf
d = pymupdf.open(sys.argv[1]); ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 200
for i, p in enumerate(d):
    t = re.sub(r'\s+', ' ', p.get_text())
    for m in re.finditer(sys.argv[2], t): print(f'p{i+1}:', t[max(0, m.start()-ctx):m.end()+ctx], '\n')
