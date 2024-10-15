import subprocess
import sys
from datetime import datetime


def bump_version(bump_type):
    subprocess.run(["bump2version", "--new-version", bump_type], check=True)

    # Extract the new version from bump2version's output
    result = subprocess.run(
        ["bump2version", "--dry-run", "--list", bump_type],
        capture_output=True,
        text=True,
    )
    new_version = None
    for line in result.stdout.splitlines():
        if line.startswith("new_version="):
            new_version = line.split("=")[-1]

    if not new_version:
        print("Error: Failed to determine the new version.")
        sys.exit(1)
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


def delete_tag(tag):
    # Delete the local and remote tag if it exists
    print(f"Deleting existing tag {tag} locally and remotely...")
    subprocess.run(["git", "tag", "-d", tag], check=True)
    subprocess.run(["git", "push", "origin", f":refs/tags/{tag}"], check=True)


def tag_exists_on_remote(tag):
    result = subprocess.run(
        ["git", "ls-remote", "--tags", "origin", tag], capture_output=True, text=True
    )
    return bool(result.stdout.strip())


def update_git(new_version: str, delete_existing_tag: bool = False):
    # Fetch tags to ensure the local repo is up to date
    subprocess.run(["git", "fetch", "--tags"], check=True)
    tag_name = f"v{new_version}"

    if tag_exists_on_remote(tag_name):
        if delete_existing_tag:
            delete_tag(tag_name)
        else:
            print(f"Tag {tag_name} already exists on the remote. Aborting!")
            sys.exit(1)

    subprocess.run(
        ["git", "commit", "-am", f"Bump version to {new_version}"], check=True
    )

    subprocess.run(
        ["git", "tag", tag_name, "-m", f"Release v{new_version}"], check=True
    )
    subprocess.run(["git", "push", "origin", tag_name], check=True)


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
