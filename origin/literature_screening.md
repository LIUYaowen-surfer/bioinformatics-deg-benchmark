# Literature screening - curator only

Checked 2026-11-15. The [catalogue](study_catalog.md) contains 20 distinct papers and 23 selected comparisons. All 23 complete author result files have been downloaded and hash-checked. The extractor produced 23 top100 reference JSONs without rerunning DEG analysis. Raw SRA downloading is a separate operation; see [downloads](downloads.md).

For each addition, the paper citation/DOI was matched to the GEO record, selected sample metadata were inspected, and GEO SRA experiment accessions were matched to ENA run records with FASTQ links. Result headers were read to verify gene IDs, log fold changes and adjusted P values (`q_value`, `padj` or `adj.P.Val`). These are author result tables, not count matrices or third-party reanalyses. Each study page links the paper, series, selected raw runs and exact author reference file.

Each answer has 100 unique original IDs per direction and disjoint up/down lists. The original seven JSONs remain byte-identical. Sixteen new tasks use one selected comparison per added paper. Other blocks or worksheets are not pooled into those tasks. Complete author files remain local and unchanged. Columns, direction evidence, eligibility counts and hashes are in the [extraction record](extraction_log.md).

No raw P value is substituted for adjusted P, and no extra significance or fold-change threshold is imposed. Signed infinite FC values with valid author tests are retained under the stated rules. Two source choices were corrected: study 10 uses oldYoung rather than oldMid for the selected adult samples; study 15 uses CTRL_SUZ12KO for the selected ESC samples rather than A-2_WT_B-2_KO from neural progenitors. Earlier downloaded candidates are preserved locally.

| Study | Source limitation or preparation requirement |
|---|---|
| 05 | Preserve assembled ucscCodingXLOC IDs/annotation; select HiSeq only, not duplicate MiSeq material. Widely reused tutorial dataset. |
| 06 | One reported FC magnitude (ENSG00000228252.4) differs from its displayed expression ratio but has the same sign. It is retained unchanged; see the extraction log. |
| 07 | Only q1/q3 (DMSO/AM580) is selected; retain experiment identifiers and XLOC annotation. |
| 08 | Merge lane/run splits per biological sample; retain coding/noncoding feature definitions. |
| 09 | Cord blood/adult is a developmental/source comparison. Direction is confirmed from the paper; use adj.P.Val. |
| 10 | GEO Young1-3 are adult (5.5-8.5 months). The matched oldYoung table reports adult/old and is flipped to old/adult. Three pools per group, five brains each; preserve the RNAoldyoung assembled annotation. |
| 11 | Resolve inconsistent mm9/mm10 metadata before fixing reference resources. |
| 12 | Preserve the deposited mfl1 label; exclude PARE/GMUCT and select only the Col0/mfl1 block. |
| 13 | The selected neuronal sheet has date-formatted numeric gene IDs, including repeated 44621/44622, and date-formatted padj cells. Stored numerical values are read without Excel display conversion. All ambiguous IDs are outside top100; none is repaired or replaced. |
| 14 | Two author tests at one locus share gene_id=Chd64 with opposite effects. Both remain in ranking; their direction-specific ranks are 438 and 1198, outside top100. No first row is selected as representative. |
| 15 | ESC source and KO/WT direction are confirmed from GEO and author code. Preserve biological replicate/block labels for reproduction of the paired model. |
| 16 | Paper Figure 4A directions for 11 genes establish q1=control and q2=mutant. Select embryonic bulk lung libraries only. |
| 17 | Retain three paired experiments/batches. Nonsignificant rows are present despite the filename. |
| 18 | Whole-tumor control/KO coefficients are flipped to KO/control. Tissue composition is part of this comparison. |
| 19 | Use padj, not raw p-value, and preserve Ensembl GeneID values. |
| 20 | Use the 0.7 mM versus 96wp pair. The paper links the correct author repository, allRNAseqScriptsFromPineauWongNgEtAl2025; GEO transposes the author names. |

Reviewed duplicate IDs are not merged or discarded. If a larger K would select one, extraction blocks that comparison as pending. At K=100 no selected ID is ambiguous and no selected comparison remains pending. Reference resources, software versions and scoring tolerances for new raw-data analyses remain to be fixed by the evaluator.

Other screened records were not counted toward the 20:

| Record | Reason for holding out |
|---|---|
| GSE95180 | LOGR scale/direction, adjusted-P interpretation and multiple RefSeq identifiers need additional checks. |
| GSE85308 | GEO descriptions disagree on the younger age group (2 vs 3 months). |
| GSE169544 | Repeated sequencing submissions and conflicting gestational-day labels complicate sample mapping. |
| GSE152988 | The stated biological replicates are not directly resolved by the bulk GEO sample records. |
| GSE247508 | The gastruloid paper reused this external dataset; its own generated data are GSE288158/GSE288157. |

Author DEG tables are references to a specific analysis, not universal biological truth. The source catalogue does not guarantee that another valid pipeline will reproduce identical rankings. Existing airway materials and the HOXA1 method dataset are especially exposed in public tutorials. Source hiding does not establish absence of training-data contamination.
