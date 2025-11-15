from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging 
import pandas as pd
import os, sys, pymongo
from NetworkSecurity.Constant import TrainingPipeline
from NetworkSecurity.Entity.entity_config import DataIngestionConfig
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()

URL=os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_data_ingestion(self):
        try:
            client = pymongo.MongoClient(URL)
            database = client[self.data_ingestion_config.database_name]
            collection = database[self.data_ingestion_config.collection_name]  
            data = pd.DataFrame(list(collection.find()))
            logging.info(f"Data shape from database: {data.shape}")
            if "_id" in data.columns:
                data = data.drop(columns=["_id"], axis=1)
            
            feature_store_dir = self.data_ingestion_config.feature_store_dir
            os.makedirs(feature_store_dir, exist_ok=True)
            feature_store_file_path = os.path.join(feature_store_dir, TrainingPipeline.FILE_NAME)
            data.to_csv(feature_store_file_path, index=False)
            logging.info(f"Feature store file created at: {feature_store_file_path}")

            train_set, test_set = train_test_split(data,
                                                   test_size=self.data_ingestion_config.train_test_split_ratio,train_size=0.7)
            os.makedirs(self.data_ingestion_config.ingested_dir, exist_ok=True)
            train_file_path = self.data_ingestion_config.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path
            train_set.to_csv(train_file_path, index=False)
            test_set.to_csv(test_file_path, index=False)
            logging.info(f"Train and test files created at: {train_file_path} and {test_file_path}")
            return train_file_path, test_file_path
        except Exception as e:
            raise NetworkSecurityException(e, sys)