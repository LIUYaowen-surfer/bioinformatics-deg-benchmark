# task_11 — research and reference notes

**Selected comparison: set2 deletion vs wild type.** Positive changes are defined as treated relative to untreated.

For preparation and evaluation only; do not give this page or its linked author results to the Agent. Use [filelink.md](filelink.md) for the selected groups and [top100.json](reference/top100.json) for evaluation.

## Study documentation

set2 deletion vs wild type; budding yeast W303. Selected samples: 3 treated / 3 control.

- Task: [task_11](../task_11/filelink.md).
- Reference: [top100 JSON](reference/top100.json).
- Paper: Sayou et al. (2017), [RNA Binding by Histone Methyltransferases Set1 and Set2](https://doi.org/10.1128/mcb.00165-17).
- DOI: [10.1128/mcb.00165-17](https://doi.org/10.1128/mcb.00165-17); [PubMed 28483910](https://pubmed.ncbi.nlm.nih.gov/28483910/).
- GEO: [GSE89238](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89238).
- SRA: [PRJNA350794](https://www.ncbi.nlm.nih.gov/sra?term=PRJNA350794); selected [treated runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR4457475%20OR%20SRR4457476%20OR%20SRR4457477%20OR%20SRR4457478%20OR%20SRR4457479%20OR%20SRR4457480%20OR%20SRR4457481%20OR%20SRR4457482%20OR%20SRR4457483%20OR%20SRR4457484%20OR%20SRR4457485%20OR%20SRR4457486) / [control runs](https://www.ncbi.nlm.nih.gov/sra?term=SRR4457463%20OR%20SRR4457464%20OR%20SRR4457465%20OR%20SRR4457466%20OR%20SRR4457467%20OR%20SRR4457468%20OR%20SRR4457469%20OR%20SRR4457470%20OR%20SRR4457471%20OR%20SRR4457472%20OR%20SRR4457473%20OR%20SRR4457474).
- Author DEG reference: [GSE89238_SET2_KO_DESeq2_output.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE89238&format=file&file=GSE89238_SET2_KO_DESeq2_output.txt.gz).
- Result fields: ID `gene_id`, log2FC `log2FoldChange`, adjusted P `padj`.

Three independent colonies per group, spread over 24 sequencing runs. Merge lane splits by biological sample during analysis. Retain the original coding/noncoding feature annotation.

Direction: Keep the author log2FC sign (treated/control).

| GEO sample | Condition | SRA runs |
|---|---|---|
| [GSM2362797](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362797) | set2 deletion | SRR4457475, SRR4457476, SRR4457477, SRR4457478 |
| [GSM2362798](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362798) | set2 deletion | SRR4457479, SRR4457480, SRR4457481, SRR4457482 |
| [GSM2362799](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362799) | set2 deletion | SRR4457483, SRR4457484, SRR4457485, SRR4457486 |
| [GSM2362794](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362794) | wild type | SRR4457463, SRR4457464, SRR4457465, SRR4457466 |
| [GSM2362795](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362795) | wild type | SRR4457467, SRR4457468, SRR4457469, SRR4457470 |
| [GSM2362796](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2362796) | wild type | SRR4457471, SRR4457472, SRR4457473, SRR4457474 |

Checked 2026-11-15. Complete reference-file SHA-256: `b783572da8b31661f49b4bbbf8daad7def5efd23d27a683c53abd78477db166c`.
Eligible distinct IDs: up=2,613, down=2,825. The JSON has exactly 100 different genes per direction, with no overlap. No DEG analysis was rerun.

## Reference provenance and migration

- Previous source study: `study_08`; previous task: `task_011`.
- Previous reference filename: `GSE89238_SET2_KO_DESeq2_output__set2_KO_vs_WT_top100.json`.
- Author input path in the unchanged [extractor](../extract_reference.py): `study_08/author_results/GSE89238_SET2_KO_DESeq2_output.txt.gz`.
- Extraction columns: ID `gene_id`, log2FC `log2FoldChange`, adjusted P `padj`; no status column configured.
- Existing extraction direction multiplier: retained (+1), giving treated / untreated. This refactor does not apply another sign change.
- Reviewed author input SHA-256: `b783572da8b31661f49b4bbbf8daad7def5efd23d27a683c53abd78477db166c`.
- Migrated JSON SHA-256: `c750fe06e62d52d90190d95e64afed273d2b5bab68ef0950651a7823224422cb`.

The existing JSON was copied byte-for-byte; no DEG analysis, extraction, sorting, or ID conversion was rerun. The common [extraction rules and legacy-layout caveat](../README.md#reference-extraction-and-compatibility) apply.
