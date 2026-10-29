"""write_status_other.py ID TITLE URL ACCESS NOTES -- writes other-biases-data/_status/<ID>.json;
file_paths = every file in the source folder (repo-relative), figures_extracted = files in figures/ named <ID>_*."""
import sys, json, glob, os
ROOT = "/home/user/gender-bias"
i, title, url, access, notes = sys.argv[1:6]
folder = glob.glob(f"{ROOT}/other-biases-data/*/{i}")[0]
files = sorted(os.path.relpath(p, ROOT) for p in glob.glob(folder + "/**/*", recursive=True) if os.path.isfile(p))
figs = sorted(os.path.relpath(p, ROOT) for p in glob.glob(f"{folder}/figures/{i}_*") if os.path.isfile(p))
os.makedirs(f"{ROOT}/other-biases-data/_status", exist_ok=True)
json.dump(dict(id=i, title=title, url_used=url, file_paths=files, access_status=access, figures_extracted=figs, notes=notes),
          open(f"{ROOT}/other-biases-data/_status/{i}.json", "w"), indent=1, ensure_ascii=False)
print(i, access, len(files), "files", len(figs), "figs")
