import os
import re


def check_project_root():
    """
    Check if the command is being executed from the project root.
    """
    if not os.path.exists("pyproject.toml"):
        print("Error: This command must be run from the project root.")
        exit(1)
    else:
        print("Running from project root.")


def harmonize_name(name):
    """
    Harmonize the given name by removing colons and replacing spaces with hyphens.
    """
    name = re.sub(r"[:?/,\\]", "", name)  # Remove colons
    name = name.replace(" ", "-")  # Replace spaces with hyphens
    return name.lower()
