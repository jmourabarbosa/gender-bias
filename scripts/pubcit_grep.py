"""Search PDF (or XML/HTML) text for patterns, printing page + context.
Usage: python3 -I pubcit_grep.py FILE PATTERN [PATTERN...]"""
import sys, re, html
f = sys.argv[1]
if f.endswith(".pdf"):
    import pymupdf
    pages = [p.get_text().replace("\n", " ") for p in pymupdf.open(f)]
else:
    t = open(f, errors="ignore").read()
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    pages = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))]
for pat in sys.argv[2:]:
    n = 0
    for i, t in enumerate(pages):
        for m in re.finditer(pat, t):
            print(f"[{pat}] p{i+1}: ...{t[max(0,m.start()-180):m.end()+180]}...")
            n += 1
            if n >= 3: break
        if n >= 3: break
