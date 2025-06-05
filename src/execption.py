import sys

# Helper function to extract error details
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script [{file_name}] at line number [{line_number}] with error message [{str(error)}]"
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base class constructor
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

"""The code provides a custom exception CustomException that, when raised, offers detailed information about where the error occurred in the code (file name and line number) as well as the error message. This can help make debugging easier by offering more specific context than standard Python exceptions."""

