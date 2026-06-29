import sys

import pandas as pd

from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)

from src.configuration import ConfigurationManager
from src.exception import CustomException
from src.logger import logger
from src.utils.common import save_object


class DataPreprocessing:

    def __init__(self):

        config = ConfigurationManager()

        self.ingestion_config = config.get_data_ingestion_config()

        self.preprocessing_config = (
            config.get_data_preprocessing_config()
        )

    def initiate_data_preprocessing(self):

        try:

            logger.info("Loading train and test datasets")

            train_df = pd.read_csv(
                self.ingestion_config.train_data_path
            )

            test_df = pd.read_csv(
                self.ingestion_config.test_data_path
            )

            target = self.ingestion_config.target_column

            X_train = train_df.drop(columns=[target])

            y_train = train_df[target]

            X_test = test_df.drop(columns=[target])

            y_test = test_df[target]

            numerical_columns = X_train.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            categorical_columns = X_train.select_dtypes(
                include=["object"]
            ).columns.tolist()

            logger.info(
                f"Numerical Columns: {numerical_columns}"
            )

            logger.info(
                f"Categorical Columns: {categorical_columns}"
            )

            numeric_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="median")),

                    ("scaler", StandardScaler())

                ]

            )

            categorical_pipeline = Pipeline(

                steps=[

                    (
                        "imputer", 
                        SimpleImputer(strategy="most_frequent")
                    ),

                    (
                        
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        )
                    )

                ]

            )

            preprocessor = ColumnTransformer(

                transformers=[

                    (
                        "num",
                        numeric_pipeline,
                        numerical_columns
                    ),

                    (
                        "cat",
                        categorical_pipeline,
                        categorical_columns
                    )

                ]

            )

            X_train_processed = preprocessor.fit_transform(
                X_train
            )

            X_test_processed = preprocessor.transform(
                X_test
            )

            save_object(

                self.preprocessing_config.preprocessor_path,

                preprocessor

            )

            logger.info(
                "Preprocessor Saved Successfully"
            )

            return (

                X_train_processed,

                X_test_processed,

                y_train,

                y_test,

                preprocessor

            )

        except Exception as e:

            raise CustomException(e, sys)