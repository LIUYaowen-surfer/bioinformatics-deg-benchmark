# Reference extraction record (top100)

Only existing author DEG results are extracted. Direction is treated/control.
Use status=OK when a test-status column exists. Exclude missing IDs, log2FC or adjusted P values and log2FC=0. No significant-column, raw-P, extra FDR or fold-change filter is applied.
Within each direction, sort by adjusted P value and then the unchanged gene-ID string. Decimal parsing preserves the stored numerical precision. Signed infinite FC values are retained when the original test is valid; they are counted below.
Each input hash binds the reviewed columns, comparison and direction to the inspected author file. Reviewed duplicate IDs are never merged or reduced to the first row; if any enters top K, formal output is blocked.

## study_01 / GSE52778_Dex_vs_Untreated_gene_exp.diff.gz

- Source: [GSE52778_Dex_vs_Untreated_gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz).
- SHA-256: `6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: 作者 gene_id：symbol 式标签，含逗号连接的复合 ID，均原样保留.
- Treated: Dex; control: Untreated; file labels: `('Dex', 'Untreated')`; sign multiplier: `-1`.
- Direction evidence: 文件内 sample_1=Dex、sample_2=Untreated；Cuffdiff 的 log2FC=log2(value_2/value_1)，故原方向是 Untreated/Dex。13,370 个 OK 且两侧表达量为正的有限值行通过数值核对（绝对误差≤1e-4）；翻转符号。
- Source rows: 23,273. Excluded: invalid status 9,760, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=7,292, down=6,221. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_01/reference/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json](study_01/reference/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_02 / GSE100732_DESeq2.results.txt.gz

- Source: [GSE100732_DESeq2.results.txt.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz).
- SHA-256: `0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df`.
- Fields: ID=`__rowname__`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: 原文件无表头的首列行名：带版本号的 ENSMUSG ID 与作者自定义线粒体 ID（例如 mt-Nd4l_4）.
- Treated: Lrpprc knockout; control: wild type; file labels: `()`; sign multiplier: `1`.
- Direction evidence: 结果表未显式保存 contrast。通过作者现成 normalized-counts 表与 GEO 样本标注交叉核对：KO 列 55219/55221/55223/55233，WT 列 55225/55227/55229/55231。19,866/19,957 个有效基因的系数符号与 KO/WT 均值方向一致，两个方向最靠前的基因亦一致，确认整体方向为 KO/WT；不翻转。不用均值替换系数，不删除其余 91 行。
- Source rows: 50,599. Excluded: invalid status 0, missing 30,642, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=10,045, down=9,912. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_02/reference/GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json](study_02/reference/GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_04 / GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz

- Source: [GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz).
- SHA-256: `4c9f9e881aa7555dd47804b261c5753e13e1b48792d5f128a3d97226ae0641d1`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: 原始 ENSG gene_id，保留版本后缀.
- Treated: si_SRSF1; control: si_CTRL; file labels: `('si_CTRL', 'si_SRSF1')`; sign multiplier: `1`.
- Direction evidence: 文件内 sample_1=si_CTRL、sample_2=si_SRSF1；按 Cuffdiff 定义为 si_SRSF1/si_CTRL。20,079 个 OK 且两侧表达量为正的有限值行通过 log2(value_2/value_1) 核对（绝对误差≤1e-4）；不翻转。
- Source rows: 58,698. Excluded: invalid status 38,268, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=9,185, down=11,245. Eligible signed-infinite FC rows: 351; selected up/down: 0/0.
- Output: [study_04/reference/GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json](study_04/reference/GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_03 / GSE96962_EC-IL-normalized-gene_exp.diff.gz

- Source: [GSE96962_EC-IL-normalized-gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-IL-normalized-gene_exp.diff.gz).
- SHA-256: `ca298b1efc7b2126adf7de67fb45b07641f29165c22448ccfc0faad1f98c9b5d`.
- Fields: ID=`SeqID`, log2FC=`log2(fold_change)`, adjusted P=`FDR AdjP_value`, status=`status`.
- ID type: 作者原始 SeqID（symbol 式标识）.
- Treated: EC IL-1β; control: EC vehicle control; file labels: `('q1', 'q2')`; sign multiplier: `1`.
- Direction evidence: 作者 GEO 提交及论文的 EC/IL-1β 对比；表内 control=q1、sample=q2，表达列明确标为 FPKM-control/FPKM-sample。10,695 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- Source rows: 23,604. Excluded: invalid status 12,892, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,423, down=5,289. Eligible signed-infinite FC rows: 17; selected up/down: 0/0.
- Output: [study_03/reference/GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json](study_03/reference/GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_03 / GSE96962_EC-TNF-normalized-gene_exp.diff.gz

- Source: [GSE96962_EC-TNF-normalized-gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-TNF-normalized-gene_exp.diff.gz).
- SHA-256: `9196e77fbd9b1a0be2aff6a2eec8d4b24e69ee8b1b0d228e0eaf3752d12e4949`.
- Fields: ID=`SeqID`, log2FC=`log2(fold_change)`, adjusted P=`FDR AdjP_value`, status=`status`.
- ID type: 作者原始 SeqID（symbol 式标识）.
- Treated: EC TNF-α; control: EC vehicle control; file labels: `('q1', 'q2')`; sign multiplier: `1`.
- Direction evidence: 作者 GEO 提交及论文的 EC/TNF-α 对比；control=q1、sample=q2。10,791 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- Source rows: 23,604. Excluded: invalid status 12,792, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,448, down=5,364. Eligible signed-infinite FC rows: 21; selected up/down: 0/0.
- Output: [study_03/reference/GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json](study_03/reference/GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_03 / GSE96962_SMC--TNF-normalized-gene_exp.diff.gz

- Source: [GSE96962_SMC--TNF-normalized-gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC--TNF-normalized-gene_exp.diff.gz).
- SHA-256: `c5ba3c6c4106842333e78ea523fd16b6640104be5ab7c82af098b277e6532b09`.
- Fields: ID=`SeqID`, log2FC=`log2(fold_change)`, adjusted P=`FDR AdjP_value`, status=`status`.
- ID type: 作者原始 SeqID（symbol 式标识）.
- Treated: SMC TNF-α; control: SMC vehicle control; file labels: `('q1', 'q2')`; sign multiplier: `1`.
- Direction evidence: 作者 GEO 提交及论文的 SMC/TNF-α 对比；control=q1、sample=q2。11,434 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- Source rows: 23,604. Excluded: invalid status 12,144, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,892, down=5,568. Eligible signed-infinite FC rows: 26; selected up/down: 0/0.
- Output: [study_03/reference/GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json](study_03/reference/GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_03 / GSE96962_SMC-IL-normalized-gene_exp.diff.gz

- Source: [GSE96962_SMC-IL-normalized-gene_exp.diff.gz](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC-IL-normalized-gene_exp.diff.gz).
- SHA-256: `0aeeb588c872cccaa43f9e549092ba201e671fd506e6272f235808fcd7f11319`.
- Fields: ID=`SeqID`, log2FC=`log2(fold_change)`, adjusted P=`FDR AdjP_value`, status=`status`.
- ID type: 作者原始 SeqID（symbol 式标识）.
- Treated: SMC IL-1β; control: SMC vehicle control; file labels: `('q1', 'q2')`; sign multiplier: `1`.
- Direction evidence: 作者 GEO 提交及论文的 SMC/IL-1β 对比；control=q1、sample=q2。11,136 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。
- Source rows: 23,604. Excluded: invalid status 12,433, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,686, down=5,485. Eligible signed-infinite FC rows: 35; selected up/down: 0/0.
- Output: [study_03/reference/GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json](study_03/reference/GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_05 / GSE37703_hiseq_cuffdiff_gene_exp.diff.gz

- Source: [GSE37703_hiseq_cuffdiff_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE37703&format=file&file=GSE37703_hiseq_cuffdiff_gene_exp.diff.gz).
- SHA-256: `d4859e418f38f8c14b79ce27a477f318f4a9001a4f191790b9c3885661564075`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original ucscCodingXLOC assembled gene IDs.
- Treated: HOXA1 knockdown; control: scramble; file labels: `['Lung_Scramble', 'Lung_A1KD']`; sign multiplier: `1`.
- Direction evidence: GEO HiSeq sample titles match Lung_Scramble and Lung_A1KD in the result. Cuffdiff defines log2FC as sample_2/sample_1. All 11,605 OK rows with positive expression and finite FC agree with log2(value_2/value_1) within 1e-4. Keep the sign.
- Source rows: 20,239. Excluded: invalid status 8,630, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,522, down=6,087. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_05/reference/GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json](study_05/reference/GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_06 / GSE60328_gene_exp.diff.gz

- Source: [GSE60328_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE60328&format=file&file=GSE60328_gene_exp.diff.gz).
- SHA-256: `6d520c57a947f2f8019b31fa76af7617e458d6b49adce49315920c66811b2355`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original versioned ENSG IDs.
- Treated: INSR shRNA; control: scramble shRNA; file labels: `['Scr_KD', 'IR_KD']`; sign multiplier: `1`.
- Direction evidence: Result labels are Scr_KD then IR_KD, matching GEO shScr and shIR samples. Cuffdiff therefore reports IR/Scr. 20,278 of 20,279 OK finite positive-expression rows agree numerically within 1e-4. ENSG00000228252.4 (COL6A4P2) has an inconsistent magnitude but the same positive direction; retain the author coefficient 0.803023 and q=0.479485 without correction. Keep the sign.
- Source rows: 48,541. Excluded: invalid status 28,072, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=10,417, down=10,052. Eligible signed-infinite FC rows: 190; selected up/down: 0/1.
- Output: [study_06/reference/GSE60328_gene_exp.diff__INSR_KD_vs_scramble_top100.json](study_06/reference/GSE60328_gene_exp.diff__INSR_KD_vs_scramble_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_07 / GSE76682_EB_AM580gene_exp.diff.gz

- Source: [GSE76682_EB_AM580gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE76682&format=file&file=GSE76682_EB_AM580gene_exp.diff.gz).
- SHA-256: `fc9c4e9cea5f137d6aa53b942f3bf0f894c54943864522da7818e28a52218ae3`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original XLOC assembled gene IDs.
- Treated: AM580, day 6; control: DMSO, day 6; file labels: `['q1', 'q3']`; sign multiplier: `1`.
- Direction evidence: GEO sample titles explicitly map day-6 DMSO to q1 and day-6 AM580 to q3. The q1/q3 row block is present in the complete file. All 29,202 OK finite positive-expression rows in that block agree with log2(value_2/value_1) within 1e-4. Keep the sign; other row blocks are recorded separately and are not pooled.
- Source rows: 104,460. Excluded: invalid status 62,971, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=20,517, down=20,972. Eligible signed-infinite FC rows: 12287; selected up/down: 81/86.
- Other comparison blocks, recorded but outside this selected task: `{"('q1', 'q2')": 104460, "('q2', 'q3')": 104460, "('q1', 'q4')": 104460, "('q2', 'q4')": 104460, "('q3', 'q4')": 104460, "('q1', 'q5')": 104460, "('q2', 'q5')": 104460, "('q3', 'q5')": 104460, "('q4', 'q5')": 104460, "('q1', 'q6')": 104460, "('q2', 'q6')": 104460, "('q3', 'q6')": 104460, "('q4', 'q6')": 104460, "('q5', 'q6')": 104460, "('q1', 'q7')": 104460, "('q2', 'q7')": 104460, "('q3', 'q7')": 104460, "('q4', 'q7')": 104460, "('q5', 'q7')": 104460, "('q6', 'q7')": 104460, "('q1', 'q8')": 104460, "('q2', 'q8')": 104460, "('q3', 'q8')": 104460, "('q4', 'q8')": 104460, "('q5', 'q8')": 104460, "('q6', 'q8')": 104460, "('q7', 'q8')": 104460}`.
- Output: [study_07/reference/GSE76682_EB_AM580gene_exp.diff__AM580_vs_DMSO_day6_top100.json](study_07/reference/GSE76682_EB_AM580gene_exp.diff__AM580_vs_DMSO_day6_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_08 / GSE89238_SET2_KO_DESeq2_output.txt.gz

- Source: [GSE89238_SET2_KO_DESeq2_output.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE89238&format=file&file=GSE89238_SET2_KO_DESeq2_output.txt.gz).
- SHA-256: `b783572da8b31661f49b4bbbf8daad7def5efd23d27a683c53abd78477db166c`.
- Fields: ID=`gene_id`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: Original yeast coding/noncoding feature IDs.
- Treated: set2 deletion; control: wild type; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: GEO processing states SET2 KO against WT. In the same author table, mean SET2 FPKM is 0.682090 in KO versus 12.601670 in WT, with FC=-3.155502; YOR383C is 469.670022 versus 44.293420, with FC=+3.126276. 5,347/5,438 eligible matched genes agree in sign with supplied group FPKM means. These means only corroborate coefficient direction; author statistics are unchanged. Keep KO/WT.
- Source rows: 18,646. Excluded: invalid status 0, missing 13,208, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=2,613, down=2,825. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_08/reference/GSE89238_SET2_KO_DESeq2_output__set2_KO_vs_WT_top100.json](study_08/reference/GSE89238_SET2_KO_DESeq2_output__set2_KO_vs_WT_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_09 / GSE100077_DifferentialExpression.csv.gz

- Source: [GSE100077_DifferentialExpression.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE100077&format=file&file=GSE100077_DifferentialExpression.csv.gz).
- SHA-256: `064b53dacc025859df89af5c756514b948d0bc47812a5e343deba65c209a52e3`.
- Fields: ID=`gene`, log2FC=`logFC`, adjusted P=`adj.P.Val`, status=`none`.
- ID type: Author gene labels.
- Treated: cord-blood-derived; control: adult-bone-marrow-derived; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: The paper Results/Fig.4 explicitly reports HBG1, HBG2 and HBZ as higher in cord-blood-derived RNA-seq samples than adult-derived samples (https://doi.org/10.1002/ajh.24805). The author table has HBG1 logFC=+4.752799 and HBG2=+4.245726, with adult globins HBB=-0.712425 and HBD=-0.586473. This establishes CB/adult; keep the sign. Use adj.P.Val, never P.Value.
- Source rows: 27,528. Excluded: invalid status 0, missing 0, zero FC 3,216. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=12,253, down=12,059. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_09/reference/GSE100077_DifferentialExpression__cord_blood_vs_adult_top100.json](study_09/reference/GSE100077_DifferentialExpression__cord_blood_vs_adult_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_10 / GSE133436_gene_exp_oldYoung_.diff.gz

- Source: [GSE133436_gene_exp_oldYoung_.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE133436&format=file&file=GSE133436_gene_exp_oldYoung_.diff.gz).
- SHA-256: `103719a4a6dcc7a151be67f5e2150accafa22f189c184b1be0a1d506ff67cf5a`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original XLOC assembled gene IDs.
- Treated: old, 26-31 months; control: adult, 5.5-8.5 months; file labels: `['old', 'young']`; sign multiplier: `-1`.
- Direction evidence: Use gene_exp_oldYoung_, not oldMid_. Its actual row labels are old then young. GEO Young1-3 have ages 5.5-8.5 months (adult in paper Table 1); VeryYoung1-3 are 3 months. Supplied sample FPKMs corroborate the mapping: cldn19 adult samples are 9.03982/7.11362/8.12401 versus 3-month samples 3.71964/2.54407/2.82978; the result young value is 11.6416 whereas the separate mid value is 4.17238. The oldYoung table reports adult/old, so flip to old/adult. All 15,175 OK finite positive-expression rows agree with value_2/value_1 within 1e-4.
- Source rows: 31,073. Excluded: invalid status 15,886, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=9,065, down=6,122. Eligible signed-infinite FC rows: 12; selected up/down: 0/0.
- Output: [study_10/reference/GSE133436_gene_exp_oldYoung_.diff__old_vs_adult_top100.json](study_10/reference/GSE133436_gene_exp_oldYoung_.diff__old_vs_adult_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_11 / GSE164712_gene_exp.diff.gz

- Source: [GSE164712_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE164712&format=file&file=GSE164712_gene_exp.diff.gz).
- SHA-256: `40dce9716d3b414d69b183b4685dff9889ed347e3e089db9220627630fb10fc5`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Author gene_id labels, including symbols.
- Treated: Tcf1/Lef1 deficient; control: wild type; file labels: `['WT_0h', 'DKO_0h']`; sign multiplier: `1`.
- Direction evidence: The table labels WT_0h then DKO_0h, matching GEO WT and Tcf1/Lef1-deficient samples. All 11,197 OK finite positive-expression rows match sample_2/sample_1 within 1e-4. Keep DKO/WT.
- Source rows: 23,951. Excluded: invalid status 12,704, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=5,512, down=5,735. Eligible signed-infinite FC rows: 50; selected up/down: 0/0.
- Output: [study_11/reference/GSE164712_gene_exp.diff__Tcf1_Lef1_DKO_vs_WT_top100.json](study_11/reference/GSE164712_gene_exp.diff__Tcf1_Lef1_DKO_vs_WT_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_12 / GSE193247_gene_exp.diff.gz

- Source: [GSE193247_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE193247&format=file&file=GSE193247_gene_exp.diff.gz).
- SHA-256: `cb03676ee7a06168098252f417ed2631778a70f3daad04d2bcc1572d17b32fed`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original TAIR gene IDs.
- Treated: mfl1 (GEO label); control: Col-0; file labels: `['Col0', 'mfl1']`; sign multiplier: `1`.
- Direction evidence: The selected table block explicitly labels Col0 then mfl1; the selected GEO samples have exactly these genotypes and Description=RNA-seq. All 22,809 OK finite positive-expression rows match sample_2/sample_1 within 1e-4. Keep mfl1/Col0. mfl1 is retained as the deposited label; no inferred gene-name replacement is used.
- Source rows: 32,823. Excluded: invalid status 9,968, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=11,644, down=11,211. Eligible signed-infinite FC rows: 46; selected up/down: 10/1.
- Other comparison blocks, recorded but outside this selected task: `{"('Col0', 'xrn4-5')": 32823, "('mfl1', 'xrn4-5')": 32823, "('Col0', 'mfl1xrn4-5')": 32823, "('mfl1', 'mfl1xrn4-5')": 32823, "('xrn4-5', 'mfl1xrn4-5')": 32823}`.
- Output: [study_12/reference/GSE193247_gene_exp.diff__mfl1_vs_Col0_top100.json](study_12/reference/GSE193247_gene_exp.diff__mfl1_vs_Col0_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_13 / GSE207163_RNA-seq.xlsx

- Source: [GSE207163_RNA-seq.xlsx](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE207163&format=file&file=GSE207163_RNA-seq.xlsx).
- SHA-256: `42d2b2b2b351ee256355d12feef0327abfecd3b81bb716a77f6e2ff57919203e`.
- Fields: ID=`gene`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: Original author gene labels.
- Worksheet: `neuron.Mut.1vsWT_day15`. Other worksheets are not pooled.
- Treated: Mut.1, day-15 neurons; control: WT, day-15 neurons; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: The selected worksheet is neuron.Mut.1vsWT_day15. Author-supplied per-sample RSEM TPMs confirm mutant/WT: Rasgrf1 means are 0.32/56.075 with FC=-7.282875; Peg13 means are 103.41/25.735 with FC=+2.016282. 16,068/16,519 matched eligible rows and all top 200 matched rows by padj agree with mutant/WT. Only exact label_label identifiers were matched for this diagnostic, without changing reference gene labels or statistics. Keep the sign.
- Source rows: 18,368. Excluded: invalid status 0, missing 1,781, zero FC 0. Duplicate IDs in source: 2.
- Eligible distinct IDs: up=8,417, down=8,169. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Duplicate review: The author XLSX stores these gene cells as Excel date-formatted numbers (numFmtId 16), producing repeated raw IDs. They are retained as stored strings, not repaired or converted. One row has missing padj; the eligible duplicated IDs rank 631-633 in the positive direction at K=100 and cannot affect either top-100 list. All other numeric/date-like IDs were also checked to be outside the selected lists. All source rows remain in ranking.
- Output: [study_13/reference/GSE207163_RNA-seq__Top1_Mut1_vs_WT_day15_top100.json](study_13/reference/GSE207163_RNA-seq__Top1_Mut1_vs_WT_day15_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_14 / GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz

- Source: [GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE218205&format=file&file=GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz).
- SHA-256: `7a056b984b2d5e5e01a42ae2e760d547fe3423bdc634ce275f4b28b1dd299e3c`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Author gene_id labels, including symbols.
- Treated: bam mutant + Mei-P26 RNAi; control: bam mutant; file labels: `['bam', 'bam_KD_meiP26']`; sign multiplier: `1`.
- Direction evidence: File row labels are bam then bam_KD_meiP26, explicitly matching the two selected GEO genotypes. All 10,160 OK finite positive-expression rows agree with sample_2/sample_1 within 1e-4. Keep RNAi/bam.
- Source rows: 16,507. Excluded: invalid status 6,228, missing 0, zero FC 0. Duplicate IDs in source: 1.
- Eligible distinct IDs: up=5,090, down=5,189. Eligible signed-infinite FC rows: 119; selected up/down: 6/9.
- Duplicate review: Two different author test_id values, Chd64 and P32, share gene_id=Chd64 and the same locus but have opposite coefficients. No row is selected as representative and no ID is replaced by test_id. Both rows remain in ranking: positive rank 438 and negative rank 1198, outside top100. Any K that brings this ambiguous ID into an answer is blocked. All source rows remain in ranking.
- Output: [study_14/reference/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26__MeiP26_KD_vs_bam_top100.json](study_14/reference/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26__MeiP26_KD_vs_bam_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_15 / GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz

- Source: [GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE223666&format=file&file=GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz).
- SHA-256: `885a1ffa50d8d1923b33cbc9d931f73c755121dd74114d2516c1fdc225285c36`.
- Fields: ID=`__rowname__`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: Original R row names / gene labels.
- Treated: Suz12 full KO; control: WT; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: The selected ESC samples explicitly point to CTRL_SUZ12KO_stats_paired.txt in GEO, not the A-2 neural-progenitor result. Author code _Code/Fig6/Main_Panels_Fig6.qmd imports this exact CTRL_SUZ12KO file with invert_l2FC=FALSE and labels positive coefficients UP in Suz12 KO (lines 92-105,918-926). Source: https://github.com/Ni-Ar/SUZ12_AS/blob/e8af7d4959a0be668308fdaae8be647506e70c4c/_Code/Fig6/Main_Panels_Fig6.qmd. Keep KO/WT.
- Source rows: 26,171. Excluded: invalid status 0, missing 9,253, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=8,548, down=8,370. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_15/reference/GSE223666_CTRL_SUZ12KO_stats_paired__Suz12_KO_vs_WT_ESC_top100.json](study_15/reference/GSE223666_CTRL_SUZ12KO_stats_paired__Suz12_KO_vs_WT_ESC_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_16 / GSE230334_gene_exp.diff.gz

- Source: [GSE230334_gene_exp.diff.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE230334&format=file&file=GSE230334_gene_exp.diff.gz).
- SHA-256: `f7d33e90b0e1bedb27b0d3814c48a4c13264bbe0a9aaec82b6f7c8d5db7b090e`.
- Fields: ID=`gene_id`, log2FC=`log2(fold_change)`, adjusted P=`q_value`, status=`status`.
- ID type: Original ENSMUSG IDs.
- Treated: Shhcre;Lonp1f/f; control: Shhcre;Lonp1f/+; file labels: `['q1', 'q2']`; sign multiplier: `1`.
- Direction evidence: Paper Figure 4A explicitly reports Foxa1, Foxa2, Shh, Ptch1, Ptch2, Hhip and Etv5 lower in mutant lungs, and Fgf10, Etv4, Bmp4 and Id2 higher (https://pmc.ncbi.nlm.nih.gov/articles/PMC12490049/). All 11 signs match the q1/q2 table, identifying q1=control and q2=mutant. All 15,445 OK finite positive-expression rows match sample_2/sample_1 within 1e-4. Keep mutant/control.
- Source rows: 31,053. Excluded: invalid status 15,601, missing 0, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=7,601, down=7,851. Eligible signed-infinite FC rows: 7; selected up/down: 0/0.
- Output: [study_16/reference/GSE230334_gene_exp.diff__Lonp1_KO_vs_control_top100.json](study_16/reference/GSE230334_gene_exp.diff__Lonp1_KO_vs_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_17 / GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz

- Source: [GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE243105&format=file&file=GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz).
- SHA-256: `776b74bb701d48ecaf6e1e715b96859f6ab68c31e7b274d9d121b7267aba27d5`.
- Fields: ID=`__rowname__`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: Author gene labels in the unnamed first column.
- Treated: siOGT; control: control siRNA; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: GEO defines paired siOGT and control experiments. Author count tables corroborate siOGT/control: OGT means 862.333333/3869.666667 with FC=-2.185610; NR1D1 means 12931.333333/4261.333333 with FC=+1.578348. 12,196/12,535 matched eligible genes and all top 200 matched rows by padj have this orientation. Means are only a diagnostic, not a replacement for paired-model coefficients. Keep the sign.
- Source rows: 14,853. Excluded: invalid status 0, missing 2,304, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=6,255, down=6,294. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_17/reference/GSE243105_sign_siOGT_control_genes_with_Batch_all__siOGT_vs_siControl_top100.json](study_17/reference/GSE243105_sign_siOGT_control_genes_with_Batch_all__siOGT_vs_siControl_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_18 / GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz

- Source: [GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE250602&format=file&file=GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz).
- SHA-256: `949d70e15c7d8e2feffd31086fe9384cdc47b1f6a13d2ac38ca4b413281cfe2e`.
- Fields: ID=`__rowname__`, log2FC=`log2FoldChange`, adjusted P=`padj`, status=`none`.
- ID type: Author gene labels in the unnamed first column.
- Treated: Sun1 KO tumors; control: control tumors; file labels: `[]`; sign multiplier: `-1`.
- Direction evidence: GEO processing explicitly describes the result as WT vs KO. Author RSEM TPMs confirm control/KO: Sun1 means in KO/control are 16.495714/54.37 yet FC=+1.508401; Ift81 means are 41.14/12.12875 yet FC=-2.288037. All top 200 matched rows by padj oppose KO/control means (16,386/20,209 across matched eligible rows). Flip the entire coefficient to KO/control; preserve coefficients and P values otherwise, including rows where simple means differ from the model.
- Source rows: 21,431. Excluded: invalid status 0, missing 417, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=11,806, down=9,208. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_18/reference/GSE250602_DESeq2_CT26_tumors_Control_vs_KO__Sun1_KO_vs_control_tumors_top100.json](study_18/reference/GSE250602_DESeq2_CT26_tumors_Control_vs_KO__Sun1_KO_vs_control_tumors_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_19 / GSE269122_ctrl_vs_Sox10ko.xlsx

- Source: [GSE269122_ctrl_vs_Sox10ko.xlsx](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE269122&format=file&file=GSE269122_ctrl_vs_Sox10ko.xlsx).
- SHA-256: `61b8668cb0b36764cf20d494c307af5d0265526c62a9e04a342c78196179572b`.
- Fields: ID=`GeneID`, log2FC=`log2(FC)`, adjusted P=`padj`, status=`none`.
- ID type: Original ENSMUSG IDs.
- Worksheet: `Rohdaten`. Other worksheets are not pooled.
- Treated: Sox10 conditional KO; control: control; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: The paper describes myelin-gene reduction in Sox10 mutants (https://pmc.ncbi.nlm.nih.gov/articles/PMC11354551/). Corresponding author coefficients are negative: Mbp ENSMUSG00000041607=-0.537210, Aspa ENSMUSG00000020774=-1.612690, Ugt8a ENSMUSG00000032854=-1.475412. The top 200 matched rows by padj also agree with KO/control means of author counts. Gene labels were used only to check direction; reference IDs remain the original GeneID values. Keep KO/control; do not infer direction from filename order.
- Source rows: 49,315. Excluded: invalid status 0, missing 25,130, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=12,236, down=11,949. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_19/reference/GSE269122_ctrl_vs_Sox10ko__Sox10_KO_vs_control_top100.json](study_19/reference/GSE269122_ctrl_vs_Sox10ko__Sox10_KO_vs_control_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## study_20 / GSE288157_DESeq2_summary.txt.gz

- Source: [GSE288157_DESeq2_summary.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE288157&format=file&file=GSE288157_DESeq2_summary.txt.gz).
- SHA-256: `46dd0af492844ab6cbdd9183bb5d42e47c77915c00c92273e7061932c7b7ff4e`.
- Fields: ID=`Ens_ID`, log2FC=`Condition_Emb_0.7mMvs96wp_l2fc`, adjusted P=`Condition_Emb_0.7mMvs96wp_padj`, status=`none`.
- ID type: Original Ens_ID values.
- Treated: 0.7 mM hydrogel; control: unembedded 96-well control; file labels: `[]`; sign multiplier: `1`.
- Direction evidence: Use the concentration-effect author code, whose sample plan places 96wp as the first/reference condition. step2-multi_DESeq2.R takes that reference, labels output my.value vs ref.value and preserves factor order; RNAseqFunctions.R exports the resulting DESeq2 coefficients unchanged. Source: https://github.com/lldelisle/allRNAseqScriptsFromPineauWongNgEtAl2025. Thus Condition_Emb_0.7mMvs96wp_l2fc is embedding/control; keep the sign. The similarly named repository in GEO processing is a typo; use the paper Data Availability URL.
- Source rows: 55,141. Excluded: invalid status 0, missing 41,577, zero FC 0. Duplicate IDs in source: 0.
- Eligible distinct IDs: up=6,861, down=6,703. Eligible signed-infinite FC rows: 0; selected up/down: 0/0.
- Output: [study_20/reference/GSE288157_DESeq2_summary__hydrogel_0p7mM_vs_unembedded_top100.json](study_20/reference/GSE288157_DESeq2_summary__hydrogel_0p7mM_vs_unembedded_top100.json). Verified: 100 different strings per direction, disjoint lists, correct signs and ordering.

## Pending comparisons

None for this K.

Cuffdiff format reference: https://cole-trapnell-lab.github.io/cufflinks/cuffdiff/index.html
The first seven configurations retain the previously reviewed settings; their evidence is preserved verbatim. Newly reviewed settings are in reference_configs.json. Use --k and a new --output-dir to change K; an ambiguous duplicate entering a larger K will block that comparison.
