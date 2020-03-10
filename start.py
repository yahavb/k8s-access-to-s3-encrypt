#! /usr/bin/python
import time
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
upload_file_name='data.file'
download_file_name='download.data.file'
s3_bucket_name='invitae-sample'


def upload(bucket_name,object_name):
  with open(object_name, "rb") as f:
    s3.upload_fileobj(f, bucket_name,object_name)

def download(bucket_name,object_name,file_name):
  s3.download_file(bucket_name,object_name,file_name)

if __name__ == "__main__":
  while True:
    print('going to upload file {} to bucket {}'.format(s3_bucket_name,upload_file_name))
    print(open(upload_file_name).read())
    upload(s3_bucket_name,upload_file_name)
    print('file uploaded file {} to bucket {}'.format(s3_bucket_name,upload_file_name))
  
    print('going to download file {} to bucket {}'.format(s3_bucket_name,download_file_name))
    file_to_be_dl=download(s3_bucket_name,upload_file_name,download_file_name) 
    print('file {} was downloaded from bucket {}'.format(s3_bucket_name,download_file_name))
    print('------------')
    time.sleep(10) 
