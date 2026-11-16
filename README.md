# Bioinformatics DEG Benchmark

## Overview

This benchmark evaluates whether an AI agent can carry out RNA-seq differential gene expression analysis from raw sequencing data, choose and use local bioinformatics tools, and reproduce the authors' ranked gene lists.

There are **23 tasks from 20 papers**. Each task supplies two groups of raw RNA-seq data, called `treated` and `untreated`, and has a reference answer extracted from an author-published DEG result table. One paper contributes four separate comparisons. Scoring counts same-direction overlap with the top 100 upregulated and top 100 downregulated reference genes, for a maximum of **200**.

This is a researcher/evaluator repository. Task READMEs preserve the papers, true conditions, source accessions, experimental designs, and reference provenance. They are not Agent prompts. All tasks share [agent_prompt.md](agent_prompt.md); only the prepared inputs described below belong in the Agent's offline workspace.

`treated` and `untreated` are benchmark aliases, not universal biological conditions. Depending on the task, `untreated` means untreated cells, vehicle control, wild type, control siRNA, or another comparison group. Positive log2 fold change always means `treated / untreated`.

## Repository structure

```text
bioinformatics-deg-benchmark/
├── README.md
├── eval_config.yaml
├── agent_prompt.md
├── task_01/
│   ├── README.md
│   ├── filelink.md
│   └── reference/
│       └── top100.json
├── ...
├── task_23/
│   ├── README.md
│   ├── filelink.md
│   └── reference/
│       └── top100.json
├── extract_reference.py
├── score_deg.py
└── scoring.md
```

- `task_XX/README.md`: inherited research documentation, the selected comparison, sample/run relationships, author-result links, extraction columns, and known limitations; evaluator only.
- `task_XX/filelink.md`: the original `treated` and `untreated` SRA download links; preparation only. These links reveal source accessions.
- `task_XX/reference/top100.json`: the existing reference answer, migrated without changing any bytes; evaluator only.
- [eval_config.yaml](eval_config.yaml): a proposed environment, input, output, and evaluation specification. It is not an installer or runner.
- [agent_prompt.md](agent_prompt.md): the single common Agent instruction.
- [extract_reference.py](extract_reference.py): the unchanged author-result extraction utility, with its legacy layout documented below.
- [score_deg.py](score_deg.py) and [scoring.md](scoring.md): the unchanged scoring utility and its usage. Both Python scripts use only the standard library.

### Tasks

