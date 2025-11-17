import os,sys,pandas as pd
import numpy as np
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging
from sklearn.impute import KNNImputer
from NetworkSecurity.Constant.TrainingPipeline import DATA_TRANSFORMATION_IMPUTER,TARGET_COLUMN
from NetworkSecurity.Entity.artifacts_config import DataTransformationArtifact, DataValidationArtifact
from NetworkSecurity.Entity.entity_config import DataTransformationConfig
from NetworkSecurity.Utills.utills import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_validation_artifact: DataValidationArtifact):
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
            self.data_transformation_config = data_transformation_config
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info("Reading validated train and test data")
            train_df=pd.read_csv(self.data_validation_artifact.valid_train_file_path)
            test_df=pd.read_csv(self.data_validation_artifact.valid_test_file_path)

            logging.info("Splitting input features and target feature from train and test data")
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]

            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN]

            logging.info("Applying KNN Imputer to handle missing values")
            imputer = KNNImputer(**self.data_transformation_config.imputer_params)

            input_feature_train_arr=imputer.fit_transform(input_feature_train_df)
            input_feature_test_arr=imputer.transform(input_feature_test_df)

            logging.info("Combining input features and target feature into single numpy array for train and test data")
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saving transformed train and test data to specified file paths")
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,
                                    array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,
                                    array=test_arr)
            
            logging.info("Saving transformation object to specified file path")
            save_object(self.data_transformation_config.transformed_object_file_path,
                                    obj=imputer)
            data_transformation_artifact=DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path
                )
            logging.info(f"Data Transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
                                  