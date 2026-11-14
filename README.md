# Offline DEG Benchmark

Minimal prompts for testing whether an AI can set up its environment, use local tools, and find differentially expressed genes without internet access.

- `task/`: anonymous task IDs and short English prompts, with no source links or accession numbers.
- `origin/`: curator-only papers, download links, filename mappings, the extraction script, and seven top-100 reference JSONs derived from author-provided DEG results.

| Task | Comparison | Curator source |
|---|---|---|
| [task_001](task/task_001.md) | Dexamethasone vs untreated airway smooth muscle cells | [study_01](origin/study_01.md) |
| [task_002](task/task_002.md) | Lrpprc knockout vs wild-type mouse hearts | [study_02](origin/study_02.md) |
| [task_003](task/task_003.md) | Smooth muscle: TNF-α vs control | [study_03](origin/study_03.md) |
| [task_004](task/task_004.md) | Smooth muscle: IL-1β vs control | [study_03](origin/study_03.md) |
| [task_005](task/task_005.md) | Endothelial: TNF-α vs control | [study_03](origin/study_03.md) |
| [task_006](task/task_006.md) | Endothelial: IL-1β vs control | [study_03](origin/study_03.md) |
| [task_007](task/task_007.md) | siSRSF1 vs control siRNA in HeLa cells | [study_04](origin/study_04.md) |

The evaluator downloads and anonymizes the relevant raw files before testing; see [preparation](origin/README.md). Reference resources and software installation packages, including dependencies, must also be available locally.

Give the model only its task prompt, anonymized raw files, and local reference/software resources. Disable network access. Keep `origin/`, this README, Git history, original downloads, and download logs outside the test environment.

The [reference answers and extraction instructions](origin/README.md#reference-answers) are for evaluation only. Each JSON contains 100 upregulated and 100 downregulated gene IDs; the script extracts existing author results without rerunning DEG analysis.

Raw sequencing files and original author result archives are not included; download them from the source links yourself. Raw-data anonymization and offline tests have not been performed. Removing identifiers reduces explicit source clues but cannot guarantee an unseen dataset or prevent recognition from experimental details or sequences.
