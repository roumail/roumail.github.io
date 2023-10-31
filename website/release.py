import hashlib
import os

import toml


def get_or_create_sha1(filename, last_sha_file):
    if not os.path.exists(filename):
        print(f"Warning: {filename} does not exist. Cannot check for changes.")
        return None

    current_sha = get_sha1(filename)

    if not os.path.exists(last_sha_file):
        with open(last_sha_file, "w") as f:
            f.write(current_sha)
        print(
            f"Warning: {last_sha_file} did not exist. Created with the current SHA of {filename}."
        )
        return current_sha

    with open(last_sha_file, "r") as f:
        last_sha = f.read().strip()

    if current_sha == last_sha:
        print("Warning: body.md has not changed since the last release.")
        return False
    else:
        with open(last_sha_file, "w") as f:
            f.write(current_sha)
        print("body.md has changed. Updating the last SHA.")

    return current_sha


def get_sha1(filename):
    sha1 = hashlib.sha1()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()


def get_version_from_pyproject():
    pyproject_data = toml.load("pyproject.toml")
    return pyproject_data["tool"]["poetry"]["version"]
