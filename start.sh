#!/bin/bash

if [ "$VIRTUAL_ENV" = "" ]; then
    echo "error: not inside inside venv"
    exit 1
fi

mkdir -p store

python3 main.py
