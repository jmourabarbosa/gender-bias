"""Build data CSVs and greyscale redraws for 05-prestige / 06-geography.
Run: python3 -I scripts/other/presgeo_redraw.py   (reads source files, writes data/*.csv, figures/*_redraw.png)
"""
import csv, collections
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = Path("/home/user/gender-bias/other-biases-data")
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#444", "axes.labelcolor": "#111", "xtick.color": "#333", "ytick.color": "#333"})
DARK, MID, LIGHT = "#222222", "#888888", "#cccccc"


def wcsv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)


def finish(fig, out, source):
    fig.text(0.01, 0.01, "Source: " + source, fontsize=8, color="#555", ha="left", va="bottom")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=200); plt.close(fig)


def hbar(ax, labels, values, colors, fmt="{:.1f}", xlabel=""):
    y = range(len(labels))
    ax.barh(list(y), values, color=colors, height=0.65, edgecolor="white", linewidth=1)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels); ax.invert_yaxis()
    m = max(values)
    for i, v in enumerate(values):
        ax.text(v + m * 0.01, i, fmt.format(v), va="center", fontsize=10, color="#111")
    ax.set_xlim(0, m * 1.15); ax.set_xlabel(xlabel)
    ax.xaxis.grid(True, color="#e5e5e5"); ax.set_axisbelow(True)


# ---------------- PRES-01 Huber et al. 2022, Fig. 1 -----------------
d = R / "05-prestige/PRES-01"
rows = [("AL (less-known author shown)", 65.4, 24.8, 7.9, 2.0),
        ("AA (anonymized)", 48.2, 28.2, 21.8, 1.8),
        ("AH (Nobel laureate shown)", 22.5, 18.6, 38.2, 20.6)]
wcsv(d / "data/PRES-01.csv", ["condition", "reject_pct", "major_revision_pct", "minor_revision_pct", "accept_pct", "source"],
     [r + ("Huber et al. 2022 PNAS, Fig. 1 data labels (PDF p.3)",) for r in rows])
fig, ax = plt.subplots(figsize=(9, 3.6))
cols = [DARK, MID, LIGHT, "#f2f2f2"]; names = ["Reject", "Major revision", "Minor revision", "Accept"]
for i, r in enumerate(rows):
    left = 0
    for j, v in enumerate(r[1:]):
        ax.barh(i, v, left=left, color=cols[j], edgecolor="white", linewidth=2, height=0.6, label=names[j] if i == 0 else None)
        if v >= 6:
            ax.text(left + v / 2, i, f"{v:.0f}%", ha="center", va="center", color="white" if j < 2 else "#111", fontsize=10)
        left += v
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in rows]); ax.invert_yaxis()
ax.set_xlim(0, 100); ax.set_xlabel("% of reviewers' recommendations")
ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.45, 1.18), frameon=False, fontsize=9)
ax.set_title("Same paper, different author shown: reviewers' recommendations", pad=28, fontsize=12)
finish(fig, d / "figures/PRES-01_redraw.png", "Huber et al. 2022, PNAS 119(41):e2205779119, Fig. 1 (n=534 reviews)")

# ---------------- PRES-05 Clauset et al. 2015: Lorenz curves from Datasets 1-6 -----------------
d = R / "05-prestige/PRES-05"; ds = d / "supplementary/datasets"
curves, summary = [], []
fig, ax = plt.subplots(figsize=(6, 6))
for name, f, ls in [("Computer science", "Dataset 3. ComputerScience_edgelist.txt", "-"),
                    ("Business", "Dataset 1. Business_edgelist.txt", "--"),
                    ("History", "Dataset 5. History_edgelist.txt", ":")]:
    vfile = f.replace("edgelist", "vertexlist").replace("Dataset 3.", "Dataset 4.").replace("Dataset 1.", "Dataset 2.").replace("Dataset 5.", "Dataset 6.")
    nv = sum(1 for l in open(ds / vfile) if l.strip() and not l.startswith("#")) - 1  # drop the 'All others' (out-of-sample) vertex
    prod = collections.Counter()
    for l in open(ds / f):
        if l.startswith("#") or not l.strip():
            continue
        u = l.split("\t")[0]
        if int(u) <= nv:  # PhD from an in-sample institution
            prod[u] += 1
    counts = sorted([prod.get(str(i), 0) for i in range(1, nv + 1)], reverse=True)
    tot = sum(counts); xs, ys, c = [0], [0], 0
    for i, v in enumerate(counts, 1):
        c += v; xs.append(100 * i / nv); ys.append(100 * c / tot)
        curves.append((name, i, round(100 * i / nv, 3), round(100 * c / tot, 3)))
    k = round(0.25 * nv); top25 = 100 * sum(counts[:k]) / tot
    summary.append((name, nv, tot, k, round(top25, 1)))
    ax.plot(xs, ys, ls, color=DARK, lw=2, label=f"{name}: top 25% → {top25:.0f}%")
