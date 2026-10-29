"""DATA-02: nationality of external researcher recruits (CR/DR) in public research organisations, by year."""
import csv, collections
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-02/data"
c = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(f"{D}/fr-esr-epst-epic-fondations-chercheurs-recrutements-nationalites.csv", encoding="utf-8-sig"), delimiter=";"):
    if r["filiere"] != "CR-DR": continue
    c[(r["annee"], r["cat_corps_dt"])][r["groupe"]] += float(r["recr"] or 0)
with open(f"{D}/DATA-02_researcher_recruits_nationality.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["annee", "corps", "France", "UE_28", "Hors_UE", "pct_foreign"])
    for k in sorted(c):
        a = c[k]; t = sum(a.values())
        w.writerow([*k, int(a["France"]), int(a["UE 28"]), int(a["Hors UE"]), round(100 * (t - a["France"]) / t, 1) if t else ""])
print(open(f"{D}/DATA-02_researcher_recruits_nationality.csv").read())
