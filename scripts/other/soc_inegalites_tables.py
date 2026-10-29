"""Transcribe the inegalites.fr HTML tables (SOC-01, SOC-02) to CSV."""
import io, sys, pandas as pd
R = '/home/user/gender-bias/other-biases-data/02-social'
def tables(f):
    t = open(f, encoding='utf-8').read()
    return pd.read_html(io.StringIO(t), decimal=',', thousands=' ')
# SOC-01
t1, t2 = tables(f'{R}/SOC-01/page.html')
for t in (t1, t2):
    t.columns = [c[1] if isinstance(c, tuple) else c for c in t.columns]
t1 = t1.rename(columns={t1.columns[0]: 'filiere'}).dropna(how='all')
t2 = t2.rename(columns={t2.columns[0]: 'origine_sociale'}).dropna(how='all')
t1.to_csv(f'{R}/SOC-01/data/SOC-01_table1_filieres.csv', index=False)
t2.to_csv(f'{R}/SOC-01/data/SOC-01.csv', index=False)
print(t1.to_string()); print(t2.to_string())
# SOC-02
(t,) = tables(f'{R}/SOC-02/page.html')
t.columns = [c[1] if isinstance(c, tuple) else c for c in t.columns]
t = t.rename(columns={t.columns[0]: 'origine_sociale'})
rows, filiere = [], None
for _, r in t.iterrows():
    if pd.isna(r['origine_sociale']): continue
    if r.iloc[1:].isna().all(): filiere = r['origine_sociale']; continue
    d = r.to_dict(); d['filiere'] = filiere; rows.append(d)
out = pd.DataFrame(rows)
out = out[['filiere', 'origine_sociale'] + [c for c in out.columns if c not in ('filiere', 'origine_sociale')]]
out.to_csv(f'{R}/SOC-02/data/SOC-02.csv', index=False)
print(out.to_string())
