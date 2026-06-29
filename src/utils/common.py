import joblib
from pathlib import Path


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