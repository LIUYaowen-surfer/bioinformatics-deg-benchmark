# study_12 - curator only

GEO-labeled mfl1 mutant vs Col-0; Arabidopsis seedlings, conventional RNA-seq. Selected samples: 3 treated / 3 control.

- Paper: Nagarajan et al. (2023), [RNA degradome analysis reveals DNE1 endoribonuclease is required for the turnover of diverse mRNA substrates in Arabidopsis](https://doi.org/10.1093/plcell/koad085).
- DOI: [10.1093/plcell/koad085](https://doi.org/10.1093/plcell/koad085); [PubMed 37070465](https://pubmed.ncbi.nlm.nih.gov/37070465/).
- GEO: [GSE193247](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193247).
- SRA: [PRJNA795486](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA795486); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR17487765%20OR%20SRR17487769%20OR%20SRR17487773) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR17487766%20OR%20SRR17487770%20OR%20SRR17487774).
- Author DEG reference: [GSE193247_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE193nnn/GSE193247/suppl/GSE193247_gene_exp.diff.gz).
- Result fields: `gene_id`, `log2(fold_change)`, `q_value`, `status`.

Three replicates per group, with TAIR gene IDs. Select only conventional RNA-seq (ATH1046-57), not PARE or GMUCT degradome libraries from the same project. GEO uses mfl1 whereas the paper uses dne1; reconcile this nomenclature before formal scoring. The file contains several genotype contrasts.

Direction: Inspected rows show sample_1=Col0 and sample_2=mfl1, i.e. mfl1/Col0.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM5777309](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777309) | mfl1 (GEO label) | SRR17487773 |
| [GSM5777313](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777313) | mfl1 (GEO label) | SRR17487769 |
| [GSM5777317](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777317) | mfl1 (GEO label) | SRR17487765 |
| [GSM5777308](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777308) | Col-0 | SRR17487774 |
| [GSM5777312](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777312) | Col-0 | SRR17487770 |
| [GSM5777316](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777316) | Col-0 | SRR17487766 |

Checked 2026-11-15. Only the header and initial rows were inspected; the complete file has not been verified.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
