"""usage: python3 -I htmltext.py <html> [regex] -> plain text (or matches with context)"""
import sys, re, html
t = open(sys.argv[1], errors='ignore').read()
t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S | re.I)
t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
if len(sys.argv) > 2:
    for m in re.finditer(sys.argv[2], t): print('...', t[max(0, m.start()-250):m.end()+250], '\n')
else: print(t)
