##Funtionality used in entire application
import os 
import sys
import numpy as np 
import pandas as pd 
import dill 

from src.exception import CustomExecption

def save_object(file_path, obj):
    '''
    This function is used to save the object to the file path.
    '''
    try:
        dir_path  = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)     # save file on specific file_path 

    except Exception as e:
        raise CustomExecption(e,sys)
