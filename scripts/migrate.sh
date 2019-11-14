#!/usr/bin/env bash
cd /Dev/trydjango/src/
source /root/Dev/trydjango/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
