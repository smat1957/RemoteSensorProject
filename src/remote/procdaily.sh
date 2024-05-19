#!/usr/bin/sh
dir='/home/mat/Documents'
dates=$(date +%Y-%m-%d)
hour=$(date +%H)
minu=$(date +%M)
if [ ${hour} -ge 23 ]; then
  if [ ${minu} -gt 57 ]; then
    cp ${dir}/w.txt ${dir}/bkup.txt
    mv ${dir}/w.txt ${dir}/data/${dates}.txt
    touch ${dir}/w.txt
    python3 ${dir}/upload0.py ${dates}
    yesterday=$(date --date "${dates} 1 days ago" +%Y-%m-%d)
    rm ${dir}/data/${yesterday}.txt
  fi
fi
