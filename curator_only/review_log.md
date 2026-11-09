# 文献与来源核查记录

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
