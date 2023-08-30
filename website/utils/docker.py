from website.etc.constants import (
    DOCKERHUB_REPO,
    DOCKERHUB_USERNAME,
    PROJECT_DIR_CONTAINER,
    RENV_PATHS_CACHE_CONTAINER,
    RENV_PATHS_LIBRARY,
)


def construct_image_name(tag):
    return f"{DOCKERHUB_USERNAME}/{DOCKERHUB_REPO}:{tag}"


def create_base_docker_run_options(project_dir_host):
    return (
        "--platform linux/x86_64",
        "--rm",
        f"-v {project_dir_host}:{PROJECT_DIR_CONTAINER}",
        f"-e RENV_PATHS_CACHE={RENV_PATHS_CACHE_CONTAINER}",
        f"-e RENV_PATHS_LIBRARY={RENV_PATHS_LIBRARY}",
    )


def create_volume_mounts(volume_mounts):
    return [f"-v {mount['local']}:{mount['container']}" for mount in volume_mounts]
