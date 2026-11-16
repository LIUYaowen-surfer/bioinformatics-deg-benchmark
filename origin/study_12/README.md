# study_12 - curator only

GEO-labeled mfl1 mutant vs Col-0; Arabidopsis seedlings, conventional RNA-seq. Selected samples: 3 treated / 3 control.

- Task: [task_015](../../task/task_015.md).
- Reference: [top100 JSON](reference/GSE193247_gene_exp.diff__mfl1_vs_Col0_top100.json).
- Paper: Nagarajan et al. (2023), [RNA degradome analysis reveals DNE1 endoribonuclease is required for the turnover of diverse mRNA substrates in Arabidopsis](https://doi.org/10.1093/plcell/koad085).
- DOI: [10.1093/plcell/koad085](https://doi.org/10.1093/plcell/koad085); [PubMed 37070465](https://pubmed.ncbi.nlm.nih.gov/37070465/).
- GEO: [GSE193247](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193247).
- SRA: [PRJNA795486](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA795486); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR17487765%20OR%20SRR17487769%20OR%20SRR17487773) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR17487766%20OR%20SRR17487770%20OR%20SRR17487774).
- Author DEG reference: [GSE193247_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE193247&format=file&file=GSE193247_gene_exp.diff.gz).
- Result fields: ID `gene_id`, log2FC `log2(fold_change)`, adjusted P `q_value`, status `status`.

Use the six conventional RNA-seq samples only, excluding PARE and GMUCT libraries. The deposited genotype label mfl1 is preserved in the task mapping and result comparison; it is not silently renamed.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM5777309](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777309) | mfl1 (GEO label) | SRR17487773 |
| [GSM5777313](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777313) | mfl1 (GEO label) | SRR17487769 |
| [GSM5777317](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777317) | mfl1 (GEO label) | SRR17487765 |
| [GSM5777308](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777308) | Col-0 | SRR17487774 |
| [GSM5777312](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777312) | Col-0 | SRR17487770 |
| [GSM5777316](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5777316) | Col-0 | SRR17487766 |

Checked 2026-11-15. Complete reference-file SHA-256: `cb03676ee7a06168098252f417ed2631778a70f3daad04d2bcc1572d17b32fed`.
Eligible distinct IDs: up=11,644, down=11,211. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
