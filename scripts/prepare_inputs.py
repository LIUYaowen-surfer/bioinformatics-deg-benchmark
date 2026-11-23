"""Prepare an anonymous Agent workspace from full-quality SRA FASTQ exports."""
import argparse
import csv
import gzip
import shutil
import tempfile
from contextlib import ExitStack
from itertools import zip_longest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


# Each accession is one biological sample. Blocks identify paired donors.
RUNS = {
    "task_01": [
        ("SRR1039509", "treated", "block1"),
        ("SRR1039513", "treated", "block2"),
        ("SRR1039517", "treated", "block3"),
        ("SRR1039521", "treated", "block4"),
        ("SRR1039508", "untreated", "block1"),
        ("SRR1039512", "untreated", "block2"),
        ("SRR1039516", "untreated", "block3"),
        ("SRR1039520", "untreated", "block4"),
    ],
    "task_02": [
        ("SRR5799230", "treated", ""),
        ("SRR5799231", "treated", ""),
        ("SRR5799232", "treated", ""),
        ("SRR5799233", "treated", ""),
        ("SRR5799234", "untreated", ""),
        ("SRR5799235", "untreated", ""),
        ("SRR5799236", "untreated", ""),
        ("SRR5799237", "untreated", ""),
    ],
}

def locate(directory, stem):
    matches = [directory / (stem + suffix) for suffix in
               (".fastq", ".fastq.gz", ".fq", ".fq.gz")]
    matches = [path for path in matches if path.is_file()]
    if len(matches) > 1:
        raise ValueError(f"Multiple FASTQ files for {stem}")
    return next(iter(matches), None)


def records(handle):
    while header := handle.readline():
        seq = handle.readline().rstrip(b"\r\n")
        plus = handle.readline()
        qual = handle.readline().rstrip(b"\r\n")
        if not (header.startswith(b"@") and header[1:].split() and
                plus.startswith(b"+") and seq and len(seq) == len(qual)):
            raise ValueError(f"Invalid four-line FASTQ in {handle.name}")
        name = header[1:].split()[0]
        yield name.removesuffix(b"/1").removesuffix(b"/2"), seq, qual


def copy_reads(paths, outputs, prefix):
    with ExitStack() as stack:
        readers, writers = [], []
        for path, output in zip(paths, outputs):
            opener = gzip.open if path.suffix == ".gz" else open
            readers.append(records(stack.enter_context(opener(path, "rb"))))
            writers.append(stack.enter_context(output.open("wb")))
        count = 0
        for count, reads in enumerate(zip_longest(*readers), 1):
            if None in reads or len({read[0] for read in reads}) != 1:
                raise ValueError(f"Mates differ in count or identifier for {paths[0]}")
            name = f"@{prefix}_{count}".encode()
            for writer, (_, seq, qual) in zip(writers, reads):
                writer.write(b"\n".join((name, seq, b"+", qual, b"")))
        if not count:
            raise ValueError(f"Empty FASTQ: {paths[0]}")


def prepare(task, source, output):
    output = output.resolve()
    if output.is_relative_to(ROOT) or ROOT.is_relative_to(output) or output.exists():
        raise ValueError("Choose a new workspace path outside the repository")
    runs = RUNS.get(task)
    if not runs:
        raise ValueError(f"Unknown task: {task}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent) as staging:
        workspace = Path(staging) / "workspace"
        inputs = workspace / "input"
        inputs.mkdir(parents=True)
        with (inputs / "samples.tsv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
            writer.writerow(["sample_id", "condition", "block", "read_layout", "read1", "read2", "unpaired"])
            for index, (run, condition, block) in enumerate(runs, 1):
                separate = locate(source, run)
                left, right = locate(source, run + "_1"), locate(source, run + "_2")
                if bool(left) != bool(right) or not (left or separate):
                    raise ValueError(f"Missing FASTQ or incomplete mate pair for {run}")
                folder = inputs / "data" / condition
                folder.mkdir(parents=True, exist_ok=True)
                prefix = f"run{index:03d}"
                files = [folder / f"{prefix}_{end}.fastq" for end in ("1", "2", "unpaired")]
                if left:
                    copy_reads([left, right], files[:2], prefix)
                if separate:
                    copy_reads([separate], [files[2] if left else files[0]], prefix + "_s")
                names = [p.relative_to(workspace).as_posix() if p.exists() else "" for p in files]
                writer.writerow([f"sample{index:02d}", condition, block,
                                 "paired" if left else "single", *names])
        shutil.copyfile(ROOT / "agent_prompt.md", workspace / "prompt.md")
        workspace.rename(output)
    return len(runs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True, choices=RUNS)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        count = prepare(args.task, args.source_dir, args.output_dir)
    except (ValueError, OSError, EOFError) as error:
        parser.exit(2, f"Preparation failed: {error}\n")
    print(f"Prepared {count} runs in {args.output_dir}")


if __name__ == "__main__":
    main()
