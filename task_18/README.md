# task_18 — research and reference notes

**Selected comparison: Suz12 full KO vs WT.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Suz12 full knockout vs wild type; mouse embryonic stem cells. Selected samples: 3 treated / 3 control.

- Task: [task_18](../task_18/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Arecco et al. (2024), [Alternative splicing decouples local from global PRC2 activity](https://doi.org/10.1016/j.molcel.2024.02.011).
- DOI: [10.1016/j.molcel.2024.02.011](https://doi.org/10.1016/j.molcel.2024.02.011); [PubMed 38452766](https://pubmed.ncbi.nlm.nih.gov/38452766/).
- GEO: [GSE223666](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE223666).
- SRA: [PRJNA927240](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA927240); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR23215987%20OR%20SRR23215988%20OR%20SRR23215989) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR23215994%20OR%20SRR23215995%20OR%20SRR23215996).
- Author DEG reference: [GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE223666&format=file&file=GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz).
- Result fields: ID `__rowname__`, log2FC `log2FoldChange`, adjusted P `padj`.

Use CTRL_SUZ12KO_stats_paired.txt for these ESC samples. A-2_WT_B-2_KO is a neural-progenitor comparison with different samples and is not used. Keep the reported biological replicate/block identifiers available to the curator.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6970308](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970308) | Suz12 full KO | SRR23215989 |
| [GSM6970309](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970309) | Suz12 full KO | SRR23215988 |
| [GSM6970310](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970310) | Suz12 full KO | SRR23215987 |
| [GSM6970301](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970301) | WT | SRR23215996 |
| [GSM6970302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970302) | WT | SRR23215995 |
| [GSM6970303](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970303) | WT | SRR23215994 |

Checked 2026-11-15. Complete reference-file SHA-256: `885a1ffa50d8d1923b33cbc9d931f73c755121dd74114d2516c1fdc225285c36`.
Eligible distinct IDs: up=8,548, down=8,370. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