ax.plot([0, 100], [0, 100], color=MID, lw=1)
ax.axvline(25, color=LIGHT, lw=1)
ax.set_xlabel("% of institutions (ranked by faculty produced)"); ax.set_ylabel("% of all tenure-track faculty produced")
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.legend(frameon=False, loc="lower right", fontsize=9)
ax.set_title("Faculty production is concentrated (US, 2011-13)", fontsize=12)
finish(fig, d / "figures/PRES-05_redraw.png", "Clauset, Arbesman & Larremore 2015, Sci. Adv. 1:e1400005, Datasets 1-6 (recomputed)")
wcsv(d / "data/PRES-05_lorenz.csv", ["discipline", "rank", "pct_institutions", "cum_pct_faculty_produced"], curves)
wcsv(d / "data/PRES-05_top25_share.csv", ["discipline", "n_institutions", "n_faculty_edges", "top25pct_n", "top25pct_share_of_faculty"], summary)
print("PRES-05", summary)

# ---------------- PRES-06 Wapman et al. 2022: Lorenz from Fig. 2 source data -----------------
d = R / "05-prestige/PRES-06"
el = collections.defaultdict(dict)
for x in csv.DictReader(open(d / "supplementary/41586_2022_5222_MOESM4_ESM.csv")):
    el[(x["Subfigure"], int(x["Element"]))][x["Attribute"]] = x["Value"]
A = sorted((float(v["X"]), float(v["Y"])) for (s, e), v in el.items() if s == "A")
xs, ys, c = [0], [0], 0
rowsA = []
for xv, yv in A:
    c += yv; xs.append(xv + (100 / len(A))); ys.append(c); rowsA.append(("Academia", round(xv + 100 / len(A), 4), round(c, 4)))
B = collections.defaultdict(list)
for (s, e), v in el.items():
    if s == "B" and v.get("TaxonomyLevel") == "Umbrella":
        B[v["TaxonomyValue"]].append((float(v["X"]) * 100, float(v["Y"]) * 100))
fig, ax = plt.subplots(figsize=(6, 6))
for dom, pts in sorted(B.items()):
    pts = sorted(pts)
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=LIGHT, lw=1)
    rowsA += [(dom, round(p[0], 4), round(p[1], 4)) for p in pts]
ax.plot(xs, ys, color=DARK, lw=2.2, label="All of academia")
ax.plot([], [], color=LIGHT, lw=1, label="8 domains")
ax.plot([0, 100], [0, 100], color=MID, lw=1)
x80 = next(xv for xv, yv in zip(xs, ys) if yv >= 80)
ax.plot([x80], [80], "o", color=DARK, ms=8)
ax.annotate(f"80% of faculty trained at\n{x80:.1f}% of universities", (x80, 80), (x80 + 12, 55), fontsize=10,
            arrowprops=dict(arrowstyle="-", color="#555"))
ax.set_xlabel("% of US universities (ranked by faculty produced)"); ax.set_ylabel("% of US-trained faculty produced")
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.legend(frameon=False, loc="lower right")
ax.set_title("US faculty production (2011-2020 census)", fontsize=12)
finish(fig, d / "figures/PRES-06_redraw.png", "Wapman et al. 2022, Nature 610:120, Fig. 2 source data (MOESM4)")
wcsv(d / "data/PRES-06_lorenz.csv", ["curve", "pct_universities", "cum_pct_faculty_produced"], rowsA)
print("PRES-06 x80", x80)

# ---------------- PRES-07 IdF share of publications -----------------
d = R / "05-prestige/PRES-07"
wcsv(d / "data/PRES-07.csv", ["region", "share_of_french_publications_pct", "year", "source"],
     [("Île-de-France", 34.5, 2019, "MESR Strater/diagnostic territorial Île-de-France (2023-11), p.3, citing OST data"),
      ("Rest of France", 65.5, 2019, "computed as 100 - 34.5")])
fig, ax = plt.subplots(figsize=(7, 2.6))
hbar(ax, ["Île-de-France", "Rest of France (12 other regions + overseas)"], [34.5, 65.5], [DARK, LIGHT], fmt="{:.1f}%",
     xlabel="% of French scientific publications (2019)")
