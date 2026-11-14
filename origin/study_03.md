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
| `SRR5368413` | `EC_control_sample01` |
| `SRR5368414` | `EC_control_sample02` |
| `SRR5368415` | `EC_control_sample03` |
| `SRR5368416` | `EC_TNFa_sample04` |
| `SRR5368417` | `EC_TNFa_sample05` |
| `SRR5368418` | `EC_TNFa_sample06` |
| `SRR5368419` | `EC_IL1B_sample07` |
| `SRR5368420` | `EC_IL1B_sample08` |
| `SRR5368421` | `EC_IL1B_sample09` |
| `SRR5368422` | `SMC_control_sample10` |
| `SRR5368423` | `SMC_control_sample11` |
| `SRR5368424` | `SMC_control_sample12` |
| `SRR5368425` | `SMC_TNFa_sample13` |
| `SRR5368426` | `SMC_TNFa_sample14` |
| `SRR5368427` | `SMC_TNFa_sample15` |
| `SRR5368428` | `SMC_IL1B_sample16` |
| `SRR5368429` | `SMC_IL1B_sample17` |
| `SRR5368430` | `SMC_IL1B_sample18` |
