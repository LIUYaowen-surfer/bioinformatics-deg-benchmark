# study_01 — curator only

Dexamethasone vs untreated human airway smooth muscle cells; 8 relevant samples.

- Paper: Himes et al. (2014), [RNA-Seq Transcriptome Profiling Identifies CRISPLD2 as a Glucocorticoid Responsive Gene that Modulates Cytokine Function in Airway Smooth Muscle Cells](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099625).
- DOI: [10.1371/journal.pone.0099625](https://doi.org/10.1371/journal.pone.0099625).
- GEO: [GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778).
- SRA: [SRP033351](https://www.ncbi.nlm.nih.gov/sra?term=SRP033351).
- Author DEG results: [Dex vs untreated](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz).

| Task | Comparison | Selected raw data |
|---|---|---|
| `task_001` | Dexamethasone vs untreated | [Download](https://www.ncbi.nlm.nih.gov/sra?term=SRR1039508%20OR%20SRR1039509%20OR%20SRR1039512%20OR%20SRR1039513%20OR%20SRR1039516%20OR%20SRR1039517%20OR%20SRR1039520%20OR%20SRR1039521) |

Use these local filename prefixes; keep this mapping outside the model environment.
Append `_R1.fastq.gz` and `_R2.fastq.gz` for paired reads; retain any unpaired reads as `_unpaired.fastq.gz`.
The same donor alias identifies the same donor across the two conditions.

| Downloaded run | Local filename prefix |
|---|---|
| `SRR1039508` | `untreated_donor01` |
| `SRR1039509` | `dexamethasone_donor01` |
| `SRR1039512` | `untreated_donor02` |
| `SRR1039513` | `dexamethasone_donor02` |
| `SRR1039516` | `untreated_donor03` |
| `SRR1039517` | `dexamethasone_donor03` |
| `SRR1039520` | `untreated_donor04` |
| `SRR1039521` | `dexamethasone_donor04` |
