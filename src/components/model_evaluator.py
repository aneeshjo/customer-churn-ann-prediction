"""
Model Evaluation Component
"""

import json
import os
import pickle
import sys

import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay
)

from src.logger import logger
from src.exception import CustomException


class ModelEvaluator:

    def __init__(self):

        self.report_dir = "artifacts/reports"

        os.makedirs(
            self.report_dir,
            exist_ok=True
        )

    def evaluate(
        self,
        model,
        history,
        X_test,
        y_test
    ):

        try:

            logger.info("Evaluating Model")

            # -----------------------
            # Predictions
            # -----------------------

            probabilities = model.predict(X_test)

            predictions = (
                probabilities >= 0.5
            ).astype(int)

            # -----------------------
            # Metrics
            # -----------------------

            metrics = {

                "Accuracy":
                    float(
                        accuracy_score(
                            y_test,
                            predictions
                        )
                    ),

                "Precision":
                    float(
                        precision_score(
                            y_test,
                            predictions
                        )
                    ),

                "Recall":
                    float(
                        recall_score(
                            y_test,
                            predictions
                        )
                    ),

                "F1 Score":
                    float(
                        f1_score(
                            y_test,
                            predictions
                        )
                    ),

                "ROC AUC":
                    float(
                        roc_auc_score(
                            y_test,
                            probabilities
                        )
                    )

            }

            # -----------------------
            # Save metrics
            # -----------------------

            with open(

                os.path.join(
                    self.report_dir,
                    "metrics.json"
                ),

                "w"

            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4
                )

            # -----------------------
            # Classification Report
            # -----------------------

            report = classification_report(
                y_test,
                predictions
            )

            with open(

                os.path.join(
                    self.report_dir,
                    "classification_report.txt"
                ),

                "w"

            ) as file:

                file.write(report)

            # -----------------------
            # Confusion Matrix
            # -----------------------

            cm = confusion_matrix(
                y_test,
                predictions
            )

            disp = ConfusionMatrixDisplay(cm)

            disp.plot()

            plt.savefig(

                os.path.join(
                    self.report_dir,
                    "confusion_matrix.png"
                )

            )

            plt.close()

            # -----------------------
            # ROC Curve
            # -----------------------

            RocCurveDisplay.from_predictions(

                y_test,

                probabilities

            )

            plt.savefig(

                os.path.join(
                    self.report_dir,
                    "roc_curve.png"
                )

            )

            plt.close()

            # -----------------------
            # Precision Recall Curve
            # -----------------------

            PrecisionRecallDisplay.from_predictions(

                y_test,

                probabilities

            )

            plt.savefig(

                os.path.join(
                    self.report_dir,
                    "precision_recall_curve.png"
                )

            )

            plt.close()

            # -----------------------
            # Training History
            # -----------------------

            history_dict = history.history

            plt.figure(figsize=(10, 5))

            plt.plot(
                history_dict["loss"],
                label="Train Loss"
            )

            plt.plot(
                history_dict["val_loss"],
                label="Validation Loss"
            )

            plt.legend()

            plt.grid(True)

            plt.savefig(

                os.path.join(
                    self.report_dir,
                    "training_history.png"
                )

            )

            plt.close()

            logger.info("Evaluation Completed")

            return metrics

        except Exception as e:

            raise CustomException(
                e,
                sys
            )