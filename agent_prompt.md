Identify the top 100 upregulated and top 100 downregulated genes in the supplied RNA-seq data, comparing `treated` with `untreated` using the sample design and your choice of available offline tools and methods.

## Gene selection

- `up` — positive log2 fold change for treated / untreated
- `down` — negative log2 fold change for treated / untreated

Within each direction, rank valid tests by ascending adjusted p-value, break ties by ascending original gene ID, and take the first 100 without applying an additional significance or fold-change cutoff.

## Output format

Return only a JSON object suitable for saving as `result.json`, following this shortened example.

```json
{
  "up": ["gene_A", "gene_B"],
  "down": ["gene_C", "gene_D"]
}
```

- Exactly two keys, `up` and `down`, each with an array of exactly 100 nonempty gene-ID strings
- Unique IDs within and across arrays, preserving original case and version suffixes
- No placeholder IDs, extra fields, Markdown fences, or explanatory text in the result
