# task_20 — research and reference notes

**Selected comparison: siOGT vs control siRNA.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

siOGT vs control siRNA; human LX-2 cells, 20 nM for 72 h. Selected samples: 3 treated / 3 control.

- Task: [task_20](../task_20/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Very et al. (2024), [O-GlcNAcylation controls pro-fibrotic transcriptional regulatory signaling in myofibroblasts](https://doi.org/10.1038/s41419-024-06773-9).
- DOI: [10.1038/s41419-024-06773-9](https://doi.org/10.1038/s41419-024-06773-9); [PubMed 38830870](https://pubmed.ncbi.nlm.nih.gov/38830870/).
- GEO: [GSE243105](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243105).
- SRA: [PRJNA1016370](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1016370); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26053372%20OR%20SRR26053373%20OR%20SRR26053374) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26053375%20OR%20SRR26053376%20OR%20SRR26053377).
- Author DEG reference: [GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE243105&format=file&file=GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz).
- Result fields: ID `__rowname__`, log2FC `log2FoldChange`, adjusted P `padj`.

Three paired independent experiments. Preserve the replicate pairing/batch. Despite sign in the filename, the author file contains nonsignificant rows; no additional significance filter is applied.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM7779398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779398) | siOGT | SRR26053374 |
| [GSM7779399](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779399) | siOGT | SRR26053373 |
| [GSM7779400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779400) | siOGT | SRR26053372 |
| [GSM7779395](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779395) | control siRNA | SRR26053377 |
| [GSM7779396](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779396) | control siRNA | SRR26053376 |
| [GSM7779397](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779397) | control siRNA | SRR26053375 |

Checked 2026-11-15. Complete reference-file SHA-256: `776b74bb701d48ecaf6e1e715b96859f6ab68c31e7b274d9d121b7267aba27d5`.
Eligible distinct IDs: up=6,255, down=6,294. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
