"""
Prediction Pipeline
"""

import pandas as pd

from src.utils.common import (
    load_model,
    load_preprocessor
)


class PredictPipeline:

    def __init__(self):

        self.model = load_model(
            "artifacts/model/best_model.keras"
        )

        self.preprocessor = load_preprocessor(
            "artifacts/preprocessor/preprocessor.pkl"
        )

    def predict(self, input_data: dict):

        df = pd.DataFrame([input_data])

        processed = self.preprocessor.transform(df)

        probability = float(
            self.model.predict(processed)[0][0]
        )

        prediction = 1 if probability >= 0.5 else 0

        return {

            "prediction": prediction,

            "probability": round(probability, 4)

        }