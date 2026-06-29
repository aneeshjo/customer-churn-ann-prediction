"""
Model Training Component
"""

import os
import sys
import pickle

import tensorflow as tf

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

from src.configuration import ConfigurationManager
from src.components.model_builder import ANNModelBuilder
from src.logger import logger
from src.exception import CustomException
from src.components.model_evaluator import ModelEvaluator


class ModelTrainer:

    def __init__(self):

        config = ConfigurationManager()

        self.training_config = config.get_training_config()

    def train(

        self,

        X_train,

        y_train

    ):

        try:

            logger.info("Starting Model Training")

            builder = ANNModelBuilder()

            model = builder.build_model(

                input_dim=X_train.shape[1]

            )

            os.makedirs(

                "artifacts/model",

                exist_ok=True

            )

            callbacks = [

                EarlyStopping(

                    monitor="val_loss",

                    patience=10,

                    restore_best_weights=True

                ),

                ReduceLROnPlateau(

                    monitor="val_loss",

                    factor=0.2,

                    patience=5,

                    min_lr=1e-5

                ),

                ModelCheckpoint(

                    filepath="artifacts/model/best_model.keras",

                    monitor="val_loss",

                    save_best_only=True

                )

            ]

            history = model.fit(

                X_train,

                y_train,

                epochs=self.training_config.epochs,

                batch_size=self.training_config.batch_size,

                validation_split=self.training_config.validation_split,

                callbacks=callbacks,

                verbose=1

            )

            with open(

                "artifacts/model/history.pkl",

                "wb"

            ) as file:

                pickle.dump(

                    history.history,

                    file

                )

            logger.info(

                "Training Completed"

            )

            return model, history

        except Exception as e:

            raise CustomException(e, sys)
        
        evaluator = ModelEvaluator()

        metrics = evaluator.evaluate(

        model,

        history,

        X_test,

        y_test

        )

        print(metrics)