import subprocess
import sys
from datetime import datetime


def bump_version(bump_type):
    subprocess.run(["bump2version", bump_type], check=True)

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


def update_git(new_version):
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
