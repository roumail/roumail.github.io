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

@task(help={
    'title': 'The title of the blog post you want to create.',
    'series': 'The series to which the blog post belongs (optional).'
})
def new_post(c, title, series=None):
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

    # Determine the path where the new blog post should be created
    if series:
        path = f"content/blog/{series}/{timestamped_dir}"
    else:
        path = f"content/blog/{timestamped_dir}"
    
    # Create the directory
    os.makedirs(path, exist_ok=True)

    # Create the new Hugo blog post
    c.run(f"hugo new --kind blog-post {path}/index.md")
    print(f"New post created at {path}/index.md")