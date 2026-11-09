# 来源、再分发与许可记录

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
