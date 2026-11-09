# Bioinformatics DEG benchmark — 数据整理版

核查/获取日期：2026-11-09（Asia/Shanghai；各次获取的 UTC 时间见 provenance）。本仓库实际保存五套现成未标准化基因计数，以及所需注释与任务草案。**未运行 DEG、未处理 FASTQ、未比对或重新计数，也未生成标准答案。**

| 论文 / 入口 | 获取与核查状态 | 完整矩阵（基因×样本） | 建议比较 / 样本数 | 输入 / 评审材料 | 尚未解决 / 出题适用性 |
|---|---|---:|---|---|---|
| Lili 2019 / GSE120783 | 作者计数和 GEO 注释已获取，34 列映射完成 | 58,302×34 | clobetasol vs untreated；17 对 | [dataset_01](model_input/dataset_01/) / [核查](curator_only/skin/) | 可起草配对题；批次与人口学逐样本表未取得，Ensembl 91/92 冲突 |
| Vahrenkamp 2018 / GSE109892 | 全计数已获取；单处理目标列明确 | 26,364×8 | E2 vs DMSO：2+2；Dex vs DMSO：2+2 | [dataset_02](model_input/dataset_02/) / [核查](curator_only/ishikawa/) | 可起草；生物/技术重复性质待核实；一联合处理列 GSM 未确认，暂缓联合处理题 |
| Fu 2015 / GSE60450 | 作者计数和 12 列映射已核实 | 27,179×12 | luminal 泌乳 2 d vs 妊娠 18.5 d：2+2 | [dataset_03](model_input/dataset_03/) / [核查](curator_only/mammary/) | 可直接进入出题；不做跨阶段配对；已有教程曝光 |
| Himes 2014 / airway | 第三方包 1.32.0 全 assay 导出，数值及 4 对供者核对通过 | 63,677×8 | dexamethasone vs untreated：4 对 | [dataset_04](model_input/dataset_04/) / [核查](curator_only/airway/) | 可直接进入配对题；适合调试/公开基线；GEO 全系列另有未纳入本对象的 8 样本 |
| Brooks 2011 / pasilla | 第三方包 1.40.0；与 DESeq2 1.52.0 官方例子计数/注释逐字节相同 | 14,599×7 | pasilla knockdown vs untreated：3+4（依包注释） | [dataset_05](model_input/dataset_05/) / [核查](curator_only/pasilla/) | 可作公开调试基线；正式准入前解决重复数矛盾、原始 GSM 映射与基因计数历史细节 |

所有矩阵主基因 ID 和列名均无缺失/重复，计数为非负整数且无缺失；未删除全零基因。皮肤 Gene name 有重复，仅作为附加注释保留，不合并。逐项维度、检查和未决注释见 [qc_summary.json](curator_only/qc_summary.json)。

## 内容边界

`model_input/` 只含计数、完成任务必需的样本注释、附加基因注释和题目草案；`curator_only/` 保存论文身份、文献对应、原始下载、处理谱系、候选映射与问题记录。部署模型评测时只提供指定输入目录；不要把整个仓库挂载给被评模型。保留的样本 ID、基因分布以及公开教程仍可识别数据，**目录分离不保证没有训练数据污染**。airway、pasilla 和 GSE60450 有明显教学曝光；其中两个 Ishikawa 对比共享对照，也不应跨训练/测试集分拆制造独立性。

## 文件与复现

每套输入包含 `counts.tsv.gz`、`samples.tsv`、`README.md`、`task.md`。每篇的 `curator_only/<name>/` 有 README、`provenance.tsv`、`qc.json`、`sample_crosswalk.tsv` 和 `original/`。原始下载文件未覆盖或改动。无损导出只是分离注释列、读取已有对象、改 TSV 表头/压缩格式、对齐注释行；不涉及重新计数。

- [完整原始来源清单](curator_only/download_manifest.tsv) 和 [全仓库 SHA-256 清单](SHA256SUMS.tsv)。
- 以下命令从仓库根目录运行。`python scripts/restore_sources.py` 可从清单恢复缺少的原始文件，严格核验原始校验值，拒绝覆盖不符文件。
- `python scripts/inspect_inputs.py` 提取包到忽略目录；`Rscript scripts/export_airway.R` 导出 airway；`python scripts/prepare.py` 整理其他计数与注释；`python scripts/write_docs.py` 写文档；`python scripts/finalize.py` 更新谱系与校验清单。
- `python scripts/validate.py` 验证校验值、矩阵/样本对应、计数导出一致性和体积限制；不运行任何表达分析。Python 下载需 requests；已完成数据导出只使用 Python 标准库与 R 基础功能。
- [后续评分设置](curator_only/scoring_settings.md) 全部待固定，不沿用论文显著基因清单作为答案。

## 再分发与未上传材料

依据 NCBI molecular data usage 规则，GEO 无明确额外限制的公开分子数据按原来源与署名保留；Bioconductor 包及派生数据遵循各自 LGPL 声明，未替第三方数据换发新许可证。详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。所有实际提交文件均低于 GitHub 50 MiB 提示线和 100 MiB 硬限制；没有 LFS 指针或伪装成数据的占位文件。

五套计数均实际上传。未上传论文全文、论文结果附表和本地研究缓存；仅保留链接、阅读记录与必要事实。皮肤补充样本表未能下载，明确记录为缺失。原 airway tar 原样包含发布者附带的 BAM/Salmon 教学素材，但本次既未使用也未处理，模型输入只含已有基因计数。完整矩阵是各下载来源的完整样本集合，不能误解为每篇所有实验的全部数据。
