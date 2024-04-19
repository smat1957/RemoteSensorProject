#!/usr/bin/bash
dir='/home/mat/Documents'
paste <(date +%Y-%m-%d,\ %H:%M:%S) <(python3 "${dir}"/adrszOD.py | awk '{print $1}')
