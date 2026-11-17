# task_14 — research and reference notes

**Selected comparison: Tcf1/Lef1 deficient vs wild type.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Tcf1/Lef1 double knockout vs wild type; naive mouse CD8 T cells. Selected samples: 3 treated / 3 control.

- Task: [task_14](../task_14/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Shan et al. (2021), [Tcf1 and Lef1 provide constant supervision to mature CD8<sup>+</sup> T cell identity and function by organizing genomic architecture](https://doi.org/10.1038/s41467-021-26159-1).
- DOI: [10.1038/s41467-021-26159-1](https://doi.org/10.1038/s41467-021-26159-1); [PubMed 34615872](https://pubmed.ncbi.nlm.nih.gov/34615872/).
- GEO: [GSE164712](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164712).
- SRA: [PRJNA691621](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA691621); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR13423165%20OR%20SRR13423166%20OR%20SRR13423167) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR13423162%20OR%20SRR13423163%20OR%20SRR13423164).
- Author DEG reference: [GSE164712_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE164712&format=file&file=GSE164712_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Three biological replicates per group. GEO contains inconsistent mm9/mm10 processing statements; the linked paper describes mm9. Fix the reference resources before an exact reproduction attempt.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM5017677](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017677) | Tcf1/Lef1 deficient | SRR13423165 |
| [GSM5017678](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017678) | Tcf1/Lef1 deficient | SRR13423166 |
| [GSM5017679](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017679) | Tcf1/Lef1 deficient | SRR13423167 |
| [GSM5017674](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017674) | wild type | SRR13423162 |
| [GSM5017675](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017675) | wild type | SRR13423163 |
| [GSM5017676](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5017676) | wild type | SRR13423164 |

Checked 2026-11-15. Complete reference-file SHA-256: `40dce9716d3b414d69b183b4685dff9889ed347e3e089db9220627630fb10fc5`.
Eligible distinct IDs: up=5,512, down=5,735. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
