from datetime import datetime as dt, timedelta
import matplotlib.dates as mdates
import sys, pandas as pd
from gcloud import GCSWrapper
from googleapiclient import discovery, errors
#from oauth2client.client import GoogleCredentials
from google.api_core.exceptions import NotFound
from myplot import graph_plot

class cloud(GCSWrapper):
    def delete_blob(self, blob_name):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name-with-gcs-path"
        blob = self._bucket.blob(blob_name)
        generation_match_precondition = None
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to delete is aborted if the object's
        # generation number does not match your precondition.
        blob.reload()
        # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = blob.generation
        blob.delete(if_generation_match=generation_match_precondition)
        print(f"Blob {blob_name} deleted.")

    def __init__(self, proj_name, bkt_name):
        super().__init__(proj_name, bkt_name)
        self.x = []
        self.y = []
        
    def readdata(self, fname):
        try:
            with open(fname, 'r') as f:
                for line in f:
                    self.chop(line)
        except FileNotFoundError:
            print(f'File {fname} not found')

    def chop(self, line):
        datestr = line[:20].strip()
        #dateval = mdates.datestr2num(datestr)
        value = float(line[25:].strip())
        self.x.append(datestr)
        self.y.append(value)

    def txt2df(self, fname):
        self.readdata(fname)
        self.df = pd.DataFrame({"mdate": self.x, "value": self.y})
        return self.df

    def num2datestr(self, num):
        return num.strftime('%Y-%m-%d, %H:%M:%S')
 
    def df2txt(self):
        ser0 = self.df.loc[:, 'mdate'].values
        ser1 = self.df.loc[:, 'value'].values
        return ser0, ser1
    
    def download_as_string(self, gcs_path):
        blob = self._bucket.blob(gcs_path)
        text = blob.download_as_string().decode()
        return text

if __name__ == '__main__':
    project_id = "superb-runner-423503-c2"
    bucket_name = "mysensor01"
    CL = cloud(project_id, bucket_name)
    #CL.show_file_names()
    dirstr = '/home/mat/Documents'
    path = dirstr + '/data/'
    nargs = len(sys.argv)
    s_format = '%Y-%m-%d'
    span = 1
    if nargs > 1:
        today = dt.strptime(sys.argv[1], s_format)
        if nargs == 3:
            span = int(sys.argv[2])
    
    datelist = []
    if span==1:
        datestr = today.strftime(s_format)
        datelist.append(datestr)
    else:
        for i in range(span):
            day = today + timedelta(days=(i))
            datestr = day.strftime(s_format)
            datelist.append(datestr)
        
    text = ""
    for datestr in datelist:
        try:
            temp = CL.download_as_string('data/'+datestr+'.txt')
        except:
            #print('=> '+datestr+'.txt : NotFoundEception!')
            continue
        text += temp
        
    mini, maxi = 20.0, -20.0
    list0 = []
    for dstr in text.split('\n'):
        if len(dstr)>0:
            line = dstr[:20] + '\t' + dstr[25:].strip()
            for i, l in enumerate(line.split('\t')):
                temp = l.strip()
                if len(temp)>0:
                    if i==0:
                        datev = mdates.datestr2num(temp)
                    else:
                        value = float(temp)
                        mini = value if (mini>value) else mini
                        maxi = value if (maxi<value) else maxi                    
            list0.append([datev, value])
    title = f'Smel Level : Min={mini:0.3f}, Max={maxi:0.3f}'
    fig = graph_plot(list0, title)
    #fig.savefig(dirstr + '/figs/' + startstr + '.png')
