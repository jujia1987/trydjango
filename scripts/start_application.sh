#!/usr/bin/env bash
cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src
python3 manage.py runserver 0.0.0.0:8000
