from google.cloud import bigquery
from execute_biqguery import ExecuteBiqguery
import os

# credential_path = 'credentials/credential_file.json'

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
client = bigquery.Client()

project = 'tech-visa-jobs'
dataset = 'teste'
path_files = 'sql'



execute  = ExecuteBiqguery(
    client=client,
    project=project,
    dataset=dataset,
    path_files=path_files
)

execute.run()