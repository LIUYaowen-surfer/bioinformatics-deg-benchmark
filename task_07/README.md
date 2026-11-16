# task_07 — research and reference notes

**Selected comparison: siSRSF1 vs control siRNA.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

siSRSF1 vs non-targeting control siRNA in HeLa cells; 4 relevant samples.

- Reference answers: [reference/](reference/).
- Paper: Olazabal-Herrero et al. (2024), [The FANCI/FANCD2 complex links DNA damage response to R-loop regulation through SRSF1-mediated mRNA export](https://pmc.ncbi.nlm.nih.gov/articles/PMC10865995/).
- DOI: [10.1016/j.celrep.2023.113610](https://doi.org/10.1016/j.celrep.2023.113610).
- GEO: [GSE212471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212471).
- SRA: [PRJNA875477](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA875477).
- Author DEG results: [siSRSF1 vs control siRNA](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_07` | siSRSF1 vs control siRNA | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR21381100%20OR%20SRR21381101%20OR%20SRR21381102%20OR%20SRR21381103) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `_R1.fastq.gz` and `_R2.fastq.gz` for paired reads; retain any unpaired reads as `_unpaired.fastq.gz`.
Sample numbers are anonymous identifiers, not pairing labels.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR21381100` | `treated_sample04` |
| `SRR21381101` | `treated_sample03` |
| `SRR21381102` | `untreated_sample02` |
| `SRR21381103` | `untreated_sample01` |

## Reference provenance and migration

- Previous source study: `study_04`; previous task: `task_007`.
- Previous reference filename: `GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz`.
- Extraction columns: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`; `status` = `OK`.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `4c9f9e881aa7555dd47804b261c5753e13e1b48792d5f128a3d97226ae0641d1`.
- Migrated JSON SHA-256: `164f8bc8900745b1652f3e631ee880c857c0bf97cd3cc73fef1677b826cdf1bd`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
