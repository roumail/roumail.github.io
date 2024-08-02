import subprocess
import sys
from datetime import datetime

import toml


# Read the current version from bumpversion configuration
def get_current_version():
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)
        return pyproject["tool"]["poetry"]["version"]


# Update the changelog.md file
def update_changelog(version):
    changelog_path = "changelog.md"
    with open(changelog_path, "r") as f:
        lines = f.readlines()

    with open(changelog_path, "w") as f:
        for line in lines:
            f.write(line)
            if line.strip() == "## [Unreleased]":
                f.write(f'\n## [{version}] - {datetime.now().strftime("%Y-%m-%d")}\n')


def main():
    bump_type = "patch"

    if len(sys.argv) > 1:
        if sys.argv[1] not in ["patch", "minor", "major"]:
            print("Invalid bump type. Use 'patch', 'minor', or 'major'.")
            sys.exit(1)
        bump_type = sys.argv[1]

    # Bump the version
    subprocess.run(["poetry", "run", "bump2version", bump_type], check=True)

    # Get the new version
    new_version = get_current_version()

    # Update the changelog
    update_changelog(new_version)

    # Commit and tag the changes
    subprocess.run(
        ["git", "commit", "-am", f"Bump version to {new_version}"], check=True
    )
    subprocess.run(["git", "tag", f"v{new_version}"], check=True)


if __name__ == "__main__":
    main()
