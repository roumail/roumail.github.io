import hashlib

import toml


def get_sha1(filename):
    sha1 = hashlib.sha1()
    with open(filename, "rb") as f:
        while chunk := f.read(128):
            sha1.update(chunk)
    return sha1.hexdigest()


def check_sha1(filename, last_sha_file):
    current_sha = get_sha1(filename)
    with open(last_sha_file, "r") as f:
        last_sha = f.read().strip()

    if current_sha == last_sha:
        print("body.md has not changed since the last release. Aborting.")
        return False
    else:
        with open(last_sha_file, "w") as f:
            f.write(current_sha)
        print("body.md has changed. Proceeding with the release.")
        return True


def get_version_from_pyproject():
    pyproject_data = toml.load("pyproject.toml")
    return pyproject_data["tool"]["poetry"]["version"]
