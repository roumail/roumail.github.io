PROJECT_ROOT_DIR := $(shell cd ..; pwd) # Go directory up from dockerfiles where you're executing the command
PROJECT_DIR_CONTAINER=/home/rstudio/project
DOCKERHUB_USERNAME := rohailt
DOCKERHUB_REPO := website-env
DOCKERHUB_TAG := linux-amd64-v1.0.1
DOCKERHUB_IMAGE= ${DOCKERHUB_USERNAME}/${DOCKERHUB_REPO}:${DOCKERHUB_TAG}
HOST_PORT ?= 8787

.PHONY: help build install run all launch-rstudio clean-previous-install restore check-rosetta
help:
	@echo "Usage:"
	@echo "	make build              - Build Docker image"
	@echo "	make install            - Install R packages"
	@echo "	make launch-rstudio     - Skip building locally and pull image from docker hub and launch rstudio"

.PHONY: build
build: check-rosetta
	@echo "Building Docker image for linux amd64 architecture..."
	@./build_docker.sh $(DOCKERHUB_IMAGE) > build.log 2>&1

.PHONY: install
install: check-rosetta
	@if [ -d "${PROJECT_ROOT_DIR}/renv" ]; then \
		echo "Previous renv installation detected. Cleaning up..."; \
		make clean-previous-install; \
	fi	
	@echo "Installing R packages..."
	@echo "R project root directory: ${PROJECT_ROOT_DIR}"
	@./run_docker_r_package_and_rstudio.sh "$(PROJECT_ROOT_DIR)" "$(PROJECT_DIR_CONTAINER)" "$(DOCKERHUB_IMAGE)" "$(HOST_PORT)" install

.PHONY: launch-rstudio
launch-rstudio: check-rosetta
	@echo "Running RStudio Server in Docker container, pulling from dockerhub"
	@echo "R project root directory: ${PROJECT_ROOT_DIR}"
	@./run_docker_r_package_and_rstudio.sh ${PROJECT_ROOT_DIR} ${PROJECT_DIR_CONTAINER} ${DOCKERHUB_IMAGE} ${HOST_PORT} launch

.PHONY: check-rosetta
check-rosetta:
	@sysctl -n sysctl.proc_translated >/dev/null 2>&1; \
	if [ $$? -eq 0 ]; then \
		echo "Rosetta is enabled."; \
	else \
		echo "Rosetta is not enabled. Please enable Rosetta and try again."; \
		exit 1; \
	fi

clean-previous-install:
	@echo "Removing previous renv installation files..."
	@echo "Deleting ${PROJECT_ROOT_DIR}/.Rprofile"
	@rm -rf ${PROJECT_ROOT_DIR}/.Rprofile
	@echo "Deleting ${PROJECT_ROOT_DIR}/renv/"
	@rm -rf ${PROJECT_ROOT_DIR}/renv/
	@echo "Previous renv installation files have been removed."
