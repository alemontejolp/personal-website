#!/usr/bin/env bash

# Script to deploy on render natively.

# exit on error
set -o errexit

poetry install
# pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
