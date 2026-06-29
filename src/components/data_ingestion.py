"""
Data Ingestion Component

Responsibilities:
1. Load dataset
2. Validate file existence
3. Split dataset
4. Save train/test datasets
"""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.configuration import ConfigurationManager
from src.logger import logger
from src.exception import CustomException
import sys


class DataIngestion:

    def __init__(self):

        config = ConfigurationManager()

        self.ingestion_config = config.get_data_ingestion_config()

    def initiate_data_ingestion(self):

        try:

            logger.info("Starting Data Ingestion")

            data_path = Path(self.ingestion_config.raw_data_path)

            if not data_path.exists():
                raise FileNotFoundError(
                    f"Dataset not found: {data_path}"
                )

            df = pd.read_csv(data_path)

            logger.info(f"Dataset Loaded Successfully")

            logger.info(f"Dataset Shape : {df.shape}")

            train_df, test_df = train_test_split(
                df,
                test_size=self.ingestion_config.test_size,
                random_state=self.ingestion_config.random_state,
                stratify=df[self.ingestion_config.target_column]
            )

            Path("artifacts").mkdir(exist_ok=True)

            train_df.to_csv(
                self.ingestion_config.train_data_path,
                index=False
            )

            test_df.to_csv(
                self.ingestion_config.test_data_path,
                index=False
            )

            logger.info("Train/Test Split Completed")

            logger.info("Data Ingestion Finished")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            raise CustomException(e, sys)