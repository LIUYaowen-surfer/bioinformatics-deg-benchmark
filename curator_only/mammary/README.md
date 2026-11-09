# Fu et al. 2015 / dataset_03

论文：[EGF-mediated Induction of Mcl-1 at the Switch to Lactation Is Essential for Alveolar Cell Survival](https://doi.org/10.1038/ncb3117)，PMID 25730472。[作者机构保存的接收稿](https://publications.wehi.edu.au/document/127) 已阅读结果“Identification of EGF…”、Figure 6 图注、RNA-seq analysis、Accession number；PDF 第 31 页的方法已渲染目视核验。论文明确给出 [GSE60450](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60450)。

Mus musculus、FVB/N、野生型雌鼠乳腺分选 luminal 与 basal 细胞。virgin、妊娠 18.5 d、泌乳 2 d，每阶段两只小鼠/独立取样，每个细胞类型阶段组合两列，共 12 列；不能称为 12 只独立小鼠。目标选 luminal 妊娠和泌乳的四列，每组两份独立生物学样本；不是相同小鼠的纵向配对。跨细胞类型的确切同鼠配对未编码，不能据 #1/#2 自行建立。

作者提交 `GSE60450_Lactation-GenewiseCounts.txt.gz`，27,179 × 12；EntrezGeneID 与非计数 Length 列。GEO 记载 mm10 / GRCm38，Subread 1.4.4、Rsubread featureCounts、NCBI 注释。论文对 Rsubread 版本的写法与 GEO 不一致，精确历史软件版本按来源各自记录，不用于本次重新计数。计数由作者提交；没有换成第三方矩阵。

样本映射以 GEO Sample_description 中完整矩阵列字符串精确匹配，绝非依据 MCL1 前缀猜条件。原 Length 单独无损导出到 `features.tsv.gz`。全部 12 列保留，任务样本以 use_primary 标注。所有原始文件批次日期为 2013-08-09；更细的制备批次待核实。测序类型以论文 SINGLE-end 方法和 ENA 全部 12 个 SINGLE run 交叉确认；某教学网页称 paired-end，与一手记录不一致，不采纳该说法。

任务覆盖 Figure 6 中阶段转录组的很小一部分，不能从 mRNA 比较推出 EGF–Mcl-1 翻译机制或存活因果结论。该数据也被 edgeR 等教程广泛使用，存在公开基线曝光，不能视为全新隐蔽测试集。

状态：可直接进入 luminal 阶段比较出题，评分软件与阈值仍须固定。输入 `../../model_input/dataset_03/`；原始文件与来源校验见 `original/`、`provenance.tsv`。
