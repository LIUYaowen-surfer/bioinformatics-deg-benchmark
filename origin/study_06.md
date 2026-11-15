# study_06 - curator only

INSR shRNA vs scramble; human CHB8 embryonic stem cells. Selected samples: 2 treated / 2 control.

- Paper: Teo et al. (2021), [Defective insulin receptor signaling in hPSCs skews pluripotency and negatively perturbs neural differentiation](https://doi.org/10.1016/j.jbc.2021.100495).
- DOI: [10.1016/j.jbc.2021.100495](https://doi.org/10.1016/j.jbc.2021.100495); [PubMed 33667549](https://pubmed.ncbi.nlm.nih.gov/33667549/).
- GEO: [GSE60328](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60328).
- SRA: [PRJNA258044](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA258044); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR1544446%20OR%20SRR1544447) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR1544444%20OR%20SRR1544445).
- Author DEG reference: [GSE60328_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60328/suppl/GSE60328_gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Two biological replicates per group. Preserve the versioned Ensembl gene IDs. This is the undifferentiated hESC RNA-seq experiment, not the paper's complete neural differentiation phenotype.

Direction: Reference labels `Scr_KD` and `IR_KD` indicate IR knockdown/control in sample_2/sample_1 order.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM1471694](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471694) | INSR shRNA | SRR1544446 |
| [GSM1471695](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471695) | INSR shRNA | SRR1544447 |
| [GSM1471692](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471692) | scramble shRNA | SRR1544444 |
| [GSM1471693](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1471693) | scramble shRNA | SRR1544445 |

Checked 2026-11-15. Complete author result file downloaded for inspection (1,792,409 bytes). SHA-256: `6d520c57a947f2f8019b31fa76af7617e458d6b49adce49315920c66811b2355`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
