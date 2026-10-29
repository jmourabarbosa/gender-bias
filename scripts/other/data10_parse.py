"""DATA-10: parse the Nature Index 2026 Research Leaders country table from the saved page.html (CSV export answered 403)."""
import re, html, csv
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-10"
t = open(f"{D}/page.html", encoding="utf-8", errors="ignore").read()
rows = []
for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", t):
    cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", c))).strip() for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)]
    if cells and cells[0].isdigit(): rows.append(cells)
hdr = ["position", "country", "share_2024", "share_2025", "count_2025", "change_in_share_2024_2025"]
with open(f"{D}/data/nature_index_2026_country_all_global.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(hdr); w.writerows(r[:6] for r in rows)
print(len(rows)); [print(r) for r in rows[:12]]
top = rows[:15][::-1]
fig, ax = plt.subplots(figsize=(7, 5.2))
ax.barh([r[1] for r in top], [float(r[3].replace(",", "")) for r in top], color=["black" if r[1] == "France" else "grey" for r in top])
for i, r in enumerate(top): ax.text(float(r[3].replace(",", "")) + 300, i, f'{float(r[3].replace(",", "")):,.0f}', va="center", fontsize=8)
ax.set_xlabel("Nature Index Share 2025 (fractional article count)", fontsize=10)
[ax.spines[s].set_visible(False) for s in ("top", "right")]
fig.text(0.01, 0.008, "Source: Nature Index 2026 Research Leaders, countries/territories, all subjects, global (page saved 2026-10-29)", fontsize=7, color="dimgrey")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(f"{D}/figures/DATA-10_redraw.png", dpi=200)
