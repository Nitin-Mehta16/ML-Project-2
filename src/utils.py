##Funtionality used in entire application
import os 
import sys
import numpy as np 
import pandas as pd 
import dill 
from sklearn.model_selection import GridSearchCV
import pickle

from src.exception import CustomException

from sklearn.metrics import r2_score

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
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report = {}
       

        for model_name, model in models.items():  # ✅ Get model name and object
            print(f"Starting model traing for --> {model}")
            param=params[model_name]

            gs = GridSearchCV(model,param,cv=3,n_jobs=1)
            gs.fit(X_train,y_train)
            
            best_params = gs.best_params_
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            ### model.fit(X_train, y_train) 

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            model_train_score = r2_score(y_train, y_train_pred)
            model_test_score = r2_score(y_test, y_test_pred)

            report[model_name] = {  # ✅ Use model_name instead of model
                f"train_score": model_train_score,
                f"test_score": model_test_score,
                f"best_params": best_params
            }

        return report

 
    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj) 
            return obj
    except Exception as e: 
        raise CustomException(e,sys)
