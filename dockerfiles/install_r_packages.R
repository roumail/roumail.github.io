#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly = TRUE)
action <- ifelse(length(args) > 0, args[1], "install")

cat("performing ", action)

install.packages("renv")
renv::init(bare=TRUE)
options(repos = c(CRAN = "https://cran.r-project.org"))

if (action == "install") {
    renv::install(c("blogdown"))
    # renv::install("url::https://cran.r-project.org/src/contrib/Archive/sybilSBML/sybilSBML_3.1.2.tar.gz")
    options(renv.config.cache.symlinks = FALSE)
    renv::isolate() # to move from cache to library   
} else if (action == "restore") {
  # Restore packages from the renv.lock file
  renv::restore()
} else {
  stop("Invalid action specified. Please use 'install' or 'restore'.")
}
