#!/bin/bash

echo copy the following to your profile

export TANULIB_HOME=/home/yourhomedir/dir_tanulib_located
export TANULIB_CONF_DIR=${TANULIB_HOME}/conf's dir
export TANULIB_DOC_DIR=replace with your doc dir
export TANULIB_BROWSER=microsoft-edge
export HOME_TMP_DIR="replace with your home dir's tmp"
export HOME_DB_PATH=/home/yourhomedir/db loc
export TLIB_ML_DATA_DIR=replace with your ML data set dir
export TANUAPP_DIR=app store dir
export TANUAPP_ML_DIR=${TANUAPP_DIR}/ml
export ENV=local

export AWS_PROFILE=localstack

# API, mostlikey APIKEY, SECRET ..
export API__(API NAME)__(env, dev|qa|prod|local|local_ut)__(VAR NAME)=xxx

alias tlibut='tlib_ut.bash'
alias tlibi='tlib_install.bash'
alias tlibs='tlib_s.bash'
alias tlibu='tlib_uninstall.bash'
alias gotlib="cd ${TANULIB_HOME}"
alias lsst='localstack_start.bash'
alias lsstop='localstack_stop.bash'
alias redisst='redis_start.bash'
alias redosstop='redis_stop.bash'
alias httpbinst='httpbin_start.bash'
alias httpbinstop='httpbin_stop.bash'
alias ap8='autopep8 -i'
alias apf='apf.bash'
alias tlibdgen='docgen.bash'
alias tlibdoc="${TANULIB_BROWSER} ${TANULIB_DOC_DIR}/api/index.html > dev/null 2>&1"
alias gomld="cd ${TLIB_ML_DATA_DIR}"
alias cvatst='cvat_start.bash'

FLASKAPP_CFG_PATH=${TANULIB_CONF_DIR}/flaskapp
FLASKAPP_CATDOG_UI_{ENV}_CFG_PATH=xxx

export PATH=${PATH}:${TANULIB_HOME}/scripts

CVAT_DIR={dir for cvat}
export FIFTYONE_CVAT_USERNAME=<YOUR_USERNAME>
export FIFTYONE_CVAT_PASSWORD=<YOUR_PASSWORD>

alias kubectl='minikube kubectl --'
alias kubels='kubectl get pod -A'

export TXFR_OUT=${HOME_TMP_DIR}/txfr_out
alias txfr_out='txfr_out.bash'

