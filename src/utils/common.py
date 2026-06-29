import joblib
from pathlib import Path
import tensorflow as tf


def save_object(file_path, obj):

    """
    Saves any Python object using Joblib.
    """

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(obj, file_path)


def load_object(file_path):

    """
    Loads a saved Joblib object.
    """

    return joblib.load(file_path)

def load_model(model_path: str):
    """
    Loads the trained TensorFlow model.
    """
    return tf.keras.models.load_model(model_path)


def load_preprocessor(preprocessor_path: str):
    """
    Loads the saved preprocessing pipeline.
    """
    return joblib.load(preprocessor_path)