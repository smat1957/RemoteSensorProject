from datetime import datetime as dt, timedelta
import glob

s_format = '%Y-%m-%d'
todaystr = (dt.now() + timedelta(days=0)).strftime(s_format)
today = dt.strptime(todaystr, s_format)

dirstr = '/home/mat/Documents'
wlist = glob.glob(dirstr + '/data/*.txt')
dlist = []
for w in wlist:
    dlist.append(dt.strptime(w[len(dirstr)+6:-4], s_format))
dlist.sort(reverse=True)	# descending order

ten_days = 10
lacklist = []
for d in range(ten_days):
    day = today - timedelta(days=d)
    if day in dlist:
       	continue 
    else:
        lacklist.append(day)

for fname in lacklist:
    #if fname != today:
    with open('lackfiles.txt', 'w') as f:
        f.write(fname.strftime(s_format)+'.txt'+'\n')
