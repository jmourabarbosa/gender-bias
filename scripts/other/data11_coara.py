"""DATA-11: CoARA/DORA uptake by country from Pölönen & Rushforth ETER-CoARA dataset (Zenodo 17846515)."""
import csv, collections, openpyxl
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-11"
ws = openpyxl.load_workbook(f"{D}/data/eter_coara_dataset_2022.xlsx", read_only=True)["Data"]
rows = list(ws.iter_rows(values_only=True)); h = rows[0]; rows = [dict(zip(h, r)) for r in rows[1:] if r[0]]
one = lambda v: 1 if v == 1 else 0
agg = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    for key in (r["Country"], "ALL"):
        a = agg[key]; a["n"] += 1
        for c in ("CoARAsign2025", "COARAmemb2025", "CoARAactionplan", "DORA2025", "HR2025"): a[c] += one(r[c])
        if r["Classification - PhD status"] == 1:
            a["n_phd"] += 1; a["coara_phd"] += one(r["CoARAsign2025"]); a["dora_phd"] += one(r["DORA2025"])
out = []
for k, a in sorted(agg.items(), key=lambda kv: -kv[1]["n"]):
    out.append(dict(country=k, n_HEI=a["n"], CoARA_signatories=a["CoARAsign2025"], CoARA_members=a["COARAmemb2025"],
                    CoARA_action_plans=a["CoARAactionplan"], DORA_signatories=a["DORA2025"], HR_award=a["HR2025"],
                    n_PhD_awarding=a["n_phd"], CoARA_signatories_PhD_awarding=a["coara_phd"], DORA_signatories_PhD_awarding=a["dora_phd"],
                    pct_CoARA=round(100 * a["CoARAsign2025"] / a["n"], 1),
                    pct_CoARA_PhD_awarding=round(100 * a["coara_phd"] / a["n_phd"], 1) if a["n_phd"] else ""))
with open(f"{D}/data/DATA-11_by_country.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
for o in out:
    if o["country"] in ("ALL", "France", "Germany", "Spain", "Italy"): print(o)
# chart: PhD-awarding HEIs, countries with >= 15 such HEIs
sel = sorted([o for o in out if o["country"] != "ALL" and o["n_PhD_awarding"] >= 15], key=lambda o: o["pct_CoARA_PhD_awarding"])
fig, ax = plt.subplots(figsize=(7, 0.32 * len(sel) + 1.4))
cols = ["black" if o["country"] == "France" else "grey" for o in sel]
ax.barh([f'{o["country"]} (n={o["n_PhD_awarding"]})' for o in sel], [o["pct_CoARA_PhD_awarding"] for o in sel], color=cols)
for i, o in enumerate(sel): ax.text(o["pct_CoARA_PhD_awarding"] + 1, i, f'{o["pct_CoARA_PhD_awarding"]:.0f}%', va="center", fontsize=9)
ax.set_xlabel("% of PhD-awarding higher-education institutions that signed CoARA (2025)", fontsize=10)
ax.set_xlim(0, 105); [ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.005, "Source: Pölönen & Rushforth 2025, CoARA by numbers dataset (ETER 2022 + CoARA 2025), Zenodo 10.5281/zenodo.17846515; our computation",
         fontsize=6.5, color="dimgrey")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(f"{D}/figures/DATA-11_redraw.png", dpi=200)
