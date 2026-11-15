# study_05 - curator only

HOXA1 knockdown vs scramble; human lung fibroblasts, HiSeq only. Selected samples: 3 treated / 3 control.

- Task: [task_008](../task/task_008.md).
- Reference: [top100 JSON](reference_json/study_05/GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json).
- Paper: Trapnell et al. (2013), [Differential analysis of gene regulation at transcript resolution with RNA-seq](https://doi.org/10.1038/nbt.2450).
- DOI: [10.1038/nbt.2450](https://doi.org/10.1038/nbt.2450); [PubMed 23222703](https://pubmed.ncbi.nlm.nih.gov/23222703/).
- GEO: [GSE37703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37703).
- SRA: [PRJNA162905](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA162905); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493369%20OR%20SRR493370%20OR%20SRR493371) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493366%20OR%20SRR493367%20OR%20SRR493368).
- Author DEG reference: [GSE37703_hiseq_cuffdiff_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE37703&format=file&file=GSE37703_hiseq_cuffdiff_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Use the six HiSeq samples only. The corresponding MiSeq records are additional sequencing of the material, not extra biological replicates. Preserve the author assembled ucscCodingXLOC annotation. This dataset is widely reused in tutorials.

Direction: Keep the author log2FC sign (treated/control). Evidence is recorded in the [extraction record](reference_json/extraction_log.md).

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
