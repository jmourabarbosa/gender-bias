"""tabular_pager.py RESOURCE_ID OUT.csv [comma-separated columns]
Pages through https://tabular-api.data.gouv.fr/api/resources/<rid>/data/ (page_size=200) with retries
(static.data.gouv.fr resets every connection through this proxy) and writes a CSV."""
import sys, csv, time, requests
rid, out = sys.argv[1], sys.argv[2]
cols = sys.argv[3] if len(sys.argv) > 3 else None
base = f"https://tabular-api.data.gouv.fr/api/resources/{rid}/data/"
def get(page):
    p = {"page": page, "page_size": 200}
    if cols: p["columns"] = cols
    for i in range(30):
        try:
            r = requests.get(base, params=p, timeout=(20, 90))
            if r.status_code == 200: return r.json()
            print("http", r.status_code, page, flush=True)
        except Exception as e:
            pass
        time.sleep(min(2 + 2 * i, 30))
    raise SystemExit(f"gave up on page {page}")
d = get(1); total = d["meta"]["total"]; npages = -(-total // 200)
fields = [k for k in d["data"][0] if k != "__id"]
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fields, extrasaction="ignore"); w.writeheader()
    w.writerows(d["data"]); n = len(d["data"])
    for pg in range(2, npages + 1):
        d = get(pg); w.writerows(d["data"]); n += len(d["data"])
        if pg % 25 == 0: print(pg, "/", npages, flush=True)
print("done", n, "of", total, out)
