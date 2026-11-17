# task_03 — research and reference notes

**Selected comparison: SMC: TNF-α vs control.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

This task contains only the comparison named above (3 treated / 3 untreated samples). The full four-comparison study notes are retained below for traceability. Use only this task's two download groups; do not pool cells, stimuli, or comparisons. The four comparisons are [task_03](../task_03/README.md), [task_04](../task_04/README.md), [task_05](../task_05/README.md), and [task_06](../task_06/README.md); each has its own answer.

## Study documentation

TNF-α or IL-1β vs vehicle control in human aortic smooth muscle cells (SMCs) and endothelial cells (ECs); 4 contrasts, 6 samples per contrast, 18 unique samples.

- Reference answers: [reference/](reference/).
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
| `task_03` | SMC: TNF-α vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368422%20OR%20SRR5368423%20OR%20SRR5368424%20OR%20SRR5368425%20OR%20SRR5368426%20OR%20SRR5368427) |
| `task_04` | SMC: IL-1β vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368422%20OR%20SRR5368423%20OR%20SRR5368424%20OR%20SRR5368428%20OR%20SRR5368429%20OR%20SRR5368430) |
| `task_05` | EC: TNF-α vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368413%20OR%20SRR5368414%20OR%20SRR5368415%20OR%20SRR5368416%20OR%20SRR5368417%20OR%20SRR5368418) |
| `task_06` | EC: IL-1β vs control | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR5368413%20OR%20SRR5368414%20OR%20SRR5368415%20OR%20SRR5368419%20OR%20SRR5368420%20OR%20SRR5368421) |

Single-end RNA-seq.

| Group | SRA runs |
|---|---|
| treated | SRR5368425, SRR5368426, SRR5368427 |
| untreated | SRR5368422, SRR5368423, SRR5368424 |
