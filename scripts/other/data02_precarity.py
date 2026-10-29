"""DATA-02: non-permanent teaching staff (MESR open data) by group and year, vs tenured staff (DATA-01); redraw."""
import csv, collections
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B = "/home/user/gender-bias/other-biases-data/10-datasets"
np_ = collections.Counter(); grp = collections.Counter()
for r in csv.DictReader(open(f"{B}/DATA-02/data/fr-esr-enseignants-nonpermanents-esr-public.csv", encoding="utf-8-sig"), delimiter=";"):
    n = int(r["effectif"] or 0); np_[r["rentree"]] += n; grp[(r["rentree"], r["categorie_pers_grp"] or "Non renseigné")] += n
ten = collections.Counter()
for r in csv.DictReader(open(f"{B}/DATA-01/data/DATA-01_by_year_region_category.csv")):
    ten[r["rentree"]] += int(r["effectif"])
years = sorted(set(np_) & set(ten))
with open(f"{B}/DATA-02/data/DATA-02_nonpermanent_vs_tenured.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["rentree", "nonpermanent_teaching_staff", "tenured_teaching_staff", "nonpermanent_share_pct"])
    for y in years: w.writerow([y, np_[y], ten[y], round(100 * np_[y] / (np_[y] + ten[y]), 1)])
with open(f"{B}/DATA-02/data/DATA-02_nonpermanent_by_group.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["rentree", "categorie_pers_grp", "effectif"]); [w.writerow([*k, grp[k]]) for k in sorted(grp)]
for y in years: print(y, np_[y], ten[y], round(100 * np_[y] / (np_[y] + ten[y]), 1))
groups = sorted({k[1] for k in grp}, key=lambda g: -grp[(years[-1], g)])
print(groups, [grp[(years[-1], g)] for g in groups])
fig, ax = plt.subplots(figsize=(7.5, 4.3))
ax.plot([int(y) for y in years], [np_[y] / 1000 for y in years], "o-", color="black", label="Non-permanent teaching staff")
ax.plot([int(y) for y in years], [ten[y] / 1000 for y in years], "s--", color="grey", label="Tenured teaching staff (MCF, PR, 2nd degree)")
ax.set_ylim(0, None); ax.set_ylabel("Head count (thousands)", fontsize=10); ax.set_xlabel("Rentrée", fontsize=10)
for y in (years[0], years[-1]):
    ax.annotate(f"{100*np_[y]/(np_[y]+ten[y]):.0f}% non-permanent", (int(y), np_[y] / 1000), xytext=(0, -20), textcoords="offset points", ha="left" if y == years[0] else "right", fontsize=8.5)
ax.legend(frameon=False, fontsize=9, loc="lower center", ncol=1)
[ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.008, "Source: MESR open data fr-esr-enseignants-nonpermanents-esr-public and fr-esr-enseignants-titulaires-esr-public; our computation", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{B}/DATA-02/figures/DATA-02_redraw.png", dpi=200)
