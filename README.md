# Offline DEG Benchmark

Minimal prompts for testing whether an AI can set up its environment, use local tools, and find differentially expressed genes without internet access.

- `task/`: anonymous task IDs, a minimal treated-versus-untreated prompt, and separate data download links for each group. Experimental names are omitted from the task text.
- `origin/`: curator-only papers, download links, filename mappings, the extraction script, and 23 top-100 reference JSONs derived from author-provided DEG results.

The [20-paper source catalogue](origin/study_catalog.md) now supplies 23 tasks and 23 top-100 reference answers. One original paper contributes four tasks; each added paper contributes its selected comparison.

| Task | Comparison | Curator source |
|---|---|---|
| [task_001](task/task_001.md) | Dexamethasone vs untreated airway smooth muscle cells | [study_01](origin/study_01.md) |
| [task_002](task/task_002.md) | Lrpprc knockout vs wild-type mouse hearts | [study_02](origin/study_02.md) |
| [task_003](task/task_003.md) | Smooth muscle: TNF-α vs control | [study_03](origin/study_03.md) |
| [task_004](task/task_004.md) | Smooth muscle: IL-1β vs control | [study_03](origin/study_03.md) |
| [task_005](task/task_005.md) | Endothelial: TNF-α vs control | [study_03](origin/study_03.md) |
| [task_006](task/task_006.md) | Endothelial: IL-1β vs control | [study_03](origin/study_03.md) |
| [task_007](task/task_007.md) | siSRSF1 vs control siRNA in HeLa cells | [study_04](origin/study_04.md) |
| [task_008](task/task_008.md) | HOXA1 knockdown vs scramble | [study_05](origin/study_05.md) |
| [task_009](task/task_009.md) | INSR shRNA vs scramble shRNA | [study_06](origin/study_06.md) |
| [task_010](task/task_010.md) | AM580, day 6 vs DMSO, day 6 | [study_07](origin/study_07.md) |
| [task_011](task/task_011.md) | set2 deletion vs wild type | [study_08](origin/study_08.md) |
| [task_012](task/task_012.md) | cord-blood-derived vs adult-bone-marrow-derived | [study_09](origin/study_09.md) |
| [task_013](task/task_013.md) | old, 26-31 months vs adult, 5.5-8.5 months | [study_10](origin/study_10.md) |
| [task_014](task/task_014.md) | Tcf1/Lef1 deficient vs wild type | [study_11](origin/study_11.md) |
| [task_015](task/task_015.md) | mfl1 (GEO label) vs Col-0 | [study_12](origin/study_12.md) |
| [task_016](task/task_016.md) | Mut.1, day-15 neurons vs WT, day-15 neurons | [study_13](origin/study_13.md) |
| [task_017](task/task_017.md) | bam mutant + Mei-P26 RNAi vs bam mutant | [study_14](origin/study_14.md) |
| [task_018](task/task_018.md) | Suz12 full KO vs WT | [study_15](origin/study_15.md) |
| [task_019](task/task_019.md) | Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+ | [study_16](origin/study_16.md) |
| [task_020](task/task_020.md) | siOGT vs control siRNA | [study_17](origin/study_17.md) |
| [task_021](task/task_021.md) | Sun1 KO tumors vs control tumors | [study_18](origin/study_18.md) |
| [task_022](task/task_022.md) | Sox10 conditional KO vs control | [study_19](origin/study_19.md) |
| [task_023](task/task_023.md) | 0.7 mM hydrogel vs unembedded 96-well control | [study_20](origin/study_20.md) |

The evaluator downloads and anonymizes the relevant raw files before testing; see [preparation](origin/README.md). Reference resources and software installation packages, including dependencies, must also be available locally.

The task download links are for preparation and can reveal the source study. For offline testing, remove the download links from the task copy and give the model only the short prompt, anonymized raw files, and local reference/software resources. Disable network access. Keep `origin/`, this README, Git history, original downloads, and download logs outside the test environment.

The [reference answers and extraction instructions](origin/README.md#reference-answers) are for evaluation only. Each JSON contains 100 upregulated and 100 downregulated gene IDs; the script extracts existing author results without rerunning DEG analysis.

Raw sequencing files and original author result archives are not versioned here. The [SRA downloader and manifest](origin/downloads.md) cover the selected 160 runs; local download progress is recorded separately. Raw-data anonymization and offline tests have not been performed. Removing identifiers reduces explicit source clues but cannot guarantee an unseen dataset or prevent recognition from experimental details or sequences.
