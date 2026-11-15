# study_05 - curator only

HOXA1 knockdown vs scramble; human lung fibroblasts, HiSeq only. Selected samples: 3 treated / 3 control.

- Paper: Trapnell et al. (2013), [Differential analysis of gene regulation at transcript resolution with RNA-seq](https://doi.org/10.1038/nbt.2450).
- DOI: [10.1038/nbt.2450](https://doi.org/10.1038/nbt.2450); [PubMed 23222703](https://pubmed.ncbi.nlm.nih.gov/23222703/).
- GEO: [GSE37703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37703).
- SRA: [PRJNA162905](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA162905); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493369%20OR%20SRR493370%20OR%20SRR493371) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR493366%20OR%20SRR493367%20OR%20SRR493368).
- Author DEG reference: [GSE37703_hiseq_cuffdiff_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE37nnn/GSE37703/suppl/GSE37703_hiseq_cuffdiff_gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

The six corresponding MiSeq records must not be counted as six additional biological replicates. The reference uses assembled `ucscCodingXLOC_` IDs, so the original annotation must accompany any later scoring setup. This method-development dataset is widely reused in tutorials.

Direction: Reference labels are `Lung_Scramble` (sample_1) and `Lung_A1KD` (sample_2). Cuffdiff reports sample_2/sample_1: knockdown/control.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM925765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925765) | HOXA1 knockdown | SRR493369 |
| [GSM925766](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925766) | HOXA1 knockdown | SRR493370 |
| [GSM925767](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925767) | HOXA1 knockdown | SRR493371 |
| [GSM925762](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925762) | scramble | SRR493366 |
| [GSM925763](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925763) | scramble | SRR493367 |
| [GSM925764](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM925764) | scramble | SRR493368 |

Checked 2026-11-15. Complete author result file downloaded for inspection (842,222 bytes). SHA-256: `d4859e418f38f8c14b79ce27a477f318f4a9001a4f191790b9c3885661564075`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
