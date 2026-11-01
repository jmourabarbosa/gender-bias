"""Parse ANR AAPG committee (CES) member lists into one row per member and committee-year.

Input: data/raw/committees/ces_aapg_<year>.pdf (see data/raw/SOURCES.md)
Output: data/processed/committee_members.csv  (names: kept local, git-ignored)

    .venv/bin/python parse_committees.py
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw" / "committees"
OUT = ROOT / "data" / "processed" / "committee_members.csv"

HEADER = re.compile(r"\b(CE\d{2})\b")
ROLE = {"président": "chair", "présidente": "chair", "président.e": "chair", "vice-président": "vice-chair",
        "vice-présidents": "vice-chair", "vice-présidente": "vice-chair", "vice-présidentes": "vice-chair",
        "vice-président.e.s": "vice-chair", "vice-président.e": "vice-chair", "membres": "member"}
SEG = re.compile(r"\S(?:.*?\S)?(?=\s{3,}|$)")


def is_upper_token(t: str) -> bool:
    letters = [c for c in t if c.isalpha()]
    return len(letters) >= 2 and sum(c.isupper() for c in letters) / len(letters) >= 0.7


def parse_name(seg: str):
    """'Anna BIRD**' -> ('Anna', 'BIRD', '**'); None if the segment is not a person name."""
    seg = re.sub(r"(\w)- (\w)", r"\1-\2", seg)  # "Marie- Christine" -> "Marie-Christine"
    m = re.match(r"^(.*?)(\*{0,2})$", seg.strip())
    text, stars = m.group(1).strip(), m.group(2)
    toks = text.split()
    if len(toks) < 2 or len(toks) > 7 or any(ch in text for ch in ",()/:;@") or text.endswith("-"):
        return None
    if is_upper_token(toks[0]) or not toks[0][0].isupper():
        return None
    # surname = trailing run of upper-case tokens
    i = len(toks)
    while i > 0 and (is_upper_token(toks[i - 1]) or toks[i - 1].lower() in {"de", "da", "van", "von", "del", "di", "le", "la", "du", "des", "ben", "el"}):
        i -= 1
    if i == len(toks) or i == 0 or not is_upper_token(toks[-1]):
        return None
    first, last = " ".join(toks[:i]), " ".join(toks[i:])
    if any(is_upper_token(t) for t in toks[:i]):
        return None
    return first, last, stars


def parse_pdf(path: Path, year: int) -> list[dict]:
    txt = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True).stdout
    rows, committee, role = [], None, None
    for page in txt.split("\f"):
        lines = page.split("\n")
        for li, line in enumerate(lines):
            low = line.strip().lower()
            if "comité d" in low and "évaluation" in low:
                continue
            h = HEADER.search(line)
            if h and len(line.strip()) < 160 and line.strip().startswith(h.group(1)):
                committee, role = h.group(1), None
                continue
            key = low.rstrip(":").strip()
            if key in ROLE:
                role = ROLE[key]
                continue
            if committee is None or role is None:
                continue
            for m in SEG.finditer(line):
                p = parse_name(m.group(0))
                if not p:
                    continue
                col = m.start()
                title = ""
                for nxt in lines[li + 1:li + 3]:
                    for m2 in SEG.finditer(nxt):
                        if abs(m2.start() - col) <= 3:
                            title = m2.group(0)
                            break
                    if title:
                        break
                rows.append({"year": year, "committee": committee, "role": role, "first_name": p[0],
                             "last_name": p[1], "stage": {"": "both", "*": "stage1", "**": "stage2"}[p[2]],
                             "title": title})
    return rows


def main():
    rows = []
    for f in sorted(RAW.glob("ces_aapg_*.pdf")):
        rows += parse_pdf(f, int(f.stem.split("_")[-1]))
    d = pd.DataFrame(rows).drop_duplicates(["year", "committee", "first_name", "last_name"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    d.to_csv(OUT, index=False)
    print(d.groupby("year").agg(members=("last_name", "size"), committees=("committee", "nunique")))
    return d


if __name__ == "__main__":
    main()
