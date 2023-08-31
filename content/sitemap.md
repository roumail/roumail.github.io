---
title: "Sitemap"
type: landing

sections:
  - block: tag_cloud
    content:
      title: Blog Tags
    #   subtitle: My subtitle
    #   text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 20
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
  - block: tag_cloud
    content:
      title: Blog categories
    #   subtitle: My subtitle
    #   text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: categories
      # Choose how many tags you would like to display (0 = all tags)
      count: 0
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
---

Browse blog posts by tags.
