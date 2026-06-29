from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing

# Step 1
ingestion = DataIngestion()
ingestion.initiate_data_ingestion()

# Step 2
preprocessing = DataPreprocessing()

X_train, X_test, y_train, y_test, preprocessor = (
    preprocessing.initiate_data_preprocessing()
)

print(X_train.shape)
print(X_test.shape)