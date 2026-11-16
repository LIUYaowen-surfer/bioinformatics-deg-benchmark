# study_07 - curator only

AM580 vs DMSO at day 6; human EB-derived HSPCs on OP9. Selected samples: 2 treated / 2 control.

- Task: [task_010](../../task/task_010.md).
- Reference: [top100 JSON](reference/GSE76682_EB_AM580gene_exp.diff__AM580_vs_DMSO_day6_top100.json).
- Paper: Dou et al. (2016), [Medial HOXA genes demarcate haematopoietic stem cell fate during human development](https://doi.org/10.1038/ncb3354).
- DOI: [10.1038/ncb3354](https://doi.org/10.1038/ncb3354); [PubMed 27183470](https://pubmed.ncbi.nlm.nih.gov/27183470/).
- GEO: [GSE76682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76682).
- SRA: [PRJNA308426](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA308426); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR3095977%20OR%20SRR3095978) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR3095975%20OR%20SRR3095976).
- Author DEG reference: [GSE76682_EB_AM580gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE76682&format=file&file=GSE76682_EB_AM580gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Keep experiments 1 and 2 identifiable. GEO explicitly maps DMSO to q1 and AM580 to q3. Only this block is ranked; other contrasts and the author XLOC identifiers are preserved in the source.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2035710](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035710) | AM580, day 6 | SRR3095977 |
| [GSM2035711](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035711) | AM580, day 6 | SRR3095978 |
| [GSM2035708](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035708) | DMSO, day 6 | SRR3095975 |
| [GSM2035709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2035709) | DMSO, day 6 | SRR3095976 |

Checked 2026-11-15. Complete reference-file SHA-256: `fc9c4e9cea5f137d6aa53b942f3bf0f894c54943864522da7818e28a52218ae3`.
Eligible distinct IDs: up=20,517, down=20,972. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
