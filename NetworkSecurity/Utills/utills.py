
import pickle
import yaml
from NetworkSecurity.Exception.exception import NetworkSecurityException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import sys
import os,numpy as np

## Read yaml file
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
## Write yaml file
def write_yaml_file(file_path: str, data: dict) -> None:
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
## Save numpy array data to file
def save_numpy_array_data(file_path: str, array) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_object(file_path: str, obj) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def load_object(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) 
    
def load_numpy_array_data(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict) -> dict:
    try:
        model_report = {}

        for model_name, model in models.items():
            param = params.get(model_name, {})
            gs = GridSearchCV(model, param, cv=3, n_jobs=-1)
            gs.fit(X_train, y_train)
            best_model = gs.best_estimator_
            best_model.fit(X_train, y_train)
            y_test_pred = best_model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            model_report[model_name] = test_model_score
        print( model_report)
        return model_report
    except Exception as e:
        raise NetworkSecurityException(e, sys)