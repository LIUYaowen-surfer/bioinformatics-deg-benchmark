# DEG 参考答案提取记录（top100）

仅提取作者现有结果，不重新运行 DEG。统一方向：处理组/对照组。
有 status 列时仅保留 OK；排除缺失 ID/log2FC/校正 P 值及 log2FC=0；不使用 significant、原始 P 值或额外显著性/倍数阈值。
分别按校正 P 值、原始 ID 字符串升序取前 K。Decimal 保留极小 P 值精度；版本号、逗号复合 ID、自定义 ID 不变。
±inf 不是缺失值，且有明确方向：在 status=OK、校正 P 值有效时按符号保留，不额外删除。
输入 SHA-256 已与作者公开文件逐字节核对；重跑脚本会核验已确认版本。重复 ID 或未配置比较会阻止相应比较进入正式答案。

## GSE52778_Dex_vs_Untreated_gene_exp.diff.gz

- 列：ID=`gene_id`；log2FC=`log2(fold_change)`；校正 P=`q_value`；检验状态=`status`。
- ID 类型：作者 gene_id：symbol 式标签，含逗号连接的复合 ID，均原样保留。
- 处理组：Dex；对照组：Untreated；标签：('Dex', 'Untreated')；翻转：True。
- 方向依据：文件内 sample_1=Dex、sample_2=Untreated；Cuffdiff 的 log2FC=log2(value_2/value_1)，故原方向是 Untreated/Dex。13,370 个 OK 且两侧表达量为正的有限值行通过数值核对（绝对误差≤1e-4）；翻转符号。
- 行数 23,273；排除无效状态 9,760、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=7,292，down=6,221；有效 ±inf 共 0，入选 up/down 分别 0/0。
- 输出：`GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz)；SHA-256：`6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f`。

## GSE100732_DESeq2.results.txt.gz

- 列：ID=`__rowname__`；log2FC=`log2FoldChange`；校正 P=`padj`；检验状态=`无状态列`。
- ID 类型：原文件无表头的首列行名：带版本号的 ENSMUSG ID 与作者自定义线粒体 ID（例如 mt-Nd4l_4）。
- 处理组：Lrpprc knockout；对照组：wild type；标签：()；翻转：False。
- 方向依据：结果表未显式保存 contrast。通过作者现成 normalized-counts 表与 GEO 样本标注交叉核对：KO 列 55219/55221/55223/55233，WT 列 55225/55227/55229/55231。19,866/19,957 个有效基因的系数符号与 KO/WT 均值方向一致，两个方向最靠前的基因亦一致，确认整体方向为 KO/WT；不翻转。不用均值替换系数，不删除其余 91 行。
- 行数 50,599；排除无效状态 0、缺失 30,642、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=10,045，down=9,912；有效 ±inf 共 0，入选 up/down 分别 0/0。
- 输出：`GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz)；SHA-256：`0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df`。

## GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz

- 列：ID=`gene_id`；log2FC=`log2(fold_change)`；校正 P=`q_value`；检验状态=`status`。
- ID 类型：原始 ENSG gene_id，保留版本后缀。
- 处理组：si_SRSF1；对照组：si_CTRL；标签：('si_CTRL', 'si_SRSF1')；翻转：False。
- 方向依据：文件内 sample_1=si_CTRL、sample_2=si_SRSF1；按 Cuffdiff 定义为 si_SRSF1/si_CTRL。20,079 个 OK 且两侧表达量为正的有限值行通过 log2(value_2/value_1) 核对（绝对误差≤1e-4）；不翻转。
- 行数 58,698；排除无效状态 38,268、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=9,185，down=11,245；有效 ±inf 共 351，入选 up/down 分别 0/0。
- 输出：`GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz)；SHA-256：`4c9f9e881aa7555dd47804b261c5753e13e1b48792d5f128a3d97226ae0641d1`。

## GSE96962_EC-IL-normalized-gene_exp.diff.gz

- 列：ID=`SeqID`；log2FC=`log2(fold_change)`；校正 P=`FDR AdjP_value`；检验状态=`status`。
- ID 类型：作者原始 SeqID（symbol 式标识）。
- 处理组：EC IL-1β；对照组：EC vehicle control；标签：('q1', 'q2')；翻转：False。
- 方向依据：作者 GEO 提交及论文的 EC/IL-1β 对比；表内 control=q1、sample=q2，表达列明确标为 FPKM-control/FPKM-sample。10,695 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- 行数 23,604；排除无效状态 12,892、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=5,423，down=5,289；有效 ±inf 共 17，入选 up/down 分别 0/0。
- 输出：`GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-IL-normalized-gene_exp.diff.gz)；SHA-256：`ca298b1efc7b2126adf7de67fb45b07641f29165c22448ccfc0faad1f98c9b5d`。