ax.set_title("Île-de-France: a third of French publications", fontsize=11)
finish(fig, d / "figures/PRES-07_redraw.png", "MESR, diagnostic territorial Île-de-France (Nov 2023), OST data for 2019")

# ---------------- PRES-08 business R&D by region -----------------
d = R / "05-prestige/PRES-08"
reg = [("Île-de-France", 17.52), ("Auvergne-Rhône-Alpes", 6.92), ("Occitanie", 4.23), ("Provence-Alpes-Côte d'Azur", 2.63),
       ("Nouvelle-Aquitaine", 2.10), ("Pays de la Loire", 1.42), ("Hauts-de-France", 1.35), ("Bretagne", 1.33),
       ("Grand Est", 1.18), ("Bourgogne-Franche-Comté", 1.16), ("Normandie", 1.03), ("Centre-Val de Loire", 0.99), ("Corse", 0.01)]
tot = sum(v for _, v in reg)
wcsv(d / "data/PRES-08.csv", ["region", "dirde_2024p_bn_eur", "share_of_metro_total_pct", "source"],
     [(r, v, round(100 * v / tot, 1), "MESRE-SIES Note Flash 2026-06, Carte 1 (PDF p.2)") for r, v in reg] +
     [("Total metropolitan (sum of map)", round(tot, 2), 100.0, "sum; note gives 41.9 bn total incl. all France")])
fig, ax = plt.subplots(figsize=(8, 5.2))
hbar(ax, [r for r, _ in reg], [v for _, v in reg], [DARK] + [MID] * (len(reg) - 1), fmt="{:.2f}", xlabel="Business R&D spending 2024 (provisional), bn €")
ax.set_title(f"Île-de-France = {100*17.52/tot:.0f}% of business R&D in France", fontsize=12)
finish(fig, d / "figures/PRES-08_redraw.png", "MESRE-SIES, Note Flash n°06, avril 2026, Carte 1")

# ---------------- PRES-09 ERC StG 2024 hosts -----------------
d = R / "05-prestige/PRES-09"
hosts = [("CNRS", 25, "national research organisation"), ("Inria", 3, "national research organisation"),
         ("Inserm", 2, "national research organisation"), ("École polytechnique", 2, "school")]
others = [("Sorbonne Université", "university"), ("Université de Haute-Alsace", "university"),
          ("Université de Versailles Saint-Quentin-en-Yvelines", "university"), ("Université Paris-Saclay", "university"),
          ("Université de Bordeaux", "university"), ("Université de Lorraine", "university"), ("Université Claude Bernard Lyon 1", "university"),
          ("Université de Rennes", "university"), ("Fondation nationale des sciences politiques (Sciences Po)", "foundation/association"),
          ("Fondation Jean-Jacques Laffont - TSE", "foundation/association"), ("Armines", "foundation/association"),
          ("École normale supérieure (ENS)", "school"), ("ENSAI", "school"), ("Institut Pasteur", "institute"),
          ("Institut du cerveau (ICM)", "institute"), ("Observatoire de la Côte d'Azur", "observatory"), ("CEA", "national research organisation")]
allh = hosts + [(n, 1, t) for n, t in others]
assert sum(h[1] for h in allh) == 49
wcsv(d / "data/PRES-09_erc_stg2024_france_hosts.csv", ["host_institution", "count", "type"], allh)
fig, ax = plt.subplots(figsize=(7, 3.2))
lab = ["CNRS", "Inria", "Inserm", "École polytechnique", "17 other hosts (1 each)"]
hbar(ax, lab, [25, 3, 2, 2, 17], [DARK, MID, MID, MID, LIGHT], fmt="{:.0f}", xlabel="ERC Starting Grants 2024 hosted in France (n = 49)")
ax.set_title("Half of France's ERC StG 2024 winners are hosted by the CNRS", fontsize=12)
finish(fig, d / "figures/PRES-09_redraw.png", "horizon-europe.gouv.fr, Résultats de l'appel ERC Starting Grants 2024")

# ---------------- PRES-10 Idex season 1 -----------------
d = R / "05-prestige/PRES-10"
idex = [("Bordeaux", "Nouvelle-Aquitaine"), ("Strasbourg", "Grand Est"), ("PSL (Paris Sciences et Lettres)", "Île-de-France"),
        ("Sorbonne Universités", "Île-de-France"), ("Sorbonne Paris Cité", "Île-de-France"), ("Paris-Saclay", "Île-de-France"),
        ("Aix-Marseille", "Provence-Alpes-Côte d'Azur"), ("Toulouse", "Occitanie")]
