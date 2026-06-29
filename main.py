from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_builder import ANNModelBuilder

# -----------------------
# Data Ingestion
# -----------------------

ingestion = DataIngestion()

ingestion.initiate_data_ingestion()

# -----------------------
# Data Preprocessing
# -----------------------

preprocessing = DataPreprocessing()

X_train, X_test, y_train, y_test, preprocessor = (

    preprocessing.initiate_data_preprocessing()

)

# -----------------------
# Model
# -----------------------

builder = ANNModelBuilder()

model = builder.build_model(

    input_dim=X_train.shape[1]

)

model.summary()