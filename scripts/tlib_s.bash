#!/bin/bash

if [ $# -eq 0 ]; then
    echo "must specify (category)/(sample_file)"
elif [ $# -eq 1 ]; then
    echo "must specify sample_file too"
else
    category=$1
    fname=$2
fi

if [ ! -e ${TANULIB_HOME}/sample/${category}/${fname}.py ]; then
    echo "file ${TANULIB_HOME}/sample/${category}/${fname}.py doesn't exist. make sure .py is removed as .py is automatically attached"    
    exit 1
fi

cd ${TANULIB_HOME}/sample/${category}
python3 ./${fname}.py 2>&1 |tee /tmp/tlibs_run.log

echo "done".
