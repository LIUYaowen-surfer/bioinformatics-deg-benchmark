# Literature screening - curator only

Checked 2026-11-15. The [catalogue](study_catalog.md) contains 20 distinct papers, including the original four. The 16 additions have author-deposited DEG result files and public SRA-linked raw sequencing records. No DEG analysis was run, no raw reads were downloaded, and no additional reference answers were generated.

For each addition, the paper citation/DOI was matched to the GEO record, selected sample metadata were inspected, and GEO SRA experiment accessions were matched to ENA run records with FASTQ links. Result headers were read to verify gene IDs, log fold changes and adjusted P values (`q_value`, `padj` or `adj.P.Val`). These are author result tables, not count matrices or third-party reanalyses. Each study page links the paper, series, selected raw runs and exact author reference file.

11 selected reference files were downloaded completely for inspection. For studies 07, 09, 12, 15 and 20, only headers and initial rows were read. The latter checks establish file type and column availability, not complete-file integrity or eligibility of every contrast. Downloaded inspection copies remain local; this repository publishes links and notes only.

Before adding formal answers, confirm contrast direction from the file and experiment, valid-test status, missing/nonfinite values, duplicate gene IDs, and at least 100 eligible genes in each direction under the existing extraction rules. Keep multi-contrast files separate. None of the 16 new entries is claimed to have passed that complete audit.

| Study | Specific follow-up |
|---|---|
| 05 | Preserve assembled ucscCodingXLOC IDs/annotation; select HiSeq only, not duplicate MiSeq material. Widely reused tutorial dataset. |
| 06 | Preserve versioned Ensembl IDs; complete row-level extraction checks. |
| 07 | Verify the q1/q3 block in the large file; retain experiment pairing and XLOC annotation. |
| 08 | Merge lane/run splits per biological sample; retain coding/noncoding feature definitions. |
| 09 | Confirm the logFC numerator and denominator. |
| 10 | Reconcile GEO Young/VeryYoung with adult/young-adult and reference mid/young labels. The selected oldMid file reports mid/old; an old/adult answer requires confirmed mapping and sign reversal. Retain pooled-sample design and XLOC annotation. |
| 11 | Resolve inconsistent mm9/mm10 metadata before fixing reference resources. |
| 12 | Confirm mfl1/dne1 naming; exclude PARE/GMUCT and split genotype contrasts. |
| 13 | Use the day-15 neuron worksheet, not the spike-in-normalized mESC/293T sheets. |
| 14 | Keep biological pools distinct; exclude the overexpression contrast. |
| 15 | Verify paired-model blocks and direction; parse the unnamed R row-ID field correctly. |
| 16 | Map anonymous q1/q2 result labels to the two genotypes. |
| 17 | Retain experimental pairing/batch; confirm coefficient direction. |
| 18 | Use whole tumors, not cultured/purified cells; confirm coefficient direction. |
| 19 | Use padj, not raw p-value; confirm coefficient direction. |
| 20 | Use the matching contrast-specific columns and full table. |

Other screened records were not counted toward the 20:

| Record | Reason for holding out |
|---|---|
| GSE95180 | LOGR scale/direction, adjusted-P interpretation and multiple RefSeq identifiers need additional checks. |
| GSE85308 | GEO descriptions disagree on the younger age group (2 vs 3 months). |
| GSE169544 | Repeated sequencing submissions and conflicting gestational-day labels complicate sample mapping. |
| GSE152988 | The stated biological replicates are not directly resolved by the bulk GEO sample records. |
| GSE247508 | The gastruloid paper reused this external dataset; its own generated data are GSE288158/GSE288157. |

Author DEG tables are references to a specific analysis, not universal biological truth. The source catalogue does not guarantee that another valid pipeline will reproduce identical rankings. Existing airway materials and the HOXA1 method dataset are especially exposed in public tutorials. Source hiding does not establish absence of training-data contamination.
