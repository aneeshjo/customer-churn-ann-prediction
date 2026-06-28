"""
setup.py

This file is responsible for packaging the project so that
it can be installed as a Python package.
"""

from setuptools import find_packages, setup

# -------------------------------------------------------------------
# Function to read requirements.txt
# -------------------------------------------------------------------

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    """
    Reads the requirements.txt file and returns
    a list of required packages.

    Parameters
    ----------
    file_path : str
        Path to requirements.txt

    Returns
    -------
    list
        List of package names
    """

    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()

        # Remove newline characters
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove editable install if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(

    # Project Name
    name="customer_churn_ann_prediction",

    # Version
    version="0.0.1",

    # Author
    author="Aneesh Jose",

    # Author Email
    author_email="aneeshjose012@gmail.com",

    # Automatically detect all packages
    packages=find_packages(),

    # Install required libraries
    install_requires=get_requirements("requirements.txt")

)