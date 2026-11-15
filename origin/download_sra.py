"""Download full-quality SRA archives from a reviewed manifest; no read processing.

python origin/download_sra.py --manifest origin/sra_manifest.json --output-dir D:\\ma_lab\\deg_answer
Rerun to resume .part files and skip already verified archives.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import threading
import time
import urllib.error
import urllib.request

LOCK=threading.Lock()
CHUNK_BYTES=32*1024*1024

def transfer_range(item,path,start,end):
    """Persist one bounded range, resuming only a matching HTTP Content-Range."""
    expected=end-start+1
    for attempt in range(1,7):
        try:
            present=path.stat().st_size if path.exists() else 0
            if present>expected:raise ValueError('Range partial exceeds expected length')
            if present==expected:return
            begin=start+present
            req=urllib.request.Request(item['url'],headers={'User-Agent':'DEG-reference-curation/1.0','Range':f'bytes={begin}-{end}'})
            with urllib.request.urlopen(req,timeout=60) as response:
                if response.status!=206 or response.headers.get('Content-Range')!=f'bytes {begin}-{end}/{item["bytes"]}':
                    raise ValueError('Server returned an unexpected range; partials preserved')
                with path.open('ab' if path.exists() else 'xb') as out:
                    for block in iter(lambda:response.read(4*1024*1024),b''):
                        if shutil.disk_usage(path.parent).free<8*1024**3:raise OSError('Less than 8 GiB free')
                        if out.tell()+len(block)>expected:raise ValueError('Range response exceeds requested length')
                        out.write(block)
            if path.stat().st_size!=expected:raise IOError('Incomplete range response')
            return
        except (OSError,urllib.error.URLError) as e:
            if attempt==6:raise
            with LOCK:print(json.dumps({'run':item['run'],'range':f'{start}-{end}','retry':attempt,'error':str(e)}),flush=True)
            time.sleep(min(5*attempt,30))

def download_ranges(item,part,connections):
    """Append completed consecutive ranges; an existing .part stays a valid prefix."""
    chunks=part.with_name(part.name+'.chunks');chunks.mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=connections) as pool:
        while True:
            offset=part.stat().st_size if part.exists() else 0
            if offset>item['bytes']:raise ValueError('Partial file is larger than expected')
            if offset==item['bytes']:return chunks
            batch=[]
            for start in range(offset,min(item['bytes'],offset+connections*CHUNK_BYTES),CHUNK_BYTES):
                end=min(start+CHUNK_BYTES,item['bytes'])-1
                path=chunks/f'{start}-{end}.chunk'
                batch.append((path,pool.submit(transfer_range,item,path,start,end)))
            for path,future in batch:future.result()
            with part.open('ab' if part.exists() else 'xb') as out:
                for path,_ in batch:
                    with path.open('rb') as src:shutil.copyfileobj(src,out,4*1024*1024)
                out.flush()
            # Files are deleted only after their bytes have been appended and closed.
            for path,_ in batch:path.unlink()
def digest(path):
    h=hashlib.md5()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    return h.hexdigest()

def atomic_json(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    os.replace(tmp,path)

def download(item,root,connections=1):
    target=root/item['relative_path'];part=target.with_suffix(target.suffix+'.part')
    marker=target.with_suffix(target.suffix+'.verified.json')
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        valid=False
        if marker.exists():
            saved=json.loads(marker.read_text(encoding='utf-8'))
            valid=(saved.get('md5')==item['md5'] and saved.get('bytes')==target.stat().st_size==item['bytes'] and saved.get('mtime_ns')==target.stat().st_mtime_ns)
        if not valid:
            valid=target.stat().st_size==item['bytes'] and digest(target)==item['md5']
        if not valid:raise ValueError(f'Existing archive differs; not overwritten: {target}')
        atomic_json(marker,dict(run=item['run'],bytes=item['bytes'],md5=item['md5'],mtime_ns=target.stat().st_mtime_ns))
        return 'verified_existing'
    for attempt in range(1,7):
        try:
            offset=part.stat().st_size if part.exists() else 0
            if offset>item['bytes']:raise ValueError('Partial file is larger than expected')
            if offset<item['bytes'] and connections>1:
                download_ranges(item,part,connections)
            elif offset<item['bytes']:
                headers={'User-Agent':'DEG-reference-curation/1.0'}
                if offset:headers['Range']=f'bytes={offset}-'
                req=urllib.request.Request(item['url'],headers=headers)
                with urllib.request.urlopen(req,timeout=60) as response:
                    if offset and (response.status!=206 or not response.headers.get('Content-Range','').startswith(f'bytes {offset}-')):
                        raise ValueError('Server did not honor resume range; partial file preserved')
                    with part.open('ab' if part.exists() else 'xb') as out:
                        for block in iter(lambda:response.read(4*1024*1024),b''):
                            if shutil.disk_usage(root).free<8*1024**3:raise OSError('Less than 8 GiB free; download stopped')
                            out.write(block)
            if part.stat().st_size!=item['bytes']:raise IOError('Downloaded size mismatch')
            observed=digest(part)
            if observed!=item['md5']:raise ValueError('MD5 mismatch; partial file preserved for investigation')
            if target.exists():raise FileExistsError('Target appeared during download')
            part.rename(target)
            atomic_json(marker,dict(run=item['run'],bytes=item['bytes'],md5=observed,mtime_ns=target.stat().st_mtime_ns))
            chunks=part.with_name(part.name+'.chunks')
            if chunks.exists():
                # Remove only this downloader's range files, after full-file verification.
                for p in chunks.iterdir():
                    if p.is_file() and re.fullmatch(r'\d+-\d+\.chunk',p.name):p.unlink()
                if not any(chunks.iterdir()):chunks.rmdir()
            return 'downloaded_verified'
        except (OSError,urllib.error.URLError) as e:
            if attempt==6:raise
            with LOCK:print(json.dumps({'run':item['run'],'retry':attempt,'error':str(e)}),flush=True)
            time.sleep(min(5*attempt,30))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--workers',type=int,default=6)
    p.add_argument('--connections-per-file',type=int,default=1)
    args=p.parse_args()
    if not 1<=args.workers<=12:p.error('workers must be between 1 and 12')
    if not 1<=args.connections_per_file<=4 or args.workers*args.connections_per_file>32:
        p.error('Use 1-4 connections per file and at most 32 total connections')
    items=json.loads(args.manifest.read_text(encoding='utf-8'))['files']
    root=args.output_dir.resolve();root.mkdir(parents=True,exist_ok=True)
    for x in items:
        resolved=(root/x['relative_path']).resolve()
        if root not in resolved.parents:raise ValueError('Manifest path escapes output folder')
        if x['format']!='sra' or not x['url'].startswith('https://'):raise ValueError('Expected full SRA archive over HTTPS')
    remaining=sum(max(0,x['bytes']-(root/x['relative_path']).stat().st_size) if (root/x['relative_path']).exists() else max(0,x['bytes']-(root/x['relative_path']).with_suffix('.sra.part').stat().st_size) if (root/x['relative_path']).with_suffix('.sra.part').exists() else x['bytes'] for x in items)
    if remaining+8*1024**3>shutil.disk_usage(root).free:raise SystemExit('Insufficient space for all remaining archives plus 8 GiB reserve')
    report={'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'total_runs':len(items),'total_bytes':sum(x['bytes'] for x in items),'runs':{}}
    report_path=root/'sra_download_status.json'
    atomic_json(report_path,report)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures={pool.submit(download,item,root,args.connections_per_file):item for item in sorted(items,key=lambda x:x['bytes'])}
        for future in concurrent.futures.as_completed(futures):
            item=futures[future]
            try:entry={'status':future.result(),'bytes':item['bytes'],'path':item['relative_path']}
            except Exception as e:entry={'status':'failed','error':str(e),'path':item['relative_path']}
            report['runs'][item['run']]=entry
            atomic_json(report_path,report)
            print(json.dumps({'run':item['run'],**entry,'completed':len(report['runs']),'total':len(items)}),flush=True)
    report['finished_utc']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    atomic_json(report_path,report)
    if any(x['status']=='failed' for x in report['runs'].values()):raise SystemExit(1)

if __name__=='__main__':main()
