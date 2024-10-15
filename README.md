# Website

The `website` python package, provides cli commands to help write blog entries
for my website on https://www.rohailtaimour.com

This repository also contains the content of the website and static assets
needed to render it on github pages using hugo.

## Dependencies

- [Hugo](https://github.com/gohugoio/hugo/releases/download/v0.111.3/hugo_extended_0.111.3_linux-amd64.tar.gz)
- For jupyter notebooks like blog post entries I use
  [Quarto](https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.450/quarto-1.3.450-macos.tar.gz)
- Python 3.10
- uv for installing dependencies
- Poetry for declaring dependencies

I came upon uv rather recently and find it fantastic so I haven't had the chance
to consolidate and avoid the need for both `poetry` and `uv` as external
dependency management.

## Directory structure

## Overview of WIP blog posts

## Quarto

One of my favourite ways to explore ideas is via jupyter notebooks and
[`quarto`](https://quarto.org/docs/websites/) provides that interface by
allowing you to add a code execution environment that helps keep text and code
in sync.

The `_quarto.yaml` file in the project root (shown below) allows the use of
rendering `*.qmd` files into regular markdown files.

```yaml
project:
  type: hugo
  render:
    - "*.qmd"
    - "!themes/"

format:
  hugo-md:
    code-fold: true
    code-summary: "Show the code"
    code-overflow: wrap
    code-tools: true
    code-block-bg: true
    code-block-border-left: "#31BAE9"
    code-copy: hover
    code-line-numbers: true
    # highlight-style:
    #   light: arrow
    #   dark: arrow-dark

execute:
  warning: false
  freeze: true
  enabled: false
```

Rendering `qmd` files to regular markdown files is done by `quarto render`. That
would render the contents of the website in the current directory. The extra
front matter you need to declare may have the following contents:

```yaml
# regular front matter ...
toc: true
format: hugo-md
jupyter:
  kernel: "scraper-series"
execute:
  enabled: true
  freeze: false
```

## Quick start

1. Install the website package using `uv pip install -e .`
2. `website --help` should list the relevant output

```bash
│ list-draft-posts   Concatenate all draft posts into a single markdown file.
│ new-post           Create a new post with a given title under a specified category.
```

## Bumping package version and updating changelog

I'm maintaining a `CHANGELOG.md` for keeping track of changes made to the python
package. The script `bump_version.py` in the project root provides the utilities
needed for releasing a new tagged version to remote. The github action
`.github/workflows/release-package.yaml` is using this script and is triggered
via a manual dispatch.
