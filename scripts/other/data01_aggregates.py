"""DATA-01: non-gender aggregates of the MESR tenured-staff file (copied from gender-bias-data):
year x region x category, year x age class x category; redraw = Île-de-France share of MCF/PR over time."""
import csv, gzip, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-01"
reg, age = collections.Counter(), collections.Counter()
with gzip.open(f"{D}/data/fr-esr-enseignants-titulaires-esr-public.csv.gz", "rt", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        n = int(r["effectif"] or 0)
        cat = r["code_categorie_assimil"]
        reg[(r["rentree"], r["etablissement_region"], cat)] += n
        age[(r["rentree"], r["classe_age3"], cat)] += n
for name, c, col in (("by_year_region_category", reg, "region"), ("by_year_age_category", age, "classe_age3")):
    with open(f"{D}/data/DATA-01_{name}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rentree", col, "code_categorie_assimil", "effectif"])
        for k in sorted(c):
            w.writerow([*k, c[k]])
years = sorted({k[0] for k in reg})
share = {}
for cat in ("MCF", "PR"):
    share[cat] = []
    for y in years:
        tot = sum(v for k, v in reg.items() if k[0] == y and k[2] == cat)
        idf = sum(v for k, v in reg.items() if k[0] == y and k[2] == cat and k[1] == "Île-de-France")
        share[cat].append(100 * idf / tot)
    print(cat, [round(s, 1) for s in share[cat]])
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot([int(y) for y in years], share["PR"], "o-", color="black", label="Professeurs (PR)")
ax.plot([int(y) for y in years], share["MCF"], "s--", color="grey", label="Maîtres de conférences (MCF)")
for cat in ("PR", "MCF"):
    ax.text(int(years[-1]) + 0.2, share[cat][-1], f"{share[cat][-1]:.1f}%", va="center", fontsize=9)
ax.set_ylim(0, 40)
ax.set_ylabel("% of tenured staff in Île-de-France\ninstitutions", fontsize=10)
ax.set_xlabel("Rentrée (academic year start)", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="lower left")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.text(0.01, 0.008, "Source: MESR-SIES/DGRH open data fr-esr-enseignants-titulaires-esr-public (head counts by institution region); our computation",
         fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(f"{D}/figures/DATA-01_redraw.png", dpi=200)
