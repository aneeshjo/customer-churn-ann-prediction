"""
================================================================================
Project Structure Generator
Project : Customer Churn Prediction using ANN
Author  : Aneesh Jose
================================================================================

Description:
------------
This script automatically creates the complete folder and file structure
required for the Customer Churn ANN project.

Advantages:
-----------
1. Eliminates manual creation of folders and files.
2. Maintains a consistent project architecture.
3. Reusable for future Deep Learning projects.
4. Saves development time.

Usage:
------
python template.py
"""

# ==============================================================================
# Import Required Libraries
# ==============================================================================

import os
from pathlib import Path

# ==============================================================================
# Project Name
# ==============================================================================

PROJECT_NAME = "src"

# ==============================================================================
# List of Files & Folders to Create
# ==============================================================================

list_of_files = [

    # --------------------------------------------------------------------------
    # GitHub Workflow
    # --------------------------------------------------------------------------
    ".github/workflows/.gitkeep",

    # --------------------------------------------------------------------------
    # Configuration
    # --------------------------------------------------------------------------
    "config/config.yaml",

    # --------------------------------------------------------------------------
    # Data
    # --------------------------------------------------------------------------
    "data/.gitkeep",

    # --------------------------------------------------------------------------
    # Artifacts
    # --------------------------------------------------------------------------
    "artifacts/model/.gitkeep",
    "artifacts/preprocessor/.gitkeep",
    "artifacts/reports/.gitkeep",

    # --------------------------------------------------------------------------
    # Logs
    # --------------------------------------------------------------------------
    "logs/.gitkeep",

    # --------------------------------------------------------------------------
    # Jupyter Notebook
    # --------------------------------------------------------------------------
    "notebook/ANN_Experiments.ipynb",

    # --------------------------------------------------------------------------
    # Testing
    # --------------------------------------------------------------------------
    "tests/__init__.py",
    "tests/test_model.py",
    "tests/test_preprocessing.py",

    # --------------------------------------------------------------------------
    # Source Package
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/__init__.py",

    f"{PROJECT_NAME}/logger.py",
    f"{PROJECT_NAME}/exception.py",
    f"{PROJECT_NAME}/configuration.py",

    # --------------------------------------------------------------------------
    # Constants
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/constants/__init__.py",

    # --------------------------------------------------------------------------
    # Entity
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",

    # --------------------------------------------------------------------------
    # Utilities
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/utils/common.py",
    f"{PROJECT_NAME}/utils/dl_utils.py",

    # --------------------------------------------------------------------------
    # Components
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/components/__init__.py",

    f"{PROJECT_NAME}/components/data_ingestion.py",

    f"{PROJECT_NAME}/components/data_preprocessing.py",

    f"{PROJECT_NAME}/components/model_builder.py",

    f"{PROJECT_NAME}/components/model_trainer.py",

    f"{PROJECT_NAME}/components/model_evaluator.py",

    # --------------------------------------------------------------------------
    # Pipelines
    # --------------------------------------------------------------------------
    f"{PROJECT_NAME}/pipeline/__init__.py",

    f"{PROJECT_NAME}/pipeline/train_pipeline.py",

    f"{PROJECT_NAME}/pipeline/predict_pipeline.py",

    # --------------------------------------------------------------------------
    # Root Files
    # --------------------------------------------------------------------------
    "app.py",
    "main.py",
    "setup.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "LICENSE"
]

# ==============================================================================
# Create Project Structure
# ==============================================================================

for filepath in list_of_files:

    # Convert string path into Path object
    filepath = Path(filepath)

    # Separate directory and filename
    filedir, filename = os.path.split(filepath)

    # --------------------------------------------------------------------------
    # Create Folder if it doesn't exist
    # --------------------------------------------------------------------------
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # --------------------------------------------------------------------------
    # Create Empty File
    # --------------------------------------------------------------------------
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as file:
            pass

        print(f"✅ Created : {filepath}")

    else:

        print(f"✔ Already Exists : {filepath}")

print("\nProject Structure Created Successfully!")