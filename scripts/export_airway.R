# Lossless export of the EXISTING airway object. No normalization or analysis.
# Run after inspect_inputs.py extracts the pinned source archive to _work/packages.
# Uses base R serialization attributes, so no Bioconductor installation is needed.
options(stringsAsFactors=FALSE)
pkg <- "_work/packages/airway"
desc <- read.dcf(file.path(pkg, "DESCRIPTION"))
stopifnot(desc[1,"Package"] == "airway", desc[1,"Version"] == "1.32.0")
env <- new.env()
load(file.path(pkg, "data/airway.RData"), envir=env)
obj <- env$airway
stopifnot(identical(as.character(attr(obj,"class")), "RangedSummarizedExperiment"))
assay_list <- attr(attr(attr(obj,"assays"),"data"),"listData")
stopifnot(identical(names(assay_list), "counts"))
counts <- assay_list[["counts"]]
cd <- attr(obj,"colData")
samples <- as.data.frame(attr(cd,"listData"), check.names=FALSE)
sample_ids <- attr(cd,"rownames")
gene_ids <- attr(attr(attr(obj,"rowRanges"),"partitioning"),"NAMES")
stopifnot(is.matrix(counts), is.integer(counts), nrow(counts)==length(gene_ids),
          ncol(counts)==length(sample_ids), nrow(samples)==length(sample_ids),
          identical(as.character(samples$Run), sample_ids))
dir.create("model_input/dataset_04",recursive=TRUE,showWarnings=FALSE)
dir.create("curator_only/airway",recursive=TRUE,showWarnings=FALSE)
out <- data.frame(gene_id=gene_ids, counts, check.names=FALSE)
names(out) <- c("gene_id", sample_ids)
con <- gzfile("model_input/dataset_04/counts.tsv.gz","wt")
write.table(out,con,sep="\t",quote=FALSE,row.names=FALSE,na="NA")
close(con)
write.table(data.frame(matrix_column=sample_ids,samples,check.names=FALSE),
            "curator_only/airway/object_colData.tsv",sep="\t",quote=FALSE,row.names=FALSE,na="NA")
back <- read.delim(gzfile("model_input/dataset_04/counts.tsv.gz"),check.names=FALSE)
stopifnot(identical(back[[1]],gene_ids),identical(names(back)[-1],sample_ids),
          identical(unname(as.matrix(back[,-1])),unname(counts)))
capture.output(list(package=desc[1,c("Package","Version","License","git_last_commit","git_last_commit_date")],
                    object_class=class(obj),assay_name=names(assay_list),dimensions=dim(counts),
                    export="base R load; assays/data/listData/counts; rowRanges/partitioning/NAMES; colData/rownames and listData; write.table; exact integer roundtrip verified",
                    session=sessionInfo()),file="curator_only/airway/export_session.txt")
cat("Exported and verified",nrow(counts),"genes x",ncol(counts),"samples\n")
