# study_20 - curator only

0.7 mM dextran hydrogel embedding at 96 h vs no embedding; mouse gastruloids. Selected samples: 3 treated / 3 control.

- Task: [task_023](../task/task_023.md).
- Reference: [top100 JSON](reference_json/study_20/GSE288157_DESeq2_summary__hydrogel_0p7mM_vs_unembedded_top100.json).
- Paper: Pineau et al. (2025), [Fine-tuning mechanical constraints reveals uncoupled patterning and gene expression programs in murine gastruloids](https://doi.org/10.1242/dev.204711).
- DOI: [10.1242/dev.204711](https://doi.org/10.1242/dev.204711); [PubMed 41020403](https://pubmed.ncbi.nlm.nih.gov/41020403/).
- GEO: [GSE288157](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288157).
- SRA: [PRJNA1216293](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1216293); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR32145088%20OR%20SRR32145089%20OR%20SRR32145090) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR32145094%20OR%20SRR32145095%20OR%20SRR32145096).
- Author DEG reference: [GSE288157_DESeq2_summary.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE288157&format=file&file=GSE288157_DESeq2_summary.txt.gz).
- Result fields: ID `Ens_ID`, log2FC `Condition_Emb_0.7mMvs96wp_l2fc`, adjusted P `Condition_Emb_0.7mMvs96wp_padj`.

Three replicates per group. Only the 0.7 mM versus 96wp column pair is ranked. Author code at allRNAseqScriptsFromPineauWongNgEtAl2025 confirms the reference condition; the differently ordered repository name in GEO is a typo.

Direction: Keep the author log2FC sign (treated/control). Evidence is recorded in the [extraction record](reference_json/extraction_log.md).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM8760158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760158) | 0.7 mM hydrogel | SRR32145090 |
| [GSM8760159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760159) | 0.7 mM hydrogel | SRR32145089 |
| [GSM8760160](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760160) | 0.7 mM hydrogel | SRR32145088 |
| [GSM8760152](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760152) | unembedded 96-well control | SRR32145096 |
| [GSM8760153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760153) | unembedded 96-well control | SRR32145095 |
| [GSM8760154](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8760154) | unembedded 96-well control | SRR32145094 |

Checked 2026-11-15. Complete reference-file SHA-256: `46dd0af492844ab6cbdd9183bb5d42e47c77915c00c92273e7061932c7b7ff4e`.
Eligible distinct IDs: up=6,861, down=6,703. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.
