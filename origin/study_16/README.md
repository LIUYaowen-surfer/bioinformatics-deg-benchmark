# study_16 - curator only

Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+; E13.5 whole mouse lungs. Selected samples: 4 treated / 3 control.

- Task: [task_019](../../task/task_019.md).
- Reference: [top100 JSON](reference/GSE230334_gene_exp.diff__Lonp1_KO_vs_control_top100.json).
- Paper: Xu et al. (2025), [Mitochondrial Lon Peptidase 1 Controls Diaphragm and Lung Development in a Context-Dependent Manner](https://doi.org/10.70322/jrbtm.2025.10008).
- DOI: [10.70322/jrbtm.2025.10008](https://doi.org/10.70322/jrbtm.2025.10008); [PubMed 41049046](https://pubmed.ncbi.nlm.nih.gov/41049046/).
- GEO: [GSE230334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230334).
- SRA: [PRJNA958384](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA958384); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR24258427%20OR%20SRR24258428%20OR%20SRR24258429%20OR%20SRR24258430) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR24258431%20OR%20SRR24258432%20OR%20SRR24258433).
- Author DEG reference: [GSE230334_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE230334&format=file&file=GSE230334_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Four mutant and three control bulk RNA-seq lung samples. Exclude adult single-cell/influenza experiments. The paper Figure 4A directions for 11 named genes identify q1 as control and q2 as mutant.

Direction: Keep the author log2FC sign (treated/control). Evidence is recorded in the [extraction record](../extraction_log.md).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM7214002](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214002) | Shhcre;Lonp1f/f | SRR24258430 |
| [GSM7214003](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214003) | Shhcre;Lonp1f/f | SRR24258429 |
| [GSM7214004](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214004) | Shhcre;Lonp1f/f | SRR24258428 |
| [GSM7214005](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214005) | Shhcre;Lonp1f/f | SRR24258427 |
| [GSM7213999](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7213999) | Shhcre;Lonp1f/+ | SRR24258433 |
| [GSM7214000](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214000) | Shhcre;Lonp1f/+ | SRR24258432 |
| [GSM7214001](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214001) | Shhcre;Lonp1f/+ | SRR24258431 |

Checked 2026-11-15. Complete reference-file SHA-256: `f7d33e90b0e1bedb27b0d3814c48a4c13264bbe0a9aaec82b6f7c8d5db7b090e`.
Eligible distinct IDs: up=7,601, down=7,851. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
