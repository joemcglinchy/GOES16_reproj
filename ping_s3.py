import boto3
import os, sys
from boto.s3.connection import S3Connection
import boto

conn = boto.connect_s3()
#conn = S3Connection(profile='default')
bucket = conn.get_bucket('noaa-goes16')
# for key in bucket.list():
    # print key.name.encode('utf-8')
    
    
s3 = boto3.resource('s3')
bucket3 = s3.Bucket('noaa-goes16')