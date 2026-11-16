# Curator-only preparation

The [20-paper catalogue](study_catalog.md) provides 23 configured tasks and reference JSONs. See [downloads](downloads.md) for the selected raw archives and [curation notes](literature_screening.md) for source issues.

1. Download the two groups using the selected task's `treated` and `untreated` links. Keep the original downloads and this source mapping outside the test environment.
2. Prepare full-quality raw FASTQ copies in a separate folder for each task. Use `treated`/`untreated` filenames and anonymous sample identifiers, retaining donor pairing where applicable. Follow the study page's run-to-sample mapping; multiple sequencing runs are not extra biological replicates. Do not trim, filter, align, or count reads during preparation.
3. Replace source-bearing FASTQ identifiers and descriptions with unique anonymous read IDs, including identifiers on `+` lines. Preserve all sequences, quality scores, records, order, and mate relationships. Renaming a downloaded file alone is insufficient: default [SRA Toolkit FASTQ headers](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump) contain accessions. Check filenames, directories, headers, and compressed-file metadata for source identifiers.
4. Remove the download links from the task copy before placing its short prompt and prepared FASTQ files in a fresh offline workspace, with local reference resources and software installation packages. Exclude this repository, Git history, source archives, download logs, papers, and reference results. Use the papers and author DEG tables only for evaluation outside that workspace.

`treated` and `untreated` are benchmark aliases for the experimental and comparator groups. Depending on the study, `untreated` means untreated, vehicle control, wild type, or control siRNA; the actual conditions remain documented in the study pages. Reference-answer direction is `treated / untreated`.

These are raw-data preparation instructions, not a claim that the FASTQ files have already been downloaded or anonymized. The widely used airway study is particularly exposed in teaching materials; anonymization does not eliminate prior-data exposure.

Each study uses the same folder layout:

```text
origin/study_01/
├── README.md
└── reference/
    └── <comparison>_top100.json
```

Shared scripts, the catalogue and extraction log stay directly under `origin/`.

## Reference answers

[extract_reference.py](extract_reference.py) extracts existing author results using Python's standard library. Seven original file configurations are built in; [reference_configs.json](reference_configs.json) adds the 16 new comparisons. All 23 JSONs were checked against their author tables; the original seven answers remain byte-identical. See the [extraction record](extraction_log.md).

| Task | Comparison | Reference JSON |
|---|---|---|
| `task_001` | Dexamethasone vs untreated | [Top 100](study_01/reference/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json) |
| `task_002` | Lrpprc knockout vs wild type | [Top 100](study_02/reference/GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json) |
| `task_003` | SMC: TNF-α vs control | [Top 100](study_03/reference/GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json) |
| `task_004` | SMC: IL-1β vs control | [Top 100](study_03/reference/GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json) |
| `task_005` | EC: TNF-α vs control | [Top 100](study_03/reference/GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json) |
| `task_006` | EC: IL-1β vs control | [Top 100](study_03/reference/GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json) |
| `task_007` | siSRSF1 vs control siRNA | [Top 100](study_04/reference/GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json) |
| `task_008` | HOXA1 knockdown vs scramble | [Top 100](study_05/reference/GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json) |
| `task_009` | INSR shRNA vs scramble shRNA | [Top 100](study_06/reference/GSE60328_gene_exp.diff__INSR_KD_vs_scramble_top100.json) |
| `task_010` | AM580, day 6 vs DMSO, day 6 | [Top 100](study_07/reference/GSE76682_EB_AM580gene_exp.diff__AM580_vs_DMSO_day6_top100.json) |
| `task_011` | set2 deletion vs wild type | [Top 100](study_08/reference/GSE89238_SET2_KO_DESeq2_output__set2_KO_vs_WT_top100.json) |
| `task_012` | cord-blood-derived vs adult-bone-marrow-derived | [Top 100](study_09/reference/GSE100077_DifferentialExpression__cord_blood_vs_adult_top100.json) |
| `task_013` | old, 26-31 months vs adult, 5.5-8.5 months | [Top 100](study_10/reference/GSE133436_gene_exp_oldYoung_.diff__old_vs_adult_top100.json) |
| `task_014` | Tcf1/Lef1 deficient vs wild type | [Top 100](study_11/reference/GSE164712_gene_exp.diff__Tcf1_Lef1_DKO_vs_WT_top100.json) |
| `task_015` | mfl1 (GEO label) vs Col-0 | [Top 100](study_12/reference/GSE193247_gene_exp.diff__mfl1_vs_Col0_top100.json) |
| `task_016` | Mut.1, day-15 neurons vs WT, day-15 neurons | [Top 100](study_13/reference/GSE207163_RNA-seq__Top1_Mut1_vs_WT_day15_top100.json) |
| `task_017` | bam mutant + Mei-P26 RNAi vs bam mutant | [Top 100](study_14/reference/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26__MeiP26_KD_vs_bam_top100.json) |
| `task_018` | Suz12 full KO vs WT | [Top 100](study_15/reference/GSE223666_CTRL_SUZ12KO_stats_paired__Suz12_KO_vs_WT_ESC_top100.json) |
| `task_019` | Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+ | [Top 100](study_16/reference/GSE230334_gene_exp.diff__Lonp1_KO_vs_control_top100.json) |
| `task_020` | siOGT vs control siRNA | [Top 100](study_17/reference/GSE243105_sign_siOGT_control_genes_with_Batch_all__siOGT_vs_siControl_top100.json) |
| `task_021` | Sun1 KO tumors vs control tumors | [Top 100](study_18/reference/GSE250602_DESeq2_CT26_tumors_Control_vs_KO__Sun1_KO_vs_control_tumors_top100.json) |
| `task_022` | Sox10 conditional KO vs control | [Top 100](study_19/reference/GSE269122_ctrl_vs_Sox10ko__Sox10_KO_vs_control_top100.json) |
| `task_023` | 0.7 mM hydrogel vs unembedded 96-well control | [Top 100](study_20/reference/GSE288157_DESeq2_summary__hydrogel_0p7mM_vs_unembedded_top100.json) |

Each JSON contains only `up` and `down`, with 100 unique, non-overlapping gene IDs per direction. Direction is treatment/control; the airway, old/adult zebrafish and Sun1 tumor signs are reversed during extraction. Eligible genes are ranked by adjusted P value, then the original gene ID string. No additional significance or fold-change threshold is applied. Original IDs are preserved.

To reproduce, retain the original seven files at the input root and place each added file under `study_XX/author_results/`, as specified in reference_configs.json. Then run from the repository root:

```sh
python origin/extract_reference.py --config origin/reference_configs.json --input-dir "<local-author-results-folder>" --output-dir origin
```

For a different K, add `--k 50` and choose a new output folder, such as `--output-dir reference_output_top50`. Input hashes are checked against the reviewed files. Keep the script, source tables, answers, and extraction record outside the model's test environment.

Two files contain reviewed duplicate IDs. All source rows remain in ranking; none of those ambiguous IDs enters top100. The script blocks a larger K if it would include one. No first-row selection, ID conversion or silent repair is performed.
