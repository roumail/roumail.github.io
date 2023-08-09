DOCKERHUB_USERNAME = "rohailt"
DOCKERHUB_REPO = "website-env"
PROJECT_DIR_CONTAINER = "/home/rstudio/project"
RENV_PATHS_CACHE_CONTAINER = f"{PROJECT_DIR_CONTAINER}/renv/cache"
RENV_PATHS_LIBRARY = f"{PROJECT_DIR_CONTAINER}/renv/library"


def construct_image_name(tag):
    return f"{DOCKERHUB_USERNAME}/{DOCKERHUB_REPO}:{tag}"


def create_base_docker_run_options(project_dir_host):
    return (
        f"--platform linux/x86_64",
        f"--rm",
        f"-v {project_dir_host}:{PROJECT_DIR_CONTAINER}",
        f"-e RENV_PATHS_CACHE={RENV_PATHS_CACHE_CONTAINER}",
        f"-e RENV_PATHS_LIBRARY={RENV_PATHS_LIBRARY}",
    )
