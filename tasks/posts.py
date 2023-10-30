from invoke import task

from website.task_helpers import create_new_post, concatenate_drafts, check_project_root


@task
def check_project_root_task(c):
    """
    Check if the command is being executed from the project root.
    """
    check_project_root()


@task(
    pre=[check_project_root_task],
    help={
        "title": "The title of the blog post you want to create.",
        "series": "The series to which the blog post belongs (optional).",
        "quarto": "Initialize a quarto_document",
    },
)
def new_post(c, title, series=None, quarto=False):
    """
    Create a new post with a given title under a specified category.
    Optionally, specify a series name.
    """
    create_new_post(title, series, quarto)


@task(
    pre=[check_project_root_task],
    help={
        "file_out": "The output file name for concatenated drafts. Defaults to 'concatenated_drafts.md'.",
        "search_directory": "The directory to search for draft posts. Defaults to 'content/post'.",
        "search_string": "The string to search for in the markdown files to identify drafts. Defaults to 'draft: true'.",
    },
)
def list_draft_posts(
    c,
    file_out="current_draft_posts.md",
    search_directory="content/post",
    search_string="draft: true",
):
    """
    Concatenate all draft posts into a single markdown file.
    """
    concatenate_drafts(
        file_out=file_out,
        search_directory=search_directory,
        search_string=search_string,
    )
