"""Parse BiasWatchNeuro conference posts (fetched via the WordPress.com public REST API:
https://public-api.wordpress.com/wp/v2/sites/biaswatchneuro.com/posts?per_page=100&page=N)
into data/biaswatchneuro.csv. Usage: python3 -I biaswatchneuro_scrape.py all_posts.json out.csv"""
import csv, html, json, re, sys

posts = json.load(open(sys.argv[1]))

def text(h):
    h = re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</div>', '\n', h)
    t = html.unescape(re.sub(r'<[^>]+>', '', h)).replace('\xa0', ' ')
    return re.sub(r'\n\s*\n+', '\n', t)

RATIO = re.compile(r'^(?P<label>[^\n:]{0,80}?ratio[^\n:]{0,60}?)\s*:\s*(?P<w>\d+)\s*(?:women|woman|females?|w)\b\s*[:,/]?\s*(?P<m>\d+)\s*(?:men|man|males?|m)\b[^\n(]*(?:\((?P<p>[\d.]+)\s*%\))?',
                   re.I | re.M)
BASE = re.compile(r'base rate[^\n:]*:\s*(?:~|approx\.?|about)?\s*(?P<a>[\d.]+)\s*%?\s*(?:[-–—to]+\s*(?P<b>[\d.]+))?\s*%?', re.I)

def pick(matches):
    # prefer an overall line: "speaker gender ratio" incl. keynotes / invited / faculty; avoid keynote-only lines
    def score(m):
        l = m.group('label').lower()
        s = 0
        if 'keynote speaker' in l and 'incl' not in l: s -= 5
        if 'organi' in l or 'committee' in l or 'chair' in l: s -= 4
        if 'speaker' in l or 'faculty' in l or 'invited' in l or 'lecturer' in l or 'presenter' in l: s += 2
        if 'incl' in l or 'total' in l or 'overall' in l: s += 1
        return s
    return max(matches, key=lambda m: (score(m), -matches.index(m)))

rows, skipped = [], 0
for p in posts:
    t = text(p['content']['rendered'])
    ms = list(RATIO.finditer(t))
    if not ms:
        skipped += 1
        continue
    m = pick(ms)
    w, n_m = int(m.group('w')), int(m.group('m'))
    n = w + n_m
    if n == 0:
        skipped += 1
        continue
    title = html.unescape(re.sub(r'<[^>]+>', '', p['title']['rendered'])).replace('\xa0', ' ').strip()
    yr = re.search(r'\b(19[89]\d|20[0-3]\d)\b', title)
    year = int(yr.group(1)) if yr else int(p['date'][:4])
    b = BASE.search(t)
    base = raw = ''
    if b:
        a = float(b.group('a')); bb = float(b.group('b')) if b.group('b') else None
        if bb is not None and bb >= a and bb <= 100:
            base = round((a + bb) / 2, 1); raw = f'{b.group("a")}-{b.group("b")}%'
        elif a <= 100:
            base = a; raw = f'{b.group("a")}%'
    rows.append(dict(conference=title, year=year, n_speakers=n, n_women=w,
                     pct_women=round(100 * w / n, 1), base_rate_pct=base, url=p['link'],
                     ratio_label=m.group('label').strip(), pct_reported=m.group('p') or '',
                     base_rate_raw=raw, post_date=p['date'][:10],
                     flag=('reported_pct_disagrees_with_counts' if m.group('p') and abs(float(m.group('p')) - 100 * w / n) > 3 else '')))

rows.sort(key=lambda r: (r['post_date'], r['conference']))
cols = ['conference', 'year', 'n_speakers', 'n_women', 'pct_women', 'base_rate_pct', 'url',
        'ratio_label', 'pct_reported', 'base_rate_raw', 'post_date', 'flag']
with open(sys.argv[2], 'w', newline='') as f:
    wr = csv.DictWriter(f, cols); wr.writeheader(); wr.writerows(rows)
print(f'{len(posts)} posts, {len(rows)} conference rows, {skipped} posts without a parseable ratio line')
