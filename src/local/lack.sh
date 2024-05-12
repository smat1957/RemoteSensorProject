#!/bin/bash
TODAY=$(date +%Y-%m-%d)
PASS='mypassword'
USR='mat'
ADDR='192.168.3.27'
DIR='/home/mat/Documents'
cp ${DIR}/w.txt ${DIR}/bkup.txt
source ${DIR}/venv11/bin/activate
  ${DIR}/venv11/bin/python3 ${DIR}/lackdata.py | \
while read LINE; do (
  grep ^"${LINE}" ${DIR}/w.txt > ${DIR}/"${LINE}".wrk
  sshpass -p ${PASS} ssh -n ${USR}@${ADDR}\
    grep ^"${LINE}" ${DIR}/w.txt >> ${DIR}/"${LINE}".wrk
  CMD=test\ -e\ ${DIR}/data/"${LINE}".txt
  RC=$(sshpass -p ${PASS} ssh -n ${USR}@${ADDR} ${CMD};echo $?)
  if [ ${RC} -eq 0 ]; then
    sshpass -p ${PASS} ssh -n ${USR}@${ADDR}\
      grep ^"${LINE}" ${DIR}/data/${LINE}.txt >> ${DIR}/"${LINE}".wrk
  fi
  sort ${DIR}/"${LINE}".wrk > ${DIR}/"${LINE}".wrk2
  uniq ${DIR}/"${LINE}".wrk2 > ${DIR}/"${LINE}".wrk
  rm ${DIR}/"${LINE}".wrk2
  match=$(echo "${LINE}" | awk "/^${TODAY}/")
  if [ -n "${match}" ]; then
    cp ${DIR}/"${LINE}".wrk ${DIR}/w.txt
  else
    cp ${DIR}/"${LINE}".wrk ${DIR}/data/"${LINE}".txt
  fi
  rm ${DIR}/"${LINE}".wrk
) < /dev/null; done
deactivate
