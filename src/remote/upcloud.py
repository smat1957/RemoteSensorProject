from datetime import datetime as dt
import sys
from gcloud import GCSWrapper

class cloud(GCSWrapper):
    def __init__(self, proj_name, bkt_name):
        super().__init__(proj_name, bkt_name)

if __name__ == '__main__':
    project_id = "myprojectid"
    bucket_name = "mybucketname"
    CL = cloud(project_id, bucket_name)
    dirstr = '/home/mat/Documents'
    path = dirstr + '/data/'
    datestr = dt.now().strftime('%Y-%m-%d')
    if len(sys.argv) > 1:
        datestr = sys.argv[1]
    CL.upload_file(path+datestr+'.txt', 'data/'+datestr+'.txt')
