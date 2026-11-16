# task_21 — research and reference notes

**Selected comparison: Sun1 KO tumors vs control tumors.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Sun1 knockout vs control; CT26 whole tumors at day 14. Selected samples: 7 treated / 8 control.

- Task: [task_21](../task_21/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Nasr et al. (2024), [A computational pipeline for identifying gene targets and signalling pathways in cancer cells to improve lymphocyte infiltration and immune checkpoint therapy efficacy](https://doi.org/10.1016/j.ebiom.2024.105167).
- DOI: [10.1016/j.ebiom.2024.105167](https://doi.org/10.1016/j.ebiom.2024.105167); [PubMed 38805852](https://pubmed.ncbi.nlm.nih.gov/38805852/).
- GEO: [GSE250602](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250602).
- SRA: [PRJNA1054607](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1054607); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR27292554%20OR%20SRR27292555%20OR%20SRR27292556%20OR%20SRR27292557%20OR%20SRR27292558%20OR%20SRR27292559%20OR%20SRR27292560) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR27292546%20OR%20SRR27292547%20OR%20SRR27292548%20OR%20SRR27292549%20OR%20SRR27292550%20OR%20SRR27292551%20OR%20SRR27292552%20OR%20SRR27292553).
- Author DEG reference: [GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE250602&format=file&file=GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz).
- Result fields: ID `__rowname__`, log2FC `log2FoldChange`, adjusted P `padj`.

Seven knockout and eight control whole tumors. Do not substitute cultured-cell or purified-cell tables. The author result is control/KO and is flipped to KO/control. Tissue-composition changes are part of this comparison.

Direction: Flip the author log2FC sign to treated/control.

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

Checked 2026-11-15. Complete reference-file SHA-256: `949d70e15c7d8e2feffd31086fe9384cdc47b1f6a13d2ac38ca4b413281cfe2e`.
Eligible distinct IDs: up=11,806, down=9,208. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_18`; previous task: `task_021`.
- Previous reference filename: `GSE250602_DESeq2_CT26_tumors_Control_vs_KO__Sun1_KO_vs_control_tumors_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_18/author_results/GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz`.
- Extraction columns: ID `__rowname__`, log2FC `log2FoldChange`, adjusted P `padj`; no status column configured.
- Existing extraction direction multiplier: reversed (-1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `949d70e15c7d8e2feffd31086fe9384cdc47b1f6a13d2ac38ca4b413281cfe2e`.
- Migrated JSON SHA-256: `994e94bdb4089e749b7b09e66a523c8a69a3d4bdefe88a55d121912201fc47df`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
