"""Extract ranked reference gene lists; never fit or rerun a DEG analysis.

Python standard library only. Seven original configurations are built in;
--config reference_configs.json adds the sixteen reviewed study comparisons.
    python extract_reference.py
    python extract_reference.py --config reference_configs.json
    python extract_reference.py --config reference_configs.json --k 50 --output-dir reference_json_top50

Edit FILE_CONFIGS to change a column, contrast, or confirmed direction.
Set multiplier=None for an unconfirmed contrast; it will not produce a JSON.
The input SHA-256 values bind the reviewed directions to these exact files.
"""
import argparse
from collections import Counter, defaultdict
import csv
from decimal import Decimal, InvalidOperation
import gzip
import hashlib
import heapq
import json
from pathlib import Path
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET

DEFAULT_K = 100
MISSING = {'', 'NA', 'N/A', 'NaN', 'nan', 'NULL', 'null', '-', '.'}

# Each contrast is separate. labels follows group_cols, not the filename order.
# multiplier=1 keeps the reported sign; -1 reverses it to treatment/control.
FILE_CONFIGS = [
    dict(file='GSE52778_Dex_vs_Untreated_gene_exp.diff.gz',
         gene_col='gene_id', lfc_col='log2(fold_change)', padj_col='q_value', status_col='status',
         group_cols=('sample_1', 'sample_2'), row_names=False,
         id_type='作者 gene_id：symbol 式标签，含逗号连接的复合 ID，均原样保留',
         sha256='6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_Dex_vs_Untreated_gene_exp.diff.gz',
         contrasts=[dict(labels=('Dex', 'Untreated'), treatment='Dex', control='Untreated',
                         multiplier=-1, name='Dex_vs_Untreated',
                         evidence='文件内 sample_1=Dex、sample_2=Untreated；Cuffdiff 的 log2FC=log2(value_2/value_1)，故原方向是 Untreated/Dex。13,370 个 OK 且两侧表达量为正的有限值行通过数值核对（绝对误差≤1e-4）；翻转符号。')]),
    dict(file='GSE100732_DESeq2.results.txt.gz',
         gene_col='__rowname__', lfc_col='log2FoldChange', padj_col='padj', status_col=None,
         group_cols=(), row_names=True,
         id_type='原文件无表头的首列行名：带版本号的 ENSMUSG ID 与作者自定义线粒体 ID（例如 mt-Nd4l_4）',
         sha256='0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.results.txt.gz',
         contrasts=[dict(labels=(), treatment='Lrpprc knockout', control='wild type',
                         multiplier=1, name='Lrpprc_KO_vs_WT',
                         evidence='结果表未显式保存 contrast。通过作者现成 normalized-counts 表与 GEO 样本标注交叉核对：KO 列 55219/55221/55223/55233，WT 列 55225/55227/55229/55231。19,866/19,957 个有效基因的系数符号与 KO/WT 均值方向一致，两个方向最靠前的基因亦一致，确认整体方向为 KO/WT；不翻转。不用均值替换系数，不删除其余 91 行。')]),
    dict(file='GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz',
         gene_col='gene_id', lfc_col='log2(fold_change)', padj_col='q_value', status_col='status',
         group_cols=('sample_1', 'sample_2'), row_names=False,
         id_type='原始 ENSG gene_id，保留版本后缀',
         sha256='4c9f9e881aa7555dd47804b261c5753e13e1b48792d5f128a3d97226ae0641d1',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212471/suppl/GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz',
         contrasts=[dict(labels=('si_CTRL', 'si_SRSF1'), treatment='si_SRSF1', control='si_CTRL',
                         multiplier=1, name='siSRSF1_vs_siCTRL',
                         evidence='文件内 sample_1=si_CTRL、sample_2=si_SRSF1；按 Cuffdiff 定义为 si_SRSF1/si_CTRL。20,079 个 OK 且两侧表达量为正的有限值行通过 log2(value_2/value_1) 核对（绝对误差≤1e-4）；不翻转。')]),
    dict(file='GSE96962_EC-IL-normalized-gene_exp.diff.gz',
         gene_col='SeqID', lfc_col='log2(fold_change)', padj_col='FDR AdjP_value', status_col='status',
         group_cols=('control', 'sample'), row_names=False, id_type='作者原始 SeqID（symbol 式标识）',
         sha256='ca298b1efc7b2126adf7de67fb45b07641f29165c22448ccfc0faad1f98c9b5d',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-IL-normalized-gene_exp.diff.gz',
         contrasts=[dict(labels=('q1', 'q2'), treatment='EC IL-1β', control='EC vehicle control',
                         multiplier=1, name='EC_IL1B_vs_EC_control',
                         evidence='作者 GEO 提交及论文的 EC/IL-1β 对比；表内 control=q1、sample=q2，表达列明确标为 FPKM-control/FPKM-sample。10,695 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。')]),
    dict(file='GSE96962_EC-TNF-normalized-gene_exp.diff.gz',
         gene_col='SeqID', lfc_col='log2(fold_change)', padj_col='FDR AdjP_value', status_col='status',
         group_cols=('control', 'sample'), row_names=False, id_type='作者原始 SeqID（symbol 式标识）',
         sha256='9196e77fbd9b1a0be2aff6a2eec8d4b24e69ee8b1b0d228e0eaf3752d12e4949',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_EC-TNF-normalized-gene_exp.diff.gz',
         contrasts=[dict(labels=('q1', 'q2'), treatment='EC TNF-α', control='EC vehicle control',
                         multiplier=1, name='EC_TNFa_vs_EC_control',
                         evidence='作者 GEO 提交及论文的 EC/TNF-α 对比；control=q1、sample=q2。10,791 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。')]),
    dict(file='GSE96962_SMC--TNF-normalized-gene_exp.diff.gz',
         gene_col='SeqID', lfc_col='log2(fold_change)', padj_col='FDR AdjP_value', status_col='status',
         group_cols=('control', 'sample'), row_names=False, id_type='作者原始 SeqID（symbol 式标识）',
         sha256='c5ba3c6c4106842333e78ea523fd16b6640104be5ab7c82af098b277e6532b09',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC--TNF-normalized-gene_exp.diff.gz',
         contrasts=[dict(labels=('q1', 'q2'), treatment='SMC TNF-α', control='SMC vehicle control',
                         multiplier=1, name='SMC_TNFa_vs_SMC_control',
                         evidence='作者 GEO 提交及论文的 SMC/TNF-α 对比；control=q1、sample=q2。11,434 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。')]),
    dict(file='GSE96962_SMC-IL-normalized-gene_exp.diff.gz',
         gene_col='SeqID', lfc_col='log2(fold_change)', padj_col='FDR AdjP_value', status_col='status',
         group_cols=('control', 'sample'), row_names=False, id_type='作者原始 SeqID（symbol 式标识）',
         sha256='0aeeb588c872cccaa43f9e549092ba201e671fd506e6272f235808fcd7f11319',
         source='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96962/suppl/GSE96962_SMC-IL-normalized-gene_exp.diff.gz',
         contrasts=[dict(labels=('q1', 'q2'), treatment='SMC IL-1β', control='SMC vehicle control',
                         multiplier=1, name='SMC_IL1B_vs_SMC_control',
                         evidence='作者 GEO 提交及论文的 SMC/IL-1β 对比；control=q1、sample=q2。11,136 个 OK 且两侧表达量为正的有限值行符合 log2(FPKM-sample/FPKM-control)（误差≤1e-4）；不翻转。')]),
]


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


