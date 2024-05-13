#!/usr/bin/sh
### sudo apt install -y sshpass ###
dir='/home/mat/Documents'
ip='192.168.3.27'
pass='mypassword'
usr='mat'
sshpass -p ${pass} ssh ${usr}@${ip} "bash ${dir}/sensor.sh" >> ${dir}/w.txt
