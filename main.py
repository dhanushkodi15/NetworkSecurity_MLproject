
import os,sys
from NetworkSecurity.Entity.entity_config import (
    DataIngestionConfig, 
    TrainingPipelineConfig, 
    DataValidationConfig,
    DataTransformationConfig
    )
from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Components.data_validation import DataValidation
from NetworkSecurity.Components.data_transformation import DataTransformation
from NetworkSecurity.Logging.logger import logging
def main():
    try:
        training_pipelinee_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion(data_ingestion_config)
        train_set, test_set = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed successfully. Train file: {train_set}, Test file: {test_set}")
        data_validation_config=DataValidationConfig()
        data_validation=DataValidation(data_validation_config, data_ingestion_config)
        data_validation_status=data_validation.initiate_data_validation(train_set, test_set)
        logging.info(f"Data validation completed successfully. Status: {data_validation_status}")
        data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation(data_transformation_config,
                                               data_validation.data_validation_artifact)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info(f"Data transformation completed successfully. Artifact: {data_transformation_artifact}")

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
if __name__ == "__main__":
    main()