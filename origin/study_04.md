# study_04 — curator only

siSRSF1 vs non-targeting control siRNA in HeLa cells; 4 relevant samples.

- Paper: Olazabal-Herrero et al. (2024), [The FANCI/FANCD2 complex links DNA damage response to R-loop regulation through SRSF1-mediated mRNA export](https://pmc.ncbi.nlm.nih.gov/articles/PMC10865995/).
- DOI: [10.1016/j.celrep.2023.113610](https://doi.org/10.1016/j.celrep.2023.113610).
- GEO: [GSE212471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212471).
- SRA: [PRJNA875477](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA875477).
- Author DEG results: [siSRSF1 vs control siRNA](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_007` | siSRSF1 vs control siRNA | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR21381100%20OR%20SRR21381101%20OR%20SRR21381102%20OR%20SRR21381103) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `_R1.fastq.gz` and `_R2.fastq.gz` for paired reads; retain any unpaired reads as `_unpaired.fastq.gz`.
Sample numbers are anonymous identifiers, not pairing labels.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR21381100` | `SRSF1_siRNA_sample04` |
| `SRR21381101` | `SRSF1_siRNA_sample03` |
| `SRR21381102` | `control_siRNA_sample02` |
| `SRR21381103` | `control_siRNA_sample01` |
