import pandas as pd
from gcloud import GCSWrapper

class cloud(GCSWrapper):
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
        ser0 = self.df.loc[:, 'mdate']
        ser1 = self.df.loc[:, 'value']
        return ser0, ser1

if __name__ == '__main__':
    project_id = "myprojectid"
    bucket_name = "mybucketname"
    CL = cloud(project_id, bucket_name)
    CL.show_file_names()
    dirstr = '/home/mat/Documents'
    path = dirstr + '/data/'
    datestr = '2024-05-10'
    CL.upload_file(path+datestr+'.txt', 'data/'+datestr+'.txt')
    CL.download_file(dirstr+'/'+datestr+'.txt', 'data/'+datestr+'.txt')
    df = CL.txt2df(dirstr+'/'+datestr+'.txt')
    df.to_csv("gs://"+bucket_name+"/data/"+datestr+".csv", index=False)
    CL.show_file_names()
    data_df = pd.read_csv("gs://"+bucket_name+"/data/"+datestr+".csv")
    print(data_df)
