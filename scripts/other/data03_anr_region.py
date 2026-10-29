"""DATA-03: Île-de-France share of ANR (DOS/DGDS, ANR_01) funding by year, from partner-level allocations.
Year = AAP.Edition from the projects file (joined on Projet.Code_Decision) when available, else the year in the
decision code (ANR-YY-...). Only partners with Financement.Source == 'ANR' and a French address are counted."""
import csv, os, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-03"
P = f"{D}/data/anr-dgds-depuis-2010-partenaires.csv"
J = f"{D}/data/anr-dgds-depuis-2010-projets.csv"
edition = {}
if os.path.exists(J):
    for r in csv.DictReader(open(J, encoding="utf-8")):
        edition[r["Projet.Code_Decision"]] = r["AAP.Edition"]
agg = collections.defaultdict(lambda: collections.Counter())
for r in csv.DictReader(open(P, encoding="utf-8")):
    if r["Projet.Partenaire.Financement.Source"] != "ANR":
        continue
    amt = float(r["Projet.Partenaire.Aide_allouee.ANR"] or 0)
    code = r["Projet.Code_Decision"]
    y = int(edition.get(code) or (2000 + int(code[4:6])))
    reg, pays = r["Projet.Partenaire.Adresse.Region"], r["Projet.Partenaire.Adresse.Pays"]
    a = agg[y]
    a["total_eur"] += amt
    if reg:
        a["known_region_eur"] += amt
        if reg == "Île-de-France":
            a["idf_eur"] += amt
            a["idf_partners"] += 1
        a["known_region_partners"] += 1
    elif pays == "France":
        a["france_no_region_eur"] += amt
    else:
        a["foreign_or_unknown_eur"] += amt
rows = []
for y in sorted(agg):
    a = agg[y]
    rows.append(dict(year=y, total_anr_partner_eur=round(a["total_eur"]), known_region_eur=round(a["known_region_eur"]),
                     idf_eur=round(a["idf_eur"]), france_no_region_eur=round(a["france_no_region_eur"]),
                     foreign_or_unknown_eur=round(a["foreign_or_unknown_eur"]),
                     idf_share_of_known_region_pct=round(100 * a["idf_eur"] / a["known_region_eur"], 1) if a["known_region_eur"] else "",
                     pct_funding_with_region=round(100 * a["known_region_eur"] / a["total_eur"], 1) if a["total_eur"] else "",
                     idf_partners=a["idf_partners"], known_region_partners=a["known_region_partners"],
                     year_source="AAP.Edition" if edition else "decision code"))
with open(f"{D}/data/anr_region_share.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0]))
    w.writeheader()
    w.writerows(rows)
for r in rows:
    print(r["year"], r["idf_share_of_known_region_pct"], r["pct_funding_with_region"], round(r["total_anr_partner_eur"] / 1e6, 1))

ok = [r for r in rows if r["pct_funding_with_region"] and r["pct_funding_with_region"] >= 90]
low = [r for r in rows if r not in ok and r["idf_share_of_known_region_pct"] != ""]
fig, ax = plt.subplots(figsize=(7.5, 4.3))
ax.plot([r["year"] for r in ok], [r["idf_share_of_known_region_pct"] for r in ok], "o-", color="black", lw=2)
if low:
    ax.plot([r["year"] for r in low], [r["idf_share_of_known_region_pct"] for r in low], "o", color="white", mec="grey",
            label="<90% of funding has a region (not comparable)")
    ax.legend(frameon=False, fontsize=9, loc="lower left")
for r in ok:
    ax.text(r["year"], r["idf_share_of_known_region_pct"] + 0.8, f'{r["idf_share_of_known_region_pct"]:.0f}', ha="center", fontsize=8)
ax.axhline(18.8, color="grey", ls="--", lw=1)
ax.text(rows[0]["year"], 19.6, "Île-de-France share of French population (~19%)", fontsize=8, color="dimgrey")
ax.set_ylim(0, 50)
ax.set_ylabel("Île-de-France share of ANR funding\n(% of partner allocations with a region)", fontsize=10)
ax.set_xlabel("Call year (AAP edition)" if edition else "Year in ANR decision code", fontsize=10)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.text(0.01, 0.008, "Source: ANR_01 open data (data.gouv.fr), projects & partners since 2010, Aide_allouee.ANR by partner region; our computation",
         fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(f"{D}/figures/DATA-03_redraw.png", dpi=200)
