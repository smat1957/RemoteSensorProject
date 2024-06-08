from datetime import datetime as dt
from datetime import timedelta
import sys
import pandas as pd
from gcloud import GCSWrapper

class cloud(GCSWrapper):
    def delete_blob(self, blob_name):
        """https://cloud.google.com/storage/docs/samples/storage-delete-file?hl=ja#storage_delete_file-python"""
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

    def list_file_names(self):
        """バケット内のファイル一覧を表示
        """
        #[print(file.name) for file in self._client.list_blobs(self._bucket)]
        list = []
        for file in self._client.list_blobs(self._bucket):
            list.append(file);
        return list	

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

    rdays = 100 
    s_format = '%Y-%m-%d'
    dstr = (dt.now() - timedelta(days=rdays)).strftime(s_format)
    date_obj = dt.strptime(dstr, s_format)
    flist = CL.list_file_names()
    for f in flist:
        for i, fname in enumerate(str(f).split(' ')):
            if i==2:
                if fname[5]!=',' and fname[:5]=='data/':
                    dateobj = dt.strptime(fname[5:15], s_format)
                    if dateobj<date_obj:
                        entry='data/'+fname[5:15]+'.txt'
                        #print(entry)
                        CL.delete_blob(entry)

    dirstr = '/home/mat/Documents'
    path = dirstr + '/data/'
    datestr = dt.now().strftime('%Y-%m-%d')
    if len(sys.argv) > 1:
        datestr = sys.argv[1]
    #print(datestr)
    CL.upload_file(path+datestr+'.txt', 'data/'+datestr+'.txt')
