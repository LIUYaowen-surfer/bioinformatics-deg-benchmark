"""Download immutable public inputs; no sequencing processing or DEG analysis."""
import argparse, csv, hashlib, json, time
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'curator_only' / 'download_manifest.tsv'
FIELDS = ['dataset','local_path','source_url','resolved_url','original_filename','retrieved_at_utc','size_bytes','sha256','version','role']

def fetch(dataset, url, relpath, version='', role='original'):
    dest = ROOT / relpath
    dest.parent.mkdir(parents=True, exist_ok=True)
    old = []
    if MANIFEST.exists():
        with MANIFEST.open(encoding='utf-8',newline='') as f: old = list(csv.DictReader(f,delimiter='\t'))
    records = [x for x in old if x['local_path']==relpath]
    if dest.exists():
        digest=hashlib.sha256(dest.read_bytes()).hexdigest()
        if records and digest==records[-1]['sha256']:
            print('VERIFIED',relpath,flush=True); return dest
        raise RuntimeError('Refusing to overwrite untracked or changed original: '+relpath)
    for attempt in range(3):
        try:
            r=requests.get(url,timeout=(30,180),headers={'User-Agent':'DEG-benchmark-curation/1.0 (public data research)'})
            r.raise_for_status()
            data=r.content
            if relpath.endswith(('.gz','.tgz')) and not data.startswith(b'\x1f\x8b'): raise ValueError('Expected gzip, got '+r.headers.get('Content-Type',''))
            if not data: raise ValueError('Empty response')
            dest.write_bytes(data)
            row=dict(zip(FIELDS,[dataset,relpath,url,r.url,url.split('/')[-1],datetime.now(timezone.utc).isoformat(),len(data),hashlib.sha256(data).hexdigest(),version,role]))
            MANIFEST.parent.mkdir(parents=True,exist_ok=True)
            with MANIFEST.open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader();w.writerows(old+[row])
            print('DOWNLOADED',relpath,len(data),flush=True);return dest
        except Exception as e:
            if attempt==2: raise
            print('RETRY',relpath,str(e),flush=True);time.sleep(2)

def main():
    jobs=[]
    for ds,gse,filename in [
        ('skin','GSE120783','GSE120783_raw_read_counts.txt.gz'),
        ('ishikawa','GSE109892','GSE109892_Ishi_RNAseq_allsets_raw.counts.txt.gz'),
        ('mammary','GSE60450','GSE60450_Lactation-GenewiseCounts.txt.gz'),
        ('airway','GSE52778',None)]:
        base=f'https://ftp.ncbi.nlm.nih.gov/geo/series/{gse[:-3]}nnn/{gse}'
        jobs.append((ds,f'{base}/soft/{gse}_family.soft.gz',f'curator_only/{ds}/original/{gse}_family.soft.gz','','GEO sample metadata'))
        if filename: jobs.append((ds,f'{base}/suppl/{filename}',f'curator_only/{ds}/original/{filename}','','author-deposited counts'))
    for ds,v in [('airway','1.32.0'),('pasilla','1.40.0')]:
        jobs.append((ds,f'https://bioconductor.org/packages/3.23/data/experiment/src/contrib/{ds}_{v}.tar.gz',f'curator_only/{ds}/original/{ds}_{v}.tar.gz',f'Bioconductor 3.23; {ds} {v}','package source archive'))
    errors=[]
    for job in jobs:
        try: fetch(*job)
        except Exception as e: errors.append({'job':job,'error':str(e)});print('FAILED',job[0],str(e),flush=True)
    (ROOT/'curator_only'/'acquisition_errors.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
    if errors: raise SystemExit(1)

if __name__=='__main__': main()
