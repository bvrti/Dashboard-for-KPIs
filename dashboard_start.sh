#!/bin/bash

WORKDIR="/var/django/projects/dashboard"

cd ${WORKDIR}

gunicorn --bind=0.0.0.0:8822 app.wsgi