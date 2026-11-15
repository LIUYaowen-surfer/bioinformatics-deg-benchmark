# study_13 - curator only

Top1(R548Q) mutant clone 1 vs wild type; day-15 mESC-derived neurons. Selected samples: 2 treated / 2 control.

- Paper: Lau et al. (2023), [Transcriptional repression by a secondary DNA binding surface of DNA topoisomerase I safeguards against hypertranscription](https://doi.org/10.1038/s41467-023-42078-9).
- DOI: [10.1038/s41467-023-42078-9](https://doi.org/10.1038/s41467-023-42078-9); [PubMed 37833256](https://pubmed.ncbi.nlm.nih.gov/37833256/).
- GEO: [GSE207163](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207163).
- SRA: [PRJNA854061](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA854061); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR19900767%20OR%20SRR19900768) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR19900797%20OR%20SRR19900798).
- Author DEG reference: [GSE207163_RNA-seq.xlsx](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE207nnn/GSE207163/suppl/GSE207163_RNA-seq.xlsx).
- Result fields: Sheet `neuron.Mut.1vsWT_day15`: `gene`, `log2FoldChange`, `padj`.

Two samples per group. Restrict this choice to the neuron worksheet; the workbook also contains mutant clone 2 and spike-in-normalized mESC/293T comparisons. The paper describes default DESeq2 analysis for neurons, unlike its ERCC-normalized comparisons.

Direction: The worksheet explicitly labels Mut.1vsWT; desired direction is mutant/wild type. Verify the coefficient sign during extraction.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6280719](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280719) | Mut.1, day-15 neurons | SRR19900768 |
| [GSM6280720](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280720) | Mut.1, day-15 neurons | SRR19900767 |
| [GSM6280723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280723) | WT, day-15 neurons | SRR19900798 |
| [GSM6280724](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6280724) | WT, day-15 neurons | SRR19900797 |

Checked 2026-11-15. Complete author result file downloaded for inspection (17,500,220 bytes). SHA-256: `42d2b2b2b351ee256355d12feef0327abfecd3b81bb716a77f6e2ff57919203e`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
