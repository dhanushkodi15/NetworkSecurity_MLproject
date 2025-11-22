from NetworkSecurity.Exception.exception import NetworkSecurityException

import os,sys

class NetworkModelEstimator:
    def __init__(self, preprocessor,model):
        try:
            self.model = model
            self.preprocessor = preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def predict(self,X):
        try:
            X_transformed = self.preprocessor.transform(X)
            y_pred = self.model.predict(X_transformed)
            return y_pred
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
