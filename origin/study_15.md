# study_15 - curator only

Suz12 full knockout vs wild type; mouse embryonic stem cells. Selected samples: 3 treated / 3 control.

- Paper: Arecco et al. (2024), [Alternative splicing decouples local from global PRC2 activity](https://doi.org/10.1016/j.molcel.2024.02.011).
- DOI: [10.1016/j.molcel.2024.02.011](https://doi.org/10.1016/j.molcel.2024.02.011); [PubMed 38452766](https://pubmed.ncbi.nlm.nih.gov/38452766/).
- GEO: [GSE223666](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE223666).
- SRA: [PRJNA927240](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA927240); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR23215987%20OR%20SRR23215988%20OR%20SRR23215989) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR23215994%20OR%20SRR23215995%20OR%20SRR23215996).
- Author DEG reference: [GSE223666_A-2_WT_B-2_KO_stats_paired.txt.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE223nnn/GSE223666/suppl/GSE223666_A-2_WT_B-2_KO_stats_paired.txt.gz).
- Result fields: Unnamed leading gene-ID field (R row names), `log2FoldChange`, `padj`.

GEO overall design explicitly defines KO as Suz12 full knockout. Keep this comparison separate from isoform deletions, rescues, and neural differentiation. The result has one more field per row than the header (R row-name export). The paired-model/block specification and its relation to replicate labels need verification.

Direction: No explicit coefficient label inside the inspected rows; do not infer KO/WT from the filename alone.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM6970308](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970308) | Suz12 full KO | SRR23215989 |
| [GSM6970309](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970309) | Suz12 full KO | SRR23215988 |
| [GSM6970310](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970310) | Suz12 full KO | SRR23215987 |
| [GSM6970301](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970301) | WT | SRR23215996 |
| [GSM6970302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970302) | WT | SRR23215995 |
| [GSM6970303](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6970303) | WT | SRR23215994 |

Checked 2026-11-15. Only the header and initial rows were inspected; the complete file has not been verified.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
