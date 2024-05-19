#!/usr/bin/sh
dir='/home/mat/Documents'
echo 'Enter date string : YYYY-mm-dd'
read dates
. ${dir}/venv11/bin/activate
  python3 ${dir}/mycloud.py ${dates} | python3 ${dir}/daily.py
deactivate
