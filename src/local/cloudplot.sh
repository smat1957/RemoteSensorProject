#!/usr/bin/sh
dir='/home/mat/Documents'
today=$(date +%Y-%m-%d)
yesterday=$(date --date "${today} 1 days ago" +%Y-%m-%d)
days='1'
if [ $# -eq 0 ]; then
  days='1'
  dates=$yesterday
elif [ $# -eq 1 ]; then
  days=$1
  dates=$yesterday
elif [ $# -eq 2 ]; then
  days=$1
  if [ $(date -d "$2" +%s) -ge $(date -d "${today}" +%s) ]; then
    dates=$yesterday
  else
    dates=$2
  fi
fi
if [ $# -le 2 ]; then
  # echo $dates $days
  . ${dir}/venv11/bin/activate
    python3 ${dir}/cloudplot.py ${dates} ${days}
  deactivate
fi
