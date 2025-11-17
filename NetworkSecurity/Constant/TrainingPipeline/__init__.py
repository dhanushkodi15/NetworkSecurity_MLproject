import os,sys
import numpy as np


##data ingestion constants

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

## Validation constants

DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_VALID_DIR = "validated"
DATA_VALIDATION_INVALID_DIR = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"

## Schema file path
SCHEMA_FILE_PATH = os.path.join("Data_Schema","schema.yaml")

## Transformation constants
DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed_data"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_FILE_NAME = "transformed_object.pkl"

DATA_TRANSFORMATION_IMPUTER: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

