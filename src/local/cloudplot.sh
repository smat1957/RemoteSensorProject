#!/usr/bin/sh
dir='/home/mat/Documents'
today=$(date +%Y-%m-%d)
dates=$(date --date "${today} 1 days ago" +%Y-%m-%d)
days='1'
if [ $# -gt 0 ]; then
  days=$1
  if [ $# -eq 2 ]; then
  if [ $(date -d "$2" +%s) -lt $(date -d "${today}" +%s) ]; then
    dates=$2
  fi
  fi
fi
if [ $# -le 2 ]; then
  # echo $dates $days
  . ${dir}/venv11/bin/activate
    python3 ${dir}/cloudplot.py ${dates} ${days}
  deactivate
fi
