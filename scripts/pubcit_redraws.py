"""Greyscale redraws for PUB/CIT sources whose figures are tables, text or web charts.
Run: python3 -I scripts/pubcit_redraws.py  (from anywhere; paths are absolute)"""
import csv, datetime, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import openpyxl

ROOT = "/home/user/gender-bias/gender-bias-data"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
DARK, MID, LIGHT = "#222222", "#777777", "#bbbbbb"

def save(fig, path):
    fig.tight_layout(); fig.savefig(path, dpi=300); plt.close(fig); print("wrote", path)

# CIT-02: Table 3 median citations by author pair (Chatterjee & Werner 2021)
d = f"{ROOT}/05-citations/CIT-02"
rows = [("Woman primary,\nwoman senior", 33), ("Woman primary,\nman senior", 38.5),
        ("Man primary,\nwoman senior", 42), ("Man primary,\nman senior", 59)]
os.makedirs(f"{d}/data", exist_ok=True)
with open(f"{d}/data/table3_median_citations_by_author_pair.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["author_pair", "median_citations"])
    for k, v in rows: w.writerow([k.replace("\n", " "), v])
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar([r[0] for r in rows], [r[1] for r in rows], color=[LIGHT, LIGHT, MID, DARK], edgecolor=DARK)
for i, (_, v) in enumerate(rows): ax.text(i, v + 1, f"{v:g}", ha="center")
ax.set_ylabel("Median citations (original research)")
ax.set_title("Citations by primary/senior author gender\n(5 high-impact medical journals, 2015-2018)", fontsize=11)
save(fig, f"{d}/figures/CIT-02_redraw.png")

# CIT-08: % women speakers by colloquium chair gender (Nittrouer et al. 2018, Study 3 text)
d = f"{ROOT}/05-citations/CIT-08"
os.makedirs(f"{d}/data", exist_ok=True)
vals = [("Female chair (n=11)", 49), ("Male chair (n=23)", 30)]
with open(f"{d}/data/speakers_by_chair_gender.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["chair_gender", "pct_women_speakers"]); w.writerows(vals)
fig, ax = plt.subplots(figsize=(5, 4))
ax.bar([v[0] for v in vals], [v[1] for v in vals], color=[MID, DARK])
for i, (_, v) in enumerate(vals): ax.text(i, v + 1, f"{v}%", ha="center")
ax.set_ylim(0, 60); ax.set_ylabel("Colloquium speakers who are women (%)")
ax.set_title("Women speakers by colloquium chair gender", fontsize=11)
save(fig, f"{d}/figures/CIT-08_redraw.png")

# PUB-11: female first-author share, Mar-Apr 2019 vs Mar-Apr 2020 (Nature Index Flourish data).
# Column order follows the Nature graphic (PUB-08 fig): JanFeb19, MarApr19, JanFeb20, MarApr20.
d = f"{ROOT}/04-publishing/PUB-11"
with open(f"{d}/data/flourish_2386034.csv") as f:
    r = list(csv.reader(f))[1:]
pf = lambda s: float(s.strip("%"))
names = [x[0] for x in r]; y19 = [pf(x[2]) for x in r]; y20 = [pf(x[4]) for x in r]
fig, ax = plt.subplots(figsize=(7, 4.5))
idx = range(len(names))
ax.barh([i + 0.2 for i in idx], y19, 0.4, color=LIGHT, edgecolor=DARK, label="Mar-Apr 2019")
ax.barh([i - 0.2 for i in idx], y20, 0.4, color=DARK, label="Mar-Apr 2020")
ax.set_yticks(list(idx)); ax.set_yticklabels(names)
ax.set_xlabel("Women's share of first authors (%)"); ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)
ax.set_title("Preprint first authorship, 2019 vs 2020", fontsize=11)
save(fig, f"{d}/figures/PUB-11_redraw.png")

# CIT-12: share of biology faculty (2024 census) whose Wikipedia page existed by each year
d = f"{ROOT}/05-citations/CIT-12"
ws = openpyxl.load_workbook(f"{d}/data/rspb20252566_si_001_TableS1.xlsx", read_only=True).active
data = list(ws.iter_rows(values_only=True))[7:]
tot = {"F": 0, "M": 0}; years = {"F": [], "M": []}; has = {"F": 0, "M": 0}
for row in data:
    g = row[1]
    if g not in tot: continue
    tot[g] += 1
    if row[7] == "Yes":
        has[g] += 1
        c = row[12]
        if isinstance(c, (datetime.date, datetime.datetime)): years[g].append(c.year)
        elif c: years[g].append(int(str(c)[:4]))
print("CIT-12 totals", tot, "with page", has, {g: round(100 * has[g] / tot[g], 2) for g in tot})
yrs = list(range(2004, 2025))
with open(f"{d}/data/cumulative_share_with_page_by_year.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["year", "pct_women_with_page", "pct_men_with_page"])
    cum = {g: [100 * sum(1 for y in years[g] if y <= Y) / tot[g] for Y in yrs] for g in tot}
    for i, Y in enumerate(yrs): w.writerow([Y, round(cum["F"][i], 2), round(cum["M"][i], 2)])
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(yrs, cum["F"], color=DARK, lw=2, label=f"Women (n={tot['F']})")
ax.plot(yrs, cum["M"], color=MID, lw=2, ls="--", label=f"Men (n={tot['M']})")
ax.set_ylabel("% with a Wikipedia biography\n(by page creation year)"); ax.legend(frameon=False)
ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
ax.set_title("US R1 biology faculty (2024 census) on Wikipedia", fontsize=11)
save(fig, f"{d}/figures/CIT-12_redraw.png")
