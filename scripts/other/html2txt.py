import sys, re, html
t = open(sys.argv[1], errors='ignore').read()
t = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', t)
t = re.sub(r'(?s)<[^>]+>', ' ', t)
t = html.unescape(t)
t = re.sub(r'[ \t\r\f\v]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
print(t)
