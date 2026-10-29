"""anr_fetch_by_year.py OUTDIR -- ANR_01 (DOS/DGDS) since-2010 projects+partners via tabular-api.data.gouv.fr CSV
export, split by decision-code year (ANR-YY-) because the full-file export is refused (403) and
static.data.gouv.fr resets every connection through this proxy. Writes one merged CSV per table."""
import sys, io, csv, time, requests
out = sys.argv[1]
T = "https://tabular-api.data.gouv.fr/api/resources/{}/data/csv/"
RES = {"partenaires": ("4b576f41-8f4a-4f0f-860a-98eca420f3b9", None),
       "projets": ("87d29a24-392e-4a29-a009-83eddcff3e66",
                   "Projet.Code_Decision,AAP.Edition,Projet.Acronyme,Projet.Titre.Anglais,Programme.Acronyme,Projet.Montant.AF.Aide_allouee.ANR,Projet.T0 scientifique")}


def get(url, params):
    for i in range(25):
        try:
            r = requests.get(url, params=params, timeout=(20, 180))
            if r.status_code == 200 and r.text.startswith("__id"):
                return r.text
            print("http", r.status_code, params, r.text[:120], flush=True)
        except Exception:
            pass
        time.sleep(min(3 + 3 * i, 40))
    raise SystemExit(f"gave up {params}")


for name, (rid, cols) in RES.items():
    rows, header = [], None
    for yy in range(10, 27):
        p = {"Projet.Code_Decision__contains": f"ANR-{yy:02d}-"}
        if cols:
            p["columns"] = cols
        rd = list(csv.reader(io.StringIO(get(T.format(rid), p))))
        header = header or rd[0]
        assert rd[0] == header
        rows += rd[1:]
        print(name, yy, len(rd) - 1, flush=True)
    with open(f"{out}/anr-dgds-depuis-2010-{name}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print("wrote", name, len(rows))
