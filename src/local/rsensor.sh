#!/usr/bin/bash
### sudo apt install -y sshpass ###
dir='/home/mat/Documents'
sshpass -p passion40 ssh mat@192.168.3.27 ~/Documents/sensor.sh >> "${dir}"/w.txt