wcsv(d / "data/PRES-10.csv", ["idex_season1_winner", "region", "source"], [i + ("L'Etudiant/EducPros, Idex bilan saison 1",) for i in idex])
fig, ax = plt.subplots(figsize=(7, 2.4))
hbar(ax, ["Île-de-France", "Rest of France"], [4, 4], [DARK, LIGHT], fmt="{:.0f} of 8", xlabel="First-wave Idex winners (2011-2012)")
ax.set_xlim(0, 5.2)
ax.set_title("Half of the first 8 Idex went to the Paris region", fontsize=12)
finish(fig, d / "figures/PRES-10_redraw.png", "L'Etudiant/EducPros, 'Idex : des milliards qui coûtent cher' (2014)")

# ---------------- GEO-03 Harris et al. 2017, Table 2 -----------------
d = R / "06-geography/GEO-03"
t2 = [("1 DOTS tuberculosis RCT", "Strength", 50.9, 50.3, -0.54, -3.32, 2.25), ("1 DOTS tuberculosis RCT", "Relevance", 26.4, 29.1, 2.69, 0.27, 5.11),
      ("1 DOTS tuberculosis RCT", "Recommendation", 27.3, 29.9, 2.76, 0.27, 5.26),
      ("2 HIV services cross-sectional", "Strength", 42.9, 44.9, 1.97, -0.52, 4.46), ("2 HIV services cross-sectional", "Relevance", 24.3, 29.7, 5.51, 3.01, 8.02),
      ("2 HIV services cross-sectional", "Recommendation", 26.3, 27.6, 1.30, -1.11, 3.70),
      ("3 Rosuvastatin RCT", "Strength", 55.8, 59.8, 3.98, 1.16, 6.79), ("3 Rosuvastatin RCT", "Relevance", 34.4, 42.4, 8.09, 5.34, 10.84),
      ("3 Rosuvastatin RCT", "Recommendation", 33.6, 39.0, 5.50, 2.75, 8.25),
      ("4 Methadone cross-sectional", "Strength", 39.5, 39.5, 0.10, -2.63, 2.83), ("4 Methadone cross-sectional", "Relevance", 25.8, 27.9, 2.00, -0.48, 4.47),
      ("4 Methadone cross-sectional", "Recommendation", 24.5, 27.6, 3.07, 0.54, 5.60),
      ("Combined", "Strength", 47.3, 49.4, 1.35, -0.06, 2.76), ("Combined", "Relevance", 27.7, 33.4, 4.50, 3.16, 5.83),
      ("Combined", "Recommendation", 27.9, 32.1, 3.05, 1.77, 4.33)]
wcsv(d / "data/GEO-03.csv", ["abstract", "criterion", "mean_low_income_source", "mean_high_income_source", "diff_fe", "ci_low", "ci_high", "source"],
     [r + ("Harris et al. 2017 Health Affairs, accepted manuscript Table 2 (PDF pp.36-37); scale 0-100, n=347",) for r in t2])
comb = [r for r in t2 if r[0] == "Combined"]
fig, ax = plt.subplots(figsize=(7.5, 3.8))
import numpy as np
x = np.arange(3); w = 0.36
ax.bar(x - w / 2, [r[2] for r in comb], w, color=LIGHT, edgecolor="white", label="Same abstract attributed to a low-income country")
ax.bar(x + w / 2, [r[3] for r in comb], w, color=DARK, edgecolor="white", label="... attributed to a high-income country")
for i, r in enumerate(comb):
    ax.text(i - w / 2, r[2] + 0.8, f"{r[2]:.1f}", ha="center", fontsize=10)
    ax.text(i + w / 2, r[3] + 0.8, f"{r[3]:.1f}", ha="center", fontsize=10)
ax.set_xticks(x); ax.set_xticklabels(["Strength of evidence\n(+1.35, n.s.)", "Relevance\n(+4.50***)", "Would recommend\nto a peer (+3.05***)"])
ax.set_ylabel("Mean rating (0-100)"); ax.set_ylim(0, 60); ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.set_title("347 English clinicians rated the same 4 abstracts twice", fontsize=12)
finish(fig, d / "figures/GEO-03_redraw.png", "Harris et al. 2017, Health Affairs 36(11):1997, Table 2 (within-person fixed effects)")

# ---------------- GEO-04 Harris et al. 2017 IAT categories (Table 3) -----------------
d = R / "06-geography/GEO-04"
iat = [("Moderate pro-poor", 4, 1.25, -0.509), ("Slight pro-poor", 8, 2.49, -0.232), ("Neutral", 32, 9.97, 0.017),
       ("Slight pro-rich", 43, 13.4, 0.251), ("Moderate pro-rich", 94, 29.28, 0.515), ("Strong pro-rich", 67, 20.87, 0.748),
       ("Very strong pro-rich", 73, 22.74, 1.038)]
