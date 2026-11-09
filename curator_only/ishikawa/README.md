# Vahrenkamp et al. 2018 / dataset_02

论文：[Clinical and Genomic Crosstalk between Glucocorticoid Receptor and Estrogen Receptor α in Endometrial Cancer](https://pubmed.ncbi.nlm.nih.gov/29539426/)，DOI 10.1016/j.celrep.2018.02.076。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5870123/) 的 Cell Culture、RNA-Seq、Figure 6 及 DATA AND SOFTWARE AVAILABILITY 已核查。论文给出总系列 GSE109893；[GSE109892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109892) 是 RNA-seq 子系列，并列 PMID 29539426。

对象为 Homo sapiens Ishikawa 子宫内膜癌细胞系。8 个样本：DMSO、10 nM E2、100 nM Dex、两者联合，各有来源标注的重复 1/2。RNA-seq 处理为 8 h，覆盖 Figure 6 的表达响应部分。GEO 通用 treatment protocol 写 1 h，与其样本 characteristics 及论文区分 RNA-seq 8 h 的写法冲突；8 h 的采用依据与冲突均保留。

作者提交未标准化基因计数 `GSE109892_Ishi_RNAseq_allsets_raw.counts.txt.gz`，26,364 × 8；第一列 Geneid 为基因符号式标签，不能擅自宣称是稳定 Ensembl/Entrez ID。GEO 说明 HISAT2 2.0.4、featureCounts 1.5.1、hg19。未把另列的 normalized.counts 文件作为输入。ENA 支持每个 GSM 对应的实验有一个 SINGLE run；这些 run 数量不能单独证明生物学独立性。

7 列可通过矩阵列名 + _RNA_seq 与 GEO title 大小写敏感地精确连接。最后一列 `Ishi_Dex_E2_1` 无对应标题；GSM2973408 标为 `Ishi_Dex_E2_2_RNA_seq`。它是可能的列名笔误，但仅凭集合差不能证明，故保留原列名、原值，GSM 映射与分组标待核实，记录候选而不改名。另一联合处理列 `IshI_Dex_E2_1` 有明确对应。两列均不进入建议任务。

E2 / DMSO 和 Dex / DMSO 各 2 对 2 的列均明确；两题共享两个 DMSO 样本。GEO 只写 replicate，已读方法未明确其为独立培养还是技术重复；批次、跨条件阻断信息也未提供。不能把 1/2 直接作 paired donor，也不能把 8 个文库声称为 8 个不同供者。

状态：全计数已获取核对，单处理比较可起草；正式评分前需明确重复独立性。联合处理比较暂缓。输入 `../../model_input/dataset_02/`；来源、未经修正的列和映射证据见 `original/`、`sample_crosswalk.tsv`、`provenance.tsv`。本题不涉及患者临床关联、ChIP/ATAC 或体内表型。
