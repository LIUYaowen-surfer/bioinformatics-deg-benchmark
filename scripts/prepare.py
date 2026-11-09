"""Lossless format exports, explicit sample joins and structural QC only."""
from pathlib import Path
import csv,gzip,hashlib,json,tarfile,collections,re,shutil,sys,platform
from inspect_inputs import soft_records
ROOT=Path(__file__).resolve().parents[1]
DATASETS={'skin':'dataset_01','ishikawa':'dataset_02','mammary':'dataset_03','airway':'dataset_04','pasilla':'dataset_05'}
DERIVED=[]
UNKNOWN='待核实'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write_tsv(p,rows,fields=None):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 if fields is None: fields=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def read_table(p):
 op=gzip.open if str(p).endswith('.gz') else open
 with op(p,'rt',encoding='utf-8',newline='') as f:return list(csv.reader(f,delimiter='\t'))
def gz_table(p,rows):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('wb') as raw:
  with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as z:
   import io
   with io.TextIOWrapper(z,encoding='utf-8',newline='') as t:
    csv.writer(t,delimiter='\t',lineterminator='\n').writerows(rows)
def member(ds,archive,name,out):
 p=ROOT/'curator_only'/ds/'original'/archive
 with tarfile.open(p) as t: data=t.extractfile(name).read()
 dest=ROOT/out;dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists() and dest.read_bytes()!=data: raise RuntimeError('changed extracted source '+out)
 dest.write_bytes(data)
 DERIVED.append((ds,out,[str(p.relative_to(ROOT)).replace('\\','/')],'byte-identical archive member: '+name))
 return dest
def chars(s):return dict(x.split(': ',1) for x in s.get('!Sample_characteristics_ch1',[]) if ': ' in x)
def base(col,s=None):
 return dict(matrix_column=col,original_sample_id=s['accession'][0] if s else UNKNOWN,
  group=UNKNOWN,use_primary='false',use_secondary='false',subject_id='NA',biological_replicate='NA',
  replicate_type=UNKNOWN,cell_type='NA',stage='NA',batch=UNKNOWN,sequencing_type=UNKNOWN,
  time_hours='NA',metadata_status='verified' if s else UNKNOWN)
def cross(col,s,evidence,status='verified'):
 return dict(matrix_column=col,geo_accession=s['accession'][0] if s else UNKNOWN,
  geo_title=s['!Sample_title'][0] if s else UNKNOWN,mapping_status=status,evidence=evidence,
  database_relations=' | '.join(s.get('!Sample_relation',[])) if s else UNKNOWN)
