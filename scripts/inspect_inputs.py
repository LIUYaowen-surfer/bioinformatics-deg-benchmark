from pathlib import Path
import gzip,tarfile,json
ROOT=Path(__file__).resolve().parents[1]
def soft_records(path):
 records=[];cur=None
 for line in gzip.open(path,'rt',encoding='utf-8'):
  line=line.rstrip('\r\n')
  if line.startswith('^SAMPLE = '):
   cur={'accession':[line.split(' = ',1)[1]]};records.append(cur)
  elif line.startswith('^'): cur=None
  elif cur is not None and ' = ' in line:
   k,v=line.split(' = ',1);cur.setdefault(k,[]).append(v)
 return records
if __name__=='__main__':
 for ds in ['skin','ishikawa','mammary','airway']:
  folder=ROOT/'curator_only'/ds/'original'
  records=soft_records(next(folder.glob('*family.soft.gz')))
  (ROOT/'curator_only'/ds/'geo_samples.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
  print('\nDATASET',ds)
  for s in records: print(s['accession'],s.get('!Sample_title'),s.get('!Sample_characteristics_ch1'))
  print('FIRST_PROCESSING',records[0].get('!Sample_data_processing'))
  for p in folder.glob('*counts*.gz'):
   print('COUNTS',p.name)
   with gzip.open(p,'rt') as f:
    for _ in range(3): print(f.readline().rstrip())
 for ds in ['airway','pasilla']:
  p=next((ROOT/'curator_only'/ds/'original').glob('*.tar.gz'))
  with tarfile.open(p) as tar:
   print('\nPACKAGE',ds,[(m.name,m.size) for m in tar.getmembers() if m.isfile()])
   target=ROOT/'_work'/'packages';target.mkdir(parents=True,exist_ok=True)
   tar.extractall(target,filter='data')
