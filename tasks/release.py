from invoke import task

from website.task_helpers import get_version_from_pyproject
from .posts import check_project_root_task


@task(pre=[check_project_root_task])
def tag_version(c):
    """
    Create a new Git tag with the version from pyproject.toml and push it to 
    the remote repository.

    Presupposes that you've already done poetry version bump using 
    poetry version patch/minor, etc
    """
    version = get_version_from_pyproject()
    print(f"Current version is {version}")

    # Create a new Git tag
    c.run(f"git tag v{version}")

    # Push the tag to the remote repository
    c.run(f"git push origin v{version}")

    print(f"Git tag v{version} has been created and pushed.")
