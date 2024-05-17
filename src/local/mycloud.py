import pandas as pd
from gcloud import GCSWrapper

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
    df.to_csv('gs://'+bucket_name+'/data/'+datestr+'.csv', index=False)
    CL.show_file_names()
    data_df = pd.read_csv('gs://'+bucket_name+'/data/'+datestr+'.csv')
    print(data_df)
    CL.delete_blob('data/'+datestr+'.csv')
    CL.show_file_names()
