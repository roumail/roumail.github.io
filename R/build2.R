#/usr/bin/env Rscript

# # Check if packages are installed. Install them if they are not already installed.
# packages <- c('blogdown', 'remotes')
# if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
#   install.packages(setdiff(packages, rownames(installed.packages())))
# }

# # Get Hugo version from vercel.json
# hugo_version <- system2('jq', args = c('-r', '.build.env.HUGO_VERSION', 'vercel.json'), stdout = TRUE)

# # Check if Hugo is installed
# if (!blogdown::find_hugo()) {
#   # Install Hugo
#   blogdown::install_hugo(version = hugo_version)
# }

# # Build the site
# blogdown::build_site(local = FALSE)
