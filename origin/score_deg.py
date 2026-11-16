"""Score same-direction DEG overlap as a count: 0..200 for top100 per direction.

Standard library only. Run in the evaluator environment, outside the LLM workspace.
"""
import argparse
import json
from pathlib import Path

DEFAULT_K = 100
TASK_REFERENCES = {
    "task_001": "study_01/reference/GSE52778_Dex_vs_Untreated_gene_exp.diff__Dex_vs_Untreated_top100.json",
    "task_002": "study_02/reference/GSE100732_DESeq2.results__Lrpprc_KO_vs_WT_top100.json",
    "task_003": "study_03/reference/GSE96962_SMC--TNF-normalized-gene_exp.diff__SMC_TNFa_vs_SMC_control_top100.json",
    "task_004": "study_03/reference/GSE96962_SMC-IL-normalized-gene_exp.diff__SMC_IL1B_vs_SMC_control_top100.json",
    "task_005": "study_03/reference/GSE96962_EC-TNF-normalized-gene_exp.diff__EC_TNFa_vs_EC_control_top100.json",
    "task_006": "study_03/reference/GSE96962_EC-IL-normalized-gene_exp.diff__EC_IL1B_vs_EC_control_top100.json",
    "task_007": "study_04/reference/GSE212471_si_CTRL-siSRSF1.gene_exp.diff__siSRSF1_vs_siCTRL_top100.json",
    "task_008": "study_05/reference/GSE37703_hiseq_cuffdiff_gene_exp.diff__HOXA1_KD_vs_scramble_top100.json",
    "task_009": "study_06/reference/GSE60328_gene_exp.diff__INSR_KD_vs_scramble_top100.json",
    "task_010": "study_07/reference/GSE76682_EB_AM580gene_exp.diff__AM580_vs_DMSO_day6_top100.json",
    "task_011": "study_08/reference/GSE89238_SET2_KO_DESeq2_output__set2_KO_vs_WT_top100.json",
    "task_012": "study_09/reference/GSE100077_DifferentialExpression__cord_blood_vs_adult_top100.json",
    "task_013": "study_10/reference/GSE133436_gene_exp_oldYoung_.diff__old_vs_adult_top100.json",
    "task_014": "study_11/reference/GSE164712_gene_exp.diff__Tcf1_Lef1_DKO_vs_WT_top100.json",
    "task_015": "study_12/reference/GSE193247_gene_exp.diff__mfl1_vs_Col0_top100.json",
    "task_016": "study_13/reference/GSE207163_RNA-seq__Top1_Mut1_vs_WT_day15_top100.json",
    "task_017": "study_14/reference/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26__MeiP26_KD_vs_bam_top100.json",
    "task_018": "study_15/reference/GSE223666_CTRL_SUZ12KO_stats_paired__Suz12_KO_vs_WT_ESC_top100.json",
    "task_019": "study_16/reference/GSE230334_gene_exp.diff__Lonp1_KO_vs_control_top100.json",
    "task_020": "study_17/reference/GSE243105_sign_siOGT_control_genes_with_Batch_all__siOGT_vs_siControl_top100.json",
    "task_021": "study_18/reference/GSE250602_DESeq2_CT26_tumors_Control_vs_KO__Sun1_KO_vs_control_tumors_top100.json",
    "task_022": "study_19/reference/GSE269122_ctrl_vs_Sox10ko__Sox10_KO_vs_control_top100.json",
    "task_023": "study_20/reference/GSE288157_DESeq2_summary__hydrogel_0p7mM_vs_unembedded_top100.json"
}


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError(f"Non-standard JSON value: {value}")


def read_json(path):
    """Load strict JSON; never unwrap code fences or repair model output."""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                          object_pairs_hook=_unique_object,
                          parse_constant=_reject_constant)
    except (ValueError, UnicodeError) as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error


def validate_answer(answer, label, k):
    if not isinstance(answer, dict) or set(answer) != {"up", "down"}:
        raise ValueError(f"{label} must contain exactly the keys 'up' and 'down'")
    groups = {}
    for direction in ("up", "down"):
        genes = answer[direction]
        if not isinstance(genes, list):
            raise ValueError(f"{label}.{direction} must be a list")
        if len(genes) != k:
            raise ValueError(f"{label}.{direction} must contain exactly {k} IDs; got {len(genes)}")
        if any(not isinstance(gene, str) or not gene.strip() for gene in genes):
            raise ValueError(f"{label}.{direction} must contain nonempty gene-ID strings")
        groups[direction] = set(genes)
        if len(groups[direction]) != k:
            raise ValueError(f"{label}.{direction} contains duplicate gene IDs")
    if groups["up"] & groups["down"]:
        raise ValueError(f"{label}.up and {label}.down must not overlap")
    return groups


def score_deg(prediction, reference, k=DEFAULT_K):
    """Return exact, case-sensitive overlap counts; ignore order within each list."""
    if type(k) is not int or k < 1:
        raise ValueError("k must be a positive integer")
    expected = validate_answer(reference, "reference", k)
    observed = validate_answer(prediction, "prediction", k)
    up = len(observed["up"] & expected["up"])
    down = len(observed["down"] & expected["down"])
    return {"score": up + down, "max_score": 2 * k,
            "up_overlap": up, "down_overlap": down}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prediction", required=True, type=Path,
                        help="LLM result JSON with up/down lists")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--task", choices=sorted(TASK_REFERENCES),
                        help="Select the corresponding bundled top100 reference")
    source.add_argument("--reference", type=Path, help="Explicit reference JSON path")
    parser.add_argument("--k", type=int, default=DEFAULT_K,
                        help="IDs per direction; custom K requires --reference")
    parser.add_argument("--output", type=Path,
                        help="Also save UTF-8 JSON to a new file; existing files are never overwritten")
    args = parser.parse_args(argv)
    try:
        if args.task and args.k != DEFAULT_K:
            raise ValueError("Bundled tasks use k=100; use --reference for another K")
        reference = (Path(__file__).resolve().parent / TASK_REFERENCES[args.task]
                     if args.task else args.reference)
        if args.output and args.output.resolve() in {args.prediction.resolve(), reference.resolve()}:
            raise ValueError("Output must not overwrite the prediction or reference")
        result = score_deg(read_json(args.prediction), read_json(reference), args.k)
        payload = json.dumps(result, indent=2) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(payload)
        print(payload, end="")
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({"score": None, "error": str(error)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
