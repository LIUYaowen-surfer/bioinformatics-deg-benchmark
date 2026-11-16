# task_01 — research and reference notes

**Selected comparison: Dexamethasone vs untreated.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Dexamethasone vs untreated human airway smooth muscle cells; 8 relevant samples.

- Reference answers: [reference/](reference/).
- Paper: Himes et al. (2014), [RNA-Seq Transcriptome Profiling Identifies CRISPLD2 as a Glucocorticoid Responsive Gene that Modulates Cytokine Function in Airway Smooth Muscle Cells](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099625).
- DOI: [10.1371/journal.pone.0099625](https://doi.org/10.1371/journal.pone.0099625).
- GEO: [GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778).
- SRA: [SRP033351](https://www.ncbi.nlm.nih.gov/sra?term=SRP033351).
- Author DEG results: [Dex vs untreated](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_01` | Dexamethasone vs untreated | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR1039508%20OR%20SRR1039509%20OR%20SRR1039512%20OR%20SRR1039513%20OR%20SRR1039516%20OR%20SRR1039517%20OR%20SRR1039520%20OR%20SRR1039521) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `_R1.fastq.gz` and `_R2.fastq.gz` for paired reads; retain any unpaired reads as `_unpaired.fastq.gz`.
The same donor alias identifies the same donor across the two conditions.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR1039508` | `untreated_donor01` |
| `SRR1039509` | `treated_donor01` |
| `SRR1039512` | `untreated_donor02` |
| `SRR1039513` | `treated_donor02` |
| `SRR1039516` | `untreated_donor03` |
| `SRR1039517` | `treated_donor03` |
| `SRR1039520` | `untreated_donor04` |
| `SRR1039521` | `treated_donor04` |

## Reference provenance and migration

- Previous source study: `study_01`; previous task: `task_001`.
- Previous reference filename: `GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `GSE52778_Dex_vs_Untreated_gene_exp.diff.gz`.
- Extraction columns: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`; `status` = `OK`.
- Existing extraction direction multiplier: reversed (-1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f`.
- Migrated JSON SHA-256: `69a845e754bffd0d8f27a2eab6cbb706ee110af3aef5a8aae5f7609e50773ae7`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
