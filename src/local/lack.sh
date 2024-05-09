#!/bin/bash
TODAY=`date +%Y-%m-%d`
searchstring="${TODAY}.txt"
PWRD='passion40'
USR='mat'
ADDR='192.168.3.27'
DIR='/home/mat/Documents'
FILE_NAME="${DIR}"/lackfiles.txt
while read LINE
do
  match=$(echo "${LINE}" | awk "/^$searchstring/")
  if [ -n "$match" ]; then
    cp "${DIR}"/w.txt "${DIR}"/ww.txt
    sshpass -p "${PWRD}" ssh "${USR}"@"${ADDR}" cat "${DIR}"/w.txt >> "${DIR}"/ww.txt
    sort -u "${DIR}"/ww.txt > ${DIR}/www.txt
    rm ${DIR}/ww.txt
    mv ${DIR}/www.txt ${DIR}/ww.txt
  else
    RC=$(sshpass -p ${PWRD} ssh ${USR}@${ADDR} 'test -f ${DIR}/data/${LINE};echo $?')
    if [ ${RC} -eq 0 ]; then
      sshpass -p "${PWRD}" ssh "${USR}"@"${ADDR}" cat "${DIR}"/data/"${LINE}" > "${DIR}"/dataalt/"${LINE}"
    fi 
  fi 
done < ${FILE_NAME}

