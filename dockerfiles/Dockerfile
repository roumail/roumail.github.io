FROM rocker/rstudio:4.3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        parallel \
        git \
        libxt-dev \
        xorg \ 
        gawk \
        curl \
        procps \
        libcurl4-openssl-dev \
        autoconf \
        automake \
        gcc \
        python3-pip \
        make \
        libtool \
        pkg-config \
        systemd \
        libxml2-dev\
        wget && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.utf8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

RUN update-alternatives --install /usr/bin/awk awk /usr/bin/gawk 10 && \
    update-alternatives --set awk /usr/bin/gawk   

RUN awk --version


ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV RSTUDIO_USER=rstudio
ENV PROJECT_DIR=/home/${RSTUDIO_USER}/project
WORKDIR ${PROJECT_DIR}