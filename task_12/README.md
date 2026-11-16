# task_12 — research and reference notes

**Selected comparison: cord-blood-derived vs adult-bone-marrow-derived.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Cord-blood-derived vs adult-bone-marrow-derived human erythroid cells after xenograft. Selected samples: 3 treated / 3 control.

- Task: [task_12](../task_12/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Fiorini et al. (2017), [Developmentally-faithful and effective human erythropoiesis in immunodeficient and Kit mutant mice](https://doi.org/10.1002/ajh.24805).
- DOI: [10.1002/ajh.24805](https://doi.org/10.1002/ajh.24805); [PubMed 28568895](https://pubmed.ncbi.nlm.nih.gov/28568895/).
- GEO: [GSE100077](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100077).
- SRA: [PRJNA390632](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA390632); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR5687582%20OR%20SRR5687583%20OR%20SRR5687584) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR5687579%20OR%20SRR5687580%20OR%20SRR5687581).
- Author DEG reference: [GSE100077_DifferentialExpression.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE100077&format=file&file=GSE100077_DifferentialExpression.csv.gz).
- Result fields: ID `gene`, log2FC `logFC`, adjusted P `adj.P.Val`.

Three independent xenograft recipients per group. Use adj.P.Val, not P.Value. This is a source/developmental comparison, with treated/untreated used only as benchmark aliases.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2670892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670892) | cord-blood-derived | SRR5687582 |
| [GSM2670893](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670893) | cord-blood-derived | SRR5687583 |
| [GSM2670894](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670894) | cord-blood-derived | SRR5687584 |
| [GSM2670889](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670889) | adult-bone-marrow-derived | SRR5687579 |
| [GSM2670890](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670890) | adult-bone-marrow-derived | SRR5687580 |
| [GSM2670891](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670891) | adult-bone-marrow-derived | SRR5687581 |

Checked 2026-11-15. Complete reference-file SHA-256: `064b53dacc025859df89af5c756514b948d0bc47812a5e343deba65c209a52e3`.
Eligible distinct IDs: up=12,253, down=12,059. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_09`; previous task: `task_012`.
- Previous reference filename: `GSE100077_DifferentialExpression__cord_blood_vs_adult_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_09/author_results/GSE100077_DifferentialExpression.csv.gz`.
- Extraction columns: ID `gene`, log2FC `logFC`, adjusted P `adj.P.Val`; no status column configured.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `064b53dacc025859df89af5c756514b948d0bc47812a5e343deba65c209a52e3`.
- Migrated JSON SHA-256: `26c5590a502e041456dcf919e1f97c7680b412b1fd209961574ced5ee4dcd456`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
