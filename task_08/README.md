# task_08 — research and reference notes

**Selected comparison: HOXA1 knockdown vs scramble.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

HOXA1 knockdown vs scramble; human lung fibroblasts, HiSeq only. Selected samples: 3 treated / 3 control.

- Task: [task_08](../task_08/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Trapnell et al. (2013), [Differential analysis of gene regulation at transcript resolution with RNA-seq](https://doi.org/10.1038/nbt.2450).
- DOI: [10.1038/nbt.2450](https://doi.org/10.1038/nbt.2450); [PubMed 23222703](https://pubmed.ncbi.nlm.nih.gov/23222703/).
- GEO: [GSE37703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37703).
- SRA: [PRJNA162905](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA162905); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493369%20OR%20SRR493370%20OR%20SRR493371) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493366%20OR%20SRR493367%20OR%20SRR493368).
- Author DEG reference: [GSE37703_hiseq_cuffdiff_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE37703&format=file&file=GSE37703_hiseq_cuffdiff_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Use the six HiSeq samples only. The corresponding MiSeq records are additional sequencing of the material, not extra biological replicates. Preserve the author assembled ucscCodingXLOC annotation. This dataset is widely reused in tutorials.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM925765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925765) | HOXA1 knockdown | SRR493369 |
| [GSM925766](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925766) | HOXA1 knockdown | SRR493370 |
| [GSM925767](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925767) | HOXA1 knockdown | SRR493371 |
| [GSM925762](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925762) | scramble | SRR493366 |
| [GSM925763](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925763) | scramble | SRR493367 |
| [GSM925764](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925764) | scramble | SRR493368 |

Checked 2026-11-15. Complete reference-file SHA-256: `d4859e418f38f8c14b79ce27a477f318f4a9001a4f191790b9c3885661564075`.
Eligible distinct IDs: up=5,522, down=6,087. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_05`; previous task: `task_008`.
- Previous reference filename: `GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_05/author_results/GSE37703_hiseq_cuffdiff_gene_exp.diff.gz`.
- Extraction columns: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`; `status` = `OK`.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `d4859e418f38f8c14b79ce27a477f318f4a9001a4f191790b9c3885661564075`.
- Migrated JSON SHA-256: `573a9accdb7b0a6b808fb3b10d2e94fb65100229d897b954584c6d9da339d778`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
