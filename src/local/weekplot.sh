#!/usr/bin/sh
dir='/home/mat/Documents'
if [ $# -eq 1 ]; then
dates=$1
. ${dir}/venv11/bin/activate
  python3 ${dir}/mycloud.py -w ${dates} | python3 ${dir}/weekly.py
deactivate
fi
