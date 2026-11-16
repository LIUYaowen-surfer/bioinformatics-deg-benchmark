You are provided with RNA-seq data from treated and untreated samples.

Your task is to identify differentially expressed genes (DEGs) between the two groups.

Perform the necessary analysis using the provided data, experimental design information, reference resources, and available bioinformatics tools. You may choose an appropriate analysis workflow.

Return the top 100 upregulated genes and top 100 downregulated genes, ranked by adjusted p-value within each direction. Break ties by gene identifier in ascending string order. Do not substitute unadjusted p-values.

Do not apply an additional significance or fold-change cutoff when selecting the top 100 genes. Exclude invalid tests, missing gene identifiers or test results, and zero log2 fold changes.

Upregulation and downregulation are defined relative to the untreated group: positive log2(treated / untreated) is upregulated; negative is downregulated.

Use gene identifiers consistent with the provided reference annotation. Preserve identifier strings, including version suffixes and composite identifiers.

Save your answer as result.json in the workspace root. Your final response must be the same valid JSON object containing exactly two keys: "up" and "down".

Each key must contain an array of exactly 100 unique, nonempty gene identifier strings. The two arrays must not overlap. Do not invent identifiers or duplicate genes to fill a list.

Do not include explanations, Markdown formatting, or additional text in the final response.
