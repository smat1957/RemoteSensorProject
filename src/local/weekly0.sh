#!/usr/bin/sh
dir='/home/mat/Documents'
echo 'Enter last date string : YYYY-mm-dd'
read dates
. ${dir}/venv11/bin/activate
  python3 ${dir}/mycloud.py -w ${dates} | python3 ${dir}/weekly.py
deactivate
