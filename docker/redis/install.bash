#!/bin/bash
set -x

export LOCALSTACK_DOCKER_NAME=tlib_localstack
export LOCALSTACK_VOLUME_DIR=${HOME_TMP_DIR}/tlib_localstack_volume

docker-compose up -d
