"""fetch_retry.py URL OUT [tries=8]  -- streaming download with retries/backoff (flaky proxy tunnel)."""
import sys, time, requests
url, out = sys.argv[1], sys.argv[2]
tries = int(sys.argv[3]) if len(sys.argv) > 3 else 8
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
for i in range(tries):
    try:
        with requests.get(url, headers=UA, stream=True, timeout=(30, 120), allow_redirects=True) as r:
            print("HTTP", r.status_code, r.headers.get("content-type"), r.headers.get("content-length"), flush=True)
            if r.status_code != 200:
                if r.status_code in (403, 404, 410, 429): sys.exit(1)
                raise RuntimeError(r.status_code)
            n = 0
            with open(out, "wb") as f:
                for c in r.iter_content(1 << 16):
                    f.write(c); n += len(c)
            cl = r.headers.get("content-length")
            if cl and not r.headers.get("content-encoding") and int(cl) != n: raise RuntimeError(f"short {n}/{cl}")
            print("ok", n, out); sys.exit(0)
    except SystemExit: raise
    except Exception as e:
        print("try", i, "fail", repr(e)[:150], flush=True); time.sleep(5 * (i + 1))
sys.exit(2)
