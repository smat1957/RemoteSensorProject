import sys
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.dates as mdates
from myplot import graph_plot

dirstr = '/home/mat/Documents'
s_format = '%Y-%m-%d'
today = dt.now()
if len(sys.argv) > 1:
    today = dt.strptime(sys.argv[1], s_format)
startstr = (today - timedelta(days=7)).strftime(s_format)

datelist = []
for i in range(7):
    day = today - timedelta(days=(7-i))
    datelist.append(day.strftime(s_format))

list0=[]
for fname in datelist:
    try:
        with open(dirstr + "/data/" + fname + ".txt") as f:
            for line in f:
                datestr = line[:20].strip()
                datev = mdates.datestr2num(datestr)
                value = float(line[25:].strip())
                list0.append([datev, value])
    except FileNotFoundError:
        continue

graph_plot(list0, dirstr, startstr, True)