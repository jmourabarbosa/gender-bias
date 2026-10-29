"""mesr_export.py OUTDIR dataset_id [...] -- full CSV export (';'-separated) of MESR Opendatasoft datasets
via /api/explore/v2.1/catalog/datasets/<id>/exports/csv?delimiter=%3B, plus metadata JSON; retries because the
host resets connections through the proxy; gzips files > 90 MB."""
import sys, os, time, gzip, shutil, requests
out = sys.argv[1]
B = "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/"
def dl(url, dest):
    for i in range(15):
        try:
            with requests.get(url, stream=True, timeout=(20, 300)) as r:
                if r.status_code != 200:
                    print("http", r.status_code, url, flush=True); time.sleep(5); continue
                with open(dest, "wb") as f:
                    for c in r.iter_content(1 << 16): f.write(c)
            return True
        except Exception as e:
            print("retry", i, repr(e)[:80], flush=True); time.sleep(min(4 + 4 * i, 40))
    return False
for ds in sys.argv[2:]:
    ok = dl(B + ds, f"{out}/{ds}.metadata.json") and dl(B + ds + "/exports/csv?delimiter=%3B", f"{out}/{ds}.csv")
    p = f"{out}/{ds}.csv"
    if ok and os.path.getsize(p) > 90e6:
        with open(p, "rb") as a, gzip.open(p + ".gz", "wb") as b: shutil.copyfileobj(a, b)
        os.remove(p); p += ".gz"
    print(ds, "OK" if ok else "FAILED", os.path.getsize(p) if ok else "", flush=True)
