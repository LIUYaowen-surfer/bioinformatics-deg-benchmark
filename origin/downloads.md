# Local downloads - curator only

The [manifest](sra_manifest.json) contains the 160 unique runs selected for 20 papers / 23 tasks, totaling 338,863,412,489 bytes (338.86 GB). URLs, expected sizes and MD5 checksums come from the NCBI SRA Data Locator. The archive format is full-quality SRA, not SRA Lite. Shared controls are downloaded once.

From the repository root, use Python's standard library:

```powershell
python origin/download_sra.py --manifest origin/sra_manifest.json --output-dir "D:\ma_lab\deg_answer" --workers 12
```

Archives are stored as `study_XX/sra/SRR.../SRR....sra`. The [downloader](download_sra.py) resumes `.sra.part` files and verifies exact size and MD5 before marking an archive complete. Do not run two copies against the same destination. Keep at least 8 GiB free beyond the remaining downloads. An existing conflicting archive is reported without overwriting it.

Check `D:\ma_lab\deg_answer\sra_download_status.json` for the current result of each run. `downloaded_verified` and `verified_existing` are completed states; a `.part` file is incomplete. A task is ready at the raw-archive level only when every selected run in its two links has a verified archive. The repository does not claim that all downloads have finished merely because this manifest exists.

Author result files, reference answers and the extractor are stored locally at `C:\Users\1\Desktop\ma_lab\deg_answer`. The original seven author files stay at that folder's root; added files are under `study_XX/author_results/`. Reference outputs are under `reference_json/`, with study subfolders for the additions. Original downloads are not modified or replaced; earlier candidate tables are retained separately from the configured inputs.

Only source links, task prompts, scripts, manifest and derived top100 gene lists are uploaded. Raw SRA archives and complete author tables are not included in Git. No FASTQ conversion, anonymization, alignment, counting or DEG analysis is performed by these scripts. The offline preparation steps in [README](README.md) remain for the evaluator to perform separately.
