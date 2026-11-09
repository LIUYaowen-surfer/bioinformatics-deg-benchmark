"""Read-only acquisition of public documentation; full papers stay local in _work."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import requests, json, hashlib
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
SOURCES={
 'skin_paper':'https://pmc.ncbi.nlm.nih.gov/articles/PMC6814545/',
 'ishikawa_paper':'https://pmc.ncbi.nlm.nih.gov/articles/PMC5870123/',
 'airway_paper':'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099625',
 'pasilla_paper':'https://pmc.ncbi.nlm.nih.gov/articles/PMC3032923/',
 'mammary_paper':'https://publications.wehi.edu.au/document/127',
 'airway_vignette':'https://bioconductor.org/packages/3.23/data/experiment/vignettes/airway/inst/doc/airway.html',
 'pasilla_vignette':'https://bioconductor.org/packages/3.23/data/experiment/vignettes/pasilla/inst/doc/create_objects.html',
 'deseq2_vignette':'https://bioconductor.org/packages/3.23/bioc/vignettes/DESeq2/inst/doc/DESeq2.html',
 'ncbi_policy':'https://www.ncbi.nlm.nih.gov/home/about/policies/',
 'geo_disclaimer':'https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html',
 'github_limits':'https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github',
 'mammary_targets':'https://bioinf.wehi.edu.au/edgeR/MiMB2016/targets.txt',
}
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=90);r.raise_for_status()
  ext='.pdf' if r.content.startswith(b'%PDF') else '.html'
  folder=ROOT/'_work'/'sources';folder.mkdir(parents=True,exist_ok=True)
  p=folder/(name+ext);p.write_bytes(r.content)
  if ext=='.html': p.with_suffix('.txt').write_text(BeautifulSoup(r.content,'html.parser').get_text('\n',strip=True),encoding='utf-8')
  return dict(source_id=name,url=url,resolved_url=r.url,local_path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(r.content).hexdigest(),size_bytes=len(r.content),retrieved_at_utc=datetime.now(timezone.utc).isoformat(),status='downloaded; content requires review')
 except Exception as e: return dict(source_id=name,url=url,status=str(e))
with ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(get,SOURCES.items()))
(ROOT/'curator_only'/'documentation_sources.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
for x in rows: print(x['source_id'],x['status'],x.get('size_bytes'),flush=True)
