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

        

