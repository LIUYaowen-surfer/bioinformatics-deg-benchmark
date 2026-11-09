"""Write curation documentation and task drafts; never computes DEG results."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def put(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n',encoding='utf-8')

COMMON_TASK='''
输入为本目录的 `counts.tsv.gz` 与 `samples.tsv`。矩阵第一列是 `gene_id`，其余列全部是未标准化计数。仅选取本题指定的样本；提交时记录实际采用的样本列。`samples.tsv` 已按矩阵顺序排列；仍须检验一一对应。

预期输出：逐基因表，至少包含 `gene_id`、`log2_fold_change`、`p_value`、`adjusted_p_value`、`test_status`；另附比较方向、实际设计、采用的软件与版本、未检验基因的原因和简短结果解释。正的 log2 fold change 表示本题指定的目标条件表达更高。不要把未检验或无法估计的值改为 0，不要只交显著基因。

这是待定稿任务草案，尚无标准答案。本次整理没有运行 DEG。统计方法、软件版本、显著性阈值、效应量阈值、低表达处理、多重检验范围、异常值处理、LFC 收缩和数值评分容差均须在评分前固定；请勿自行将一套默认设置视为既定评分标准。
'''

MODEL={
'dataset_01':('皮肤处理的配对表达比较','''比较 `use_primary=true` 的全部 34 个样本，以 `clobetasol` 为目标、`untreated` 为参照。方向为 log2(clobetasol / untreated)。同一 `subject_id` 的两列是一位受试者的不同皮肤取样，应考虑 17 位受试者的配对，例如受试者效应加处理效应。数字或 individual 前缀是原注释的一部分，不能将缺号补成新受试者。批次未核实；不要从文件名推断批次。若需加入受试者内不变的年龄、性别等变量，应检查它们与受试者效应的可辨识性。

范围仅为健康受试者全层皮肤在该时间点的处理相关基因表达变化。不能据此确认直接受体靶点、转录因子调控网络、特定细胞类型的效应、临床疗效或长期皮肤老化机制。'''),
'dataset_02':('细胞系单一激素与溶剂对照','''主任务：仅用 `use_primary=true` 的 4 列，比较 `E2` 与 `DMSO`，方向为 log2(E2 / DMSO)。可单独制定第二题：仅用 `use_secondary=true` 的 4 列，比较 `Dex` 与 `DMSO`，方向为 log2(Dex / DMSO)。每个条件各有两个来源记录中的重复编号。两个任务共享 DMSO 对照，不应当作完全独立的数据集拆分训练与测试。

目前没有证据将重复编号 1/2 当作配对受试者或已确认批次，不能直接加入“配对”项。重复是否为独立生物学培养仍待核实，正式评分应先解决这一点。联合处理列全部保留，但不属于以上两题；其中一个列的样本对应关系未确定，禁止把它当作任一单处理重复。8 小时来自论文与样本特征字段，通用处理说明存在时间冲突。

范围仅为该细胞系的表达响应。不能单凭这些比较推出患者生存、体内子宫增生、受体共占位或两种激素的相互作用机制。'''),
'dataset_03':('乳腺 luminal 细胞的阶段比较','''仅用 `use_primary=true` 的 4 列，即 `cell_type=luminal` 且 `stage` 为 `pregnancy_18.5d` 或 `lactation_2d`。方向为 log2(lactation_2d / pregnancy_18.5d)。每阶段两个独立生物学样本。保留的 virgin 与 basal 样本不进入本题。重复编号 #1/#2 不表示跨阶段的同一只小鼠，不能设为配对。基因长度在 `features.tsv.gz`，不属于计数列。

范围仅为该分选细胞群两阶段的基因表达差异。不能从 mRNA 差异直接证明蛋白翻译调控、特定因子的必需性、细胞存活或干预造成的因果机制。每组仅两例，解释应受此限制。'''),
'dataset_04':('气道平滑肌细胞的供者配对比较','''使用全部 8 列，比较 `dexamethasone` 与 `untreated`，方向为 log2(dexamethasone / untreated)。同一 `subject_id` 对应同一供者来源的细胞系，应考虑四位供者的配对，例如供者效应加处理效应。所有提供样本均无 albuterol 处理。成对测序的两端不是两个独立样本，也不能把同一供者的两条件当作两个独立供者。

范围仅为这四位供者来源细胞的地塞米松响应。不能直接证明某基因调控细胞因子的机制、哮喘临床疗效、遗传变异效应或其他细胞类型中的响应。'''),
'dataset_05':('pasilla 敲低的基因层面表达比较','''使用全部 7 列，比较 `pasilla_knockdown` 与 `untreated`，方向为 log2(pasilla_knockdown / untreated)。包内注释定义 3 个敲低样本和 4 个对照样本。应考虑 `sequencing_type` 的单端／双端差异，例如测序类型加处理效应，并检查设计可辨识性。`number_of_lanes` 是来源记录的技术测序信息，不能展开为独立生物重复或充当配对变量。列名和原注释名存在明确的 fb 后缀关系，已保留两者。

样本分组在所提供整理版中可核实；这些列到原始实验记录的完整交叉映射仍待核实。本题可用于公开流程调试，正式评审前应解决来源差异。范围仅为基因总表达，不能以本题答案替代可变剪接、外显子使用、RNA 调控图谱或跨物种保守性结论。''')
}
for id,(title,body) in MODEL.items():
 put(f'model_input/{id}/task.md',f'# 任务草案：{title}\n\n'+body+'\n'+COMMON_TASK)
 put(f'model_input/{id}/README.md',f'''# {id}

本目录提供现成的基因计数及分析所需注释，任务见 [task.md](task.md)。未进行标准化、过滤、插补、统计检验或 DEG 分析。

- `counts.tsv.gz`：UTF-8、制表符分隔、gzip 压缩；第一列 `gene_id`，其余为完整样本集合的非负整数计数；行列顺序保留。
- `samples.tsv`：`matrix_column` 与计数列严格同序；`original_sample_id` 保留来源编号；`group`、`use_primary`、`use_secondary` 指定分组和建议任务样本。
- `subject_id` 仅在有配对证据时提供；`biological_replicate` 的含义以 `replicate_type` 和任务说明为准。数字相同不自动形成配对。
- `NA` 表示此简化任务不适用或未提供；`待核实` 与 `metadata_status` 表示明确未解决的来源信息，不是新分组。
- 若有 `features.tsv.gz`，它是从来源文件无损分离的基因附加注释，不能作为计数列。

模型不需要访问评审目录；论文身份、原始文件、来源和核查记录由评审材料单独维护。''')

DOCS={
'skin':'''# Lili et al. 2019 / dataset_01

论文：[Transcriptomic Network Interactions in Human Skin Treated with Topical Glucocorticoid Clobetasol Propionate](https://doi.org/10.1016/j.jid.2019.04.021)，PMID 31247200。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6814545/) 的 Human skin biopsies、RNASeq data analysis 与 DATA AVAILABILITY 已核查。数据声明明确引用 [GSE120783](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120783)。GEO 的 citation 字段为较早的 PMID 28259685；这不等于选定论文错误，须保留双向证据。

目标对应论文初始全层皮肤转录组比较（Figure 1），不是后续细胞干预或网络实验。17 位健康受试者各提供处理和未处理取样，共 34 列；0.05% clobetasol propionate 单次处理，24 h，右上臂处理、左上臂对照。物种 Homo sapiens。生物学单位为受试者；论文中的 qRT-PCR 技术重复不属于本计数矩阵。

计数为作者提交的 `GSE120783_raw_read_counts.txt.gz`；数据库说明为 STAR / HTSeq 得到的基因计数。全文与 GEO 均支持其与标准化文件分开存在；未获取或使用 VST 文件。完整矩阵 58,302 基因 × 34 样本；Ensembl gene ID 为主键。原文件的 Gene name 单独无损保存到模型的 features 文件。

矩阵列去掉末尾 .fq.gz 或 .fastq.gz 后与 GSM title 精确匹配；配对来自 GEO `individual`，不是相邻列、HS 编号或推断性别。17 个配对均一对一。`sample_crosswalk.tsv` 保留所有映射；`geo_samples.json` 为 SOFT 的无损字段解析视图。

问题：主基因 ID 完整且唯一，但 Gene name 有重复，不能按 symbol 静默合并。原文称 Ensembl 91，GEO 处理说明称 Ensembl 92，计数文件的精确注释版本待核实；不改 ID。论文模型含批次与人口学协变量，GEO 未提供逐样本批次/年龄/性别映射；补充 Table S1 的 xlsx 下载被服务器拒绝，未据文件名补齐。受试者配对可用于简单任务，但不能声称严格复刻论文调整模型或论文统计结果。

状态：原始计数和样本已获取；可进入配对 DEG 任务起草。固定评分前需决定如何处理未知批次。原始数据、SHA-256 及来源见 `original/`、`provenance.tsv`；输入见 `../../model_input/dataset_01/`。
''',
'ishikawa':'''# Vahrenkamp et al. 2018 / dataset_02

论文：[Clinical and Genomic Crosstalk between Glucocorticoid Receptor and Estrogen Receptor α in Endometrial Cancer](https://pubmed.ncbi.nlm.nih.gov/29539426/)，DOI 10.1016/j.celrep.2018.02.076。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5870123/) 的 Cell Culture、RNA-Seq、Figure 6 及 DATA AND SOFTWARE AVAILABILITY 已核查。论文给出总系列 GSE109893；[GSE109892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109892) 是 RNA-seq 子系列，并列 PMID 29539426。

对象为 Homo sapiens Ishikawa 子宫内膜癌细胞系。8 个样本：DMSO、10 nM E2、100 nM Dex、两者联合，各有来源标注的重复 1/2。RNA-seq 处理为 8 h，覆盖 Figure 6 的表达响应部分。GEO 通用 treatment protocol 写 1 h，与其样本 characteristics 及论文区分 RNA-seq 8 h 的写法冲突；8 h 的采用依据与冲突均保留。

作者提交未标准化基因计数 `GSE109892_Ishi_RNAseq_allsets_raw.counts.txt.gz`，26,364 × 8；第一列 Geneid 为基因符号式标签，不能擅自宣称是稳定 Ensembl/Entrez ID。GEO 说明 HISAT2 2.0.4、featureCounts 1.5.1、hg19。未把另列的 normalized.counts 文件作为输入。ENA 支持每个 GSM 对应的实验有一个 SINGLE run；这些 run 数量不能单独证明生物学独立性。

7 列可通过矩阵列名 + _RNA_seq 与 GEO title 大小写敏感地精确连接。最后一列 `Ishi_Dex_E2_1` 无对应标题；GSM2973408 标为 `Ishi_Dex_E2_2_RNA_seq`。它是可能的列名笔误，但仅凭集合差不能证明，故保留原列名、原值，GSM 映射与分组标待核实，记录候选而不改名。另一联合处理列 `IshI_Dex_E2_1` 有明确对应。两列均不进入建议任务。

E2 / DMSO 和 Dex / DMSO 各 2 对 2 的列均明确；两题共享两个 DMSO 样本。GEO 只写 replicate，已读方法未明确其为独立培养还是技术重复；批次、跨条件阻断信息也未提供。不能把 1/2 直接作 paired donor，也不能把 8 个文库声称为 8 个不同供者。

状态：全计数已获取核对，单处理比较可起草；正式评分前需明确重复独立性。联合处理比较暂缓。输入 `../../model_input/dataset_02/`；来源、未经修正的列和映射证据见 `original/`、`sample_crosswalk.tsv`、`provenance.tsv`。本题不涉及患者临床关联、ChIP/ATAC 或体内表型。
''',
'mammary':'''# Fu et al. 2015 / dataset_03

论文：[EGF-mediated Induction of Mcl-1 at the Switch to Lactation Is Essential for Alveolar Cell Survival](https://doi.org/10.1038/ncb3117)，PMID 25730472。[作者机构保存的接收稿](https://publications.wehi.edu.au/document/127) 已阅读结果“Identification of EGF…”、Figure 6 图注、RNA-seq analysis、Accession number；PDF 第 31 页的方法已渲染目视核验。论文明确给出 [GSE60450](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60450)。

Mus musculus、FVB/N、野生型雌鼠乳腺分选 luminal 与 basal 细胞。virgin、妊娠 18.5 d、泌乳 2 d，每阶段两只小鼠/独立取样，每个细胞类型阶段组合两列，共 12 列；不能称为 12 只独立小鼠。目标选 luminal 妊娠和泌乳的四列，每组两份独立生物学样本；不是相同小鼠的纵向配对。跨细胞类型的确切同鼠配对未编码，不能据 #1/#2 自行建立。

作者提交 `GSE60450_Lactation-GenewiseCounts.txt.gz`，27,179 × 12；EntrezGeneID 与非计数 Length 列。GEO 记载 mm10 / GRCm38，Subread 1.4.4、Rsubread featureCounts、NCBI 注释。论文对 Rsubread 版本的写法与 GEO 不一致，精确历史软件版本按来源各自记录，不用于本次重新计数。计数由作者提交；没有换成第三方矩阵。

样本映射以 GEO Sample_description 中完整矩阵列字符串精确匹配，绝非依据 MCL1 前缀猜条件。原 Length 单独无损导出到 `features.tsv.gz`。全部 12 列保留，任务样本以 use_primary 标注。所有原始文件批次日期为 2013-08-09；更细的制备批次待核实。测序类型以论文 SINGLE-end 方法和 ENA 全部 12 个 SINGLE run 交叉确认；某教学网页称 paired-end，与一手记录不一致，不采纳该说法。

任务覆盖 Figure 6 中阶段转录组的很小一部分，不能从 mRNA 比较推出 EGF–Mcl-1 翻译机制或存活因果结论。该数据也被 edgeR 等教程广泛使用，存在公开基线曝光，不能视为全新隐蔽测试集。

状态：可直接进入 luminal 阶段比较出题，评分软件与阈值仍须固定。输入 `../../model_input/dataset_03/`；原始文件与来源校验见 `original/`、`provenance.tsv`。
''',
'airway':'''# Himes et al. 2014 / dataset_04

论文：[RNA-Seq Transcriptome Profiling Identifies CRISPLD2 as a Glucocorticoid Responsive Gene that Modulates Cytokine Function in Airway Smooth Muscle Cells](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099625)，PMID 24926665。[GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778) 对应关系由全文 RNA-seq 方法、结果以及 airway 包说明共同确认。目标是初始地塞米松转录组实验，不是后续 CRISPLD2 敲低或细胞因子实验。

Homo sapiens，四位供者来源的原代气道平滑肌细胞；1 µM dexamethasone 18 h 与 untreated/vehicle 对照，每供者两列，共 8 列、四对。GEO 全系列有 16 个样本，另含 albuterol 和联合处理；本次下载的 airway 对象本来只含未加 albuterol 的 8 列，完整导出其全部样本，并非本次从 16 列计数裁剪而成。GEO 作者提交的 FPKM 和差异结果表不符合本题计数输入要求。

采用第三方 Michael Love 整理的 [airway](https://bioconductor.org/packages/3.23/data/experiment/html/airway.html) **1.32.0**，Bioconductor 3.23，commit deb0a4f；原始 source tar 保留。读取 `data/airway.RData` 中 airway 对象的 counts assay：63,677 × 8，Ensembl gene ID。包 vignette 说明这批历史计数来自 STAR、GRCh37 / Ensembl 75 与 summarizeOverlaps Union；不是论文原始 Cufflinks/FPKM 流水线的数值复刻。包中另有 gse / Salmon 例子，本题不使用。

导出用 R 4.6.1 的 load 与基础属性读取，未安装或运行 DEG 软件。具体属性路径和 write.table 过程见 `../../scripts/export_airway.R`；`export_session.txt` 记录环境；导出后所有整数、基因 ID 和样本顺序已与对象精确回读相等。对象列名来自 colData，基因 ID 来自 rowRanges 的 names。

对象 colData 与包内 sample_table.csv 的八样本一致；Run ↔ GSM ↔ 供者编号 ↔ dex 标注逐一与当前 GEO 核对。包附 SRA 表确认成对测序，单个 run 的两端不是两个样本。保留 ERCC mix 注释，但不将其自动当作批次。当前重新渲染的网页 vignette 示例曾显示 16 行且 cell/dex 字段异常；未采用该网页运行输出覆盖稳定存储的八样本注释。

状态：可直接进入配对 DEG 出题，尤其适合流程调试/公开基线。此数据已有大量教学材料，文件分离不保证免于训练数据污染。输入 `../../model_input/dataset_04/`；原始包及导出谱系见 provenance。
''',
'pasilla':'''# Brooks et al. 2011 / dataset_05

论文：[Conservation of an RNA Regulatory Map between Drosophila and Mammals](https://doi.org/10.1101/gr.108662.110)，PMID 20921232。[全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3032923/) 的 Results、RNA interference、Deep sequencing 与数据存档部分已核查；相关原始记录属于 [GSE18508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE18508)，包说明引用 GSM461176–GSM461181。细胞为 Drosophila melanogaster S2-DRSC，比较 pasilla RNAi 敲低与未处理。

采用 Wolfgang Huber / Alejandro Reyes 第三方整理的 [pasilla 1.40.0](https://bioconductor.org/packages/3.23/data/experiment/html/pasilla.html)，Bioconductor 3.23，commit df6e823。直接从 source tar 提取 `inst/extdata/pasilla_gene_counts.tsv` 和 `pasilla_sample_annotation.csv`。完整基因矩阵 14,599 × 7，FlyBase FBgn ID；不是包内用于外显子演示的小型 DEXSeqDataSet，也不是由本次汇总外显子计数生成。

进一步获取 DESeq2 **1.52.0** source archive：其官方例子的 gzip 解压后与 pasilla gene TSV 逐字节一致，样本 CSV 也逐字节一致；仅比较文件，未运行 DESeq2。计数列与注释行以精确的列名 + fb 对接，随后只重排注释行；来源列顺序从未更改。[官方示例](https://bioconductor.org/packages/3.23/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) 明确描述此后缀和顺序差异。

包内分组为 3 个 treated、4 个 untreated 生物学重复；treated 有 1 个 single-read、2 个 paired-end，untreated 各 2 个。保留每样本 number of lanes，不把 lane 或 read mate 当作生物重复。包 vignette 记录历史 TopHat 1.2.0 / BDGP5.25.62，但现版本没有把基因 TSV 的完整历史计数命令单独列清；不把外显子生成脚本误称为基因矩阵的精确计数流程，确切 gene-count 工具/参数待核实。

来源差异：论文正文与 Table 1 脚注称 4 个敲低、3 个未处理，和包注释相反。GEO 所引用六个 GSM 只有 3 个未处理与 3 个敲低；第七列的原始映射不能凭后缀猜定。ENA 调查发现：untreated2 的总 reads/6 lanes 与 GSM461176 对应 run 总量一致；untreated1 的总量/2 runs 与 GSM461182 一致（在包引用的六 GSM 范围外）；其余候选见 crosswalk。这是支持追溯的推断，不是已确认映射。treated1 的包 lane 数与 ENA run 数也不同。保留矛盾，不擅改组别、不删除第七列、不声称其为重复测序合并。

状态：整理版可用于公开流程调试，正式 benchmark 准入需解决论文/原始记录映射与重复数差异。仅能提出基因总表达问题，不能复现论文的剪接调控图谱或跨物种机制结论。广泛教学曝光已标注。输入 `../../model_input/dataset_05/`；完整原文件和候选追溯见 original、sample_crosswalk 与 provenance。
'''
}
for ds,t in DOCS.items():put(f'curator_only/{ds}/README.md',t)

put('README.md','''# Bioinformatics DEG benchmark — 数据整理版

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
''')

put('curator_only/scoring_settings.md','''# 后续需要固定的评分设置

本次无 DEG 标准答案，无显著基因列表，也未运行统计分析。任务草案不是最终评分规范。

1. 每题的准入状态、确切样本清单、参照条件、配对/批次设计；Ishikawa 重复独立性、皮肤批次、pasilla 来源差异须先裁定。
2. 统计方法、软件/依赖版本与运行环境；是否允许多种合理方法及如何评分。
3. 低表达/全零基因策略、可检验基因集合、独立过滤、异常值与缺失结果的处理。
4. 归一化/offset、离散度估计、检验类型、零假设和协变量编码；这些只在未来分析阶段执行。
5. log2 fold change 方向、是否收缩、是否设效应量阈值、置信区间要求。
6. 多重检验校正方法、校正基因集合、显著性阈值；论文原阈值不会自动成为 benchmark 阈值。
7. 结果表字段、排序、ID 保持规则、浮点容差、NA/test_status、可复现代码和设计解释评分。
8. 评分只覆盖相应基因表达小题；不以完整机制、网络、临床结论或论文 DEG 数量作为正确答案。
9. 数据曝光与划分策略：教学数据主要用于公开基线；共享样本不能跨拆分泄漏。
''')
put('curator_only/review_log.md','''# 文献与来源核查记录

核查日 2026-11-09；所有选定论文保留，没有替换。

| 数据 | 已读一手材料 / 定位 | 用途与限制 |
|---|---|---|
| skin | PMC6814545：Human skin biopsies、RNASeq data analysis、Figure 1、DATA AVAILABILITY；GSE120783 family SOFT | 确认论文关系与配对；PMC 普通下载受到 403/验证码限制，已通过网页检索所提供的全文章节核查；Table S1 下载未成功 |
| ishikawa | PMC5870123：Cell Culture、RNA-Seq、Figure 6、DATA AND SOFTWARE AVAILABILITY；GSE109892 SOFT；ENA PRJNA432245 | 核实子系列和处理时间，保留通用 protocol 的 1 h 冲突；未获得明确生物重复定义 |
| mammary | WEHI 作者接收稿：PDF 第9页结果、第24页 Figure 6 图注、第31页 RNA-seq、第33页 accession；GSE60450 SOFT；ENA PRJNA258286 | PDF 第31页渲染目视确认 single-end；原始列字符串与样本描述精确匹配 |
| airway | PLOS 原文结果、RNA-seq 方法及 GEO 存档信息；GSE52778 SOFT；airway DESCRIPTION、RData、样本表、SRA 表、vignette | 明确第三方再处理，区分 GEO 16 样本与对象已有8样本；不采用重新渲染网页的错误示例注释 |
| pasilla | PMC3032923 Results、Table 1、Methods、存档信息；GSE18508 SOFT；pasilla 1.40.0、DESeq2 1.52.0 源码包；ENA SRP001537 | 保留论文4/3与包3/4冲突；官方例子与包文件逐字节核对；候选 GSM 推断未升级为事实 |

原论文和教程中现成 DEG 结果未进入模型输入，也没有被用来生成答案。只读论文的原始分析方法用于确认数据性质，并未执行。

`documentation_sources.json` 是本地文档下载尝试清单：其中 200 下载可能仍是验证码页；不是内容已核查的自动证明。本表和逐篇 README 才是人工核查状态。缓存 `_work/` 不提交；可核实事实以对应链接、已保存数据库记录和包文件为证。
''')
put('THIRD_PARTY_NOTICES.md','''# 来源、再分发与许可记录

核查日期 2026-11-09。下列是数据整理采用的来源条件，不将整仓库重新授权为一个统一数据许可证。

| 材料 | 条件 / 处理 |
|---|---|
| GEO 作者提交计数、SOFT 和样本事实 | [NCBI Molecular Data Usage](https://www.ncbi.nlm.nih.gov/home/about/policies/#data) 说明 NCBI 本身不限制分子数据的使用或分发，也不接受提交者要求限制再利用/再分发的数据；同时不替提交者转让知识产权。所检查记录未发现额外限制。保留来源、作者、accession 和原文件；不宣称这些数据由本仓库授予无限制新许可。 |
| airway 1.32.0 | DESCRIPTION 声明 LGPL，原始包与声明原样保留；发布者 Michael Love，源 https://git.bioconductor.org/packages/airway 。|
| pasilla 1.40.0 | DESCRIPTION 声明 LGPL，原始包与声明原样保留；发布者 Wolfgang Huber / Alejandro Reyes，源 https://git.bioconductor.org/packages/pasilla 。|
| DESeq2 1.52.0 参考文件 | DESCRIPTION 声明 LGPL (>= 3)；仅作为官方示例文件的核对来源，未安装或运行。源 https://git.bioconductor.org/packages/DESeq2 。|
| ENA 公开运行元数据 | [EMBL-EBI Terms of use](https://www.ebi.ac.uk/about/terms-of-use/)；仅保存公开测序运行注释，保留来源 URL 与原响应，尊重原数据的归属。|
| 论文正文/补充结果 | 未再分发全文或结果附表；链接回出版方/机构库/PMC。论文可阅读不自动等于可任意再分发。 |

`LICENSES/` 附 LGPL-2、LGPL-2.1、LGPL-3 与 GPL-3 文本供查阅；两个数据包只标 LGPL、没有明确主版本，因此保留该不确定性，不擅自改为特定版本。压缩原包属于对应源码的原样分发；导出说明见每篇 provenance。

GitHub 文件限制核查：[About large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)：Git 对超过 50 MiB 的文件提示，超过 100 MiB 阻止。仓库验证脚本在上传前检查全部提交文件；本次所有单文件都低于 50 MiB。原始计数没有因体积限制省略。

本次新编的整理脚本与说明没有代表作者更改第三方数据许可；后续若公开发布 benchmark，应继续保留原作者归属、已知数据缺陷和来源条款。
''')
put('.gitignore','''_work/
__pycache__/
*.pyc
_delivery_verification/
''')
put('.gitattributes','''# Preserve original bytes and checksum reproducibility on every platform.
* -text
''')
print('Documentation and five task drafts written; no DEG computation.')
