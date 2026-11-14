# study_03 — curator only

TNF-α or IL-1β vs vehicle control in human aortic smooth muscle cells (SMCs) and endothelial cells (ECs); 4 contrasts, 6 samples per contrast, 18 unique samples.

- Paper: Pan et al. (2018), [Analysis of Combined Transcriptomes Identifies Gene Modules that Differentially Respond to Pathogenic Stimulation of Vascular Smooth Muscle and Endothelial Cells](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762668/).
- DOI: [10.1038/s41598-017-18675-2](https://doi.org/10.1038/s41598-017-18675-2).
- GEO: [GSE96962](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96962).
- SRA: [SRP102361](https://www.ncbi.nlm.nih.gov/sra?term=SRP102361).

| Comparison | Author DEG results |
|---|---|
| SMC: TNF-α vs control | [Results](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC--TNF-normalized-gene_exp.diff.gz) |
| SMC: IL-1β vs control | [Results](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC-IL-normalized-gene_exp.diff.gz) |
| EC: TNF-α vs control | [Results](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-TNF-normalized-gene_exp.diff.gz) |
| EC: IL-1β vs control | [Results](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-IL-normalized-gene_exp.diff.gz) |

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_003` | SMC: TNF-α vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368422%20OR%20SRR5368423%20OR%20SRR5368424%20OR%20SRR5368425%20OR%20SRR5368426%20OR%20SRR5368427) |
| `task_004` | SMC: IL-1β vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368422%20OR%20SRR5368423%20OR%20SRR5368424%20OR%20SRR5368428%20OR%20SRR5368429%20OR%20SRR5368430) |
| `task_005` | EC: TNF-α vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368413%20OR%20SRR5368414%20OR%20SRR5368415%20OR%20SRR5368416%20OR%20SRR5368417%20OR%20SRR5368418) |
| `task_006` | EC: IL-1β vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368413%20OR%20SRR5368414%20OR%20SRR5368415%20OR%20SRR5368419%20OR%20SRR5368420%20OR%20SRR5368421) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `.fastq.gz` for single-end reads.
Sample numbers are anonymous identifiers, not pairing labels.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR5368413` | `untreated_sample01` |
| `SRR5368414` | `untreated_sample02` |
| `SRR5368415` | `untreated_sample03` |
| `SRR5368416` | `treated_sample04` |
| `SRR5368417` | `treated_sample05` |
| `SRR5368418` | `treated_sample06` |
| `SRR5368419` | `treated_sample07` |
| `SRR5368420` | `treated_sample08` |
| `SRR5368421` | `treated_sample09` |
| `SRR5368422` | `untreated_sample10` |
| `SRR5368423` | `untreated_sample11` |
| `SRR5368424` | `untreated_sample12` |
| `SRR5368425` | `treated_sample13` |
| `SRR5368426` | `treated_sample14` |
| `SRR5368427` | `treated_sample15` |
| `SRR5368428` | `treated_sample16` |
| `SRR5368429` | `treated_sample17` |
| `SRR5368430` | `treated_sample18` |