| Task | Selected comparison | Downloads | Reference |
|---|---|---|---|
| [task_01](task_01/README.md) | Dexamethasone vs untreated | [Links](task_01/filelink.md) | [Top 100](task_01/reference/top100.json) |
| [task_02](task_02/README.md) | Lrpprc knockout vs wild type | [Links](task_02/filelink.md) | [Top 100](task_02/reference/top100.json) |
| [task_03](task_03/README.md) | SMC: TNF-α vs control | [Links](task_03/filelink.md) | [Top 100](task_03/reference/top100.json) |
| [task_04](task_04/README.md) | SMC: IL-1β vs control | [Links](task_04/filelink.md) | [Top 100](task_04/reference/top100.json) |
| [task_05](task_05/README.md) | EC: TNF-α vs control | [Links](task_05/filelink.md) | [Top 100](task_05/reference/top100.json) |
| [task_06](task_06/README.md) | EC: IL-1β vs control | [Links](task_06/filelink.md) | [Top 100](task_06/reference/top100.json) |
| [task_07](task_07/README.md) | siSRSF1 vs control siRNA | [Links](task_07/filelink.md) | [Top 100](task_07/reference/top100.json) |
| [task_08](task_08/README.md) | HOXA1 knockdown vs scramble | [Links](task_08/filelink.md) | [Top 100](task_08/reference/top100.json) |
| [task_09](task_09/README.md) | INSR shRNA vs scramble shRNA | [Links](task_09/filelink.md) | [Top 100](task_09/reference/top100.json) |
| [task_10](task_10/README.md) | AM580, day 6 vs DMSO, day 6 | [Links](task_10/filelink.md) | [Top 100](task_10/reference/top100.json) |
| [task_11](task_11/README.md) | set2 deletion vs wild type | [Links](task_11/filelink.md) | [Top 100](task_11/reference/top100.json) |
| [task_12](task_12/README.md) | cord-blood-derived vs adult-bone-marrow-derived | [Links](task_12/filelink.md) | [Top 100](task_12/reference/top100.json) |
| [task_13](task_13/README.md) | old, 26-31 months vs adult, 5.5-8.5 months | [Links](task_13/filelink.md) | [Top 100](task_13/reference/top100.json) |
| [task_14](task_14/README.md) | Tcf1/Lef1 deficient vs wild type | [Links](task_14/filelink.md) | [Top 100](task_14/reference/top100.json) |
| [task_15](task_15/README.md) | mfl1 (GEO label) vs Col-0 | [Links](task_15/filelink.md) | [Top 100](task_15/reference/top100.json) |
| [task_16](task_16/README.md) | Mut.1, day-15 neurons vs WT, day-15 neurons | [Links](task_16/filelink.md) | [Top 100](task_16/reference/top100.json) |
| [task_17](task_17/README.md) | bam mutant + Mei-P26 RNAi vs bam mutant | [Links](task_17/filelink.md) | [Top 100](task_17/reference/top100.json) |
| [task_18](task_18/README.md) | Suz12 full KO vs WT | [Links](task_18/filelink.md) | [Top 100](task_18/reference/top100.json) |
| [task_19](task_19/README.md) | Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+ | [Links](task_19/filelink.md) | [Top 100](task_19/reference/top100.json) |
| [task_20](task_20/README.md) | siOGT vs control siRNA | [Links](task_20/filelink.md) | [Top 100](task_20/reference/top100.json) |
| [task_21](task_21/README.md) | Sun1 KO tumors vs control tumors | [Links](task_21/filelink.md) | [Top 100](task_21/reference/top100.json) |
| [task_22](task_22/README.md) | Sox10 conditional KO vs control | [Links](task_22/filelink.md) | [Top 100](task_22/reference/top100.json) |
| [task_23](task_23/README.md) | 0.7 mM hydrogel vs unembedded 96-well control | [Links](task_23/filelink.md) | [Top 100](task_23/reference/top100.json) |

## Environment setup

