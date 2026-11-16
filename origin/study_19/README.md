# study_19 - curator only

Conditional Sox10 knockout vs control; mouse corpus callosum, dpi21. Selected samples: 4 treated / 4 control.

- Task: [task_022](../../task/task_022.md).
- Reference: [top100 JSON](reference/GSE269122_ctrl_vs_Sox10ko__Sox10_KO_vs_control_top100.json).
- Paper: Jörg et al. (2024), [Transcription Factors Sox8 and Sox10 Contribute with Different Importance to the Maintenance of Mature Oligodendrocytes](https://doi.org/10.3390/ijms25168754).
- DOI: [10.3390/ijms25168754](https://doi.org/10.3390/ijms25168754); [PubMed 39201442](https://pubmed.ncbi.nlm.nih.gov/39201442/).
- GEO: [GSE269122](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269122).
- SRA: [PRJNA1120355](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1120355); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR29290890%20OR%20SRR29290891%20OR%20SRR29290892%20OR%20SRR29290893) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR29290898%20OR%20SRR29290899%20OR%20SRR29290900%20OR%20SRR29290901).
- Author DEG reference: [GSE269122_ctrl_vs_Sox10ko.xlsx](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE269122&format=file&file=GSE269122_ctrl_vs_Sox10ko.xlsx).
- Result fields: ID `GeneID`, log2FC `log2(FC)`, adjusted P `padj`; worksheet `Rohdaten`.

Four samples per group. Exclude Sox8-only and double-knockout samples. Use padj, not p-value, and preserve the Ensembl GeneID field.

Direction: Keep the author log2FC sign (treated/control).

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

Checked 2026-11-15. Complete reference-file SHA-256: `61b8668cb0b36764cf20d494c307af5d0265526c62a9e04a342c78196179572b`.
Eligible distinct IDs: up=12,236, down=11,949. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
