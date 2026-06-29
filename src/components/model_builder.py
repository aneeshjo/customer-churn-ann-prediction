"""
Builds the Artificial Neural Network.
"""

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from src.configuration import ConfigurationManager
from src.logger import logger


class ANNModelBuilder:

    def __init__(self):

        config = ConfigurationManager()

        self.model_config = config.get_model_config()

        self.training_config = config.get_training_config()

    def build_model(self, input_dim: int):

        logger.info("Building ANN Model")

        model = Sequential()

        hidden_layers = self.model_config.hidden_layers

        dropout = self.model_config.dropout

        activation = self.model_config.activation

        # -------------------------------
        # First Hidden Layer
        # -------------------------------

        model.add(

            Dense(

                hidden_layers[0],

                activation=activation,

                input_shape=(input_dim,)

            )

        )

        if dropout[0] > 0:

            model.add(

                Dropout(dropout[0])

            )

        # -------------------------------
        # Remaining Hidden Layers
        # -------------------------------

        for neurons, drop in zip(

            hidden_layers[1:],

            dropout[1:]

        ):

            model.add(

                Dense(

                    neurons,

                    activation=activation

                )

            )

            if drop > 0:

                model.add(

                    Dropout(drop)

                )

        # -------------------------------
        # Output Layer
        # -------------------------------

        model.add(

            Dense(

                1,

                activation=self.model_config.output_activation

            )

        )

        # -------------------------------
        # Compile
        # -------------------------------

        model.compile(

            optimizer=tf.keras.optimizers.Adam(

                learning_rate=self.training_config.learning_rate

            ),

            loss="binary_crossentropy",

            metrics=[

                "accuracy",

                tf.keras.metrics.Precision(),

                tf.keras.metrics.Recall(),

                tf.keras.metrics.AUC()

            ]

        )

        logger.info("Model Built Successfully")

        return model