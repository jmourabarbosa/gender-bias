"""DATA-04: host-country grant counts from ERC call statistics PDFs (page 'Grantees by Country of Host Institution');
values and country codes are read from the chart text layer and checked against the stated total; plus redraw."""
import re, glob, csv, pymupdf
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-04"
files = sorted(glob.glob(f"{D}/data/erc-*-statistics.pdf")) + [f"{D}/source.pdf"]
out = []
for f in files:
    doc = pymupdf.open(f)
    for p in doc:
        t = p.get_text()
        if "Country of Host Institution" not in t: continue
        call = re.search(r"ERC (\w+) Grants? (\d{4})", t); total = int(re.search(r"Total (\d+) grants", t).group(1))
        body = t.split("grants", 1)[1]
        toks = re.findall(r"\b[A-Z]{2}\b|\b\d+\b", body)
        codes = [x for x in toks if x.isalpha()]
        nums = [int(x) for x in toks if x.isdigit()]
        n = len(codes)
        # drop the page number if present (leading small number not part of values), then take values until axis ticks (0,...)
        for start in range(0, 3):
            vals = nums[start:start + n]
            if sum(vals) == total and vals == sorted(vals, reverse=True): break
        else:
            raise SystemExit(f"cannot parse {f}")
        name = f"{call.group(1)}{call.group(2)}"
        for c, v in zip(codes, vals): out.append(dict(call=name, host_country=c, grants=v, share_pct=round(100 * v / total, 1), call_total=total, page=doc.page_count and p.number + 1, file=f.split("/")[-1]))
        print(name, total, "FR:", dict(zip(codes, vals)).get("FR"))
with open(f"{D}/data/erc_host_country.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, list(out[0])); w.writeheader(); w.writerows(out)
calls = sorted({o["call"] for o in out}, key=lambda s: (s[-4:], s))
top = ["DE", "UK", "FR", "NL", "CH", "ES", "IT"]
fig, ax = plt.subplots(figsize=(7.5, 4.2))
wd = 0.8 / len(calls); greys = ["black", "dimgrey", "darkgrey", "lightgrey"]
for i, c in enumerate(calls):
    d = {o["host_country"]: o["share_pct"] for o in out if o["call"] == c}
    ax.bar([j + i * wd for j in range(len(top))], [d.get(k, 0) for k in top], wd, color=greys[i % 4], edgecolor="black", label=c)
ax.set_xticks([j + wd * (len(calls) - 1) / 2 for j in range(len(top))], top)
ax.set_ylabel("% of ERC grants hosted", fontsize=10); ax.legend(frameon=False, fontsize=8)
[ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.008, "Source: ERC call statistics PDFs (StG/CoG/AdG 2025, StG 2026), 'Grantees by Country of Host Institution'; our transcription", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{D}/figures/DATA-04_redraw.png", dpi=200)
