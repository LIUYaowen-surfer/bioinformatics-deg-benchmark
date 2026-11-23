"""Extract ranked reference lists for task_01 and task_02 from verified author tables."""
import argparse
from collections import Counter, defaultdict
import csv
from decimal import Decimal, InvalidOperation
import gzip
import hashlib
import heapq
import json
from pathlib import Path

DEFAULT_K = 100
MISSING = {'', 'NA', 'N/A', 'NaN', 'nan', 'NULL', 'null', '-', '.'}

# Each contrast is separate. labels follows group_cols, not the filename order.
# multiplier=1 keeps the reported sign; -1 reverses it to treatment/control.
FILE_CONFIGS = [{'file': 'GSE52778_Dex_vs_Untreated_gene_exp.diff.gz',
  'task': 'task_01',
  'sha256': '6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ('sample_1', 'sample_2'),
  'row_names': False,
  'contrasts': [{'labels': ('Dex', 'Untreated'), 'name': 'Dex_vs_Untreated', 'multiplier': -1}]},
 {'file': 'GSE100732_DESeq2.results.txt.gz',
  'task': 'task_02',
  'sha256': '0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df',
  'gene_col': '__rowname__',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': (),
  'row_names': True,
  'contrasts': [{'labels': (), 'name': 'Lrpprc_KO_vs_WT', 'multiplier': 1}]}]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(text):
    if text.strip() in MISSING:
        return None
    try:
        value = Decimal(text)
    except InvalidOperation as error:
        raise ValueError(f'Unrecognized numeric value: {text!r}') from error
    return None if value.is_nan() else value


def table_rows(path):
    with gzip.open(path, 'rt', encoding='utf-8-sig', newline='') as stream:
        yield from csv.reader(stream, delimiter='\t')


def read_groups(path, cfg):
    groups = defaultdict(list)
    reader = table_rows(path)
    try:
        header = next(reader)
        if cfg['row_names'] is True:
            header = ['__rowname__'] + header
        required = [cfg['gene_col'], cfg['lfc_col'], cfg['padj_col'], *cfg['group_cols']]
        if cfg['status_col']:
            required.append(cfg['status_col'])
        if len(set(header)) != len(header) or not set(required) <= set(header):
            raise ValueError('Missing or duplicated column names')
        for line, cells in enumerate(reader, 2):
            if len(cells) != len(header):
                raise ValueError(f'Column count mismatch on line {line}')
            row = dict(zip(header, cells))
            labels = tuple(row[c] for c in cfg['group_cols'])
            groups[labels].append((line, row))
    finally:
        reader.close()
    return groups


