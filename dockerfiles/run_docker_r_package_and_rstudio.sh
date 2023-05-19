#!/usr/bin/env bash
# run_docker_r_package_and_rstudio.sh

set -a 

PROJECT_DIR_HOST="$1"
PROJECT_DIR_CONTAINER="$2"
DOCKERHUB_IMAGE="$3"
HOST_PORT="$4"
ACTION="$5"
RENV_PATHS_CACHE_CONTAINER=${PROJECT_DIR_CONTAINER}/renv/cache
RENV_PATHS_LIBRARY=${PROJECT_DIR_CONTAINER}/renv/library

# Pull docker image 
docker pull ${DOCKERHUB_IMAGE}

# Set the default host port to 8787 if not specified
if [ -z "${HOST_PORT}" ]; then
    HOST_PORT=8787
fi

# Common docker run options
DOCKER_RUN_OPTIONS=(--platform linux/x86_64 \
--rm -v "${PROJECT_DIR_HOST}:${PROJECT_DIR_CONTAINER}" \
-e RENV_PATHS_CACHE=${RENV_PATHS_CACHE_CONTAINER} \
 -e RENV_PATHS_LIBRARY=${RENV_PATHS_LIBRARY})
    
if [ "${ACTION}" == "install" ]; then
    # Run the container in detached mode
    # docker run -dit "${DOCKER_RUN_OPTIONS[@]}" --name tmp_container_name ${DOCKERHUB_IMAGE} bash
    # Execute your commands in the running container
    # docker exec tmp_container_name su rstudio -c "Rscript ${PROJECT_DIR_CONTAINER}/dockerfiles/install_r_packages.R install"
    # Stop and remove the container
    # docker rm -f tmp_container_name
    # # Run the container and install the packages
    # docker run "${DOCKER_RUN_OPTIONS[@]}" ${DOCKERHUB_IMAGE} Rscript -e 'list.dirs(full.names = TRUE, recursive = TRUE)' #''
    docker run "${DOCKER_RUN_OPTIONS[@]}" ${DOCKERHUB_IMAGE} su rstudio -c "Rscript ${PROJECT_DIR_CONTAINER}/dockerfiles/install_r_packages.R install"
elif [ "${ACTION}" == "launch" ]; then
    # Launch RStudio Server
    LAUNCH_OPTIONS=("-p" "${HOST_PORT}:8787" "-e" "PASSWORD=yourpassword" "--name" "rstudio_server")
    docker run "${DOCKER_RUN_OPTIONS[@]}" "${LAUNCH_OPTIONS[@]}" ${DOCKERHUB_IMAGE} /init
elif [ "${ACTION}" == "restore" ]; then
    # Run the container and restore the packages
    docker run "${DOCKER_RUN_OPTIONS[@]}" ${DOCKERHUB_IMAGE} su rstudio -c "Rscript ${PROJECT_DIR_CONTAINER}/dockerfiles/install_r_packages.R restore"
else
    echo "Invalid action specified. Please use 'install' or 'launch'."
    exit 1
fi
