# study_19 - curator only

Conditional Sox10 knockout vs control; mouse corpus callosum, dpi21. Selected samples: 4 treated / 4 control.

- Paper: Jörg et al. (2024), [Transcription Factors Sox8 and Sox10 Contribute with Different Importance to the Maintenance of Mature Oligodendrocytes](https://doi.org/10.3390/ijms25168754).
- DOI: [10.3390/ijms25168754](https://doi.org/10.3390/ijms25168754); [PubMed 39201442](https://pubmed.ncbi.nlm.nih.gov/39201442/).
- GEO: [GSE269122](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269122).
- SRA: [PRJNA1120355](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1120355); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR29290890%20OR%20SRR29290891%20OR%20SRR29290892%20OR%20SRR29290893) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR29290898%20OR%20SRR29290899%20OR%20SRR29290900%20OR%20SRR29290901).
- Author DEG reference: [GSE269122_ctrl_vs_Sox10ko.xlsx](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE269nnn/GSE269122/suppl/GSE269122_ctrl_vs_Sox10ko.xlsx).
- Result fields: Sheet `Rohdaten`: `GeneID`, `log2(FC)`, `padj`.

Four samples per group. Exclude Sox8 knockout and double-knockout samples. The workbook includes both p-value and padj: use padj for ranking even where the paper's figures discuss raw-P thresholds. Preserve Ensembl gene IDs.

Direction: The sheet lacks an explicit coefficient label. Resolve KO/control direction before extracting an answer.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM8306669](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306669) | Sox10 conditional KO | SRR29290893 |
| [GSM8306670](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306670) | Sox10 conditional KO | SRR29290892 |
| [GSM8306671](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306671) | Sox10 conditional KO | SRR29290891 |
| [GSM8306672](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306672) | Sox10 conditional KO | SRR29290890 |
| [GSM8306661](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306661) | control | SRR29290901 |
| [GSM8306662](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306662) | control | SRR29290900 |
| [GSM8306663](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306663) | control | SRR29290899 |
| [GSM8306664](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8306664) | control | SRR29290898 |

Checked 2026-11-15. Complete author result file downloaded for inspection (2,266,456 bytes). SHA-256: `61b8668cb0b36764cf20d494c307af5d0265526c62a9e04a342c78196179572b`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
