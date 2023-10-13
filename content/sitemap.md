---
title: "Sitemap"
type: landing

sections:
# - block: tag_cloud
  #   content:
  #     title: Popular Topics
  #   design:
  #     columns: '2'
  - block: tag_cloud
    content:
      title: Blog Tags
    #   subtitle: My subtitle
      text: Choose a tag to see all the posts associated with it.
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 20
    design:
      columns: '2'
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
  - block: tag_cloud
    content:
      title: Blog categories
      subtitle: Drumming, technology, musings.
      text: Welcome to the categories section of my blog. Here, you can explore posts organized by various topics. Choose a category to see all the posts associated with it.
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: categories
      # Choose how many tags you would like to display (0 = all tags)
      count: 0
    design:
      columns: '2'
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
---
