#!/usr/bin/env bash
cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src
#nohup python3 manage.py runserver 0.0.0.0:8000 &
python3 manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