def xlsx_rows(path, sheet_name):
    """Read stored cell values without recalculating or editing the workbook."""
    ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as book:
        shared = []
        if 'xl/sharedStrings.xml' in book.namelist():
            shared = [''.join(si.itertext()) for si in ET.fromstring(book.read('xl/sharedStrings.xml')).findall('x:si', ns)]
        rels = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(book.read('xl/_rels/workbook.xml.rels'))}
        sheets = ET.fromstring(book.read('xl/workbook.xml')).findall('x:sheets/x:sheet', ns)
        chosen = [s for s in sheets if s.attrib['name'] == sheet_name]
        if len(chosen) != 1:
            raise ValueError(f'Missing or ambiguous worksheet: {sheet_name}')
        relation = chosen[0].attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
        target = rels[relation]
        member = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl', target))
        with book.open(member) as stream:
            for _, row in ET.iterparse(stream, events=('end',)):
                if row.tag != '{' + ns['x'] + '}row':
                    continue
                values = {}
                for cell in row.findall('x:c', ns):
                    letters = re.match(r'[A-Z]+', cell.attrib['r']).group()
                    index = 0
                    for c in letters:
                        index = index * 26 + ord(c) - ord('A') + 1
                    v = cell.find('x:v', ns)
                    inline = cell.find('x:is', ns)
                    text = v.text if v is not None and v.text is not None else ''.join(inline.itertext()) if inline is not None else ''
                    if cell.attrib.get('t') == 's':
                        text = shared[int(text)]
                    if cell.attrib.get('t') == 'e' or (cell.find('x:f', ns) is not None and v is None):
                        raise ValueError(f'Unusable formula/cache at {sheet_name}!{cell.attrib["r"]}')
                    values[index - 1] = text
                if values:
                    yield [values.get(i, '') for i in range(max(values) + 1)]
                row.clear()


