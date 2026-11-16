# DEG overlap scoring

[score_deg.py](score_deg.py) accepts two JSON file paths and prints one integer score. Choose the corresponding reference yourself. Only Python's standard library is needed.

Both JSON files must contain exactly `up` and `down`. Each value must be a list of 100 different, nonempty gene-ID strings, with no ID appearing in both lists.

Score = matching upregulated IDs + matching downregulated IDs, from **0 to 200**, with no normalization. Wrong-direction matches receive no credit. List order is ignored; gene IDs must match exactly, including case and version suffixes.

From the repository root:

```sh
python origin/score_deg.py model_result.json reference.json
```

Example output for 80 correct upregulated and 70 correct downregulated IDs:

```text
150
```

Both files are read-only. Invalid files or data produce an error on stderr and exit code 2, with no score on stdout. Successful scoring exits with code 0. Keep references outside the LLM workspace.
