#!/bin/bash

set -e
echo "in for celery"
while ! nc -z django 8000; do
    echo "Waiting for the django Server"
    echo $SQL_HOST
    sleep 3
done
echo "done waiting for django server, starting celery"
celery -A stockapi worker -l INFO