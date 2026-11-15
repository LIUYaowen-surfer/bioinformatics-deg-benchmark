# study_11 - curator only

Tcf1/Lef1 double knockout vs wild type; naive mouse CD8 T cells. Selected samples: 3 treated / 3 control.

- Paper: Shan et al. (2021), [Tcf1 and Lef1 provide constant supervision to mature CD8<sup>+</sup> T cell identity and function by organizing genomic architecture](https://doi.org/10.1038/s41467-021-26159-1).
- DOI: [10.1038/s41467-021-26159-1](https://doi.org/10.1038/s41467-021-26159-1); [PubMed 34615872](https://pubmed.ncbi.nlm.nih.gov/34615872/).
- GEO: [GSE164712](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164712).
- SRA: [PRJNA691621](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA691621); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR13423165%20OR%20SRR13423166%20OR%20SRR13423167) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR13423162%20OR%20SRR13423163%20OR%20SRR13423164).
- Author DEG reference: [GSE164712_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE164nnn/GSE164712/suppl/GSE164712_gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Three biological replicates per group. GEO has inconsistent mm9/mm10 processing statements; the linked 2021 paper describes mm9. Fix the reference genome before benchmarking. A later paper also cites this series; it is not counted as an additional independent dataset here.

Direction: Reference labels `WT_0h` and `DKO_0h` indicate double knockout/wild type in sample_2/sample_1 order.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM5017677](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017677) | Tcf1/Lef1 deficient | SRR13423165 |
| [GSM5017678](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017678) | Tcf1/Lef1 deficient | SRR13423166 |
| [GSM5017679](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017679) | Tcf1/Lef1 deficient | SRR13423167 |
| [GSM5017674](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017674) | wild type | SRR13423162 |
| [GSM5017675](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017675) | wild type | SRR13423163 |
| [GSM5017676](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017676) | wild type | SRR13423164 |

Checked 2026-11-15. Complete author result file downloaded for inspection (791,702 bytes). SHA-256: `40dce9716d3b414d69b183b4685dff9889ed347e3e089db9220627630fb10fc5`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
