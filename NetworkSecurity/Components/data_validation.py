from NetworkSecurity.Entity.entity_config import DataIngestionConfig, DataValidationConfig  
from NetworkSecurity.Constant import TrainingPipeline
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging
from NetworkSecurity.Utills.utills import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp

import pandas as pd
import os, sys

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig,
                 data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20} ")
            self.data_validation_config = data_validation_config
            self.data_ingestion_config = data_ingestion_config
            self.schema_file_path = TrainingPipeline.SCHEMA_FILE_PATH
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def read_data(self, filepath: str)->pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def validate_number_of_columns(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> bool:
        try:
            
            schema_content = read_yaml_file(self.schema_file_path)
            expected_num_columns = len(schema_content['columns'])

            logging.info(f"Expected number of columns: {expected_num_columns}")
            logging.info(f"Train data columns: {train_df.shape[1]}, Test data columns: {test_df.shape[1]}")

            if train_df.shape[1] == expected_num_columns and test_df.shape[1] == expected_num_columns:
                logging.info("Number of columns validation successful")
                return True
            else:
                logging.info("Number of columns validation failed")
                return False
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_numerical_of_columns(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> bool:
        try:
            schema_content = read_yaml_file(self.schema_file_path)
            numerical_columns = schema_content['numerical_columns']

            logging.info(f"Numerical columns from schema: {numerical_columns}")

            train_numerical_cols = [col for col in train_df.columns if train_df[col].dtype in ['int64', 'float64']]
            test_numerical_cols = [col for col in test_df.columns if test_df[col].dtype in ['int64', 'float64']]

            logging.info(f"Numerical columns in train data: {train_numerical_cols}")
            logging.info(f"Numerical columns in test data: {test_numerical_cols}")

            if set(numerical_columns).issubset(set(train_numerical_cols)) and set(numerical_columns).issubset(set(test_numerical_cols)):
                logging.info("Numerical columns validation successful")
                return True
            else:
                logging.info("Numerical columns validation failed")
                return False
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def validate_data_drift(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> bool:
        try:
            status = True
            report = {}
            for column in train_df.columns:
                if train_df[column].dtype in ['int64', 'float64']:
                    train_data = train_df[column].dropna()
                    test_data = test_df[column].dropna()
                    ks_statistic, p_value = ks_2samp(train_data, test_data)
                    alpha = 0.05
                    if p_value < alpha:
                        status = False
                        report[column] = {
                            "ks_statistic": float(ks_statistic),
                            "p_value": float(p_value),
                            "drift_status": "Drift Detected"
                        }
                    else:
                        report[column] = {
                            "ks_statistic": float(ks_statistic),
                            "p_value": float(p_value),
                            "drift_status": "No Drift"
                        }
            logging.info("Data drift validation completed")
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(drift_report_file_path, report)
            return status
           

        except Exception as e:
            raise NetworkSecurityException(e, sys)

        
    def initiate_data_validation(self, train_file_path: str, test_file_path: str):
        try:
            train_file_path=self.data_ingestion_config.train_file_path
            test_file_path=self.data_ingestion_config.test_file_path

            ## Read data
            train_df=self.read_data(train_file_path)
            test_df=self.read_data(test_file_path)
            logging.info("Read train and test data completed")

            column_statues=self.validate_number_of_columns(train_df, test_df)
            numerical_columns_status=self.validate_numerical_of_columns(train_df, test_df)
            drift_status=self.validate_data_drift(train_df, test_df)

            os.makedirs(self.data_validation_config.valid_data_dir, exist_ok=True)
            
            train_df.to_csv(self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_df.to_csv(self.data_validation_config.valid_test_file_path, index=False, header=True)
            logging.info("Valid train and test files are saved.")
            return{
                "column_statues": column_statues,
                "numerical_columns_status": numerical_columns_status,
                "drift_status": drift_status
            }
        except Exception as e:
            raise NetworkSecurityException(e, sys)
            
            

        





