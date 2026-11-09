"""Verify delivered files, counts, metadata and lossless exports; does NOT analyze expression."""
from pathlib import Path
import csv,gzip,hashlib,json,tarfile,collections
ROOT=Path(__file__).resolve().parents[1]
def read(p):
 op=gzip.open if str(p).endswith('.gz') else open
 with op(p,'rt',encoding='utf-8',newline='') as f:return list(csv.reader(f,delimiter='\t'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(p):return list(csv.DictReader(p.open(encoding='utf-8'),delimiter='\t'))
manifest=table(ROOT/'curator_only/download_manifest.tsv')
for r in manifest:
 p=ROOT/r['local_path'];assert digest(p)==r['sha256'],p
for r in table(ROOT/'SHA256SUMS.tsv'):
 p=ROOT/r['path'];assert digest(p)==r['sha256'],p
 assert p.stat().st_size==int(r['size_bytes']),p
 assert p.stat().st_size<50*1024*1024,p
for ds,id,n,pcols,selected in [('skin','dataset_01',58302,34,34),('ishikawa','dataset_02',26364,8,4),('mammary','dataset_03',27179,12,4),('airway','dataset_04',63677,8,8),('pasilla','dataset_05',14599,7,7)]:
 folder=ROOT/'model_input'/id;rows=read(folder/'counts.tsv.gz');samples=table(folder/'samples.tsv')
 assert len(rows)-1==n and len(rows[0])-1==pcols
 assert rows[0][1:]==[r['matrix_column'] for r in samples]
 assert len(set(r[0] for r in rows[1:]))==n and all(r[0] for r in rows[1:])
 assert len(set(rows[0][1:]))==pcols
 assert all(len(r)==pcols+1 and all(x.isdigit() for x in r[1:]) for r in rows[1:])
 assert sum(x['use_primary']=='true' for x in samples)==selected
 if ds in ['skin','ishikawa','mammary']:
  original=read(next((ROOT/'curator_only'/ds/'original').glob('*counts*.gz')))
  offset=1 if ds=='ishikawa' else 2
  assert rows==[['gene_id']+original[0][offset:]]+[[r[0]]+r[offset:] for r in original[1:]]
  if offset==2: assert read(folder/'features.tsv.gz')==[['gene_id',original[0][1]]]+[[r[0],r[1]] for r in original[1:]]
 if ds in ['skin','airway']:
  pairs=collections.defaultdict(list)
  for r in samples:pairs[r['subject_id']].append(r['group'])
  assert all(len(v)==2 and len(set(v))==2 for v in pairs.values())
 if ds=='airway':
  stored=list(csv.DictReader((ROOT/'curator_only/airway/package_files/inst/extdata/sample_table.csv').open(encoding='utf-8')))
  exported=table(ROOT/'curator_only/airway/object_colData.tsv')
  assert len(stored)==len(exported)==8
  for a,b in zip(stored,exported):
   assert a['']==b['matrix_column']
   for k in a:
    if k:assert a[k]==b[k],(k,a[k],b[k])
  assert 'exact integer roundtrip verified' in (ROOT/'curator_only/airway/export_session.txt').read_text()
 if ds=='pasilla':
  assert rows==read(ROOT/'curator_only/pasilla/package_files/pasilla_gene_counts.tsv')
  ref=ROOT/'curator_only/pasilla/deseq2_reference/inst/extdata'
  assert gzip.decompress((ref/'pasilla_gene_counts.tsv.gz').read_bytes())==(ROOT/'curator_only/pasilla/package_files/pasilla_gene_counts.tsv').read_bytes()
  assert (ref/'pasilla_sample_annotation.csv').read_bytes()==(ROOT/'curator_only/pasilla/package_files/pasilla_sample_annotation.csv').read_bytes()
 for filename in ['README.md','task.md','samples.tsv','counts.tsv.gz']:assert (folder/filename).is_file()
 for filename in ['README.md','provenance.tsv','qc.json','sample_crosswalk.tsv']:assert (ROOT/'curator_only'/ds/filename).is_file()
 print(ds,'PASS',n,'x',pcols,'selected',selected)
print('PASS: original hashes, delivered checksums, all matrix/sample joins, unchanged count exports, paired designs, official-example equality and file-size checks. No DEG run.')
