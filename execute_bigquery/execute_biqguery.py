import os
from google.cloud import bigquery


class ExecuteBiqguery():

    def __init__(self,
                client:bigquery.Client,
                credential_path:str,
                path_files:str,
                project:str,
                dataset:str
                ):

        self.client= client
        self.credential_path= credential_path
        self.path_files= path_files
        self.project= project
        self.dataset= dataset


        

    def execute_query(self,query):
        query_job = self.client.query(query)  # Make an API request.

        print("Job data:")
        print(query_job)



    def define_project_dataset(self,query):
        return query\
                .replace('[project]',self.project)\
                .replace('[dataset]',self.dataset)


    def read_files(self):
        return os.listdir(self.path_files)

    def extract_query(self,path_file):
        with open(f"{self.path_files}/{path_file}") as sql:
            return sql.read()


    def run(self):
        for file in self.read_files():
            query = self.extract_query(file)
            query = self.define_project_dataset(query)     
            
            self.execute_query(query)
            