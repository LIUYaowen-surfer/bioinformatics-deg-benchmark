# Bioinformatics DEG Benchmark

Minimal tasks for testing whether an AI can obtain raw RNA-seq data, set up its environment, use analysis tools, and identify differentially expressed genes.

- `task/`: a short English prompt and an SRA link restricted to the relevant samples.
- `origin/`: paper, DOI, GEO/SRA links, and the authors' DEG results for evaluation.

Give the model only the selected task file. Use the paper and its author-supplied DEG results as the reference.

| Study | Comparison | Task | Origin |
|---|---|---|---|
| GSE52778 | Dexamethasone vs untreated airway smooth muscle cells | [Task](task/GSE52778.md) | [Source](origin/GSE52778.md) |
| GSE100732 | Lrpprc knockout vs wild-type mouse hearts | [Task](task/GSE100732.md) | [Source](origin/GSE100732.md) |
| GSE96962 | TNF-α or IL-1β vs control, separately in smooth muscle and endothelial cells | [4 tasks](task/GSE96962/) | [Source](origin/GSE96962.md) |
| GSE212471 | siSRSF1 vs control siRNA in HeLa cells | [Task](task/GSE212471.md) | [Source](origin/GSE212471.md) |

This version contains links only; data files and analysis results are not included. No analysis has been run. Public datasets, especially airway, may already occur in teaching materials or model training data; folder separation does not prevent contamination.

Links checked: 2026-11-09.
