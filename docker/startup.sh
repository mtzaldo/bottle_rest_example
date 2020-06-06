#!/bin/bash

pip install --upgrade pip
pip install -r requirements.txt

python -m unittest

status=$?

if [ $status != 0 ]; then
    echo ""
    echo "Tests FAILED: exit container"
    exit $status
fi

cd ./rest

python ./startup.py