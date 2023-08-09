from invoke import task

from .config import read_config
from .constants import construct_image_name, create_base_docker_run_options
from .rosetta import check_rosetta


@task(pre=[check_rosetta])
def install(c):
    config = read_config()
    project_root_dir, tag = config["project_root_dir"], config["tag"]
    dockerhub_image = construct_image_name(tag)
    docker_run_options = create_base_docker_run_options(project_root_dir)

    r_commands = [
        "install.packages('renv')",
        "renv::init(bare=TRUE)",
        "options(repos = c(CRAN = 'https://cran.r-project.org'))",
        "renv::install(c('blogdown'))",
        "options(renv.config.cache.symlinks = FALSE)",
        "renv::isolate()",
    ]

    r_script = "; ".join(r_commands)

    docker_run_command = (
        "docker run",
        " ".join(docker_run_options),
        dockerhub_image,
        "su rstudio -c",
        f"'Rscript -e \"{r_script}\"'",
    )

    c.run(f"docker pull {dockerhub_image}")
    c.run(" ".join(docker_run_command))
