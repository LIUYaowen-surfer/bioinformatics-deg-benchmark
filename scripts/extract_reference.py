"""Extract ranked reference gene lists; never fit or rerun a DEG analysis.

Python standard library only. All 23 reviewed file configurations are built in.
    python scripts/extract_reference.py
    python scripts/extract_reference.py --k 50 --output-dir reference_output_top50

Answers are written to <output-dir>/study_XX/reference/.
Use a new output root for legacy layouts. Eligibility counts are printed to stdout.

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
FILE_CONFIGS = [{'file': 'GSE52778_Dex_vs_Untreated_gene_exp.diff.gz',
  'study': 'study_01',
  'sha256': '6c6ca5ce509e98ea9d5fb9aef698b2a0fbf4c778997c7ceaf95a42cbf15eb63f',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ('sample_1', 'sample_2'),
  'row_names': False,
  'contrasts': [{'labels': ('Dex', 'Untreated'), 'name': 'Dex_vs_Untreated', 'multiplier': -1}]},
 {'file': 'GSE100732_DESeq2.results.txt.gz',
  'study': 'study_02',
  'sha256': '0f9b9bf95603221d1b19d40315c8f57b64e7a15f919ccaddb03ef0eef5b238df',
  'gene_col': '__rowname__',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': (),
  'row_names': True,
  'contrasts': [{'labels': (), 'name': 'Lrpprc_KO_vs_WT', 'multiplier': 1}]},
 {'file': 'GSE212471_si_CTRL-siSRSF1.gene_exp.diff.gz',
  'study': 'study_04',
  'sha256': '4c9f9e881aa7555dd47804b261c5753e13e1b48792d5f128a3d97226ae0641d1',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ('sample_1', 'sample_2'),
  'row_names': False,
  'contrasts': [{'labels': ('si_CTRL', 'si_SRSF1'), 'name': 'siSRSF1_vs_siCTRL', 'multiplier': 1}]},
 {'file': 'GSE96962_EC-IL-normalized-gene_exp.diff.gz',
  'study': 'study_03',
  'sha256': 'ca298b1efc7b2126adf7de67fb45b07641f29165c22448ccfc0faad1f98c9b5d',
  'gene_col': 'SeqID',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'FDR AdjP_value',
  'status_col': 'status',
  'group_cols': ('control', 'sample'),
  'row_names': False,
  'contrasts': [{'labels': ('q1', 'q2'), 'name': 'EC_IL1B_vs_EC_control', 'multiplier': 1}]},
 {'file': 'GSE96962_EC-TNF-normalized-gene_exp.diff.gz',
  'study': 'study_03',
  'sha256': '9196e77fbd9b1a0be2aff6a2eec8d4b24e69ee8b1b0d228e0eaf3752d12e4949',
  'gene_col': 'SeqID',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'FDR AdjP_value',
  'status_col': 'status',
  'group_cols': ('control', 'sample'),
  'row_names': False,
  'contrasts': [{'labels': ('q1', 'q2'), 'name': 'EC_TNFa_vs_EC_control', 'multiplier': 1}]},
 {'file': 'GSE96962_SMC--TNF-normalized-gene_exp.diff.gz',
  'study': 'study_03',
  'sha256': 'c5ba3c6c4106842333e78ea523fd16b6640104be5ab7c82af098b277e6532b09',
  'gene_col': 'SeqID',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'FDR AdjP_value',
  'status_col': 'status',
  'group_cols': ('control', 'sample'),
  'row_names': False,
  'contrasts': [{'labels': ('q1', 'q2'), 'name': 'SMC_TNFa_vs_SMC_control', 'multiplier': 1}]},
 {'file': 'GSE96962_SMC-IL-normalized-gene_exp.diff.gz',
  'study': 'study_03',
  'sha256': '0aeeb588c872cccaa43f9e549092ba201e671fd506e6272f235808fcd7f11319',
  'gene_col': 'SeqID',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'FDR AdjP_value',
  'status_col': 'status',
  'group_cols': ('control', 'sample'),
  'row_names': False,
  'contrasts': [{'labels': ('q1', 'q2'), 'name': 'SMC_IL1B_vs_SMC_control', 'multiplier': 1}]},
 {'file': 'study_05/author_results/GSE37703_hiseq_cuffdiff_gene_exp.diff.gz',
  'study': 'study_05',
  'sha256': 'd4859e418f38f8c14b79ce27a477f318f4a9001a4f191790b9c3885661564075',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': ['Lung_Scramble', 'Lung_A1KD'], 'name': 'HOXA1_KD_vs_scramble', 'multiplier': 1}]},
 {'file': 'study_06/author_results/GSE60328_gene_exp.diff.gz',
  'study': 'study_06',
  'sha256': '6d520c57a947f2f8019b31fa76af7617e458d6b49adce49315920c66811b2355',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': ['Scr_KD', 'IR_KD'], 'name': 'INSR_KD_vs_scramble', 'multiplier': 1}]},
 {'file': 'study_07/author_results/GSE76682_EB_AM580gene_exp.diff.gz',
  'study': 'study_07',
  'sha256': 'fc9c4e9cea5f137d6aa53b942f3bf0f894c54943864522da7818e28a52218ae3',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': True,
  'contrasts': [{'labels': ['q1', 'q3'], 'name': 'AM580_vs_DMSO_day6', 'multiplier': 1}]},
 {'file': 'study_08/author_results/GSE89238_SET2_KO_DESeq2_output.txt.gz',
  'study': 'study_08',
  'sha256': 'b783572da8b31661f49b4bbbf8daad7def5efd23d27a683c53abd78477db166c',
  'gene_col': 'gene_id',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'set2_KO_vs_WT', 'multiplier': 1}]},
 {'file': 'study_09/author_results/GSE100077_DifferentialExpression.csv.gz',
  'study': 'study_09',
  'sha256': '064b53dacc025859df89af5c756514b948d0bc47812a5e343deba65c209a52e3',
  'gene_col': 'gene',
  'lfc_col': 'logFC',
  'padj_col': 'adj.P.Val',
  'status_col': None,
  'group_cols': [],
  'row_names': False,
  'delimiter': ',',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'cord_blood_vs_adult', 'multiplier': 1}]},
 {'file': 'study_10/author_results/GSE133436_gene_exp_oldYoung_.diff.gz',
  'study': 'study_10',
  'sha256': '103719a4a6dcc7a151be67f5e2150accafa22f189c184b1be0a1d506ff67cf5a',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': ['old', 'young'], 'name': 'old_vs_adult', 'multiplier': -1}]},
 {'file': 'study_11/author_results/GSE164712_gene_exp.diff.gz',
  'study': 'study_11',
  'sha256': '40dce9716d3b414d69b183b4685dff9889ed347e3e089db9220627630fb10fc5',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': ['WT_0h', 'DKO_0h'], 'name': 'Tcf1_Lef1_DKO_vs_WT', 'multiplier': 1}]},
 {'file': 'study_12/author_results/GSE193247_gene_exp.diff.gz',
  'study': 'study_12',
  'sha256': 'cb03676ee7a06168098252f417ed2631778a70f3daad04d2bcc1572d17b32fed',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': True,
  'contrasts': [{'labels': ['Col0', 'mfl1'], 'name': 'mfl1_vs_Col0', 'multiplier': 1}]},
 {'file': 'study_13/author_results/GSE207163_RNA-seq.xlsx',
  'study': 'study_13',
  'sha256': '42d2b2b2b351ee256355d12feef0327abfecd3b81bb716a77f6e2ff57919203e',
  'gene_col': 'gene',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': False,
  'delimiter': '\t',
  'sheet': 'neuron.Mut.1vsWT_day15',
  'selected_only': False,
  'reviewed_duplicate_ids': ['44621', '44622'],
  'contrasts': [{'labels': [], 'name': 'Top1_Mut1_vs_WT_day15', 'multiplier': 1}]},
 {'file': 'study_14/author_results/GSE218205_gene_exp.diff_bam_vs_bam_KD_meiP26.txt.gz',
  'study': 'study_14',
  'sha256': '7a056b984b2d5e5e01a42ae2e760d547fe3423bdc634ce275f4b28b1dd299e3c',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'reviewed_duplicate_ids': ['Chd64'],
  'contrasts': [{'labels': ['bam', 'bam_KD_meiP26'], 'name': 'MeiP26_KD_vs_bam', 'multiplier': 1}]},
 {'file': 'study_15/author_results/GSE223666_CTRL_SUZ12KO_stats_paired.txt.gz',
  'study': 'study_15',
  'sha256': '885a1ffa50d8d1923b33cbc9d931f73c755121dd74114d2516c1fdc225285c36',
  'gene_col': '__rowname__',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': True,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'Suz12_KO_vs_WT_ESC', 'multiplier': 1}]},
 {'file': 'study_16/author_results/GSE230334_gene_exp.diff.gz',
  'study': 'study_16',
  'sha256': 'f7d33e90b0e1bedb27b0d3814c48a4c13264bbe0a9aaec82b6f7c8d5db7b090e',
  'gene_col': 'gene_id',
  'lfc_col': 'log2(fold_change)',
  'padj_col': 'q_value',
  'status_col': 'status',
  'group_cols': ['sample_1', 'sample_2'],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': ['q1', 'q2'], 'name': 'Lonp1_KO_vs_control', 'multiplier': 1}]},
 {'file': 'study_17/author_results/GSE243105_sign_siOGT_control_genes_with_Batch_all.csv.gz',
  'study': 'study_17',
  'sha256': '776b74bb701d48ecaf6e1e715b96859f6ab68c31e7b274d9d121b7267aba27d5',
  'gene_col': '__rowname__',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': 'blank',
  'delimiter': ',',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'siOGT_vs_siControl', 'multiplier': 1}]},
 {'file': 'study_18/author_results/GSE250602_DESeq2_CT26_tumors_Control_vs_KO.csv.gz',
  'study': 'study_18',
  'sha256': '949d70e15c7d8e2feffd31086fe9384cdc47b1f6a13d2ac38ca4b413281cfe2e',
  'gene_col': '__rowname__',
  'lfc_col': 'log2FoldChange',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': 'blank',
  'delimiter': ',',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'Sun1_KO_vs_control_tumors', 'multiplier': -1}]},
 {'file': 'study_19/author_results/GSE269122_ctrl_vs_Sox10ko.xlsx',
  'study': 'study_19',
  'sha256': '61b8668cb0b36764cf20d494c307af5d0265526c62a9e04a342c78196179572b',
  'gene_col': 'GeneID',
  'lfc_col': 'log2(FC)',
  'padj_col': 'padj',
  'status_col': None,
  'group_cols': [],
  'row_names': False,
  'delimiter': '\t',
  'sheet': 'Rohdaten',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'Sox10_KO_vs_control', 'multiplier': 1}]},
 {'file': 'study_20/author_results/GSE288157_DESeq2_summary.txt.gz',
  'study': 'study_20',
  'sha256': '46dd0af492844ab6cbdd9183bb5d42e47c77915c00c92273e7061932c7b7ff4e',
  'gene_col': 'Ens_ID',
  'lfc_col': 'Condition_Emb_0.7mMvs96wp_l2fc',
  'padj_col': 'Condition_Emb_0.7mMvs96wp_padj',
  'status_col': None,
  'group_cols': [],
  'row_names': False,
  'delimiter': '\t',
  'selected_only': False,
  'contrasts': [{'labels': [], 'name': 'hydrogel_0p7mM_vs_unembedded', 'multiplier': 1}]}]


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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output-dir', type=Path, help='Root containing study_XX/reference/ folders')
    parser.add_argument('--k', type=int, default=DEFAULT_K)
    args = parser.parse_args()
    if args.k < 1:
        parser.error('K must be a positive integer')
    source = args.input_dir.resolve()
    output = (args.output_dir or source/'reference_json').resolve()
    if output == source:
        parser.error('Use a separate output directory')
    configs = FILE_CONFIGS.copy()
    if any(not re.fullmatch(r'study_[0-9]{2}', cfg.get('study', '')) for cfg in configs):
        parser.error('Each file configuration needs a study_XX identifier')
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
                        name = (Path(cfg['study']) / 'reference' / f'{stem}__{contrast["name"]}_top{args.k}.json').as_posix()
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
    legacy = [*output.glob('*_top*.json'), *output.glob('study_*/*_top*.json'),
              *output.glob('reference_json/**/*.json')]
    if legacy:
        raise SystemExit('Legacy answer layout detected. Move it to study_XX/reference/ or use a new --output-dir; nothing was overwritten.')
    existing = {p.relative_to(output).as_posix() for p in output.glob('study_*/reference/**/*.json')} if output.exists() else set()
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
