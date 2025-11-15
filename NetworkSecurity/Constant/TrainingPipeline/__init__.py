import os,sys


## start data ingestion constants

DATA_INGESTION_COLLECTION_NAME = "Network_data"
DATA_INGESTION_DATABASE_NAME = "KODI"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION = 0.3

## TRAINING PIPELINE CONSTANTS

PIPELINE_NAME = "NetworkSecurityPipeline"
ARTIFACT_DIR = "artifacts"
TARGET_COLUMN = "CLASS_LABEL"
FILE_NAME = "phisingdataset.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
