"""Extract ranked reference gene lists; never fit or rerun a DEG analysis.

Python standard library only. Place this script beside the seven source files.
    python extract_reference.py
    python extract_reference.py --k 50 --output-dir reference_json_top50

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


def read_groups(path, cfg):
    groups = defaultdict(list)
    with gzip.open(path, 'rt', encoding='utf-8-sig', newline='') as stream:
        reader = csv.reader(stream, delimiter='\t')
        header = next(reader)
        if cfg['row_names']:
            header = ['__rowname__'] + header  # R row names have no header cell.
        required = [cfg['gene_col'], cfg['lfc_col'], cfg['padj_col'], *cfg['group_cols']]
        if cfg['status_col']:
            required.append(cfg['status_col'])
        if len(set(header)) != len(header) or not set(required) <= set(header):
            raise ValueError('Missing or duplicated column names')
        for line, cells in enumerate(reader, 2):
            if len(cells) != len(header):
                raise ValueError(f'Column count mismatch on line {line}')
            row = dict(zip(header, cells))
            groups[tuple(row[c] for c in cfg['group_cols'])].append((line, row))
    return groups


def extract(rows, cfg, contrast, k):
    counts = Counter()
    occurrences = defaultdict(list)
    for line, row in rows:
        identifier = row[cfg['gene_col']]
        if identifier.strip() not in MISSING:
            occurrences[identifier].append(line)
    duplicates = {key: lines for key, lines in occurrences.items() if len(lines) > 1}
    if duplicates:
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
    counts.update(rows=len(rows), up=len(upward), down=len(downward), duplicates=0,
                  infinite_lfc=sum(not r[1].is_finite() for r in candidates))
    if contrast['multiplier'] not in (-1, 1):
        return None, counts, '方向未确认；up/down 数量暂按原文件正负号记录。'
    if len(upward) < k or len(downward) < k:
        return None, counts, f'有效基因不足 K={k}，不补齐或自动降低 K。'
    rank_key = lambda row: (row[2], row[0])  # Decimal padj, then untouched ID string.
    chosen = {'up': sorted(upward, key=rank_key)[:k],
              'down': sorted(downward, key=rank_key)[:k]}
    answer = {direction: [r[0] for r in selected] for direction, selected in chosen.items()}
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
    lines = [f'# DEG 参考答案提取记录（top{k}）', '',
             '仅提取作者现有结果，不重新运行 DEG。统一方向：处理组/对照组。',
             '有 status 列时仅保留 OK；排除缺失 ID/log2FC/校正 P 值及 log2FC=0；不使用 significant、原始 P 值或额外显著性/倍数阈值。',
             '分别按校正 P 值、原始 ID 字符串升序取前 K。Decimal 保留极小 P 值精度；版本号、逗号复合 ID、自定义 ID 不变。',
             '±inf 不是缺失值，且有明确方向：在 status=OK、校正 P 值有效时按符号保留，不额外删除。',
             '输入 SHA-256 已与作者公开文件逐字节核对；重跑脚本会核验已确认版本。重复 ID 或未配置比较会阻止相应比较进入正式答案。', '']
    for entry in entries:
        cfg, contrast = entry['cfg'], entry.get('contrast')
        lines += [f'## {cfg["file"]}', '',
                  f'- 列：ID=`{cfg["gene_col"]}`；log2FC=`{cfg["lfc_col"]}`；校正 P=`{cfg["padj_col"]}`；检验状态=`{cfg["status_col"] or "无状态列"}`。',
                  f'- ID 类型：{cfg["id_type"]}。']
        if contrast:
            lines += [f'- 处理组：{contrast["treatment"]}；对照组：{contrast["control"]}；标签：{contrast["labels"]}；翻转：{contrast["multiplier"] == -1}。',
                      f'- 方向依据：{contrast["evidence"]}']
        counts = entry.get('counts', {})
        if counts:
            lines += [f'- 行数 {counts["rows"]:,}；排除无效状态 {counts["invalid_status"]:,}、缺失 {counts["missing"]:,}、零 log2FC {counts["zero_lfc"]:,}；重复 ID {counts["duplicates"]}。',
                      f'- 方向统一后有效基因：up={counts["up"]:,}，down={counts["down"]:,}；有效 ±inf 共 {counts["infinite_lfc"]}，入选 up/down 分别 {counts["selected_infinite_up"]}/{counts["selected_infinite_down"]}。']
        lines += [f'- 输出：`{entry["output"]}`；已验证 up/down 各 {k} 个不同字符串、不相交、方向及排序正确。' if entry.get('output') else f'- 待确认：{entry["issue"]}',
                  f'- [作者文件]({cfg["source"]})；SHA-256：`{cfg["sha256"]}`。', '']
    pending = [e for e in entries if e.get('issue')]
    lines += ['## 未解决的问题', '', '无。' if not pending else '\n'.join(f'- {e["cfg"]["file"]}: {e["issue"]}' for e in pending), '',
              '## 方向核查补充与重跑', '',
              '- [Cuffdiff 官方格式说明](https://cole-trapnell-lab.github.io/cufflinks/cuffdiff/index.html)：log2FC 为第二组/第一组；q 为 FDR-adjusted P；OK 表示检验成功。',
              '- [GSE96962](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96962) 和[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5762668/)明确四个细胞类型/刺激对比及 solvent controls；表内 FPKM-control/FPKM-sample 和逐行比值核对共同确定方向，而非仅由文件名判断。',
              '- DESeq2 方向辅助来源：[作者现成表达表](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE100nnn/GSE100732/suppl/GSE100732_DESeq2.normalised_counts.txt.gz)，SHA-256 `c12f436e8d6cacb2aca6d48c34dcd4900e987bec3da2c05f083ce7e1fa27ec21`；[GEO 样本标注](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100732)：GSM2692145–2148 为 KO，GSM2692149–2152 为 WT，对应文库列见该文件方向依据。',
              '- DESeq2 核对示例：ENSMUSG00000005667.8 的 KO/WT 均值为 2340.875736/45.007997，作者 log2FC=+5.679036；ENSMUSG00000101111.1 的均值为 17836.530087/705964.212566，作者 log2FC=-5.306634。该核对只识别整体方向，不替换原始系数或重算 P 值；91 行简单均值方向与模型系数不同，仍严格使用原作者系数。',
              '- 原目录运行 `python extract_reference.py`；修改 K 可用 `python extract_reference.py --k 50 --output-dir reference_json_top50`。脚本离线运行，全部列名/比较/方向在 FILE_CONFIGS 中；新方向未核实时设 multiplier=None。']
    path.write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--k', type=int, default=DEFAULT_K)
    args = parser.parse_args()
    if args.k < 1:
        parser.error('K must be a positive integer')
    source = args.input_dir.resolve()
    output = (args.output_dir or source/'reference_json').resolve()
    if output == source:
        parser.error('Use a separate output directory')
    entries, answers, before = [], {}, {}
    for cfg in FILE_CONFIGS:
        path = source/cfg['file']
        try:
            before[path] = sha256(path)
            if before[path] != cfg['sha256']:
                raise ValueError('Input hash changed; recheck column/contrast/direction configuration')
            groups = read_groups(path, cfg)
            expected = {c['labels']: c for c in cfg['contrasts']}
            for labels in sorted(set(groups) | set(expected)):
                contrast = expected.get(labels)
                entry = {'cfg': cfg, 'contrast': contrast}
                try:
                    if contrast is None or labels not in groups:
                        raise ValueError(f'Unconfigured or missing comparison labels: {labels}')
                    answer, counts, issue = extract(groups[labels], cfg, contrast, args.k)
                    entry.update(counts=counts, issue=issue)
                    if answer is not None:
                        stem = cfg['file'].removesuffix('.gz').removesuffix('.txt')
                        name = f'{stem}__{contrast["name"]}_top{args.k}.json'
                        answers[name] = json.dumps(answer, ensure_ascii=False, indent=2)+'\n'
                        entry['output'] = name
                except (ValueError, InvalidOperation) as error:
                    entry['issue'] = str(error)
                entries.append(entry)
        except (OSError, ValueError, KeyError, StopIteration) as error:
            entries.append({'cfg': cfg, 'issue': str(error)})
    # Never leave stale or unrelated JSONs mixed with this run's formal answers.
    existing = {p.name for p in output.glob('*.json')} if output.exists() else set()
    if existing - set(answers):
        raise SystemExit('Output folder contains stale/unrelated JSONs. Use a new --output-dir; nothing was overwritten.')
    for name, text in answers.items():
        path = output/name
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
