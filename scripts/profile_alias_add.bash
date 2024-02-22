#!/bin/bash

echo copy the following to your profile

export TANULIB_HOME=/home/yourhomedir/dir_tanulib_located
export TANULIB_CONF_DIR=${TANULIB_HOME}/conf's dir
export HOME_TMP_DIR="replace with your home dir's tmp"
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

export PATH=${PATH}:${TANULIB_HOME}/scripts
