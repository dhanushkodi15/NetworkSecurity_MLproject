import sys,os,json,ssl

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

import certifi
certificate_authority=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        pass
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mangodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            ssl_context = ssl.create_default_context(cafile=certifi.where())
            ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2


            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=30000)
            
            self.mongo_client.admin.command('ping')
            self.database=self.mongo_client[self.database]
            self.collection=self.database[collection]
            self.collection.insert_many(self.records)

            return len(self.records)
        
        except pymongo.errors.ConnectionFailure as conn_err:
            raise NetworkSecurityException(f"Connection Error: {conn_err}", sys)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH = os.path.join(os.path.dirname(__file__), "DataSet", "Phishing_Legitimate_full.csv")
    DATABASE="KODI"
    Collection='Network_data'
    network_obj=NetworkDataExtract()
    records=network_obj.csv_to_json(file_path=FILE_PATH)
    no_of_records=network_obj.insert_data_mangodb(records,DATABASE,Collection)
    print(no_of_records)