#!/usr/bin/sh
### sudo apt install -y sshpass ###
dir='/home/mat/Documents'
ip='192.168.3.27'
pass='mypassword'
usr='myuserid'
sshpass -p "${pass}" ssh "${usr}"@"${ip}" ~/Documents/sensor.sh >> "${dir}"/w.txt
