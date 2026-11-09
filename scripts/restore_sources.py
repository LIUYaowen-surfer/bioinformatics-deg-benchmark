"""Restore missing originals from the pinned manifest; never overwrite or recompute counts."""
from pathlib import Path
import csv,hashlib,requests
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'curator_only/download_manifest.tsv').open(encoding='utf-8'),delimiter='\t'))
for row in rows:
 p=(ROOT/row['local_path']).resolve()
 if not p.is_relative_to(ROOT):raise RuntimeError('Path outside repository')
 if p.exists():
  if hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:raise RuntimeError('Existing original differs; refusing to overwrite: '+row['local_path'])
  print('Verified',row['local_path']);continue
 r=requests.get(row['source_url'],timeout=(30,180));r.raise_for_status()
 if hashlib.sha256(r.content).hexdigest()!=row['sha256']:raise RuntimeError('Remote contents changed; do not accept silently: '+row['source_url'])
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(r.content)
 print('Restored',row['local_path'])
