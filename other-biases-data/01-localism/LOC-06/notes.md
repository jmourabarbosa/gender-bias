# LOC-06 - Godechot, Issiakou, Renisio & Rougier (2025), Le localisme universitaire, nouvelles évaluations

- **Citation:** Godechot O., Issiakou R., Renisio Y., Rougier A. (2025), La Vie des idées / Books & Ideas, 18 novembre 2025 (French text).
- **url_used:** https://booksandideas.net/IMG/pdf/20251118_godechot-2.pdf (byte-identical to https://laviedesidees.fr/IMG/pdf/20251118_godechot-2.pdf)
- **access_status:** downloaded

## Headline number
On ~7,900 MCF hirings 2017-2024, local candidates have 9.5 (wide scope) to 10.7 (narrow scope) times the odds of external ones (Mantel-Haenszel; Tableau 2, PDF p.12). By CNU section the OR ranges from 0.5 (mathematics) to 29 (physiology) (p.13, fig. 1 p.15). MESR local-recruitment rate fell from 32% (2002) to 27% (2008) and 21% (2010), ~20-22% since 2018 (fig. 3 p.19, text p.20).

**Key-number check:** **MATCH** (9.5-10.7; physiology OR ~29).

## Figures (PDF page of origin)
- `figures/LOC-06_fig1.png`: Figure 1, PDF p.15: MH odds ratio by CNU section (log scale)
- `figures/LOC-06_fig2.png`: Figure 3, PDF p.19: MCF local-recruitment rate 2002-2022 (MESR data)
- `figures/LOC-06_fig3.png`: Figure 4, PDF p.21: odds ratios 1970-80 (2008 article) vs 2017-24 by discipline
- `figures/LOC-06_redraw.png`: B/W redraw of fig. 1 with 95% CIs

## Data
data/LOC-06.csv: per CNU section N recruits, N local recruits, expected locals (printed in the figure labels) + odds ratio and 95% CI **read from the vector drawing** of fig. 1 (log axis calibrated on tick labels, max residual 0.08 pt); checks: physiology 29.0, biochemistry 22.5, maths 0.5 match the text (p.13). CI lower bounds equal to 0.5/1.0 (maths, anthropology, constituants élémentaires) may be clipped at the axis. The ORs are not printed as numbers in the source, so treat as approximate. data/LOC-06_fig3_local_rate.csv: local-recruitment rate 2002-2022 digitized from fig. 3 (no 2013 point in the figure).

## Notes
French original page saved as page_laviedesidees.html. It links a replication archive http://olivier.godechot.free.fr/hopfichiers/localisme_2025.zip - NOT fetched: plain-HTTP host does not resolve through the sandbox proxy and HTTPS is refused. The user can download it manually.

Scripts: `scripts/other/` (figtools.py for crops; see the per-source scripts named after the IDs).
