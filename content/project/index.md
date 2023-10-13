---
# Leave the homepage title empty to use the site title
title:
date: 2023-10-10

type: landing

sections:
  - block: markdown
    content:
      title: Gallery
      subtitle: ''
      text: |-
        {{< gallery album="demo" >}}
    design:
      columns: '1'
  - block: collection
    id: featured
    content:
      title: Featured Publications
      subtitle: ''
      filters: 
        folders: 
            - publication # event, talk
      featured_only: true
    design:
      view: card  # showcase, compact
      columns: '2'
      # For Showcase view, flip alternate rows?
    #   flip_alt_rows: false
---

#   - block: collection
#     id: talks
#     content:
#       title: Recent & Upcoming Talks
#       filters:
#         folders:
#           - event
#     design:
#       columns: '2'
#       view: compact
# # - block: portfolio
# #     id: projects
# #     content:
# #     title: Projects
# #     filters:
# #         folders:
# #         - project
# #     # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
# #     default_button_index: 0
# #     # Filter toolbar (optional).
# #     # Add or remove as many filters (`filter_button` instances) as you like.
# #     # To show all items, set `tag` to "*".
# #     # To filter by a specific tag, set `tag` to an existing tag name.
# #     # To remove the toolbar, delete the entire `filter_button` block.
# #     buttons:
# #         - name: All
# #         tag: '*'
# #         - name: Deep Learning
# #         tag: Deep Learning
# #         - name: Other
# #         tag: Demo
# #     design:
# #     # Choose how many columns the section has. Valid values: '1' or '2'.
# #     columns: '1'
# #     view: showcase
# #     # For Showcase view, flip alternate rows?
# #     flip_alt_rows: false