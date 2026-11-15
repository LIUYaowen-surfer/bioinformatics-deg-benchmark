# study_16 - curator only

Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+; E13.5 whole mouse lungs. Selected samples: 4 treated / 3 control.

- Paper: Xu et al. (2025), [Mitochondrial Lon Peptidase 1 Controls Diaphragm and Lung Development in a Context-Dependent Manner](https://doi.org/10.70322/jrbtm.2025.10008).
- DOI: [10.70322/jrbtm.2025.10008](https://doi.org/10.70322/jrbtm.2025.10008); [PubMed 41049046](https://pubmed.ncbi.nlm.nih.gov/41049046/).
- GEO: [GSE230334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230334).
- SRA: [PRJNA958384](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA958384); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR24258427%20OR%20SRR24258428%20OR%20SRR24258429%20OR%20SRR24258430) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR24258431%20OR%20SRR24258432%20OR%20SRR24258433).
- Author DEG reference: [GSE230334_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE230nnn/GSE230334/suppl/GSE230334_gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Four mutant and three control bulk RNA-seq samples. Exclude adult single-cell and influenza-related samples. The 2025 paper explicitly identifies GSE230334 for this bulk experiment; the other linked 2024 paper is not counted again. IDs are Ensembl mouse gene IDs.

Direction: The result uses q1/q2 without genotype names. Their group mapping and log2FC direction remain unresolved.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM7214002](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214002) | Shhcre;Lonp1f/f | SRR24258430 |
| [GSM7214003](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214003) | Shhcre;Lonp1f/f | SRR24258429 |
| [GSM7214004](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214004) | Shhcre;Lonp1f/f | SRR24258428 |
| [GSM7214005](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214005) | Shhcre;Lonp1f/f | SRR24258427 |
| [GSM7213999](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7213999) | Shhcre;Lonp1f/+ | SRR24258433 |
| [GSM7214000](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214000) | Shhcre;Lonp1f/+ | SRR24258432 |
| [GSM7214001](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7214001) | Shhcre;Lonp1f/+ | SRR24258431 |

Checked 2026-11-15. Complete author result file downloaded for inspection (1,137,779 bytes). SHA-256: `f7d33e90b0e1bedb27b0d3814c48a4c13264bbe0a9aaec82b6f7c8d5db7b090e`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