Use [eval_config.yaml](eval_config.yaml) as the deployment specification. It suggests Linux/Ubuntu 24.04 LTS, Python 3.12.8, R 4.4.2 with Bioconductor 3.20, common Python scientific libraries, and explicit versions of FastQC, fastp, STAR, HISAT2, Salmon, samtools, featureCounts/subread, DESeq2, edgeR, and limma. The R/Bioconductor pairing follows the [Bioconductor release table](https://bioconductor.org/about/release-announcements/); individual release sources are recorded in the YAML.

These are a proposed historical software baseline, not the original authors' versions or a claim that an environment has been installed. The combination and its transitive dependencies have not been integration-tested. This YAML is a custom specification: do not pass it directly to `conda env create`, and do not assume either Python script reads it.

Before a formal run:

1. Build a Linux environment or image using the specified releases and their documented installation instructions. Include transitive dependencies and a compatible Java runtime for FastQC. Make the listed tools available; the Agent can choose which to use. No fixed alignment, quantification, or DEG pipeline is required.
2. Resolve and record the complete package set, executable versions, R `sessionInfo()`, and image digest or environment lock. Keep the same deployed resources across Agents compared on one task. Record any deviation from the proposed baseline. Verify tools start and R packages load before disabling network access. Cache any additional permitted installation packages and dependencies in advance.
3. Prepare task-specific genome sequences, GTF/GFF annotation, and appropriate alignment/quantification resources outside Git. Freeze assembly and annotation releases, identifier namespace, source URLs, local paths, and checksums. Supply compatible indexes, or permit their construction offline from the supplied sequences. Transcript-based workflows may also require transcript sequences and a transcript-to-gene map.
4. Fill the task's `reference_resources.overrides` in an evaluator-side copy of the configuration. Each override follows the fields under `reference_resources.defaults`; it replaces those defaults for that task. Do not use a modern annotation silently when the author results use versioned or custom identifiers such as XLOC. Unresolved resource choices must be checked before formal scoring.
5. Set and record CPU, memory, time, and disk allowances based on the selected task. They are deliberately `null` in the template because no validated limits have been established. Enforce limits and offline isolation through the external runner or operating system; editing the YAML alone does not enforce them.

The Agent chooses its analysis workflow within this prepared environment. This follows the open-ended scientific-task motivation discussed in [GeneBench-Pro](https://jeremyhli.org/writing/genebench-pro/); this repository does not reproduce its environment or scoring protocol.

## Usage workflow

### Step 1: Select a task

For example, choose [task_01](task_01/README.md). Read its research notes as the evaluator and identify the selected comparison, biological samples, donor pairing, and sequencing runs. For tasks 03–06, each README retains the full shared study documentation but explicitly names its own comparison; use only that task's selected groups.

### Step 2: Download the data

Follow [task_01/filelink.md](task_01/filelink.md) for its two groups. Download only the linked SRA runs, retaining original downloads and source mappings outside the Agent workspace. If the download is an SRA archive, obtain full-quality FASTQ using an appropriate SRA export tool before testing; preserve paired, single-end, and unpaired reads. Downloading and lossless FASTQ export are preparation, not DEG analysis.

Do not trim, filter, align, normalize, or generate counts during preparation. Multiple sequencing runs or lane splits from the same sample remain technical subdivisions of that sample, not additional biological replicates. Consult the task README for the run-to-sample mapping.

### Step 3: Prepare the environment

Complete the [environment setup](#environment-setup) for this task. Stage the necessary software and reference resources locally before disabling the Agent's network access. The repository does not include FASTQ, genomes, annotations, indexes, installed software, or a finished Docker/Conda environment.

### Step 4: Prepare a separate Agent workspace

Create a fresh directory outside the repository. Copy only the common Prompt, lossless anonymous raw-data copies, necessary experimental design information, and reference/software resources. For example:

```text
agent_workspace/
├── agent_prompt.md
├── input/
│   ├── samples.tsv
│   └── data/
│       ├── treated/
│       └── untreated/
├── resources/
│   ├── genome.fa
│   ├── annotation.gtf
│   └── indexes/          # optional; suitable for the provided tools
├── packages/             # optional offline installation cache
└── result.json           # produced by the Agent
```

The paths above are an example, not bundled files. Use GTF or GFF as appropriate. Prepare `input/samples.tsv` from the documented sample relationships: one row per sequencing run or library file set, with anonymous `sample_id`, `condition` (`treated`/`untreated`), `read_layout`, and relative FASTQ paths. Include mate paths, unpaired-read paths, donor/pair IDs, and batch/block labels when applicable. Reuse `sample_id` across runs of the same biological sample. Do not infer pairing from sample order. If essential design information is unresolved, settle it before the run. Preserve this information while withholding the true treatment names and source accessions.

To reduce explicit source clues, anonymize filenames, directories, FASTQ read identifiers/descriptions (including `+` lines), and compressed-file metadata. Preserve every sequence, quality score, record, order, and mate relationship; apply consistent unique read aliases. File renaming alone is insufficient because default [SRA Toolkit FASTQ headers](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump) can contain accessions. Keep original downloads and the source-to-alias mapping with the evaluator.

Do not copy or mount the whole repository. Exclude task/root READMEs, `filelink.md`, all `reference/top100.json` files, author DEG tables, papers, source archives, download logs, Git history, extraction/scoring tools, evaluator configuration, and artifacts from other tasks. Mount only the explicit inputs above. The configuration's separation rules need an external runner to enforce them; this refactor does not create or verify a live Agent workspace.

### Step 5: Run the Agent

Start the Agent in the fresh workspace with [agent_prompt.md](agent_prompt.md). Disable its network/browser access for formal offline evaluation. The Agent independently chooses and executes an RNA-seq workflow using the staged data, design information, and tools.

The Agent writes `result.json` in the workspace root and returns the same JSON object as its final response. It must contain exactly `up` and `down`, each holding 100 unique, nonempty gene-ID strings; the two lists must be disjoint. Rank by adjusted P value within each direction, breaking ties by the unchanged ID string, with no additional significance or fold-change cutoff. Do not substitute raw P values. Missing results, invalid tests, and zero log2FC are not eligible.

This is a shape illustration only; an actual output needs 100 IDs per array:

```json
{
  "up": ["gene_id_1", "gene_id_2"],
  "down": ["gene_id_3", "gene_id_4"]
}
```

Do not fabricate IDs or pad lists when a workflow cannot produce 100 eligible genes in a direction. Such a run does not meet the output contract; the scorer reports invalid output rather than silently lowering K.

### Step 6: Evaluate outside the Agent workspace

Copy the produced `result.json` to an evaluator-owned location. From the repository root, run:

```bash
python score_deg.py result.json task_01/reference/top100.json
```

Replace the task path with the selected task. The scorer accepts exactly two JSON paths and prints one integer. It does not select a task automatically or read `eval_config.yaml`. Invalid JSON or invalid lists cause an error, exit code 2, and no numeric score. See [scoring.md](scoring.md).

### Step 7: Interpret the score

```text
score = |predicted_up ∩ reference_up| + |predicted_down ∩ reference_down|
```

The range is **0–200**, with no normalization. A result with 80 matching upregulated genes and 70 matching downregulated genes scores 150. Wrong-direction matches receive no credit. Matching is exact and case/version sensitive; list order does not affect the score. The scorer checks membership and format, not the provenance or statistical validity of the Agent's analysis.

Different defensible workflows, reference annotations, and statistical methods can yield different rankings. Overlap measures reproduction of the authors' selected results; it is not a universal measure of biological correctness and does not establish the paper's broader mechanistic conclusions. Record the workflow and environment alongside each score outside the Agent workspace.

## Reference extraction and compatibility

The 23 existing JSONs were moved without changing their content, formatting, order, or gene IDs. No author table was re-extracted and no DEG analysis was rerun for this refactor. The two Python scripts were moved from `origin/` to the root without changing their bytes or algorithms. Old `task_001`–`task_023` IDs map in order to `task_01`–`task_23`; each task README records its previous study and reference filename.

The existing extraction rule uses the configured original gene ID, log2FC, adjusted-P column, and valid test status (`OK`, where present). Missing required fields and zero log2FC are excluded. It does not filter on a `significant` flag, an additional adjusted-P cutoff, or a fold-change threshold. Eligible rows are ranked by adjusted P value, then the untouched gene-ID string, separately by direction. Author signs were reversed during the original extraction for airway (`task_01`), old/adult zebrafish (`task_13`), and Sun1 tumors (`task_21`) to give treated/untreated. No sign is changed again during migration or scoring.

Two author files contain reviewed duplicate IDs. All source rows remain in ranking and those ambiguous IDs lie outside the selected top 100. The extractor blocks a larger K if it would include one; it does not keep the first row, merge IDs, repair spreadsheet identifiers, or silently convert them. See [task_16](task_16/README.md) and [task_17](task_17/README.md).

**The unchanged extractor still uses the legacy `study_XX` layout.** It does not generate `task_XX/reference/top100.json`. Its `FILE_CONFIGS` expects the original seven files at the input root, and the 16 added author files under `study_XX/author_results/`. It verifies their reviewed SHA-256 values and emits `<output-dir>/study_XX/reference/<source>__<comparison>_top100.json`.

If you later need to re-extract author tables, prepare that exact input layout outside the Agent workspace and use a new scratch output directory:

```bash
python extract_reference.py \
  --input-dir /path/to/original-author-results \
  --output-dir /path/to/new-reference-scratch \
  --k 100
```

Inspect the reported completed/pending comparisons and map any outputs using the previous filenames in the task READMEs. Do not direct the legacy output at the repository or assume it updates the migrated answers. For another K, use a separate output directory; the unchanged scorer still requires K=100, so those results are outside the present scoring protocol. Normal benchmark use requires only the existing reference JSONs and `score_deg.py`.

## Notes and limitations

- Raw sequencing data, original author result archives, and large reference resources are not stored in GitHub. Users download them; this refactor did not download, anonymize, analyze, or generate sequencing data.
- Preserve biological replication, pairing and batch structure. Some samples are biological pools; some have multiple runs. `task_01` has paired donors, `task_11` has lane/run splits, and `task_20` has paired experiments. Keep the specific design notes for every task.
- Exact genome/annotation choices and computational limits are not yet frozen. `task_14` retains an mm9/mm10 metadata conflict. Tasks using custom XLOC or coding/noncoding annotation require matching reference resources. Do not call these fully standardized offline runs until the deployment choices have been recorded.
- Existing source anomalies and scope restrictions are retained in each task README, including the INSR fold-change discrepancy, spreadsheet IDs in `task_16`, duplicate Chd64 tests in `task_17`, and the specific ESC and whole-tumor comparisons in `task_18` and `task_21`.
- Papers, author results and reference answers must remain outside the Agent's workspace. This public repository and its history contain them. Directory organization and anonymization cannot guarantee absence of training-data contamination or prevent study recognition from sequences or experimental details.
- Airway (`task_01`) and the HOXA1 dataset (`task_08`) are widely used in teaching; they are especially suitable for workflow debugging or a public baseline. Author-derived DEG lists are reference results, not unique biological ground truth.
- The environment file is a specification, not a Dockerfile, Conda lock, installed environment, or evaluation harness. Network restrictions, allowed mounts, software validation and per-task resource preparation remain deployment work.

## Paper and source catalogue

The original 20-paper catalogue is retained here. Source checks were recorded on 2026-11-15; restructuring does not represent a new literature review. Counts are selected sample records, treated/control, not sequencing-run counts. The four Pan comparisons remain separate tasks and share some controls.

| Task(s) | Paper | Selected comparison | Samples T/C | Data | Author DEG reference |
|---|---|---|---|---|---|
| [task_01](task_01/README.md) | [Himes 2014](https://doi.org/10.1371/journal.pone.0099625) | Dexamethasone vs untreated; human airway smooth muscle | 4/4, paired donors | [GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=SRP033351) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz) |
| [task_02](task_02/README.md) | [Siira 2017](https://doi.org/10.1038/s41467-017-01221-z) | Lrpprc knockout vs wild type; mouse hearts | 4/4 | [GSE100732](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100732) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=SRP110979) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz) |
| [task_03](task_03/README.md), [task_04](task_04/README.md), [task_05](task_05/README.md), [task_06](task_06/README.md) | [Pan 2018](https://doi.org/10.1038/s41598-017-18675-2) | TNF-alpha or IL-1beta vs control, separately in vascular SMCs and ECs | 3/3 per contrast; 18 unique samples | [GSE96962](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96962) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=SRP102361) | [Four author tables](task_03/README.md) |
| [task_07](task_07/README.md) | [Olazabal-Herrero 2024](https://doi.org/10.1016/j.celrep.2023.113610) | siSRSF1 vs control siRNA; HeLa cells | 2/2 | [GSE212471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212471) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA875477) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz) |
| [task_08](task_08/README.md) | [Trapnell 2013](https://doi.org/10.1038/nbt.2450) | HOXA1 knockdown vs scramble; human lung fibroblasts, HiSeq only | 3/3 | [GSE37703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37703) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA162905) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE37nnn/GSE37703/suppl/GSE37703_hiseq_cuffdiff_gene_exp.diff.gz) |
| [task_09](task_09/README.md) | [Teo 2021](https://doi.org/10.1016/j.jbc.2021.100495) | INSR shRNA vs scramble; human CHB8 embryonic stem cells | 2/2 | [GSE60328](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60328) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA258044) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60328/suppl/GSE60328_gene_exp.diff.gz) |
| [task_10](task_10/README.md) | [Dou 2016](https://doi.org/10.1038/ncb3354) | AM580 vs DMSO at day 6; human EB-derived HSPCs on OP9 | 2/2 | [GSE76682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76682) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA308426) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE76nnn/GSE76682/suppl/GSE76682_EB_AM580gene_exp.diff.gz) |
| [task_11](task_11/README.md) | [Sayou 2017](https://doi.org/10.1128/mcb.00165-17) | set2 deletion vs wild type; budding yeast W303 | 3/3 | [GSE89238](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89238) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA350794) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89238/suppl/GSE89238_SET2_KO_DESeq2_output.txt.gz) |
| [task_12](task_12/README.md) | [Fiorini 2017](https://doi.org/10.1002/ajh.24805) | Cord-blood-derived vs adult-bone-marrow-derived human erythroid cells after xenograft | 3/3 | [GSE100077](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100077) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA390632) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100077/suppl/GSE100077_DifferentialExpression.csv.gz) |
| [task_13](task_13/README.md) | [Erbaba 2020](https://doi.org/10.1016/j.neurobiolaging.2020.04.017) | Old vs adult zebrafish brain-derived progenitor-enriched cultures | 3/3 | [GSE133436](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133436) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA551453) | [Author table](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE133436&format=file&file=GSE133436_gene_exp_oldYoung_.diff.gz) |
| [task_14](task_14/README.md) | [Shan 2021](https://doi.org/10.1038/s41467-021-26159-1) | Tcf1/Lef1 double knockout vs wild type; naive mouse CD8 T cells | 3/3 | [GSE164712](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164712) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA691621) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE164nnn/GSE164712/suppl/GSE164712_gene_exp.diff.gz) |
| [task_15](task_15/README.md) | [Nagarajan 2023](https://doi.org/10.1093/plcell/koad085) | GEO-labeled mfl1 mutant vs Col-0; Arabidopsis seedlings, conventional RNA-seq | 3/3 | [GSE193247](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193247) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA795486) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE193nnn/GSE193247/suppl/GSE193247_gene_exp.diff.gz) |
| [task_16](task_16/README.md) | [Lau 2023](https://doi.org/10.1038/s41467-023-42078-9) | Top1(R548Q) mutant clone 1 vs wild type; day-15 mESC-derived neurons | 2/2 | [GSE207163](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207163) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA854061) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE207nnn/GSE207163/suppl/GSE207163_RNA-seq.xlsx) |
| [task_17](task_17/README.md) | [Gui 2023](https://doi.org/10.1016/j.celrep.2023.112181) | Mei-P26 RNAi vs control in bam-mutant Drosophila ovaries | 2/2 | [GSE218205](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218205) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA902740) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE218nnn/GSE218205/suppl/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz) |
| [task_18](task_18/README.md) | [Arecco 2024](https://doi.org/10.1016/j.molcel.2024.02.011) | Suz12 full knockout vs wild type; mouse embryonic stem cells | 3/3 | [GSE223666](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE223666) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA927240) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE223nnn/GSE223666/suppl/GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz) |
| [task_19](task_19/README.md) | [Xu 2025](https://doi.org/10.70322/jrbtm.2025.10008) | Shhcre;Lonp1f/f vs Shhcre;Lonp1f/+; E13.5 whole mouse lungs | 4/3 | [GSE230334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230334) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA958384) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE230nnn/GSE230334/suppl/GSE230334_gene_exp.diff.gz) |
| [task_20](task_20/README.md) | [Very 2024](https://doi.org/10.1038/s41419-024-06773-9) | siOGT vs control siRNA; human LX-2 cells, 20 nM for 72 h | 3/3 | [GSE243105](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243105) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1016370) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE243nnn/GSE243105/suppl/GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz) |
| [task_21](task_21/README.md) | [Nasr 2024](https://doi.org/10.1016/j.ebiom.2024.105167) | Sun1 knockout vs control; CT26 whole tumors at day 14 | 7/8 | [GSE250602](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250602) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1054607) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE250nnn/GSE250602/suppl/GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz) |
| [task_22](task_22/README.md) | [Jörg 2024](https://doi.org/10.3390/ijms25168754) | Conditional Sox10 knockout vs control; mouse corpus callosum, dpi21 | 4/4 | [GSE269122](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269122) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1120355) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE269nnn/GSE269122/suppl/GSE269122_ctrl_vs_Sox10ko.xlsx) |
| [task_23](task_23/README.md) | [Pineau 2025](https://doi.org/10.1242/dev.204711) | 0.7 mM dextran hydrogel embedding at 96 h vs no embedding; mouse gastruloids | 3/3 | [GSE288157](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288157) / [SRA](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA1216293) | [Author table](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE288nnn/GSE288157/suppl/GSE288157_DESeq2_summary.txt.gz) |

Only documentation, source links, configuration, the common Prompt, the two utilities, and derived reference gene lists are versioned. Consult each task README for the full original research notes and selected run mapping.
