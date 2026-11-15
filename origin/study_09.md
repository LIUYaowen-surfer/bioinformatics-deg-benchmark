# study_09 - curator only

Cord-blood-derived vs adult-bone-marrow-derived human erythroid cells after xenograft. Selected samples: 3 treated / 3 control.

- Paper: Fiorini et al. (2017), [Developmentally-faithful and effective human erythropoiesis in immunodeficient and Kit mutant mice](https://doi.org/10.1002/ajh.24805).
- DOI: [10.1002/ajh.24805](https://doi.org/10.1002/ajh.24805); [PubMed 28568895](https://pubmed.ncbi.nlm.nih.gov/28568895/).
- GEO: [GSE100077](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100077).
- SRA: [PRJNA390632](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA390632); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR5687582%20OR%20SRR5687583%20OR%20SRR5687584) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR5687579%20OR%20SRR5687580%20OR%20SRR5687581).
- Author DEG reference: [GSE100077_DifferentialExpression.csv.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100077/suppl/GSE100077_DifferentialExpression.csv.gz).
- Result fields: `gene`, `logFC`, `adj.P.Val`.

Three xenograft recipients per source group; human CD235a+ cells were collected 14-16 weeks after transplantation. This compares developmental sources, not a drug treatment. Use adj.P.Val, not P.Value.

Direction: The table has no explicit numerator/denominator columns. The logFC coefficient direction remains to be confirmed.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2670892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670892) | cord-blood-derived | SRR5687582 |
| [GSM2670893](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670893) | cord-blood-derived | SRR5687583 |
| [GSM2670894](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670894) | cord-blood-derived | SRR5687584 |
| [GSM2670889](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670889) | adult-bone-marrow-derived | SRR5687579 |
| [GSM2670890](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670890) | adult-bone-marrow-derived | SRR5687580 |
| [GSM2670891](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2670891) | adult-bone-marrow-derived | SRR5687581 |

Checked 2026-11-15. Only the header and initial rows were inspected; the complete file has not been verified.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
