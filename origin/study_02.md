# study_02 — curator only

Lrpprc knockout vs wild-type mouse hearts; 8 samples.

- Paper: Siira et al. (2017), [LRPPRC-mediated folding of the mitochondrial transcriptome](https://pmc.ncbi.nlm.nih.gov/articles/PMC5691074/).
- DOI: [10.1038/s41467-017-01221-z](https://doi.org/10.1038/s41467-017-01221-z).
- GEO: [GSE100732](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100732), the RNA-seq subset of [GSE100733](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100733).
- SRA: [SRP110979](https://www.ncbi.nlm.nih.gov/sra?term=SRP110979).
- Author DEG results: [Knockout vs wild type](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_002` | Lrpprc knockout vs wild type | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5799230%20OR%20SRR5799231%20OR%20SRR5799232%20OR%20SRR5799233%20OR%20SRR5799234%20OR%20SRR5799235%20OR%20SRR5799236%20OR%20SRR5799237) |

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
