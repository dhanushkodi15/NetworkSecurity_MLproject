import os,sys

from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging
from NetworkSecurity.Utills.ml_utills.model.estimator import NetworkModelEstimator
from NetworkSecurity.Utills.utills import load_numpy_array_data, evaluate_models, load_object, save_object
from NetworkSecurity.Utills.ml_utills.metrics.classification_metrics import calculate_classification_metrics

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from NetworkSecurity.Entity.entity_config import ModelTrainerConfig
from NetworkSecurity.Entity.artifacts_config import DataTransformationArtifact,ModelTrainerArtifact

class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,
                 data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def train_model(self,X_train,y_train, X_test,y_test):
        try:
            models={
                "LogisticRegression":LogisticRegression(),
                "DecisionTree":DecisionTreeClassifier(),
                "RandomForest":RandomForestClassifier(),
                "GradientBoosting":GradientBoostingClassifier(),
                "AdaBoost":AdaBoostClassifier()
            }
            params={
                "LogisticRegression":{},
                "DecisionTree":{
                    'criterion':['gini','entropy'],
                    # 'max_depth':[3,5,10,15],
                },
                "RandomForest":{
                    'n_estimators':[50,100,200],
                    # 'criterion':['gini','entropy'],
                    # 'max_depth':[3,5,10],
                },
                "GradientBoosting":{
                    'learning_rate':[0.01,0.1,0.2],
                    # 'n_estimators':[50,100,200],
                    # 'subsample':[0.6,0.8,1.0],
                },
                "AdaBoost":{
                    'n_estimators':[50,100,200],
                    # 'learning_rate':[0.01,0.1,0.2],
                }
            }
            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,
                                               X_test=X_test,y_test=y_test,
                                               models=models,
                                               params=params)
            
            best_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_score)
            ]
            best_model = models[best_model_name]
            logging.info(f"Best model found , Model Name : {best_model_name} , R2 Score : {best_score}")

            y_train_pred = best_model.predict(X_train)
            classification_metric_train = calculate_classification_metrics(y_true=y_train, y_pred=y_train_pred)

            y_test_pred = best_model.predict(X_test)
            classification_metric_test = calculate_classification_metrics(y_true=y_test, y_pred=y_test_pred)

            preprocessor=load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            model_estimator = NetworkModelEstimator(preprocessor=preprocessor, model=best_model)

            model_dir_path=os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)
            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                        obj=model_estimator)
            
            logging.info(f"Trained model saved at : {self.model_trainer_config.trained_model_file_path}")
            return ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric_artifact=classification_metric_train,
                test_metric_artifact=classification_metric_test
            )
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            train_array = load_numpy_array_data(train_file_path)
            test_array = load_numpy_array_data(test_file_path)

            X_train,y_train = train_array[:,:-1],train_array[:,-1]
            X_test,y_test = test_array[:,:-1],test_array[:,-1]

            return self.train_model(X_train=X_train,y_train=y_train,
                                    X_test=X_test,y_test=y_test)
        except Exception as e:
            raise NetworkSecurityException(e,sys)