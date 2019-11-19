#!/usr/bin/env bash
cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src 
sed -e 's/DEBUG = True/DEBUG = False/g' trydjango/settings.py > trydjango/settings.py #overwrite the file
cat trydjango/settings.py | grep DEBUG
echo 'Start Migration'
python3 manage.py makemigrations
python3 manage.py migrate
