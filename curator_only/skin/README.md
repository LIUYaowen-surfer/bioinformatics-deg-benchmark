# Lili et al. 2019 / dataset_01

论文：[Transcriptomic Network Interactions in Human Skin Treated with Topical Glucocorticoid Clobetasol Propionate](https://doi.org/10.1016/j.jid.2019.04.021)，PMID 31247200。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6814545/) 的 Human skin biopsies、RNASeq data analysis 与 DATA AVAILABILITY 已核查。数据声明明确引用 [GSE120783](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120783)。GEO 的 citation 字段为较早的 PMID 28259685；这不等于选定论文错误，须保留双向证据。

目标对应论文初始全层皮肤转录组比较（Figure 1），不是后续细胞干预或网络实验。17 位健康受试者各提供处理和未处理取样，共 34 列；0.05% clobetasol propionate 单次处理，24 h，右上臂处理、左上臂对照。物种 Homo sapiens。生物学单位为受试者；论文中的 qRT-PCR 技术重复不属于本计数矩阵。

计数为作者提交的 `GSE120783_raw_read_counts.txt.gz`；数据库说明为 STAR / HTSeq 得到的基因计数。全文与 GEO 均支持其与标准化文件分开存在；未获取或使用 VST 文件。完整矩阵 58,302 基因 × 34 样本；Ensembl gene ID 为主键。原文件的 Gene name 单独无损保存到模型的 features 文件。

矩阵列去掉末尾 .fq.gz 或 .fastq.gz 后与 GSM title 精确匹配；配对来自 GEO `individual`，不是相邻列、HS 编号或推断性别。17 个配对均一对一。`sample_crosswalk.tsv` 保留所有映射；`geo_samples.json` 为 SOFT 的无损字段解析视图。

问题：主基因 ID 完整且唯一，但 Gene name 有重复，不能按 symbol 静默合并。原文称 Ensembl 91，GEO 处理说明称 Ensembl 92，计数文件的精确注释版本待核实；不改 ID。论文模型含批次与人口学协变量，GEO 未提供逐样本批次/年龄/性别映射；补充 Table S1 的 xlsx 下载被服务器拒绝，未据文件名补齐。受试者配对可用于简单任务，但不能声称严格复刻论文调整模型或论文统计结果。

状态：原始计数和样本已获取；可进入配对 DEG 任务起草。固定评分前需决定如何处理未知批次。原始数据、SHA-256 及来源见 `original/`、`provenance.tsv`；输入见 `../../model_input/dataset_01/`。
