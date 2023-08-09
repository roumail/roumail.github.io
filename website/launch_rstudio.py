from invoke import task
from .rosetta import check_rosetta
from .constants import construct_image_name, create_base_docker_run_options


@task(pre=[check_rosetta])
def launch_rstudio(c, project_root_dir, tag, host_port=8787):
    dockerhub_image = construct_image_name(tag)
    docker_run_options = create_base_docker_run_options(project_root_dir)

    launch_options = (
        f"-p {host_port}:8787",
        "-p 60791:60791",
        "-e PASSWORD=yourpassword",
        "--name rstudio_server",
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
