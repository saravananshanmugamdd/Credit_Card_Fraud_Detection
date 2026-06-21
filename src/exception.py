import sys

def error_messag_details(error, error_details=sys):
    """this returns detailed error message with file_name and line_number"""
    _,_,exc_tb=error_details.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message=(
        f"error occured in python script :[{file_name}]"
        f"erorr occured in line number :[{exc_tb.tb_lineno}]"
        f"error message :[{str(error)}]"
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_messag_details(
            error_message,
            error_detail
        )

    def __str__(self):
        return self.error_message
