"""ANR funding by coordinator gender.

Regenerates every table, figure and data/processed file from data/raw/ in one run:

    .venv/bin/python analysis.py

Inputs (see data/raw/SOURCES.md):
  - ANR_01 (DGDS, ex-DOS) projects (xlsx) and partners (csv), 2010 onwards
  - ANR_02 (DGPIE, France 2030) projects and partners (csv), context only
  - Insee Fichier des prénoms, nat2021.csv
  - committee_labels_anr_fr.json: CE committee labels read from anr.fr project pages
"""
from __future__ import annotations

import json
import os
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import warnings

warnings.filterwarnings("ignore", message=".*rank-deficient.*")
warnings.filterwarnings("ignore", category=RuntimeWarning)

os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
FIG = ROOT / "figures"
TAB = ROOT / "tables"
for d in (PROC, FIG, TAB):
    d.mkdir(parents=True, exist_ok=True)

PROJ_XLSX = RAW / "anr-dgds-depuis-2010-projets-finances-20261002-projets.xlsx"
PART_CSV = RAW / "anr-dgds-depuis-2010-projets-finances-20261002-partenaires.csv"
PIA_PROJ = RAW / "anr-dgpie-depuis-2010-projets-finances-20261002-projets.csv"
PIA_PART = RAW / "anr-dgpie-depuis-2010-projets-finances-20261002-partenaires.csv"
INSEE = RAW / "nat2021.csv"
CE_LABELS = RAW / "committee_labels_anr_fr.json"

RNG = np.random.default_rng(20261101)
N_BOOT = 2000
MAIN_YEARS = (2010, 2025)  # 2026 edition is still being contracted: excluded
MIN_PER_GENDER = 30

# Colours: categorical slots 1-2 of the reference palette (women = orange, men = blue)
C_F, C_M = "#eb6834", "#2a78d6"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({
    "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb", "savefig.facecolor": "#fcfcfb",
    "axes.edgecolor": INK2, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "text.color": INK, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
    "font.size": 9, "axes.titlesize": 10, "axes.titleweight": "bold", "lines.linewidth": 2,
    "legend.frameon": False,
})

K = "Projet.Code_Decision"
AMT = "Projet.Montant.AF.Aide_allouee.ANR"

# ---------------------------------------------------------------------------
# Committee -> domain (my grouping of the CE committee labels, see report)
# ---------------------------------------------------------------------------
DOMAIN_CE = {
    "Environnement & Terre": ["CE01", "CE02", "CE03", "CE04", "CE21", "CE22", "CE32", "CE34", "CE43", "CE49"],
    "Biologie-Santé": ["CE11", "CE12", "CE13", "CE14", "CE15", "CE16", "CE17", "CE18", "CE19", "CE20",
                       "CE35", "CE36", "CE37", "CE44", "CE52"],
    "Matière & Ingénierie": ["CE05", "CE06", "CE07", "CE08", "CE09", "CE10", "CE24", "CE29", "CE30", "CE31",
                             "CE42", "CE47", "CE50", "CE51", "CE57"],
    "Numérique & Maths": ["CE23", "CE25", "CE33", "CE39", "CE40", "CE46", "CE48"],
    "Interfaces maths-numérique": ["CE38", "CE45", "CE56"],
    "SHS": ["CE26", "CE27", "CE28", "CE41", "CE53", "CE54", "CE55"],
}
CE_TO_DOMAIN = {ce: dom for dom, ces in DOMAIN_CE.items() for ce in ces}
SUBSETS = [  # (file tag, committees, figure title) for the per-field median-award figure
    ("_neuro", ["CE16", "CE37", "CE28", "SV4"],
     "Neuroscience (CE16, CE37, CE28; SV4 2012-13): median award, women vs. men"),
    ("_physics", ["CE30", "CE31", "CE47", "CE57"],
     "Physics (CE30, CE31, CE47, CE57): median award, women vs. men"),
]
NEURO = {"CE16", "CE37", "CE28", "CE14", "SV4"}  # SV4 = 2012-13 Blanc/JCJC "SVSE 4 Neurosciences"


def old_domain(c: str) -> str:
    """Domain for the 2012-2013 Blanc/JCJC committee codes (S01..S10, SV1..SV8, SH1..SH3, S56)."""
    if c.startswith("SV"):
        return "Biologie-Santé"
    if c.startswith("SH") or c == "S56":
        return "SHS"
    if c in ("S01", "S02"):
        return "Numérique & Maths"
    if c == "S06":
        return "Environnement & Terre"
    if c.startswith("S"):
        return "Matière & Ingénierie"
    return "Non précisé"


def strip_accents(s: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))


def norm_name(s) -> str:
    if not isinstance(s, str):
        return ""
    s = strip_accents(s).upper().strip()
    s = s.replace("’", "'").replace(".", " ")
    s = " ".join(s.split())
    return s.replace(" - ", "-").replace(" ", "-")


# ---------------------------------------------------------------------------
# 1. Load
# ---------------------------------------------------------------------------
def load():
    proj = pd.read_excel(PROJ_XLSX)
    part = pd.read_csv(PART_CSV, sep=";", low_memory=False)
    insee = pd.read_csv(INSEE, sep=";", dtype={"annais": str}, keep_default_na=False)
    return proj, part, insee


# ---------------------------------------------------------------------------
# 2. Gender reference from Insee
# ---------------------------------------------------------------------------
def build_reference(insee: pd.DataFrame) -> pd.DataFrame:
    i = insee[~insee["preusuel"].str.startswith("_")].copy()
    i["key"] = i["preusuel"].map(norm_name)
    t = i.pivot_table(index="key", columns="sexe", values="nombre", aggfunc="sum", fill_value=0)
    t.columns = ["m", "f"]  # sexe 1 = male, 2 = female
    t["n"] = t.m + t.f
    t["pf"] = t.f / t.n
    return t


def classify(pf: float, thr: float) -> str:
    if pf >= thr:
        return "F"
    if pf <= 1 - thr:
        return "M"
    return "U"


def infer_gender(first: pd.Series, ref: pd.DataFrame, thr: float) -> pd.DataFrame:
    pf = ref["pf"].to_dict()
    out = []
    for raw in first:
        key = norm_name(raw)
        g, rule = "U", "absent"
        if key:
            cands = [(key, "full")]
            parts = [p for p in key.split("-") if p]
            if len(parts) > 1:
                cands.append((parts[0], "first-element"))
            for cand, r in cands:
                if cand in pf:
                    g, rule = classify(pf[cand], thr), r
                    if g == "U":
                        rule = r + "-ambiguous"
                    break
        else:
            rule = "missing"
        out.append((g, rule))
    return pd.DataFrame(out, columns=["g", "rule"], index=first.index)


