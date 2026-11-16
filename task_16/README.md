# task_16 — research and reference notes

**Selected comparison: Mut.1, day-15 neurons vs WT, day-15 neurons.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

Top1(R548Q) mutant clone 1 vs wild type; day-15 mESC-derived neurons. Selected samples: 2 treated / 2 control.

- Task: [task_16](../task_16/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Lau et al. (2023), [Transcriptional repression by a secondary DNA binding surface of DNA topoisomerase I safeguards against hypertranscription](https://doi.org/10.1038/s41467-023-42078-9).
- DOI: [10.1038/s41467-023-42078-9](https://doi.org/10.1038/s41467-023-42078-9); [PubMed 37833256](https://pubmed.ncbi.nlm.nih.gov/37833256/).
- GEO: [GSE207163](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207163).
- SRA: [PRJNA854061](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA854061); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR19900767%20OR%20SRR19900768) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR19900797%20OR%20SRR19900798).
- Author DEG reference: [GSE207163_RNA-seq.xlsx](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE207163&format=file&file=GSE207163_RNA-seq.xlsx).
- Result fields: ID `gene`, log2FC `log2FoldChange`, adjusted P `padj`; worksheet `neuron.Mut.1vsWT_day15`.

Use only the neuron.Mut.1vsWT_day15 worksheet and the four neuronal samples. The workbook contains date-formatted numeric gene cells with duplicate IDs; all remain in source ranking but lie outside top100. Increasing K is blocked if an ambiguous ID enters either list. No gene ID was repaired or converted.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6280719](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280719) | Mut.1, day-15 neurons | SRR19900768 |
| [GSM6280720](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280720) | Mut.1, day-15 neurons | SRR19900767 |
| [GSM6280723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280723) | WT, day-15 neurons | SRR19900798 |
| [GSM6280724](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280724) | WT, day-15 neurons | SRR19900797 |

Checked 2026-11-15. Complete reference-file SHA-256: `42d2b2b2b351ee256355d12feef0327abfecd3b81bb716a77f6e2ff57919203e`.
Eligible distinct IDs: up=8,417, down=8,169. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_13`; previous task: `task_016`.
- Previous reference filename: `GSE207163_RNA-seq__Top1_Mut1_vs_WT_day15_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_13/author_results/GSE207163_RNA-seq.xlsx`.
- Extraction columns: ID `gene`, log2FC `log2FoldChange`, adjusted P `padj`; no status column configured.
- Worksheet: `neuron.Mut.1vsWT_day15`.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `42d2b2b2b351ee256355d12feef0327abfecd3b81bb716a77f6e2ff57919203e`.
- Migrated JSON SHA-256: `05621d80de39fd113b0b6c41dded5cc7d883a38d364e03eb8f4029ea14623fba`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
