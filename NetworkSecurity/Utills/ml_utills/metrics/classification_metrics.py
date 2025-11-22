from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Entity.artifacts_config import ClassificationMetric
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import sys

def calculate_classification_metrics(y_true, y_pred) -> ClassificationMetric:
    try:
        # Calculate metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        roc_auc = roc_auc_score(y_true, y_pred)

        return ClassificationMetric(
            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1_score=f1,
            roc_auc=roc_auc
        )
    except Exception as e:
        raise NetworkSecurityException(e, sys)