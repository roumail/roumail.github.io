import os
import re
from datetime import datetime

from invoke import task


def update_series(post_path, series):
    index_file_path = os.path.join(post_path, "index.md")
    with open(index_file_path, "r") as f:
        lines = f.readlines()

    with open(index_file_path, "w") as f:
        for line in lines:
            if "series:" in line:
                f.write(f"series: {series}\n")
            else:
                f.write(line)


def harmonize_name(name):
    """
    Harmonize the given name by removing colons and replacing spaces with hyphens.
    """
    name = re.sub(r":", "", name)  # Remove colons
    name = name.replace(" ", "-")  # Replace spaces with hyphens
    return name.lower()


@task(
    help={
        "title": "The title of the blog post you want to create.",
        "series": "The series to which the blog post belongs (optional).",
        "quarto": "Initialize a quarto_document",
    }
)
def new_post(c, title, series=None, quarto=False):
    """
    Create a new post with a given title under a specified category.
    Optionally, specify a series name.
    """
    # Harmonize the title and series names
    title_harmonized = harmonize_name(title)
    if series:
        series_harmonized = f"series-{harmonize_name(series)}"

    # Create a timestamped directory
    timestamp = datetime.now().strftime("%Y-%m-%d")
    timestamped_dir = f"{timestamp}-{title_harmonized}"

    # Determine the path where the new blog post should be created
    if series:
        post_dir = f"content/post/{series_harmonized}/{timestamped_dir}"
    else:
        post_dir = f"content/post/{timestamped_dir}"

    # Create the directory
    os.makedirs(post_dir, exist_ok=True)

    # Determine the file extension based on the quarto flag
    file_ext = ".qmd" if quarto else ".md"
    path2post = f"{post_dir}/index{file_ext}"

    # Create the new Hugo blog post
    c.run(f"hugo new --kind blog-post {path2post}")
    print(f"New post created at {path2post}")

    # Add Quarto specific format specifications if quarto flag is enabled
    if quarto:
        with open(path2post, "a") as f:
            f.write("\nformat: hugo-md\njupyter: python3\n")

    # Check if a series is specified
    if series:
        path2series_dir = f"content/post/{series_harmonized}"

        # Update the series front matter in index.md
        update_series(post_dir, series_harmonized)

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

# View.
#   1 = List
#   2 = Compact
#   3 = Card
view: 2
"""
                )
            print(f"_index.md for series '{series}' created at {index_file_path}")
