You are provided with RNA-seq data from treated and untreated samples.
Your task is to identify differentially expressed genes (DEGs) between the two groups.
Return only a JSON object with exactly two keys, "up" and "down", containing the top 100 upregulated and top 100 downregulated gene IDs respectively as arrays of unique strings, ranked by adjusted p-value within each direction (ties by ascending gene ID).
