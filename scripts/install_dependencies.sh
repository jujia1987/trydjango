#!/usr/bin bash
yum install -y python3
pip3 install virtualenv
cd /home/ec2-user/Dev/trydjango
export PATH="$PATH:/usr/local/bin/"
virtualenv -p python3 .
source bin/activate
pip3 install django==2.0.7
