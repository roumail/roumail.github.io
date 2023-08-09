import os
from invoke import task

from .utils.config import read_config
from .rosetta import check_rosetta
from .utils.constants import construct_image_name


@task(pre=[check_rosetta])
def build(c):
    """
    Build Docker image for linux amd64 architecture.
    """
    config = read_config()
    tag = config["image_tag"]
    uid = os.getuid()
    gid = os.getgid()
    username = os.getlogin()
    image_name = construct_image_name(tag)

    c.run(
        f"docker build --no-cache --platform linux/amd64 "
        f"--build-arg UID={uid} "
        f"--build-arg GID={gid} "
        f"--build-arg USERNAME={username} "
        f"-t {image_name} ."
    )
    c.run(f"docker push {image_name}")