def table_rows(path, cfg):
    if path.suffix == '.xlsx':
        yield from xlsx_rows(path, cfg['sheet'])
    else:
        opener = gzip.open if path.suffix == '.gz' else open
        with opener(path, 'rt', encoding='utf-8-sig', newline='') as stream:
            yield from csv.reader(stream, delimiter=cfg.get('delimiter', '\t'))


def read_groups(path, cfg):
    groups = defaultdict(list)
    reader = table_rows(path, cfg)
    try:
        header = next(reader)
        if cfg['row_names'] is True:
            header = ['__rowname__'] + header
        elif cfg['row_names'] == 'blank':
            if header[0] != '':
                raise ValueError('Expected an explicitly blank leading header cell')
            header[0] = '__rowname__'
        required = [cfg['gene_col'], cfg['lfc_col'], cfg['padj_col'], *cfg['group_cols']]
        if cfg['status_col']:
            required.append(cfg['status_col'])
        if len(set(header)) != len(header) or not set(required) <= set(header):
            raise ValueError('Missing or duplicated column names')
        selected = {tuple(c['labels']) for c in cfg['contrasts']}
        ignored = Counter()
        for line, cells in enumerate(reader, 2):
            if path.suffix == '.xlsx' and len(cells) < len(header):
                cells += [''] * (len(header) - len(cells))
            if len(cells) != len(header):
                raise ValueError(f'Column count mismatch on line {line}')
            row = dict(zip(header, cells))
            labels = tuple(row[c] for c in cfg['group_cols'])
            if cfg.get('selected_only') and labels not in selected:
                ignored[labels] += 1
                continue
            groups[labels].append((line, row))
        cfg['_other_comparisons'] = {str(k): v for k, v in ignored.items()}
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


