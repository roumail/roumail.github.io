from invoke import task

from .config import read_config, create_volume_mounts
from .rosetta import check_rosetta
from .constants import construct_image_name, create_base_docker_run_options


@task(pre=[check_rosetta])
def launch_rstudio(c):
    """
    Running RStudio Server in Docker container, pulling from dockerhub.
    pass volume mounts, etc
    """
    config = read_config()
    project_root_dir, tag, host_port = (
        config["project_root_dir"],
        config["tag"],
        config["host_port"],
    )
    dockerhub_image = construct_image_name(tag)
    docker_run_options = create_base_docker_run_options(project_root_dir)
    volume_mounts = create_volume_mounts(config["volume_mounts"])

    launch_options = (
        f"-p {host_port}:8787",
        "-p 60791:60791",
        "-e PASSWORD=yourpassword",
        "--name rstudio_server",
        *volume_mounts,
    )

    docker_run_command = (
        "docker run",
        " ".join(docker_run_options),
        " ".join(launch_options),
        dockerhub_image,
        "/init",
    )

    c.run(f"docker pull {dockerhub_image}")
    c.run(" ".join(docker_run_command))
    print("Running RStudio Server in Docker container, pulling from dockerhub")
    print(f"R project root directory: {project_root_dir}")