## GSE96962_EC-TNF-normalized-gene_exp.diff.gz

- 列：ID=`SeqID`；log2FC=`log2(fold_change)`；校正 P=`FDR AdjP_value`；检验状态=`status`。
- ID 类型：作者原始 SeqID（symbol 式标识）。
- 处理组：EC TNF-α；对照组：EC vehicle control；标签：('q1', 'q2')；翻转：False。
- 方向依据：作者 GEO 提交及论文的 EC/TNF-α 对比；control=q1、sample=q2。10,791 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- 行数 23,604；排除无效状态 12,792、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=5,448，down=5,364；有效 ±inf 共 21，入选 up/down 分别 0/0。
- 输出：`GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-TNF-normalized-gene_exp.diff.gz)；SHA-256：`9196e77fbd9b1a0be2aff6a2eec8d4b24e69ee8b1b0d228e0eaf3752d12e4949`。

## GSE96962_SMC--TNF-normalized-gene_exp.diff.gz

- 列：ID=`SeqID`；log2FC=`log2(fold_change)`；校正 P=`FDR AdjP_value`；检验状态=`status`。
- ID 类型：作者原始 SeqID（symbol 式标识）。
- 处理组：SMC TNF-α；对照组：SMC vehicle control；标签：('q1', 'q2')；翻转：False。
- 方向依据：作者 GEO 提交及论文的 SMC/TNF-α 对比；control=q1、sample=q2。11,434 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- 行数 23,604；排除无效状态 12,144、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=5,892，down=5,568；有效 ±inf 共 26，入选 up/down 分别 0/0。
- 输出：`GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC--TNF-normalized-gene_exp.diff.gz)；SHA-256：`c5ba3c6c4106842333e78ea523fd16b6640104be5ab7c82af098b277e6532b09`。

## GSE96962_SMC-IL-normalized-gene_exp.diff.gz

- 列：ID=`SeqID`；log2FC=`log2(fold_change)`；校正 P=`FDR AdjP_value`；检验状态=`status`。
- ID 类型：作者原始 SeqID（symbol 式标识）。
- 处理组：SMC IL-1β；对照组：SMC vehicle control；标签：('q1', 'q2')；翻转：False。
- 方向依据：作者 GEO 提交及论文的 SMC/IL-1β 对比；control=q1、sample=q2。11,136 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- 行数 23,604；排除无效状态 12,433、缺失 0、零 log2FC 0；重复 ID 0。
- 方向统一后有效基因：up=5,686，down=5,485；有效 ±inf 共 35，入选 up/down 分别 0/0。
- 输出：`GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json`；已验证 up/down 各 100 个不同字符串、不相交、方向及排序正确。
- [作者文件](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC-IL-normalized-gene_exp.diff.gz)；SHA-256：`0aeeb588c872cccaa43f9e549092ba201e671fd506e6272f235808fcd7f11319`。

## 未解决的问题

无。

## 方向核查补充与重跑

- [Cuffdiff 官方格式说明](https://cole-trapnell-lab.github.io/cufflinks/cuffdiff/index.html)：log2FC 为第二组/第一组；q 为 FDR-adjusted P；OK 表示检验成功。
- [GSE96962](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96962) 和[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762668/)明确四个细胞类型/刺激对比及 solvent controls；表内 FPKM-control/FPKM-sample 和逐行比值核对共同确定方向，而非仅由文件名判断。
- DESeq2 方向辅助来源：[作者现成表达表](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.normalised_counts.txt.gz)，SHA-256 `c12f436e8d6cacb2aca6d48c34dcd4900e987bec3da2c05f083ce7e1fa27ec21`；[GEO 样本标注](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100732)：GSM2692145–2148 为 KO，GSM2692149–2152 为 WT，对应文库列见该文件方向依据。
- DESeq2 核对示例：ENSMUSG00000005667.8 的 KO/WT 均值为 2340.875736/45.007997，作者 log2FC=+5.679036；ENSMUSG00000101111.1 的均值为 17836.530087/705964.212566，作者 log2FC=-5.306634。该核对只识别整体方向，不替换原始系数或重算 P 值；91 行简单均值方向与模型系数不同，仍严格使用原作者系数。
- 原目录运行 `python extract_reference.py`；修改 K 可用 `python extract_reference.py --k 50 --output-dir reference_json_top50`。脚本离线运行，全部列名/比较/方向在 FILE_CONFIGS 中；新方向未核实时设 multiplier=None。
