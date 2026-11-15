# study_20 - curator only

0.7 mM dextran hydrogel embedding at 96 h vs no embedding; mouse gastruloids. Selected samples: 3 treated / 3 control.

- Paper: Pineau et al. (2025), [Fine-tuning mechanical constraints reveals uncoupled patterning and gene expression programs in murine gastruloids](https://doi.org/10.1242/dev.204711).
- DOI: [10.1242/dev.204711](https://doi.org/10.1242/dev.204711); [PubMed 41020403](https://pubmed.ncbi.nlm.nih.gov/41020403/).
- GEO: [GSE288157](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288157).
- SRA: [PRJNA1216293](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1216293); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR32145088%20OR%20SRR32145089%20OR%20SRR32145090) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR32145094%20OR%20SRR32145095%20OR%20SRR32145096).
- Author DEG reference: [GSE288157_DESeq2_summary.txt.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE288nnn/GSE288157/suppl/GSE288157_DESeq2_summary.txt.gz).
- Result fields: `Ens_ID`, `Condition_Emb_0.7mMvs96wp_l2fc`, `Condition_Emb_0.7mMvs96wp_padj`.

Three replicates per group. The result stores multiple contrasts in separate column sets; exclude no-Chiron, 0.8 mM and 1.0 mM columns from this task. The paper's newly generated data are under GSE288158, including this subseries; GSE247508 is reused external data and is not substituted for it.

Direction: The column name explicitly labels embedding vs 96wp; desired direction is embedded/control. Check the coefficient convention during extraction.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM8760158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760158) | 0.7 mM hydrogel | SRR32145090 |
| [GSM8760159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760159) | 0.7 mM hydrogel | SRR32145089 |
| [GSM8760160](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760160) | 0.7 mM hydrogel | SRR32145088 |
| [GSM8760152](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760152) | unembedded 96-well control | SRR32145096 |
| [GSM8760153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760153) | unembedded 96-well control | SRR32145095 |
| [GSM8760154](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760154) | unembedded 96-well control | SRR32145094 |

Checked 2026-11-15. Only the header and initial rows were inspected; the complete file has not been verified.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
