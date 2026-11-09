# dataset_04

本目录提供现成的基因计数及分析所需注释，任务见 [task.md](task.md)。未进行标准化、过滤、插补、统计检验或 DEG 分析。

- `counts.tsv.gz`：UTF-8、制表符分隔、gzip 压缩；第一列 `gene_id`，其余为完整样本集合的非负整数计数；行列顺序保留。
- `samples.tsv`：`matrix_column` 与计数列严格同序；`original_sample_id` 保留来源编号；`group`、`use_primary`、`use_secondary` 指定分组和建议任务样本。
- `subject_id` 仅在有配对证据时提供；`biological_replicate` 的含义以 `replicate_type` 和任务说明为准。数字相同不自动形成配对。
- `NA` 表示此简化任务不适用或未提供；`待核实` 与 `metadata_status` 表示明确未解决的来源信息，不是新分组。
- 若有 `features.tsv.gz`，它是从来源文件无损分离的基因附加注释，不能作为计数列。

模型不需要访问评审目录；论文身份、原始文件、来源和核查记录由评审材料单独维护。
