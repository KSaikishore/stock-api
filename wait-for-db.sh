#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput
set -e

while ! nc -z db 5432; do
    echo "Waiting for the postgress Server"
    echo $SQL_HOST
    sleep 3
done
# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations main
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000