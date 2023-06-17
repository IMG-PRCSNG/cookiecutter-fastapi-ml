#! /bin/bash

set -euo pipefail

# Create user if it doesn't exist
USER_ID=${LOCAL_UID}
GROUP_ID=${LOCAL_GID:-$LOCAL_UID}

id -g "${GROUP_ID}" &>/dev/null || groupadd --gid ${GROUP_ID} user
id -u "${USER_ID}" &>/dev/null || useradd \
    --uid ${USER_ID} \
    --gid ${GROUP_ID} \
    --create-home \
    --home /home/user \
    --shell /bin/bash \
    --comment "user" \
    user

export HOME=/home/user
echo "Starting with UID: ${USER_ID}, GID: ${GROUP_ID} - $@"

# Activate conda environment
source /opt/conda/etc/profile.d/conda.sh
conda activate {{ cookiecutter.project_slug }}-env

# gosu exec
exec /usr/sbin/gosu user "$@"