
import yaml
from NetworkSecurity.Exception.exception import NetworkSecurityException
import sys

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