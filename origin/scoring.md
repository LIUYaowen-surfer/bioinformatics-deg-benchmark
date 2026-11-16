# DEG overlap scoring

[score_deg.py](score_deg.py) compares one LLM result with its reference. Python's standard library is sufficient. Run it in the evaluator environment; keep this script and the references outside the LLM workspace.

Both JSON files must contain exactly `up` and `down`. Each value must be a list of 100 different, nonempty gene-ID strings, with no ID appearing in both lists.

```text
up_overlap   = |predicted_up ∩ reference_up|
down_overlap = |predicted_down ∩ reference_down|
score        = up_overlap + down_overlap
```

The score is an integer from **0 to 200**, with no normalization. Wrong-direction matches receive no credit. Order within a list does not affect the score. Matching is case-sensitive and uses the original ID strings: no trimming, version removal, symbol conversion or splitting of composite IDs.

From the repository root:

```sh
python origin/score_deg.py --task task_001 --prediction model_result.json
```

All 23 task-to-reference mappings are explicit in the script. To supply a reference directly:

```sh
python origin/score_deg.py --prediction model_result.json --reference origin/study_01/reference/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json
```

Example output for 80 correct upregulated and 70 correct downregulated IDs:

```json
{
  "score": 150,
  "max_score": 200,
  "up_overlap": 80,
  "down_overlap": 70
}
```

Add `--output score.json` to save the result to a new UTF-8 file. Existing files are never overwritten. A custom reference can use `--k 50`; both lists must then contain exactly 50 IDs and the maximum score is 100. Bundled tasks always use K=100.

Malformed JSON, extra/missing keys, duplicate IDs, nonstring IDs, wrong list sizes or overlapping up/down lists are rejected. The script does not truncate, pad or silently deduplicate. File/data errors return JSON with `"score": null` and an `"error"` message, and exit with code 2; do not treat this as a valid zero score. A successful score exits with code 0. Reference files are validated by the same rules as predictions.
