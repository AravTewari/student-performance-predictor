import sys
from src.logger import logging

def error_message_detail(error, message: sys):
    _, _, exec_traceback = sys.exc_info()
    file_name = exec_traceback.tb_frame.f_code.co_filename
    err_msg = f"Error in{file_name} at line {exec_traceback.tb_lineno}: {str(error)}"

    return err_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
