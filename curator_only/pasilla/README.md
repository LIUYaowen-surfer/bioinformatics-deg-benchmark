# Brooks et al. 2011 / dataset_05

论文：[Conservation of an RNA Regulatory Map between Drosophila and Mammals](https://doi.org/10.1101/gr.108662.110)，PMID 20921232。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3032923/) 的 Results、RNA interference、Deep sequencing 与数据存档部分已核查；相关原始记录属于 [GSE18508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE18508)，包说明引用 GSM461176–GSM461181。细胞为 Drosophila melanogaster S2-DRSC，比较 pasilla RNAi 敲低与未处理。

采用 Wolfgang Huber / Alejandro Reyes 第三方整理的 [pasilla 1.40.0](https://bioconductor.org/packages/3.23/data/experiment/html/pasilla.html)，Bioconductor 3.23，commit df6e823。直接从 source tar 提取 `inst/extdata/pasilla_gene_counts.tsv` 和 `pasilla_sample_annotation.csv`。完整基因矩阵 14,599 × 7，FlyBase FBgn ID；不是包内用于外显子演示的小型 DEXSeqDataSet，也不是由本次汇总外显子计数生成。

进一步获取 DESeq2 **1.52.0** source archive：其官方例子的 gzip 解压后与 pasilla gene TSV 逐字节一致，样本 CSV 也逐字节一致；仅比较文件，未运行 DESeq2。计数列与注释行以精确的列名 + fb 对接，随后只重排注释行；来源列顺序从未更改。[官方示例](https://bioconductor.org/packages/3.23/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) 明确描述此后缀和顺序差异。

包内分组为 3 个 treated、4 个 untreated 生物学重复；treated 有 1 个 single-read、2 个 paired-end，untreated 各 2 个。保留每样本 number of lanes，不把 lane 或 read mate 当作生物重复。包 vignette 记录历史 TopHat 1.2.0 / BDGP5.25.62，但现版本没有把基因 TSV 的完整历史计数命令单独列清；不把外显子生成脚本误称为基因矩阵的精确计数流程，确切 gene-count 工具/参数待核实。

来源差异：论文正文与 Table 1 脚注称 4 个敲低、3 个未处理，和包注释相反。GEO 所引用六个 GSM 只有 3 个未处理与 3 个敲低；第七列的原始映射不能凭后缀猜定。ENA 调查发现：untreated2 的总 reads/6 lanes 与 GSM461176 对应 run 总量一致；untreated1 的总量/2 runs 与 GSM461182 一致（在包引用的六 GSM 范围外）；其余候选见 crosswalk。这是支持追溯的推断，不是已确认映射。treated1 的包 lane 数与 ENA run 数也不同。保留矛盾，不擅改组别、不删除第七列、不声称其为重复测序合并。

状态：整理版可用于公开流程调试，正式 benchmark 准入需解决论文/原始记录映射与重复数差异。仅能提出基因总表达问题，不能复现论文的剪接调控图谱或跨物种机制结论。广泛教学曝光已标注。输入 `../../model_input/dataset_05/`；完整原文件和候选追溯见 original、sample_crosswalk 与 provenance。
