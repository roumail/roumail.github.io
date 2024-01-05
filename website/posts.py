import os
import re
from datetime import datetime
from pathlib import Path

from website.task_helpers import harmonize_name


def update_series_frontmatter(post_path: str, series: str):
    with open(post_path, "r") as f:
        lines = f.readlines()

    with open(post_path, "w") as f:
        for line in lines:
            if "series:" in line:
                f.write(f'series: ["{series}"]\n')
            else:
                f.write(line)


def add_quarto_frontmatter(post_path: str):
    """
    Adds Quarto specific front matter to the post file.

    Parameters:
        post_path (str): The path to the post file.
    """
    # Read the current content of the file
    with open(post_path, "r") as f:
        content = f.readlines()

    # Find the end of the YAML front matter block
    end_of_frontmatter_index = None
    for i, line in enumerate(content):
        # Assuming the first line is always ---
        if line.strip() == "---" and i > 0:
            end_of_frontmatter_index = i
            break

    # If the end of the front matter block is found, insert the Quarto front matter
    if end_of_frontmatter_index is not None:
        quarto_frontmatter = ["format: hugo-md\n", "jupyter: python3\n"]
        content.insert(end_of_frontmatter_index, "\n".join(quarto_frontmatter))

        # Write the modified content back to the file
        with open(post_path, "w") as f:
            content = "".join(content)
            f.write(content)
        print(f"Quarto front matter added to {post_path}")
    else:
        print("Error: Could not find the end of the YAML front matter block.")


def create_new_post(title, series=None, quarto=False):
    # Harmonize the title and series names
    title_harmonized = harmonize_name(title)
    if series:
        series_path_name = f"series-{harmonize_name(series)}"

    # Create a timestamped directory
    timestamp = datetime.now().strftime("%Y-%m-%d")
    timestamped_dir = f"{timestamp}-{title_harmonized}"

    # Determine the path where the new blog post should be created
    if series:
        post_dir = f"content/post/{series_path_name}/{timestamped_dir}"
    else:
        post_dir = f"content/post/{timestamped_dir}"

    # Create the directory
    os.makedirs(post_dir, exist_ok=True)

    # Determine the file extension based on the quarto flag
    path2post = Path(f"{post_dir}/index.md")

    # Create the new Hugo blog post
    os.system(f"hugo new --kind blog-post {path2post}")
    print(f"New post created at {path2post}")

    # Add Quarto specific format specifications if quarto flag is enabled
    if quarto:
        path2post_qmd = path2post.with_suffix(".qmd")
        path2post.rename(path2post_qmd)
        path2post = path2post_qmd
        add_quarto_frontmatter(path2post)

    # Check if a series is specified
    if series:
        path2series_dir = f"content/post/{series_path_name}"

        # Update the series front matter in index.md
        update_series_frontmatter(path2post, series)
        print(f"Updated series front matter for '{series}' at {path2post}")

        # Path to the _index.md file
        index_file_path = os.path.join(path2series_dir, "_index.md")

        # Check if _index.md already exists
        if not os.path.exists(index_file_path):
            # Create _index.md with the specified content
            with open(index_file_path, "w") as f:
                f.write(
                    f"""---
title: {series}
cms_exclude: true
draft: true
series: [\"{series}\"]
type: series
view: 2
---
"""
                )
            print(f"_index.md for series '{series}' created at {index_file_path}")


def concatenate_drafts(
    file_out="concatenated_drafts.md",
    search_directory="content/post",
    search_string="draft: true",
):
    """
    Concatenate all draft posts into a single markdown file.

    Parameters:
        file_out (str): The output file name. Defaults to "concatenated_drafts.md".
        search_directory (str): The directory to search for draft posts. Defaults to "content/post".
        search_string (str): The string to search for in the markdown files to identify drafts. Defaults to "draft: true".
    """

    # Initialize an empty file to store the concatenated drafts
    drafts = []
    with open(file_out, "w") as f:
        f.write("")

    # Loop through each markdown file in the specified search directory
    for filepath in Path(search_directory).rglob("*.md"):
        with open(filepath, "r") as f:
            content = f.read()
        # Check if the file contains the specified search string

        if search_string in content or "complete me" in content.lower():
            blog_name = re.sub(f"{search_directory}/", "", str(filepath.parent))
            print(f"Appending {blog_name} to {file_out}")
            drafts.append(blog_name)

    drafts.sort()

    # Write the sorted drafts back to the file
    with open(file_out, "w") as f:
        f.write("\n".join(drafts))
    print(f"Drafts have been concatenated into {file_out}")
