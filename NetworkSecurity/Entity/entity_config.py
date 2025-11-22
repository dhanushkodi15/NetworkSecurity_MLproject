from datetime import datetime
import os
from NetworkSecurity.Constant import TrainingPipeline

class DataIngestionConfig:
    def __init__(self):
        self.database_name = TrainingPipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = TrainingPipeline.DATA_INGESTION_COLLECTION_NAME
        self.data_ingestion_dir = os.path.join(TrainingPipeline.ARTIFACT_DIR,
                                               TrainingPipeline.DATA_INGESTION_DIR_NAME,
                                                f"{datetime.now().strftime('%d_%m_%Y__%H_%M_%S')}")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,
                                              TrainingPipeline.DATA_INGESTION_FEATURE_STORE_DIR)
        self.ingested_dir = os.path.join(self.data_ingestion_dir,
                                         TrainingPipeline.DATA_INGESTION_INGESTED_DIR)
        self.train_file_path = os.path.join(self.ingested_dir,
                                            TrainingPipeline.TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.ingested_dir,
                                           TrainingPipeline.TEST_FILE_NAME)
        self.train_test_split_ratio = TrainingPipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION

class TrainingPipelineConfig:
    def __init__(self):
        self.pipeline_name = TrainingPipeline.PIPELINE_NAME
        self.artifact_name = TrainingPipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,
                                         f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        self.target_column = TrainingPipeline.TARGET_COLUMN
        self.file_name = TrainingPipeline.FILE_NAME

class DataValidationConfig:
    def __init__(self):
        self.data_validation_dir = os.path.join(TrainingPipeline.ARTIFACT_DIR,
                                                TrainingPipeline.DATA_VALIDATION_DIR_NAME,
                                                f"{datetime.now().strftime('%d_%m_%Y__%H_%M_%S')}")
        self.valid_data_dir =  os.path.join(self.data_validation_dir,
                                            TrainingPipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir = os.path.join(self.data_validation_dir,
                                             TrainingPipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path = os.path.join(self.valid_data_dir,
                                              TrainingPipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path = os.path.join(self.valid_data_dir,
                                             TrainingPipeline.TEST_FILE_NAME)
        self.invalid_train_file_path = os.path.join(self.invalid_data_dir,
                                              TrainingPipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path = os.path.join(self.invalid_data_dir,
                                             TrainingPipeline.TEST_FILE_NAME)
        self.drift_report_dir = os.path.join(self.data_validation_dir,
                                             TrainingPipeline.DATA_VALIDATION_DRIFT_REPORT_DIR)
        self.drift_report_file_path = os.path.join(self.drift_report_dir,
                                                  TrainingPipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        

class DataTransformationConfig():
    def __init__(self):
        self.data_transformation_dir = os.path.join(TrainingPipeline.ARTIFACT_DIR,
                                                    TrainingPipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_data_dir = os.path.join(self.data_transformation_dir,
                                                 TrainingPipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR)
        self.transformed_object_dir = os.path.join(self.data_transformation_dir,
                                                  TrainingPipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR)
        self.transformed_train_file_path = os.path.join(self.transformed_data_dir,
                                                        TrainingPipeline.TRAIN_FILE_NAME.replace("csv","npy"))
        self.transformed_test_file_path = os.path.join(self.transformed_data_dir,
                                                       TrainingPipeline.TEST_FILE_NAME.replace("csv","npy"))
        self.transformed_object_file_path = os.path.join(self.transformed_object_dir,
                                                        TrainingPipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_FILE_NAME)
        self.imputer_params = TrainingPipeline.DATA_TRANSFORMATION_IMPUTER

class ModelTrainerConfig():
    def __init__(self):
        self.model_trainer_dir = os.path.join(TrainingPipeline.ARTIFACT_DIR,
                                              TrainingPipeline.MODEL_TRAINER_DIR_NAME)
        self.trained_model_file_path = os.path.join(self.model_trainer_dir,
                                                    TrainingPipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
                                                    TrainingPipeline.MODEL_TRAINER_TRAINED_MODEL_FILE_NAME)
        self.base_accuracy = TrainingPipeline.MODEL_TRAINER_BASE_ACCURACY
        self.expected_score_diff = TrainingPipeline.MODEL_TRAINER_EXPECTED_SCORE_DIFF