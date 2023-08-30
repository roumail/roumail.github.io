import importlib.metadata

PACKAGE_NAME = "website"
PACKAGE_VERSION = importlib.metadata.version(PACKAGE_NAME)
DOCKERHUB_USERNAME = "rohailt"
DOCKERHUB_REPO = "website-env"
PROJECT_DIR_CONTAINER = "/home/rstudio/project"
HOME_DIR_CONTAINER = "/home/rstudio"
IMAGE_TAG = "linux-amd64-v1.0.2"
RENV_PATHS_CACHE_CONTAINER = f"{PROJECT_DIR_CONTAINER}/renv/cache"
RENV_PATHS_LIBRARY = f"{PROJECT_DIR_CONTAINER}/renv/library"
