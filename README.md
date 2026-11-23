# Bioinformatics DEG Benchmark

Identify the top 100 upregulated and top 100 downregulated genes from raw RNA-seq reads. Each task compares a treated group with its control and uses the authors’ differential expression table as the reference.

| Task | Comparison | Design | Raw data | Reference |
|---|---|---|---|---|
| [task_01](task_01/README.md) | Dexamethasone vs untreated human airway smooth muscle cells | Four donors, each sampled in both conditions | [Runs](task_01/filelink.md) | [Top 100](task_01/reference/top100.json) |
| [task_02](task_02/README.md) | Lrpprc knockout vs wild-type mouse hearts | Four samples per group | [Runs](task_02/filelink.md) | [Top 100](task_02/reference/top100.json) |

## Prepare the workspace

1. Choose a task and download its linked runs. Export full-quality paired-end FASTQ files into one directory, such as `downloads/`. Use split-3 filenames: `SRR…_1.fastq`, `SRR…_2.fastq`, and `SRR….fastq` if there are additional unpaired reads. The script accepts .fq or .fastq, plain or gzip-compressed. Check run identity and layout against source metadata before preparation.
2. From the repository root, run the command below with a new output path outside the repository. For the mouse task, substitute `task_02` and `../agent_workspace_02`.

```sh
python scripts/prepare_inputs.py --task task_01 --source-dir downloads --output-dir ../agent_workspace_01
```

[prepare_inputs.py](scripts/prepare_inputs.py) contains the two run mappings and the airway donor pairs. It creates `prompt.md`, anonymous FASTQs under `input/data/`, and `input/samples.tsv` with the condition, sample ID, block and workspace-relative read paths. Matching block IDs in task_01 identify the same donor. Block is blank for task_02. The script rewrites read names while preserving sequence, quality, order and mate relationships. Output FASTQs are uncompressed.

## Run the Agent

Stage species-appropriate genome sequences, annotations and any indexes or transcript-to-gene maps needed by the available tools. Record assembly and annotation versions, gene-ID namespace, tool versions and resource limits. [eval_config.yaml](eval_config.yaml) lists suggested software versions. It is not an installed or tested environment lock.

Give the Agent the prepared workspace and reference resources in an isolated offline environment. Keep task documentation, original filenames, author tables, answer JSONs, evaluator scripts and repository history outside that environment. Use the same resources for all Agents on a given task. The Agent chooses its workflow and follows the shared [prompt](agent_prompt.md) to write `result.json` in the workspace root.

## Score the result

Run the evaluator outside the Agent workspace with the reference for the selected task.

```sh
python scripts/score_deg.py ../agent_workspace_01/result.json task_01/reference/top100.json
```

The score counts exact same-direction gene-ID matches, from 0 to 200. Within each direction the requested ranking uses ascending adjusted p-value, with ties broken by original gene ID. The score uses set overlap and preserves case and version suffixes. See [scoring.md](scoring.md) for format validation.

## Reproduce the reference lists

The two checked-in reference JSONs are ready for scoring. To regenerate them, download the author tables linked from the two task READMEs into one directory and run:

```sh
python scripts/extract_reference.py --input-dir author_tables --output-dir ../regenerated
```

The extractor checks the source SHA-256 values and writes `task_01/reference/top100.json` and `task_02/reference/top100.json` under the output directory. It reverses the source fold-change sign for task_01 and keeps it for task_02 so positive means higher expression in the treated group. Missing measurements, invalid tests and zero fold changes are excluded. No extra significance or fold-change threshold is applied.
