#!/usr/bin bash
cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src
kill $(ps aux |grep runserver | grep 'Sl+' | awk -F' ' '{print $2}')
