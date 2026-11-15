# study_18 - curator only

Sun1 knockout vs control; CT26 whole tumors at day 14. Selected samples: 7 treated / 8 control.

- Paper: Nasr et al. (2024), [A computational pipeline for identifying gene targets and signalling pathways in cancer cells to improve lymphocyte infiltration and immune checkpoint therapy efficacy](https://doi.org/10.1016/j.ebiom.2024.105167).
- DOI: [10.1016/j.ebiom.2024.105167](https://doi.org/10.1016/j.ebiom.2024.105167); [PubMed 38805852](https://pubmed.ncbi.nlm.nih.gov/38805852/).
- GEO: [GSE250602](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250602).
- SRA: [PRJNA1054607](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1054607); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR27292554%20OR%20SRR27292555%20OR%20SRR27292556%20OR%20SRR27292557%20OR%20SRR27292558%20OR%20SRR27292559%20OR%20SRR27292560) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR27292546%20OR%20SRR27292547%20OR%20SRR27292548%20OR%20SRR27292549%20OR%20SRR27292550%20OR%20SRR27292551%20OR%20SRR27292552%20OR%20SRR27292553).
- Author DEG reference: [GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE250nnn/GSE250602/suppl/GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz).
- Result fields: Unnamed first column (gene ID), `log2FoldChange`, `padj`.

Seven knockout and eight control tumor samples. Use the whole-tumor reference; separate cultured-cell and purified-cell files represent different experiments. The cultured subset has only one KO sample. Whole-tumor differences also reflect cellular composition.

Direction: Desired direction is KO/control. The inspected header does not state the coefficient direction; filename order is insufficient evidence.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM7982766](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982766) | Sun1 KO tumors | SRR27292560 |
| [GSM7982767](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982767) | Sun1 KO tumors | SRR27292559 |
| [GSM7982768](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982768) | Sun1 KO tumors | SRR27292558 |
| [GSM7982769](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982769) | Sun1 KO tumors | SRR27292557 |
| [GSM7982770](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982770) | Sun1 KO tumors | SRR27292556 |
| [GSM7982771](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982771) | Sun1 KO tumors | SRR27292555 |
| [GSM7982772](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982772) | Sun1 KO tumors | SRR27292554 |
| [GSM7982773](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982773) | control tumors | SRR27292553 |
| [GSM7982774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982774) | control tumors | SRR27292552 |
| [GSM7982775](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982775) | control tumors | SRR27292551 |
| [GSM7982776](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982776) | control tumors | SRR27292550 |
| [GSM7982777](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982777) | control tumors | SRR27292549 |
| [GSM7982778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982778) | control tumors | SRR27292548 |
| [GSM7982779](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982779) | control tumors | SRR27292547 |
| [GSM7982780](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7982780) | control tumors | SRR27292546 |

Checked 2026-11-15. Complete author result file downloaded for inspection (803,165 bytes). SHA-256: `949d70e15c7d8e2feffd31086fe9384cdc47b1f6a13d2ac38ca4b413281cfe2e`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
