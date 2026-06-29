"""
configuration.py

Responsible for reading config.yaml
and converting it into Python objects.
"""

import yaml

from src.constants import CONFIG_FILE_PATH

from src.entity.config_entity import (
    TrainingConfig,
    ModelConfig,
    CallbackConfig
)


class ConfigurationManager:

    def __init__(self):

        with open(CONFIG_FILE_PATH, "r") as yaml_file:

            self.config = yaml.safe_load(yaml_file)

    # ---------------------------------------------------

    def get_training_config(self):

        training = self.config["training"]

        return TrainingConfig(

            epochs=training["epochs"],

            batch_size=training["batch_size"],

            learning_rate=training["learning_rate"],

            validation_split=training["validation_split"],

            random_state=training["random_state"]

        )

    # ---------------------------------------------------

    def get_model_config(self):

        model = self.config["model"]

        return ModelConfig(

            hidden_layers=model["hidden_layers"],

            activation=model["activation"],

            output_activation=model["output_activation"]

        )

    # ---------------------------------------------------

    def get_callback_config(self):

        callback = self.config["callbacks"]

        return CallbackConfig(

            early_stopping_patience=callback["early_stopping_patience"],

            reduce_lr_patience=callback["reduce_lr_patience"],

            checkpoint_monitor=callback["checkpoint_monitor"]

        )