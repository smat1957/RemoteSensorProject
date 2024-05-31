#!/usr/bin/sh
dir='/home/mat/Documents'
today=$(date +%Y-%m-%d)
dates=$(date --date "${today} 1 days ago" +%Y-%m-%d)
if [ $# -ge 1 ]; then
  if [ $(date -d "$1" +%s) -lt $(date -d "${today}" +%s) ]; then
    dates=$1
  fi
fi
. ${dir}/venv11/bin/activate
  python3 ${dir}/mycloud.py -w ${dates} | python3 ${dir}/weekly.py
deactivate
