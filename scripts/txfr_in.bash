#!/bin/bash

set -e
set -x

if [ ! -e ${TXFR_OUT} ]; then
    echo "$TXFR_OUT is not found"
    exit 1
fi

cp -fR ${TXFR_OUT}/* .
