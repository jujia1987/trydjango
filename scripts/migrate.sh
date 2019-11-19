#!/usr/bin/env bash
cd /home/ec2-user/Dev/trydjango/src/trydjango
sed -e 's/DEBUG = True/DEBUG = False/g' settings.py > settings.py #overwrite the file
echo 'Start Migration'
cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src
python3 manage.py makemigrations
python3 manage.py migrate
