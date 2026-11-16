# task_13 — research and reference notes

**Selected comparison: old, 26-31 months vs adult, 5.5-8.5 months.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Old vs adult zebrafish brain-derived progenitor-enriched cultures. Selected samples: 3 treated / 3 control.

- Task: [task_13](../task_13/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Erbaba et al. (2020), [Zebrafish brain RNA sequencing reveals that cell adhesion molecules are critical in brain aging](https://doi.org/10.1016/j.neurobiolaging.2020.04.017).
- DOI: [10.1016/j.neurobiolaging.2020.04.017](https://doi.org/10.1016/j.neurobiolaging.2020.04.017); [PubMed 32629311](https://pubmed.ncbi.nlm.nih.gov/32629311/).
- GEO: [GSE133436](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133436).
- SRA: [PRJNA551453](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA551453); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR9608464%20OR%20SRR9608466%20OR%20SRR9608467%20OR%20SRR9608470%20OR%20SRR9608471) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR9608465%20OR%20SRR9608468%20OR%20SRR9608469%20OR%20SRR9608472%20OR%20SRR9608473).
- Paper copy: [institutional repository](https://repository.bilkent.edu.tr/bitstreams/8636fd66-1b67-46e4-91b6-ac0e3606773a/download).
- Author DEG reference: [GSE133436_gene_exp_oldYoung_.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE133436&format=file&file=GSE133436_gene_exp_oldYoung_.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Three independent pools per group, five brains per pool. GEO Young1-3 are adult (5.5-8.5 months); VeryYoung1-3 are 3 months. The checked oldYoung result matches the selected old/adult samples. The previously listed oldMid table corresponds to a different comparison and is not used. Preserve XLOC IDs and the matching RNAoldyoung merged annotation.

Direction: Flip the author log2FC sign to treated/control.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM3908617](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908617) | old, 26-31 months | SRR9608464 |
| [GSM3908619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908619) | old, 26-31 months | SRR9608466, SRR9608467 |
| [GSM3908621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908621) | old, 26-31 months | SRR9608470, SRR9608471 |
| [GSM3908618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908618) | adult, 5.5-8.5 months | SRR9608465 |
| [GSM3908620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908620) | adult, 5.5-8.5 months | SRR9608468, SRR9608469 |
| [GSM3908622](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908622) | adult, 5.5-8.5 months | SRR9608472, SRR9608473 |

Checked 2026-11-15. Complete reference-file SHA-256: `103719a4a6dcc7a151be67f5e2150accafa22f189c184b1be0a1d506ff67cf5a`.
Eligible distinct IDs: up=9,065, down=6,122. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_10`; previous task: `task_013`.
- Previous reference filename: `GSE133436_gene_exp_oldYoung_.diff__old_vs_adult_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_10/author_results/GSE133436_gene_exp_oldYoung_.diff.gz`.
- Extraction columns: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`; `status` = `OK`.
- Existing extraction direction multiplier: reversed (-1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `103719a4a6dcc7a151be67f5e2150accafa22f189c184b1be0a1d506ff67cf5a`.
- Migrated JSON SHA-256: `51ae31589a81eddb8cd23d15391510931b8bf725b313149a0f55b611a8ca42b2`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
