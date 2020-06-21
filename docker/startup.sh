#!/bin/bash

pip install --upgrade pip
pip install -r requirements.txt
pip install flake8

echo "##############################"
echo " Running UNIT TESTS"
echo "##############################"
python -m unittest

status=$?

if [ $status != 0 ]; then
    echo ""
    echo "Tests FAILED: exit container"
    exit $status
fi

echo "##############################"
echo " Running FLAKE8 LINTING"
echo "##############################"
flake8 rest

status=$?

if [ $status != 0 ]; then
    echo ""
    echo "Linting FAILED: exit container"
    exit $status
fi

cd ./rest

python ./startup.py