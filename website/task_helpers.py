import os
import re
from datetime import datetime
from pathlib import Path


def check_project_root():
    """
    Check if the command is being executed from the project root.
    """
    if not os.path.exists("pyproject.toml"):
        print("Error: This command must be run from the project root.")
        exit(1)
    else:
        print("Running from project root.")


def update_series(post_path: str, series: str):
    with open(post_path, "r") as f:
        lines = f.readlines()

    with open(post_path, "w") as f:
        for line in lines:
            if "series:" in line:
                f.write(f'series: ["{series}"]\n')
            else:
                f.write(line)


def harmonize_name(name):
    """
    Harmonize the given name by removing colons and replacing spaces with hyphens.
    """
    name = re.sub(r"[:?/\]", "", name)  # Remove colons
    name = name.replace(" ", "-")  # Replace spaces with hyphens
    return name.lower()


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
    with open(file_out, "w") as f:
        f.write("")

    # Loop through each markdown file in the specified search directory
    for filename in os.listdir(search_directory):
        if filename.endswith(".md"):
            filepath = os.path.join(search_directory, filename)
            with open(filepath, "r") as f:
                content = f.read()

            # Check if the file contains the specified search string
            if search_string in content:
                print(f"Appending {filename} to {file_out}")
                with open(file_out, "a") as f:
                    f.write(content)
                    f.write("\n---\n")

    print(f"Drafts have been concatenated into {file_out}")


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
        with open(path2post, "a") as f:
            f.write("\nformat: hugo-md\njupyter: python3\n")

    # Check if a series is specified
    if series:
        path2series_dir = f"content/post/{series_path_name}"

        # Update the series front matter in index.md
        update_series(path2post, series)
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
---
"""
                )
            print(f"_index.md for series '{series}' created at {index_file_path}")
