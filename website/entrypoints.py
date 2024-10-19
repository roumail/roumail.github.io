import typer

from website.posts import concatenate_drafts, create_new_post
from website.task_helpers import check_project_root

app = typer.Typer(
    add_completion=False, help="Utility helpers for working on my website."
)


@app.command(help="Create a new (series) post with a given title.")
def new_post(
    title: str = typer.Option(help="The title of the blog."),
    series: str
    | None = typer.Option(
        help="The series the blog post entry belongs to.", default=None
    ),
    quarto: bool = typer.Option(
        help="Initialize a quarto_document instead of regular markdown", default=False
    ),
):
    check_project_root()
    create_new_post(title, series, quarto)


@app.command(help="Concatenate all draft posts into a single markdown file.")
def list_draft_posts(
    file_out: str = typer.Option(
        help="The output file name for concatenated drafts.",
        default="current_draft_posts.md",
    ),
):
    check_project_root()
    concatenate_drafts(
        file_out=file_out,
        search_directory="content/post",
        search_string="draft: true",
    )


if __name__ == "__main__":
    app()
