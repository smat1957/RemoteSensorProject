#!/usr/bin/sh
dir='/home/mat/Documents'
today=$(date +%Y-%m-%d)
dates=$(date --date "${today} 1 days ago" +%Y-%m-%d)
days='1' rows='2' cols='3'
if [ $# -gt 0 ]; then
  days=$1
  if [ "${days}" -gt 6 ]; then days='6'; fi
  if [ $# -ge 2 ]; then
  if [ $(date -d "$2" +%s) -lt $(date -d "${today}" +%s) ]; then
    dates=$2
  fi
  fi
  if [ $# -ge 3 ]; then
    rows=$3 cols=$4
    if [ "${rows}" -gt 2 ]; then rows='2'; fi
    if [ "${cols}" -gt 3 ]; then cols='3'; fi
  fi
fi
if [ $# -le 4 ]; then
  #echo $# $1 $2 $3 $4
  #echo $dates "$days" "$rows" "$cols"
  . ${dir}/venv11/bin/activate
    python3 ${dir}/cloudplot.py ${dates} ${days} ${rows} ${cols}
  deactivate
fi
