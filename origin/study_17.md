# study_17 - curator only

siOGT vs control siRNA; human LX-2 cells, 20 nM for 72 h. Selected samples: 3 treated / 3 control.

- Paper: Very et al. (2024), [O-GlcNAcylation controls pro-fibrotic transcriptional regulatory signaling in myofibroblasts](https://doi.org/10.1038/s41419-024-06773-9).
- DOI: [10.1038/s41419-024-06773-9](https://doi.org/10.1038/s41419-024-06773-9); [PubMed 38830870](https://pubmed.ncbi.nlm.nih.gov/38830870/).
- GEO: [GSE243105](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243105).
- SRA: [PRJNA1016370](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1016370); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26053372%20OR%20SRR26053373%20OR%20SRR26053374) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR26053375%20OR%20SRR26053376%20OR%20SRR26053377).
- Author DEG reference: [GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE243nnn/GSE243105/suppl/GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz).
- Result fields: Unnamed first column (gene ID/symbol), `log2FoldChange`, `padj`.

Three paired independent experiments; retain the experimental batch/pair information. Despite 'sign' in its filename, the result includes nonsignificant rows. Do not apply an extra significance filter when extracting ranked reference lists.

Direction: Desired direction is siOGT/control. Confirm the author model coefficient before finalizing extraction.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM7779398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779398) | siOGT | SRR26053374 |
| [GSM7779399](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779399) | siOGT | SRR26053373 |
| [GSM7779400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779400) | siOGT | SRR26053372 |
| [GSM7779395](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779395) | control siRNA | SRR26053377 |
| [GSM7779396](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779396) | control siRNA | SRR26053376 |
| [GSM7779397](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7779397) | control siRNA | SRR26053375 |

Checked 2026-11-15. Complete author result file downloaded for inspection (833,988 bytes). SHA-256: `776b74bb701d48ecaf6e1e715b96859f6ab68c31e7b274d9d121b7267aba27d5`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
