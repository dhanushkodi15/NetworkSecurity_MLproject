
import os,sys
from NetworkSecurity.Entity.entity_config import DataIngestionConfig, TrainingPipelineConfig
from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging
def main():
    try:
        training_pipelinee_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion(data_ingestion_config)
        train_set, test_set = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed successfully. Train file: {train_set}, Test file: {test_set}")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
if __name__ == "__main__":
    main()