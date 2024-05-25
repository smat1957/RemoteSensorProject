#!/usr/bin/sh
dir='/home/mat/Documents'
today=$(date +%Y-%m-%d)
days='1'
if [ $# -ge 1 ]; then
  days=$1
  if [ $# -eq 2 ]; then
    today=$2
  fi
fi
dates=$(date --date "${today} ${days} days ago" +%Y-%m-%d)
. ${dir}/venv11/bin/activate
  python3 ${dir}/cloudplot.py ${dates} ${days}
deactivate
