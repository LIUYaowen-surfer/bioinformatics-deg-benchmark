# study_10 - curator only

Old vs adult zebrafish brain-derived progenitor-enriched cultures. Selected samples: 3 treated / 3 control.

- Paper: Erbaba et al. (2020), [Zebrafish brain RNA sequencing reveals that cell adhesion molecules are critical in brain aging](https://doi.org/10.1016/j.neurobiolaging.2020.04.017).
- DOI: [10.1016/j.neurobiolaging.2020.04.017](https://doi.org/10.1016/j.neurobiolaging.2020.04.017); [PubMed 32629311](https://pubmed.ncbi.nlm.nih.gov/32629311/).
- GEO: [GSE133436](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133436).
- SRA: [PRJNA551453](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA551453); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR9608464%20OR%20SRR9608466%20OR%20SRR9608467%20OR%20SRR9608470%20OR%20SRR9608471) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR9608465%20OR%20SRR9608468%20OR%20SRR9608469%20OR%20SRR9608472%20OR%20SRR9608473).
- Author DEG reference: [GSE133436_gene_exp_oldMid_.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE133436&format=file&file=GSE133436_gene_exp_oldMid_.diff.gz).
- Paper copy: [institutional repository](https://repository.bilkent.edu.tr/bitstreams/8636fd66-1b67-46e4-91b6-ac0e3606773a/download).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Three independent pools per age group, five brains per pool (paper Table 1). GEO calls the adult samples Young1-3 and the 3-month samples VeryYoung1-3. The oldMid reference is proposed for old/adult; oldYoung is a different age contrast. Confirm the file's mid-to-adult mapping before scoring. Preserve XLOC IDs and the matching assembled GTF; do not merge the three contrast files.

Direction: The file uses sample_1=old and sample_2=mid, so its FC is mid/old. Old/adult would require a sign flip once mid=adult is confirmed.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM3908617](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908617) | old, 26-31 months | SRR9608464 |
| [GSM3908619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908619) | old, 26-31 months | SRR9608466, SRR9608467 |
| [GSM3908621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908621) | old, 26-31 months | SRR9608470, SRR9608471 |
| [GSM3908618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908618) | adult, 5.5-8.5 months | SRR9608465 |
| [GSM3908620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908620) | adult, 5.5-8.5 months | SRR9608468, SRR9608469 |
| [GSM3908622](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3908622) | adult, 5.5-8.5 months | SRR9608472, SRR9608473 |

Checked 2026-11-15. Complete author result file downloaded for inspection (1,131,230 bytes). SHA-256: `672198b7833a8c230f86e4f61cbc1c3244dec7c35042d156ce78952302b1501f`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
