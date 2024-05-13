#!/usr/bin/bash
dir='/home/mat/Documents'
cd ${dir}
source ${dir}/venv11/bin/activate
  python3 ${dir}/rtplot.py
deactivate
