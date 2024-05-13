#!/usr/bin/sh
dir='/home/mat/Documents'
cd ${dir}
source ${dir}/venv11/bin/activate
python3 ${dir}/rtplot.py
deactivate
