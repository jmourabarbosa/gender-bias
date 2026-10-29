"""DATA-02: Île-de-France share of IUF nominations (by period) + cross-dataset comparison figure
(IdF share of population, tenured staff (DATA-01), ANR funding (DATA-03), IUF nominations)."""
import csv, collections
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B = "/home/user/gender-bias/other-biases-data/10-datasets"
rows = list(csv.DictReader(open(f"{B}/DATA-02/data/fr-esr-iuf-les-membres.csv", encoding="utf-8-sig"), delimiter=";"))
per = collections.defaultdict(collections.Counter)
for r in rows:
    y = int(r["annee"]); p = f"{(y // 5) * 5}-{(y // 5) * 5 + 4}"
    for key in (p, "all"):
        per[key]["n"] += 1; per[key]["idf"] += r["reg_nom"] == "Île-de-France"; per[key]["known"] += bool(r["reg_nom"])
with open(f"{B}/DATA-02/data/DATA-02_iuf_idf_share.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["period", "nominations", "with_region", "ile_de_france", "idf_share_pct"])
    for k in sorted(per): w.writerow([k, per[k]["n"], per[k]["known"], per[k]["idf"], round(100 * per[k]["idf"] / per[k]["known"], 1)])
print(open(f"{B}/DATA-02/data/DATA-02_iuf_idf_share.csv").read())
# recent IUF (2020-2026)
rec = [r for r in rows if int(r["annee"]) >= 2020 and r["reg_nom"]]
iuf = 100 * sum(r["reg_nom"] == "Île-de-France" for r in rec) / len(rec)
anr = [r for r in csv.DictReader(open(f"{B}/DATA-03/data/anr_region_share.csv")) if 2020 <= int(r["year"]) <= 2025]
anr_share = 100 * sum(float(r["idf_eur"]) for r in anr) / sum(float(r["known_region_eur"]) for r in anr)
reg = collections.Counter(); tot = collections.Counter()
for r in csv.DictReader(open(f"{B}/DATA-01/data/DATA-01_by_year_region_category.csv")):
    if r["rentree"] == "2024" and r["code_categorie_assimil"] in ("MCF", "PR"):
        tot[r["code_categorie_assimil"]] += int(r["effectif"])
        if r["region"] == "Île-de-France": reg[r["code_categorie_assimil"]] += int(r["effectif"])
bars = [("Population\n(Insee 2024)", 18.2), ("Tenured MCF\n(2024)", 100 * reg["MCF"] / tot["MCF"]), ("Tenured PR\n(2024)", 100 * reg["PR"] / tot["PR"]),
        ("ANR funding\n(2020-2025)", anr_share), ("IUF nominations\n(2020-2026)", iuf)]
print(bars)
with open(f"{B}/DATA-02/data/DATA-02_idf_concentration_comparison.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["indicator", "idf_share_pct"]); [w.writerow([b[0].replace("\n", " "), round(b[1], 1)]) for b in bars]
fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.bar([b[0] for b in bars], [b[1] for b in bars], color=["white", "lightgrey", "grey", "dimgrey", "black"], edgecolor="black")
for i, b in enumerate(bars): ax.text(i, b[1] + 0.8, f"{b[1]:.0f}%", ha="center", fontsize=11)
ax.set_ylim(0, 50); ax.set_ylabel("Île-de-France share (%)", fontsize=10); ax.tick_params(axis="x", labelsize=9)
[ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.008, "Sources: Insee; MESR open data (tenured staff, IUF members); ANR_01 open data. Our computation (other-biases-data DATA-01/02/03)", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{B}/DATA-02/figures/DATA-02_redraw2_idf_concentration.png", dpi=200)
