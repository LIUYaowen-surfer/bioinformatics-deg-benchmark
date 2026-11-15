# study_14 - curator only

Mei-P26 RNAi vs control in bam-mutant Drosophila ovaries. Selected samples: 2 treated / 2 control.

- Paper: Gui et al. (2023), [Simultaneous activation of Tor and suppression of ribosome biogenesis by TRIM-NHL proteins promotes terminal differentiation](https://doi.org/10.1016/j.celrep.2023.112181).
- DOI: [10.1016/j.celrep.2023.112181](https://doi.org/10.1016/j.celrep.2023.112181); [PubMed 36870055](https://pubmed.ncbi.nlm.nih.gov/36870055/).
- GEO: [GSE218205](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218205).
- SRA: [PRJNA902740](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA902740); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26619845%20OR%20SRR26619846) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26619841%20OR%20SRR26619842).
- Author DEG reference: [GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE218nnn/GSE218205/suppl/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Two biological pools per group, each containing 120 ovary pairs; individual ovaries are not separate replicates. Exclude the Mei-P26 overexpression samples and the separate overexpression comparison.

Direction: Reference labels bam and bam_KD_meiP26 indicate knockdown/control in sample_2/sample_1 order.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6736623](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736623) | bam mutant + Mei-P26 RNAi | SRR26619845 |
| [GSM6736624](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736624) | bam mutant + Mei-P26 RNAi | SRR26619846 |
| [GSM6736619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736619) | bam mutant | SRR26619841 |
| [GSM6736620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736620) | bam mutant | SRR26619842 |

Checked 2026-11-15. Complete author result file downloaded for inspection (577,523 bytes). SHA-256: `7a056b984b2d5e5e01a42ae2e760d547fe3423bdc634ce275f4b28b1dd299e3c`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
