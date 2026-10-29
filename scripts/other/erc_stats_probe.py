"""Probe erc.europa.eu/system/files/<YYYY-MM>/erc-<year>-<type>-statistics.pdf for StG/CoG/AdG calls (result month unknown)."""
import requests, sys
out = sys.argv[1]
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/124.0"}
for year in range(2021, 2027):
    for t in ("stg", "cog", "adg"):
        found = None
        for y in (year - 1, year, year + 1):
            for m in range(1, 13):
                u = f"https://erc.europa.eu/system/files/{y}-{m:02d}/erc-{year}-{t}-statistics.pdf"
                try:
                    r = requests.head(u, headers=H, timeout=20, allow_redirects=True)
                except Exception:
                    continue
                if r.status_code == 200 and "pdf" in r.headers.get("content-type", ""):
                    found = u; break
            if found: break
        print(year, t, found, flush=True)
        if found:
            r = requests.get(found, headers=H, timeout=60)
            open(f"{out}/erc-{year}-{t}-statistics.pdf", "wb").write(r.content)