def secondary_gender(first: pd.Series) -> pd.Series:
    import gender_guesser.detector as gd
    d = gd.Detector(case_sensitive=False)
    res = []
    for raw in first:
        if not isinstance(raw, str) or not raw.strip():
            res.append("U")
            continue
        tok = strip_accents(raw).replace("-", " ").split()[0]
        r = d.get_gender(tok)
        res.append({"female": "F", "male": "M"}.get(r, "U"))
    return pd.Series(res, index=first.index)


# ---------------------------------------------------------------------------
# 3. Project table
# ---------------------------------------------------------------------------
FIRMS = {"PME (petite et moyenne entreprise)", "ETI (entreprise de taille intermédiaire)", "GE (grande entreprise)"}


def build_projects(proj, part, ref, ce_labels):
    prog = proj["Programme.Acronyme"].fillna("")
    is_aapg = prog.str.startswith("AAPG") | (prog == "Appel à projets générique")
    is_blanc = prog.isin(["BLANC", "Blanc 2013"])
    is_jcjc = prog.isin(["JCJC", "JC"])
    p = proj[is_aapg | is_blanc | is_jcjc].copy()
    p["call"] = np.where(is_aapg[p.index], "AAPG", np.where(is_blanc[p.index], "Blanc", "JCJC"))
    p["year"] = p["AAP.Edition"].astype(int)
    p["amount"] = p[AMT]
    seg = p[K].str.split("-").str[2]
    p["code_seg"] = seg

    # partners
    q = part.copy()
    q["foreign"] = q["Projet.Partenaire.Adresse.Pays"].notna() & (q["Projet.Partenaire.Adresse.Pays"] != "France")
    q["firm"] = q["Projet.Partenaire.Categorie_organisme"].isin(FIRMS)
    g = q.groupby(K).agg(
        n_partners=("foreign", "size"),
        n_foreign=("foreign", "sum"),
        has_firm=("firm", "any"),
        n_coord=("Projet.Partenaire.Est_coordinateur", "sum"),
        partner_sum=("Projet.Partenaire.Aide_allouee.ANR", "sum"),
    )
    p = p.join(g, on=K)
    coords = (q[q["Projet.Partenaire.Est_coordinateur"]]
              .sort_values("Projet.Partenaire.Code_Decision")
              .drop_duplicates(K, keep="first")
              .set_index(K)["Projet.Partenaire.Responsable_scientifique.Prenom"])
    p["coord_first_name"] = p[K].map(coords)
    p["n_coord"] = p["n_coord"].fillna(0).astype(int)

    # committee
    def committee(row):
        s = row.code_seg
        if row.call == "AAPG":
            return s
        if len(s) == 4 and s[0] in "BJ" and s[1] == "S":  # BS09 / JS09 / BSV4 / JSH1 ...
            return s[1:]
        return "NA"
    p["committee"] = p.apply(committee, axis=1)
    p = p[~p.committee.isin(["ACHN", "CERA"])].copy()  # one-off instruments inside the AAPG code space

    def domain(c):
        if c.startswith("CE9"):
            return "International (CE9x)"
        if c.startswith("CE"):
            return CE_TO_DOMAIN.get(c, "Non précisé")
        if c == "NA":
            return "Non précisé"
        return old_domain(c)
    p["domain"] = p.committee.map(domain)
    def clabel(c):
        lab = (ce_labels.get(c) or {}).get("label")
        if lab:
            return lab.replace("e`", "è").replace("e´", "é")
        if c == "SV4":
            return "SV4 - SVSE 4 Neurosciences (Blanc/JCJC 2012-13)"
        if c.startswith("CE9"):
            return f"{c} - international bilateral call (label not published)"
        if c.startswith("S"):
            return f"{c} - Blanc/JCJC 2012-13 committee"
        return c
    p["committee_label"] = p.committee.map(clabel)

    # instrument (true for 2010-13; proxy for AAPG 2014+)
    def proxy(row):
        if row.n_partners == 1:
            return "Mono-team (JCJC/PRME)"
        if row.committee.startswith("CE9") or row.n_foreign > 0:
            return "PRCI-like"
        if row.has_firm:
            return "PRCE-like"
        return "PRC-like"
    p["instrument_proxy"] = p.apply(proxy, axis=1)
    p["instrument"] = np.where(p.call == "AAPG", p.instrument_proxy, p.call)

    # gender
    for thr, tag in ((0.95, ""), (0.99, "_99")):
        gi = infer_gender(p["coord_first_name"], ref, thr)
        p["gender" + tag] = gi.g
        p["rule" + tag] = gi.rule
    p.loc[p.n_coord == 0, ["gender", "gender_99"]] = "U"
    p.loc[p.n_coord == 0, ["rule", "rule_99"]] = "no-coordinator"
    p["gender_secondary"] = secondary_gender(p["coord_first_name"])
    p["gender_combined"] = np.where(p.gender == "U", p.gender_secondary, p.gender)
    p["female"] = (p.gender == "F").astype(int)
    return p


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def save_fig(fig, name, data: pd.DataFrame):
    fig.savefig(FIG / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    data.to_csv(FIG / f"{name}.csv", index=False)


def boot_ratio(f: np.ndarray, m: np.ndarray, stat=np.median, n=N_BOOT):
    bf = RNG.choice(f, size=(n, len(f)), replace=True)
    bm = RNG.choice(m, size=(n, len(m)), replace=True)
    r = stat(bf, axis=1) / stat(bm, axis=1)
    return stat(f) / stat(m), np.percentile(r, 2.5), np.percentile(r, 97.5)


def fit(df, formula):
    """OLS of `formula` with HC3 standard errors; returns the `female` effect as a % difference.

    Fixed-effect dummies are often collinear (e.g. 2012-13 committee codes only exist in those years),
    and statsmodels' HC3 is unreliable on a rank-deficient design. So collinear columns are removed
    first (pivoted QR, `female` always kept), and observations with leverage ~1 (singleton cells, which
    carry no information on `female` and make HC3 undefined) are dropped."""
    import patsy
    import scipy.linalg as sla
    import statsmodels.api as sm
    y, X = patsy.dmatrices(formula, data=df.reset_index(drop=True), return_type="dataframe")
    y = y.iloc[:, 0].values
    n_drop = 0
    for _ in range(3):
        cols = list(X.columns)
        fi = cols.index("female")
        order = [fi] + [i for i in range(len(cols)) if i != fi]
        Xo = X.values[:, order]
        # pivoted QR on the non-female columns after projecting female first keeps female in the basis
        _, r, piv = sla.qr(Xo, mode="economic", pivoting=True)
        d = np.abs(np.diag(r))
        rank = int((d > 1e-9 * d.max()).sum())
        keep = sorted(piv[:rank])
        if 0 not in keep:  # female collinear with fixed effects: cannot be estimated
            return {"pct": np.nan, "lo": np.nan, "hi": np.nan, "p": np.nan, "n": len(y), "n_dropped_leverage1": n_drop}
        Xk = Xo[:, keep]
        q, _ = np.linalg.qr(Xk)
        h = (q ** 2).sum(axis=1)
        bad = h > 1 - 1e-8
        if not bad.any():
            break
        n_drop += int(bad.sum())
        X, y = X.loc[~bad].reset_index(drop=True), y[~bad]
        X = X.loc[:, X.abs().sum(axis=0) > 0]
    m = sm.OLS(y, Xk).fit(cov_type="HC3")
    j = keep.index(0)
    b_, se = m.params[j], m.bse[j]
    return {"pct": np.expm1(b_) * 100, "lo": np.expm1(b_ - 1.96 * se) * 100, "hi": np.expm1(b_ + 1.96 * se) * 100,
            "p": m.pvalues[j], "n": int(m.nobs), "n_dropped_leverage1": n_drop}


def pct(x):
    return f"{x:+.1f}%"


def md(df: pd.DataFrame, floatfmt=None) -> str:
    d = df.copy()
    for c in d.columns:
        if d[c].dtype.kind == "f":
            d[c] = d[c].map(lambda v: "" if pd.isna(v) else (floatfmt or "{:,.3g}").format(v))
    cols = list(d.columns)
    lines = ["| " + " | ".join(map(str, cols)) + " |", "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in d.iterrows():
        lines.append("| " + " | ".join(str(v) for v in r.values) + " |")
    return "\n".join(lines)


INSTR_ORDER = ["JCJC", "Blanc", "Mono-team (JCJC/PRME)", "PRC-like", "PRCE-like", "PRCI-like"]


# ---------------------------------------------------------------------------
# Analyses
# ---------------------------------------------------------------------------
def descriptives(a):
    rows = []
    for (ins, y), s in a.groupby(["instrument", "year"]):
        f, m = s[s.gender == "F"].amount, s[s.gender == "M"].amount
        rows.append({"instrument": ins, "year": y, "n": len(s), "n_F": len(f), "n_M": len(m),
                     "n_unknown": int((s.gender == "U").sum()),
                     "share_F_known": len(f) / max(len(f) + len(m), 1),
                     "mean_F": f.mean(), "mean_M": m.mean(), "median_F": f.median(), "median_M": m.median(),
                     "ratio_median_FM": f.median() / m.median() if len(f) and len(m) else np.nan})
    t = pd.DataFrame(rows)
    t["instrument"] = pd.Categorical(t.instrument, INSTR_ORDER)
    t = t.sort_values(["instrument", "year"])
    t.to_csv(TAB / "1_descriptives_instrument_year.csv", index=False)

    # Figure: median award per year, one panel per instrument
    ins_list = [i for i in INSTR_ORDER if i in set(a.instrument)]
    fig, axes = plt.subplots(2, 3, figsize=(10, 5.6))
    for ax, ins in zip(axes.flat, ins_list):
        s = t[(t.instrument == ins) & (t.n_F >= 10) & (t.n_M >= 10)]
        ax.plot(s.year, s.median_M / 1e3, color=C_M, marker="o", ms=4, label="Men")
        ax.plot(s.year, s.median_F / 1e3, color=C_F, marker="o", ms=4, label="Women")
        ax.set_title(ins, loc="left")
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ymax = np.nanmax(t[(t.n_F >= 10) & (t.n_M >= 10)][["median_F", "median_M"]].values) / 1e3 * 1.08
    for ax in axes.flat:
        ax.set_ylim(0, ymax)
    for ax in axes[:, 0]:
        ax.set_ylabel("Median award (k€, nominal)")
    for ax in axes.flat[len(ins_list):]:
        ax.set_visible(False)
    axes.flat[0].legend(loc="lower left")
    fig.suptitle("ANR generic call: median award by coordinator gender, per instrument", x=0.01, ha="left",
                 fontweight="bold")
    fig.text(0.01, -0.02, "Blanc/JCJC 2010-13: ANR programme. 2014-25 AAPG instruments are proxies from the "
             "partner list (see report). Cells with <10 women or <10 men hidden.", fontsize=7, color=INK2)
    fig.tight_layout()
    save_fig(fig, "fig1_median_award_by_instrument_year", t)
    return t


def pooled_and_within(a):
    rows = []
    f, m = a[a.gender == "F"].amount.values, a[a.gender == "M"].amount.values
    r, lo, hi = boot_ratio(f, m)
    rm, lom, him = boot_ratio(f, m, stat=np.mean)
    rows.append({"group": "All instruments pooled (raw)", "n_F": len(f), "n_M": len(m),
                 "share_F": len(f) / (len(f) + len(m)),
                 "median_F": np.median(f), "median_M": np.median(m), "ratio_median": r, "lo": lo, "hi": hi,
                 "mean_F": f.mean(), "mean_M": m.mean(), "ratio_mean": rm, "lo_mean": lom, "hi_mean": him})
    for ins in INSTR_ORDER:
        s = a[a.instrument == ins]
        f, m = s[s.gender == "F"].amount.values, s[s.gender == "M"].amount.values
        if len(f) < 10 or len(m) < 10:
            continue
        r, lo, hi = boot_ratio(f, m)
        rm, lom, him = boot_ratio(f, m, stat=np.mean)
        rows.append({"group": ins, "n_F": len(f), "n_M": len(m), "share_F": len(f) / (len(f) + len(m)),
                     "median_F": np.median(f), "median_M": np.median(m), "ratio_median": r, "lo": lo, "hi": hi,
                     "mean_F": f.mean(), "mean_M": m.mean(), "ratio_mean": rm, "lo_mean": lom, "hi_mean": him})
    t = pd.DataFrame(rows)
    t.to_csv(TAB / "2_3_pooled_vs_within_instrument.csv", index=False)

    # Within instrument x year median ratio (pooled over years: median of yearly ratios is reported in table 1)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    y = np.arange(len(t))[::-1]
    for yi, (_, r) in zip(y, t.iterrows()):
        pooled = r.group.startswith("All")
        ax.plot([r.lo, r.hi], [yi, yi], color=INK2 if pooled else C_F, lw=2)
        ax.plot(r.ratio_median, yi, "o", color=INK2 if pooled else C_F, ms=7, mec="#fcfcfb", mew=1.5)
        ax.annotate(f"{r.ratio_median:.3f}  [{r.lo:.3f}, {r.hi:.3f}]   n={r.n_F:,}F / {r.n_M:,}M",
                    (max(t.hi.max(), 1.02) + 0.005, yi), va="center", fontsize=7.5, color=INK2,
                    annotation_clip=False)
    ax.axvline(1, color=INK, lw=1)
    ax.set_yticks(y, t.group)
    ax.set_xlabel("Women / men ratio of median award (bootstrap 95% CI)")
    ax.set_title("Pooled gap vs. like-for-like gap (2010-2025)", loc="left")
    ax.grid(axis="y", visible=False)
    save_fig(fig, "fig3_within_instrument_median_ratio", t)
    return t


def regressions(a, gender_col="gender", label="main"):
    d = a[a[gender_col].isin(["F", "M"])].copy()
    d["female"] = (d[gender_col] == "F").astype(int)
    d["log_amt"] = np.log(d.amount)
    d["np_cap"] = d.n_partners.clip(upper=8).astype(int)
    d["iy"] = d.instrument + "_" + d.year.astype(str)
    specs = {
        "A: instrument + year + committee": "log_amt ~ female + C(instrument) + C(year) + C(committee)",
        "B: A + number of partners": "log_amt ~ female + C(instrument) + C(year) + C(committee) + C(np_cap)",
        "C: instrument×year + committee + partners": "log_amt ~ female + C(iy) + C(committee) + C(np_cap)",
    }
    rows = []
    for k, f in specs.items():
        rows.append({"variant": label, "spec": k, **fit(d, f)})
    # by instrument
    for ins in INSTR_ORDER:
        s = d[d.instrument == ins]
        if (s.female == 1).sum() < MIN_PER_GENDER or (s.female == 0).sum() < MIN_PER_GENDER:
            continue
        rows.append({"variant": label, "spec": f"{ins}: year + committee", **fit(s, "log_amt ~ female + C(year) + C(committee)")})
        rows.append({"variant": label, "spec": f"{ins}: year + committee + partners",
                     **fit(s, "log_amt ~ female + C(year) + C(committee) + C(np_cap)")})
    return pd.DataFrame(rows)


def by_domain_committee(a):
    d = a[a.gender.isin(["F", "M"])].copy()
    d["female"] = (d.gender == "F").astype(int)
    d["log_amt"] = np.log(d.amount)
    d["np_cap"] = d.n_partners.clip(upper=8).astype(int)
    rows = []
    for dom, s in d.groupby("domain"):
        nf, nm = (s.female == 1).sum(), (s.female == 0).sum()
        if nf < MIN_PER_GENDER or nm < MIN_PER_GENDER:
            continue
        r = fit(s, "log_amt ~ female + C(instrument) + C(year) + C(committee)")
        r2 = fit(s, "log_amt ~ female + C(instrument) + C(year) + C(committee) + C(np_cap)")
        rows.append({"level": "domain", "unit": dom, "label": dom, "n_F": nf, "n_M": nm, "share_F": nf / (nf + nm),
                     **r, "pct_partners": r2["pct"], "lo_partners": r2["lo"], "hi_partners": r2["hi"]})
    for c, s in d.groupby("committee"):
        nf, nm = (s.female == 1).sum(), (s.female == 0).sum()
        if nf < MIN_PER_GENDER or nm < MIN_PER_GENDER or c == "NA":
            continue
        r = fit(s, "log_amt ~ female + C(instrument) + C(year)")
        r2 = fit(s, "log_amt ~ female + C(instrument) + C(year) + C(np_cap)")
        rows.append({"level": "committee", "unit": c, "label": s.committee_label.iloc[0],
                     "domain": s.domain.iloc[0], "neuro": c in NEURO, "n_F": nf, "n_M": nm,
                     "share_F": nf / (nf + nm), **r,
                     "pct_partners": r2["pct"], "lo_partners": r2["lo"], "hi_partners": r2["hi"]})
    t = pd.DataFrame(rows)
    t.to_csv(TAB / "5_by_domain_committee.csv", index=False)

    # within-instrument median ratios by domain (cells with >=30 per gender)
    cells = []
    for (dom, ins), s in d.groupby(["domain", "instrument"]):
        f, m = s[s.female == 1].amount.values, s[s.female == 0].amount.values
        if len(f) < MIN_PER_GENDER or len(m) < MIN_PER_GENDER:
            continue
        r, lo, hi = boot_ratio(f, m)
        cells.append({"domain": dom, "instrument": ins, "n_F": len(f), "n_M": len(m), "ratio_median": r,
                      "lo": lo, "hi": hi})
    cells = pd.DataFrame(cells)
    cells.to_csv(TAB / "5_domain_instrument_median_ratio.csv", index=False)

    # Forest plot: domains then committees (sorted), highlight Biologie-Santé & neuro
    dom = t[t.level == "domain"].sort_values("pct")
    com = t[t.level == "committee"].sort_values("pct")
    fig, axes = plt.subplots(1, 2, figsize=(11, 9.5), gridspec_kw={"width_ratios": [1, 1.25]})
    for ax, s, title in ((axes[0], dom, "By domain"), (axes[1], com, "By committee (≥30 women and ≥30 men)")):
        y = np.arange(len(s))
        for yi, (_, r) in zip(y, s.iterrows()):
            hl = (r.get("neuro") is True) or (r.level == "domain" and r.unit == "Biologie-Santé")
            col = C_F if hl else INK2
            ax.plot([r.lo, r.hi], [yi, yi], color=col, lw=1.6 if hl else 1.1)
            ax.plot(r.pct, yi, "o", color=col, ms=5.5 if hl else 4, mec="#fcfcfb", mew=1)
        labels = [f"{r.unit}" if r.level == "domain" else f"{r.unit} {r.label.split(' - ', 1)[-1][:38]}"
                  for _, r in s.iterrows()]
        ax.set_yticks(y, labels, fontsize=7 if len(s) > 20 else 8.5)
        for tl, (_, r) in zip(ax.get_yticklabels(), s.iterrows()):
            if (r.get("neuro") is True) or (r.level == "domain" and r.unit == "Biologie-Santé"):
                tl.set_color(C_F)
                tl.set_fontweight("bold")
        ax.axvline(0, color=INK, lw=1)
        ax.set_xlabel("Award difference, women vs men (%, 95% CI)")
        ax.set_title(title, loc="left")
        ax.grid(axis="y", visible=False)
    fig.suptitle("Adjusted award gap by field (log award ~ female + instrument + year [+ committee])",
                 x=0.01, ha="left", fontweight="bold")
    fig.text(0.01, 0.005, "Highlighted: Biologie-Santé domain and neuroscience-related committees "
             "(CE16, CE37, CE28, CE14; SV4 = 2012-13 Neurosciences).", fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    save_fig(fig, "fig5_gap_by_domain_committee", t)
    return t, cells


def fit_median(df, formula):
    """Median (quantile 0.5) regression of `formula`; returns the `female` effect as a % difference.

    On log award, exp(coef) is the women/men ratio of conditional medians (the median commutes with
    log). Collinear fixed-effect columns are removed first (pivoted QR, `female` kept). CIs use
    statsmodels' robust sandwich (Hall-Sheather bandwidth)."""
    import patsy
    import scipy.linalg as sla
    import statsmodels.api as sm
    y, X = patsy.dmatrices(formula, data=df.reset_index(drop=True), return_type="dataframe")
    cols = list(X.columns)
    fi = cols.index("female")
    order = [fi] + [i for i in range(len(cols)) if i != fi]
    Xo = X.values[:, order]
    _, r, piv = sla.qr(Xo, mode="economic", pivoting=True)
    d = np.abs(np.diag(r))
    keep = sorted(piv[: int((d > 1e-9 * d.max()).sum())])
    m = sm.QuantReg(y.iloc[:, 0].values, Xo[:, keep]).fit(q=0.5, max_iter=5000)
    j = keep.index(0)
    b_, se = m.params[j], m.bse[j]
    return {"pct": np.expm1(b_) * 100, "lo": np.expm1(b_ - 1.96 * se) * 100, "hi": np.expm1(b_ + 1.96 * se) * 100,
            "p": m.pvalues[j], "n": int(m.nobs)}


FIG2_MODELS = [  # (label in figure, key in model_fit, formula rhs)
    ("Raw", "Raw", "female"),
    ("Same team size", "Team size", "female + C(np_cap)"),
    ("Same team size,\ncommittee and year", "Team size + committee + year",
     "female + C(np_cap) + C(committee) + C(year)"),
    ("Same team size, committee,\nyear and instrument", "+ instrument (full)",
     "female + C(np_cap) + C(committee) + C(year) + C(instrument)"),
]


def raw_vs_team_size(a, fit_table, tag="", title="ANR generic call 2010-2025: median award, women vs. men"):
    """Median regressions with increasing controls, with each model's cross-validated pseudo-R1."""
    d = a[a.gender.isin(["F", "M"])].copy()
    d["female"] = (d.gender == "F").astype(int)
    d["log_amt"] = np.log(d.amount)
    d["np_cap"] = d.n_partners.clip(upper=8).astype(int)
    cv = fit_table.set_index("model")["cv_pseudo_R1"]
    rows = [{"model": lab, **fit_median(d, "log_amt ~ " + rhs), "cv_pseudo_R1": cv[key]}
            for lab, key, rhs in FIG2_MODELS]
    t = pd.DataFrame(rows)
    for c in ("pct", "lo", "hi"):
        t["ratio_" + c] = 1 + t[c] / 100
    flat = t.assign(model=t.model.str.replace("\n", " "))
    flat.to_csv(TAB / f"2b_raw_vs_team_size{tag}.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    y = list(range(len(t)))  # raw at the bottom, each added control one row up (crop from the top to build up)
    for yi, (_, r) in zip(y, t.iterrows()):
        col = INK2 if r.model == "Raw" else C_F
        ax.plot([r.ratio_lo, r.ratio_hi], [yi, yi], color=col, lw=2.5)
        ax.plot(r.ratio_pct, yi, "o", color=col, ms=8, mec="#fcfcfb", mew=1.5)
        ax.annotate(f"{r.ratio_pct:.3f}  [{r.ratio_lo:.3f}, {r.ratio_hi:.3f}]", (r.ratio_pct, yi),
                    xytext=(0, 9), textcoords="offset points", ha="center", fontsize=8.5, color=INK2,
                    bbox=dict(boxstyle="square,pad=0.1", fc="#fcfcfb", ec="none"), zorder=5)
    ax.axvline(1, color=INK, lw=1, zorder=1)
    # direction cues at the bottom (kept by any top crop)
    ya = -0.55
    for x1, x2, txt, ha in ((0.996, 0.976, "Women get less", "right"), (1.004, 1.024, "Men get less", "left")):
        ax.annotate("", xy=(x2, ya), xytext=(x1, ya),
                    arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1, mutation_scale=9))
        ax.text(x2 + (-0.002 if ha == "right" else 0.002), ya, txt, ha=ha, va="center", fontsize=8,
                color=INK2, style="italic")
    ax.set_yticks(y, t.model)
    ax.set_ylim(-0.8, len(t) - 0.4)
    lo = min(0.92, t.ratio_lo.min() - 0.01)
    hi = max(1.05, t.ratio_hi.max() + 0.01)
    ax.set_xlim(lo, hi)
    # CV R2 column to the right of the plot
    xr = hi + (hi - lo) * 0.04
    for yi, (_, r) in zip(y, t.iterrows()):  # label on every row so any crop keeps it
        ax.text(xr, yi, f"CV R² {r.cv_pseudo_R1:.2f}", fontsize=9, color=INK2, va="center")
    ax.set_xlabel("Women / men ratio of median award (median regression, 95% CI)")
    ax.set_title(title, loc="left")
    ax.grid(axis="y", visible=False)
    fig.text(0.01, -0.08, f"n = {t.n.iloc[0]:,} projects. Team size = number of partners (1, 2, ... 8+). "
             "Quantile regression on log award, robust CIs. CV R² = 5-fold cross-validated pseudo-R¹ "
             "(share of absolute error removed vs. predicting the median).", fontsize=6.5, color=INK2, wrap=True)
    save_fig(fig, f"fig2_raw_vs_team_size{tag}", flat)
    return t


def model_fit(a, k=5, tag=""):
    """Fit comparison of the median-regression models: in-sample pseudo-R1 (Koenker-Machado) and
    k-fold cross-validated median absolute error of log award (reported as a typical % error)."""
    import patsy
    import scipy.linalg as sla
    import statsmodels.api as sm
    d = a[a.gender.isin(["F", "M"])].copy().reset_index(drop=True)
    d["female"] = (d.gender == "F").astype(int)
    d["log_amt"] = np.log(d.amount)
    d["np_cap"] = d.n_partners.clip(upper=8).astype(int)
    models = {
        "Raw": "female",
        "Team size": "female + C(np_cap)",
        "Team size + committee": "female + C(np_cap) + C(committee)",
        "Team size + committee + year": "female + C(np_cap) + C(committee) + C(year)",
        "+ instrument (full)": "female + C(np_cap) + C(committee) + C(year) + C(instrument)",
    }
    y = d.log_amt.values

    def qfit(X, yy):
        _, r, piv = sla.qr(X, mode="economic", pivoting=True)
        dd = np.abs(np.diag(r))
        keep = sorted(piv[: int((dd > 1e-9 * dd.max()).sum())])
        m = sm.QuantReg(yy, X[:, keep]).fit(q=0.5, max_iter=5000)
        beta = np.zeros(X.shape[1])
        beta[keep] = m.params
        return beta

    folds = RNG.permutation(len(d)) % k
    base_loss = np.abs(y - np.median(y)).sum()
    rows = []
    for name, rhs in models.items():
        X = np.asarray(patsy.dmatrix(rhs, d))
        beta = qfit(X, y)
        r1 = 1 - np.abs(y - X @ beta).sum() / base_loss
        cv_err = np.empty(len(d))
        cv_base = np.empty(len(d))
        for f in range(k):
            tr, te = folds != f, folds == f
            b = qfit(X[tr], y[tr])
            # committee/year levels absent from the training fold get coefficient 0 (rare)
            cv_err[te] = np.abs(y[te] - X[te] @ b)
            cv_base[te] = np.abs(y[te] - np.median(y[tr]))
        rows.append({"model": name, "n_params": int(np.linalg.matrix_rank(X)), "pseudo_R1": r1,
                     "cv_pseudo_R1": 1 - cv_err.sum() / cv_base.sum(),
                     "cv_median_abs_err_log": np.median(cv_err), "cv_mean_abs_err_log": cv_err.mean(),
                     "cv_typical_pct_error": np.expm1(np.median(cv_err)) * 100})
    t = pd.DataFrame(rows)
    t.to_csv(TAB / f"2c_model_fit{tag}.csv", index=False)
    return t


NON_STEM_DOMAINS = {"SHS"}  # SHS committees (incl. CE28 cognition/language, which ANR files under SHS)


def field_histograms(a, min_per_gender=20):
    """Full median model fitted separately in every committee (>= MIN_PER_GENDER women and men):
    log award ~ female + team size + year + instrument. Histogram of the women/men ratios, overall
    and split STEM vs non-STEM, with an inverse-variance pooled estimate and a heterogeneity test."""
    from scipy import stats
    d = a[a.gender.isin(["F", "M"])].copy()
    d["female"] = (d.gender == "F").astype(int)
    d["log_amt"] = np.log(d.amount)
    d["np_cap"] = d.n_partners.clip(upper=8).astype(int)
    rows = []
    for c, s_ in d.groupby("committee"):
        nf, nm = int(s_.female.sum()), int((1 - s_.female).sum())
        if c == "NA" or nf < min_per_gender or nm < min_per_gender:
            continue
        r = fit_median(s_, "log_amt ~ female + C(np_cap) + C(year) + C(instrument)")
        b = np.log1p(r["pct"] / 100)
        se = (np.log1p(r["hi"] / 100) - np.log1p(r["lo"] / 100)) / (2 * 1.96)
        dom = s_.domain.iloc[0]
        rows.append({"committee": c, "label": s_.committee_label.iloc[0], "domain": dom,
                     "group": "Non-STEM (SHS)" if dom in NON_STEM_DOMAINS else "STEM",
                     "n_F": nf, "n_M": nm, "ratio": np.exp(b), "lo": 1 + r["lo"] / 100, "hi": 1 + r["hi"] / 100,
                     "log_ratio": b, "se_log": se, "p": r["p"]})
    t = pd.DataFrame(rows).sort_values("ratio")
    t.to_csv(TAB / "8_full_model_by_committee.csv", index=False)

    def pooled(x):
        w = 1 / x.se_log ** 2
        b = (w * x.log_ratio).sum() / w.sum()
        se = np.sqrt(1 / w.sum())
        q = (w * (x.log_ratio - b) ** 2).sum()
        k = len(x)
        return {"k": k, "pooled": np.exp(b), "lo": np.exp(b - 1.96 * se), "hi": np.exp(b + 1.96 * se),
                "Q": q, "Q_p": stats.chi2.sf(q, k - 1), "I2": max(0.0, (q - (k - 1)) / q) * 100 if q > 0 else 0.0,
                "n_sig_05": int((x.p < 0.05).sum()), "median_ratio": x.ratio.median()}
    summ = pd.DataFrame([{"group": "All", **pooled(t)}] +
                        [{"group": g, **pooled(x)} for g, x in t.groupby("group")])
    summ.to_csv(TAB / "8_full_model_by_committee_summary.csv", index=False)

    lo_edge = np.floor(min(t.ratio.min(), 0.85) / 0.02) * 0.02
    hi_edge = np.ceil(max(t.ratio.max(), 1.15) / 0.02) * 0.02
    bins = np.arange(lo_edge, hi_edge + 1e-9, 0.02)

    def panel(ax, x, title, sm):
        counts, _, _ = ax.hist(x.ratio, bins=bins, color=INK2, edgecolor="#fcfcfb", linewidth=1.5)
        top = max(counts.max(), 1)
        ax.set_ylim(0, top * 1.45)
        ax.axvline(1, color=INK, lw=1)
        ax.set_title(title, loc="left", pad=20)
        ax.text(0, 1.015, f"{int(sm['k'])} committees · pooled {sm['pooled']:.3f} [{sm['lo']:.3f}, {sm['hi']:.3f}] · "
                f"{int(sm['n_sig_05'])} significant at 5% · heterogeneity p = {sm['Q_p']:.2f}",
                transform=ax.transAxes, ha="left", va="bottom", fontsize=7.5, color=INK2)
        ax.set_ylabel("Committees")
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax.grid(axis="x", visible=False)
        ya = top * 1.25
        for x1, x2, lab, ha in ((0.995, 0.955, "Women get less", "right"), (1.005, 1.045, "Men get less", "left")):
            ax.annotate("", xy=(x2, ya), xytext=(x1, ya),
                        arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1, mutation_scale=9))
            ax.text(x2 + (-0.003 if ha == "right" else 0.003), ya, lab, ha=ha, va="center",
                    fontsize=7.5, color=INK2, style="italic")

    S = summ.set_index("group")
    fig, ax = plt.subplots(figsize=(7, 3.4))
    panel(ax, t, "Women / men median award ratio, full model fitted in each committee", S.loc["All"])
    ax.set_xlabel("Women / men ratio of median award (same team size, year and instrument)")
    fig.text(0.01, -0.09, f"One estimate per ANR committee with ≥{min_per_gender} women and ≥{min_per_gender} men coordinators (2010-2025). "
             "Pooled = inverse-variance weighted.", fontsize=7, color=INK2)
    save_fig(fig, "fig7_full_model_by_committee_hist", t)

    fig, axes = plt.subplots(2, 1, figsize=(7, 5.4), sharex=True)
    for ax, g in zip(axes, ["STEM", "Non-STEM (SHS)"]):
        panel(ax, t[t.group == g], g, S.loc[g])
    axes[1].set_xlabel("Women / men ratio of median award (same team size, year and instrument)")
    fig.text(0.01, -0.04, "Non-STEM = social sciences and humanities committees (CE26, CE27, CE28, CE41, CE53, CE54, "
             "CE55;\n2012-13 SH codes and S56). All other committees = STEM. "
             f"Committees with ≥{min_per_gender} women and ≥{min_per_gender} men.", fontsize=7, color=INK2)
    fig.tight_layout()
    save_fig(fig, "fig8_full_model_by_committee_hist_stem", t)
    return t, summ


def share_funding(a):
    d = a[a.gender.isin(["F", "M"])]
    g = d.groupby("year").apply(lambda s: pd.Series({
        "share_projects_F": (s.gender == "F").mean(),
        "share_funding_F": s.loc[s.gender == "F", "amount"].sum() / s.amount.sum(),
        "n_known": len(s),
    }), include_groups=False).reset_index()
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(g.year, g.share_projects_F * 100, color=C_F, marker="o", ms=4, label="Share of projects")
    ax.plot(g.year, g.share_funding_F * 100, color=INK2, marker="s", ms=4, ls="--", lw=1.6, label="Share of funding")
    last = g.iloc[-1]
    ax.annotate(f"projects {last.share_projects_F*100:.1f}%", (last.year, last.share_projects_F * 100),
                xytext=(5, 3), textcoords="offset points", fontsize=8, color=INK2)
    ax.annotate(f"funding {last.share_funding_F*100:.1f}%", (last.year, last.share_funding_F * 100),
                xytext=(5, -10), textcoords="offset points", fontsize=8, color=INK2)
    ax.set_ylim(15, 45)
    ax.set_ylabel("Women coordinators (%)")
    ax.set_title("Women's share of ANR generic-call projects and of the money (known gender)", loc="left")
    ax.legend(loc="upper left")
    ax.set_xlim(g.year.min() - 0.5, g.year.max() + 2)
    fig.text(0.01, -0.03, "2010-13: Blanc + JCJC programmes; 2014-25: AAPG. Nominal euros.", fontsize=7, color=INK2)
    save_fig(fig, "fig6_share_projects_vs_funding", g)
    return g


def validation(a):
    anr = {2015: 28.2, 2018: 30.0, 2020: 32.3, 2022: 32.6, 2024: 35.5}
    s = a[a.call == "AAPG"]
    rows = []
    for y in sorted(s.year.unique()):
        x = s[s.year == y]
        nf, nm, nu = (x.gender == "F").sum(), (x.gender == "M").sum(), (x.gender == "U").sum()
        comb = x.gender_combined
        rows.append({"year": y, "n": len(x), "share_F_of_known": nf / (nf + nm) * 100,
                     "share_F_of_all": nf / len(x) * 100,
                     "share_F_with_secondary": (comb == "F").sum() / (comb.isin(["F", "M"])).sum() * 100,
                     "unknown_pct": nu / len(x) * 100, "ANR_report": anr.get(y, np.nan)})
    t = pd.DataFrame(rows)
    t["diff_known_vs_ANR"] = t.share_F_of_known - t.ANR_report
    t["flag_gt3pts"] = t.diff_known_vs_ANR.abs() > 3
    t.to_csv(TAB / "validation_vs_anr.csv", index=False)

    fig, ax = plt.subplots(figsize=(6.5, 3.3))
    ax.plot(t.year, t.share_F_of_known, color=C_F, marker="o", ms=4, label="This analysis (known gender)")
    v = t.dropna(subset=["ANR_report"])
    ax.plot(v.year, v.ANR_report, "D", color=INK, ms=6, label="ANR report", ls="none")
    ax.set_ylabel("Women among AAPG coordinators (%)")
    ax.set_ylim(20, 40)
    ax.legend(loc="upper left")
    ax.set_title("Validation: inferred share vs. ANR's published share", loc="left")
    save_fig(fig, "fig0_validation_vs_anr", t)
    return t


def unknown_profile(a):
    by_year = a.groupby("year").apply(lambda s: (s.gender == "U").mean() * 100, include_groups=False).rename("unknown_pct")
    by_instr = a.groupby("instrument").apply(lambda s: (s.gender == "U").mean() * 100, include_groups=False).rename("unknown_pct")
    cmp = a.assign(g=a.gender.map({"F": "Women", "M": "Men", "U": "Unknown"})).groupby("g").agg(
        n=("amount", "size"), median_amount=("amount", "median"), mean_amount=("amount", "mean"),
        mean_partners=("n_partners", "mean"))
    mix = pd.crosstab(a.gender, a.instrument, normalize="index").mul(100).round(1)
    rules = a.rule.value_counts()
    sec = a[a.gender == "U"].gender_secondary.value_counts()
    return by_year, by_instr, cmp, mix, rules, sec


def robustness(a):
    out = []
    variants = {
        "Main (Insee ≥95%)": (a, "gender"),
        "Strict Insee ≥99%": (a, "gender_99"),
        "Unknown assigned by gender-guesser": (a, "gender_combined"),
        "Excluding top 1% awards": (a[a.amount <= a.amount.quantile(0.99)], "gender"),
    }
    for name, (d, gcol) in variants.items():
        # median ratios within instrument
        for ins in INSTR_ORDER:
            s = d[d.instrument == ins]
            f, m = s[s[gcol] == "F"].amount.values, s[s[gcol] == "M"].amount.values
            if len(f) < 10 or len(m) < 10:
                continue
            r, lo, hi = boot_ratio(f, m)
            out.append({"variant": name, "estimate": f"median ratio: {ins}", "value": r, "lo": lo, "hi": hi,
                        "n": len(f) + len(m)})
        reg = regressions(d, gender_col=gcol, label=name)
        for _, r in reg[reg.spec.str.startswith(("A:", "B:"))].iterrows():
            out.append({"variant": name, "estimate": "regression " + r.spec + " (%)", "value": r.pct,
                        "lo": r.lo, "hi": r.hi, "n": r.n})
    t = pd.DataFrame(out)
    t.to_csv(TAB / "7_robustness.csv", index=False)
    return t


def proxy_validation(p):
    """How well does the partner-based proxy recover the true 2010-13 JCJC/Blanc split?"""
    s = p[p.call.isin(["JCJC", "Blanc"])]
    t = pd.crosstab(s.call, s.instrument_proxy, margins=True)
    return t


def pia_context(ref):
    """ANR_02 (France 2030 / PIA, DGPIE): context only, excluded from the main analysis."""
    pr = pd.read_csv(PIA_PROJ, sep=";", low_memory=False)
    pt = pd.read_csv(PIA_PART, sep=";", low_memory=False)
    co = (pt[pt["Projet.Partenaire.Est_coordinateur"].astype(str).isin(["True", "Oui"])]
          .drop_duplicates(K).set_index(K)["Projet.Partenaire.Responsable_scientifique.Prenom"])
    pr["g"] = infer_gender(pr[K].map(co), ref, 0.95).g.values
    known = pr[pr.g.isin(["F", "M"])]
    return {"n_projects": len(pr), "years": f"{pr['Action.Edition'].min()}-{pr['Action.Edition'].max()}",
            "total_eur": pr["Projet.Aide_allouee"].sum(), "median_eur": pr["Projet.Aide_allouee"].median(),
            "share_F_known": (known.g == "F").mean(), "share_funding_F": known.loc[known.g == "F", "Projet.Aide_allouee"].sum() / known["Projet.Aide_allouee"].sum(),
            "unknown_pct": (pr.g == "U").mean() * 100, "columns": list(pr.columns)}


# ---------------------------------------------------------------------------
def main():
    proj, part, insee = load()
    ref = build_reference(insee)
    ce_labels = json.loads(CE_LABELS.read_text())
    p = build_projects(proj, part, ref, ce_labels)

    out_cols = [K, "year", "call", "instrument", "instrument_proxy", "committee", "committee_label", "domain",
                "amount", "n_partners", "n_foreign", "has_firm", "n_coord", "coord_first_name", "gender",
                "rule", "gender_99", "gender_secondary"]
    p[out_cols].rename(columns={K: "code"}).to_csv(PROC / "projects_with_gender.csv", index=False)

    a = p[(p.year >= MAIN_YEARS[0]) & (p.year <= MAIN_YEARS[1]) & p.amount.gt(0)].copy()

    res = {}
    res["proxy_validation"] = proxy_validation(p)
    res["validation"] = validation(a)
    res["unknown"] = unknown_profile(a)
    res["desc"] = descriptives(a)
    res["within"] = pooled_and_within(a)
    reg = regressions(a)
    reg.to_csv(TAB / "4_regressions.csv", index=False)
    res["reg"] = reg
    res["dom"], res["cells"] = by_domain_committee(a)
    res["model_fit"] = model_fit(a)
    res["raw_team"] = raw_vs_team_size(a, res["model_fit"])
    for tag, ces, title in SUBSETS:
        s_ = a[a.committee.isin(ces)]
        mf = model_fit(s_, tag=tag)
        raw_vs_team_size(s_, mf, tag=tag, title=title)
    res["field_hist"] = field_histograms(a)
    res["share"] = share_funding(a)
    res["robust"] = robustness(a)
    res["pia"] = pia_context(ref)

    # summary bits for the report
    summary = {
        "n_projects_scope": int(len(a)),
        "n_projects_all_years": int(len(p)),
        "years": MAIN_YEARS,
        "coord_counts": p.n_coord.value_counts().sort_index().to_dict(),
        "rows_proj": int(len(proj)), "rows_part": int(len(part)), "cols_proj": list(proj.columns),
        "cols_part": list(part.columns),
        "amount_matches_partner_sum": float(((p.amount - p.partner_sum).abs() < 1).mean()),
        "n_2026_excluded": int((p.year == 2026).sum()),
        "n_zero_amount": int((p.amount.fillna(0) <= 0).sum()),
        "programme_counts": p.groupby(["call", "year"]).size().unstack(fill_value=0),
        "instrument_counts": pd.crosstab(a.instrument, a.year),
        "committee_counts": a.committee.value_counts(),
        "unknown_overall": float((a.gender == "U").mean() * 100),
        "ref_size": len(ref),
    }
    res["summary"] = summary
    pd.to_pickle(res, PROC / "results.pkl")
    print_console(res)
    return res


def print_console(res):
    pd.set_option("display.width", 200)
    s = res["summary"]
    print("scope", s["n_projects_scope"], "coord counts", s["coord_counts"], "unknown %", round(s["unknown_overall"], 1))
    print(res["proxy_validation"])
    print(res["validation"].round(1).to_string())
    print(res["within"].round(3).to_string())
    print(res["reg"].round(2).to_string())
    print(res["dom"][res["dom"].level == "domain"].round(2).to_string())
    print(res["robust"].round(3).to_string())


if __name__ == "__main__":
    main()
