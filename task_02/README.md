# task_02 — research and reference notes

**Selected comparison: Lrpprc knockout vs wild type.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Lrpprc knockout vs wild-type mouse hearts; 8 samples.

- Reference answers: [reference/](reference/).
- Paper: Siira et al. (2017), [LRPPRC-mediated folding of the mitochondrial transcriptome](https://pmc.ncbi.nlm.nih.gov/articles/PMC5691074/).
- DOI: [10.1038/s41467-017-01221-z](https://doi.org/10.1038/s41467-017-01221-z).
- GEO: [GSE100732](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100732), the RNA-seq subset of [GSE100733](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100733).
- SRA: [SRP110979](https://www.ncbi.nlm.nih.gov/sra?term=SRP110979).
- Author DEG results: [Knockout vs wild type](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_02` | Lrpprc knockout vs wild type | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5799230%20OR%20SRR5799231%20OR%20SRR5799232%20OR%20SRR5799233%20OR%20SRR5799234%20OR%20SRR5799235%20OR%20SRR5799236%20OR%20SRR5799237) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `_R1.fastq.gz` and `_R2.fastq.gz` for paired reads; retain any unpaired reads as `_unpaired.fastq.gz`.
Sample numbers are anonymous identifiers, not pairing labels.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR5799230` | `treated_sample01` |
| `SRR5799231` | `treated_sample02` |
| `SRR5799232` | `treated_sample03` |
| `SRR5799233` | `treated_sample04` |
| `SRR5799234` | `untreated_sample05` |
| `SRR5799235` | `untreated_sample06` |
| `SRR5799236` | `untreated_sample07` |
| `SRR5799237` | `untreated_sample08` |

## Reference provenance and migration

- Previous source study: `study_02`; previous task: `task_002`.
- Previous reference filename: `GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `GSE100732_DESeq2.results.txt.gz`.
- Extraction columns: ID `__rowname__`, log2FC `log2FoldChange`, adjusted P `padj`; no status column configured.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df`.
- Migrated JSON SHA-256: `f9f9f264a4a5dcb8cc989b6ae4905195f8eb1fc494da5d9d0fd2b4f3bd7604c6`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
