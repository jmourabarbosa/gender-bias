"""DATA-02: doctoral enrolments and funding of new doctoral students by year (MESR ED dataset)."""
import csv, collections
D = "/home/user/gender-bias/other-biases-data/10-datasets/DATA-02/data"
c = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(f"{D}/fr-esr-effectifs-doctorants-docteurs-ecoles-doctorales-financements-doctorants-c.csv", encoding="utf-8-sig"), delimiter=";"):
    for k in ("premiers_inscrits", "total_inscrits", "nombre_soutenances", "fin", "nofin", "activite_perso", "nr"):
        try: c[r["annee"]][k] += int(float(r[k] or 0))
        except ValueError: pass
with open(f"{D}/DATA-02_doctorants_by_year.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["annee", "total_inscrits", "premiers_inscrits", "soutenances", "new_funded", "new_unfunded", "new_salaried_other_activity", "new_not_reported", "pct_new_funded"])
    for y in sorted(c):
        a = c[y]; base = a["fin"] + a["nofin"] + a["activite_perso"] + a["nr"]
        w.writerow([y, a["total_inscrits"], a["premiers_inscrits"], a["nombre_soutenances"], a["fin"], a["nofin"], a["activite_perso"], a["nr"],
                    round(100 * a["fin"] / base, 1) if base else ""])
print(open(f"{D}/DATA-02_doctorants_by_year.csv").read())
