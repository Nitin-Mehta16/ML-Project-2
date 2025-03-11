## For Exception handeling 

import sys # sys library will automatically have information about any execption happening 
from src.logger import logging 

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name --> [{0}], line number--> [{1}], error message --> [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error) )
    
    return error_message
    
class CustomExecption(Exception):  ## CustomExecption--> child class  of parent class -->Python's built-in Exception class
    def __init__(self, error_message,error_detail:sys):  #error_detail:sys --> error_detail = sys
        super().__init__(error_message) #Calls super().__init__(error_message), which initializes the built-in Exception class. #The Exception class stores error_message in args
        self.error_message=error_message_details(error_message,error_detail) #if exception clas store erro_message then why are be re defining it?? =>> By default, Python's built-in Exception class will only store the original error message (e.g., "Something went wrong"), But to enhance debugging, we redefine it.
    def __str__(self):
        return self.error_message #__str__ is a special method (dunder method) in Python that defines how an object should be represented as a human-readable string when you use print(object) or str(object).


if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomExecption(e,sys)

        

