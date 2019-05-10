from sklearn.metrics import (confusion_matrix, accuracy_score,
                             recall_score, precision_score,
                             f1_score, roc_curve, roc_auc_score)


def get(y_true, y_pred):
    # Indicators
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    # Metrics
    recall = recall_score(y_true, y_pred)
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    # ROC
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred)

    return {"indicators": {"tn": tn,
                           "fp": fp,
                           "fn": fn,
                           "tp": tp},
            "metrics":
                {"recall": recall,
                 "accuracy": accuracy,
                 "precision": precision,
                 "f1": f1},
            "roc":
                {"fpr": fpr,
                 "tpr": tpr,
                 "thresholds": thresholds,
                 "auc": auc}}
