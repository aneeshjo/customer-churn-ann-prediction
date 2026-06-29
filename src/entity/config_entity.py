"""
Entity Classes

These classes define the structure of our configuration.

Using dataclasses makes the code cleaner,
more readable,
and provides type hints.
"""

from dataclasses import dataclass


@dataclass
class TrainingConfig:

    epochs: int

    batch_size: int

    learning_rate: float

    validation_split: float

    random_state: int


@dataclass
class ModelConfig:

    hidden_layers: list

    activation: str

    output_activation: str


@dataclass
class CallbackConfig:

    early_stopping_patience: int

    reduce_lr_patience: int

    checkpoint_monitor: str