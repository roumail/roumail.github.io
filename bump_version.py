import sys
from datetime import datetime

import toml


# Read the current version from bumpversion configuration
def get_current_version():
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)
        return pyproject["tool"]["poetry"]["version"]


def bump_version(bump_type):
    current_version = get_current_version()
    major, minor, patch = map(int, current_version.split("."))

    if bump_type == "patch":
        patch += 1
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "major":
        major += 1
        minor = 0
        patch = 0

    new_version = f"{major}.{minor}.{patch}"

    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)

    pyproject["project"]["version"] = new_version

    with open("pyproject.toml", "w") as f:
        toml.dump(pyproject, f)

    return new_version


# Update the changelog.md file
def update_changelog(version):
    changelog_path = "CHANGELOG.md"
    with open(changelog_path, "r") as f:
        lines = f.readlines()

    with open(changelog_path, "w") as f:
        for line in lines:
            f.write(line)
            if line.strip() == "## [Unreleased]":
                f.write(f'\n## [{version}] - {datetime.now().strftime("%Y-%m-%d")}\n')


def update_git(new_version):
    import subprocess

    subprocess.run(
        ["git", "commit", "-am", f"Bump version to {new_version}"], check=True
    )
    subprocess.run(
        ["git", "tag", f"v{new_version}", "-m", f"Release v{new_version}"], check=True
    )
    subprocess.run(["git", "push", "origin", f"v{new_version}"], check=True)


def main():
    bump_type = "patch"

    if len(sys.argv) > 1:
        if sys.argv[1] not in ["patch", "minor", "major"]:
            print("Invalid bump type. Use 'patch', 'minor', or 'major'.")
            sys.exit(1)
        bump_type = sys.argv[1]

    # Bump the version
    new_version = bump_version(bump_type)

    # Update the changelog
    update_changelog(new_version)

    # Commit and tag the changes
    update_git(new_version)


if __name__ == "__main__":
    main()
