import typer

from website.posts import concatenate_drafts, create_new_post
from website.task_helpers import check_project_root

app = typer.Typer()


@app.command()
def new_post(title: str, series=None, quarto=False):
    """
    Create a new post with a given title under a specified category.
    Optionally, specify a series name.
    Params:
        "title": "The title of the blog post you want to create."
        "series": "The series to which the blog post belongs (optional)."
        "quarto": "Initialize a quarto_document, defaults to False"
    """
    check_project_root()
    create_new_post(title, series, quarto)


@app.command()
def list_draft_posts(
    file_out="current_draft_posts.md",
    search_directory="content/post",
    search_string="draft: true",
):
    """
    Concatenate all draft posts into a single markdown file.
    Params
        "file_out": "The output file name for concatenated drafts. Defaults to 'concatenated_drafts.md'."
        "search_directory": "The directory to search for draft posts. Defaults to 'content/post'."
        "search_string": "The string to search for in the markdown files to identify drafts. Defaults to 'draft: true'."
    """
    check_project_root()
    concatenate_drafts(
        file_out=file_out,
        search_directory=search_directory,
        search_string=search_string,
    )
