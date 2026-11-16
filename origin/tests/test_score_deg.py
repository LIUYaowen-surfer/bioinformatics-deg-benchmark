import contextlib
import copy
import io
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ORIGIN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ORIGIN))
from score_deg import DEFAULT_K, TASK_REFERENCES, main, read_json, score_deg


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.reference = {
            "up": [f"up_{i:03}" for i in range(100)],
            "down": [f"down_{i:03}" for i in range(100)],
        }

    def test_perfect_match_and_reordering(self):
        prediction = {key: list(reversed(ids)) for key, ids in self.reference.items()}
        self.assertEqual(score_deg(prediction, self.reference),
                         {"score": 200, "max_score": 200, "up_overlap": 100, "down_overlap": 100})

    def test_known_partial_match_is_not_normalized(self):
        prediction = {"up": self.reference["up"][:80] + [f"other_up_{i}" for i in range(20)],
                      "down": self.reference["down"][:70] + [f"other_down_{i}" for i in range(30)]}
        before = copy.deepcopy(prediction)
        self.assertEqual(score_deg(prediction, self.reference),
                         {"score": 150, "max_score": 200, "up_overlap": 80, "down_overlap": 70})
        self.assertEqual(prediction, before)

    def test_swapped_directions_receive_zero(self):
        prediction = {"up": self.reference["down"], "down": self.reference["up"]}
        self.assertEqual(score_deg(prediction, self.reference)["score"], 0)

    def test_no_overlap_is_a_valid_zero(self):
        prediction = {key: ["other_" + gene for gene in ids]
                      for key, ids in self.reference.items()}
        self.assertEqual(score_deg(prediction, self.reference)["score"], 0)

    def test_exact_ids_and_custom_k(self):
        reference = {"up": ["ENSG1.7", "GeneA", "geneA,geneB"],
                     "down": ["D1", "D2", "D3"]}
        prediction = {"up": ["ENSG1", "genea", "geneA"], "down": ["D1", "D2", "D3"]}
        self.assertEqual(score_deg(prediction, reference, k=3),
                         {"score": 3, "max_score": 6, "up_overlap": 0, "down_overlap": 3})
        prediction["up"] = [" ENSG1.7", "GeneA ", "geneA,geneB "]
        self.assertEqual(score_deg(prediction, reference, k=3)["up_overlap"], 0)

    def test_invalid_predictions_and_references_are_rejected(self):
        invalid = []
        for edit in (
            lambda d: d["up"].pop(),
            lambda d: d["up"].append("extra"),
            lambda d: d["up"].__setitem__(0, d["up"][1]),
            lambda d: d["up"].__setitem__(0, d["down"][0]),
            lambda d: d["up"].__setitem__(0, 123),
            lambda d: d["up"].__setitem__(0, "  "),
            lambda d: d.update(extra=[]),
            lambda d: d.pop("down"),
            lambda d: d.update(up="not a list"),
        ):
            obj = copy.deepcopy(self.reference)
            edit(obj)
            invalid.append(obj)
        for obj in [*invalid, [], None]:
            with self.subTest(obj=str(obj)[:50]):
                with self.assertRaises(ValueError):
                    score_deg(obj, self.reference)
                with self.assertRaises(ValueError):
                    score_deg(self.reference, obj)
        for k in [0, -1, True, 1.5]:
            with self.assertRaises(ValueError):
                score_deg(self.reference, self.reference, k)

    def test_strict_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            for raw in ['{"up": [], "up": [], "down": []}',
                        '{"up": [NaN], "down": []}', '```json\n{}\n```']:
                path.write_text(raw, encoding="utf-8")
                with self.assertRaises(ValueError):
                    read_json(path)

    def test_all_task_mappings_and_references(self):
        self.assertEqual(set(TASK_REFERENCES), {f"task_{n:03}" for n in range(1, 24)})
        self.assertEqual(len(set(TASK_REFERENCES.values())), 23)
        documented = {}
        for line in (ORIGIN / "README.md").read_text(encoding="utf-8").splitlines():
            match = re.search(r"\[Top 100\]\(([^)]+)\)", line)
            if match:
                documented[line.split("|")[1].strip().strip("`")] = match[1]
        self.assertEqual(TASK_REFERENCES, documented)
        for task, relative in TASK_REFERENCES.items():
            with self.subTest(task=task):
                data = read_json(ORIGIN / relative)
                self.assertEqual(score_deg(data, data)["score"], 2 * DEFAULT_K)

    def run_cli(self, args):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(args)
        return code, json.loads(stream.getvalue())

    def test_cli_saved_output_errors_and_input_protection(self):
        reference = ORIGIN / TASK_REFERENCES["task_001"]
        before = reference.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "score.json"
            args = ["--task", "task_001", "--prediction", str(reference)]
            code, result = self.run_cli(args + ["--output", str(output)])
            self.assertEqual(code, 0)
            self.assertEqual(result["score"], 200)
            self.assertEqual(read_json(output), result)
            saved = output.read_bytes()
            for target in [output, reference]:
                code, result = self.run_cli(args + ["--output", str(target)])
                self.assertEqual(code, 2)
                self.assertIsNone(result["score"])
            self.assertEqual(output.read_bytes(), saved)
            prediction = Path(tmp) / "incomplete.json"
            prediction.write_text('{"up": [], "down": []}', encoding="utf-8")
            code, result = self.run_cli(["--reference", str(reference), "--prediction", str(prediction)])
            self.assertEqual(code, 2)
            self.assertIsNone(result["score"])
            self.assertIn("exactly 100", result["error"])
            code, result = self.run_cli(args + ["--k", "50"])
            self.assertEqual(code, 2)
            self.assertIsNone(result["score"])
        self.assertEqual(reference.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
