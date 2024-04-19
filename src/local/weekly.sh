#!/usr/bin/bash
dir='/home/mat/Documents'
dates=`date +%Y-%m-%d`
hour=`date +%H`
minu=`date +%M`
if [ "${hour}" -ge 0 ]; then
  if [ "${minu}" -gt 0 ]; then
    source "${dir}"/venv11/bin/activate
      "${dir}"/venv11/bin/python3 "${dir}"/weekly.py "${dates}"
    deactivate
  fi
fi
