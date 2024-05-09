#!/bin/bash
TODAY="date +%Y-%m-%d"
searchstring=${TODAY}.txt
PASS='mypassword'
USR='mat'
ADDR='192.168.3.27'
DIR='/home/mat/Documents'
FILE_NAME=${DIR}/lackfiles.txt
while read LINE
do
  match=$(echo "${LINE}" | awk "/^$searchstring/")
  if [ -n "${match}" ]; then
    cp ${DIR}/w.txt ${DIR}/ww.txt
    sshpass -p ${PASS} ssh ${USR}@${ADDR} cat ${DIR}/w.txt >> ${DIR}/ww.txt
    sort -u ${DIR}/ww.txt > ${DIR}/w.txt
    rm ${DIR}/ww.txt
  else
    CMD=test\ -e\ ${DIR}/data/${LINE}
    RC=$(sshpass -p ${PASS} ssh ${USR}@${ADDR} ${CMD};echo $?)
    if [ ${RC} -eq 0 ]; then
      sshpass -p ${PASS} scp ${USR}@${ADDR}:${DIR}/data/${LINE} ${DIR}/dataalt/${LINE}
    fi
  fi
done < ${FILE_NAME}

