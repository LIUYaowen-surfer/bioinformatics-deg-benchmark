"""Build provenance, unresolved-issue tables and checksums. No expression analysis."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib
from prepare import DATASETS,write_tsv,sha
ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
manifest=list(csv.DictReader((ROOT/'curator_only/download_manifest.tsv').open(encoding='utf-8'),delimiter='\t'))
for r in manifest:
 if '/filereport?' in r['source_url']:r['original_filename']='API response; no server filename (saved as '+Path(r['local_path']).name+')'
write_tsv(ROOT/'curator_only/download_manifest.tsv',manifest)
trans=json.loads((ROOT/'curator_only/transformations.json').read_text(encoding='utf-8'))
by_path={r['local_path']:r for r in manifest}
lookup={row[1]:row for row in trans}
fields=['local_path','file_role','source_url','original_filename','retrieved_at_utc','curated_at_utc','version','sha256','size_bytes','parent_files','parent_sha256','operation']
for ds,id in DATASETS.items():
 rows=[]
 for r in manifest:
  if r['dataset']!=ds:continue
  rows.append(dict(local_path=r['local_path'],file_role=r['role'],source_url=r['source_url'],original_filename=r['original_filename'],
   retrieved_at_utc=r['retrieved_at_utc'],curated_at_utc='',version=r['version'] or 'GEO/ENA snapshot; accession and retrieved timestamp identify source',
   sha256=r['sha256'],size_bytes=r['size_bytes'],parent_files='',parent_sha256='',operation='download; bytes unchanged'))
 paths=list((ROOT/'curator_only'/ds).rglob('*'))+list((ROOT/'model_input'/id).rglob('*'))
 for p in sorted(paths):
  if not p.is_file() or p.name=='provenance.tsv':continue
  rel=p.relative_to(ROOT).as_posix()
  if rel in by_path:continue
  t=lookup.get(rel)
  parents=t[2] if t else [r['local_path'] for r in manifest if r['dataset']==ds]
  parents=[x for x in parents if (ROOT/x).is_file()]
  srcs=[by_path[x] for x in parents if x in by_path]
  rows.append(dict(local_path=rel,file_role='derived/exported/curated',source_url=' | '.join(dict.fromkeys(x['source_url'] for x in srcs)),
   original_filename=' | '.join(dict.fromkeys(x['original_filename'] for x in srcs)),
   retrieved_at_utc=' | '.join(dict.fromkeys(x['retrieved_at_utc'] for x in srcs)),curated_at_utc=now,
   version=' | '.join(dict.fromkeys(x['version'] for x in srcs if x['version'])) or 'curation v1',
   sha256=sha(p),size_bytes=p.stat().st_size,parent_files=' | '.join(parents),parent_sha256=' | '.join(sha(ROOT/x) for x in parents),
   operation=t[3] if t else 'curator-authored record or structural QC; see README and scripts; paper links are documented separately'))
 write_tsv(ROOT/'curator_only'/ds/'provenance.tsv',rows,fields)

issues=[
 ['skin','batch/demographics','pending','Sample-level batch, age, sex mapping missing from GEO; paper models these factors; Table S1 download failed.','Paired task draft possible; scoring specification must decide handling of unknown batch.'],
 ['skin','annotation_version','conflict','Paper Ensembl 91 vs GEO Ensembl 92.','Keep original Ensembl IDs; do not claim exact paper preprocessing reproduction.'],
 ['skin','gene_symbols','reported_not_fixed','1656 excess rows share Gene name values. Primary Ensembl IDs unique.','Keep all rows; no symbol aggregation.'],
 ['ishikawa','column_to_sample','pending','Ishi_Dex_E2_1 has no exact GEO title match; candidate GSM2973408 is unconfirmed.','Does not affect E2/Dex vs DMSO columns; exclude joint-treatment comparisons until resolved.'],
 ['ishikawa','replicate_type','pending','Replicate numbers 1/2 reported; biological vs technical independence not explicitly established in reviewed methods.','Resolve before formal scoring; do not assume paired blocks.'],
 ['ishikawa','duration','conflict_documented','GEO generic treatment protocol 1 h vs characteristics and paper RNA-seq 8 h.','Use 8 h with explicit evidence; preserve conflicting source.'],
 ['mammary','cross_cell_pairing','pending','Same-mouse correspondence across basal/luminal is not encoded by a unique animal ID.','No effect on proposed luminal-only independent stage contrast; do not infer pairing from repeat number.'],
 ['mammary','processing_version','conflict_documented','Paper Rsubread version rendering and GEO Subread 1.4.4 differ.','Existing count file used unchanged; no reconstruction.'],
 ['airway','third_party_processing','documented','Object is a third-party gene recount, distinct from author FPKM processing; 8 columns vs GEO 16.','Full existing assay retained; not a complete reproduction of all GEO experiments.'],
 ['airway','web_vignette_output','conflict_documented','Current rendered example shows malformed 16-row cell/dex annotations; stored object and CSV agree with GEO.','Use verified stored object/CSV; do not overwrite from displayed example.'],
 ['pasilla','replicate_counts','conflict','Paper says 4 treated/3 untreated; package says 3 treated/4 untreated.','Public debug baseline only until original lineage resolved.'],
 ['pasilla','original_GSM_crosswalk','pending','Package cites six GSM records for seven matrix columns. ENA suggests untreated1 may be GSM461182; mappings remain candidates.','Do not claim complete original-sample lineage or relabel groups.'],
 ['pasilla','counting_history','pending','Current package documents exon pipeline; exact historical gene-TSV counting implementation not independently established.','Use supplied integer gene matrix and official example equivalence, without asserting undocumented tool parameters.'],
 ['pasilla','lanes_vs_runs','conflict','treated1 package reports 5 lanes while candidate ENA experiment contains 6 runs; paired read totals also differ.','Runs/lanes are technical units, not independent biological replicates; no merging/recounting performed.'],
 ['all','scoring_settings','not_fixed','Methods, versions, thresholds and numeric tolerances are not fixed; no DEG output generated.','All task files remain drafts.'],
]
write_tsv(ROOT/'curator_only/known_issues.tsv',[dict(zip(['dataset','topic','status','finding','task_impact'],r)) for r in issues])
write_tsv(ROOT/'curator_only/unavailable_sources.tsv',[dict(dataset='skin',requested_item='Supplemental Table S1 sample-level metadata',url='https://pmc.ncbi.nlm.nih.gov/articles/PMC6814545/bin/NIHMS1532721-supplement-9.xlsx',status='HTTP 403; no valid XLSX acquired',missing='batch/age/sex original sample mapping',local_data_present='raw counts and GEO paired samples present',action='URL retained; no imputation or placeholder data uploaded')])

index=[]
comparisons={'skin':'clobetasol_vs_untreated','ishikawa':'E2_vs_DMSO;Dex_vs_DMSO','mammary':'luminal_lactation2d_vs_pregnancy18.5d','airway':'dexamethasone_vs_untreated','pasilla':'pasilla_knockdown_vs_untreated'}
status={'skin':'draft_ready_batch_pending','ishikawa':'draft_ready_replicate_independence_pending','mammary':'ready_for_task_development','airway':'ready_public_baseline','pasilla':'public_debug_baseline_original_lineage_pending'}
for ds,id in DATASETS.items():
 q=json.loads((ROOT/'curator_only'/ds/'qc.json').read_text(encoding='utf-8'))
 samples=list(csv.DictReader((ROOT/'model_input'/id/'samples.tsv').open(encoding='utf-8'),delimiter='\t'))
 index.append(dict(dataset=id,paper_key=ds,count_rows=q['rows'],full_sample_count=q['sample_columns'],
  primary_sample_count=sum(x['use_primary']=='true' for x in samples),secondary_sample_count=sum(x['use_secondary']=='true' for x in samples),
  comparison=comparisons[ds],data_status='acquired_and_structurally_verified',readiness=status[ds],
  model_path=f'model_input/{id}',curator_path=f'curator_only/{ds}',issues_path='curator_only/known_issues.tsv'))
write_tsv(ROOT/'dataset_index.tsv',index)

def included(p):
 parts=p.relative_to(ROOT).parts
 return p.is_file() and not any(x in ['.git','_work','__pycache__','_delivery_verification'] for x in parts) and p.name!='SHA256SUMS.tsv'
files=sorted(p for p in ROOT.rglob('*') if included(p))
write_tsv(ROOT/'SHA256SUMS.tsv',[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p),size_bytes=p.stat().st_size) for p in files])
print('Provenance finalized:',len(files),'files;',sum(p.stat().st_size for p in files),'bytes; largest',max(p.stat().st_size for p in files),'bytes')