def extract(rows, cfg, contrast, k):
    counts = Counter()
    occurrences = defaultdict(list)
    for line, row in rows:
        identifier = row[cfg['gene_col']]
        if identifier.strip() not in MISSING:
            occurrences[identifier].append(line)
    duplicates = {key: lines for key, lines in occurrences.items() if len(lines) > 1}
    reviewed_duplicates = set(cfg.get('reviewed_duplicate_ids', []))
    if duplicates and set(duplicates) != reviewed_duplicates:
        examples = list(duplicates.items())[:10]
        raise ValueError(f'{len(duplicates)} duplicate IDs within this contrast; inspect rows, do not select the first: {examples}')
    candidates = []
    for line, row in rows:
        if cfg['status_col'] and row[cfg['status_col']] != 'OK':
            counts['invalid_status'] += 1
            continue
        identifier = row[cfg['gene_col']]
        lfc, padj = number(row[cfg['lfc_col']]), number(row[cfg['padj_col']])
        if identifier.strip() in MISSING or lfc is None or padj is None:
            counts['missing'] += 1
            continue
        if not padj.is_finite() or not Decimal(0) <= padj <= Decimal(1):
            raise ValueError(f'Invalid adjusted P value on line {line}: {row[cfg["padj_col"]]}')
        if lfc == 0:
            counts['zero_lfc'] += 1
            continue
        if contrast['multiplier'] == -1:
            lfc = lfc.copy_negate()
        candidates.append((identifier, lfc, padj, line))
    upward = [r for r in candidates if r[1] > 0]
    downward = [r for r in candidates if r[1] < 0]
    counts.update(rows=len(rows), up=len({r[0] for r in upward}), down=len({r[0] for r in downward}), duplicates=len(duplicates),
                  eligible_up_rows=len(upward), eligible_down_rows=len(downward),
                  infinite_lfc=sum(not r[1].is_finite() for r in candidates))
    if contrast['multiplier'] not in (-1, 1):
        return None, counts, '方向未确认；up/down 数量暂按原文件正负号记录。'
    if counts['up'] < k or counts['down'] < k:
        return None, counts, f'有效基因不足 K={k}，不补齐或自动降低 K。'
    rank_key = lambda row: (row[2], row[0])  # Decimal padj, then untouched ID string.
    chosen = {'up': sorted(upward, key=rank_key)[:k],
              'down': sorted(downward, key=rank_key)[:k]}
    answer = {direction: [r[0] for r in selected] for direction, selected in chosen.items()}
    if reviewed_duplicates & (set(answer['up']) | set(answer['down'])):
        return None, counts, 'A reviewed duplicate ID enters the selected top K; no rows were merged or discarded. Resolve the ambiguity before scoring.'
    for direction, pool in [('up', upward), ('down', downward)]:
        selected = answer[direction]
        expected = [r[0] for r in heapq.nsmallest(k, pool, key=rank_key)]
        if selected != expected or len(set(selected)) != k or not all(isinstance(g, str) for g in selected):
            raise ValueError(f'Ranking/uniqueness verification failed: {direction}')
        counts[f'selected_infinite_{direction}'] = sum(not r[1].is_finite() for r in chosen[direction])
    if set(answer['up']) & set(answer['down']):
        raise ValueError('up and down overlap')
    return answer, counts, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output-dir', type=Path, help='Root containing task directories with reference outputs')
    parser.add_argument('--k', type=int, default=DEFAULT_K)
    args = parser.parse_args()
    if args.k < 1:
        parser.error('K must be a positive integer')
    source = args.input_dir.resolve()
    output = (args.output_dir or source/'reference_json').resolve()
    if output == source:
        parser.error('Use a separate output directory')
    configs = FILE_CONFIGS.copy()
    entries, answers, before = [], {}, {}
    for cfg in configs:
        path = source/cfg['file']
        try:
            before[path] = sha256(path)
            if before[path] != cfg['sha256']:
                raise ValueError('Input hash changed; recheck column/contrast/direction configuration')
            groups = read_groups(path, cfg)
            expected = {tuple(c['labels']): c for c in cfg['contrasts']}
            for labels in sorted(set(groups) | set(expected)):
                contrast = expected.get(labels)
                entry = {'cfg': cfg, 'contrast': contrast}
                try:
                    if contrast is None or labels not in groups:
                        raise ValueError(f'Unconfigured or missing comparison labels: {labels}')
                    answer, counts, issue = extract(groups[labels], cfg, contrast, args.k)
                    entry.update(counts=counts, issue=issue)
                    if answer is not None:
                        name = (Path(cfg['task']) / 'reference' / f'top{args.k}.json').as_posix()
                        if name in answers:
                            raise ValueError(f'Duplicate output filename: {name}')
                        answers[name] = json.dumps(answer, ensure_ascii=False, indent=2)+'\n'
                        entry['output'] = name
                except (ValueError, InvalidOperation) as error:
                    entry['issue'] = str(error)
                entries.append(entry)
        except (OSError, ValueError, KeyError, StopIteration) as error:
            entries.append({'cfg': cfg, 'issue': str(error)})
    # Check only answer folders; the output root may also hold curator configs/manifests.
    existing = {p.relative_to(output).as_posix() for p in output.glob('task_*/reference/**/*.json')} if output.exists() else set()
    if existing - set(answers):
        raise SystemExit('Output folder contains stale/unrelated JSONs. Use a new --output-dir; nothing was overwritten.')
    for name, text in answers.items():
        path = output/name
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.read_text(encoding='utf-8') != text:
            raise SystemExit(f'Existing output differs: {path}. Use a new --output-dir.')
    for path, original_hash in before.items():
        if sha256(path) != original_hash:
            raise RuntimeError(f'Source file changed during extraction: {path}')
    output.mkdir(parents=True, exist_ok=True)
    for name, text in answers.items():
        path = output/name
        if not path.exists():
            with path.open('x', encoding='utf-8', newline='\n') as stream:
                stream.write(text)
    pending = sum(bool(e.get('issue')) for e in entries)
    print(f'Completed: {len(answers)} formal JSONs; {pending} pending comparisons. K={args.k}.')
    for entry in entries:
        if entry.get('output'):
            print(f'OK {entry["output"]}: eligible up={entry["counts"]["up"]}, down={entry["counts"]["down"]}')
        else:
            print(f'PENDING {entry["cfg"]["file"]}: {entry["issue"]}')


if __name__ == '__main__':
    main()
