#!/bin/bash

# Function to harmonize names by removing special characters and replacing spaces with hyphens
harmonize_name() {
  echo "$1" | sed 's/[:?/,\\]//g' | tr ' ' '-' | tr '[:upper:]' '[:lower:]'
}

# Function to create a new blog post
create_new_post() {
  local title="$1"
  local series="$2"

  # Harmonize the title and series names
  local title_harmonized
  title_harmonized=$(harmonize_name "$title")
  local series_path_name
  if [[ -n "$series" ]]; then
    series_path_name="series-$(harmonize_name "$series")"
  fi

  # Create a timestamped directory
  local timestamp
  timestamp=$(date +%Y-%m-%d)
  local timestamped_dir="${timestamp}-${title_harmonized}"

  # Determine the path where the new blog post should be created
  local post_dir
  if [[ -n "$series" ]]; then
    post_dir="content/post/${series_path_name}/${timestamped_dir}"
  else
    post_dir="content/post/${timestamped_dir}"
  fi

  # Create the directory
  mkdir -p "$post_dir"

  # Path to the new post file
  local post_path="${post_dir}/index.md"

  # Create the new Hugo blog post
  hugo new --kind blog-post "$post_path"
  echo "New post created at $post_path"

  # Check if a series is specified
  if [[ -n "$series" ]]; then
    local series_dir="content/post/${series_path_name}"

    # Update the series front matter in the new post
    update_series_frontmatter "$post_path" "$series"
    echo "Updated series front matter for '$series' in $post_path"

    # Path to the _index.md file for the series
    local index_file_path="${series_dir}/_index.md"

    # Check if _index.md already exists
    if [[ ! -f "$index_file_path" ]]; then
      # Create _index.md with the specified content
      cat > "$index_file_path" <<EOF
---
title: $series
cms_exclude: true
series: ["$series"]
draft: true
type: series
view: 2
---
EOF
      echo "_index.md for series '$series' created at $index_file_path"
    fi
  fi
}

# Function to update series front matter in a post
update_series_frontmatter() {
  local post_path="$1"
  local series="$2"

  # Check if the series key exists in the front matter
  if grep -q "^series:" "$post_path"; then
    sed -i '' "s/^series:.*/series: [\"$series\"]/" "$post_path"
  else
    sed -i '' "/^---$/a\
series: [\"$series\"]\
" "$post_path"
  fi
}

# Main script logic
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <title> [series]"
  exit 1
fi

title="$1"
series="$2"
create_new_post "$title" "$series"
