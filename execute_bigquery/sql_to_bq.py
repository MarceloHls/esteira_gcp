from google.cloud import bigquery
import os
import sys

#Credentials

path = "sql"
a = os.listdir(path)
print(f"{path}/{a[0]}")
