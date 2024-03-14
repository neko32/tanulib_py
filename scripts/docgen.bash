#!/bin/bash

if [ ! -e ${TANULIB_DOC_DIR} ]; then
    echo "TANULIB_DOC_DIR env is not found"
    exit 1
fi

pdoc ${TANULIB_HOME}/tanukilib/tlib -o ${TANULIB_DOC_DIR}/api
