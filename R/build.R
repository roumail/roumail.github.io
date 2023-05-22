# R/build.R

# Install packages
install.packages(c('blogdown', 'remotes'))

# Get Hugo version from vercel.json
hugo_version <- system2('jq', args = c('-r', '.build.env.HUGO_VERSION', 'vercel.json'), stdout = TRUE)

# Install Hugo
blogdown::install_hugo(version = hugo_version)

# Build the site
blogdown::build_site()
