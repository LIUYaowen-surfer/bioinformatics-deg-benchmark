# study_14 - curator only

Mei-P26 RNAi vs control in bam-mutant Drosophila ovaries. Selected samples: 2 treated / 2 control.

- Task: [task_017](../../task/task_017.md).
- Reference: [top100 JSON](reference/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26__MeiP26_KD_vs_bam_top100.json).
- Paper: Gui et al. (2023), [Simultaneous activation of Tor and suppression of ribosome biogenesis by TRIM-NHL proteins promotes terminal differentiation](https://doi.org/10.1016/j.celrep.2023.112181).
- DOI: [10.1016/j.celrep.2023.112181](https://doi.org/10.1016/j.celrep.2023.112181); [PubMed 36870055](https://pubmed.ncbi.nlm.nih.gov/36870055/).
- GEO: [GSE218205](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218205).
- SRA: [PRJNA902740](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA902740); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26619845%20OR%20SRR26619846) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26619841%20OR%20SRR26619842).
- Author DEG reference: [GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE218205&format=file&file=GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Two biological pools per group, each containing 120 ovary pairs. Exclude overexpression samples. Two author tests share gene_id=Chd64 with opposite effects; they are both retained in ranking and both lie outside top100. Increasing K is blocked if that ID enters an answer.

Direction: Keep the author log2FC sign (treated/control). Evidence is recorded in the [extraction record](../extraction_log.md).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6736623](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736623) | bam mutant + Mei-P26 RNAi | SRR26619845 |
| [GSM6736624](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736624) | bam mutant + Mei-P26 RNAi | SRR26619846 |
| [GSM6736619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736619) | bam mutant | SRR26619841 |
| [GSM6736620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6736620) | bam mutant | SRR26619842 |

Checked 2026-11-15. Complete reference-file SHA-256: `7a056b984b2d5e5e01a42ae2e760d547fe3423bdc634ce275f4b28b1dd299e3c`.
Eligible distinct IDs: up=5,090, down=5,189. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
