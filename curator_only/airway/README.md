# Himes et al. 2014 / dataset_04

论文：[RNA-Seq Transcriptome Profiling Identifies CRISPLD2 as a Glucocorticoid Responsive Gene that Modulates Cytokine Function in Airway Smooth Muscle Cells](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099625)，PMID 24926665。[GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778) 对应关系由全文 RNA-seq 方法、结果以及 airway 包说明共同确认。目标是初始地塞米松转录组实验，不是后续 CRISPLD2 敲低或细胞因子实验。

Homo sapiens，四位供者来源的原代气道平滑肌细胞；1 µM dexamethasone 18 h 与 untreated/vehicle 对照，每供者两列，共 8 列、四对。GEO 全系列有 16 个样本，另含 albuterol 和联合处理；本次下载的 airway 对象本来只含未加 albuterol 的 8 列，完整导出其全部样本，并非本次从 16 列计数裁剪而成。GEO 作者提交的 FPKM 和差异结果表不符合本题计数输入要求。

采用第三方 Michael Love 整理的 [airway](https://bioconductor.org/packages/3.23/data/experiment/html/airway.html) **1.32.0**，Bioconductor 3.23，commit deb0a4f；原始 source tar 保留。读取 `data/airway.RData` 中 airway 对象的 counts assay：63,677 × 8，Ensembl gene ID。包 vignette 说明这批历史计数来自 STAR、GRCh37 / Ensembl 75 与 summarizeOverlaps Union；不是论文原始 Cufflinks/FPKM 流水线的数值复刻。包中另有 gse / Salmon 例子，本题不使用。

导出用 R 4.6.1 的 load 与基础属性读取，未安装或运行 DEG 软件。具体属性路径和 write.table 过程见 `../../scripts/export_airway.R`；`export_session.txt` 记录环境；导出后所有整数、基因 ID 和样本顺序已与对象精确回读相等。对象列名来自 colData，基因 ID 来自 rowRanges 的 names。

对象 colData 与包内 sample_table.csv 的八样本一致；Run ↔ GSM ↔ 供者编号 ↔ dex 标注逐一与当前 GEO 核对。包附 SRA 表确认成对测序，单个 run 的两端不是两个样本。保留 ERCC mix 注释，但不将其自动当作批次。当前重新渲染的网页 vignette 示例曾显示 16 行且 cell/dex 字段异常；未采用该网页运行输出覆盖稳定存储的八样本注释。

状态：可直接进入配对 DEG 出题，尤其适合流程调试/公开基线。此数据已有大量教学材料，文件分离不保证免于训练数据污染。输入 `../../model_input/dataset_04/`；原始包及导出谱系见 provenance。
