"""Compare two DEG JSON files and print a score from 0 to 200."""
import argparse
import json
from pathlib import Path

K = 100


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError(f"Non-standard JSON value: {value}")


def load_genes(path):
    """Read and validate one JSON without changing its gene IDs."""
    try:
        answer = json.loads(Path(path).read_text(encoding="utf-8-sig"),
                            object_pairs_hook=_unique_object,
                            parse_constant=_reject_constant)
    except (OSError, ValueError) as error:
        raise ValueError(f"{path}: {error}") from error
    if not isinstance(answer, dict) or set(answer) != {"up", "down"}:
        raise ValueError(f"{path}: expected exactly the keys 'up' and 'down'")
    groups = {}
    for direction in ("up", "down"):
        genes = answer[direction]
        if not isinstance(genes, list):
            raise ValueError(f"{path}: '{direction}' must be a list")
        if len(genes) != K:
            raise ValueError(f"{path}: '{direction}' must contain exactly {K} IDs; got {len(genes)}")
        if any(not isinstance(gene, str) or not gene.strip() for gene in genes):
            raise ValueError(f"{path}: '{direction}' must contain nonempty gene-ID strings")
        groups[direction] = set(genes)
        if len(groups[direction]) != K:
            raise ValueError(f"{path}: '{direction}' contains duplicate gene IDs")
    if groups["up"] & groups["down"]:
        raise ValueError(f"{path}: 'up' and 'down' must not overlap")
    return groups


def score_deg(prediction, reference):
    """Accept two JSON file paths and return the same-direction overlap count."""
    predicted = load_genes(prediction)
    expected = load_genes(reference)
    return sum(len(predicted[key] & expected[key]) for key in ("up", "down"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prediction", type=Path, help="Model result JSON")
    parser.add_argument("reference", type=Path, help="Reference JSON chosen by the user")
    args = parser.parse_args()
    try:
        print(score_deg(args.prediction, args.reference))
    except ValueError as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
