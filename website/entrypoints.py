from __future__ import annotations

from typing import Optional

import typer
from typing_extensions import Annotated

from website.posts import concatenate_drafts, create_new_post
from website.task_helpers import check_project_root

app = typer.Typer(add_completion=False)


@app.callback()
def callback():
    """
    Utility helpers for working on my website.
    """


@app.command()
def new_post(
    title: Annotated[str, typer.Argument(help="The title of the blog.")],
    series: Annotated[
        Optional[str],
        typer.Argument(help="The series the blog post entry belongs to."),
    ] = None,
    quarto: Annotated[
        bool,
        typer.Option(
            help="Initialize a quarto_document instead of regular markdown",
        ),
    ] = False,
):
    """
    Create a new (series) post with a given title.
    """
    check_project_root()
    create_new_post(title, series, quarto)


@app.command()
def list_draft_posts(
    file_out: Annotated[
        str,
        typer.Argument(
            help="The output file name for concatenated drafts.",
        ),
    ] = "current_draft_posts.md",
):
    """
    Concatenate all draft posts into a single markdown file.
    """
    check_project_root()
    concatenate_drafts(
        file_out=file_out,
        search_directory="content/post",
        search_string="draft: true",
    )
