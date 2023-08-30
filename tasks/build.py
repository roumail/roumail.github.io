import logging
import os

from invoke import task

from website.utils.ConfigManager import ConfigManager
from website.utils.docker import construct_image_name
from website.utils.logging import LoggerFile, get_logger

from .rosetta import check_rosetta

config_manager = ConfigManager()
config = config_manager.get_config()


log = get_logger(__name__)


@task(pre=[check_rosetta])
def build(c):
    """
    Build Docker image for linux amd64 architecture.
    """
    tag = config.get("image_tag")
    uid = os.getuid()
    gid = os.getgid()
    username = os.getlogin()
    image_name = construct_image_name(tag)
    log_file = LoggerFile(log, logging.INFO)

    c.run(
        f"docker build --no-cache --platform linux/amd64 "
        f"--build-arg UID={uid} "
        f"--build-arg GID={gid} "
        f"--build-arg USERNAME={username} "
        f"-t {image_name} .",
        out_stream=log_file,
        err_stream=log_file,
    )
    c.run(f"docker push {image_name}", out_stream=log_file, err_stream=log_file)
