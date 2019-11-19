#!/usr/bin/env bash
#cd /home/ec2-user/Dev/trydjango
#source bin/activate
#cd /home/ec2-user/Dev/trydjango/src
#kill $(ps aux |grep runserver | grep 'Sl+' | awk -F' ' '{print $2}')


cd /home/ec2-user/Dev/trydjango
source bin/activate
cd /home/ec2-user/Dev/trydjango/src
pid=$(ps aux |grep runserver | grep 'Sl' | awk -F' ' '{print $2}')
if [ ! -z $pid]

then kill $pid

fi

