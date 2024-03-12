#!/bin/bash

set -x

if [ $# -eq 0 ]; then
    echo "must specify input file"
    exit 1
fi

file=$1

autopep8 -i ${file}
flake8 --max-line-length=100 ${file}
