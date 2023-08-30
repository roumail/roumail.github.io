import os

from invoke import task


@task
def new_post(c, title, category, series=None):
    """
    Create a new post with a given title under a specified category.
    Optionally, specify a series name.
    """
    # Replace spaces in the title with hyphens
    filename = title.replace(" ", "-").lower()

    # Create the directory for the category if it doesn't exist
    category_path = f"content/blog/{category}"
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Determine the archetype to use based on the category
    archetype = f"{category}-blog"
    if series:
        archetype = "series"

    # Use Hugo to create the new post
    os.system(f"hugo new --kind {archetype} blog/{category}/{filename}.md")

    # If it's part of a series, add the series metadata
    if series:
        with open(f"{category_path}/{filename}.md", "a") as f:
            f.write(f"series: {series}\n")

    print(f"New post created at {category_path}/{filename}.md")
