import subprocess
import sys


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


def main():
    bump_type = "patch"

    if len(sys.argv) > 1:
        if sys.argv[1] not in ["patch", "minor", "major"]:
            print("Invalid bump type. Use 'patch', 'minor', or 'major'.")
            sys.exit(1)
        bump_type = sys.argv[1]

    # Bump the version
    new_version = bump_version(bump_type)
    print(f"Bumped version to {new_version}")


if __name__ == "__main__":
    main()
