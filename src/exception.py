"""
exception.py

Provides a custom exception class that includes
the filename and line number where the error occurred.
"""

import sys


def error_message_detail(error, error_detail: sys):
    """
    Returns detailed error information.
    """

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"Error occurred in Python script: [{file_name}] "
        f"Line Number: [{exc_tb.tb_lineno}] "
        f"Error Message: [{str(error)}]"
    )


class CustomException(Exception):
    """
    Custom Exception Class.
    """

    def __init__(self, error_message, error_detail: sys):

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):

        return self.error_message