ARG BASE_IMAGE="ubuntu:22.04"

FROM $BASE_IMAGE as dev

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH=/opt/conda/bin:$PATH


# Setup build dependencies
RUN deps="bzip2 \
    ca-certificates \
    build-essential \
    wget \
    gosu" && \
    apt-get -yq update && \
    apt-get install -y --no-install-recommends ${deps} && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Setup miniconda
ARG CONDA_VERSION=py310_23.3.1-0
ARG CONDA_SHA256SUM=aef279d6baea7f67940f16aad17ebe5f6aac97487c7c03466ff01f4819e5a651
RUN set -x && \
    UNAME_M="$(uname -m)" && \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh" && \
    SHA256SUM=${CONDA_SHA256SUM} && \
    wget "${MINICONDA_URL}" -O miniconda.sh -q && \
    echo "${SHA256SUM} miniconda.sh" > shasum && \
    sha256sum --check --status shasum && \
    mkdir -p /opt && \
    sh miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh shasum && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# Setup environment
WORKDIR /app
COPY environment.yml .
RUN --mount=type=cache,target=/opt/conda/pkgs conda env create -f environment.yml


# Setup entrypoint and commands
COPY docker/entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]
CMD [ "python3", "-m", "ml_fastapi", "serve"]


# Copy Project files in prod image
FROM dev AS prod

COPY {{ cookiecutter.project_slug }} ./{{ cookiecutter.project_slug }}
COPY scripts ./scripts
COPY tests ./tests