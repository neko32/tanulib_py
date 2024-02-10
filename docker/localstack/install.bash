#!/bin/bash
set -x

if [ -z "${HOME_TMP_DIR}" ] || [ ! -d ${HOME_TMP_DIR} ]; then
    echo "HOME_TMP_DIR must be defined and it must be a directory"
    exit 1
fi

export LOCALSTACK_DOCKER_NAME=tlib_localstack
export LOCALSTACK_VOLUME_DIR=${HOME_TMP_DIR}/tlib_localstack_volume

docker-compose up -d