wcsv(d / "data/GEO-04.csv", ["iat_category", "n", "pct", "mean_d", "source"], [r + ("Harris et al. 2017 Global Health 13:80, Table 3 (PDF p.5); total n=321, mean d=0.57 (0.52-0.61)",) for r in iat])
fig, ax = plt.subplots(figsize=(8, 3.8))
cols = [LIGHT, LIGHT, MID, DARK, DARK, DARK, DARK]
ax.bar(range(7), [r[2] for r in iat], color=cols, edgecolor="white", width=0.7)
for i, r in enumerate(iat):
    ax.text(i, r[2] + 0.6, f"{r[2]:.0f}%", ha="center", fontsize=10)
ax.set_xticks(range(7)); ax.set_xticklabels([r[0].replace(" ", "\n", 1) for r in iat], fontsize=9)
ax.set_ylabel("% of respondents (n = 321)"); ax.set_ylim(0, 35)
ax.set_title("Implicit association 'rich country = good research': 86% pro-rich, 4% pro-poor", fontsize=11)
finish(fig, d / "figures/GEO-04_redraw.png", "Harris, Macinko, Jimenez & Mullachery 2017, Globalization and Health 13:80, Table 3")

# ---------------- GEO-06 Smith et al. APCs, Table 5 -----------------
d = R / "06-geography/GEO-06"
t5 = [("Single", "Lower-middle", 9.14, 5.22), ("Single", "Upper-middle", 31.36, 9.57), ("Single", "High", 59.24, 85.22),
      ("First", "Low", 2.38, 0.51), ("First", "Lower-middle", 13.88, 4.91), ("First", "Upper-middle", 27.75, 17.06), ("First", "High", 56.92, 77.53)]
wcsv(d / "data/GEO-06.csv", ["author", "world_bank_lending_group", "pct_nonOA_parent_bootstrap", "pct_OA_mirror", "source"],
     [r + ("Smith et al. preprint (MetaArXiv s7cx4, Revision 2) Table 5 (PDF p.31)",) for r in t5])
first = [r for r in t5 if r[0] == "First"]
fig, ax = plt.subplots(figsize=(7.5, 3.8))
x = np.arange(4)
ax.bar(x - w / 2, [r[2] for r in first], w, color=LIGHT, edgecolor="white", label="Subscription (non-OA) articles, Parent journals")
ax.bar(x + w / 2, [r[3] for r in first], w, color=DARK, edgecolor="white", label="Gold OA (APC) articles, Mirror journals")
for i, r in enumerate(first):
    ax.text(i - w / 2, r[2] + 1, f"{r[2]:.1f}", ha="center", fontsize=9); ax.text(i + w / 2, r[3] + 1, f"{r[3]:.1f}", ha="center", fontsize=9)
ax.set_xticks(x); ax.set_xticklabels(["Low income", "Lower-middle", "Upper-middle", "High income"])
ax.set_ylabel("% of first authors"); ax.set_ylim(0, 90); ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.set_title("Where first authors are based, by World Bank income group", fontsize=12)
finish(fig, d / "figures/GEO-06_redraw.png", "Smith, Merz, Borden, Gulick, Kshirsagar & Bruna 2021, QSS 2(4):1123 (preprint Table 5)")

# ---------------- GEO-09 Mbaye et al. 2019 -----------------
d = R / "06-geography/GEO-09"
au = [("At least one Africa-based author", 1109, 93.2), ("African first author", 552, 49.8), ("African last author", 458, 41.3)]
wcsv(d / "data/GEO-09.csv", ["authorship_position", "n_articles", "pct_of_1182", "source"], [r + ("Mbaye et al. 2019 BMJ Glob Health 4:e001855, abstract/Results (PDF p.1, p.3)",) for r in au])
fig, ax = plt.subplots(figsize=(7.5, 2.8))
hbar(ax, [r[0] for r in au], [r[2] for r in au], [LIGHT, DARK, DARK], fmt="{:.1f}%", xlabel="% of 1,182 papers (6 infectious diseases, Africa, 1980-2016)")
ax.set_xlim(0, 110)
ax.set_title("Research conducted in Africa: who leads the paper?", fontsize=12)
finish(fig, d / "figures/GEO-09_redraw.png", "Mbaye et al. 2019, BMJ Global Health 4:e001855")
print("done")