def write_log(path, entries, k):
    lines = [f'# Reference extraction record (top{k})', '',
             'Only existing author DEG results are extracted. Direction is treated/control.',
             'Use status=OK when a test-status column exists. Exclude missing IDs, log2FC or adjusted P values and log2FC=0. No significant-column, raw-P, extra FDR or fold-change filter is applied.',
             'Within each direction, sort by adjusted P value and then the unchanged gene-ID string. Decimal parsing preserves the stored numerical precision. Signed infinite FC values are retained when the original test is valid; they are counted below.',
             'Each input hash binds the reviewed columns, comparison and direction to the inspected author file. Reviewed duplicate IDs are never merged or reduced to the first row; if any enters top K, formal output is blocked.', '']
    for entry in entries:
        cfg, contrast = entry['cfg'], entry.get('contrast')
        lines += [f'## {cfg.get("study", "Original study")} / {Path(cfg["file"]).name}', '',
                  f'- Source: [{Path(cfg["file"]).name}]({cfg["source"]}).',
                  f'- SHA-256: `{cfg["sha256"]}`.',
                  f'- Fields: ID=`{cfg["gene_col"]}`, log2FC=`{cfg["lfc_col"]}`, adjusted P=`{cfg["padj_col"]}`, status=`{cfg["status_col"] or "none"}`.',
                  f'- ID type: {cfg["id_type"]}.']
        if cfg.get('sheet'):
            lines += [f'- Worksheet: `{cfg["sheet"]}`. Other worksheets are not pooled.']
        if contrast:
            lines += [f'- Treated: {contrast["treatment"]}; control: {contrast["control"]}; file labels: `{contrast["labels"]}`; sign multiplier: `{contrast["multiplier"]}`.',
                      f'- Direction evidence: {contrast["evidence"]}']
        counts = entry.get('counts', {})
        if counts:
            lines += [f'- Source rows: {counts["rows"]:,}. Excluded: invalid status {counts["invalid_status"]:,}, missing {counts["missing"]:,}, zero FC {counts["zero_lfc"]:,}. Duplicate IDs in source: {counts["duplicates"]}.',
                      f'- Eligible distinct IDs: up={counts["up"]:,}, down={counts["down"]:,}. Eligible signed-infinite FC rows: {counts["infinite_lfc"]}; selected up/down: {counts["selected_infinite_up"]}/{counts["selected_infinite_down"]}.']
        if cfg.get('duplicate_review'):
            lines += [f'- Duplicate review: {cfg["duplicate_review"]} All source rows remain in ranking.']
        if cfg.get('_other_comparisons'):
            lines += [f'- Other comparison blocks, recorded but outside this selected task: `{cfg["_other_comparisons"]}`.']
        if entry.get('output'):
            lines += [f'- Output: [{entry["output"]}]({entry["output"]}). Verified: {k} different strings per direction, disjoint lists, correct signs and ordering.']
        else:
            lines += [f'- Pending: {entry["issue"]}']
        lines += ['']
    pending = [e for e in entries if e.get('issue')]
    lines += ['## Pending comparisons', '', 'None for this K.' if not pending else '\n'.join(f'- {e["cfg"]["file"]}: {e["issue"]}' for e in pending), '',
              'Cuffdiff format reference: https://cole-trapnell-lab.github.io/cufflinks/cuffdiff/index.html',
              'The first seven configurations retain the previously reviewed settings; their evidence is preserved verbatim. Newly reviewed settings are in reference_configs.json. Use --k and a new --output-dir to change K; an ambiguous duplicate entering a larger K will block that comparison.', '']
    path.write_text('\n'.join(lines), encoding='utf-8', newline='\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--k', type=int, default=DEFAULT_K)
    parser.add_argument('--config', type=Path, help='Additional reviewed per-file JSON settings; appended to the seven original files')
    args = parser.parse_args()
    if args.k < 1:
        parser.error('K must be a positive integer')
    source = args.input_dir.resolve()
    output = (args.output_dir or source/'reference_json').resolve()
    if output == source:
        parser.error('Use a separate output directory')
    configs = FILE_CONFIGS.copy()
    if args.config:
        configs += json.loads(args.config.read_text(encoding='utf-8'))['files']
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
                        stem = Path(cfg['file']).name.removesuffix('.gz').removesuffix('.txt').removesuffix('.csv').removesuffix('.xlsx')
                        name = (Path(cfg.get('output_subdir', '')) / f'{stem}__{contrast["name"]}_top{args.k}.json').as_posix()
                        if name in answers:
                            raise ValueError(f'Duplicate output filename: {name}')
                        answers[name] = json.dumps(answer, ensure_ascii=False, indent=2)+'\n'
                        entry['output'] = name
                except (ValueError, InvalidOperation) as error:
                    entry['issue'] = str(error)
                entries.append(entry)
        except (OSError, ValueError, KeyError, StopIteration) as error:
            entries.append({'cfg': cfg, 'issue': str(error)})
    # Never leave stale or unrelated JSONs mixed with this run's formal answers.
    existing = {p.relative_to(output).as_posix() for p in output.rglob('*.json')} if output.exists() else set()
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
    write_log(output/'extraction_log.md', entries, args.k)
    if args.config:
        # Machine-readable audit is kept outside the strict reference-JSON tree.
        report = [{'source':e['cfg']['file'], 'output':e.get('output'), 'issue':e.get('issue'),
                   'counts':dict(e.get('counts',{})), 'contrast':e.get('contrast'),
                   'other_comparisons':e['cfg'].get('_other_comparisons',{})} for e in entries]
        (output.parent/(output.name+'_audit.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    pending = sum(bool(e.get('issue')) for e in entries)
    print(f'Completed: {len(answers)} formal JSONs; {pending} pending comparisons. K={args.k}.')
    for entry in entries:
        if entry.get('output'):
            print(f'OK {entry["output"]}: eligible up={entry["counts"]["up"]}, down={entry["counts"]["down"]}')
        else:
            print(f'PENDING {entry["cfg"]["file"]}: {entry["issue"]}')
    print(f'Record: {output / "extraction_log.md"}')


if __name__ == '__main__':
    main()
