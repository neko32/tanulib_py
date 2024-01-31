#!/bin/bash

cd ${TANULIB_HOME}/unittest

if [ $# -eq 0 ]; then
    file_to_run=(*.py)
elif [ $# -eq 1 ]; then
    file_to_run=$1
else
    file_to_run=(*.py)
fi

for test_file in "${file_to_run[@]}"
do
    if [[ ${test_file} == test_* ]]; then
        test_file=`echo ${test_file}|awk '{print substr($1, 6)}'`
    fi
    if [[ ${test_file} == *\.py ]]; then
        test_file=`echo ${test_file}|awk '{print substr($1, 0, length($1) - 3)}'`
    fi
    if [ ! -f test_${test_file}.py ]; then
        echo "test file test_${test_file}.py not found. skipping.."
    else
        python3 test_${test_file}.py
    fi
done
