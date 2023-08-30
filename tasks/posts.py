import os
import re
from datetime import datetime

from invoke import task


def harmonize_name(name):
    """
    Harmonize the given name by removing colons and replacing spaces with hyphens.
    """
    name = re.sub(r":", "", name)  # Remove colons
    name = name.replace(" ", "-")  # Replace spaces with hyphens
    return name


def update_series(category_path, series):
    with open(f"{category_path}/index.md", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("series:"):
            f.write(f"series: {series}\n")
        else:
            f.write(line)


@task
def new_post(c, title, category, series=None):
    """
    Create a new post with a given title under a specified category.
    Optionally, specify a series name.
    """
    # Replace spaces in the title with hyphens
    title = harmonize_name(title)
    if series:
        series = harmonize_name(series)

    # Create a timestamped directory
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # Include the series name in the directory if provided
    if series:
        timestamped_dir = f"{timestamp}-{series}-{title}"
    else:
        timestamped_dir = f"{timestamp}-{title}"

    # Create the directory for the category if it doesn't exist
    category_path = f"content/blog/{category}/{timestamped_dir}"
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Determine the archetype to use based on the category
    archetype = f"{category}-blog"
    if series:
        archetype = "series"

    # Use Hugo to create the new post
    os.system(f"hugo new --kind {archetype} blog/{category}/{timestamped_dir}/index.md")

    # If it's part of a series, add the series metadata
    if series:
        update_series(category_path, series)

    print(f"New post created at {category_path}/index.md")
