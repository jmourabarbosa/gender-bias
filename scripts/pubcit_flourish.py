"""Extract _Flourish_data and column names from a Flourish embed HTML into CSV.
Usage: python3 -I pubcit_flourish.py embed.html out.csv"""
import sys, json, re, csv
t = open(sys.argv[1], encoding="utf-8", errors="ignore").read()
def grab(name):
    i = t.find(name + " = ")
    if i < 0: return None
    obj, _ = json.JSONDecoder().raw_decode(t[i + len(name) + 3:])
    return obj
data = grab("_Flourish_data")
cols = grab("_Flourish_data_column_names") or {}
m = re.search(r'"title"\s*:\s*"([^"]*)"', t)
print("title:", m.group(1) if m else None, "| cols:", cols.get("data"))
rows = data["data"]
c = cols.get("data", {})
header = [c.get("label", "label")] + (c.get("value") or [f"value{i}" for i in range(len(rows[0]["value"]))])
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f); w.writerow(header)
    for r in rows: w.writerow([r["label"]] + r["value"])
print(len(rows), "rows")
