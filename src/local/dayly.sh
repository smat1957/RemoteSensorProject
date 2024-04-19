#!/usr/bin/bash
dir='/home/mat/Documents'
dates=`date +%Y-%m-%d`
hour=`date +%H`
minu=`date +%M`
#echo ${dates}
#echo ${hour}
#echo ${minu}
if [ "${hour}" -ge 23 ]; then
  if [ "${minu}" -gt 55 ]; then
    cp "${dir}"/w.txt "${dir}"/bkup.txt
    mv "${dir}"/w.txt "${dir}"/data/"${dates}".txt
    touch "${dir}"/w.txt
    source "${dir}"/venv11/bin/activate
      "${dir}"/venv11/bin/python3 "${dir}"/dayly.py "${dates}"
    deactivate
  fi
fi
