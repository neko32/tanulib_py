#!/bin/bash

echo copy the following to your profile

export TANULIB_HOME=/home/yourhomedir/dir_tanulib_located

export AWS_PROFILE=localstack

alias tlibut='tlib_ut.bash'
alias tlibi='tlib_install.bash'
alias tlibu='tlib_uninstall.bash'
alias gotlib="cd ${TANULIB_HOME}"
alias lsst='localstack_start.bash'
alias lsstop='localstack_stop.bash'