def qc(ds,rows,samples):
 header,*data=rows; ids=[r[0] for r in data]; columns=header[1:]
 lens=[i+2 for i,r in enumerate(data) if len(r)!=len(header)]
 invalid=[(i+2,columns[j],v) for i,r in enumerate(data) for j,v in enumerate(r[1:]) if not re.fullmatch(r'\d+',v)]
 missing=[i+2 for i,x in enumerate(ids) if not x or x in ['NA','NaN','null']]
 duplicates={k:v for k,v in collections.Counter(ids).items() if v>1}
 out=dict(dataset=ds,rows=len(data),sample_columns=len(columns),gene_id_missing_rows=missing,
  duplicate_gene_ids=duplicates,duplicate_columns={k:v for k,v in collections.Counter(columns).items() if v>1},
  invalid_count_cells=invalid[:100],invalid_count_cell_count=len(invalid),row_width_mismatch_lines=lens,
  samples_exactly_in_matrix_order=columns==[x['matrix_column'] for x in samples],
  integer_nonnegative_counts=not invalid,
  all_zero_rows_retained=sum(all(x=='0' for x in r[1:]) for r in data),
  unresolved_sample_rows=[x['matrix_column'] for x in samples if x['metadata_status']!='verified'],
  operations='structural validation only; no normalization, filtering, imputation, aggregation, statistical testing or DEG estimation')
 (ROOT/'curator_only'/ds/'qc.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 if lens or invalid or missing or duplicates or out['duplicate_columns'] or not out['samples_exactly_in_matrix_order']:
  raise RuntimeError('QC issue reported; not repaired: '+ds)
 return out

def main():
 reports=[]
 for ds,id in DATASETS.items():
  orig=ROOT/'curator_only'/ds/'original';model=ROOT/'model_input'/id;model.mkdir(parents=True,exist_ok=True)
  geo=soft_records(next(orig.glob('*family.soft.gz')))
  (orig.parent/'geo_samples.json').write_text(json.dumps(geo,ensure_ascii=False,indent=2),encoding='utf-8')
  samples=[];cw=[]
  if ds in ['skin','ishikawa','mammary']:
   p=next(orig.glob('*counts*.gz'));src=read_table(p);offset=1 if ds=='ishikawa' else 2
   rows=[['gene_id']+src[0][offset:]]+[[r[0]]+r[offset:] for r in src[1:]]
   gz_table(model/'counts.tsv.gz',rows)
   DERIVED.append((ds,f'model_input/{id}/counts.tsv.gz',[p.relative_to(ROOT).as_posix()],f'lossless TSV; first ID header -> gene_id; {offset-1} non-count annotation column(s) moved to features; all rows/columns/order/count tokens retained'))
   assert read_table(model/'counts.tsv.gz')==rows
   if offset==2:
    features=[['gene_id',src[0][1]]]+[[r[0],r[1]] for r in src[1:]]
    gz_table(model/'features.tsv.gz',features)
    DERIVED.append((ds,f'model_input/{id}/features.tsv.gz',[p.relative_to(ROOT).as_posix()],'lossless separation of non-count annotation column; unchanged row order'))
   for col in rows[0][1:]:
    if ds=='skin':
     title=re.sub(r'\.(?:fastq|fq)\.gz$','',col)
     hits=[s for s in geo if s['!Sample_title'][0]==title];assert len(hits)==1
     s=hits[0];c=chars(s);x=base(col,s)
     x.update(group='clobetasol' if c['condition']=='gc' else 'untreated',use_primary='true',subject_id=c['individual'],
      biological_replicate=c['individual'],replicate_type='paired_subject',cell_type='full_thickness_skin',
      sequencing_type='single_end',time_hours='24')
     samples.append(x);cw.append(cross(col,s,'Remove terminal .fq.gz/.fastq.gz for exact GEO title join; condition and individual from GEO characteristics, not filename.'))
    elif ds=='mammary':
     hits=[s for s in geo if col in s.get('!Sample_description',[])];assert len(hits)==1
     s=hits[0];c=chars(s);x=base(col,s)
     typ='luminal' if c['immunophenotype']=='luminal cell population' else 'basal'
     stage={'virgin':'virgin','18.5 day pregnancy':'pregnancy_18.5d','2 day lactation':'lactation_2d'}[c['developmental stage']]
     x.update(group=stage,use_primary=str(typ=='luminal' and stage!='virgin').lower(),biological_replicate=s['!Sample_title'][0].split('#')[1],
      replicate_type='independent_biological_sample',cell_type=typ,stage=stage,raw_file_batch_date='2013-08-09',sequencing_type='single_end',
      genotype=c['genotype/variation'],strain=c['strain/background'],sex=c['gender'])
     samples.append(x);cw.append(cross(col,s,'Exact match to GEO Sample_description full matrix column; stage and cell type from characteristics; repeat label from title, not a cross-stage mouse ID.'))
    else:
     hits=[s for s in geo if s['!Sample_title'][0]==col+'_RNA_seq']
     if len(hits)==1:
      s=hits[0];c=chars(s);x=base(col,s);tr=c['treatment']
      group='Dex_E2' if ' and ' in tr else 'Dex' if 'Dexamethasone' in tr else 'E2' if 'Estradiol' in tr else 'DMSO'
      x.update(group=group,use_primary=str(group in ['E2','DMSO']).lower(),use_secondary=str(group in ['Dex','DMSO']).lower(),
       biological_replicate=c['replicate'],replicate_type='replicate_number_reported_biological_vs_technical_unconfirmed',cell_type='Ishikawa',
       sequencing_type='single_end',time_hours='8',metadata_status='sample_match_verified_replicate_type_pending')
      samples.append(x);cw.append(cross(col,s,'Exact case-sensitive matrix column + _RNA_seq = GEO title. Replicate numbers are NOT paired subjects or verified batches.'))
     else:
      assert col=='Ishi_Dex_E2_1'
      x=base(col);x.update(cell_type='Ishikawa',metadata_status='unresolved_column_to_GSM');samples.append(x)
      y=cross(col,None,'No exact title match. Candidate GSM2973408 has title Ishi_Dex_E2_2_RNA_seq; inferred from set complement only, NOT accepted or silently renamed.','pending')
      y['candidate_geo_accession']='GSM2973408';cw.append(y)
  elif ds=='airway':
   for name in ['DESCRIPTION','data/airway.RData','inst/extdata/sample_table.csv','inst/extdata/SraRunInfo_SRP033351.csv','inst/doc/airway.Rmd']:
    member(ds,'airway_1.32.0.tar.gz','airway/'+name,f'curator_only/airway/package_files/{name}')
   rows=read_table(model/'counts.tsv.gz')
   tab=list(csv.DictReader((orig.parent/'object_colData.tsv').open(encoding='utf-8'),delimiter='\t'))
   for d in tab:
    s=next(s for s in geo if s['accession'][0]==d['SampleName']);c=chars(s)
    assert c['cell line']==d['cell']
    assert (c['treatment']=='Dexamethasone')==(d['dex']=='trt')
    assert d['albut']=='untrt'
    x=base(d['matrix_column'],s);x.update(group='dexamethasone' if d['dex']=='trt' else 'untreated',use_primary='true',
     subject_id=d['cell'],biological_replicate=d['cell'],replicate_type='paired_donor',cell_type='airway_smooth_muscle',
     sequencing_type='paired_end',time_hours='18',ercc_mix=c['ercc_mix'],albuterol='untreated')
    samples.append(x);cw.append(cross(d['matrix_column'],s,'RData colData Run/SampleName and stored sample_table.csv; cell and dex independently checked against GEO.'))
   DERIVED.append((ds,f'model_input/{id}/counts.tsv.gz',['curator_only/airway/original/airway_1.32.0.tar.gz'],'base R object export; see export_airway.R and export_session.txt; exact integer roundtrip verified; whole 8-column airway assay'))
  else:
   p=member(ds,'pasilla_1.40.0.tar.gz','pasilla/inst/extdata/pasilla_gene_counts.tsv','curator_only/pasilla/package_files/pasilla_gene_counts.tsv')
   a=member(ds,'pasilla_1.40.0.tar.gz','pasilla/inst/extdata/pasilla_sample_annotation.csv','curator_only/pasilla/package_files/pasilla_sample_annotation.csv')
   for name in ['DESCRIPTION','inst/doc/create_objects.Rmd']:
    member(ds,'pasilla_1.40.0.tar.gz','pasilla/'+name,f'curator_only/pasilla/package_files/{name}')
   for name in ['DESCRIPTION','inst/extdata/pasilla_gene_counts.tsv.gz','inst/extdata/pasilla_sample_annotation.csv']:
    member(ds,'DESeq2_1.52.0.tar.gz','DESeq2/'+name,f'curator_only/pasilla/deseq2_reference/{name}')
   ref=orig.parent/'deseq2_reference'/'inst'/'extdata'
   assert gzip.decompress((ref/'pasilla_gene_counts.tsv.gz').read_bytes())==p.read_bytes()
   assert (ref/'pasilla_sample_annotation.csv').read_bytes()==a.read_bytes()
   rows=read_table(p);gz_table(model/'counts.tsv.gz',rows)
   DERIVED.append((ds,f'model_input/{id}/counts.tsv.gz',['curator_only/pasilla/original/pasilla_1.40.0.tar.gz'],'gzip encoding of complete package gene matrix; all values/IDs/order unchanged; byte-identical to decompressed DESeq2 1.52.0 example'))
   anno=list(csv.DictReader(a.open(encoding='utf-8')))
   candidates={'untreated1':'GSM461182','untreated2':'GSM461176','untreated3':'GSM461177','untreated4':'GSM461178','treated1':'GSM461179','treated2':'GSM461180','treated3':'GSM461181'}
   for col in rows[0][1:]:
    d=next(r for r in anno if r['file']==col+'fb');x=base(col)
    x.update(original_sample_id=d['file'],group='pasilla_knockdown' if d['condition']=='treated' else 'untreated',use_primary='true',
     biological_replicate=d['file'],replicate_type='biological_per_package_original_crosswalk_pending',cell_type='S2_DRSC',
     sequencing_type='single_read' if d['type']=='single-read' else 'paired_end',number_of_lanes=d['number of lanes'],
     metadata_status='package_annotation_verified_GEO_crosswalk_pending')
    samples.append(x);y=cross(col,None,'Package annotation file matched by exact matrix column + fb, per DESeq2 official vignette. GEO candidate is an inference from title/layout/run totals; not an established original crosswalk.','package_verified_original_pending')
    y.update(package_sample_id=d['file'],candidate_geo_accession=candidates[col]);cw.append(y)
  write_tsv(model/'samples.tsv',samples)
  write_tsv(orig.parent/'sample_crosswalk.tsv',cw)
  parents=[p.relative_to(ROOT).as_posix() for p in orig.iterdir() if p.is_file()]
  DERIVED.append((ds,f'model_input/{id}/samples.tsv',parents,'explicit source-based sample annotation; no imputation; unresolved fields labeled; rows reordered to match matrix'))
  report=qc(ds,rows,samples)
  if ds=='skin':
   symbols=[r[1] for r in src[1:]]
   report['duplicate_gene_symbol_excess_rows']=sum(v-1 for v in collections.Counter(symbols).values() if v>1)
   report['gene_symbol_missing_like_rows']=sum(x in ['','NA','NaN','-'] for x in symbols)
   report['paired_subjects']=len(set(s['subject_id'] for s in samples))
   for sub in set(s['subject_id'] for s in samples): assert sorted(s['group'] for s in samples if s['subject_id']==sub)==['clobetasol','untreated']
  if ds=='airway':
   report['paired_subjects']=len(set(s['subject_id'] for s in samples))
   for sub in set(s['subject_id'] for s in samples): assert sorted(s['group'] for s in samples if s['subject_id']==sub)==['dexamethasone','untreated']
  if ds=='pasilla':report['DESeq2_1.52.0_counts_and_annotation_byte_equal']=True
  (orig.parent/'qc.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
  reports.append(report)
  print(ds,report['rows'],report['sample_columns'],'validated',flush=True)
 (ROOT/'curator_only'/'qc_summary.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
 (ROOT/'curator_only'/'transformations.json').write_text(json.dumps(DERIVED,ensure_ascii=False,indent=2),encoding='utf-8')
 (ROOT/'curator_only'/'curation_environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'no_DEG_run':True},indent=2),encoding='utf-8')
if __name__=='__main__':main()
