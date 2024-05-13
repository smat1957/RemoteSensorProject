#!/usr/bin/sh
TODAY=$(date +%Y-%m-%d)
PASS='mypassword'
USR='mat'
ADDR='192.168.3.27'
DIR='/home/mat/Documents'
cp ${DIR}/w.txt ${DIR}/bkup.txt
python3 ${DIR}/lackdata.py | \
while read LINE; do (
  grep ^${LINE} ${DIR}/bkup.txt > ${DIR}/${LINE}.wrk
  sshpass -p ${PASS} ssh -n ${USR}@${ADDR} \
    "grep ^${LINE} ${DIR}/w.txt" >> ${DIR}/${LINE}.wrk
  CMD=test\ -e\ ${DIR}/data/${LINE}.txt
  RC=$(sshpass -p ${PASS} ssh -n ${USR}@${ADDR} ${CMD};echo $?)
  if [ ${RC} -eq 0 ]; then
    sshpass -p ${PASS} ssh -n ${USR}@${ADDR} \
      "grep ^${LINE} ${DIR}/data/${LINE}.txt" >> ${DIR}/${LINE}.wrk
  else
    echo ${LINE}.txt ': not exists at remote machine'
  fi
  sort ${DIR}/${LINE}.wrk | uniq - > ${DIR}/${LINE}.wrk2
  rm ${DIR}/${LINE}.wrk
  if [ -s ${DIR}/${LINE}.wrk2 ]; then
    match=$(echo "${LINE}" | awk "/^${TODAY}/")
    if [ -n "${match}" ]; then
      cp ${DIR}/${LINE}.wrk2 ${DIR}/w.txt
    else
      cp ${DIR}/${LINE}.wrk2 ${DIR}/data/${LINE}.txt
    fi
  fi
  rm ${DIR}/${LINE}.wrk2
) < /dev/null; done
