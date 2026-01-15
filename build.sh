#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python src/manage.py collectstatic --no-input

# Run migrations
python src/manage.py migrate

# Create superuser (if configured)
python src/create_superuser.py
