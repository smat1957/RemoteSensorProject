#!/usr/bin/sh
dir='/home/mat/Documents'
dates="date +%Y-%m-%d"
hour="date +%H"
minu="date +%M"
if [ "${dour}" -ge 23 ]; then
  if [ "${minu}" -gt 55 ]; then
    cp "${dir}"/w.txt "${dir}"/bkup.txt
    mv "${dir}"/w.txt "${dir}"/data/"${dates}".txt
    touch "${dir}"/w.txt
    chmod 666 "${dir}"/w.txt
  fi
fi
