from invoke import task

from website.release import get_version_from_pyproject, get_or_create_sha1
from .posts import check_project_root_task


@task(pre=[check_project_root_task])
def tag_version(c):
    """
    Create a new Git tag with the version from pyproject.toml and push it to
    the remote repository.

    Presupposes that you've already done poetry version bump using
    poetry version patch/minor, etc
    """
    # Check if body.md has changed
    current_sha = get_or_create_sha1("body.md", ".last_body_md_sha")
    if current_sha is False:
        print("Warning: body.md has not changed since the last release. Aborting.")
        return

    version = get_version_from_pyproject()
    print(f"Current version is {version}")

    # Create a new Git tag
    c.run(f"git tag v{version}")

    # Push the tag to the remote repository
    c.run(f"git push origin v{version}")

    print(f"Git tag v{version} has been created and pushed.")
