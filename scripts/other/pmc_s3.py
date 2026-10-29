"""pmc_s3.py PMCID OUTDIR -- fetch latest version of a PMC article from the pmc-oa-opendata S3 bucket
(source.pdf, article.xml/json, figure JPGs into figures/)."""
import sys, re, os, requests
pmc, out = sys.argv[1], sys.argv[2]
S3 = "https://pmc-oa-opendata.s3.amazonaws.com"
keys = re.findall(r"<Key>([^<]+)</Key>", requests.get(f"{S3}/?list-type=2&prefix={pmc}.", timeout=60).text)
latest = sorted({k.split("/")[0] for k in keys}, key=lambda v: int(v.split(".")[-1]))[-1]
os.makedirs(f"{out}/figures", exist_ok=True)
for k in keys:
    if not k.startswith(latest + "/"): continue
    n = k.split("/")[1]
    if n.endswith(".txt"): continue
    dest = (f"{out}/figures/{n}" if n.endswith((".jpg", ".png", ".gif")) else f"{out}/source.pdf" if n.endswith(".pdf")
            else f"{out}/article{os.path.splitext(n)[1]}" if n.endswith((".xml", ".json")) else f"{out}/supplementary/{n}")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    r = requests.get(f"{S3}/{k}", timeout=120); r.raise_for_status()
    open(dest, "wb").write(r.content); print(dest, len(r.content))
