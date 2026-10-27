"""Fetch NIH Data Book reports (success rates by sex) as JSON and write tidy CSVs.
API discovered from https://report.nih.gov/nihdatabook/ app bundle:
  https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=<id>
  https://report.nih.gov/reportweb/api/report/Get/<id>   (metadata, footnotes)
"""
import csv, json, sys, urllib.request, os
UA = "gender-bias-talk-collector/1.0 (mailto:joaoifodase@gmail.com)"
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60))
for rid in [131, 132]:
    d = get(f"https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId={rid}")
    m = get(f"https://report.nih.gov/reportweb/api/report/Get/{rid}")
    json.dump({"data": d, "meta": m}, open(f"{out}/nih_databook_report{rid}.json", "w"), indent=1)
    with open(f"{out}/nih_databook_report{rid}.csv", "w", newline="") as f:
        w = csv.writer(f)
        if d.get("dataSets"):
            hdr = d["data"][0][0]
            w.writerow(["dataset"] + hdr)
            for name, tab in zip(d["dataSets"], d["data"]):
                for row in tab[1:]:
                    w.writerow([name] + row)
        else:
            for row in d["data"]:
                w.writerow(row)
    print(rid, m.get("ReportName"), d.get("lastUpdated"))
