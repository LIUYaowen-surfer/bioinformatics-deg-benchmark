# study_06 - curator only

INSR shRNA vs scramble; human CHB8 embryonic stem cells. Selected samples: 2 treated / 2 control.

- Task: [task_009](../../task/task_009.md).
- Reference: [top100 JSON](reference/GSE60328_gene_exp.diff__INSR_KD_vs_scramble_top100.json).
- Paper: Teo et al. (2021), [Defective insulin receptor signaling in hPSCs skews pluripotency and negatively perturbs neural differentiation](https://doi.org/10.1016/j.jbc.2021.100495).
- DOI: [10.1016/j.jbc.2021.100495](https://doi.org/10.1016/j.jbc.2021.100495); [PubMed 33667549](https://pubmed.ncbi.nlm.nih.gov/33667549/).
- GEO: [GSE60328](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60328).
- SRA: [PRJNA258044](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA258044); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR1544446%20OR%20SRR1544447) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR1544444%20OR%20SRR1544445).
- Author DEG reference: [GSE60328_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE60328&format=file&file=GSE60328_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Two biological replicates per group. Preserve the versioned Ensembl IDs. One source FC magnitude is inconsistent with its displayed expression ratio; it is retained unchanged and documented in the extraction record.

Direction: Keep the author log2FC sign (treated/control). Evidence is recorded in the [extraction record](../extraction_log.md).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM1471694](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471694) | INSR shRNA | SRR1544446 |
| [GSM1471695](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471695) | INSR shRNA | SRR1544447 |
| [GSM1471692](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471692) | scramble shRNA | SRR1544444 |
| [GSM1471693](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471693) | scramble shRNA | SRR1544445 |

Checked 2026-11-15. Complete reference-file SHA-256: `6d520c57a947f2f8019b31fa76af7617e458d6b49adce49315920c66811b2355`.
Eligible distinct IDs: up=10,417, down=10,052. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
