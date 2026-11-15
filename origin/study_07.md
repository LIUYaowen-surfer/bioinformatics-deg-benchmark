# study_07 - curator only

AM580 vs DMSO at day 6; human EB-derived HSPCs on OP9. Selected samples: 2 treated / 2 control.

- Paper: Dou et al. (2016), [Medial HOXA genes demarcate haematopoietic stem cell fate during human development](https://doi.org/10.1038/ncb3354).
- DOI: [10.1038/ncb3354](https://doi.org/10.1038/ncb3354); [PubMed 27183470](https://pubmed.ncbi.nlm.nih.gov/27183470/).
- GEO: [GSE76682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76682).
- SRA: [PRJNA308426](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA308426); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR3095977%20OR%20SRR3095978) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR3095975%20OR%20SRR3095976).
- Author DEG reference: [GSE76682_EB_AM580gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE76nnn/GSE76682/suppl/GSE76682_EB_AM580gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

GEO sample titles explicitly identify control as q1 and AM580 as q3. Keep experiments 1 and 2 identifiable. The 78,704,528-byte compressed reference contains multiple comparisons and assembled XLOC IDs. Only its header/initial rows were read; the q1/q3 row block still needs to be isolated and checked.

Direction: Desired direction is q3/q1. The inspected initial block is q1/q2, so no extraction configuration or sign flip is finalized.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2035710](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035710) | AM580, day 6 | SRR3095977 |
| [GSM2035711](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035711) | AM580, day 6 | SRR3095978 |
| [GSM2035708](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035708) | DMSO, day 6 | SRR3095975 |
| [GSM2035709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035709) | DMSO, day 6 | SRR3095976 |

Checked 2026-11-15. Only the header and initial rows were inspected; the complete file has not been verified.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
