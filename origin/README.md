# Curator-only preparation

1. Download only the runs listed for the selected task. Keep the original downloads and this source mapping outside the test environment.
2. Prepare full-quality raw FASTQ copies and use the anonymous filename prefixes in the study page. These names retain condition labels and, where applicable, donor pairing. Do not trim, filter, align, or count reads during preparation.
3. Replace source-bearing FASTQ identifiers and descriptions with unique anonymous read IDs, including identifiers on `+` lines. Preserve all sequences, quality scores, records, order, and mate relationships. Renaming a downloaded file alone is insufficient: default [SRA Toolkit FASTQ headers](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump) contain accessions. Check filenames, directories, headers, and compressed-file metadata for source identifiers.
4. Place the selected prompt and prepared FASTQ files in a fresh offline workspace, with local reference resources and software installation packages. Exclude this repository, Git history, source archives, download logs, papers, and reference results. Use the papers and author DEG tables only for evaluation outside that workspace.

These are raw-data preparation instructions, not a claim that the FASTQ files have already been downloaded or anonymized. The widely used airway study is particularly exposed in teaching materials; anonymization does not eliminate prior-data exposure.

## Reference answers

[extract_reference.py](extract_reference.py) extracts the existing author DEG tables using explicit per-file settings and Python's standard library. It does not rerun DEG analysis. The seven JSONs and [extraction record](reference_json/extraction_log.md) are copied unchanged from the checked local outputs.

| Task | Comparison | Reference JSON |
|---|---|---|
| `task_001` | Dexamethasone vs untreated | [Top 100](reference_json/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json) |
| `task_002` | Lrpprc knockout vs wild type | [Top 100](reference_json/GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json) |
| `task_003` | SMC: TNF-α vs control | [Top 100](reference_json/GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json) |
| `task_004` | SMC: IL-1β vs control | [Top 100](reference_json/GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json) |
| `task_005` | EC: TNF-α vs control | [Top 100](reference_json/GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json) |
| `task_006` | EC: IL-1β vs control | [Top 100](reference_json/GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json) |
| `task_007` | siSRSF1 vs control siRNA | [Top 100](reference_json/GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json) |

Each JSON contains only `up` and `down`, with 100 unique, non-overlapping gene IDs per direction. Direction is treatment/control; the airway log2FC sign is reversed during extraction. Eligible genes are ranked by adjusted P value, then the original gene ID string. No additional significance or fold-change threshold is applied. Original IDs are preserved.

To reproduce, download the seven author result archives linked in the study pages into a local folder, retaining their filenames, then run from the repository root:

```sh
python origin/extract_reference.py --input-dir "<local-author-results-folder>" --output-dir origin/reference_json
```

For a different K, add `--k 50` and choose a new output folder, such as `--output-dir origin/reference_json_top50`. Input hashes are checked against the reviewed files. Keep the script, source tables, answers, and extraction record outside the model's test environment.
