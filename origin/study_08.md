# study_08 - curator only

set2 deletion vs wild type; budding yeast W303. Selected samples: 3 treated / 3 control.

- Paper: Sayou et al. (2017), [RNA Binding by Histone Methyltransferases Set1 and Set2](https://doi.org/10.1128/mcb.00165-17).
- DOI: [10.1128/mcb.00165-17](https://doi.org/10.1128/mcb.00165-17); [PubMed 28483910](https://pubmed.ncbi.nlm.nih.gov/28483910/).
- GEO: [GSE89238](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89238).
- SRA: [PRJNA350794](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA350794); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR4457475%20OR%20SRR4457476%20OR%20SRR4457477%20OR%20SRR4457478%20OR%20SRR4457479%20OR%20SRR4457480%20OR%20SRR4457481%20OR%20SRR4457482%20OR%20SRR4457483%20OR%20SRR4457484%20OR%20SRR4457485%20OR%20SRR4457486) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR4457463%20OR%20SRR4457464%20OR%20SRR4457465%20OR%20SRR4457466%20OR%20SRR4457467%20OR%20SRR4457468%20OR%20SRR4457469%20OR%20SRR4457470%20OR%20SRR4457471%20OR%20SRR4457472%20OR%20SRR4457473%20OR%20SRR4457474).
- Author DEG reference: [GSE89238_SET2_KO_DESeq2_output.txt.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89238/suppl/GSE89238_SET2_KO_DESeq2_output.txt.gz).
- Result fields: `gene_id`, `log2FoldChange`, `padj`.

Three independently grown colonies per group. The six samples span 24 runs; sequencing lanes are not biological replicates. The reference includes coding and noncoding features, so its annotation/ID definition needs to be retained.

Direction: The author result is the SET2-KO comparison; the SET2 row has negative log2FoldChange. Confirm the exact model coefficient when configuring formal extraction.

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2362797](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362797) | set2 deletion | SRR4457475, SRR4457476, SRR4457477, SRR4457478 |
| [GSM2362798](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362798) | set2 deletion | SRR4457479, SRR4457480, SRR4457481, SRR4457482 |
| [GSM2362799](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362799) | set2 deletion | SRR4457483, SRR4457484, SRR4457485, SRR4457486 |
| [GSM2362794](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362794) | wild type | SRR4457463, SRR4457464, SRR4457465, SRR4457466 |
| [GSM2362795](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362795) | wild type | SRR4457467, SRR4457468, SRR4457469, SRR4457470 |
| [GSM2362796](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362796) | wild type | SRR4457471, SRR4457472, SRR4457473, SRR4457474 |

Checked 2026-11-15. Complete author result file downloaded for inspection (1,005,666 bytes). SHA-256: `b783572da8b31661f49b4bbbf8daad7def5efd23d27a683c53abd78477db166c`.

Public raw-run records and FASTQ links were checked through SRA-linked GEO metadata and ENA. Raw reads were not downloaded. This is a source-screened candidate: full row validity, duplicate IDs, finite values, direction and 100 eligible genes per side still need extraction-level checks. No new reference JSON or model task has been created.
