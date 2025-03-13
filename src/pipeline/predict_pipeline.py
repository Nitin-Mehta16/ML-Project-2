import sys
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
         pass
    
    def predict(self,user_data):
        try:
            logging.info("Locating model and preprocess")
            model_path = r"C:\Users\nitin\DS&ML\31. Ml Project\artifact\trained_model.pkl"
            preprocess_path = r"C:\Users\nitin\DS&ML\31. Ml Project\artifact\preprocessor.pkl"  # handle categorical and numerical data
            logging.info("Loading Model and preprocess")
            model=load_object(file_path=model_path)
            preprocess=load_object(file_path=preprocess_path)
            logging.info("Transforming user data")
            data_transform=preprocess.transform(user_data)
            logging.info("Predicting user data")
            prediction= model.predict(data_transform)
            logging.info("Prediction completed")
            return prediction
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData():
    def __init__(self,gender: str,
            race_ethnicity: int,
            parental_level_of_education: str,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int):   

            logging.info("Creating custom data object")
            self.gender = gender

            self.race_ethnicity = race_ethnicity

            self.parental_level_of_education = parental_level_of_education

            self.lunch = lunch

            self.test_preparation_course = test_preparation_course

            self.reading_score = reading_score

            self.writing_score = writing_score

    def convert_data_as_data_frame(self):
        try:
            logging.info("Converting user data to dataframe")
            custom_data_input_dict = {
            "gender": [self.gender],
            "race_ethnicity": [self.race_ethnicity],
            "parental_level_of_education": [self.parental_level_of_education],
            "lunch": [self.lunch],
            "test_preparation_course": [self.test_preparation_course],
            "reading_score": [self.reading_score],
            "writing_score": [self.writing_score],
            }
            data = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe created")
            return data
    
        except Exception as e:
            raise CustomException(e,sys)

              
         