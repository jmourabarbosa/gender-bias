"""Fetch MESR 'fr-esr-enseignants-titulaires-esr-public' (Opendatasoft v2.1) with retries.
Usage: fetch_mesr_ec.py OUTDIR [full]"""
import sys, time, requests, os
out = sys.argv[1]; full = len(sys.argv) > 2
B = 'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-enseignants-titulaires-esr-public/exports/csv'
H = {'User-Agent': 'gender-bias-source-collector/1.0 (mailto:joaoifodase@gmail.com)'}
jobs = [('aggregated_by_year_sex_category_section.csv', {'delimiter': ';', 'select': 'rentree,annee_universitaire,sexe,categorie_assimilation,code_categorie_assimil,grande_discipline,groupe_cnu,code_section_cnu,section_cnu,sum(effectif) as effectif',
         'group_by': 'rentree,annee_universitaire,sexe,categorie_assimilation,code_categorie_assimil,grande_discipline,groupe_cnu,code_section_cnu,section_cnu'})]
if full: jobs.append(('fr-esr-enseignants-titulaires-esr-public.csv', {'delimiter': ';'}))
for name, params in jobs:
    for attempt in range(8):
        try:
            with requests.get(B, params=params, headers=H, stream=True, timeout=(30, 300)) as r:
                r.raise_for_status()
                with open(os.path.join(out, name + '.part'), 'wb') as f:
                    for chunk in r.iter_content(1 << 20): f.write(chunk)
            os.replace(os.path.join(out, name + '.part'), os.path.join(out, name)); print('ok', name, r.url); break
        except Exception as e:
            print('retry', attempt, name, type(e).__name__, str(e)[:120]); time.sleep(15 * (attempt + 1))
