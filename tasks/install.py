from invoke import task

from website.utils.ConfigManager import ConfigManager
from website.utils.docker import construct_image_name, create_base_docker_run_options

from .rosetta import check_rosetta

config_manager = ConfigManager()
config = config_manager.get_config()


# TODO: check if clean install needed

# clean-previous-install:
# 	@echo "Removing previous renv installation files..."
# 	@echo "Deleting ${PROJECT_ROOT_DIR}/.Rprofile"
# 	@rm -rf ${PROJECT_ROOT_DIR}/.Rprofile
# 	@echo "Deleting ${PROJECT_ROOT_DIR}/renv/"
# 	@rm -rf ${PROJECT_ROOT_DIR}/renv/
# 	@echo "Previous renv installation files have been removed."


@task(pre=[check_rosetta])
def install(c):
    """
    Install R packages.
    If a previous renv installation is detected, it will be cleaned up first.
    """
    project_root_dir, tag = config.get("project_root_dir"), config.get("image_tag")
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
