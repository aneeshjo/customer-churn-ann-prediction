"""
Training Pipeline
"""

from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer


class TrainPipeline:

    def run(self):

        ingestion = DataIngestion()

        ingestion.initiate_data_ingestion()

        preprocessing = DataPreprocessing()

        (

            X_train,

            X_test,

            y_train,

            y_test,

            preprocessor

        ) = preprocessing.initiate_data_preprocessing()

        trainer = ModelTrainer()

        model, history = trainer.train(

            X_train,

            y_train

        )

        return (

            model,

            history,

            X_test,

            y_test

        )