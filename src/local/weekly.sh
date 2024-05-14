#!/usr/bin/sh
dir='/home/mat/Documents'
dates=$(date +%Y-%m-%d)
hour=$(date +%H)
minu=$(date +%M)
if [ ${hour} -ge 0 ]; then
  if [ ${minu} -gt 0 ]; then
    . ${dir}/venv11/bin/activate
      python3 ${dir}/weekly.py ${dates}
    deactivate
  fi
fi
