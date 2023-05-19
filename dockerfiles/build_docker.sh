#!/usr/bin/env bash
# build_docker.sh
set -a
DOCKERHUB_IMAGE="$1"

docker build --no-cache --platform linux/amd64 -t ${DOCKERHUB_IMAGE} .

# Run an interactive session with the built image
# docker run --rm -it ${DOCKERHUB_USERNAME}/${DOCKERHUB_REPO}:${DOCKERHUB_TAG} bash

docker push ${DOCKERHUB_IMAGE}